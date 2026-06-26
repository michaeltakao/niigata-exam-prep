#!/usr/bin/env python3
"""Inject just-the-docs ``title`` front-matter into learner-facing pages.

just-the-docs shows a page in the sidebar **only if it has a ``title``** in its
YAML front-matter (opt-in navigation). This script gives a ``title`` to the
learner-facing pages that currently lack front-matter, deriving the title from
the page's first level-1 heading (``# ...``). Internal report pages are left
untouched so they stay out of the navigation.

Design notes
------------
* **Idempotent**: a file that already starts with ``---`` (front-matter) is
  skipped, so re-running is safe.
* **Non-destructive to body**: only a front-matter block is *prepended*; the
  original Markdown body is never modified.
* **Dry-run by default**: prints a unified diff of every change. Pass
  ``--apply`` to write the files.

Assumptions
-----------
* Each target file has a single leading ``# `` H1 used as the title source.
* Titles may contain ``—``, ``★``, emoji, parentheses, ``:`` — all handled by
  double-quoting and escaping in YAML.
"""

from __future__ import annotations

import argparse
import difflib
import sys
from dataclasses import dataclass
from pathlib import Path

# Directories whose pages are part of the learner navigation and therefore want
# a sidebar title. (Paths are relative to the repository root.)
TARGET_DIRS: tuple[str, ...] = (
    "02_textbook",
    "03_drills",
    "05_mock-exams",
    "09_study-plans",
    "10_remediation",
    "07_technique-guide",
    "01_roadmap",
    "07_mastery",
    "08_schedule",
    "00_exam-analysis",
    "04_question-map",
)


@dataclass(frozen=True)
class Change:
    """A single planned front-matter injection.

    Parameters
    ----------
    path : Path
        File to be modified.
    title : str
        Title string extracted from the first H1.
    new_text : str
        Full new file content (front-matter + original body).
    old_text : str
        Original file content (for diffing).
    """

    path: Path
    title: str
    new_text: str
    old_text: str


def _yaml_quote(value: str) -> str:
    """Return ``value`` as a safely double-quoted YAML scalar.

    Parameters
    ----------
    value : str
        Raw title text.

    Returns
    -------
    str
        Double-quoted scalar with ``\\`` and ``"`` escaped.
    """
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _extract_h1(text: str) -> str | None:
    """Extract the first level-1 heading text from Markdown ``text``.

    Parameters
    ----------
    text : str
        File contents.

    Returns
    -------
    str | None
        The heading text (without the leading ``# ``), or ``None`` if the file
        has no H1.
    """
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return None


def plan_file(path: Path) -> Change | None:
    """Plan a title injection for a single file.

    Parameters
    ----------
    path : Path
        Markdown file to inspect.

    Returns
    -------
    Change | None
        A planned change, or ``None`` if the file already has front-matter or
        has no H1 to use as a title.
    """
    text = path.read_text(encoding="utf-8")
    if text.lstrip().startswith("---"):
        return None  # already has front-matter
    title = _extract_h1(text)
    if title is None:
        return None
    front_matter = f"---\ntitle: {_yaml_quote(title)}\n---\n\n"
    return Change(path=path, title=title, new_text=front_matter + text, old_text=text)


def collect_changes(root: Path) -> list[Change]:
    """Collect planned changes across all target directories.

    Parameters
    ----------
    root : Path
        Repository root.

    Returns
    -------
    list[Change]
        Planned changes, sorted by path.
    """
    changes: list[Change] = []
    for rel in TARGET_DIRS:
        directory = root / rel
        if not directory.is_dir():
            continue
        for md in sorted(directory.rglob("*.md")):
            change = plan_file(md)
            if change is not None:
                changes.append(change)
    return changes


def main(argv: list[str] | None = None) -> int:
    """CLI entry point.

    Parameters
    ----------
    argv : list[str] | None
        Argument vector (defaults to ``sys.argv[1:]``).

    Returns
    -------
    int
        Process exit code.
    """
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
    args = parser.parse_args(argv)

    changes = collect_changes(args.root)
    if not changes:
        print("inject_titles: no files need a title (already up to date).")
        return 0

    for change in changes:
        rel = change.path.relative_to(args.root)
        diff = difflib.unified_diff(
            change.old_text.splitlines(keepends=True)[:1],
            change.new_text.splitlines(keepends=True)[:5],
            fromfile=f"a/{rel}",
            tofile=f"b/{rel}",
        )
        sys.stdout.write("".join(diff))
        print(f"  -> title: {change.title}")

    print(f"\ninject_titles: {len(changes)} file(s) to update.")
    if not args.apply:
        print("Dry-run only. Re-run with --apply to write.")
        return 0

    for change in changes:
        change.path.write_text(change.new_text, encoding="utf-8")
    print(f"Applied front-matter to {len(changes)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
