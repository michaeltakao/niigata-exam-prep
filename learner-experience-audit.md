---
nav_exclude: true
---

# Learner Experience Audit
# START_HERE.md + SCHEDULE.md
# Audience: complete beginner, iPad only

> **Epistemic label:** Time estimates are model-derived (100 wpm effective reading speed
> for C textbook, 8 min / Easy problem, 14 min / Medium problem). Actual times will vary
> ±30% based on individual reading speed and problem difficulty.
>
> Audit date: 2026-06-22

---

## Executive Summary

| Metric | Result |
|---|---|
| Days exceeding 2.5 h | **0 of 13** |
| Longest day | Day 13 — 135 min (2.2 h) |
| Shortest day | Day 5 — 72 min (1.2 h) |
| Max taps from cold start to lesson | **3 taps** |
| Sections with high cognitive load | 3 (START_HERE link tables, Day 3 Step 3, Day 8) |
| Broken links | 0 |
| Days with unclear completion criteria | 2 (Day 8, Day 12) |
| iPad app dependency | **Unspecified — critical gap** |

---

## 1. Navigation Audit (Tap Count)

### Path from cold start

```
App open → find START_HERE.md (1–2 taps, depends on app)
         → tap SCHEDULE link (1 tap)
         → scroll to today's day (scroll, no tap)
         → tap lesson link (1 tap)
Total: 3–4 taps to reach first lesson
```

**Second day onward** (SCHEDULE.md remembered/bookmarked):
```
App open → SCHEDULE.md (1 tap)
         → scroll to today → tap lesson (1 tap)
Total: 2 taps
```

### Tap count to each destination from SCHEDULE.md

| Destination | Taps from SCHEDULE.md |
|---|---|
| Any textbook chapter | 1 tap |
| Any drill file | 1 tap |
| Mock exam | 1 tap |
| Remediation file | 1 tap |
| formula-first guide | 1 tap |
| Progress sheet | 1 tap |
| START_HERE.md | 1 tap (back link at top) |

**Result: Navigation depth is excellent.** Every resource is reachable in 1 tap from the schedule.

### Problem: SCHEDULE.md scroll depth

SCHEDULE.md is 376 lines. A student opening it on Day 9 must scroll past Days 1–8 (≈230 lines) to reach Day 9.

**No jump-to-today navigation exists inside SCHEDULE.md.**

On a 10.9-inch iPad in portrait mode, one screen ≈ 40–50 lines. Reaching Day 9 requires 4–5 full swipe-scrolls. Day 13 requires 7–8 swipes.

---

## 2. Cognitive Load Assessment

### START_HERE.md

**Section: "教材の場所"** — 4 separate link tables (Textbook / Drill / Mock / Remediation) with a total of 18 distinct links visible at once. A beginner who opens START_HERE.md before their first session will see this full directory and may feel paralysed about where to start.

**Issue:** The 3-step instruction at the top ("1. SCHEDULE.md を開く / 2. 今日を探す / 3. チェックする") is correct and simple. But then the page continues for 60+ lines with resource tables the student does not need on Day 1.

**Risk level:** Medium. The student is told to open SCHEDULE.md immediately, but the long directory below the fold may cause "what should I be doing?" confusion on first open.

---

### SCHEDULE.md — Per-day issues

#### Day 2 — Two textbooks in one sitting

Day 2 covers L02 (1575 words) AND L03 (1631 words), plus 8 drill problems from two files.

**Estimated load:** 115 min — highest among Days 1–7.

The student has just completed Day 1 (their first-ever C experience). Day 2 immediately doubles the volume with two independent topics and requires switching between four files (L02 textbook → L02 drills → L03 textbook → L03 drills).

**Risk:** Medium. The day is within time budget, but context-switching between two topics without rest is cognitively demanding for a beginner.

---

#### Day 3 — Hidden prerequisite (formula-first guide)

Step 3 reads: "変数トレース表の練習（[解き方テクニック](07_technique-guide/formula-first.md) を先に読む）"

A beginner following the steps in order will:
1. Read L04 textbook (Step 1)
2. Write loop components (Step 2)
3. Reach Step 3 and discover they must first read a separate 426-line guide

**Issue:** The formula-first guide is a prerequisite for the drills, but it appears as a mid-session step rather than a Day 1 or Day 3 opening task. The phrase "先に読む" (read this first) inside a Step 3 instruction is easy to miss.

**Risk:** Medium-high. If the student skips the technique guide and goes directly to the drills, they attempt loop tracing without the trace-table method, increasing error rate and frustration.

---

#### Day 8 — Open-ended review with no recovery path

Day 8 instructs:
- Step 1: "今まで間違えた問題を全部見直す"
- Step 3/4: "苦手 1/2 の Easy ドリルを最初から解き直す"

**Two assumptions that may not hold:**

1. The student has been marking wrong problems in the drill files. If they haven't been using `[x]` notation or writing margin notes, Step 1 has no input to work from. There is no fallback instruction ("もし印をつけていなければ、全ての Easy E1–E5 を解き直す").

2. The student can self-identify their weakest topics. Metacognitive self-assessment is difficult for beginners. A beginner who "doesn't know what they don't know" may choose the wrong topics to review.

**Risk:** High. Day 8 is the only recovery day before the back-to-back Recursion (Day 9) + Pointers (Day 10) + Exam (Day 11). An ineffective Day 8 leaves no margin.

---

#### Day 9 — fib(5) without a worked binary tree example

Step 4 instructs the student to trace `fib(5)` by hand "同じように" (the same way as factorial).

`fact(4)` is a linear chain (4→3→2→1). `fib(5)` is a binary tree with 15 recursive calls and branch merging. These are qualitatively different to trace by hand for a beginner. `fib(5)` without a worked partial example will take significantly longer than the 22-minute estimate — or may be abandoned.

**Risk:** Medium. The completion check only requires `fact(4) = 24`, so `fib(5)` is technically optional. But a student who spends 40+ min on a failed `fib(5)` trace ends the day demoralized.

---

#### Day 9 — Ambiguous drill reference

Step 5 says: "ドリルの再帰トレース問題を解く（教科書の例題 or [L06ドリル](03_drills/L6_functions.md) の再帰問題）"

`L6_functions.md` is a 953-line functions drill file. A beginner will not know which problems within it are recursion problems. No problem numbers are given. The alternative "教科書の例題" is equally vague — which examples?

**Risk:** Medium. Vague instructions → student either skips the step or wastes time searching.

---

#### Day 12 — Remediation is unbounded

"Re-solve wrong problems (30 min)" and "Remediate 2nd weak area (25 min)" assume the student can self-pace to the minute. In practice, a struggling student may spend the entire 2 hours on one topic and skip the second.

**Risk:** Low-medium. Day 12 has no hard time constraint in the schedule instructions.

---

## 3. Time Estimates Per Day

Time model:
- Textbook: 100 wpm effective (C code requires slow reading)
- Easy drill: 8 min each | Medium: 14 min each
- Trace table from scratch: 10–22 min depending on problem depth

| Day | Topic | Est. time | Flag |
|---|---|---|---|
| 1 | Variables (L01) | **80 min** (1.3 h) | — |
| 2 | Operators + Conditionals (L02/L03) | **115 min** (1.9 h) | heaviest of Days 1–7 |
| 3 | Loops Part 1 + formula-first | **84 min** (1.4 h) | — |
| 4 | Loops Part 2 | **104 min** (1.7 h) | — |
| 5 | Arrays Part 1 | **72 min** (1.2 h) | lightest day |
| 6 | Arrays Part 2 + bubble sort | **100 min** (1.7 h) | — |
| 7 | Functions | **113 min** (1.9 h) | — |
| 8 | Review | **125 min** (2.1 h) | at-risk if self-assessment fails |
| 9 | Recursion | **89 min** (1.5 h) | fib(5) may run over |
| 10 | Pointers | **82 min** (1.4 h) | — |
| 11 | Mock Exam A | **113 min** (1.9 h) | fixed (90 min exam) |
| 12 | Remediation | **124 min** (2.1 h) | unbounded risk |
| 13 | Mock Exam B + Final | **135 min** (2.2 h) | longest day |

**No day exceeds 2.5 hours (150 min)** under the model.

Day 5 is under-loaded at 72 min — a beginner struggling with arrays may benefit from an additional optional drill set here.

---

## 4. Sections Longer Than 15 Minutes (Individual Activities)

| Activity | Location | Est. time |
|---|---|---|
| Read any textbook chapter | Days 1–7, 9–10 | 12–17 min (active reading adds 20–30 min) |
| formula-first guide | Day 3 Step 3 | 20 min |
| Any 5-problem Easy drill set | Days 1–8 | 40 min |
| Any 3-problem Medium drill set | Days 4, 6, 7 | 42 min |
| Trace fib(5) by hand | Day 9 Step 4 | 22 min (likely 35+ min in practice) |
| Mock exam | Days 11, 13 | 90 min (fixed) |

All textbook readings are above the 15-minute mark in practice. This is by design — the student is a complete beginner who cannot skim technical content. The 15-minute threshold is not a problem here; it is expected.

---

## 5. iPad-Specific Issues

### Critical: No markdown app is specified

START_HERE.md and SCHEDULE.md rely on:
- `[ ]` interactive checkboxes
- Inline fill-in fields (`___ / 100`, `苦手 1: ___`)
- Markdown link rendering (`[教科書を読む](...)`)

These require a markdown editor, not the default Files app or Notes app.

Without a compatible app (Obsidian, iA Writer, Bear, or 1Writer), the student sees raw text with `[ ]`, `[link text](url)` as literal characters — the entire navigation system breaks.

**This is the single highest-risk issue in the learner experience.**

---

### SCHEDULE.md has no "jump to today" anchor list

A 376-line single file with no internal navigation means scrolling on every session open.

---

## 6. Motivation and Pacing

### Positive signals

- Every day has a single, concrete **目標** (goal) — one sentence.
- Every day ends with a **終了チェック** — a binary pass/fail the student can self-assess.
- 📌 remediation hints are placed close to the drill steps where the student is most likely to be stuck.
- "余裕があれば" (if you have time) markers on optional hard problems correctly signal that they are not required.

### Gaps

1. **No time estimate is shown on any day header.** A student who feels she is falling behind does not know if she is on pace or not.
2. **The "重要度" star ratings in START_HERE.md show ★★★★★ for 7 of 13 days.** When everything is "最重要", the word loses meaning.
3. **Day 8 has no concrete success state.** If the student cannot write all 4 patterns from memory at Step 5, there is no instruction on whether to continue to Day 9 or repeat.
4. **No rest or break signals.** A 113-minute session (Day 11: exam day) with no suggested break may cause fatigue errors in the last third of the exam.

---

## 7. Recommended Fixes (Priority Order)

| # | Fix | Effort | Risk addressed |
|---|---|---|---|
| 1 | Add iPad app recommendation to START_HERE.md (Obsidian is free on iPad) | 1 line | Critical: rendering |
| 2 | Add a "Jump to Day" anchor list at the top of SCHEDULE.md | 13 lines | Scroll depth |
| 3 | Move formula-first guide to Day 1 Step 3 or Day 3 Step 1 (before textbook) | 2 line edits | Day 3 hidden prerequisite |
| 4 | Day 8: add fallback instruction ("印がない場合は…") and explicit pass/fail condition | 3 lines | Open-ended review |
| 5 | Day 9: replace fib(5) with a worked partial trace of fib(4); mark fib(5) as optional | 5 lines | Overwhelm risk |
| 6 | Day 9 Step 5: give explicit problem numbers ("L06ドリル M4–M6") | 1 line edit | Ambiguous reference |
| 7 | Add estimated time to each day header in SCHEDULE.md | 13 line edits | Pacing |
| 8 | Day 5: add E5–E6 as optional ("余裕があれば") to fill the lighter day | 2 lines | Underload |

---

## 8. Files Assessed

| File | Lines | Status |
|---|---|---|
| `START_HERE.md` | 102 | Usable — 1 critical gap (app) |
| `SCHEDULE.md` | 376 | Usable — 3 structural gaps (scroll, Day 3, Day 8) |

No new educational content was added or altered during this audit.
