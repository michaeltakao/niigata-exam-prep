---
title: "Remediation: Loops (L04) — Tier-1★"
---

# Remediation: Loops (L04) — Tier-1★

**Trigger**: Score < 50% on L04 drills, or Mastery Band ≤ 1 (Recognition).  
**Goal**: Reach Band 3 (Independent) — write loop constructs from memory with reference.

---

## Phase 1 — Concept Re-read

Reference: `02_textbook/L04` (re-read all sections before proceeding).

Key concepts to solidify:

| Construct | Syntax | When to Use |
|-----------|--------|-------------|
| `for` | `for (init; condition; update)` | Known iteration count |
| `while` | `while (condition)` | Condition-driven, unknown count |
| `do-while` | `do { ... } while (condition);` | Must execute at least once |
| `break` | exits innermost loop immediately | Early exit on condition |
| `continue` | skips rest of current iteration | Skip specific cases |
| Nested loops | outer + inner | 2D traversal, multiplication tables |

**Critical rule**: The `for` loop header has three parts separated by semicolons — not commas.

---

## Phase 2 — Traced Examples

### Example 1: Counting Loop

```c
#include <stdio.h>
int main(void) {
    int i;
    for (i = 1; i <= 5; i++) {
        printf("%d\n", i);
    }
    return 0;
}
```

**Trace table**:

| Iteration | i (before test) | Condition `i<=5` | Output | i (after update) |
|-----------|-----------------|------------------|--------|-------------------|
| 1         | 1               | true             | 1      | 2                 |
| 2         | 2               | true             | 2      | 3                 |
| 3         | 3               | true             | 3      | 4                 |
| 4         | 4               | true             | 4      | 5                 |
| 5         | 5               | true             | 5      | 6                 |
| —         | 6               | false → exit     | —      | —                 |

**Output**: `1 2 3 4 5` (one per line)

---

### Example 2: Accumulator with while

```c
#include <stdio.h>
int main(void) {
    int sum = 0, i = 1;
    while (i <= 10) {
        sum += i;
        i++;
    }
    printf("Sum = %d\n", sum);
    return 0;
}
```

**Trace table** (abbreviated):

| i  | Condition | sum before | sum after |
|----|-----------|------------|-----------|
| 1  | true      | 0          | 1         |
| 2  | true      | 1          | 3         |
| 3  | true      | 3          | 6         |
| …  | …         | …          | …         |
| 10 | true      | 45         | 55        |
| 11 | false     | —          | 55        |

**Output**: `Sum = 55`

---

### Example 3: Nested Loop (Multiplication Table)

```c
#include <stdio.h>
int main(void) {
    int i, j;
    for (i = 1; i <= 3; i++) {
        for (j = 1; j <= 3; j++) {
            printf("%d ", i * j);
        }
        printf("\n");
    }
    return 0;
}
```

**Trace table**:

| i | j | i*j | Output event |
|---|---|-----|--------------|
| 1 | 1 | 1   | print `1 `   |
| 1 | 2 | 2   | print `2 `   |
| 1 | 3 | 3   | print `3 \n` |
| 2 | 1 | 2   | print `2 `   |
| 2 | 2 | 4   | print `4 `   |
| 2 | 3 | 6   | print `6 \n` |
| 3 | 1 | 3   | print `3 `   |
| 3 | 2 | 6   | print `6 `   |
| 3 | 3 | 9   | print `9 \n` |

**Output**:
```
1 2 3 
2 4 6 
3 6 9 
```

---

### Example 4: Early Exit with break

```c
#include <stdio.h>
int main(void) {
    int i;
    for (i = 1; i <= 10; i++) {
        if (i == 5) {
            break;
        }
        printf("%d\n", i);
    }
    printf("Loop ended at i = %d\n", i);
    return 0;
}
```

**Trace table**:

| i | Condition `i==5` | Action         | Output      |
|---|------------------|----------------|-------------|
| 1 | false            | print          | `1`         |
| 2 | false            | print          | `2`         |
| 3 | false            | print          | `3`         |
| 4 | false            | print          | `4`         |
| 5 | true             | break → exit   | (no print)  |

After loop: `Loop ended at i = 5`

**Key insight**: `i` retains its value after `break`. The loop did NOT reach `i = 6`.

---

## Phase 3 — Scaffolded Drills

### Drill 1 (Fill-in-the-blank) — Print even numbers 2 to 20

```c
#include <stdio.h>
int main(void) {
    int i;
    for (i = ___; i <= ___; i += ___) {
        printf("%d\n", i);
    }
    return 0;
}
```

> Hint: Start at 2, end at 20, step by 2.

**Expected output**: `2 4 6 8 10 12 14 16 18 20` (one per line)

---

### Drill 2 (Fill-in-the-blank) — Count down from 5 to 1

```c
#include <stdio.h>
int main(void) {
    int i = 5;
    while (___) {
        printf("%d\n", i);
        ___;
    }
    return 0;
}
```

> Hint: Condition keeps looping while i > 0. Don't forget to decrement.

**Expected output**: `5 4 3 2 1` (one per line)

---

### Drill 3 (Fix the bug) — Sum of 1 to N

The following code has a bug. Find and fix it.

```c
#include <stdio.h>
int main(void) {
    int i, sum = 0;
    for (i = 1; i < 10; i++) {   /* BUG HERE */
        sum += i;
    }
    printf("Sum 1..10 = %d\n", sum);
    return 0;
}
```

> Hint: Should sum 1 through 10 inclusive. What is the boundary condition?

**Expected output**: `Sum 1..10 = 55`

---

### Drill 4 (Fix the bug) — Print until negative

```c
#include <stdio.h>
int main(void) {
    int values[] = {3, 7, 2, -1, 5};
    int i;
    for (i = 0; i < 5; i++) {
        if (values[i] < 0)
            continue;   /* BUG: should be break */
        printf("%d\n", values[i]);
    }
    return 0;
}
```

> Hint: We want to STOP at the first negative, not skip it. Which keyword is correct?

**Expected output**: `3 7 2`

---

### Drill 5 (Write from scratch) — Multiplication table row

Write a complete C program that reads an integer `n` (assume 1 ≤ n ≤ 9) and prints the n-times table from n×1 to n×9.

> Hint: Use a single `for` loop. `printf("%d x %d = %d\n", n, j, n*j)` formats nicely.

**Expected output** (for n=3):
```
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
```

---

## Phase 4 — Exit Quiz

### MCQ (1 point each)

**Q1.** What is the output of the following code?
```c
int i;
for (i = 0; i < 3; i++) {
    printf("%d ", i);
}
```
- A) `0 1 2 3`
- B) `0 1 2`  ← correct
- C) `1 2 3`
- D) infinite loop

**Q2.** A `do-while` loop differs from a `while` loop because:
- A) it uses different syntax only
- B) the body always executes at least once  ← correct
- C) it cannot use `break`
- D) it counts down automatically

**Q3.** After `break` executes inside a `for` loop:
- A) the program terminates
- B) the update expression runs one more time
- C) execution jumps to the statement after the loop  ← correct
- D) the condition is re-evaluated

**Q4.** What does `continue` do?
- A) exits the loop entirely
- B) skips to the next iteration  ← correct
- C) restarts from `i = 0`
- D) calls the next function

**Q5.** How many times does `printf` execute?
```c
int i;
for (i = 10; i > 0; i -= 3) {
    printf("x");
}
```
- A) 10
- B) 3
- C) 4  ← correct (i = 10, 7, 4, 1 → then i=-2, condition false)
- D) infinite

### Short Answer (2 points each)

**SA1.** Write a `for` loop that prints integers 1 through 10, one per line.

*Model answer*:
```c
int i;
for (i = 1; i <= 10; i++) {
    printf("%d\n", i);
}
```

**SA2.** Write a `while` loop that sums all elements of `int arr[5] = {2, 4, 6, 8, 10}` and stores the result in `sum`.

*Model answer*:
```c
int arr[5] = {2, 4, 6, 8, 10};
int sum = 0, i = 0;
while (i < 5) {
    sum += arr[i];
    i++;
}
/* sum == 30 */
```

---

## Graduation Criterion

- [ ] Exit quiz score ≥ 80% (≥ 7/9 points)
- [ ] At least 3 of 5 scaffolded drills answered correctly

When both boxes are checked, update `06_progress/student-progress.md`: set Loops mastery to Band 3 (50%) and schedule next spaced-rep review in `08_schedule/review-schedule.md`.
