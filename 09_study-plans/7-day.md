# 7-Day Crash Course — Tier-1 Focus

**Goal:** Reach ≥75% mastery on Loops, Arrays, Functions, and Pointers before any other topics.  
**Daily commitment:** 3–4 hours/day  
**Target exam score:** ≥65% (baseline pass)

---

## Day 1 — Diagnostic + Loops Foundation (3.5h)

**Morning (1h): Diagnostic**
- Read and complete `diagnostic-checklist.md`
- Identify your current weak topics
- Record baseline in `06_progress/student-progress.md` (all scores = 0%)

**Afternoon (1.5h): L04 Loops — Concept**
- Read `02_textbook/L04` fully
- Trace these constructs by hand:
  - `for` loop with index
  - `while` loop with condition
  - `do-while` loop
  - nested loop
- Complete `03_drills/L4` Q1–4

**Evening (1h): Self-Quiz**
- Without notes: write a `for` loop that prints 1–10
- Without notes: write a `while` loop that sums an array
- Check answers against `02_textbook/L04`
- Record score in `06_progress/student-progress.md`

**Pass criterion:** ≥60% on drills Q1–4. If below, spend 30 extra minutes re-reading before Day 2.

---

## Day 2 — Arrays (4h)

**Morning (1.5h): L05 Arrays — Concept**
- Read `02_textbook/L05` fully
- Trace: 1D array declaration, initialization, access by index
- Trace: 2D array row-major traversal

**Afternoon (1.5h): Drills**
- Complete `03_drills/L5` Q1–6
- For every wrong answer: re-read the relevant section, rework the question

**Evening (1h): Combined Practice**
- Write a program that: declares an int array[10], fills it with squares (i²), prints it
- Include a loop from Day 1 (link the two topics)
- Record score in `06_progress/student-progress.md`

**Pass criterion:** ≥65% on drills Q1–6.

---

## Day 3 — Functions (4h)

**Morning (1.5h): L06 Functions — Concept**
- Read `02_textbook/L06` fully
- Trace: function declaration, definition, call, return value
- Trace: pass-by-value vs. pass-by-pointer (preview for Day 5)

**Afternoon (1.5h): Drills**
- Complete `03_drills/L6` Q1–6
- Draw the call stack for at least one example by hand

**Evening (1h): Combined Practice**
- Write a function `int sum_array(int arr[], int n)` that returns the sum of an array
- Call it from `main()` using your Day 2 array
- Record score in `06_progress/student-progress.md`

**Pass criterion:** ≥65% on drills Q1–6.

---

## Day 4 — Pointers (4h)

**Morning (1.5h): L07 Pointers — Concept**
- Read `02_textbook/L07` fully
- Draw a memory diagram for: `int x = 5; int *p = &x;`
- Trace: `*p = 10` (what changes?), `p++` (what changes?)
- Trace: pointer to array, pointer as function argument

**Afternoon (1.5h): Drills**
- Complete `03_drills/L7` Q1–6
- For every question: draw the memory diagram first, then answer

**Evening (1h): Combined Practice**
- Rewrite `sum_array` from Day 3 using pointer arithmetic instead of indexing
- Verify same output
- Record score in `06_progress/student-progress.md`

**Pass criterion:** ≥60% on drills Q1–6. (Pointers are hard — 60% is acceptable today.)

---

## Day 5 — Loops Review + Arrays Review (3.5h)

**This is your spaced-rep Day 3 for L04 and L05.**

**Morning (1h): Loops Recall**
- Without notes: write `for`, `while`, `do-while` from memory
- Check against `02_textbook/L04`
- Complete `03_drills/L4` Q5–8

**Afternoon (1h): Arrays Recall**
- Without notes: write 1D and 2D array initialization
- Complete `03_drills/L5` Q5–8

**Evening (1.5h): Functions + Pointers Combined**
- Complete `03_drills/L6` Q7–8 and `03_drills/L7` Q7–8
- Write a function that takes an int pointer and doubles the value at that address
- Record all scores in `06_progress/student-progress.md`

**Pass criterion:** ≥70% across all four drill sets today.

---

## Day 6 — Remediation (3h)

Identify your two lowest-scoring topics from Days 1–5.

**Option A — Pointers weak:**
- Read `10_remediation/pointers.md` fully
- Redo `03_drills/L7` Q1–4 with fresh paper, draw every memory diagram
- Target: ≥70% re-attempt

**Option B — Arrays weak:**
- Read `10_remediation/arrays.md` fully
- Redo `03_drills/L5` Q1–4 focused on index errors
- Target: ≥70% re-attempt

**Option C — Loops weak:**
- Read `10_remediation/loops.md` fully
- Trace three nested-loop examples by hand
- Target: ≥70% re-attempt

**Option D — Functions weak:**
- Read `10_remediation/functions.md` fully
- Re-trace call stack examples, rewrite without notes
- Target: ≥70% re-attempt

Spend 1.5h on your weakest topic, then 1h on your second weakest, then 30 min reviewing scores.

**Record remediation scores in `06_progress/student-progress.md`.**

---

## Day 7 — Mock Exam A Simulation (3h)

**Instructions:**
1. Close all notes and textbooks — exam conditions
2. Set a timer for 90 minutes
3. Attempt `05_mock-exams/mock-A` in full

**After the exam (1h):**
- Grade immediately using the answer key
- Record score in `06_progress/student-progress.md`
- For each wrong answer: identify which topic it tested
- Route each wrong topic to its remediation file (`10_remediation/`)

**Gap Analysis table (fill in):**

| Topic | Questions Wrong | Remediation File | Priority |
|-------|----------------|-----------------|----------|
| L04 Loops | | `10_remediation/loops.md` | |
| L05 Arrays | | `10_remediation/arrays.md` | |
| L06 Functions | | `10_remediation/functions.md` | |
| L07 Pointers | | `10_remediation/pointers.md` | |

**Pass criterion for 7-day plan:** Mock A score ≥60%.  
If ≥60%: plan complete, proceed to 14-day plan for full coverage.  
If <60%: repeat Days 5–7 cycle before advancing.

---

## Score Log

| Day | Topic | Drill Score | Notes |
|-----|-------|------------|-------|
| 1 | L04 Loops | /10 | |
| 2 | L05 Arrays | /10 | |
| 3 | L06 Functions | /10 | |
| 4 | L07 Pointers | /10 | |
| 5 | Review day | /10 | |
| 6 | Remediation | — | |
| 7 | Mock A | /100 | |
