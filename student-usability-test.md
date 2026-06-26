---
nav_exclude: true
---

# Student Usability Test — STUDENT_HOME.md
**Date:** 2026-06-23
**Scenario:** Complete beginner, iPad only, Obsidian installed, no instructor contact.
**Session scope:** First 15 minutes → Day 1 study launch.
**Method:** Cognitive walkthrough simulating a student with C score = 1/100 and zero prior
programming exposure.

---

## 1. First 15 Minutes — Step-by-Step Simulation

### 0:00 — Opens STUDENT_HOME.md in Obsidian

Student has been told "Open the file called STUDENT_HOME.md."
Obsidian renders the file cleanly. Checkboxes and links are visible and tappable.

**First impression:** "このページだけ開けば迷わない" — reassuring. Student feels oriented.

---

### 0:01–0:02 — Reads "今日は何日目？"

Student scans the date table looking for today (2026-06-23).
Finds: **Day 1 — 変数・データ型**.

**Outcome:** Student correctly identifies their day. ✓

**Confusion point A (Low):** The table shows Day 0 at the top as "今日" still
(the banner says "Day 0（今日）"). On Day 1 onward this is no longer accurate —
the student must remember that "today" means *their* row, not the Day 0 row.

---

### 0:02–0:05 — Reads "初日にやること（Day 0）"

Student is on Day 1, but this section's header says "Day 0 — 2026-06-22 のみ."
The student reads it anyway because it appears first after the date table.

**Confusion point B (Medium — time cost):**
The student spends ~2 minutes reading the Day 0 orientation section even though it no longer
applies. The priority table and score trajectory are useful context, but a Day 1 student
does not need to "Step 3 — 明日の準備" — that moment has passed.

**Notation confusion (Medium):**
The priority table lists "L04 ループ", "L05 配列", "L06 関数". The "L" prefix is never
defined anywhere in `STUDENT_HOME.md`. A complete beginner may wonder: "What is L? Is that
a lesson, a level, a lab?" This is the first encounter with the notation.

**"ブックマークしておいてください" (Low-Medium):**
Step 3 says to "bookmark" the L01 files. Obsidian on iPad supports starring files
(`...` menu → Star), but a beginner who has never used Obsidian does not know this.
No instruction is given for how to bookmark.

---

### 0:05–0:07 — Scrolls to "毎日のやること（Day 1〜13）"

Student reads Step 1: "日別スケジュールを開く → SCHEDULE.md."
Taps the SCHEDULE.md link.

**Tap count so far: 1**

---

### 0:07–0:08 — Lands in SCHEDULE.md

Student sees the back-link "← 学習ホームに戻る" at the top — good orientation signal.
Sees the Day table TOC. Finds "Day 1" row, taps the anchor link "→ Day 1."

**Tap count: 2**

**Confusion point C (Medium — platform risk):**
In-file anchor links (`#day-1--変数データ型...`) work in Obsidian but may fail in other
Markdown apps (iA Writer, Bear, default Files preview). If the anchor fails, the student
must manually scroll ~400 lines to find Day 1. Estimated abandonment risk on scroll: ~15%.

---

### 0:08–0:09 — Reads Day 1 checklist in SCHEDULE.md

Steps are clear and numbered. Checkboxes are present and tappable. 
Step 1 has a direct link to L01 textbook.

**Timing confusion (Low-Medium):**
Day 1 header says "約 80 分." The L01 textbook file itself says "所要時間: 90〜120分."
A beginner reading both will see different numbers for the same task. They will not know
which to trust. Likely outcome: mild anxiety, no action change.

---

### 0:09 — Taps L01 教科書 link

**Tap count: 3** (STUDENT_HOME → SCHEDULE → Day1 anchor → L01 textbook)

---

### 0:09–0:15 — Inside L01 textbook

The textbook opens at Section 1 "コンセプト概要." Dense explanatory prose, then the
locker analogy, then syntax diagrams. Well-structured for a beginner.

**Confusion point D (Medium — scope ambiguity):**
SCHEDULE.md Day 1 Step 2 says: "教科書に出てくる変数宣言の例を **全部** ノートに手で写す."
The L01 textbook contains approximately 30 code blocks across 11 sections. A beginner does
not know which of these are "variable declaration examples" and which are context. They may
try to copy everything (takes 45+ minutes) or give up.

**No code execution path (Low — environment constraint):**
The textbook says "このコードを実行すると…" in several places. The student has only an
iPad and no terminal. There is no instruction anywhere about what to do when they cannot
run code. The student must mentally trace all outputs. This increases cognitive load for
every exercise.

---

### End of 15-minute window

**Where the student is:** Inside L01 textbook, reading Section 3 or 4.
**Taps made:** 3
**Files opened:** STUDENT_HOME.md → SCHEDULE.md → L01 textbook
**Drills started:** No

---

## 2. Confusion Points Catalog

| ID | Location | Description | Severity | Drop risk |
|---|---|---|---|---|
| A | STUDENT_HOME.md date table | Day 0 row still reads "今日" on Day 1+ | Low | 5% |
| B | STUDENT_HOME.md Day 0 section | Day 0 orientation visible and read on Day 1; includes steps that no longer apply | Medium | 10% time cost |
| C | SCHEDULE.md | Anchor links may fail on non-Obsidian apps; student must scroll 400 lines | Medium | 15% |
| D | SCHEDULE.md Day 1 Step 2 | "全部ノートに手で写す" — scope of "all examples" is undefined | Medium | 10% |
| E | Throughout | "L01", "L02"… notation never defined | Medium | 5% |
| F | STUDENT_HOME.md Step 3 | "ブックマークしておいてください" — no iPad instruction | Low-Medium | 3% |
| G | L01 textbook vs SCHEDULE.md | Timing discrepancy: 90–120 min vs 80 min | Low | 2% |
| H | L01 textbook throughout | "実行すると…" — no way to run code on iPad; no alternative given | Low | 5% |

---

## 3. Click Path Analysis

### Current path to Day 1 study material

```
STUDENT_HOME.md
  └─ tap: SCHEDULE.md                        (click 1)
       └─ tap: [→ Day 1] anchor              (click 2)
            └─ tap: L01 textbook link        (click 3)
                 └─ [reading begins]
```

**3 taps to reach the primary study material.**

### Unnecessary tap

Tap 1 (STUDENT_HOME → SCHEDULE.md) is structurally necessary because the daily checklist
lives in SCHEDULE.md. However, if STUDENT_HOME.md surfaced the *current day's direct link*
prominently (e.g., "今日（Day 1）はここから → L01 教科書"), the student could bypass
SCHEDULE.md entirely and reach the textbook in 1 tap.

SCHEDULE.md is not wasted — its step-by-step checklist is the most actionable Day 1 content
in the repo. The issue is that a beginner does not know this before tapping in.

### Recommended path (after fix)

```
STUDENT_HOME.md
  └─ "今日はDay 1" direct link → L01 textbook  (click 1)
  └─ or: SCHEDULE.md → Day 1 checklist         (click 1, then scroll/anchor)
```

---

## 4. Day 1 Completion Probability

**Definition of "Day 1 complete":** Student finishes SCHEDULE.md Day 1 Steps 1–6
(reads L01 textbook, writes self-test, completes drill E1–E5, reviews answers).

### Probability estimate: **65%**

| Factor | Direction | Weight | Rationale |
|---|---|---|---|
| STUDENT_HOME.md is clear and reassuring | + | High | "このページだけ" reduces decision fatigue |
| SCHEDULE.md Day 1 checklist is step-by-step | + | High | No guessing required once student arrives |
| L01 textbook quality | + | Medium | Good analogies, progressive difficulty |
| L01 drill has answers + hints | + | Medium | Self-correction possible without instructor |
| 3-tap path to study material | − | Medium | ~20% of beginners lose momentum between STUDENT_HOME and L01 |
| Day 0 section read on Day 1 | − | Low | ~10% time cost, minor disorientation |
| Anchor link failure risk | − | Medium | ~15% chance of needing manual scroll |
| "全部写す" scope ambiguity | − | Medium | Student may over-scope Step 2 and run out of time |
| No code execution on iPad | − | Low | Increases cognitive load, slightly demotivating |

### Drop-off model

```
Opens STUDENT_HOME.md       → 100%
Reaches SCHEDULE.md Day 1   →  78%  (3-tap friction + Day 0 section distraction)
Opens L01 textbook          →  75%
Completes textbook read     →  70%  (scope ambiguity in Step 2 causes some to stall)
Completes drill E1–E5       →  65%  (fatigue, no code execution environment)
```

**Assumption:** These drop-off estimates are based on general usability research norms for
self-study materials with a learner at 0% baseline, not direct measurement.
Actual completion rate could vary ±15%.

---

## 5. Prioritized Recommendations

| Priority | Recommendation | Change location | Impact |
|---|---|---|---|
| P1 | Add a "今日（Day N）はここから" dynamic box near the top of STUDENT_HOME.md that shows today's date, day number, and a **direct link to today's textbook** | STUDENT_HOME.md | Reduces path from 3 taps to 1; biggest single gain |
| P2 | Clarify Step 2 in SCHEDULE.md Day 1: replace "全部ノートに手で写す" with explicit scope ("各セクションの最後にある ★ 印のコード例のみ") | SCHEDULE.md | Eliminates scope ambiguity; prevents time overrun |
| P3 | Define "L01 = 第1章（変数・型）" on first use in STUDENT_HOME.md (one sentence or a small legend table) | STUDENT_HOME.md | Removes notation confusion for every subsequent reference |
| P4 | Add a note under "ブックマークしておいてください": "Obsidian の場合: ファイルを長押し → スター ★ を付ける" | STUDENT_HOME.md | Removes app-specific gap |
| P5 | Add "コードは実行できなくてOK。出力を頭で追うだけで十分" note in L01 textbook introduction | 02_textbook/L01 | Removes anxiety for iPad-only students |
| P6 | Collapse the Day 0 section in STUDENT_HOME.md after 2026-06-22 by noting at top "Day 0（2026-06-22）は終了。Day 1 以降はスキップしてください" | STUDENT_HOME.md | Prevents Day 1 students from reading stale content |

---

## 6. Summary Verdict

The current `STUDENT_HOME.md` gives a beginner a clear orientation and links to every
study file they need. The content quality is high. The primary usability gap is
**path length**: a student who has never used Obsidian or studied C must make 3 taps and
read through a Day 0 section that no longer applies before reaching Day 1 material.

Implementing P1 (direct today-link) and P2 (scope clarification) alone would raise the
estimated Day 1 completion probability from **65% to ~80%**.
