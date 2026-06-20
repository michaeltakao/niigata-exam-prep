# Spaced Repetition Review Schedule

## Overview

Five review sessions per topic using expanding intervals:

| Session | Interval | Focus |
|---------|----------|-------|
| Day 1   | Study day | Initial concept + first drills |
| Day 3   | +2 days  | Recall + fill-blank exercises |
| Day 7   | +4 days  | Independent writing from memory |
| Day 14  | +7 days  | Timed drill set + mock section |
| Day 30  | +16 days | Full mock routing + mastery check |

**Pass criterion:** ≥80% on the self-quiz or drill set for that session. If you score below 80%, repeat the session the next day before advancing.

---

## Topic × Interval Grid

| Topic | Day 1 (Study) | Day 3 (Recall) | Day 7 (Write) | Day 14 (Timed) | Day 30 (Mock) |
|-------|--------------|----------------|--------------|----------------|--------------|
| **L01 Variables** | `02_textbook/L01` + `03_drills/L1` Q1-3 | `03_drills/L1` Q4-6, self-quiz | Write 5 variable declarations from memory | `03_drills/L1` full set, ≤20 min | `05_mock-exams/mock-A` §1 |
| **L02 Operators** | `02_textbook/L02` + `03_drills/L2` Q1-3 | `03_drills/L2` Q4-6, trace expressions | Write operator precedence table + 3 examples | `03_drills/L2` full set, ≤20 min | `05_mock-exams/mock-A` §2 |
| **L03 Conditionals** | `02_textbook/L03` + `03_drills/L3` Q1-3 | `03_drills/L3` Q4-6, trace if/switch | Write if-else and switch from memory | `03_drills/L3` full set, ≤20 min | `05_mock-exams/mock-A` §3 |
| **L04 Loops ★** | `02_textbook/L04` + `03_drills/L4` Q1-4 | `03_drills/L4` Q5-8, trace loops | Write for/while/do-while from memory | `03_drills/L4` full set, ≤25 min | `05_mock-exams/mock-B` §1 |
| **L05 Arrays ★** | `02_textbook/L05` + `03_drills/L5` Q1-4 | `03_drills/L5` Q5-8, index tracing | Write 1D/2D array init + traversal | `03_drills/L5` full set, ≤25 min | `05_mock-exams/mock-B` §2 |
| **L06 Functions ★** | `02_textbook/L06` + `03_drills/L6` Q1-4 | `03_drills/L6` Q5-8, trace call stack | Write function with params + return | `03_drills/L6` full set, ≤25 min | `05_mock-exams/mock-B` §3 |
| **L07 Pointers ★** | `02_textbook/L07` + `03_drills/L7` Q1-4 | `03_drills/L7` Q5-8, draw memory diagram | Write pointer declaration + deref + arithmetic | `03_drills/L7` full set, ≤30 min | `05_mock-exams/mock-C` §1 |
| **L08 Strings** | `02_textbook/L08` + `03_drills/L8` Q1-3 | `03_drills/L8` Q4-6, trace string ops | Write strcmp/strcpy/strlen usage | `03_drills/L8` full set, ≤20 min | `05_mock-exams/mock-C` §2 |
| **L09 Structs** | `02_textbook/L09` | Re-read + write struct definition | Write struct + member access + array of structs | Timed struct problem ≤20 min | `05_mock-exams/mock-C` §3 |
| **L10 File I/O** | `02_textbook/L10` | Re-read + fopen/fclose trace | Write file read/write program | Timed File I/O problem ≤20 min | `05_mock-exams/mock-A` §4 |
| **L11 Recursion** | `02_textbook/L11` | Trace factorial/fibonacci by hand | Write recursive function from scratch | Timed recursion problem ≤25 min | `05_mock-exams/mock-B` §4 |

★ = Tier-1 priority topics (60% of exam weight)

---

## Session Checklists

### Day 1 — Initial Study
- [ ] Read the textbook chapter fully (`02_textbook/Lxx`)
- [ ] Work through Q1-4 of the drill set (`03_drills/Lx`)
- [ ] Write the key syntax rule from memory (no looking)
- [ ] Score yourself: count correct drill answers / total
- [ ] Record score in `06_progress/student-progress.md`
- [ ] Flag any question you got wrong as a weak point

### Day 3 — First Review (Recall)
- [ ] Without opening the textbook, write the syntax from memory
- [ ] Check against textbook — note any gaps
- [ ] Complete the mid-section drill questions
- [ ] Trace at least one code snippet by hand (output prediction)
- [ ] Score ≥80%? → continue. <80%? → re-read today, retry tomorrow

### Day 7 — Second Review (Write)
- [ ] Write a complete program from memory using this topic
- [ ] Compile mentally (check for syntax errors)
- [ ] Complete the full drill set under time pressure
- [ ] No hints, no references during writing phase
- [ ] Score ≥80%? → continue. <80%? → open `10_remediation/` for this topic

### Day 14 — Third Review (Timed + Mock Section)
- [ ] Complete the full drill set within the time limit in the grid
- [ ] Attempt the corresponding mock exam section (partial)
- [ ] Grade immediately and note wrong answers
- [ ] Update mastery % in `07_mastery/mastery-rubric.md`
- [ ] If mastery < 75% → schedule remediation session this week

### Day 30 — Fourth Review (Mock Routing)
- [ ] Attempt the full mock exam section listed in the grid
- [ ] Time yourself: simulate exam conditions (no notes, no hints)
- [ ] Record score in `06_progress/student-progress.md`
- [ ] If score < 70% → run full remediation plan (`10_remediation/`)
- [ ] If score ≥ 80% → mark topic as **Exam Ready** in mastery rubric

---

## Passing Thresholds by Session

| Session | Minimum Score | Action if Below Threshold |
|---------|--------------|--------------------------|
| Day 1   | ≥60%         | Re-read chapter; retry Q1-4 |
| Day 3   | ≥70%         | Redo Day 1 drills before Day 7 |
| Day 7   | ≥75%         | Open `10_remediation/` for topic |
| Day 14  | ≥75%         | Full remediation + extra drill session |
| Day 30  | ≥80%         | Full remediation + re-attempt mock section |

---

## Notes

- Tier-1★ topics (L04–L07) get +5 min time allowance due to complexity.
- Pointers (L07): always draw a memory-address diagram during Day 3 review.
- If a mock exam section covers multiple topics, route to the single weakest topic's remediation file first.
- Re-run `diagnostic-checklist.md` after Day 14 to recalibrate your weak-topic list.
