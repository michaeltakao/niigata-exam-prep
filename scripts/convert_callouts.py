#!/usr/bin/env python3
"""Convert ``::: type`` callout fences into kramdown-friendly ``<div>`` blocks.

The source notes use a Pandoc-style fenced-div syntax for coloured callouts::

    ::: formula
    **内積の性質**
    - $a \\cdot b = 0$
    :::

kramdown (GitHub Pages) does **not** understand ``:::`` and emits it as literal
text, and — worse — it does not process the math/Markdown inside. This script
rewrites each callout into::

    <div class="callout callout-formula" markdown="1">

    **内積の性質**
    - $$a \\cdot b = 0$$

    </div>

The ``markdown="1"`` attribute makes kramdown process the inner Markdown and
math, and the surrounding blank lines let block-level math (``$$...$$`` on its
own line) be recognised. Colours and the label (📘公式 etc.) are added in CSS.

Design notes
------------
* **Idempotent**: files with no ``^:::`` opener/closer are left unchanged, so
  re-running is safe.
* **Code-fence aware**: lines inside ```` ``` ```` / ``~~~`` fences are never
  touched.
* **Balance check**: refuses to convert a file whose openers and closers do not
  balance (prints a warning and skips it), to avoid corrupting nesting.
* **Dry-run by default**; pass ``--apply`` to write.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass
from pathlib import Path

CALLOUT_TYPES: tuple[str, ...] = ("formula", "example", "warning", "examtip")

_OPEN_RE = re.compile(r"^:::[ \t]*(" + "|".join(CALLOUT_TYPES) + r")[ \t]*$")
_CLOSE_RE = re.compile(r"^:::[ \t]*$")
_FENCE_RE = re.compile(r"^[ \t]*(```|~~~)")


@dataclass(frozen=True)
class Change:
    """A planned callout conversion for one file."""

    path: Path
    new_text: str
    old_text: str
    count: int


def convert_text(text: str) -> tuple[str, int]:
    """Convert all ``:::`` callouts in ``text`` to ``<div>`` blocks.

    Parameters
    ----------
    text : str
        File contents.

    Returns
    -------
    tuple[str, int]
        ``(new_text, n_openers_converted)``. If openers and closers do not
        balance the original text is returned with a count of ``-1``.
    """
    lines = text.splitlines(keepends=False)
    out: list[str] = []
    in_fence = False
    open_depth = 0
    n_open = 0

    for line in lines:
        if _FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue

        open_match = _OPEN_RE.match(line)
        if open_match:
            ctype = open_match.group(1)
            out.append(f'<div class="callout callout-{ctype}" markdown="1">')
            out.append("")  # blank line so kramdown treats inner content as blocks
            open_depth += 1
            n_open += 1
            continue

        if _CLOSE_RE.match(line) and open_depth > 0:
            out.append("")  # blank line before closing the div
            out.append("</div>")
            open_depth -= 1
            continue

        out.append(line)

    if open_depth != 0:
        return text, -1

    new_text = "\n".join(out)
    if text.endswith("\n"):
        new_text += "\n"
    return new_text, n_open


def plan_file(path: Path) -> Change | None:
    """Plan a callout conversion for ``path`` (or ``None`` if nothing to do)."""
    text = path.read_text(encoding="utf-8")
    if not any(_OPEN_RE.match(line) for line in text.splitlines()):
        return None
    new_text, count = convert_text(text)
    if count < 0:
        print(f"WARNING: unbalanced ::: in {path}; skipped.", file=sys.stderr)
        return None
    if new_text == text:
        return None
    return Change(path=path, new_text=new_text, old_text=text, count=count)


def collect_changes(root: Path) -> list[Change]:
    """Collect callout conversions for every ``*.md`` under ``root``."""
    changes: list[Change] = []
    skip = {".git", "scripts", "templates", "vendor", "node_modules"}
    for md in sorted(root.rglob("*.md")):
        if any(part in skip for part in md.relative_to(root).parts):
            continue
        change = plan_file(md)
        if change is not None:
            changes.append(change)
    return changes


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Repository root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write the changes. Without this flag, only a dry-run diff is shown.",
    )
    parser.add_argument(
        "--show-diff",
        action="store_true",
        help="Print the full unified diff for each file (verbose).",
    )
    args = parser.parse_args(argv)

    changes = collect_changes(args.root)
    if not changes:
        print("convert_callouts: nothing to convert (already up to date).")
        return 0

    total = 0
    for change in changes:
        rel = change.path.relative_to(args.root)
        total += change.count
        print(f"{rel}: {change.count} callout(s)")
        if args.show_diff:
            diff = difflib.unified_diff(
                change.old_text.splitlines(keepends=True),
                change.new_text.splitlines(keepends=True),
                fromfile=f"a/{rel}",
                tofile=f"b/{rel}",
            )
            sys.stdout.write("".join(diff))

    print(f"\nconvert_callouts: {len(changes)} file(s), {total} callout(s).")
    if not args.apply:
        print("Dry-run only. Re-run with --apply to write.")
        return 0

    for change in changes:
        change.path.write_text(change.new_text, encoding="utf-8")
    print(f"Applied to {len(changes)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
