# Remediation: Functions (L06) — Tier-1★

**Trigger**: Score < 50% on L06 drills, or Mastery Band ≤ 1 (Recognition).  
**Goal**: Reach Band 3 (Independent) — declare, define, and call functions from memory.

---

## Phase 1 — Concept Re-read

Reference: `02_textbook/L06` (re-read all sections before proceeding).

Key concepts to solidify:

| Concept | Syntax / Rule |
|---------|---------------|
| Prototype | `int square(int x);` — declared before `main`, defines signature |
| Definition | `int square(int x) { return x * x; }` — the actual code |
| Return type | `int`, `double`, `void` — must match `return` statement |
| `void` function | no return value; use for side-effect functions |
| Pass by value | C always copies arguments — callee cannot modify caller's variable |
| Scope | local variables inside `{}` are not visible outside |
| Call | `int r = square(5);` — passes value 5, stores returned value |

**Critical rules**:
- If you call a function before defining it, you **must** provide a prototype.
- C passes arguments **by value** — a function cannot change the caller's variable unless a pointer is passed.
- `return` in a `void` function is written as `return;` or omitted.

---

## Phase 2 — Traced Examples

### Example 1: Simple Return-Value Function

```c
#include <stdio.h>

int square(int x) {
    return x * x;
}

int main(void) {
    int a = 4;
    int result = square(a);
    printf("square(%d) = %d\n", a, result);
    return 0;
}
```

**Trace table** (call `square(4)`):

| Step | Location | Variable | Value | Notes |
|------|----------|----------|-------|-------|
| 1    | main     | a        | 4     | declared |
| 2    | call     | x (copy) | 4     | argument copied into `x` |
| 3    | square   | x * x    | 16    | computed |
| 4    | return   | —        | 16    | value returned to caller |
| 5    | main     | result   | 16    | stored |

**Output**: `square(4) = 16`

---

### Example 2: void Function with Side Effects

```c
#include <stdio.h>

void print_line(int n) {
    int i;
    for (i = 0; i < n; i++) {
        printf("-");
    }
    printf("\n");
}

int main(void) {
    print_line(5);
    printf("Hello\n");
    print_line(5);
    return 0;
}
```

**Trace**:

| Step | Call           | Effect           |
|------|----------------|------------------|
| 1    | `print_line(5)` | prints `-----\n` |
| 2    | `printf`       | prints `Hello\n` |
| 3    | `print_line(5)` | prints `-----\n` |

**Output**:
```
-----
Hello
-----
```

**Key insight**: `void` functions use `printf` or modify global/pointer state — they do not `return` a value.

---

### Example 3: Function Calling Another Function

```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int sum_three(int x, int y, int z) {
    return add(add(x, y), z);
}

int main(void) {
    printf("%d\n", sum_three(2, 3, 5));
    return 0;
}
```

**Trace** (call `sum_three(2, 3, 5)`):

| Step | Expression       | Value | Notes |
|------|------------------|-------|-------|
| 1    | `add(2, 3)`      | 5     | inner call |
| 2    | `add(5, 5)`      | 10    | outer call, using result of step 1 |
| 3    | `return 10`      | 10    | returned to main |

**Output**: `10`

---

### Example 4: Recursive Call — Preview (details in L11)

```c
#include <stdio.h>

int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);  /* calls itself */
}

int main(void) {
    printf("4! = %d\n", factorial(4));
    return 0;
}
```

**Abbreviated call stack**:

```
factorial(4)
  → 4 * factorial(3)
        → 3 * factorial(2)
              → 2 * factorial(1)
                    → 1   (base case)
              → 2 * 1 = 2
        → 3 * 2 = 6
  → 4 * 6 = 24
```

**Output**: `4! = 24`

> This is a preview. For full recursion mastery, complete `10_remediation/` after finishing L11 or see `02_textbook/L11`.

---

## Phase 3 — Scaffolded Drills

### Drill 1 (Fill-in-the-blank) — Write square()

```c
#include <stdio.h>

___ square(___ x) {
    return ___;
}

int main(void) {
    printf("%d\n", square(7));
    return 0;
}
```

> Hint: The function takes one integer and returns its square. Return type matches input type.

**Expected output**: `49`

---

### Drill 2 (Fill-in-the-blank) — Demonstrate pass-by-value limitation

```c
#include <stdio.h>

void try_swap(int a, int b) {
    int temp = a;
    a = ___;
    b = ___;
    printf("Inside: a=%d, b=%d\n", a, b);
}

int main(void) {
    int x = 3, y = 7;
    try_swap(x, y);
    printf("Outside: x=%d, y=%d\n", x, y);
    return 0;
}
```

> Hint: The swap works on local copies. What do you expect the "Outside" line to print?

**Expected output**:
```
Inside: a=7, b=3
Outside: x=3, y=7
```

*(Note: the original variables are unchanged — this is the key learning point.)*

---

### Drill 3 (Fix the bug) — Max of two numbers

```c
#include <stdio.h>

int max(int a, int b) {
    if (a > b)
        return a;
    return b;
}

int main(void) {
    int result;
    result = max(10, 25)
    printf("Max = %d\n", result);  /* BUG */
    return 0;
}
```

> Hint: Look for a missing punctuation mark in `main`.

**Expected output**: `Max = 25`

---

### Drill 4 (Fix the bug) — Iterative factorial

```c
#include <stdio.h>

int factorial(int n) {
    int result = 1, i;
    for (i = 1; i <= n; i++) {
        result *= i;
    }
}   /* BUG */

int main(void) {
    printf("5! = %d\n", factorial(5));
    return 0;
}
```

> Hint: The function declares `int factorial(int n)` but is missing something at the end.

**Expected output**: `5! = 120`

---

### Drill 5 (Write from scratch) — Modular program: greet

Write a complete C program with:
1. A `void` function `print_greeting(char name[])` that prints `Hello, <name>!`
2. A `main` that calls it twice with `"Alice"` and `"Bob"`.

> Hint: Use `printf("Hello, %s!\n", name);` inside the function. Declare the function before `main`.

**Expected output**:
```
Hello, Alice!
Hello, Bob!
```

---

## Phase 4 — Exit Quiz

### MCQ (1 point each)

**Q1.** A function prototype `double area(double r);` tells the compiler:
- A) where the function is defined
- B) the function's name, parameter type, and return type  ← correct
- C) how many times the function is called
- D) the function's address in memory

**Q2.** What is the return type of `void greet(void)`?
- A) `int`
- B) a pointer
- C) nothing is returned  ← correct
- D) `char`

**Q3.** In C, function arguments are passed:
- A) by reference (the function modifies the original)
- B) by value (the function gets a copy)  ← correct
- C) by pointer automatically
- D) by global variable

**Q4.** A variable declared inside a function is:
- A) visible to all functions
- B) visible only within that function (local scope)  ← correct
- C) stored in the heap
- D) automatically initialized to 0

**Q5.** Which is the correct way to call `int add(int a, int b)` and store the result?
- A) `add(3, 4);`
- B) `int r; add(3, 4, r);`
- C) `int r = add(3, 4);`  ← correct
- D) `int r = add{3, 4};`

### Short Answer (2 points each)

**SA1.** Write a function prototype AND definition for a function named `abs_val` that takes one `int` and returns its absolute value (positive version).

*Model answer*:
```c
/* Prototype */
int abs_val(int x);

/* Definition */
int abs_val(int x) {
    if (x < 0)
        return -x;
    return x;
}
```

**SA2.** Write a function `int array_sum(int arr[], int n)` that returns the sum of all elements in `arr`.

*Model answer*:
```c
int array_sum(int arr[], int n) {
    int total = 0, i;
    for (i = 0; i < n; i++) {
        total += arr[i];
    }
    return total;
}
```

---

## Graduation Criterion

- [ ] Exit quiz score ≥ 80% (≥ 7/9 points)
- [ ] At least 3 of 5 scaffolded drills answered correctly

When both boxes are checked, update `06_progress/student-progress.md`: set Functions mastery to Band 3 (50%) and schedule next spaced-rep review in `08_schedule/review-schedule.md`.
