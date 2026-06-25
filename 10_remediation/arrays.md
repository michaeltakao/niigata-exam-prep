---
render_with_liquid: false
---

# Remediation: Arrays (L05) — Tier-1★

**Trigger**: Score < 50% on L05 drills, or Mastery Band ≤ 1 (Recognition).  
**Goal**: Reach Band 3 (Independent) — declare, initialize, pass, and traverse arrays from memory.

---

## Phase 1 — Concept Re-read

Reference: `02_textbook/L05` (re-read all sections before proceeding).

Key concepts to solidify:

| Concept | Syntax / Rule |
|---------|---------------|
| 1D declaration | `int a[5];` — 5 elements, indices 0–4 |
| Initialization | `int a[5] = {1, 2, 3, 4, 5};` or `int a[] = {1,2,3};` |
| Access | `a[0]` is first element; `a[n-1]` is last |
| 2D declaration | `int m[3][4];` — 3 rows, 4 columns |
| sizeof | `sizeof(a) / sizeof(a[0])` gives element count |
| Pass to function | Array decays to pointer: `void f(int arr[], int n)` |

**Critical rules**:
- Array indices start at **0**, not 1. `a[5]` on a 5-element array is **out-of-bounds** (undefined behavior).
- When passing an array to a function, the **size must be passed separately** — `sizeof` inside the function gives pointer size, not array size.

---

## Phase 2 — Traced Examples

### Example 1: Array Initialization and Access

```c
#include <stdio.h>
int main(void) {
    int a[5] = {10, 20, 30, 40, 50};
    int i;
    for (i = 0; i < 5; i++) {
        printf("a[%d] = %d\n", i, a[i]);
    }
    return 0;
}
```

**Memory layout** (after initialization):

| Index | 0  | 1  | 2  | 3  | 4  |
|-------|----|----|----|----|----|
| Value | 10 | 20 | 30 | 40 | 50 |

**Trace table**:

| i | a[i] | Output         |
|---|------|----------------|
| 0 | 10   | `a[0] = 10`    |
| 1 | 20   | `a[1] = 20`    |
| 2 | 30   | `a[2] = 30`    |
| 3 | 40   | `a[3] = 40`    |
| 4 | 50   | `a[4] = 50`    |
| 5 | —    | loop exits     |

---

### Example 2: Linear Search

```c
#include <stdio.h>
int main(void) {
    int a[6] = {4, 7, 2, 9, 1, 5};
    int target = 9, found = -1;
    int i;
    for (i = 0; i < 6; i++) {
        if (a[i] == target) {
            found = i;
            break;
        }
    }
    if (found >= 0)
        printf("Found at index %d\n", found);
    else
        printf("Not found\n");
    return 0;
}
```

**Trace table** (searching for 9):

| i | a[i] | a[i]==9? | Action      |
|---|------|----------|-------------|
| 0 | 4    | no       | continue    |
| 1 | 7    | no       | continue    |
| 2 | 2    | no       | continue    |
| 3 | 9    | **yes**  | found=3, break |

**Output**: `Found at index 3`

---

### Example 3: Array as Function Argument

```c
#include <stdio.h>

int sum(int arr[], int n) {
    int total = 0, i;
    for (i = 0; i < n; i++) {
        total += arr[i];
    }
    return total;
}

int main(void) {
    int data[4] = {3, 6, 2, 8};
    int result = sum(data, 4);
    printf("Sum = %d\n", result);
    return 0;
}
```

**Trace** (inside `sum` with arr={3,6,2,8}, n=4):

| i | arr[i] | total before | total after |
|---|--------|--------------|-------------|
| 0 | 3      | 0            | 3           |
| 1 | 6      | 3            | 9           |
| 2 | 2      | 9            | 11          |
| 3 | 8      | 11           | 19          |

**Output**: `Sum = 19`

**Key insight**: `data` is passed without brackets — the function receives the address of the first element.

---

### Example 4: 2D Array Traversal

{% raw %}
```c
#include <stdio.h>
int main(void) {
    int m[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int i, j;
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 3; j++) {
            printf("%d ", m[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```
{% endraw %}

**Memory layout** (row-major):

| Index | [0][0] | [0][1] | [0][2] | [1][0] | [1][1] | [1][2] |
|-------|--------|--------|--------|--------|--------|--------|
| Value | 1      | 2      | 3      | 4      | 5      | 6      |

**Trace table**:

| i | j | m[i][j] | Output     |
|---|---|---------|------------|
| 0 | 0 | 1       | `1 `       |
| 0 | 1 | 2       | `2 `       |
| 0 | 2 | 3       | `3 \n`     |
| 1 | 0 | 4       | `4 `       |
| 1 | 1 | 5       | `5 `       |
| 1 | 2 | 6       | `6 \n`     |

**Output**:
```
1 2 3 
4 5 6 
```

---

## Phase 3 — Scaffolded Drills

### Drill 1 (Fill-in-the-blank) — Declare, initialize, and print

```c
#include <stdio.h>
int main(void) {
    int scores[___] = {85, 92, 78, 95, 60};
    int i;
    for (i = 0; i < ___; i++) {
        printf("scores[%d] = %d\n", ___, ___);
    }
    return 0;
}
```

> Hint: 5 elements. The loop runs while i is less than the array size.

**Expected output**:
```
scores[0] = 85
scores[1] = 92
scores[2] = 78
scores[3] = 95
scores[4] = 60
```

---

### Drill 2 (Fill-in-the-blank) — Find maximum

```c
#include <stdio.h>
int main(void) {
    int a[5] = {3, 17, 8, 25, 11};
    int max = a[___];    /* start with first element */
    int i;
    for (i = 1; i < 5; i++) {
        if (a[i] ___ max) {
            max = ___;
        }
    }
    printf("Max = %d\n", max);
    return 0;
}
```

> Hint: Initialize max to `a[0]`. Replace max when current element is greater.

**Expected output**: `Max = 25`

---

### Drill 3 (Fix the bug) — Reverse an array

```c
#include <stdio.h>
int main(void) {
    int a[5] = {1, 2, 3, 4, 5};
    int i;
    for (i = 0; i <= 5; i++) {   /* BUG */
        printf("%d ", a[4 - i]);
    }
    printf("\n");
    return 0;
}
```

> Hint: When `i = 5`, what index does `a[4 - i]` compute? Is that valid?

**Expected output**: `5 4 3 2 1`

---

### Drill 4 (Fix the bug) — Function that doubles each element

```c
#include <stdio.h>

void double_all(int arr[], int n) {
    int i;
    for (i = 0; i < n; i++) {
        arr[i] = arr[i] + arr[i];
    }
}

int main(void) {
    int data[3] = {5, 10, 15};
    double_all(data);   /* BUG */
    int i;
    for (i = 0; i < 3; i++) {
        printf("%d ", data[i]);
    }
    printf("\n");
    return 0;
}
```

> Hint: The function signature requires two arguments. What is the second argument?

**Expected output**: `10 20 30`

---

### Drill 5 (Write from scratch) — Sum of a 2D array

Write a complete C program that declares `int grid[3][3]` initialized to:
```
1 2 3
4 5 6
7 8 9
```
Then compute and print the total sum of all elements.

> Hint: Use nested `for` loops with an accumulator `total = 0`.

**Expected output**: `Total = 45`

---

## Phase 4 — Exit Quiz

### MCQ (1 point each)

**Q1.** Given `int a[4] = {10, 20, 30, 40};`, what is `a[3]`?
- A) 30
- B) 40  ← correct
- C) out-of-bounds
- D) 0

**Q2.** Which declaration is valid for a 3-element array with values 1, 2, 3?
- A) `int a[3] = {1, 2, 3};`  ← correct
- B) `int a[3] = {1, 2, 3, 4};`
- C) `int a[0] = {1, 2, 3};`
- D) `int a{3} = [1, 2, 3];`

**Q3.** To find the number of elements using `sizeof`, you write:
- A) `sizeof(a)`
- B) `sizeof(a) * sizeof(a[0])`
- C) `sizeof(a) / sizeof(a[0])`  ← correct
- D) `sizeof(a[0])`

**Q4.** When an array is passed to a function `void f(int arr[], int n)`, modifying `arr[0]` inside `f`:
- A) has no effect on the original array
- B) modifies the original array  ← correct
- C) causes a compile error
- D) copies the array first

**Q5.** `int m[2][3]` has how many total elements?
- A) 2
- B) 3
- C) 5
- D) 6  ← correct

### Short Answer (2 points each)

**SA1.** Declare an integer array named `nums` of size 5, initialize it with values 10, 20, 30, 40, 50, and write a loop that prints each element.

*Model answer*:
```c
int nums[5] = {10, 20, 30, 40, 50};
int i;
for (i = 0; i < 5; i++) {
    printf("%d\n", nums[i]);
}
```

**SA2.** Write a function `int find_min(int arr[], int n)` that returns the minimum value in an array of `n` integers.

*Model answer*:
```c
int find_min(int arr[], int n) {
    int min = arr[0];
    int i;
    for (i = 1; i < n; i++) {
        if (arr[i] < min)
            min = arr[i];
    }
    return min;
}
```

---

## Graduation Criterion

- [ ] Exit quiz score ≥ 80% (≥ 7/9 points)
- [ ] At least 3 of 5 scaffolded drills answered correctly

When both boxes are checked, update `06_progress/student-progress.md`: set Arrays mastery to Band 3 (50%) and schedule next spaced-rep review in `08_schedule/review-schedule.md`.
