---
nav_exclude: true
---

# Day 1 Readiness Report — 2026-06-22

## Status: READY WITH NOTES

All essential files exist. Two schedule-authority issues require attention before Day 1 begins.
See the Warnings section below before opening SCHEDULE.md.

---

## Day 1 At-a-Glance

| Item | Value |
|---|---|
| Day 1 date | **2026-06-23** (today 2026-06-22 = Day 0, the diagnostic date) |
| Estimated study time | **75 min** (SCHEDULE.md: 80 min / coach.py scope: 60–90 min — midpoint) |
| Topics (coach.py — authoritative) | **L01 変数・型・printf/scanf + L02 演算子・式** |
| Drill target | **L1 Q1–5 + L2 Q1–3** |
| Pass criteria | L1 ≥60% (3/5 correct), L2 ≥60% |

---

## Step-by-Step Day 1 Workflow

| Step | Action | File / Command | Est. time |
|---|---|---|---|
| 1 | Read START_HERE.md (entry point orientation) | START_HERE.md | 5 min |
| 2 | Read textbook L01 | 02_textbook/L01_variables-types.md | 15 min |
| 3 | Work drills L1 Q1–Q5 | 03_drills/L1_variables.md | 20 min |
| 4 | Read textbook L02 | 02_textbook/L02_operators-expressions.md | 10 min |
| 5 | Work drills L2 Q1–Q3 | 03_drills/L2_expressions.md | 15 min |
| 6 | Run `make coach` → enter session data | Terminal (project root) | 3 min |
| 7 | Run `make status` to see current readiness snapshot | Terminal (project root) | 2 min |
| 8 | Record drill score in score-tracking.md | score-tracking.md | 5 min |

**Total: ~75 min**

---

## Warnings

### ℹ️ RESOLVED — SCHEDULE.md vs coach.py Schedule Conflict

`START_HERE.md` and `SCHEDULE.md` now carry an in-file notice directing students to follow
`make coach` when daily topics diverge. The underlying schedules differ (see table below),
but the authority is now unambiguous at the point the student reads it.

**Authoritative schedule: `scripts/coach.py`**

Reason: `coach.py`'s SCHEDULE dict was derived from the priority analysis in
`exam-priority-ranking.md` (13-day optimised plan, last updated 2026-06-22). SCHEDULE.md
predates this optimisation. The exam-priority-ranking.md file explicitly states:
> "scripts/coach.py は本スケジュール（13日）に基づき動作する。"

| Day | SCHEDULE.md (START_HERE.md points here) | coach.py — AUTHORITATIVE |
|---|---|---|
| 1 | L01 のみ（変数・データ型）80 min | **L01+L02** 同日完了 |
| 2 | L02+L03（演算子+条件分岐） | L03 条件分岐のみ |
| 7 | L06 関数 | L05 配列 Easy |
| 9 | L11 再帰 | L05 探索+最大最小 |
| 10 | L07 ポインタ | L06 関数 |
| 11 | 模擬試験 A | L06 再帰 |
| 12 | 弱点補強 | Mock A（60分時間制限）|
| 13 | 模擬試験 B | ギャップ補強 + L07 Easy |

**Action**: For the daily topic and drill assignment, always run `make coach` and follow its output.
Use SCHEDULE.md only for its within-day step-by-step checklists (reading instructions, drill
links, "今日の終了チェック" items) — not for determining which day covers which topic.

---

### ℹ️ Timing — Why Day 1 is Tomorrow (2026-06-23)

`coach.py` reads the baseline date from `score-tracking.md`:

```
| 2026-06-22 | Diagnostic (Day 0) | 1 | ...
```

It then computes: `current_day = (today − baseline_date).days`

Today (2026-06-22) gives `current_day = 0`. Running `make coach` today displays:

```
本日は Day 0（診断日 2026-06-22 基準）。
明日からDay 1スタート。`exam-priority-ranking.md` と `high-yield-topics.md` を読んでください。
```

**Use today (Day 0)** to read `exam-priority-ranking.md` and `high-yield-topics.md`.
Day 1 drills begin 2026-06-23.

---

### ℹ️ mastery-state.json Does Not Exist Yet — Expected

`06_progress/mastery-state.json` is created automatically on the first completed `make coach`
session. It does not exist before Day 1. `coach.py` handles this gracefully (lines 131–133):

```python
def load_mastery_state() -> MasteryState:
    if not MASTERY_STATE_PATH.exists():
        return MasteryState()  # starts fresh
```

The missing file is expected. No action required.

---

### ℹ️ `make status` Shows Baseline (1/100) Only — Expected

`report.py` reads `success-metrics.md` and `score-tracking.md`. Both currently contain only
baseline / placeholder data. The status report will render a zeroed-out readiness bar.
This is correct behaviour at Day 0; it will update as drill scores are entered.

---

### ℹ️ `make analyze` Is Not Yet Applicable

`analyze_mock.py` requires a completed mock exam (Mock A / B / C) as input.
First applicable use: **Day 12**, after completing Mock A.

---

## File Health Check

| File | Status | Notes |
|---|---|---|
| START_HERE.md | ✅ exists | Entry point |
| SCHEDULE.md | ✅ exists | Supplementary checklists (see ⚠️ above) |
| scripts/coach.py | ✅ exists | Authoritative schedule — `make coach` |
| scripts/report.py | ✅ exists | `make status` |
| scripts/analyze_mock.py | ✅ exists | `make analyze` (Day 12+) |
| Makefile | ✅ exists | Targets: coach, status, analyze, check |
| score-tracking.md | ✅ exists | Baseline 2026-06-22, 1/100 |
| exam-priority-ranking.md | ✅ exists | Read on Day 0 |
| exam-survival-mode.md | ✅ exists | Reference during exam week |
| high-yield-topics.md | ✅ exists | Read on Day 0 |
| success-metrics.md | ✅ exists | Placeholder — expected zeroed output |
| baseline-assessment.md | ✅ exists | |
| 02_textbook/L01_variables-types.md | ✅ exists | Day 1 textbook |
| 02_textbook/L02_operators-expressions.md | ✅ exists | Day 1 textbook |
| 03_drills/L1_variables.md | ✅ exists | Day 1 drills |
| 03_drills/L2_expressions.md | ✅ exists | Day 1 drills |
| 03_drills/L3_conditions.md | ✅ exists | Day 2 drills |
| 03_drills/L4_loops.md | ✅ exists | Days 3–6 drills |
| 03_drills/L5_arrays.md | ✅ exists | Days 7–9 drills |
| 03_drills/L6_functions.md | ✅ exists | Days 10–11 drills |
| 03_drills/L7_pointers.md | ✅ exists | Day 13 drills |
| 10_remediation/loops.md | ✅ exists | Supplementary — reference if stuck |
| 10_remediation/arrays.md | ✅ exists | Supplementary |
| 10_remediation/functions.md | ✅ exists | Supplementary |
| 10_remediation/pointers.md | ✅ exists | Supplementary |
| 06_progress/mastery-state.json | ❌ not yet | Created on first `make coach` run — expected |
| 06_progress/daily-coaching-report.md | ❌ not yet | Created on first `make coach` run — expected |

---

## Total Time Estimate

| Step | Time |
|---|---|
| Orientation (START_HERE.md + `make coach` Day 0 output) | 8 min |
| L01 textbook read | 15 min |
| L01 drills (Q1–Q5) | 20 min |
| L02 textbook read | 10 min |
| L02 drills (Q1–Q3) | 15 min |
| Close-out (`make status` + score-tracking.md update) | 7 min |
| **Total** | **~75 min** |
