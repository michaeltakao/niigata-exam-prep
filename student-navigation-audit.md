# Student Navigation Audit — 2026-06-23

**Scope:** Every student-facing file reachable from the repo root.
**Method:** Enumerate all `.md` files in student-visible directories; cross-reference against
links present in `STUDENT_HOME.md`; verify entry-point exclusivity.
**Standard:** Every file a student needs must be reachable in ≤2 taps from `STUDENT_HOME.md`.

---

## 1. Pre-Audit State (Issues Found)

| # | Issue | Severity |
|---|---|---|
| 1 | `SCHEDULE.md` line 8 linked back to `START_HERE.md` (instructor file) | High |
| 2 | `SCHEDULE.md` line 399 second back-link also pointed to `START_HERE.md` | High |
| 3 | `SCHEDULE.md` opening blockquote referenced `make coach` — a terminal command unavailable on iPad | High |
| 4 | `START_HERE.md` had no instructor-only marker; a student opening it would not know to leave | High |
| 5 | `03_drills/L8_exam.md` (30-question exam-format drill) not linked from `STUDENT_HOME.md` | Medium |
| 6 | `02_textbook/L06_strings.md` (SHOULD topic) not linked from `STUDENT_HOME.md` | Medium |
| 7 | `score-tracking.md` (mock exam score log) not linked from `STUDENT_HOME.md` | Medium |
| 8 | Two competing root-level entry points with overlapping purpose (`START_HERE.md`, `STUDENT_HOME.md`) | High |

---

## 2. Changes Made

| File | Change |
|---|---|
| `START_HERE.md` | Added `🔒 [INSTRUCTOR FILE]` banner at top with redirect link to `STUDENT_HOME.md` |
| `SCHEDULE.md` line 8 | Back-link changed from `START_HERE.md` → `STUDENT_HOME.md` |
| `SCHEDULE.md` line 399 | Second back-link changed from `START_HERE.md` → `STUDENT_HOME.md` |
| `SCHEDULE.md` blockquote | Removed `make coach` reference; replaced with canonical-authority note pointing to `STUDENT_HOME.md` |
| `STUDENT_HOME.md` | Added link to `03_drills/L8_exam.md` in mock exams table |
| `STUDENT_HOME.md` | Added link to `02_textbook/L06_strings.md` in textbook quick-reference (labelled "時間があれば") |
| `STUDENT_HOME.md` | Added link to `score-tracking.md` in Step 3 score-recording section |

---

## 3. Post-Audit Link Coverage

### 3a. Textbooks (`02_textbook/`)

| File | STUDENT_HOME.md | Status | Notes |
|---|---|---|---|
| L01_variables-types.md | ✓ | Linked | Day 1 primary |
| L02_operators-expressions.md | ✓ | Linked | Day 2 primary |
| L03_conditions.md | ✓ | Linked | Day 2 secondary |
| L04_loops.md | ✓ | Linked | Days 3–7 primary |
| L05_arrays.md | ✓ | Linked | Days 5–7 primary |
| L06_strings.md | ✓ | Linked | Labelled "時間があれば" |
| L07_functions.md | ✓ | Linked | Days 7, 11–12 primary |
| L08_pointers.md | ✓ | Linked | Day 10 primary |
| L09_structs.md | — | Intentionally omitted | SKIP topic (0 exam appearances R6–R8) |
| L10_algorithms.md | — | Intentionally omitted | SKIP topic (not in 13-day scope) |
| L11_recursion.md | ✓ | Linked | Day 9 primary |

### 3b. Drills (`03_drills/`)

| File | STUDENT_HOME.md | Status |
|---|---|---|
| L1_variables.md | ✓ | Linked |
| L2_expressions.md | ✓ | Linked |
| L3_conditions.md | ✓ | Linked |
| L4_loops.md | ✓ | Linked |
| L5_arrays.md | ✓ | Linked |
| L6_functions.md | ✓ | Linked |
| L7_pointers.md | ✓ | Linked |
| L8_exam.md | ✓ | Linked (added this session) |

### 3c. Mock Exams (`05_mock-exams/`)

| File | STUDENT_HOME.md | Status |
|---|---|---|
| mock-exam-A.md | ✓ | Linked — Day 11 |
| mock-exam-B.md | ✓ | Linked — Day 13 |
| mock-exam-C.md | ✓ | Linked — optional |

### 3d. Progress & Scores

| File | STUDENT_HOME.md | Status |
|---|---|---|
| 06_progress/student-progress.md | ✓ | Linked — daily drills |
| score-tracking.md | ✓ | Linked (added this session) — mock exams |

### 3e. Remediation (`10_remediation/`)

| File | STUDENT_HOME.md | Status |
|---|---|---|
| loops.md | ✓ | Linked |
| arrays.md | ✓ | Linked |
| functions.md | ✓ | Linked |
| pointers.md | ✓ | Linked |

### 3f. Supplementary

| File | STUDENT_HOME.md | Status |
|---|---|---|
| SCHEDULE.md | ✓ | Linked — daily checklist |
| 07_technique-guide/formula-first.md | ✓ | Linked — exam techniques |

---

## 4. Entry Point Verification

**Criterion:** Exactly one root-level file should function as the student entry point.

| File | Role | Student-Facing? | Has Instructor Banner? |
|---|---|---|---|
| `STUDENT_HOME.md` | **Primary student entry point** | Yes | n/a |
| `START_HERE.md` | Instructor / legacy | Marked instructor-only | ✓ Added this session |
| `SCHEDULE.md` | Daily checklist (secondary) | Yes — reached via `STUDENT_HOME.md` | n/a — back-link fixed |
| `README.md` | Developer overview | No student language | — |

**Result: exactly one student entry point — `STUDENT_HOME.md`.**

---

## 5. Files Intentionally Hidden from Students

The following root-level files exist but are not linked from `STUDENT_HOME.md` and contain no
student-actionable content:

| File | Category |
|---|---|
| `README.md` | Developer overview |
| `STATUS.md` | Developer status tracking |
| `START_HERE.md` | Instructor entry point (now marked) |
| `instructor-dashboard.md` | Instructor view |
| `acceptance-test.md` | Instructor pass/fail criteria |
| `day1-readiness-report.md` | Instructor audit |
| `baseline-assessment.md` | Instructor diagnostic |
| `exam-priority-ranking.md` | Developer priority analysis |
| `high-yield-topics.md` | Developer ROI analysis |
| `score-prediction.md` | Developer prediction model |
| `code-verification-report.md` | Developer QA |
| `repository-hygiene-report.md` | Developer hygiene |
| `improvement-analysis.md` | Developer analysis |
| `learner-experience-audit.md` | Developer UX audit |
| `learner-feedback-form.md` | Developer template |
| `mock-exam-workflow.md` | Instructor workflow |
| `weekly-review.md` | Instructor review |
| `diagnostic-checklist.md` | Error-classification engine (instructor) |
| `00_exam-analysis/` | Instructor exam analysis |
| `01_roadmap/` | Instructor planning |
| `04_question-map/` | Instructor question mapping |
| `07_mastery/` | Instructor mastery rubric |
| `08_math/`, `09_physics/` | Other subjects (out of 13-day scope) |
| `09_study-plans/` | Instructor long-plan templates |
| `08_schedule/` | Instructor scheduling |
| `scripts/` | Developer tools |
| `templates/` | Developer LaTeX template |
| `Makefile` | Developer build |
| `.gitignore`, `.git/`, `.ruff_cache/` | Version control |

---

## 6. Link Integrity Check

```
Total links in STUDENT_HOME.md : 36
Broken links                   : 0
Files covered (student-facing) : 28 / 28  (L09, L10 intentionally omitted)
Entry points                   : 1  (STUDENT_HOME.md)
Outbound links to START_HERE.md from student files : 0
```

**Status: PASS — navigation is complete, consistent, and single-entry.**
