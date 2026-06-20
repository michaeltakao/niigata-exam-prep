"""Convert local markdown files to Notion-flavored Markdown.

Handles:
  - Strip YAML frontmatter
  - :::formula / :::example / :::warning / :::examtip blocks → callout
  - Inline math $...$ → $`...$` (Notion syntax)
  - Block math $$...$$ is kept as-is (already valid in Notion)
  - Standard tables stay as standard markdown (Notion MCP accepts them)
"""

import re
import sys
from pathlib import Path

# Callout config: directive → (icon, color)
CALLOUT_MAP = {
    "formula": ("📐", "blue_bg"),
    "example": ("📝", "gray_bg"),
    "warning": ("⚠️", "red_bg"),
    "examtip": ("🎯", "green_bg"),
    "hint": ("💡", "yellow_bg"),
}


def strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter block if present."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:].lstrip("\n")
    return text


def convert_div_blocks(text: str) -> str:
    """Convert :::type ... ::: blocks to Notion callout syntax."""
    lines = text.split("\n")
    result: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^:::\s*(\w+)\s*$", line)
        if m:
            directive = m.group(1)
            icon, color = CALLOUT_MAP.get(directive, ("📝", "gray_bg"))
            result.append(f'<callout icon="{icon}" color="{color}">')
            i += 1
            # Collect block content until closing :::
            while i < len(lines) and not re.match(r"^:::\s*$", lines[i]):
                result.append("\t" + lines[i])
                i += 1
            result.append("</callout>")
            i += 1  # skip closing :::
        else:
            result.append(line)
            i += 1
    return "\n".join(result)


def expand_block_math(text: str) -> str:
    """Convert single-line $$...$$ to multiline Notion block math.

    Notion requires:
        $$
        equation
        $$

    This handles both indented (inside callout) and non-indented cases.
    """
    lines = text.split("\n")
    result = []
    in_code = False
    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
        if in_code:
            result.append(line)
            continue
        # Match optional leading whitespace then $$...$$
        m = re.match(r"^(\s*)\$\$(.+?)\$\$\s*$", line)
        if m:
            indent = m.group(1)
            eq = m.group(2)
            result.append(f"{indent}$$")
            result.append(f"{indent}{eq}")
            result.append(f"{indent}$$")
        else:
            result.append(line)
    return "\n".join(result)


def convert_inline_math(text: str) -> str:
    """Convert $...$ inline math to Notion $`...$` syntax.

    Skips:
      - Block math ($$...$$)
      - Content inside code fences (```...```)
      - Content inside callout tags already
    """
    lines = text.split("\n")
    in_code_block = False
    result = []
    for line in lines:
        # Track code fences
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            result.append(line)
            continue
        if in_code_block:
            result.append(line)
            continue

        # Skip lines that are part of block math ($$)
        if line.strip().startswith("$$") or line.strip() == "$$":
            result.append(line)
            continue

        # Convert inline $...$ → $`...$`
        # Strategy: tokenize, preserving $$...$$ spans first
        converted = _convert_line_inline_math(line)
        result.append(converted)

    return "\n".join(result)


def _convert_line_inline_math(line: str) -> str:
    """Convert inline $...$ on a single line, skipping $$ spans."""
    # First pass: protect $$ ... $$ spans by replacing with placeholder
    # (block math that might appear inline in a table cell)
    protected = []
    out_parts = []
    idx = 0
    s = line
    # Replace $$...$$ with placeholders
    placeholder_map: dict[str, str] = {}
    p_count = 0

    def protect_double_dollar(text: str) -> str:
        nonlocal p_count
        result = []
        i = 0
        while i < len(text):
            if text[i:i+2] == "$$":
                end = text.find("$$", i + 2)
                if end != -1:
                    key = f"\x00BLOCK{p_count}\x00"
                    placeholder_map[key] = text[i:end+2]
                    result.append(key)
                    p_count += 1
                    i = end + 2
                    continue
            result.append(text[i])
            i += 1
        return "".join(result)

    protected_line = protect_double_dollar(s)

    # Now convert remaining $...$ → $`...`$
    # Use regex that matches $...$ where content doesn't contain newlines
    # Avoid matching $ used in other contexts
    def replace_inline(m: re.Match) -> str:
        content = m.group(1)
        return f"$`{content}`$"

    converted = re.sub(r"\$([^$\n]+?)\$", replace_inline, protected_line)

    # Restore placeholders
    for key, val in placeholder_map.items():
        converted = converted.replace(key, val)

    return converted


def convert_file(path: Path) -> str:
    """Full conversion pipeline for a single markdown file."""
    text = path.read_text(encoding="utf-8")
    text = strip_frontmatter(text)
    text = convert_div_blocks(text)
    text = convert_inline_math(text)
    return text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python to_notion_md.py <file.md>")
        sys.exit(1)
    p = Path(sys.argv[1])
    print(convert_file(p))
