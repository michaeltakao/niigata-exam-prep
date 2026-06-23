#!/usr/bin/env python3
"""新潟大学 編入試験対策 status reporter.

Read-only: never writes to any markdown file.
Stdlib only — no pip dependencies.
Run from the repo root or via ``make status``.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).parent.parent

# ── Constants ──────────────────────────────────────────────────────────────

TIER1_TOPICS: frozenset[str] = frozenset({"L04", "L05", "L06", "L07"})

# Confirmed remediation files; checked for existence at runtime.
REMEDIATION_FILES: dict[str, str] = {
    "L04": "loops.md",
    "L05": "arrays.md",
    "L06": "functions.md",
    "L07": "pointers.md",
}

BAR_WIDTH = 10
BAR_FULL = "█"
BAR_EMPTY = "░"


# ── Data types ─────────────────────────────────────────────────────────────

@dataclass
class TopicMastery:
    code: str            # e.g. "L04"
    name: str            # e.g. "Loops"
    tier: str            # "1★" or "2"
    mastery: Optional[float]   # 0–100 or None if all cells blank
    target: Optional[float]    # target % from table


@dataclass
class ScoreData:
    baseline: Optional[float] = None
    current: Optional[float] = None


@dataclass
class CompletionData:
    chapters_read: int = 0
    chapters_total: int = 11
    drills_passed: int = 0
    drills_total: int = 8


# ── Parsing helpers ────────────────────────────────────────────────────────

def _parse_pct(raw: str) -> Optional[float]:
    """Parse a mastery cell such as '75%↑' or '65%' into a float.

    Parameters
    ----------
    raw : str
        Cell content from a markdown table, possibly with trend suffix.

    Returns
    -------
    Optional[float]
        Percentage value (0–100), or None for blank/dash cells.
    """
    s = raw.strip()
    if not s or s in ("-", "—", "___", "N/A", "n/a"):
        return None
    s = re.sub(r"[↑→↓]+$", "", s).strip()
    s = s.rstrip("%").strip()
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def _split_row(line: str) -> list[str]:
    """Split a markdown table row into stripped cell strings."""
    cells = [c.strip() for c in line.strip().split("|")]
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1] == "":
        cells = cells[:-1]
    return cells


def _is_separator(cells: list[str]) -> bool:
    """Return True if every cell is composed only of dashes and colons."""
    return bool(cells) and all(
        c.replace("-", "").replace(":", "").strip() == "" for c in cells
    )


def _table_rows(text: str, header_hint: str) -> list[list[str]]:
    """Extract data rows from the first markdown table following *header_hint*.

    The search is case-insensitive on the section header line.

    Parameters
    ----------
    text : str
        Full file content.
    header_hint : str
        Substring to locate the section header (e.g. "Mastery % Tracker").

    Returns
    -------
    list[list[str]]
        Each element is a list of stripped cell strings for one data row.
        Empty list if the table cannot be found or has no data rows.
    """
    lines = text.splitlines()
    in_table = False
    past_separator = False
    rows: list[list[str]] = []

    for line in lines:
        if header_hint.lower() in line.lower():
            in_table = True
            past_separator = False
            rows = []
            continue

        if not in_table:
            continue

        stripped = line.strip()
        if stripped.startswith("|"):
            cells = _split_row(stripped)
            if _is_separator(cells):
                past_separator = True
            elif past_separator:
                rows.append(cells)
        elif rows:
            # First non-pipe line after we have data → table is over.
            break

    return rows


# ── Parsers ────────────────────────────────────────────────────────────────

def parse_mastery(path: Path) -> list[TopicMastery]:
    """Parse the Mastery % Tracker table from *success-metrics.md*.

    Reads the most recent non-blank week column per topic (checks
    Final % → Week 4 → Week 3 → Week 2 → Week 1 in that order).

    Parameters
    ----------
    path : Path
        Path to success-metrics.md.

    Returns
    -------
    list[TopicMastery]
        One entry per topic row found in the table; empty on failure.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"  [WARN] {path.name} not found — skipping mastery section",
              file=sys.stderr)
        return []

    rows = _table_rows(text, "Mastery % Tracker")
    if not rows:
        print(f"  [WARN] Mastery % Tracker table not found in {path.name}",
              file=sys.stderr)
        return []

    # Column layout (0-based after border removal):
    # 0=Topic  1=Tier  2=Week1%  3=Week2%  4=Week3%  5=Week4%  6=Final%
    # 7=Target%  8=Met?
    WEEK_COLS = [6, 5, 4, 3, 2]  # priority: Final %, then Week 4 → 1
    TARGET_COL = 7

    topics: list[TopicMastery] = []
    for row in rows:
        if len(row) < 2:
            continue
        topic_cell = row[0]
        tier_cell = row[1]

        mastery: Optional[float] = None
        for col in WEEK_COLS:
            if col < len(row):
                val = _parse_pct(row[col])
                if val is not None:
                    mastery = val
                    break

        target: Optional[float] = None
        if TARGET_COL < len(row):
            target = _parse_pct(row[TARGET_COL])

        m = re.match(r"(L\d+)\s*(.*)", topic_cell)
        if not m:
            continue
        code = m.group(1)
        name = m.group(2).strip()

        topics.append(TopicMastery(
            code=code,
            name=name,
            tier=tier_cell.strip(),
            mastery=mastery,
            target=target,
        ))

    return topics


def parse_scores(score_path: Path, baseline_path: Path) -> ScoreData:
    """Parse baseline and latest assessment scores.

    Primary source: Score Log table in *score-tracking.md*.
    Fallback for baseline: ``baseline-assessment.md`` working-estimate line.

    Parameters
    ----------
    score_path : Path
        Path to score-tracking.md.
    baseline_path : Path
        Path to baseline-assessment.md.

    Returns
    -------
    ScoreData
        .baseline = Day-0 score (or None), .current = latest score (or None).
    """
    data = ScoreData()

    try:
        text = score_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"  [WARN] {score_path.name} not found — skipping score section",
              file=sys.stderr)
        return data

    # Column layout: 0=Date  1=Assessment  2=Score(/100)  3=Δ  4=PassThreshold  5=Notes
    rows = _table_rows(text, "Score Log")
    baseline_score: Optional[float] = None
    latest_score: Optional[float] = None

    for row in rows:
        if len(row) < 3:
            continue
        assessment = row[1].strip()
        raw_score = row[2].strip()

        score_val: Optional[float] = None
        if raw_score and raw_score not in ("-", "—", ""):
            try:
                score_val = float(raw_score)
            except ValueError:
                pass

        if "Diagnostic" in assessment and "Day 0" in assessment:
            if score_val is not None:
                baseline_score = score_val
        elif score_val is not None:
            latest_score = score_val  # last non-blank row wins

    data.baseline = baseline_score

    if latest_score is not None:
        data.current = latest_score
    elif baseline_score is not None:
        data.current = baseline_score  # only baseline known so far

    # Fallback: try baseline-assessment.md for the Day-0 anchor.
    if data.baseline is None:
        try:
            ba = baseline_path.read_text(encoding="utf-8")
            m = re.search(
                r"Day\s*0\s*baseline[^\n]*?(\d+(?:\.\d+)?)\s*/\s*100", ba
            )
            if m:
                data.baseline = float(m.group(1))
                if data.current is None:
                    data.current = data.baseline
        except FileNotFoundError:
            pass

    return data


def parse_completion(path: Path) -> CompletionData:
    """Count completed checkboxes in the Module Completion Checklist.

    Counts ``[x]`` in:
    - "First Read" column of the Textbook Chapters table (→ chapters_read)
    - "Passed (≥70%)" column of the Drill Sets table (→ drills_passed)

    Parameters
    ----------
    path : Path
        Path to 06_progress/student-progress.md.

    Returns
    -------
    CompletionData
        chapter and drill completion counts.
    """
    data = CompletionData()

    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"  [WARN] {path.name} not found — skipping completion section",
              file=sys.stderr)
        return data

    lines = text.splitlines()

    in_chapter = False
    in_drill = False
    past_ch_sep = False
    past_dr_sep = False
    chapters_read = 0
    drills_passed = 0

    for line in lines:
        stripped = line.strip()

        # Section detection (order matters: more specific first).
        if "Textbook Chapters" in line:
            in_chapter = True
            in_drill = False
            past_ch_sep = False
            continue
        if "Drill Sets" in line:
            in_chapter = False
            in_drill = True
            past_dr_sep = False
            continue
        if "Mock Exams" in line:
            in_chapter = False
            in_drill = False
            continue

        if not stripped.startswith("|"):
            continue

        cells = _split_row(stripped)

        if in_chapter:
            if _is_separator(cells):
                past_ch_sep = True
            elif past_ch_sep and len(cells) >= 3:
                # Column layout: 0=#  1=Chapter  2=First Read  3=Drill Done  4=Review Done
                first_read = cells[2] if len(cells) > 2 else ""
                if "[x]" in first_read.lower():
                    chapters_read += 1

        elif in_drill:
            if _is_separator(cells):
                past_dr_sep = True
            elif past_dr_sep and len(cells) >= 5:
                # Column layout: 0=Drill  1=Topic  2=Attempted  3=Score  4=Passed(≥70%)
                passed = cells[4] if len(cells) > 4 else ""
                if "[x]" in passed.lower():
                    drills_passed += 1

    data.chapters_read = chapters_read
    data.drills_passed = drills_passed
    return data


# ── Computations ───────────────────────────────────────────────────────────

def compute_predicted(
    topics: list[TopicMastery],
) -> tuple[Optional[float], Optional[float], Optional[float]]:
    """Compute predicted exam score from mastery averages.

    Formula: ``predicted = (tier1_avg × 0.6) + (tier2_avg × 0.4)``
    Excludes topics whose mastery is None.

    Parameters
    ----------
    topics : list[TopicMastery]
        All topics from the mastery table.

    Returns
    -------
    tuple[Optional[float], Optional[float], Optional[float]]
        (tier1_avg, tier2_avg, predicted).  Any element may be None if
        insufficient data.
    """
    tier1_vals = [
        t.mastery for t in topics
        if t.code in TIER1_TOPICS and t.mastery is not None
    ]
    tier2_vals = [
        t.mastery for t in topics
        if t.code not in TIER1_TOPICS and t.mastery is not None
    ]

    t1_avg: Optional[float] = sum(tier1_vals) / len(tier1_vals) if tier1_vals else None
    t2_avg: Optional[float] = sum(tier2_vals) / len(tier2_vals) if tier2_vals else None

    if t1_avg is not None and t2_avg is not None:
        predicted: Optional[float] = (t1_avg * 0.6) + (t2_avg * 0.4)
    elif t1_avg is not None:
        predicted = t1_avg * 0.6
    elif t2_avg is not None:
        predicted = t2_avg * 0.4
    else:
        predicted = None

    return t1_avg, t2_avg, predicted


# ── Rendering helpers ──────────────────────────────────────────────────────

def _bar(pct: float) -> str:
    filled = min(BAR_WIDTH, max(0, round(pct / 100 * BAR_WIDTH)))
    return BAR_FULL * filled + BAR_EMPTY * (BAR_WIDTH - filled)


def _fmt_pct(v: Optional[float]) -> str:
    return f"{v:.0f}%" if v is not None else "--"


def _fmt_score(v: Optional[float]) -> str:
    return f"{v:.0f}" if v is not None else "--"


def _yn(b: Optional[bool]) -> str:
    if b is None:
        return "--"
    return "YES" if b else "NO "


def _verdict(score_ok: Optional[bool], mastery_ok: Optional[bool]) -> str:
    if score_ok is None or mastery_ok is None:
        return "NOT YET"
    if score_ok and mastery_ok:
        return "PASS"
    if score_ok or mastery_ok:
        return "PARTIAL"
    return "FAIL"


# ── Report renderer ────────────────────────────────────────────────────────

def render(
    topics: list[TopicMastery],
    scores: ScoreData,
    t1_avg: Optional[float],
    t2_avg: Optional[float],
    predicted: Optional[float],
    completion: CompletionData,
) -> None:
    """Print the full status report to stdout."""
    today = date.today().isoformat()
    SEP = "═" * 46

    print(SEP)
    print(f"  新潟大学 編入試験対策 STATUS  {today}")
    print(SEP)

    # ── SCORE ─────────────────────────────────────────────────────────────
    print()
    print("[SCORE]")
    baseline = scores.baseline
    current = scores.current

    delta_str = "--"
    if baseline is not None and current is not None:
        delta = current - baseline
        sign = "+" if delta >= 0 else ""
        delta_str = f"{sign}{delta:.0f}"

    print(f"  Baseline (Day 0) : {_fmt_score(baseline):>3} / 100")
    print(f"  Latest           : {_fmt_score(current):>3} / 100   Δ = {delta_str}")

    # ── PREDICTED SCORE ───────────────────────────────────────────────────
    print()
    print("[PREDICTED SCORE]")
    print(f"  Tier-1★ avg  : {_fmt_pct(t1_avg):>4}")
    print(f"  Tier-2  avg  : {_fmt_pct(t2_avg):>4}")
    if predicted is not None:
        print(f"  Predicted    : {predicted:.0f} / 100")
    else:
        print("  Predicted    : -- / 100")
        print("  (Fill success-metrics.md after your first study session.)")

    # ── MASTERY ───────────────────────────────────────────────────────────
    print()
    print("[MASTERY]")
    if not topics:
        print("  (No mastery data — fill success-metrics.md.)")
    else:
        for t in topics:
            star = "★" if t.code in TIER1_TOPICS else " "
            pct_str = _fmt_pct(t.mastery)
            tgt_str = _fmt_pct(t.target)
            bar_str = _bar(t.mastery) if t.mastery is not None else BAR_EMPTY * BAR_WIDTH
            flag = ""
            if t.mastery is not None and t.target is not None and t.mastery < t.target:
                flag = "  ← below"
            label = f"{t.code} {t.name}"
            print(
                f"  {label:<16} {bar_str}  {pct_str:>4}  {star}  "
                f"target {tgt_str}{flag}"
            )

    # ── MILESTONE ─────────────────────────────────────────────────────────
    print()
    print("[MILESTONE]")

    tier1_topics = [t for t in topics if t.code in TIER1_TOPICS]

    def _d7_score() -> Optional[bool]:
        if scores.baseline is None or scores.current is None:
            return None
        return scores.current >= scores.baseline + 15

    def _d7_mastery() -> Optional[bool]:
        vals = [t.mastery for t in tier1_topics]
        if not vals or any(v is None for v in vals):
            return None
        return all(v >= 50 for v in vals)  # type: ignore[operator]

    def _d14_score() -> Optional[bool]:
        if scores.current is None:
            return None
        return scores.current >= 60

    def _d14_mastery() -> Optional[bool]:
        vals = [t.mastery for t in tier1_topics]
        if not vals or any(v is None for v in vals):
            return None
        return all(v >= 75 for v in vals)  # type: ignore[operator]

    def _d30_score() -> Optional[bool]:
        if scores.current is None:
            return None
        return scores.current >= 75

    def _d30_mastery() -> Optional[bool]:
        vals = [t.mastery for t in topics]
        if not vals or any(v is None for v in vals):
            return None
        return all(v >= 75 for v in vals)  # type: ignore[operator]

    s7, m7 = _d7_score(), _d7_mastery()
    s14, m14 = _d14_score(), _d14_mastery()
    s30, m30 = _d30_score(), _d30_mastery()

    print(
        f"  Day  7  score≥baseline+15? {_yn(s7)}  "
        f"Tier-1★≥50%? {_yn(m7)}  → {_verdict(s7, m7)}"
    )
    print(
        f"  Day 14  score≥60?          {_yn(s14)}  "
        f"Tier-1★≥75%? {_yn(m14)}  → {_verdict(s14, m14)}"
    )
    print(
        f"  Day 30  score≥75?          {_yn(s30)}  "
        f"all≥75%?     {_yn(m30)}  → {_verdict(s30, m30)}"
    )

    # ── PRIORITY TOPICS ───────────────────────────────────────────────────
    print()
    print("[PRIORITY TOPICS]  (study these next)")

    all_none = all(t.mastery is None for t in topics)
    if not topics or all_none:
        print("  (Fill success-metrics.md after your first study session.)")
    else:
        def _sort_key(t: TopicMastery) -> tuple[float, int]:
            m = t.mastery if t.mastery is not None else -1.0
            tier_rank = 0 if t.code in TIER1_TOPICS else 1
            return (m, tier_rank)

        sorted_topics = sorted(topics, key=_sort_key)
        remed_dir = ROOT / "10_remediation"

        for rank, t in enumerate(sorted_topics[:3], start=1):
            star = "★" if t.code in TIER1_TOPICS else " "
            pct_str = _fmt_pct(t.mastery)
            tgt = t.target if t.target is not None else 75.0
            current_m = t.mastery if t.mastery is not None else 0.0
            gap = tgt - current_m
            gap_str = f"needs +{gap:.0f} pts to target" if gap > 0 else "target reached"

            remed = ""
            remed_file = REMEDIATION_FILES.get(t.code)
            if remed_file and (remed_dir / remed_file).exists():
                remed = f"  → 10_remediation/{remed_file}"

            label = f"{t.code} {t.name}"
            print(
                f"  {rank}. {label:<18} {pct_str:>4}  {star}  {gap_str}{remed}"
            )

    # ── COMPLETION ────────────────────────────────────────────────────────
    print()
    print("[COMPLETION]")
    print(f"  Modules:  {completion.chapters_read} / {completion.chapters_total} chapters read")
    print(f"  Drills:   {completion.drills_passed} / {completion.drills_total} drill sets passed")

    print(SEP)


# ── Entry point ────────────────────────────────────────────────────────────

def main() -> None:
    """Load all tracking files and print the status report."""
    topics = parse_mastery(ROOT / "success-metrics.md")
    scores = parse_scores(
        ROOT / "score-tracking.md",
        ROOT / "baseline-assessment.md",
    )
    t1_avg, t2_avg, predicted = compute_predicted(topics)
    completion = parse_completion(ROOT / "06_progress" / "student-progress.md")

    render(topics, scores, t1_avg, t2_avg, predicted, completion)


if __name__ == "__main__":
    main()
