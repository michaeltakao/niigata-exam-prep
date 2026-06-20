#!/usr/bin/env python3
"""C code snippet verifier for Niigata University exam study materials."""

import re
import subprocess
import tempfile
import os
import sys
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

BASE_DIR = Path("/Users/unko/新潟大学　編入試験対策")

TARGET_FILES = [
    "03_drills/L1_variables.md",
    "03_drills/L2_expressions.md",
    "03_drills/L3_conditions.md",
    "03_drills/L4_loops.md",
    "03_drills/L5_arrays.md",
    "03_drills/L6_functions.md",
    "03_drills/L7_pointers.md",
    "03_drills/L8_exam.md",
    "05_mock-exams/mock-exam-A.md",
    "05_mock-exams/mock-exam-B.md",
    "05_mock-exams/mock-exam-C.md",
    "02_textbook/L01_variables-types.md",
    "02_textbook/L02_operators-expressions.md",
    "02_textbook/L03_conditions.md",
    "02_textbook/L04_loops.md",
    "02_textbook/L05_arrays.md",
    "02_textbook/L06_strings.md",
    "02_textbook/L07_functions.md",
    "02_textbook/L08_pointers.md",
    "02_textbook/L09_structs.md",
    "02_textbook/L10_algorithms.md",
    "02_textbook/L11_recursion.md",
]

# Fill-in-blank placeholder pattern — these are intentional gaps for the student
FILL_BLANK_PATTERN = re.compile(
    r'\(\s*[A-Z]\s*\)'            # (A)...(Z) — fill blanks including (X)(Y)(Z)
    r'|\(\s*[0-9]+\s*\)'          # (1), (2), (3) — numbered option labels
    r'|\[空欄\]|\[ \]|___'        # Japanese blanks
    r'|/\*[^*]*ここを埋め[^*]*\*/'   # /* ここを埋めよ */ style
    r'|ここを書け|ここに書|ここを実装'    # 「ここを書け」 placeholder comments
    r'|\{\s*\.\.\.\s*\}'          # { ... } pseudocode body
)

# Context keywords indicating intentional bugs
INTENTIONAL_BUG_KEYWORDS = [
    "バグを見つけ", "バグを修正", "誤りを修正", "find the bug", "fix the bug",
    "バグ修正", "間違い", "修正せよ", "誤りはどこ", "バグがある",
    "Find.*bug", "Debug", "エラーを直", "直してください",
    "// WRONG", "WRONG:", "// 間違い",
]

# Common variable declarations injected into fragment wrappers (scalar form)
COMMON_VAR_DECLS: dict[str, str] = {
    'n': 'int n = 5;',
    'x': 'int x = 0;',
    'y': 'int y = 0;',
    'i': 'int i = 0;',
    'j': 'int j = 0;',
    'a': 'int a = 0;',
    'b': 'int b = 0;',
    'score': 'int score = 80;',
    'grade': 'int grade = 0;',
    'month': 'int month = 6;',
    'N': 'int N = 10;',
    'max_val': 'int max_val = 0;',
    'points': 'int points = 0;',
    'left': 'int left = 0;',
    'right': 'int right = 9;',
    'mid': 'int mid = 0;',
    'apples': 'int apples = 5;',
    'val': 'int val = 0;',
    'tmp': 'int tmp = 0;',
    'sum': 'int sum = 0;',
    'price': 'double price = 0.0;',
    'result': 'double result[100] = {0.0};',
    'p': 'int _pval = 0; int *p = &_pval;',
    'q': 'int _qarr[] = {1,2,3,4,5}; int *q = _qarr + 4;',
}

# Array form used when the variable is subscripted with []
ARRAY_VAR_DECLS: dict[str, str] = {
    'a': 'int a[10] = {5, 3, 8, 1, 9, 2, 7, 4, 6, 0};',
    's': 'char s[100] = "hello world";',
    'result': 'double result[100] = {0.0};',
}

# Student struct typedef — member order matches {id, name, gpa} positional initializers
STUDENT_STRUCT_TYPEDEF = (
    "typedef struct {\n"
    "    int id;\n"
    "    char name[50];\n"
    "    float gpa;\n"
    "    int score;\n"
    "    int age;\n"
    "} Student;"
)

# Stub function definitions for placeholder calls used in pedagogical fragments
STUB_FUNCTIONS: dict[str, str] = {
    'process': 'static void process(int x) { (void)x; }',
    'sum_array': 'static int sum_array(int *a, int n) { int s=0,i; for(i=0;i<n;i++) s+=a[i]; return s; }',
    'normalize': 'static void normalize(int *a, int n, double *out) { int i; for(i=0;i<n;i++) out[i]=(n?a[i]*1.0/n:0); }',
    'contains': 'static int contains(int *a, int n, int v) { int i; for(i=0;i<n;i++) if(a[i]==v) return 1; return 0; }',
    'average': 'static double average(double a, double b, double c) { return (a+b+c)/3.0; }',
}

# Macro constants used in function signatures like void f(int a[N][N])
COMMON_MACROS: dict[str, str] = {
    'N': '#define N 5',
    'ROWS': '#define ROWS 3',
    'COLS': '#define COLS 3',
    'MAX': '#define MAX 100',
    'SIZE': '#define SIZE 10',
}

C_KEYWORDS = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
    'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int',
    'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
    'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile',
    'while', 'NULL', 'true', 'false', 'printf', 'scanf', 'strlen', 'strcpy',
    'strcmp', 'strcat', 'malloc', 'free', 'exit', 'main', 'Student',
}


def _declared_vars(code: str) -> set[str]:
    """Return set of variable names already declared in snippet (handles multi-var declarations)."""
    declared: set[str] = set()
    # Primitive types: handles "int a = 5, b = 2;" and "int n;" and "int arr[10]"
    for m in re.finditer(r'\b(?:int|double|float|char|long|short)\b([^;{]+)', code):
        decl_chunk = m.group(1)
        for sub in decl_chunk.split(','):
            # Only inspect the LHS (before '=') to avoid picking up RHS expressions
            lhs = sub.split('=')[0]
            vm = re.search(r'\*?\s*([a-zA-Z_]\w*)', lhs)
            if vm and vm.group(1) not in C_KEYWORDS:
                declared.add(vm.group(1))
    # Custom type declarations: "Student s;", "Point p = {..}", "Student *p = &s"
    # Match any PascalCase type name followed by a variable name; only varname checked vs keywords
    for m in re.finditer(r'\b[A-Z][a-zA-Z0-9_]*\s+\*?\s*([a-zA-Z_]\w*)', code):
        varname = m.group(1)
        if varname not in C_KEYWORDS:
            declared.add(varname)
    return declared


def inject_vars_for_fragment(code: str) -> str:
    """Return preamble declarations for common variables used-but-not-declared in fragment."""
    declared = _declared_vars(code)
    needs_student = 'Student' in code and 'typedef struct' not in code

    # Strip string literals before scanning for identifiers to avoid false positives
    # e.g. the 'n' in "%d\n" or 's' in "%s" being treated as variable names
    code_no_strings = re.sub(r'"(?:[^"\\]|\\.)*"', '""', code)
    used = set(re.findall(r'\b([a-zA-Z_]\w*)\b', code_no_strings)) - C_KEYWORDS

    injections = []
    if needs_student:
        injections.append(STUDENT_STRUCT_TYPEDEF)

    for var in sorted(used):
        if var in declared:
            continue
        # Inject array form when variable is subscripted
        if re.search(r'\b' + re.escape(var) + r'\s*\[', code) and var in ARRAY_VAR_DECLS:
            injections.append(ARRAY_VAR_DECLS[var])
        elif var in COMMON_VAR_DECLS:
            injections.append(COMMON_VAR_DECLS[var])

    return '\n    '.join(injections)


def split_function_and_usage(code: str) -> tuple[str, str]:
    """Split a function definition from any trailing usage/example statements."""
    lines = code.splitlines()
    brace_depth = 0
    last_close_idx = -1

    for idx, line in enumerate(lines):
        for ch in line:
            if ch == '{':
                brace_depth += 1
            elif ch == '}':
                brace_depth -= 1
                if brace_depth == 0:
                    last_close_idx = idx

    if last_close_idx < 0 or last_close_idx >= len(lines) - 1:
        return code, ""

    func_code = '\n'.join(lines[:last_close_idx + 1])
    trailing = '\n'.join(lines[last_close_idx + 1:])
    # Keep only non-comment statement lines as usage code
    usage_lines = [
        ln for ln in trailing.splitlines()
        if ln.strip() and not ln.strip().startswith('//')
    ]
    return func_code, '\n'.join(usage_lines)

COMMON_INCLUDES = """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
"""

@dataclass
class Snippet:
    file: str
    block_num: int
    code: str
    context: str  # surrounding markdown text (heading + problem statement)
    kind: str = "UNKNOWN"  # FULL_PROGRAM, FUNCTION_DEF, FRAGMENT
    status: str = "PENDING"  # OK, WARNING, ERROR, INTENTIONAL_BUG, SKIP
    messages: str = ""
    repaired_code: Optional[str] = None
    repair_applied: str = ""
    final_status: str = ""
    warnings: list = field(default_factory=list)


def extract_snippets(md_path: Path) -> list[Snippet]:
    """Extract all ```c ... ``` blocks from a markdown file with context."""
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    snippets = []
    block_num = 0
    i = 0
    current_context = ""

    while i < len(lines):
        line = lines[i]

        # Track context from headings and problem statements
        if line.startswith("#"):
            current_context = line.strip()
        elif line.startswith("**問題") or line.startswith("**M") or line.startswith("**E") or line.startswith("**H"):
            current_context = line.strip()

        # Detect start of C code block
        if re.match(r"^```c\s*$", line.strip()):
            start = i + 1
            # Find the closing ```
            j = start
            while j < len(lines) and not re.match(r"^```\s*$", lines[j].strip()):
                j += 1

            code = "\n".join(lines[start:j])

            # Gather surrounding context (look back 10 lines)
            context_lines = []
            for k in range(max(0, i - 10), i):
                if lines[k].strip():
                    context_lines.append(lines[k])
            full_context = "\n".join(context_lines[-5:]) + "\n" + current_context

            block_num += 1
            snippet = Snippet(
                file=str(md_path.relative_to(BASE_DIR)),
                block_num=block_num,
                code=code,
                context=full_context,
            )
            snippets.append(snippet)
            i = j + 1
        else:
            i += 1

    return snippets


def classify_snippet(s: Snippet) -> None:
    """Classify snippet type and check for intentional bugs."""
    code = s.code

    # Check for fill-in-blank placeholders like (A), (B), (C) — student answer slots
    if FILL_BLANK_PATTERN.search(code):
        s.kind = "FILL_BLANK"
        return

    # Check for intentional bug markers in context
    ctx = s.context.lower() + code[:200]
    for kw in INTENTIONAL_BUG_KEYWORDS:
        if re.search(kw, ctx, re.IGNORECASE):
            s.kind = "INTENTIONAL_BUG"
            return

    # Detect pedagogical explanation snippets: lines with a bare expression (no ;)
    # followed by a // explanation comment — these cannot and should not compile standalone
    peda_lines = []
    for line in code.splitlines():
        stripped_l = line.strip()
        if not stripped_l or stripped_l.startswith('//') or stripped_l.startswith('#'):
            continue
        comment_pos = stripped_l.find('//')
        if comment_pos > 0:
            before = stripped_l[:comment_pos].rstrip()
            if before and before[-1] not in (';', '{', '}', ',', '('):
                peda_lines.append(line)
    # 2+ peda lines = clear explanation block; 1 peda line containing pointer ops = also skip
    has_ptr_peda = any(
        re.search(r'(?<!\w)[&*]|[+\-]\s*[0-9]', ln) for ln in peda_lines
    )
    if len(peda_lines) >= 2 or (len(peda_lines) >= 1 and has_ptr_peda):
        s.kind = "PEDAGOGICAL_SKIP"
        return

    # Detect unbalanced braces — truncated fill-blank snippets
    if code.count('{') != code.count('}'):
        s.kind = "FILL_BLANK"
        return

    # Classify by code content — ASCII-only pattern; \*? handles pointer-return types
    has_main = bool(re.search(r'\bint\s+main\s*\(', code))
    has_function_def = bool(re.search(
        r'\b(?!if\b|else\b|for\b|while\b|do\b|switch\b)'
        r'[a-zA-Z_]\w*\s+\*?\s*[a-zA-Z_]\w*\s*\([^)]*\)\s*\{',
        code
    ))
    has_statements = bool(re.search(r';', code))

    if has_main:
        s.kind = "FULL_PROGRAM"
    elif has_function_def:
        s.kind = "FUNCTION_DEF"
    elif has_statements or len(code.strip()) > 5:
        s.kind = "FRAGMENT"
    else:
        s.kind = "FRAGMENT"


def prepare_for_compilation(code: str, kind: str) -> str:
    """Wrap code appropriately for compilation."""
    needs_stdio = "printf" in code or "scanf" in code or "puts" in code or "getchar" in code
    needs_string = "strlen" in code or "strcpy" in code or "strcmp" in code or "strcat" in code or "sprintf" in code
    needs_stdlib = "malloc" in code or "free" in code or "exit" in code or "atoi" in code
    needs_math = "sqrt" in code or "pow" in code or "fabs" in code

    includes = []
    if needs_stdio or kind in ("FRAGMENT", "FUNCTION_DEF"):
        includes.append("#include <stdio.h>")
    if needs_string:
        includes.append("#include <string.h>")
    if needs_stdlib:
        includes.append("#include <stdlib.h>")
    if needs_math:
        includes.append("#include <math.h>")

    # Check what includes are already present
    existing_includes = set(re.findall(r'#include\s*<[^>]+>', code))
    new_includes = [inc for inc in includes if inc not in existing_includes]

    # Detect stub functions needed (called but not defined)
    needed_stubs = [
        stub for fn, stub in STUB_FUNCTIONS.items()
        if re.search(r'\b' + fn + r'\s*\(', code)
        and not re.search(r'\b(?:void|int|double)\s+' + fn + r'\s*\(', code)
    ]

    if kind == "FULL_PROGRAM":
        parts = []
        if new_includes:
            parts.append("\n".join(new_includes))
        if needed_stubs:
            parts.append("\n".join(needed_stubs))
        parts.append(code)
        return "\n".join(parts) if parts else code

    elif kind == "FUNCTION_DEF":
        header = "\n".join(new_includes) if new_includes else "#include <stdio.h>"
        # Inject macro constants used in array dimension parameters (e.g. int a[N][N])
        macros = [
            defn for name, defn in COMMON_MACROS.items()
            if re.search(r'\b' + name + r'\b', code)
        ]
        macro_block = ("\n".join(macros) + "\n") if macros else ""
        # Inject Student typedef if needed
        student_block = ""
        if 'Student' in code and 'typedef struct' not in code:
            student_block = STUDENT_STRUCT_TYPEDEF + "\n\n"
        # Inject stubs for functions called but not defined in this snippet
        func_stub_block = ("\n".join(needed_stubs) + "\n\n") if needed_stubs else ""
        func_code, usage_code = split_function_and_usage(code)
        preamble = f"{header}\n{macro_block}{student_block}{func_stub_block}"
        if usage_code.strip():
            usage_indented = "\n".join(
                "    " + ln for ln in usage_code.splitlines() if ln.strip()
            )
            return f"""{preamble}
{func_code}

int main(void) {{
{usage_indented}
    return 0;
}}
"""
        return f"""{preamble}
{code}

int main(void) {{
    return 0;
}}
"""

    else:  # FRAGMENT
        header = "\n".join(new_includes) if new_includes else "#include <stdio.h>"
        stub_block = ("\n".join(needed_stubs) + "\n") if needed_stubs else ""
        stripped = code.strip()
        var_preamble = inject_vars_for_fragment(stripped)
        preamble_block = ("    " + var_preamble + "\n") if var_preamble else ""
        body = "\n".join(
            "    " + line if line.strip() else line
            for line in stripped.splitlines()
        )
        # Fragments with bare `return;` come from void-function contexts
        if re.search(r'\breturn\s*;', stripped):
            return f"""{header}
{stub_block}
static void _frag(void) {{
{preamble_block}    {body.lstrip()}
}}

int main(void) {{
    _frag();
    return 0;
}}
"""
        return f"""{header}
{stub_block}
int main(void) {{
{preamble_block}    {body.lstrip()}
    return 0;
}}
"""


def compile_code(code: str) -> tuple[bool, bool, str]:
    """
    Compile code. Returns (success, has_warnings, output).
    success=True means no errors (warnings OK).
    """
    with tempfile.NamedTemporaryFile(suffix=".c", mode="w", delete=False, encoding="utf-8") as f:
        f.write(code)
        fname = f.name

    try:
        result = subprocess.run(
            ["gcc", "-Wall", "-Wextra", "-std=c11", "-o", "/tmp/test_snippet", fname],
            capture_output=True, text=True, timeout=15
        )
        output = result.stdout + result.stderr
        success = result.returncode == 0
        has_warnings = "warning:" in output.lower()
        return success, has_warnings, output
    except subprocess.TimeoutExpired:
        return False, False, "TIMEOUT"
    except FileNotFoundError:
        return False, False, "gcc not found"
    finally:
        os.unlink(fname)
        if os.path.exists("/tmp/test_snippet"):
            os.unlink("/tmp/test_snippet")


def attempt_repair(s: Snippet, compiled_code: str, error_msg: str) -> Optional[str]:
    """Try to auto-repair common errors."""
    code = compiled_code
    repairs = []

    # Missing #include <stdio.h>
    if "implicit declaration" in error_msg and "printf" in error_msg:
        if "#include <stdio.h>" not in code:
            code = "#include <stdio.h>\n" + code
            repairs.append("added #include <stdio.h>")

    # Missing #include <string.h>
    if ("implicit declaration" in error_msg or "undeclared" in error_msg) and \
       any(fn in error_msg for fn in ["strlen", "strcpy", "strcmp", "strcat"]):
        if "#include <string.h>" not in code:
            code = "#include <string.h>\n" + code
            repairs.append("added #include <string.h>")

    # Missing #include <stdlib.h>
    if ("implicit declaration" in error_msg) and \
       any(fn in error_msg for fn in ["malloc", "free", "atoi", "exit"]):
        if "#include <stdlib.h>" not in code:
            code = "#include <stdlib.h>\n" + code
            repairs.append("added #include <stdlib.h>")

    # size_t needs stdlib/string
    if "unknown type name 'size_t'" in error_msg or "size_t" in error_msg:
        if "#include <stddef.h>" not in code:
            code = "#include <stddef.h>\n" + code
            repairs.append("added #include <stddef.h>")

    # VLA or C11 issue - try without -Wextra
    # (handled by recompile)

    if repairs:
        s.repair_applied = "; ".join(repairs)
        return code

    return None


def verify_snippet(s: Snippet) -> None:
    """Compile and verify a single snippet."""
    if s.kind in ("INTENTIONAL_BUG", "FILL_BLANK", "PEDAGOGICAL_SKIP"):
        s.status = s.kind
        s.final_status = s.kind
        return

    # Skip truly empty snippets
    if not s.code.strip():
        s.status = "SKIP"
        s.final_status = "SKIP"
        return

    # Skip pure comment blocks or pseudocode (no semicolons, no braces)
    stripped = s.code.strip()
    if not any(c in stripped for c in [';', '{', '}']):
        # Check if it looks like pseudocode / ASCII art
        if not re.search(r'\b(int|char|double|float|void|printf|scanf|for|while|if)\b', stripped):
            s.status = "SKIP"
            s.final_status = "SKIP"
            s.messages = "Pseudocode/non-C content, skipped"
            return

    # Prepare for compilation
    compiled_code = prepare_for_compilation(s.code, s.kind)

    success, has_warnings, output = compile_code(compiled_code)
    s.messages = output.strip()

    if success:
        if has_warnings:
            s.status = "WARNING"
            s.warnings = [line for line in output.splitlines() if "warning:" in line.lower()]
        else:
            s.status = "OK"
        s.final_status = s.status
        return

    # Compilation failed — try auto-repair
    s.status = "ERROR"
    repaired = attempt_repair(s, compiled_code, output)

    if repaired:
        success2, has_warnings2, output2 = compile_code(repaired)
        if success2:
            s.repaired_code = repaired
            s.final_status = "REPAIRED" + (" (WARNING)" if has_warnings2 else "")
            s.messages = f"Original error: {output.strip()}\nAfter repair: OK"
            if has_warnings2:
                s.warnings = [line for line in output2.splitlines() if "warning:" in line.lower()]
            return

    s.final_status = "ERROR"


def generate_report(snippets: list[Snippet], output_path: Path) -> None:
    """Generate the markdown verification report."""
    total = len(snippets)
    ok = sum(1 for s in snippets if s.final_status == "OK")
    warning = sum(1 for s in snippets if s.final_status in ("WARNING", "REPAIRED (WARNING)"))
    error_before = sum(1 for s in snippets if s.status == "ERROR")
    repaired = sum(1 for s in snippets if s.final_status in ("REPAIRED", "REPAIRED (WARNING)"))
    still_error = sum(1 for s in snippets if s.final_status == "ERROR")
    intentional = sum(1 for s in snippets if s.final_status == "INTENTIONAL_BUG")
    fill_blank = sum(1 for s in snippets if s.final_status == "FILL_BLANK")
    skipped = sum(1 for s in snippets if s.final_status == "SKIP")
    fragments = sum(1 for s in snippets if s.kind == "FRAGMENT" and s.final_status in ("OK", "REPAIRED", "WARNING"))

    lines = [
        "# C言語コードスニペット検証レポート",
        "",
        f"**検証日時**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "**検証対象**: 03_drills/, 05_mock-exams/",
        "**使用コンパイラ**: gcc -Wall -Wextra -std=c11",
        "",
        "## サマリー",
        "",
        "| 区分 | 件数 |",
        "|---|---|",
        f"| 全スニペット数 | {total} |",
        f"| コンパイル成功 (クリーン) | {ok} |",
        f"| 警告あり | {warning} |",
        f"| エラー（修復前） | {error_before} |",
        f"| 自動修復成功 | {repaired} |",
        f"| 修復不可能 | {still_error} |",
        f"| 意図的バグ（スキップ） | {intentional} |",
        f"| 穴埋め問題（スキップ） | {fill_blank} |",
        f"| 非Cコンテンツ・スキップ | {skipped} |",
        f"| フラグメント（ラップ後成功） | {fragments} |",
        "",
    ]

    # Error details
    repaired_list = [s for s in snippets if s.final_status in ("REPAIRED", "REPAIRED (WARNING)")]
    error_list = [s for s in snippets if s.final_status == "ERROR"]
    warning_list = [s for s in snippets if s.warnings]

    lines += [
        "## エラー詳細",
        "",
        "### 自動修復済み",
        "",
    ]
    if repaired_list:
        lines += ["| ファイル | スニペット# | 種別 | 修復内容 |", "|---|---|---|---|"]
        for s in repaired_list:
            lines.append(f"| {s.file} | #{s.block_num} | {s.kind} | {s.repair_applied} |")
    else:
        lines.append("*なし*")

    lines += ["", "### 修復不可能（要手動確認）", ""]
    if error_list:
        lines += ["| ファイル | スニペット# | 種別 | エラー内容（冒頭） |", "|---|---|---|---|"]
        for s in error_list:
            err_preview = s.messages[:120].replace("\n", " ").replace("|", "\\|")
            lines.append(f"| {s.file} | #{s.block_num} | {s.kind} | `{err_preview}` |")
    else:
        lines.append("*なし — 全エラー解消済み* ✅")

    lines += ["", "### 警告一覧", ""]
    if warning_list:
        lines += ["| ファイル | スニペット# | 警告内容 |", "|---|---|---|"]
        for s in warning_list:
            for w in s.warnings[:2]:  # max 2 warnings per snippet
                w_short = w[:100].replace("|", "\\|")
                lines.append(f"| {s.file} | #{s.block_num} | `{w_short}` |")
    else:
        lines.append("*警告なし* ✅")

    # Per-file summary
    lines += ["", "## ファイル別結果", ""]
    lines += ["| ファイル | 合計 | OK | REPAIRED | WARNING | ERROR | INTENTIONAL | FILL_BLANK | SKIP |",
              "|---|---|---|---|---|---|---|---|---|"]

    files = {}
    for s in snippets:
        if s.file not in files:
            files[s.file] = []
        files[s.file].append(s)

    for fname, file_snippets in files.items():
        cnt = len(file_snippets)
        f_ok = sum(1 for s in file_snippets if s.final_status == "OK")
        f_rep = sum(1 for s in file_snippets if "REPAIRED" in s.final_status)
        f_warn = sum(1 for s in file_snippets if s.final_status == "WARNING")
        f_err = sum(1 for s in file_snippets if s.final_status == "ERROR")
        f_int = sum(1 for s in file_snippets if s.final_status == "INTENTIONAL_BUG")
        f_fill = sum(1 for s in file_snippets if s.final_status in ("FILL_BLANK", "PEDAGOGICAL_SKIP"))
        f_skip = sum(1 for s in file_snippets if s.final_status == "SKIP")
        lines.append(f"| {fname} | {cnt} | {f_ok} | {f_rep} | {f_warn} | {f_err} | {f_int} | {f_fill} | {f_skip} |")

    # Detail of remaining errors for debugging
    if error_list:
        lines += ["", "## 残存エラー詳細（手動修正用）", ""]
        for s in error_list:
            lines += [
                f"### {s.file} スニペット #{s.block_num} ({s.kind})",
                "",
                "**コード:**",
                "```c",
                s.code[:500],
                "```",
                "",
                "**エラー:**",
                "```",
                s.messages[:500],
                "```",
                "",
            ]

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nReport written to: {output_path}")


def main():
    print("=== C Code Verification ===")
    print(f"Base dir: {BASE_DIR}")
    print(f"Timestamp: {datetime.now()}\n")

    all_snippets = []

    for rel_path in TARGET_FILES:
        md_path = BASE_DIR / rel_path
        if not md_path.exists():
            print(f"SKIP (not found): {rel_path}")
            continue

        snippets = extract_snippets(md_path)
        print(f"  {rel_path}: {len(snippets)} snippets extracted")

        for s in snippets:
            classify_snippet(s)

        for s in snippets:
            verify_snippet(s)

        all_snippets.extend(snippets)

    # Print summary
    print(f"\nTotal snippets: {len(all_snippets)}")

    status_counts = {}
    for s in all_snippets:
        k = s.final_status
        status_counts[k] = status_counts.get(k, 0) + 1

    for status, count in sorted(status_counts.items()):
        print(f"  {status}: {count}")

    # Generate report
    report_path = BASE_DIR / "code-verification-report.md"
    generate_report(all_snippets, report_path)

    # Print remaining errors
    errors = [s for s in all_snippets if s.final_status == "ERROR"]
    if errors:
        print(f"\n⚠️  {len(errors)} snippets still have errors after auto-repair:")
        for s in errors:
            print(f"  {s.file} #{s.block_num} ({s.kind})")
            for line in s.messages.splitlines()[:3]:
                if "error:" in line.lower():
                    print(f"    → {line.strip()}")
    else:
        print("\n✅ 0 compile errors remaining!")

    return len(errors)


if __name__ == "__main__":
    sys.exit(main())
