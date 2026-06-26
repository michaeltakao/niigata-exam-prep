#!/usr/bin/env python3
"""Hide internal (non-learner) pages from the just-the-docs sidebar.

In this Jekyll setup, even a root-level Markdown file **without** front-matter
receives an auto-derived ``page.title`` (from its H1), so just-the-docs lists it
in the navigation. The instructor/report/audit pages are therefore showing as
top-level sidebar entries. This script adds ``nav_exclude: true`` to those pages
so they stay reachable by URL but disappear from the navigation.

Targets
-------
* Every root-level ``*.md`` **except** the learner entry points
  (:data:`KEEP_ROOT`).
* Every ``06_progress/*.md`` (internal progress tracking).

Idempotent: a file that already has ``nav_exclude`` is left unchanged; files
without front-matter get a fresh block prepended.

Dry-run by default; pass ``--apply`` to write.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

# Learner-facing root pages that MUST stay in the navigation.
KEEP_ROOT: frozenset[str] = frozenset(
    {"STUDENT_HOME.md", "index.md", "00_guide.md"}
)


@dataclass(frozen=True)
class Change:
    """A planned ``nav_exclude`` injection for one file."""

    path: Path
    new_text: str


def _ensure_nav_exclude(text: str) -> str | None:
    """Return ``text`` with ``nav_exclude: true`` ensured, or ``None`` if no-op.

    Parameters
    ----------
    text : str
        Original file contents.

    Returns
    -------
    str | None
        Updated contents, or ``None`` when ``nav_exclude`` is already present.
    """
    if "nav_exclude:" in text.split("---\n\n", 1)[0]:
        return None
    if text.lstrip().startswith("---"):
        # Insert into the existing front-matter, right after the opening '---'.
        lines = text.splitlines(keepends=True)
        # lines[0] is the opening '---'
        lines.insert(1, "nav_exclude: true\n")
        return "".join(lines)
    # No front-matter: prepend a minimal block.
    return "---\nnav_exclude: true\n---\n\n" + text


def collect_changes(root: Path) -> list[Change]:
    """Collect ``nav_exclude`` injections for internal pages under ``root``."""
    targets: list[Path] = [
        p for p in sorted(root.glob("*.md")) if p.name not in KEEP_ROOT
    ]
    progress = root / "06_progress"
    if progress.is_dir():
        targets += sorted(progress.glob("*.md"))

    changes: list[Change] = []
    for path in targets:
        new_text = _ensure_nav_exclude(path.read_text(encoding="utf-8"))
        if new_text is not None:
            changes.append(Change(path=path, new_text=new_text))
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
        help="Write the changes. Without this flag, only a dry-run list is shown.",
    )
    args = parser.parse_args(argv)

    changes = collect_changes(args.root)
    if not changes:
        print("hide_internal_nav: nothing to hide (already up to date).")
        return 0

    for change in changes:
        print(f"  + nav_exclude: {change.path.relative_to(args.root)}")
    print(f"\nhide_internal_nav: {len(changes)} file(s) to update.")

    if not args.apply:
        print("Dry-run only. Re-run with --apply to write.")
        return 0

    for change in changes:
        change.path.write_text(change.new_text, encoding="utf-8")
    print(f"Applied nav_exclude to {len(changes)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
