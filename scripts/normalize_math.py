#!/usr/bin/env python3
r"""Normalise inline ``$...$`` math to ``$$...$$`` for kramdown + MathJax.

kramdown (GitHub Pages) recognises **only** ``$$...$$`` as math — both inline
and display, disambiguated by context. Single-dollar ``$...$`` is left as plain
text, which (a) shows raw LaTeX and (b) corrupts rendering when the math
contains ``|`` (kramdown parses ``|...|`` as a Markdown table) or ``\\`` (parsed
as an escaped backslash, eating matrix row breaks). Converting inline ``$...$``
to ``$$...$$`` fixes all three problems at once.

Algorithm (per file, idempotent)
--------------------------------
1. Split the file on fenced code blocks (```` ``` ```` / ``~~~``); never touch
   code.
2. In each non-code segment:
   a. Protect existing ``$$...$$`` spans (incl. multi-line) with placeholders.
   b. Protect inline-code spans `` `...` `` with placeholders.
   c. Convert each remaining single-line ``$...$`` to ``$$...$$``.
   d. Restore inline-code, then ``$$`` placeholders.

Because step (a) removes every ``$$`` before step (c) runs, re-running the
script finds no single ``$`` to convert — it is idempotent.

Safety
------
* Currency / shell ``$`` is not present in this corpus (verified), and the
  conversion regex requires a closing ``$`` on the **same line** with non-empty,
  dollar-free content, so accidental matches are unlikely. Always review the
  dry-run diff before ``--apply``.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# A fenced code block: opening fence line, body, matching close fence line.
# The captured marker (group 1) must match at the close so ``` and ~~~ pair up.
_FENCE_SPLIT_RE = re.compile(r"(?ms)^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?^[ \t]*\1[ \t]*$\n?")

_DISPLAY_RE = re.compile(r"\$\$.+?\$\$", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
_INLINE_MATH_RE = re.compile(r"\$([^$\n]+?)\$")

_PLACEHOLDER = "\x00{kind}{idx}\x00"


@dataclass(frozen=True)
class Change:
    """A planned math normalisation for one file."""

    path: Path
    new_text: str
    old_text: str
    count: int


def _protect(text: str, pattern: re.Pattern[str], kind: str) -> tuple[str, list[str]]:
    """Replace every ``pattern`` match in ``text`` with an opaque placeholder.

    Parameters
    ----------
    text : str
        Input text.
    pattern : re.Pattern[str]
        Pattern whose matches must be protected from further processing.
    kind : str
        Short label used to build unique placeholder tokens.

    Returns
    -------
    tuple[str, list[str]]
        ``(protected_text, stash)`` where ``stash[i]`` is the original text of
        placeholder ``i``.
    """
    stash: list[str] = []

    def _stash(match: re.Match[str]) -> str:
        token = _PLACEHOLDER.format(kind=kind, idx=len(stash))
        stash.append(match.group(0))
        return token

    return pattern.sub(_stash, text), stash


def _restore(text: str, stash: list[str], kind: str) -> str:
    """Inverse of :func:`_protect`."""
    for idx, original in enumerate(stash):
        text = text.replace(_PLACEHOLDER.format(kind=kind, idx=idx), original)
    return text


def _normalize_segment(segment: str) -> tuple[str, int]:
    """Normalise inline math in a single non-code ``segment``.

    Returns
    -------
    tuple[str, int]
        ``(new_segment, n_inline_converted)``.
    """
    protected, display = _protect(segment, _DISPLAY_RE, "D")
    protected, code = _protect(protected, _INLINE_CODE_RE, "C")

    count = 0

    def _to_double(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return f"$${match.group(1)}$$"

    protected = _INLINE_MATH_RE.sub(_to_double, protected)

    protected = _restore(protected, code, "C")
    protected = _restore(protected, display, "D")
    return protected, count


def normalize_text(text: str) -> tuple[str, int]:
    """Normalise inline math across ``text``, skipping fenced code blocks.

    Returns
    -------
    tuple[str, int]
        ``(new_text, n_inline_converted)``.
    """
    out: list[str] = []
    total = 0
    pos = 0
    for match in _FENCE_SPLIT_RE.finditer(text):
        non_code = text[pos : match.start()]
        new_seg, n = _normalize_segment(non_code)
        out.append(new_seg)
        total += n
        out.append(match.group(0))  # code fence, unchanged
        pos = match.end()
    tail = text[pos:]
    new_tail, n = _normalize_segment(tail)
    out.append(new_tail)
    total += n
    return "".join(out), total


def plan_file(path: Path) -> Change | None:
    """Plan a math normalisation for ``path`` (or ``None`` if nothing to do)."""
    text = path.read_text(encoding="utf-8")
    if "$" not in text:
        return None
    new_text, count = normalize_text(text)
    if new_text == text or count == 0:
        return None
    return Change(path=path, new_text=new_text, old_text=text, count=count)


def collect_changes(root: Path) -> list[Change]:
    """Collect math normalisations for every ``*.md`` under ``root``."""
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
        print("normalize_math: nothing to normalise (already up to date).")
        return 0

    total = 0
    for change in changes:
        rel = change.path.relative_to(args.root)
        total += change.count
        print(f"{rel}: {change.count} inline span(s)")
        if args.show_diff:
            diff = difflib.unified_diff(
                change.old_text.splitlines(keepends=True),
                change.new_text.splitlines(keepends=True),
                fromfile=f"a/{rel}",
                tofile=f"b/{rel}",
            )
            sys.stdout.write("".join(diff))

    print(f"\nnormalize_math: {len(changes)} file(s), {total} inline span(s).")
    if not args.apply:
        print("Dry-run only. Re-run with --apply to write.")
        return 0

    for change in changes:
        change.path.write_text(change.new_text, encoding="utf-8")
    print(f"Applied to {len(changes)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
