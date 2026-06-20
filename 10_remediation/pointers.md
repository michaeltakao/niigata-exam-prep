# Remediation: Pointers (L07) — Tier-1★

**Trigger**: Score < 50% on L07 drills, or Mastery Band ≤ 1 (Recognition).  
**Goal**: Reach Band 3 (Independent) — declare, dereference, and pass pointers from memory.  
**Note**: Graduation threshold is 70% (lower than other Tier-1 topics due to inherent difficulty).

---

## Phase 1 — Concept Re-read

Reference: `02_textbook/L07` (re-read all sections before proceeding).

Key concepts to solidify:

| Concept | Syntax | Meaning |
|---------|--------|---------|
| Address-of | `&x` | The memory address where `x` is stored |
| Pointer declaration | `int *p;` | `p` holds the address of an `int` |
| Assignment | `p = &x;` | Store address of `x` in `p` |
| Dereference | `*p` | Value stored at the address `p` holds |
| Pointer arithmetic | `p + 1` | Address of the next `int` (advances by `sizeof(int)` bytes) |
| Array / pointer | `a[i]` ≡ `*(a + i)` | Array name is address of first element |
| NULL pointer | `int *p = NULL;` | Pointer that points to nothing (safe sentinel) |

**Critical rules**:
- `*` in a **declaration** means "this is a pointer". `*` in an **expression** means "dereference".
- Always initialize pointers before dereferencing. An uninitialized pointer causes undefined behavior.
- `NULL` dereferencing crashes the program. Always check before use in real code.

---

## Phase 2 — Memory Diagram Reference

Read these diagrams carefully — they are the mental model for all pointer operations.

### Diagram A: Basic Pointer

```c
int x = 5;
int *p = &x;
```

```
Address: [0x1000]      [0x1004]
Value:   [  5   ]      [0x1000]
Name:       x              p
```

- `x` lives at address `0x1000`, its value is `5`.
- `p` lives at address `0x1004`, its value is `0x1000` (the address of `x`).

### Diagram B: Dereferencing

```c
int x = 5;
int *p = &x;
*p = 99;       /* changes x via p */
```

```
Before *p = 99:           After *p = 99:
[0x1000]: 5               [0x1000]: 99
[0x1004]: 0x1000          [0x1004]: 0x1000

p still points to x; x's value changed.
```

### Diagram C: Pointer Increment

```c
int a[3] = {10, 20, 30};
int *p = a;       /* p points to a[0] */
p++;              /* p now points to a[1] */
```

```
Index:   [0]    [1]    [2]
Address: [0x100][0x104][0x108]
Value:   [ 10 ] [ 20 ] [ 30 ]

Before p++:  p = 0x100  (*p == 10)
After  p++:  p = 0x104  (*p == 20)
```

Pointer arithmetic is in units of the pointed-to type — `int *` advances by `sizeof(int)` = 4 bytes per `++`.

### Diagram D: Pointer to Array Element

```c
int a[4] = {5, 15, 25, 35};
int *p = &a[2];   /* p points to a[2] */
```

```
Index:   [0]    [1]    [2]    [3]
Value:   [ 5 ] [ 15 ] [ 25 ] [ 35 ]
                  ↑
                  p (0x108 if a starts at 0x100)
*p == 25, *(p+1) == 35, *(p-1) == 15
```

### Diagram E: Swap via Pointers

```c
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
int x = 3, y = 7;
swap(&x, &y);
```

```
Before swap:                 After swap:
x: [3]  ← *a                x: [7]  ← *a
y: [7]  ← *b                y: [3]  ← *b

a holds &x, b holds &y.
temp = *a = 3
*a = *b → x becomes 7
*b = temp → y becomes 3
```

---

## Phase 3 — Traced Examples

### Example 1: Pointer Basics

```c
#include <stdio.h>
int main(void) {
    int x = 42;
    int *p = &x;
    printf("x = %d\n", x);
    printf("&x = %p\n", (void *)&x);
    printf("p = %p\n", (void *)p);
    printf("*p = %d\n", *p);
    return 0;
}
```

**Trace + Memory Diagram**:

```
Step 1: int x = 42
  [0x2000]: 42   (x)

Step 2: int *p = &x
  [0x2004]: 0x2000  (p)

Step 3: printf("%d", x)    → 42
Step 4: printf("%p", &x)   → 0x2000
Step 5: printf("%p", p)    → 0x2000  (same as &x)
Step 6: printf("%d", *p)   → 42      (value at address 0x2000)
```

**Key insight**: `p` and `&x` print the same address. `*p` and `x` print the same value.

---

### Example 2: Pointer Arithmetic

```c
#include <stdio.h>
int main(void) {
    int a[3] = {100, 200, 300};
    int *p = a;
    int i;
    for (i = 0; i < 3; i++) {
        printf("*(p+%d) = %d\n", i, *(p + i));
    }
    return 0;
}
```

**Trace table**:

| i | p + i (address) | *(p+i) | Output           |
|---|-----------------|--------|------------------|
| 0 | 0x1000          | 100    | `*(p+0) = 100`   |
| 1 | 0x1004          | 200    | `*(p+1) = 200`   |
| 2 | 0x1008          | 300    | `*(p+2) = 300`   |

**Memory diagram during loop**:

```
a[0]@0x1000  a[1]@0x1004  a[2]@0x1008
[  100     ] [  200     ] [  300     ]
 ↑ p+0         ↑ p+1         ↑ p+2
```

---

### Example 3: Swap Function (Correct)

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int x = 3, y = 7;
    printf("Before: x=%d, y=%d\n", x, y);
    swap(&x, &y);
    printf("After:  x=%d, y=%d\n", x, y);
    return 0;
}
```

**Step-by-step memory diagram** (inside `swap`):

```
Main's variables:   x=3 @0x300,  y=7 @0x304
swap parameters:    a=0x300,     b=0x304

Step 1: temp = *a  → temp = 3
Step 2: *a = *b    → x (at 0x300) becomes 7
Step 3: *b = temp  → y (at 0x304) becomes 3

After return: x=7, y=3
```

**Output**:
```
Before: x=3, y=7
After:  x=7, y=3
```

---

### Example 4: Array Traversal via Pointer

```c
#include <stdio.h>
int main(void) {
    int a[4] = {1, 3, 5, 7};
    int *p;
    for (p = a; p < a + 4; p++) {
        printf("%d\n", *p);
    }
    return 0;
}
```

**Trace table**:

| p (address) | p < a+4? | *p | Output |
|-------------|----------|----|--------|
| a+0 = 0x100 | yes      | 1  | `1`    |
| a+1 = 0x104 | yes      | 3  | `3`    |
| a+2 = 0x108 | yes      | 5  | `5`    |
| a+3 = 0x10C | yes      | 7  | `7`    |
| a+4 = 0x110 | no       | —  | exit   |

**Memory diagram** (at loop start):

```
a[0]  a[1]  a[2]  a[3]
[ 1 ] [ 3 ] [ 5 ] [ 7 ]
  ↑
  p (initially p = a)
```

---

## Phase 4 — Scaffolded Drills (with Memory Diagram Blanks)

### Drill 1 (Fill-in-the-blank + diagram) — Declare a pointer

```c
#include <stdio.h>
int main(void) {
    int n = 10;
    int ___ ptr = ___;     /* declare pointer to n */
    printf("%d\n", ___);   /* print value via pointer */
    return 0;
}
```

Draw the memory diagram after `int *ptr = &n;`:

```
Address: [______]      [______]
Value:   [______]      [______]
Name:      n             ptr
```

> Hint: `*` declares a pointer type; `&` takes the address.

**Expected output**: `10`

---

### Drill 2 (Fill-in-the-blank + diagram) — Increment pointer

```c
#include <stdio.h>
int main(void) {
    int a[3] = {10, 20, 30};
    int *p = a;
    p___;          /* advance to a[1] */
    printf("%d\n", ___);  /* print a[1] via p */
    return 0;
}
```

Draw the memory diagram before and after `p++`:

```
Before p++:
a[0]     a[1]     a[2]
[ 10 ]  [ 20 ]  [ 30 ]
  ↑
  p

After p++:
a[0]     a[1]     a[2]
[ 10 ]  [ 20 ]  [ 30 ]
           ↑
           p
```

> Hint: `p++` moves the pointer forward by one `int`.

**Expected output**: `20`

---

### Drill 3 (Fill-in-the-blank + diagram) — Dereference to modify

```c
#include <stdio.h>
int main(void) {
    int x = 5;
    int *p = &x;
    ___ = 99;      /* change x's value through p */
    printf("%d\n", x);
    return 0;
}
```

Draw the memory diagram after the modification:

```
Address: [0x1000]      [0x1004]
Value:   [______]      [0x1000]
Name:       x              p
```

**Expected output**: `99`

---

### Drill 4 (Write from scratch + diagram) — Pass by pointer to double a value

Write a complete function `void double_val(int *p)` that doubles the value at the address `p`, and a `main` that tests it with `int x = 6`.

Expected output: `12`

Draw the memory diagram showing the before/after state of `x`.

*Model answer structure:*
```
Before double_val(&x):
[0x200]: 6   (x)

After double_val(&x):
[0x200]: 12  (x)
```

> Hint: Inside the function, use `*p = *p * 2;` or `*p *= 2;`.

---

### Drill 5 (Write from scratch + diagram) — Print array via pointer

Write a complete C program that uses a pointer (not index `[]`) to print each element of `int a[5] = {2, 4, 6, 8, 10}`.

Draw the memory diagram showing how the pointer `p` moves through the array.

> Hint: Initialize `p = a;`, loop while `p < a + 5;`, use `p++` and `*p`.

**Expected output**: `2 4 6 8 10` (one per line)

---

## Phase 5 — Exit Quiz

### MCQ (1 point each)

**Q1.** Given `int x = 7; int *p = &x;`, what is `*p`?
- A) the address of x
- B) 7  ← correct
- C) the address of p
- D) undefined

**Q2.** After `int a[3] = {1,2,3}; int *p = a; p++;`, what does `*p` equal?
- A) 1
- B) 2  ← correct
- C) 3
- D) address of a[1]

**Q3.** `*` in `int *p;` means:
- A) multiply p by something
- B) p is a pointer to int  ← correct
- C) dereference p
- D) p equals int

**Q4.** What happens if you dereference a NULL pointer?
- A) returns 0
- B) returns the address 0
- C) undefined behavior / program crash  ← correct
- D) automatically initializes the variable

**Q5.** To pass `int x` to a function so the function can modify it, you call:
- A) `f(x)`
- B) `f(*x)`
- C) `f(&x)`  ← correct
- D) `f(x[])`

### Short Answer (2 points each)

**SA1.** Write a complete `swap` function using pointers that correctly swaps two integers. Show the function signature and body.

*Model answer*:
```c
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
```

**SA2.** Draw the memory diagram for the following code after both lines execute:
```c
int x = 42;
int *p = &x;
```

*Model answer*:
```
Address: [0x1000]      [0x1004]
Value:   [  42  ]      [0x1000]
Name:       x              p

p holds the address of x.
*p gives 42. &p gives 0x1004.
```

**SA3.** What is a NULL pointer? Why is it useful? Give a one-line example of setting a pointer to NULL.

*Model answer*:
> A NULL pointer holds the value `0` (or `(void*)0`) and points to no valid memory location. It is useful as a "no value" sentinel — functions return NULL on failure, and code can test `if (p == NULL)` before dereferencing. Example: `int *p = NULL;`

---

## Graduation Criterion

- [ ] Exit quiz score ≥ 70% (≥ 9/13 points — note lower threshold)
- [ ] At least 3 of 5 scaffolded drills answered correctly **including at least one memory diagram**

When both boxes are checked, update `06_progress/student-progress.md`: set Pointers mastery to Band 3 (50%) and schedule next spaced-rep review in `08_schedule/review-schedule.md`.

> **After pointers**: If targeting Band 4+, practice pointer-to-array problems in `03_drills/L7` and the pointer section of mock exam A.
