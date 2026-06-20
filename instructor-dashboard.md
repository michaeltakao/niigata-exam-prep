# Instructor Dashboard — 新潟大学 編入試験対策 (C Programming)

> **How to use:** This is your single-glance status page. Update mastery bars and scores after each session using the instructions in §6.

---

## 1. Mastery Overview — All 11 Topics

| Topic | Tier | Mastery | Bar | Status |
|-------|------|---------|-----|--------|
| L01 Variables | Tier-2 | 0% | ░░░░░ | Not Started |
| L02 Operators | Tier-2 | 0% | ░░░░░ | Not Started |
| L03 Conditionals | Tier-2 | 0% | ░░░░░ | Not Started |
| L04 Loops ★ | Tier-1 | 0% | ░░░░░ | Not Started |
| L05 Arrays ★ | Tier-1 | 0% | ░░░░░ | Not Started |
| L06 Functions ★ | Tier-1 | 0% | ░░░░░ | Not Started |
| L07 Pointers ★ | Tier-1 | 0% | ░░░░░ | Not Started |
| L08 Strings | Tier-2 | 0% | ░░░░░ | Not Started |
| L09 Structs | Tier-2 | 0% | ░░░░░ | Not Started |
| L10 File I/O | Tier-2 | 0% | ░░░░░ | Not Started |
| L11 Recursion | Tier-2 | 0% | ░░░░░ | Not Started |

**Bar key:** ░░░░░ = 0% · █░░░░ = 20% · ██░░░ = 40% · ███░░ = 60% · ████░ = 80% · █████ = 100%

★ = **Tier-1** topic (Loops, Arrays, Functions, Pointers) — weighted **0.6** of exam score  
Tier-2 topics (all others) — weighted **0.4** of exam score

---

## 2. Estimated Exam Score

```
Estimated Score = (Avg Tier-1 Mastery × 0.6) + (Avg Tier-2 Mastery × 0.4)
               = (0% × 0.6) + (0% × 0.4)
               = 0%
```

Update by averaging the four Tier-1 % values and the seven Tier-2 % values from the table above.

| Score | Status |
|-------|--------|
| ≥ 80% | **Exam Ready** — proceed to exam simulation |
| 70–79% | **Near Ready** — polish Tier-1 topics, re-run Mock C |
| 60–69% | **At Risk** — intensive remediation on weakest Tier-1 topic |
| < 60% | **Not Ready** — restart from `diagnostic-checklist.md` |

---

## 3. Mock Exam Scores

| Exam | Score | Date | Pass Threshold | Status |
|------|-------|------|----------------|--------|
| Mock A | — | — | ≥ 70 | Not taken |
| Mock B | — | — | ≥ 75 | Not taken |
| Mock C | — | — | ≥ 80 | Not taken |

See `mock-exam-workflow.md` for the score → remediation routing process.

---

## 4. Risk Areas (Topics < 75%)

**Currently: all 11 topics are at risk (0% mastery — study not yet started).**

Once study begins, flag any topic below 75% here and route accordingly:

**Tier-1 ★ (remediation files available):**
- L04 Loops < 75% → see `10_remediation/loops.md`
- L05 Arrays < 75% → see `10_remediation/arrays.md`
- L06 Functions < 75% → see `10_remediation/functions.md`
- L07 Pointers < 75% → see `10_remediation/pointers.md`

**Tier-2 (textbook re-read):**
- L01 Variables < 75% → re-read `02_textbook/L01`
- L02 Operators < 75% → re-read `02_textbook/L02`
- L03 Conditionals < 75% → re-read `02_textbook/L03`
- L08 Strings < 75% → re-read `02_textbook/L08`
- L09 Structs < 75% → re-read `02_textbook/L09`
- L10 File I/O < 75% → re-read `02_textbook/L10`
- L11 Recursion < 75% → re-read `02_textbook/L11`

---

## 5. Priority Recommendation Queue

**Next 3 actions (execute in order):**

1. **Run diagnostic** → open `diagnostic-checklist.md`, complete self-assessment, determine starting level (Beginner / Intermediate / Advanced)
2. **Select study plan** → open `09_study-plans/` and choose based on available time:
   - < 1 week → `7-day.md` (Tier-1 only)
   - ~2 weeks → `14-day.md` (full L01–L11 + Mock A)
   - ~1 month → `30-day.md` (two passes + all mocks)
   - ~2 months → `60-day.md` (three passes + exam simulation)
3. **Begin Tier-1 Loops (L04):**
   - Read `02_textbook/L04` chapter
   - Run `03_drills/L4` exercises
   - Record drill score in `06_progress/student-progress.md`
   - Self-assess mastery band in `07_mastery/mastery-rubric.md`
   - Update L04 row in this dashboard

---

## 6. How to Update This Dashboard

After each study session:

- **Mastery bar:** Convert your mastery % from `07_mastery/mastery-rubric.md` to blocks (every 20% = one █). Edit the L0X row above.
- **Status column:** Use `Not Started` / `In Progress` / `≥ 75% ✓` / `Exam Ready ✓✓`.
- **Estimated Score:** Recalculate using the formula in §2 whenever any Tier-1 or Tier-2 mastery changes by ≥ 10%.
- **Mock scores:** Fill in the table in §3 immediately after each mock. Compare against thresholds and update §4.
- **Priority Queue (§5):** Replace completed actions with the next logical step. The queue should always show exactly 3 items.

Full score history lives in `06_progress/student-progress.md`. Band definitions live in `07_mastery/mastery-rubric.md`.

---

## 7. Legend & File Map

| Dashboard Element | Source File | Purpose |
|-------------------|-------------|---------|
| Mastery % / bars | `07_mastery/mastery-rubric.md` | 5-band rubric (0/25/50/75/100%) per topic |
| Score log | `06_progress/student-progress.md` | Raw drill & mock scores, session log |
| Mock exam scores | `05_mock-exams/` + `mock-exam-workflow.md` | Mock A/B/C papers + routing process |
| Remediation plans | `10_remediation/*.md` | Loops / Arrays / Functions / Pointers |
| Study plans | `09_study-plans/` | 7/14/30/60-day schedules |
| Spaced repetition | `08_schedule/review-schedule.md` | Day-by-day review calendar |
| Diagnostic | `diagnostic-checklist.md` | Entry-level skill placement |
| Score prediction | `score-prediction.md` | Weighted score formula & thresholds |
| Weekly review | `weekly-review.md` | Week 1–4 checkpoints |
| Success criteria | `acceptance-test.md` | Objective "Exam Ready" checklist |
| Onboarding | `student-onboarding.md` | First-time student entry guide |

---

*Last updated: — · Next review: —*
