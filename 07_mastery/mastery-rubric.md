# Mastery Rubric — C Programming Topics

> **How to use:** After each drill or exercise, find your current band honestly. Use the "How to Advance" steps to move up. You must reach **75% (Independent)** on all Tier-1★ topics before attempting Mock Exam B. **100% (Exam-ready)** is required for full marks on exam-day.

---

## L01 — Variables & Data Types

| Band | Mastery % | Descriptor |
|------|-----------|-----------|
| Cannot identify syntax | 0% | Cannot name C primitive types; confuses `int`, `float`, `char`; does not know how to declare a variable |
| Recognition | 25% | Can read a declaration like `int x = 5;` and state its type and value; cannot write one from scratch |
| Guided | 50% | Given a fill-in-blank (`int ___ = 10;`), completes it correctly; needs prompts for `unsigned`, `long`, `const` |
| Independent | 75% | Declares variables of all primitive types from memory; correctly uses `sizeof`; knows implicit type conversion rules |
| Exam-ready | 100% | Writes, traces, and debugs programs involving type mismatch bugs, overflow, and `const` correctness without aids |

### How to Advance — L01
- **0% → 25%:** Read L01 textbook. Copy every declaration example by hand. Run each snippet in your head.
- **25% → 50%:** Do Drill L1 Easy set. For each problem, write the answer before checking.
- **50% → 75%:** Write 5 programs from scratch using mixed types. Time yourself: 2 min per variable set.
- **75% → 100%:** Given buggy code with type errors, find and fix all bugs without IDE hints.

---

## L02 — Operators & Expressions

| Band | Mastery % | Descriptor |
|------|-----------|-----------|
| Cannot identify syntax | 0% | Cannot distinguish `=` from `==`; does not know `%`, `++`, `--`, or bitwise operators |
| Recognition | 25% | Traces simple expressions (`x = 3 + 4 * 2`) with correct operator precedence; cannot write compound assignments |
| Guided | 50% | Completes fill-in-blank expressions with hints; uses `+=`, `-=` correctly when shown; needs help with `?:` ternary |
| Independent | 75% | Writes expressions with all arithmetic, relational, logical, and assignment operators from memory; applies precedence rules |
| Exam-ready | 100% | Evaluates complex expressions (mixed `&&`, `||`, bitwise, ternary) in one pass; spots short-circuit evaluation issues without aids |

### How to Advance — L02
- **0% → 25%:** Memorize the C operator precedence table. Trace 10 expressions by hand.
- **25% → 50%:** Drill L1 Medium — operator evaluation problems. Write out each step.
- **50% → 75%:** Write 5 expressions for each operator category from memory. Check with compiler.
- **75% → 100%:** Take timed problems (3 min each) with complex mixed-operator expressions. No reference.

---

## L03 — Conditionals (if / switch)

| Band | Mastery % | Descriptor |
|------|-----------|-----------|
| Cannot identify syntax | 0% | Cannot write a basic `if` statement; confuses braces with parentheses in condition |
| Recognition | 25% | Traces through an `if-else if-else` chain given values; identifies which branch executes |
| Guided | 50% | Completes a partial `switch` statement with hints; writes simple `if-else` with scaffolding |
| Independent | 75% | Writes multi-branch `if-else` and `switch` structures from memory; correctly handles fall-through in `switch` |
| Exam-ready | 100% | Writes, traces, and debugs conditionals including nested `if`, missing `break` in `switch`, and boundary edge cases without aids |

### How to Advance — L03
- **0% → 25%:** Read L03 textbook. Manually trace 5 programs; predict output before running.
- **25% → 50%:** Drill L1 Easy (conditional problems). Write each `if` or `switch` from scratch.
- **50% → 75%:** Implement a grade calculator and a day-of-week printer using `switch` — no looking.
- **75% → 100%:** Debug 3 programs with intentional logic errors in conditional branches. No hints.

---

## L04 — Loops (for / while / do-while) ★ Tier-1

| Band | Mastery % | Descriptor |
|------|-----------|-----------|
| Cannot identify syntax | 0% | Cannot write a `for` loop header; confuses loop variable initialization, condition, and increment |
| Recognition | 25% | Traces a loop manually and produces correct output; cannot write one; may confuse `while` and `do-while` |
| Guided | 50% | Completes fill-in-blank loops with init/condition/increment provided; writes `while` loop with scaffolding |
| Independent | 75% | Writes `for`, `while`, and `do-while` loops from memory; uses `break` and `continue` correctly; writes nested loops |
| Exam-ready | 100% | Writes, traces, and debugs loops including off-by-one errors, infinite loops, and nested-loop matrix traversals without aids |

### How to Advance — L04
- **0% → 25%:** Read L04 textbook. Trace a loop that prints 1–10 step by step on paper.
- **25% → 50%:** Drill L2 Easy. Write a loop for each problem before seeing the answer.
- **50% → 75%:** Write a multiplication table using nested `for` loops — no reference.
- **75% → 100%:** Debug 3 loop programs with off-by-one and boundary errors. Timed: 5 min each.
- **Route if stuck:** `10_remediation/loops.md`

---

## L05 — Arrays (1D & 2D) ★ Tier-1

| Band | Mastery % | Descriptor |
|------|-----------|-----------|
| Cannot identify syntax | 0% | Cannot declare an array; confuses `arr[5]` (declaration) with `arr[4]` (last valid index) |
| Recognition | 25% | Reads and traces array traversal code; identifies correct/out-of-bounds indices; cannot write from scratch |
| Guided | 50% | Completes fill-in-blank array initialization and loop traversal with hints; writes 1D array summation with scaffolding |
| Independent | 75% | Declares, initializes, and traverses 1D and 2D arrays from memory; passes arrays to functions correctly |
| Exam-ready | 100% | Writes sorting/searching algorithms on arrays, 2D matrix operations, and debugs off-by-one/out-of-bounds bugs without aids |

### How to Advance — L05
- **0% → 25%:** Read L05 textbook. Draw an array in memory with indices. Trace three array programs.
- **25% → 50%:** Drill L3 Easy. Write initialization and traversal for each problem first.
- **50% → 75%:** Write bubble sort and linear search from memory. Verify against reference.
- **75% → 100%:** Implement 2D matrix addition and transpose without any reference. Time: 10 min.
- **Route if stuck:** `10_remediation/arrays.md`

---

## L06 — Functions & Scope ★ Tier-1

| Band | Mastery % | Descriptor |
|------|-----------|-----------|
| Cannot identify syntax | 0% | Cannot write a function with a return type and parameters; confuses function declaration with definition |
| Recognition | 25% | Reads function definitions and traces calls with given arguments; identifies return values; cannot write one |
| Guided | 50% | Completes fill-in-blank function bodies with hints; writes a simple `int add(int a, int b)` with scaffolding |
| Independent | 75% | Writes functions with correct signatures, return types, and parameter passing from memory; understands local vs. global scope |
| Exam-ready | 100% | Writes, traces, and debugs programs with multiple interacting functions, pass-by-value vs. pass-by-pointer, and scope issues without aids |

### How to Advance — L06
- **0% → 25%:** Read L06 textbook. Trace 5 function calls step by step (draw the call stack).
- **25% → 50%:** Drill L4 Easy. Write each function signature and body before checking.
- **50% → 75%:** Refactor a 50-line program into 3 functions — no reference.
- **75% → 100%:** Write and debug a program using pass-by-pointer to swap two variables. No aids, timed.
- **Route if stuck:** `10_remediation/functions.md`

---

## L07 — Pointers & Memory ★ Tier-1

| Band | Mastery % | Descriptor |
|------|-----------|-----------|
| Cannot identify syntax | 0% | Cannot distinguish `*ptr` (dereference) from `ptr` (address); does not know what `&` does |
| Recognition | 25% | Reads pointer code and traces memory addresses; identifies what `*ptr` yields; cannot write pointer code |
| Guided | 50% | Completes fill-in-blank pointer declarations and dereferences with hints; draws memory diagrams when prompted |
| Independent | 75% | Declares pointers, assigns addresses with `&`, dereferences with `*`, and passes pointers to functions from memory |
| Exam-ready | 100% | Writes pointer arithmetic, pointer-to-array traversal, pass-by-pointer, and debugs dangling/null pointer errors without any aids |

### How to Advance — L07
- **0% → 25%:** Read L07 textbook. Draw a box-and-arrow diagram for every pointer example.
- **25% → 50%:** Drill L5 Easy. For each problem, draw the memory state before writing code.
- **50% → 75%:** Write a swap function using pointers from memory. Then write pointer-based array traversal.
- **75% → 100%:** Identify and fix 3 pointer bugs (NULL deref, dangling pointer, wrong dereference level). No hints, timed: 6 min each.
- **Route if stuck:** `10_remediation/pointers.md`

---

## L08 — Strings (char arrays)

| Band | Mastery % | Descriptor |
|------|-----------|-----------|
| Cannot identify syntax | 0% | Cannot declare a `char` array for a string; does not know about the null terminator `\0` |
| Recognition | 25% | Reads string manipulation code using `strlen`, `strcpy`, `strcmp`; traces output; cannot write string operations |
| Guided | 50% | Completes fill-in-blank `printf`/string function calls with hints; writes a string copy loop with scaffolding |
| Independent | 75% | Declares and manipulates strings from memory; uses standard library functions correctly; writes a manual `strlen` equivalent |
| Exam-ready | 100% | Writes string parsing, reversal, and comparison programs; debugs buffer overflows and missing null-terminator bugs without aids |

### How to Advance — L08
- **0% → 25%:** Read L08 textbook. Memorize: `strlen`, `strcpy`, `strcat`, `strcmp` signatures.
- **25% → 50%:** Drill L6 Easy (string problems). Write each function call from memory.
- **50% → 75%:** Write a string reversal and a word-count function without reference.
- **75% → 100%:** Debug a program with a buffer overflow and a missing `\0`. Time: 8 min. No aids.

---

## L09 — Structs

| Band | Mastery % | Descriptor |
|------|-----------|-----------|
| Cannot identify syntax | 0% | Cannot write a `struct` definition; does not know how to access member fields |
| Recognition | 25% | Reads a struct definition and field access (`student.name`); traces a program using structs; cannot define one |
| Guided | 50% | Completes fill-in-blank struct definition and member access with hints; creates one struct variable with scaffolding |
| Independent | 75% | Defines structs with multiple types, declares variables, accesses members, and passes structs to functions from memory |
| Exam-ready | 100% | Writes programs with arrays of structs, pointer-to-struct access (`ptr->field`), and debugs member misuse without aids |

### How to Advance — L09
- **0% → 25%:** Read L09 textbook. Define a `Student` struct by hand; draw its memory layout.
- **25% → 50%:** Drill L6 Medium (struct problems). Write each struct definition before checking.
- **50% → 75%:** Create an array of 5 `Student` structs with name + score. Sort by score.
- **75% → 100%:** Write a function accepting a pointer to a struct and modifying its fields. No reference.

---

## L10 — File I/O

| Band | Mastery % | Descriptor |
|------|-----------|-----------|
| Cannot identify syntax | 0% | Does not know `fopen`, `fclose`, `fprintf`, `fscanf`; cannot distinguish file reading from writing |
| Recognition | 25% | Reads file I/O code and traces what gets written/read; identifies mode strings (`"r"`, `"w"`, `"a"`); cannot write it |
| Guided | 50% | Completes fill-in-blank `fopen`/`fclose` calls with hints; writes a read loop with scaffolding |
| Independent | 75% | Opens, reads, writes, and closes files from memory; checks for NULL return from `fopen`; uses `feof` correctly |
| Exam-ready | 100% | Writes file-processing programs (copy, search, modify), handles edge cases (file not found, empty file), and debugs resource leaks without aids |

### How to Advance — L10
- **0% → 25%:** Read L10 textbook. Memorize the 4-step file pattern: open → check NULL → read/write → close.
- **25% → 50%:** Drill L7 Easy. Write each open/close pair before checking.
- **50% → 75%:** Write a program that reads numbers from a file and computes their sum — no reference.
- **75% → 100%:** Debug a program missing `fclose` and one with wrong mode string. Time: 6 min. No aids.

---

## L11 — Recursion

| Band | Mastery % | Descriptor |
|------|-----------|-----------|
| Cannot identify syntax | 0% | Cannot identify the base case or recursive call in a function; does not understand the call stack |
| Recognition | 25% | Traces a recursive function (e.g., factorial, Fibonacci) and produces correct output; cannot write one |
| Guided | 50% | Completes fill-in-blank recursive function with base case and recursive call provided as hints |
| Independent | 75% | Writes factorial, Fibonacci, and sum-of-array recursive functions from memory with correct base cases |
| Exam-ready | 100% | Writes, traces, and debugs recursive programs including tree-like recursion; identifies infinite recursion bugs; converts between iterative and recursive solutions without aids |

### How to Advance — L11
- **0% → 25%:** Read L11 textbook. Draw the call stack for `factorial(4)` step by step.
- **25% → 50%:** Drill L8 Easy. For each problem, identify base case and recursive step before writing.
- **50% → 75%:** Write factorial and Fibonacci from scratch without reference. Draw the call stack.
- **75% → 100%:** Write a recursive linear search and debug a recursive function with a missing base case. No aids, timed: 8 min.

---

## Summary: Mastery Band Reference

| Band | % | What you can do |
|------|---|----------------|
| Cannot identify | 0% | Cannot read or write the syntax |
| Recognition | 25% | Read & trace only |
| Guided | 50% | Fill-in-blank with hints |
| Independent | 75% | Write from memory, reference allowed |
| Exam-ready | 100% | Write + trace + debug, no aids |

**Exam-day minimum:** Independent (75%) on all topics; Exam-ready (100%) on Tier-1★ (Loops, Arrays, Functions, Pointers).
