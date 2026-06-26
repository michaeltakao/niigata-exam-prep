---
nav_exclude: true
---

# Success Metrics

Update this file after each study session. It is the single source of truth for your exam readiness trajectory.

---

## Drill Completion Tracker

| Drill | First Attempt Date | Score | Retry Date | Retry Score | Passed (≥70%)? |
|-------|--------------------|-------|------------|-------------|----------------|
| L1 Variables | | | | | |
| L2 Operators | | | | | |
| L3 Conditionals | | | | | |
| L4 Loops | | | | | |
| L5 Arrays | | | | | |
| L6 Functions | | | | | |
| L7 Pointers | | | | | |
| L8 Integration | | | | | |

**Running total:** ___/8 drills passed

---

## Mastery % Tracker

Update the % column after each weekly review. Use values from `07_mastery/mastery-rubric.md`.

| Topic | Tier | Week 1 % | Week 2 % | Week 3 % | Week 4 % | Final % | Target % | Met? |
|-------|------|----------|----------|----------|----------|---------|----------|------|
| L01 Variables | 2 | | | | | | 65% | |
| L02 Operators | 2 | | | | | | 65% | |
| L03 Conditionals | 2 | | | | | | 65% | |
| L04 Loops | 1★ | | | | | | 80% | |
| L05 Arrays | 1★ | | | | | | 75% | |
| L06 Functions | 1★ | | | | | | 75% | |
| L07 Pointers | 1★ | | | | | | 70% | |
| L08 Strings | 2 | | | | | | 65% | |
| L09 Structs | 2 | | | | | | 60% | |
| L10 File I/O | 2 | | | | | | 60% | |
| L11 Recursion | 2 | | | | | | 60% | |

**Trend column:** After filling in each week's %, add ↑ (improving), ↓ (declining), or → (flat) in the Final % cell as a suffix. Example: `72%↑`

---

## Mock Exam Scores

| Exam | Attempt 1 Score | Date | Attempt 2 Score | Date | Pass Threshold | Passed? |
|------|----------------|------|----------------|------|---------------|---------|
| Mock A | | | | | 70% | |
| Mock B | | | | | 75% | |
| Mock C | | | | | 80% | |

---

## Predicted Score

Formula (from `score-prediction.md`):

```
Estimated Score = (Avg Tier-1 Mastery % × 0.6) + (Avg Tier-2 Mastery % × 0.4)

Avg Tier-1 = (L04 + L05 + L06 + L07) ÷ 4
Avg Tier-2 = (L01 + L02 + L03 + L08 + L09 + L10 + L11) ÷ 7
```

Blank calculation table — fill in after each weekly review:

```
Week 1:  ( ___ × 0.6) + ( ___ × 0.4) = ___
Week 2:  ( ___ × 0.6) + ( ___ × 0.4) = ___
Week 3:  ( ___ × 0.6) + ( ___ × 0.4) = ___
Week 4:  ( ___ × 0.6) + ( ___ × 0.4) = ___
Final:   ( ___ × 0.6) + ( ___ × 0.4) = ___
```

Target predicted score before exam: **≥ 75%**

---

## Usage Instructions

- **After each drill:** Add a row to the Drill Completion Tracker with today's date and score.
- **After each weekly review:** Update the Mastery % Tracker column for the current week; add trend indicator.
- **After each mock exam:** Record score immediately while the session is fresh; route to remediation if below threshold.
- **Before the exam:** Calculate Final predicted score. If < 75%, identify the lowest-mastery topic and spend remaining time there. Run `acceptance-test.md` full checklist.
