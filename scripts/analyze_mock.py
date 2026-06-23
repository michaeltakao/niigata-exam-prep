"""Mock exam analyzer for C-language exam prep.

Student inputs correct/incorrect per sub-problem; script outputs:
- Score by section with mastery labels
- Root causes for missed problems
- Predicted real exam score range
- 3-day remediation plan

Mock A structure hardcoded from 05_mock-exams/mock-exam-A.md (version: 2026-06-19).
If that file is re-scored, update MOCK_A below.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path
from typing import NamedTuple

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Mock exam structure (hardcoded from 05_mock-exams/mock-exam-A.md)
# Source: mock-exam-A.md — 大問I=35pt, 大問II=35pt, 大問III=30pt
# ---------------------------------------------------------------------------
class Problem(NamedTuple):
    num: str
    pts: int
    type_: str   # trace / fill / debug / rewrite / modify / read / impl
    skill: str


class Section(NamedTuple):
    id_: str
    topic: str
    total: int
    problems: list[Problem]


MOCK_A: dict = {
    "name": "Mock A",
    "sections": [
        Section(
            id_="I",
            topic="L04 ループ",
            total=35,
            problems=[
                Problem("I-1",  10, "trace",   "nested_loop_trace"),
                Problem("I-2",   9, "fill",    "loop_fill_blank"),
                Problem("I-3",   8, "debug",   "loop_bug_fix"),
                Problem("I-4",   4, "rewrite", "while_conversion"),
                Problem("I-5",   4, "modify",  "conditional_filter"),
            ],
        ),
        Section(
            id_="II",
            topic="L05 配列 + L04",
            total=35,
            problems=[
                Problem("II-1",  6,  "read",  "array_init"),
                Problem("II-2",  12, "fill",  "bubble_sort"),
                Problem("II-3",  6,  "trace", "sort_output"),
                Problem("II-4",  7,  "impl",  "linear_search"),
                Problem("II-5",  4,  "impl",  "pointer_minmax"),
            ],
        ),
        Section(
            id_="III",
            topic="L08 文字列 + L05 + L07",
            total=30,
            problems=[
                Problem("III-1", 6,  "read",  "strlen"),
                Problem("III-2", 10, "fill",  "string_reverse_fill"),
                Problem("III-3", 7,  "trace", "pointer_char_trace"),
                Problem("III-4", 7,  "impl",  "char_count"),
            ],
        ),
    ],
}

# ---------------------------------------------------------------------------
# Skill → topic → remediation mapping
# ---------------------------------------------------------------------------
SKILL_TO_REMEDIATION: dict[str, tuple[str, str | None, str]] = {
    "nested_loop_trace":    ("L04", "10_remediation/loops.md",     "L4 Medium M4–M6（ネストループトレース）"),
    "loop_fill_blank":      ("L04", "10_remediation/loops.md",     "L4 Easy 全問 + R8問1 過去問"),
    "loop_bug_fix":         ("L04", "10_remediation/loops.md",     "L4 Easy 全問 2周目"),
    "while_conversion":     ("L04", "10_remediation/loops.md",     "L4 Medium: while変換問題"),
    "conditional_filter":   ("L04", "10_remediation/loops.md",     "L4 Easy Q5–Q7（if+for複合）"),
    "array_init":           ("L05", "10_remediation/arrays.md",    "L5 Easy Q1–Q3"),
    "bubble_sort":          ("L05", "10_remediation/arrays.md",    "L5 H1（バブルソート完全習得）"),
    "sort_output":          ("L05", "10_remediation/arrays.md",    "L5 Medium Q5–Q7（トレース）"),
    "linear_search":        ("L05", "10_remediation/arrays.md",    "L5 M4–M6（探索実装）"),
    "pointer_minmax":       ("L07", "10_remediation/pointers.md",  "L7 E1–E5（ポインタ引数）"),
    "strlen":               ("L08", None,                           "02_textbook/L08 §1 再読（strlen の仕組み）"),
    "string_reverse_fill":  ("L08", None,                           "02_textbook/L08 再読 → L5 H4（逆順）"),
    "pointer_char_trace":   ("L07", "10_remediation/pointers.md",  "L7 E6–E10（ポインタ演算）"),
    "char_count":           ("L08", None,                           "02_textbook/L08 §2 + L6 Easy Q4"),
    # Mock B — L06 再帰関数 / L07 ポインタ / L06 関数設計 (source: mock-exam-B.md 2026-06-22)
    "fib_recursive_trace":       ("L06", "10_remediation/functions.md", "L6 M6（fib 木展開）"),
    "factorial_fill":            ("L06", "10_remediation/functions.md", "L6 M4（factorial 穴埋め）"),
    "factorial_tail_recursion":  ("L06", None,                          "02_textbook/L06 末尾再帰節 再読"),
    "fib_iterative":             ("L06", "10_remediation/functions.md", "L6 M7（反復版フィボナッチ）"),
    "pointer_array_trace":       ("L07", "10_remediation/pointers.md",  "L7 E6–E10（配列+ポインタ複合）"),
    "pointer_memory_diagram":    ("L07", "10_remediation/pointers.md",  "L7 E1–E3（メモリ図）"),
    "swap_fill":                 ("L07", "10_remediation/pointers.md",  "L7 M4（swap 実装）"),
    "pass_by_value_explain":     ("L07", None,                          "02_textbook/L07 値渡し vs 参照渡し節"),
    "pointer_uninitialized_bug": ("L07", "10_remediation/pointers.md",  "L7 E5（初期化バグ）"),
    "function_prototype":        ("L06", "10_remediation/functions.md", "L6 E1–E3（プロトタイプ）"),
    "sum_normalize_impl":        ("L06", "10_remediation/functions.md", "L6 M9（配列関数設計）"),
    "function_main_integration": ("L06", None,                          "02_textbook/L06 §5 複数関数連携"),
    "division_by_zero_handle":   ("L06", None,                          "02_textbook/L06 §6 エラー処理"),
    # Mock C — L03 制御構造 / L05 配列 / L07 ポインタ文字列再帰 (source: mock-exam-C.md 2026-06-22)
    "fizzbuzz_trace":            ("L03", None,                          "03_drills/L3 H1–H3（複合条件トレース）"),
    "conditional_grade_fill":    ("L03", None,                          "03_drills/L3 M4–M6（穴埋め）"),
    "while_boundary_bug":        ("L04", "10_remediation/loops.md",     "L4 Easy 全問（境界値）"),
    "program_explain":           ("L03", None,                          "02_textbook/L03 §4（説明問題対策）"),
    "array_init_read":           ("L05", "10_remediation/arrays.md",    "L5 Easy Q1–Q3"),
    "bubble_sort_fill":          ("L05", "10_remediation/arrays.md",    "L5 H1（バブルソート）"),
    "sort_trace":                ("L05", "10_remediation/arrays.md",    "L5 Medium Q5–Q7"),
    "linear_search_impl":        ("L05", "10_remediation/arrays.md",    "L5 M4–M6（探索実装）"),
    "pointer_arithmetic_trace":  ("L07", "10_remediation/pointers.md",  "L7 E6–E10（ポインタ演算）"),
    "to_upper_fill":             ("L07", "10_remediation/pointers.md",  "L7 M6（文字列ポインタ）"),
    "power_iter_impl":           ("L06", "10_remediation/functions.md", "L6 M5（反復実装）"),
    "code_improvement_explain":  ("L06", None,                          "02_textbook/L06 §7（改善問題対策）"),
}

# Root-cause templates (displayed per missed skill)
ROOT_CAUSE: dict[str, str] = {
    "nested_loop_trace":    "ネストループの変数変化を紙で追えていない（トレース表を書く練習が必要）",
    "loop_fill_blank":      "ループの意図を読む力が不足（初期値・条件・増分の3点セットで考える）",
    "loop_bug_fix":         "境界値（<N vs <=N）の判断ミス",
    "while_conversion":     "for と while の等価変換パターン未習得",
    "conditional_filter":   "ループ内の if 条件の組み方が不明確",
    "array_init":           "配列の初期化記法（{} 初期化）の未確認",
    "bubble_sort":          "swap ロジック（tmp 変数経由）と内側ループ上限 (n-1-i) が不明確",
    "sort_output":          "ソート後の配列状態をトレースする練習不足",
    "linear_search":        "関数の return パターン（見つかった瞬間 return）未定着",
    "pointer_minmax":       "ポインタ引数で結果を格納するパターン (*max_val = ...) 未習得",
    "strlen":               "strlen が \\0 を数えないことを知らない",
    "string_reverse_fill":  "文字列逆順の添字計算 (n/2, n-1-i) が不明確",
    "pointer_char_trace":   "*(p+k) と p[k] の等価性、p が指す先の変化のトレース不足",
    "char_count":           "文字分類条件 ('a'<=c && c<='z') の書き方未習得",
    # Mock B — L06 再帰関数 / L07 ポインタ
    "fib_recursive_trace":        "再帰木の展開（呼び出しツリー）を紙に書く練習不足",
    "factorial_fill":             "再帰の基底ケース (n<=1 → return 1) と再帰ケースのパターン未定着",
    "factorial_tail_recursion":   "末尾再帰・アキュムレータパターン未習得",
    "fib_iterative":              "再帰を反復に変換する手順（状態変数 a,b,c の使い方）未習得",
    "pointer_array_trace":        "配列先頭ポインタの演算（*(p+k) = p[k]）と移動後の状態のトレース不足",
    "pointer_memory_diagram":     "ポインタのメモリ図（箱+矢印）の描き方未習得",
    "swap_fill":                  "tmp 変数経由の swap パターン（ポインタ版）未定着",
    "pass_by_value_explain":      "値渡し（コピー）vs 参照渡し（ポインタ）の概念が未整理",
    "pointer_uninitialized_bug":  "未初期化ポインタへの書き込みは未定義動作という知識が未定着",
    "function_prototype":         "関数プロトタイプの書式（戻り値型 関数名(引数型...)）未習得",
    "sum_normalize_impl":         "複数処理を組み合わせた関数設計（最大値探索→割り算）の手順が不明確",
    "function_main_integration":  "複数関数を連携させる main() の書き方未習得",
    "division_by_zero_handle":    "ゼロ除算の危険性と早期リターンによる対処パターン未習得",
    # Mock C — L03 制御構造 / L05 配列 / L07 ポインタ文字列再帰
    "fizzbuzz_trace":             "複合条件（&&・||）の優先順位と if/else if チェーンのトレース不足",
    "conditional_grade_fill":     "条件分岐の境界値（>=90, >=70, >=60）の読み取り力不足",
    "while_boundary_bug":         "while ループの終了条件（< vs <=）の境界値バグ検出力不足",
    "program_explain":            "プログラムの意図を日本語で説明する記述力不足",
    "array_init_read":            "配列初期化 {v1,v2,...} とインデックスアクセスの基礎確認不足",
    "bubble_sort_fill":           "バブルソートの内側ループ上限 (n-1-i) と swap の空欄が埋められない",
    "sort_trace":                 "ソート各パス後の配列状態をトレースする練習不足",
    "linear_search_impl":         "線形探索の return パターン（見つかった瞬間 return index）未定着",
    "pointer_arithmetic_trace":   "p[-k] と *(p-k) の等価性・p=a+2 基準のオフセット計算の混乱",
    "to_upper_fill":              "ASCII コード差（小文字-大文字=32）と文字判定条件の未習得",
    "power_iter_impl":            "再帰関数を反復に変換するパターン（result=1, ループで掛け算）未習得",
    "code_improvement_explain":   "コード改善案（境界値チェック・標準関数活用）を文章で説明する力不足",
}

# ROI order for 3-day plan prioritization (from high-yield-topics.md)
ROI_ORDER = ["L04", "L05", "L06", "L01", "L03", "L07", "L02", "L08"]

# R01/R02/R05 rule applications
RULES: dict[str, str] = {
    "L03": "条件分岐 弱 → 複合条件（&&/||）を穴埋めで練習。全テストケースを手で確認する。",
    "L04": "[R02] ループ弱 → L4 Easy 全問 2周目。毎問トレース表を書く。",
    "L05": "[R05] 配列 Developing → L5 Easy を先に仕上げてから Medium へ。",
    "L06": "[R03] 関数・再帰 弱 → L6 Easy 全問（プロトタイプ→実装の順）。再帰はトレース表を必ず書く。",
    "L07": "[R01] ポインタ弱 → Easy のみ。*p と p の違いを暗記カード化。実装は捨ててトレースに集中。",
    "L08": "文字列は L05 が Strong になってから取り組む（依存関係あり）。",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _mastery_label(pct: float) -> str:
    if pct >= 0.70:
        return "Strong ✅"
    elif pct >= 0.40:
        return "Developing △"
    else:
        return "Weak ❌"


def _yesno(prompt: str) -> bool:
    while True:
        try:
            ans = input(f"  {prompt} [y/n]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)
        if ans in ("y", "n"):
            return ans == "y"
        print("  'y' か 'n' を入力してください。")


def _ask_mock() -> str:
    print("\nどの模擬試験を受けましたか？ [A / B / C]: ", end="")
    try:
        choice = input().strip().upper()
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)
    return choice


# ---------------------------------------------------------------------------
# Score collection
# ---------------------------------------------------------------------------
def _collect_results(mock: dict) -> dict[str, list[Problem]]:
    """Return mapping section_id → list of missed Problems."""
    missed: dict[str, list[Problem]] = {}

    for section in mock["sections"]:
        print(f"\n=== 大問 {section.id_}（{section.topic}、{section.total}点）===")
        section_missed: list[Problem] = []
        for prob in section.problems:
            correct = _yesno(f"{prob.num}（{prob.pts}点、{prob.type_}）: 正解?")
            if not correct:
                section_missed.append(prob)
        missed[section.id_] = section_missed

    return missed


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def _analyze(mock: dict, missed_by_section: dict[str, list[Problem]]) -> None:
    total_pts = sum(s.total for s in mock["sections"])
    earned = total_pts

    section_results: list[tuple[Section, int, float]] = []
    for section in mock["sections"]:
        lost = sum(p.pts for p in missed_by_section.get(section.id_, []))
        sec_earned = section.total - lost
        earned -= lost
        pct = sec_earned / section.total
        section_results.append((section, sec_earned, pct))

    print("\n" + "=" * 60)
    print(f"  {mock['name']} 結果: {earned} / {total_pts}")
    print("=" * 60)

    # Section scores
    print("\n[セクション別スコア]")
    weak_topics: list[str] = []
    for section, sec_earned, pct in section_results:
        label = _mastery_label(pct)
        marker = "  ← 重点補強" if pct < 0.70 else ""
        print(f"  大問{section.id_} {section.topic}: {sec_earned}/{section.total} ({pct*100:.0f}%) → {label}{marker}")
        if pct < 0.70:
            # Extract base topic (e.g. "L04" from "L04 ループ")
            base = section.topic.split()[0].split("+")[0].strip()
            if base not in weak_topics:
                weak_topics.append(base)

    # Root causes
    all_missed: list[Problem] = []
    for probs in missed_by_section.values():
        all_missed.extend(probs)

    if all_missed:
        print("\n[根本原因 — 間違えた問題]")
        for prob in all_missed:
            cause = ROOT_CAUSE.get(prob.skill, "詳細分析は教科書該当節を再確認")
            remed = SKILL_TO_REMEDIATION.get(prob.skill)
            remed_str = f" → {remed[2]}" if remed else ""
            print(f"  {prob.num} ({prob.skill}): {cause}{remed_str}")

    # Predicted real exam score
    pct_total = earned / total_pts
    low_pred = max(0, round(earned * 0.85))
    high_pred = min(100, round(earned * 1.15))
    print("\n[本番スコア予測]")
    print(f"  模擬試験スコア {earned}/{total_pts} ({pct_total*100:.0f}%) に基づく推定: {low_pred}〜{high_pred}点")
    print("  (Assumption: 本番試験が Mock A と同様のトピック構成の場合)")

    # 3-day remediation plan
    print("\n[ROI順 補強プラン — 次の3日間]")
    _make_3day_plan(weak_topics, all_missed)

    # Applied rules
    applied_rules: list[str] = []
    for topic in weak_topics:
        rule = RULES.get(topic)
        if rule and rule not in applied_rules:
            applied_rules.append(rule)
    if applied_rules:
        print("\n[適用ルール (score-prediction.md §4)]")
        for rule in applied_rules:
            print(f"  {rule}")

    # Log to session log
    _write_analysis_log(mock["name"], earned, total_pts, weak_topics, all_missed)
    print("\n✅ 分析結果を 06_progress/session-log.md に追記しました。")


# ---------------------------------------------------------------------------
# 3-day plan generator
# ---------------------------------------------------------------------------
def _make_3day_plan(weak_topics: list[str], all_missed: list[Problem]) -> None:
    # Sort weak topics by ROI order
    sorted_weak = sorted(
        weak_topics,
        key=lambda t: ROI_ORDER.index(t) if t in ROI_ORDER else len(ROI_ORDER),
    )

    missed_by_skill = {p.skill: p for p in all_missed}

    for day_idx, topic in enumerate(sorted_weak[:3], start=1):
        # Find the highest-priority missed skill for this topic
        topic_skills = [
            skill for skill, (t, _, _) in SKILL_TO_REMEDIATION.items()
            if t == topic and skill in missed_by_skill
        ]
        if topic_skills:
            skill = topic_skills[0]
            _, remed_file, remed_action = SKILL_TO_REMEDIATION[skill]
            file_str = f" ({remed_file})" if remed_file else ""
            print(f"  Day {day_idx}: {topic} — {remed_action}{file_str}")
        else:
            print(f"  Day {day_idx}: {topic} — Easy ドリル全問 2周目 + 教科書該当節再読")

    if len(sorted_weak) == 0:
        print("  すべての大問で Strong (≥70%) — Mock B に進んでください！")
    elif len(sorted_weak) < 3:
        print(f"  Day {len(sorted_weak) + 1}〜3: Mock A 全問を再度解く（時間制限: 60分）")


# ---------------------------------------------------------------------------
# Write to session log
# ---------------------------------------------------------------------------
def _write_analysis_log(
    mock_name: str,
    earned: int,
    total: int,
    weak_topics: list[str],
    all_missed: list[Problem],
) -> None:
    log_path = PROJECT_ROOT / "06_progress" / "session-log.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    today_str = date.today().isoformat()
    missed_str = ", ".join(p.num for p in all_missed) if all_missed else "なし"
    weak_str = ", ".join(weak_topics) if weak_topics else "なし"

    entry = (
        f"\n## 模擬試験分析 — {today_str} ({mock_name})\n"
        f"- スコア: {earned} / {total}\n"
        f"- 間違えた問題: {missed_str}\n"
        f"- 弱点トピック: {weak_str}\n"
        f"- 補強優先度 (ROI順): {weak_str}\n\n"
    )

    with log_path.open("a", encoding="utf-8") as f:
        f.write(entry)


# ---------------------------------------------------------------------------
# Mock B (hardcoded from 05_mock-exams/mock-exam-B.md — version: 2026-06-22)
# 大問I=35pt (再帰関数), 大問II=35pt (ポインタ), 大問III=30pt (関数設計)
# ---------------------------------------------------------------------------
MOCK_B: dict = {
    "name": "Mock B",
    "sections": [
        Section(
            id_="I",
            topic="L06 再帰関数",
            total=35,
            problems=[
                Problem("I-1",  10, "trace",     "fib_recursive_trace"),
                Problem("I-2",   9, "fill",      "factorial_fill"),
                Problem("I-3",   8, "impl",      "factorial_tail_recursion"),
                Problem("I-4",   8, "impl",      "fib_iterative"),
            ],
        ),
        Section(
            id_="II",
            topic="L07 ポインタ",
            total=35,
            problems=[
                Problem("II-1",  10, "trace",    "pointer_array_trace"),
                Problem("II-2",   6, "diagram",  "pointer_memory_diagram"),
                Problem("II-3",  10, "fill",     "swap_fill"),
                Problem("II-4",   5, "explain",  "pass_by_value_explain"),
                Problem("II-5",   4, "debug",    "pointer_uninitialized_bug"),
            ],
        ),
        Section(
            id_="III",
            topic="L06 関数設計",
            total=30,
            problems=[
                Problem("III-1",  4, "prototype", "function_prototype"),
                Problem("III-2", 16, "impl",      "sum_normalize_impl"),
                Problem("III-3",  5, "impl",      "function_main_integration"),
                Problem("III-4",  5, "explain",   "division_by_zero_handle"),
            ],
        ),
    ],
}

# ---------------------------------------------------------------------------
# Mock C (hardcoded from 05_mock-exams/mock-exam-C.md — version: 2026-06-22)
# 大問I=30pt (基本構文・制御構造), 大問II=35pt (配列・関数), 大問III=35pt (ポインタ・文字列・再帰)
# ---------------------------------------------------------------------------
MOCK_C: dict = {
    "name": "Mock C",
    "sections": [
        Section(
            id_="I",
            topic="L03 基本構文・制御構造",
            total=30,
            problems=[
                Problem("I-1",  8, "trace",   "fizzbuzz_trace"),
                Problem("I-2",  9, "fill",    "conditional_grade_fill"),
                Problem("I-3",  6, "debug",   "while_boundary_bug"),
                Problem("I-4",  7, "explain", "program_explain"),
            ],
        ),
        Section(
            id_="II",
            topic="L05 配列・関数",
            total=35,
            problems=[
                Problem("II-1",  8, "read",  "array_init_read"),
                Problem("II-2", 12, "fill",  "bubble_sort_fill"),
                Problem("II-3",  8, "trace", "sort_trace"),
                Problem("II-4",  7, "impl",  "linear_search_impl"),
            ],
        ),
        Section(
            id_="III",
            topic="L07 ポインタ・文字列・再帰",
            total=35,
            problems=[
                Problem("III-1", 10, "trace",   "pointer_arithmetic_trace"),
                Problem("III-2", 10, "fill",    "to_upper_fill"),
                Problem("III-3", 10, "impl",    "power_iter_impl"),
                Problem("III-4",  5, "explain", "code_improvement_explain"),
            ],
        ),
    ],
}

# ---------------------------------------------------------------------------
# Mock registry (extend here for Mock B / C when built)
# ---------------------------------------------------------------------------
MOCK_REGISTRY: dict[str, dict] = {
    "A": MOCK_A,
    "B": MOCK_B,
    "C": MOCK_C,
}


def main() -> None:
    print()
    print("=" * 60)
    print("  模擬試験アナライザー")
    print("=" * 60)

    choice = _ask_mock()

    if choice not in MOCK_REGISTRY:
        if choice in ("B", "C"):
            print(f"\n[未実装] Mock {choice} の問題構造はまだ登録されていません。")
            print("  現時点では Mock A のみ対応しています。")
        else:
            print(f"\n[エラー] '{choice}' は有効な選択肢ではありません（A / B / C）。")
        sys.exit(1)

    mock = MOCK_REGISTRY[choice]
    print(f"\n=== {mock['name']} 採点開始 ===")
    print("各問題について正解 (y) / 不正解 (n) を入力してください。\n")

    missed_by_section = _collect_results(mock)
    _analyze(mock, missed_by_section)


if __name__ == "__main__":
    main()
