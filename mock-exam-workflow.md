---
nav_exclude: true
---

# Mock Exam Workflow

## Pre-Exam Setup

Before starting a mock exam:

- [ ] Confirm which mock exam to take (A → B → C in order; do not skip)
- [ ] Verify you have met the mastery prerequisites:
  - Before Mock A: all Tier-1 topics at ≥ 25%
  - Before Mock B: all Tier-1 topics at ≥ 50%
  - Before Mock C: all Tier-1 topics at ≥ 75%
- [ ] Set a timer: **90 minutes**
- [ ] Close all reference materials except one C syntax reference sheet (if your exam permits it)
- [ ] Have paper for scratch work
- [ ] Find a quiet environment — simulate exam conditions

---

## During the Exam

- Attempt every question. Blank answers score 0; a partial attempt may earn partial credit.
- Mark uncertain answers with `?` so you can revisit them if time allows.
- Time allocation guide:
  - Variables / Operators / Conditionals: ~10 minutes total
  - Loops + Arrays: ~25 minutes total
  - Functions + Pointers: ~30 minutes total
  - Strings / Structs / File I/O / Recursion: ~25 minutes total
- If stuck on a question for more than 5 minutes, move on and return at the end.

---

## Post-Exam: Record Score

1. Grade your exam using the answer key in `05_mock-exams/`
2. Calculate: (correct answers) ÷ (total questions) × 100 = score %
3. Open `06_progress/student-progress.md`
4. Find the **Mock Exam Score** table
5. Add a row: Exam name | Score % | Date | Notes on weak areas

---

## Diagnostic Routing

| Mock Score | Action |
|-----------|--------|
| ≥ pass threshold (see below) | Proceed to next mock exam |
| 60% – threshold | Targeted remediation on failed topics, then re-test |
| < 60% | Full remediation pass on all Tier-1 topics before retaking |

**Pass thresholds:**
- Mock A: ≥ 70%
- Mock B: ≥ 75%
- Mock C: ≥ 80%

**If score < 60%:** Work through all four files in `10_remediation/` from start to finish before retaking the same mock exam.

**If score 60%–threshold:** Identify which topic sections you lost the most points on. Route only to the relevant remediation files (see below).

---

## Topic-by-Topic Routing

After grading, find the topic(s) where you scored below 70%. Route each one:

| Weak Topic | Remediation File |
|-----------|-----------------|
| Loops (L04) | `10_remediation/loops.md` |
| Arrays (L05) | `10_remediation/arrays.md` |
| Functions (L06) | `10_remediation/functions.md` |
| Pointers (L07) | `10_remediation/pointers.md` |
| Variables (L01) | Re-read `02_textbook/L01`, re-run Drill L1 |
| Operators (L02) | Re-read `02_textbook/L02`, re-run Drill L2 |
| Conditionals (L03) | Re-read `02_textbook/L03`, re-run Drill L3 |
| Strings (L08) | Re-read `02_textbook/L08`, re-run Drill L8 |
| Structs (L09) | Re-read `02_textbook/L09`, re-run Drill (if available) |
| File I/O (L10) | Re-read `02_textbook/L10`, re-run Drill (if available) |
| Recursion (L11) | Re-read `02_textbook/L11`, re-run Drill (if available) |

Complete all assigned remediation files before scheduling the re-test.

---

## Re-Test Gate

Before moving to the next mock exam, verify all of the following:

- [ ] Completed all remediation files for weak topics
- [ ] Re-ran the relevant drill(s) after remediation
- [ ] Scored ≥ 80% on the Drill L8 exit quiz (the cumulative integration drill)
- [ ] Updated mastery bands in `07_mastery/mastery-rubric.md` for all remediated topics
- [ ] Confirmed updated predicted score in `instructor-dashboard.md` is trending upward

Only schedule the next mock exam after all boxes are checked.

---

## Mock Exam Schedule

Integrated with study plans:

| Event | 7-day Plan | 14-day Plan | 30-day Plan | 60-day Plan |
|-------|-----------|------------|------------|------------|
| Mock A | Day 6 | Day 12 | Day 14 | Day 21 |
| Mock B | — | — | Day 22 | Day 35 |
| Mock C | — | — | Day 28 | Day 49 |
| Exam simulation | Day 7 | Day 14 | Day 30 | Day 56 |

Mock A = end of first full pass through all topics.
Mock B = midpoint of second pass, after targeted remediation.
Mock C = final readiness check before exam week.
