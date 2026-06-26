---
nav_exclude: true
---

# Repository Hygiene Report — 2026-06-22

## Summary

Branch is current (up-to-date with origin/main). One modified file (Makefile) and 14 untracked
files require commit decisions. Three learner-state files have been added to `.gitignore` to
prevent personal session data from entering version control.

---

## Git Status Summary

| Item | Value |
|---|---|
| Branch | main |
| Remote sync | Up to date with origin/main |
| Modified (not staged) | 1 file — `Makefile` |
| Untracked files | 14 files (see table below) |
| Staged changes | None |

---

## .gitignore Assessment

### New Entries Added (this session)

```gitignore
# Learner session state (personal, not source)
06_progress/mastery-state.json
06_progress/daily-coaching-report.md
06_progress/session-log.md
```

### Rationale

These three files are **generated state**, not source content:

| File | Why gitignore |
|---|---|
| `06_progress/mastery-state.json` | Created on first `make coach` run. Contains learner-specific drill scores and mastery levels per topic. Committing exposes individual study performance data and causes merge conflicts if the repo is cloned by another learner. |
| `06_progress/daily-coaching-report.md` | Overwritten on every `make coach` invocation. Stale historical versions in git are misleading and wasteful. |
| `06_progress/session-log.md` | Append-only learner session history. Personal performance data. Already exists from test runs in the prior session (see note below). |

**Learner-state boundary rule**: Commit source (schedules, textbooks, scripts, drill templates).
Do not commit per-learner runtime state.

**Note on existing session-log.md**: The file was written during test runs in the prior session.
After the `.gitignore` addition, it remains on disk but will no longer be tracked by git.
The student may optionally delete it (`rm 06_progress/session-log.md`) before Day 1 to start
with a clean log, or leave it in place — the coach will continue appending to it.

### Pre-existing Entries (unchanged)

| Entry | Purpose | Assessment |
|---|---|---|
| `00_exam-analysis/raw/` | Copyrighted past-exam PDFs | Correct — keep |
| `pdf/` | Build artifact directory | Correct — keep |
| `__pycache__/`, `*.pyc`, `*.pyo` | Python cache | Correct — keep |
| `.DS_Store`, `Thumbs.db` | OS metadata | Correct — keep |

---

## Untracked Files — Commit Recommendations

| File | Type | Recommendation |
|---|---|---|
| `SCHEDULE.md` | Curriculum content | **Commit** — student-facing day-by-day guide (supplementary) |
| `START_HERE.md` | Entry point | **Commit** — first file students open |
| `baseline-assessment.md` | Curriculum doc | **Commit** |
| `exam-priority-ranking.md` | Authoritative 13-day plan | **Commit** — source of truth for coach.py schedule |
| `exam-survival-mode.md` | Curriculum doc | **Commit** |
| `high-yield-topics.md` | Curriculum doc | **Commit** |
| `improvement-analysis.md` | Curriculum doc | **Commit** |
| `learner-experience-audit.md` | Curriculum doc | **Commit** |
| `learner-feedback-form.md` | Template | **Commit** |
| `score-tracking.md` | Score log | **Commit** — structure is source; Day 0 diagnostic score (1/100) already entered (see note below) |
| `scripts/coach.py` | Source code | **Commit** |
| `scripts/analyze_mock.py` | Source code | **Commit** |
| `scripts/report.py` | Source code | **Commit** |
| `06_progress/session-log.md` | Learner session history | **Gitignore only** — personal data from test runs; will not be tracked after .gitignore update |
| `Makefile` (modified) | Build tool | **Commit** — `coach`, `status`, `analyze` targets added this session |

**Note on score-tracking.md**: This file contains the Day 0 diagnostic score (1/100, 2026-06-22).
Committing it means this score enters git history permanently. This is acceptable: it is a
student's own private repository, the diagnostic score is not sensitive data, and having the
baseline in git provides an unambiguous audit trail for progress measurement.

---

## Learner-State Boundary Diagram

```
Committed (source, shared)          Gitignored (per-learner state)
──────────────────────────          ──────────────────────────────
SCHEDULE.md                         06_progress/mastery-state.json
START_HERE.md                       06_progress/daily-coaching-report.md
scripts/coach.py                    06_progress/session-log.md
scripts/analyze_mock.py
scripts/report.py
03_drills/L*.md
02_textbook/L*.md
10_remediation/*.md
score-tracking.md (as template)
exam-priority-ranking.md
Makefile
```

---

## No Secrets Found

Manual inspection of all 14 untracked files confirms:

- No `.env` files or credential files
- No API keys, tokens, or passwords
- No private keys or certificates
- `score-tracking.md` contains only academic assessment scores — not considered sensitive
- `scripts/coach.py`, `analyze_mock.py`, `report.py` — local file I/O only, no network calls or auth tokens

All files are safe to commit as recommended above.
