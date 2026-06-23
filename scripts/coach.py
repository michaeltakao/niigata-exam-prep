"""Adaptive daily study coach for C-language exam prep (v2).

New in v2: confidence tracking, mastery-state.json persistence,
pattern detection (frustration / stagnation / overload), single-action
generator, and daily-coaching-report.md output.

Backward compatible: mastery-state.json created fresh if absent.
Schedule source: exam-priority-ranking.md 13-day plan (2026-06-22).
Mastery thresholds: score-prediction.md §3.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SCORE_TRACKING = PROJECT_ROOT / "score-tracking.md"
SESSION_LOG = PROJECT_ROOT / "06_progress" / "session-log.md"
MASTERY_STATE_PATH = PROJECT_ROOT / "06_progress" / "mastery-state.json"
COACHING_REPORT_PATH = PROJECT_ROOT / "06_progress" / "daily-coaching-report.md"

# ---------------------------------------------------------------------------
# 13-day optimized schedule (from exam-priority-ranking.md — hardcoded)
# ---------------------------------------------------------------------------
SCHEDULE: dict[int, dict] = {
    1: {
        "topics": ["L01 変数・型・printf/scanf", "L02 演算子・式"],
        "drill": "L1 Q1–5 + L2 Q1–3",
        "goal": "L1 ≥60%（3/5問）、L2 ≥60%",
        "level": "L01",
    },
    2: {
        "topics": ["L03 条件分岐（if/else/switch）"],
        "drill": "L3 Q1–5",
        "goal": "L3 ドリル ≥60%",
        "level": "L03",
    },
    3: {
        "topics": ["L03 追加演習", "L04 ループ入門"],
        "drill": "L4 Easy Q1–3",
        "goal": "L4 Easy ≥2/3問正解",
        "level": "L04",
    },
    4: {
        "topics": ["L04 ネストループ集中"],
        "drill": "L4 M4–M6（ネストループトレース）",
        "goal": "ネスト変数変化を表で追える",
        "level": "L04",
    },
    5: {
        "topics": ["L04 バグ修正 + Medium演習"],
        "drill": "L4 Easy 全問 + R8問1 過去問",
        "goal": "L4 Medium ≥5/10",
        "level": "L04",
    },
    6: {
        "topics": ["L04 タイムアタック + 定着確認"],
        "drill": "L4 全問タイムアタック",
        "goal": "L4 総合 ≥70%",
        "level": "L04",
    },
    7: {
        "topics": ["L05 配列 Easy"],
        "drill": "L5 Easy Q1–4",
        "goal": "配列初期化・アクセス完全",
        "level": "L05",
    },
    8: {
        "topics": ["L05 バブルソート集中"],
        "drill": "L5 H1 + Mock A II-2",
        "goal": "バブルソート穴埋め ≥2/3",
        "level": "L05",
    },
    9: {
        "topics": ["L05 探索 + 最大最小"],
        "drill": "L5 M4–M6 + R8問2",
        "goal": "L5 Medium ≥5/10",
        "level": "L05",
    },
    10: {
        "topics": ["L06 関数（定義・呼び出し・戻り値）"],
        "drill": "L6 Easy Q1–6",
        "goal": "L6 Easy ≥5/6（int max 白紙で書ける）",
        "level": "L06",
    },
    11: {
        "topics": ["L06 再帰（fact/fib トレースのみ）"],
        "drill": "L6 M4–M6（再帰トレース）",
        "goal": "fact(4) / fib(5) トレース完璧",
        "level": "L06",
    },
    12: {
        "topics": ["Mock A 大問I + II（60分時間制限）"],
        "drill": "05_mock-exams/mock-exam-A.md → scripts/analyze_mock.py で採点",
        "goal": "大問I + II で ≥35/70（50%以上）",
        "level": "Mock",
    },
    13: {
        "topics": ["Mock A ギャップ補強", "L07 Easy（時間があれば）"],
        "drill": "Mock A 誤答再解 + L7 E1–E3",
        "goal": "弱点問題再解 ≥70%",
        "level": "L07",
    },
}

# ---------------------------------------------------------------------------
# Mastery state data model
# ---------------------------------------------------------------------------
@dataclass
class TopicRecord:
    sessions: list[dict] = field(default_factory=list)
    current_level: str = "未学習"
    consecutive_same_level: int = 0


@dataclass
class MasteryState:
    baseline_date: str = ""
    topics: dict[str, TopicRecord] = field(default_factory=dict)


def load_mastery_state() -> MasteryState:
    if not MASTERY_STATE_PATH.exists():
        return MasteryState()
    try:
        raw = json.loads(MASTERY_STATE_PATH.read_text(encoding="utf-8"))
        state = MasteryState(baseline_date=raw.get("baseline_date", ""))
        for topic, tdata in raw.get("topics", {}).items():
            state.topics[topic] = TopicRecord(
                sessions=tdata.get("sessions", []),
                current_level=tdata.get("current_level", "未学習"),
                consecutive_same_level=tdata.get("consecutive_same_level", 0),
            )
        return state
    except Exception as e:
        print(f"[警告] mastery-state.json の読み込みに失敗しました: {e}")
        print("  空の状態から開始します。")
        return MasteryState()


def save_mastery_state(state: MasteryState) -> None:
    MASTERY_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    data: dict = {
        "baseline_date": state.baseline_date,
        "topics": {
            topic: {
                "sessions": rec.sessions,
                "current_level": rec.current_level,
                "consecutive_same_level": rec.consecutive_same_level,
            }
            for topic, rec in state.topics.items()
        },
    }
    MASTERY_STATE_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# Mastery estimation
# ---------------------------------------------------------------------------
def _mastery_label_from_score(score: int, total: int = 10) -> str:
    pct = score / total if total > 0 else 0.0
    if pct >= 0.70:
        return "Strong"
    elif pct >= 0.40:
        return "Developing"
    return "Weak"


def _mastery_label_from_confidence(confidence: int) -> str:
    if confidence >= 4:
        return "Strong"
    elif confidence >= 3:
        return "Developing"
    return "Weak"


def _mastery_display(level: str) -> str:
    return {"Strong": "Strong ✅", "Developing": "Developing △", "Weak": "Weak ❌"}.get(
        level, level
    )


# ---------------------------------------------------------------------------
# Pattern detection
# ---------------------------------------------------------------------------
def detect_frustration(topic: str, state: MasteryState) -> str | None:
    """Trigger: confidence ≤ 2 for ≥2 consecutive sessions on same topic."""
    rec = state.topics.get(topic)
    if rec is None or len(rec.sessions) < 2:
        return None
    recent = rec.sessions[-2:]
    if all(s.get("confidence", 5) <= 2 for s in recent):
        return (
            f"[フラストレーション検出] {topic} で2セッション連続で自信度が低いです。"
            " 今日は10分休んでから、Easy ドリル1問だけ再挑戦してください。"
        )
    return None


def detect_stagnation(topic: str, state: MasteryState) -> str | None:
    """Trigger: consecutive_same_level ≥ 3 AND level != Strong."""
    rec = state.topics.get(topic)
    if rec is None:
        return None
    if rec.consecutive_same_level >= 3 and rec.current_level != "Strong":
        return (
            f"[停滞検出] {topic} が {rec.consecutive_same_level} セッション"
            f" {_mastery_display(rec.current_level)} のまま。"
            " アプローチを変えます → 教科書を再読してからドリルの Easy を最初から解き直してください。"
        )
    return None


def detect_overload(minutes: int) -> str | None:
    """Trigger: study time > 120 minutes."""
    if minutes > 120:
        return (
            f"[過負荷検出] 今日は長すぎます（{minutes}分）。"
            " 明日は60分以内に絞り、1トピックだけに集中してください。"
        )
    return None


# ---------------------------------------------------------------------------
# Single next action generator
# ---------------------------------------------------------------------------
def generate_single_action(
    topic_key: str,
    mastery_level: str,
    patterns: list[str],
    day: int,
    weak_problems: list[str],
) -> str:
    # 1. If pattern detected → pattern-specific action
    if patterns:
        first = patterns[0]
        if "フラストレーション" in first:
            return f"{topic_key} Easy ドリルを1問だけ解く（10分休憩後）"
        if "停滞" in first:
            return f"教科書 {topic_key} 節を再読 → Easy ドリル Q1 を白紙で解く"
        if "過負荷" in first:
            return "明日の学習時間を60分以内に制限し、最優先トピック1つだけ解く"

    # 2. Based on mastery level
    if mastery_level == "Weak":
        return f"{topic_key} Easy ドリルをもう1周（教科書見ながらでOK）"
    if mastery_level == "Developing":
        if weak_problems:
            probs = ", ".join(weak_problems[:3])
            return f"{topic_key} の間違えた問題（{probs}）を解き直す（各問5分以内）"
        return f"{topic_key} Medium ドリルを3問解く（各問5分以内）"

    # Strong → suggest next day's topic
    next_day = day + 1
    next_sched = SCHEDULE.get(next_day)
    if next_sched:
        next_topic = next_sched["topics"][0]
        return f"今日は Strong 達成！明日の予習: {next_topic} 教科書を10分読む"
    return "全スケジュール完了！Mock B を解いてください（05_mock-exams/mock-exam-B.md）"


# ---------------------------------------------------------------------------
# Rules (R01–R12 from score-prediction.md, crisis-mode relevant)
# ---------------------------------------------------------------------------
def _apply_rules(topic_lower: str, score: int | None, days_remaining: int) -> list[str]:
    advice: list[str] = []
    if days_remaining <= 7:
        if "l07" in topic_lower or "pointer" in topic_lower or "ポインタ" in topic_lower:
            if score is not None and score < 7:
                advice.append(
                    "[R01] ポインタは Easy のみ。*p と p の違いを暗記カード化。実装は捨ててトレースに集中。"
                )
        if "l04" in topic_lower or "loop" in topic_lower or "ループ" in topic_lower:
            if score is not None and score < 7:
                advice.append(
                    "[R02] ループが弱い → L4 Easy 全問を2周目。毎問トレース表を紙に書くこと。"
                )
    if days_remaining <= 3:
        advice.append(
            "[R12] 試験3日前: 「確実に取れる問題」戦略へ切り替え。"
            " トレース問題（推定30点分）に全時間を投入。"
        )
    return advice


# ---------------------------------------------------------------------------
# Baseline date reader
# ---------------------------------------------------------------------------
def _read_baseline_date() -> date:
    if not SCORE_TRACKING.exists():
        print(f"[警告] {SCORE_TRACKING} が見つかりません。今日を Day 1 として起動します。")
        return date.today()
    text = SCORE_TRACKING.read_text(encoding="utf-8")
    match = re.search(r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*Diagnostic", text)
    if match:
        return date.fromisoformat(match.group(1))
    print("[警告] score-tracking.md に診断日付が見つかりません。今日を Day 0 として計算します。")
    return date.today()


# ---------------------------------------------------------------------------
# Interactive prompts
# ---------------------------------------------------------------------------
def _prompt(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    try:
        val = input(f"  {label}{suffix}: ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)
    return val if val else default


def _prompt_int(label: str) -> int | None:
    raw = _prompt(label)
    if not raw:
        return None
    try:
        return int(raw)
    except ValueError:
        return None


def _prompt_confidence() -> int:
    while True:
        raw = _prompt("5. 自信度 (1=全くわからない, 3=なんとなく, 5=完璧)")
        if not raw:
            return 3  # default neutral
        try:
            val = int(raw)
            if 1 <= val <= 5:
                return val
        except ValueError:
            pass
        print("  1〜5 の整数を入力してください。")


# ---------------------------------------------------------------------------
# Coaching report writer
# ---------------------------------------------------------------------------
def _write_coaching_report(
    day: int,
    studied: str,
    minutes: int,
    drill_score: int | None,
    drill_total: int,
    confidence: int,
    weak_problems: list[str],
    mastery_level: str,
    prev_level: str,
    topic_key: str,
    patterns: list[str],
    next_action: str,
) -> None:
    COACHING_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    today_str = date.today().isoformat()

    score_str = f"{drill_score}/{drill_total}" if drill_score is not None else "記録なし"
    level_disp = _mastery_display(mastery_level)

    # Mastery change row
    prev_disp = _mastery_display(prev_level) if prev_level else "未学習"
    change = "→" if prev_level == mastery_level else ("↑" if mastery_level == "Strong" else "↕")

    pattern_text = "\n".join(f"- {p}" for p in patterns) if patterns else "なし"
    weak_text = ", ".join(weak_problems) if weak_problems else "なし"

    next_day = day + 1
    next_sched = SCHEDULE.get(next_day)
    next_day_text = (
        f"Day {next_day}: {' / '.join(next_sched['topics'])}"
        if next_sched
        else "スケジュール完了 → Mock B 挑戦"
    )

    report = f"""# デイリーコーチングレポート — {today_str} (Day {day})

## セッションサマリー
- 学習内容: {studied} / {minutes}分 / スコア: {score_str} ({level_disp})
- 自信度: {confidence}/5
- 難しかった問題: {weak_text}

## 習熟度更新
| トピック | 前回 | 今回 | 変化 |
|---|---|---|---|
| {topic_key} | {prev_disp} | {level_disp} | {change} |

## 検出パターン
{pattern_text}

## 次の1アクション
**{next_action}**

## 翌日スケジュール
{next_day_text}
"""
    COACHING_REPORT_PATH.write_text(report, encoding="utf-8")


# ---------------------------------------------------------------------------
# Session log writer
# ---------------------------------------------------------------------------
def _append_session_log(entry: str) -> None:
    SESSION_LOG.parent.mkdir(parents=True, exist_ok=True)
    with SESSION_LOG.open("a", encoding="utf-8") as f:
        f.write(entry)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    baseline = _read_baseline_date()
    today = date.today()
    days_elapsed = (today - baseline).days
    current_day = days_elapsed
    days_remaining = 13 - current_day

    # Load mastery state
    state = load_mastery_state()
    if not state.baseline_date:
        state.baseline_date = baseline.isoformat()

    print()
    print("=" * 60)
    print("  C言語 アダプティブコーチ — 13日最適化モード")
    print("=" * 60)

    if current_day > 13:
        print("\n✅ 13日プラン完了！Mock B/C に進んでください。")
        print("   (`exam-priority-ranking.md` のスキップ基準も参照)")
        return

    sched = SCHEDULE.get(current_day)
    if sched is None:
        print(f"\n本日は Day 0（診断日 {baseline} 基準）。")
        print(
            "明日からDay 1スタート。`exam-priority-ranking.md` と"
            " `high-yield-topics.md` を読んでください。"
        )
        return

    topics_str = " / ".join(sched["topics"])
    topic_key = sched.get("level", "L??")

    print(f"\n本日: Day {current_day} / 13  (残り {days_remaining} 日)")
    print(f"今日のスケジュール: {topics_str}")
    print(f"ドリル目標: {sched['drill']}")
    print(f"通過基準: {sched['goal']}")
    print()

    # --- Prompts ---
    print("--- セッション記録 ---")
    studied = _prompt("1. 今日勉強した内容（トピック名 or 'done'）", topics_str)
    minutes_raw = _prompt_int("2. 学習時間（分）")
    minutes = minutes_raw if minutes_raw is not None else 0

    score_raw = _prompt("3. ドリルスコア（例: 7/10、Enter でスキップ）")
    drill_score: int | None = None
    drill_total: int = 10
    if score_raw:
        m = re.match(r"(\d+)\s*/\s*(\d+)", score_raw)
        if m:
            drill_score = int(m.group(1))
            drill_total = int(m.group(2))
        else:
            try:
                drill_score = int(score_raw)
            except ValueError:
                pass

    missed_raw = _prompt("4. 難しかった問題番号（カンマ区切り、Enter でスキップ）")
    weak_problems = [x.strip() for x in missed_raw.split(",") if x.strip()] if missed_raw else []

    confidence = _prompt_confidence()

    notes = _prompt("6. メモ（任意、Enter でスキップ）")

    # --- Mastery estimation ---
    if drill_score is not None:
        score_10 = round(drill_score * 10 / drill_total) if drill_total != 10 else drill_score
        mastery_level = _mastery_label_from_score(score_10)
    else:
        mastery_level = _mastery_label_from_confidence(confidence)

    # --- Update mastery state ---
    prev_level = ""
    if topic_key not in state.topics:
        state.topics[topic_key] = TopicRecord()
    rec = state.topics[topic_key]
    prev_level = rec.current_level

    session_entry = {
        "date": today.isoformat(),
        "score": drill_score,
        "out_of": drill_total if drill_score is not None else None,
        "confidence": confidence,
        "minutes": minutes,
    }
    rec.sessions.append(session_entry)

    if rec.current_level == mastery_level:
        rec.consecutive_same_level += 1
    else:
        rec.consecutive_same_level = 1
        rec.current_level = mastery_level

    save_mastery_state(state)

    # --- Pattern detection ---
    patterns: list[str] = []
    frust = detect_frustration(topic_key, state)
    if frust:
        patterns.append(frust)
    stag = detect_stagnation(topic_key, state)
    if stag:
        patterns.append(stag)
    overload = detect_overload(minutes)
    if overload:
        patterns.append(overload)

    # --- Single next action ---
    next_action = generate_single_action(
        topic_key, mastery_level, patterns, current_day, weak_problems
    )

    # --- Rules ---
    topic_lower = studied.lower()
    rules = _apply_rules(topic_lower, drill_score, days_remaining)

    # --- Display results ---
    print()
    print("--- 結果 ---")
    score_disp = f"{drill_score}/{drill_total}" if drill_score is not None else "記録なし"
    print(f"ドリル判定: {_mastery_display(mastery_level)} ({score_disp})")
    print(f"自信度: {confidence}/5")

    if patterns:
        print()
        print("[パターン検出]")
        for p in patterns:
            print(f"  {p}")

    if rules:
        print()
        print("[緊急ルール]")
        for r in rules:
            print(f"  {r}")

    print()
    print("[次の1アクション]")
    print(f"  ▶ {next_action}")

    next_day = current_day + 1
    next_sched = SCHEDULE.get(next_day)
    print()
    if next_sched:
        next_topics = " / ".join(next_sched["topics"])
        print(f"明日 (Day {next_day}): {next_topics}")
        print(f"  → 最初にやること: {next_sched['drill']}")
        print(f"  → 目標: {next_sched['goal']}")
    else:
        print("明日以降: Mock B/C 挑戦 + 試験直前チェックリスト (`exam-survival-mode.md`)")

    # --- Write coaching report ---
    _write_coaching_report(
        day=current_day,
        studied=studied,
        minutes=minutes,
        drill_score=drill_score,
        drill_total=drill_total,
        confidence=confidence,
        weak_problems=weak_problems,
        mastery_level=mastery_level,
        prev_level=prev_level,
        topic_key=topic_key,
        patterns=patterns,
        next_action=next_action,
    )

    # --- Append session log ---
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    score_line = (
        f"ドリルスコア: {score_raw} → {_mastery_display(mastery_level)}"
        if drill_score is not None
        else "ドリルスコア: 記録なし"
    )
    missed_line = f"間違えた問題: {', '.join(weak_problems)}" if weak_problems else "間違えた問題: なし"
    notes_line = f"メモ: {notes}" if notes else ""

    entry_lines = [
        f"\n## セッション — {now_str} (Day {current_day})\n",
        f"- 学習内容: {studied}\n",
        f"- 学習時間: {minutes} 分\n",
        f"- {score_line}\n",
        f"- 自信度: {confidence}/5\n",
        f"- {missed_line}\n",
        f"- 習熟度推定: {_mastery_display(mastery_level)}\n",
        f"- 次の1アクション: {next_action}\n",
    ]
    if notes_line:
        entry_lines.append(f"- {notes_line}\n")
    if next_sched:
        entry_lines.append(
            f"- 次回: Day {next_day} — {' / '.join(next_sched['topics'])}\n"
        )
    entry_lines.append("\n")

    _append_session_log("".join(entry_lines))
    print()
    print(f"✅ セッションログを {SESSION_LOG} に追記しました。")
    print(f"✅ コーチングレポートを {COACHING_REPORT_PATH} に書き込みました。")
    print()


if __name__ == "__main__":
    main()
