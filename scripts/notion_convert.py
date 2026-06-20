"""Convert custom markdown to Notion-flavored markdown for MCP upload."""
import re
import sys
from pathlib import Path


CALLOUT_MAP = {
    'formula':  ('📐', 'blue_bg'),
    'example':  ('📝', 'gray_bg'),
    'warning':  ('⚠️',  'red_bg'),
    'examtip':  ('🎯', 'green_bg'),
    'hint':     ('💡', 'yellow_bg'),
}


def convert(content: str) -> str:
    # 1. Strip YAML frontmatter
    content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)

    # 2. Protect code blocks from transformation
    code_blocks: list[str] = []
    def save_code(m: re.Match) -> str:
        code_blocks.append(m.group(0))
        return f'\x00CODE{len(code_blocks)-1}\x00'
    content = re.sub(r'```.*?```', save_code, content, flags=re.DOTALL)

    # 3. Protect $$ block math
    math_blocks: list[str] = []
    def save_math(m: re.Match) -> str:
        math_blocks.append(m.group(0))
        return f'\x00MATH{len(math_blocks)-1}\x00'
    content = re.sub(r'\$\$.*?\$\$', save_math, content, flags=re.DOTALL)

    # 4. Convert inline math $...$ → $`...`$  (single-line only)
    content = re.sub(r'\$([^$\n`]+)\$', r'$`\1`$', content)

    # 5. Restore protected blocks
    for i, blk in enumerate(math_blocks):
        content = content.replace(f'\x00MATH{i}\x00', blk)
    for i, blk in enumerate(code_blocks):
        content = content.replace(f'\x00CODE{i}\x00', blk)

    # 6. Convert ::: callout blocks
    def make_callout(m: re.Match) -> str:
        kind = m.group(1).strip()
        inner = m.group(2).rstrip('\n')
        icon, color = CALLOUT_MAP.get(kind, ('📌', 'gray_bg'))
        lines = inner.split('\n')
        indented = '\n'.join(('\t' + ln) if ln.strip() else '' for ln in lines)
        return f'<callout icon="{icon}" color="{color}">\n{indented}\n</callout>'

    content = re.sub(r':::[ ]*(\w+)\n(.*?):::', make_callout, content, flags=re.DOTALL)

    return content.strip()


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: notion_convert.py <file.md>", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1])
    print(convert(path.read_text(encoding='utf-8')))


if __name__ == '__main__':
    main()
