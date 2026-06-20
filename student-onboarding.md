# Student Onboarding Guide

## Welcome & Overview

This LMS contains everything you need to pass the 新潟大学 transfer exam in C programming: an 11-chapter C textbook (`02_textbook/`), 8 progressive drills (`03_drills/`), 3 mock exams (`05_mock-exams/`), a diagnostic checklist, score prediction tools, and structured study plans from 7 to 60 days. Your goal is to reach exam-ready status — defined objectively in `acceptance-test.md` — by the date of your transfer exam.

---

## Step 1 — Diagnostic

Open `diagnostic-checklist.md` and answer every item honestly. Do not look up answers. Note your raw score as a percentage.

**Routing table:**

| Diagnostic Score | Recommended Plan |
|-----------------|-----------------|
| 0–30%           | 60-day plan (`09_study-plans/60-day.md`) |
| 31–60%          | 30-day plan (`09_study-plans/30-day.md`) |
| 61–80%          | 14-day plan (`09_study-plans/14-day.md`) |
| 81%+            | 7-day plan (`09_study-plans/7-day.md`) |

If you are unsure whether to round up or down, choose the longer plan. It is better to finish early than to scramble.

---

## Step 2 — Skill Placement

After the diagnostic, identify which topics you marked as unknown or uncertain. Organize them into two tiers:

**Tier-1★ (non-negotiable — must master)**
- Loops (L04)
- Arrays (L05)
- Functions (L06)
- Pointers (L07)

Even if you believe you know a Tier-1 topic, verify by running the corresponding drill before skipping it. These topics appear in almost every exam question.

**Tier-2 (important, but recoverable if partially weak)**
- Variables (L01), Operators (L02), Conditionals (L03)
- Strings (L08), Structs (L09), File I/O (L10), Recursion (L11)

Mark your placement in `06_progress/student-progress.md` under "Initial Skill Placement."

---

## Step 3 — Select Study Plan

Open `09_study-plans/` and open the file matching your routing from Step 1. Read the Day 1 instructions completely before starting any work. Each plan specifies:
- Which textbook chapter to read
- Which drill to run
- How long to spend per activity
- What to record at the end of the day

Do not skip ahead. The plans are sequenced for spaced repetition.

---

## Daily Workflow

| Time | Action |
|------|--------|
| Morning | Open your study plan, check today's topic and drill assignment |
| Study session | Read the assigned `02_textbook/L0X` chapter, then run the assigned drill in `03_drills/` |
| Evening | Record your drill score in `06_progress/student-progress.md` |
| Weekly (Day 7, 14, 21, 28) | Update mastery band in `07_mastery/mastery-rubric.md`; run `weekly-review.md` checklist |
| Monthly / at plan milestone | Run mock exam per `mock-exam-workflow.md` |

Keep sessions to 60–90 minutes. Consistent short sessions beat irregular marathons.

---

## How to Log Scores

1. Open `06_progress/student-progress.md`
2. Find the **Score Log** table
3. Add a new row with today's date, topic name, and your Easy / Medium / Hard question scores
4. In the **Weak-Topic Flags** section, mark any topic where your Hard score is below 60%
5. Save the file

Example row:
```
| 2026-06-21 | L04 Loops | 10/10 | 8/10 | 5/10 |
```

---

## How to Update Mastery Bands

1. Open `07_mastery/mastery-rubric.md`
2. Find the section for your current topic (e.g., "L04 Loops")
3. Read the 5 band descriptors (0% / 25% / 50% / 75% / 100%)
4. Honestly assess which band you currently meet — pick the highest band where you meet ALL criteria
5. Record your current band with the date
6. Open `instructor-dashboard.md` and update the progress bar for that topic

Update mastery bands at least once per week, after completing a drill.

---

## Key File Map

| File | Purpose |
|------|---------|
| `diagnostic-checklist.md` | Entry assessment — determines your study plan |
| `06_progress/student-progress.md` | Daily score log + completion tracker |
| `07_mastery/mastery-rubric.md` | 5-band mastery self-assessment per topic |
| `instructor-dashboard.md` | One-page view of all mastery bars + exam score estimate |
| `acceptance-test.md` | Objective checklist — all boxes checked = Exam Ready |
