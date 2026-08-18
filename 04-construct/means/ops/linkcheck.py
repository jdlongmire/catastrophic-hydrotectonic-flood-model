#!/usr/bin/env python3
"""linkcheck — verify every relative link in the repo resolves.

Exists because both hand-done renumber sweeps on 2026-08-17 broke
cross-references, and the WP-HTF-0001 structural refactor moved essentially
every file in the tree. Link integrity is now a gated check rather than
something noticed later by a reader.

Checks relative markdown links and image embeds. External URLs, mailto: and
doi: are out of scope — this verifies the tree is internally coherent, not
that the internet is up.

Usage:  python3 04-construct/means/ops/linkcheck.py [--quiet]
Exit code is nonzero if any link is unresolved.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]

LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SKIP_DIRS = {".git"}
EXTERNAL = ("http://", "https://", "mailto:", "doi:", "ftp://", "#")


def targets(line: str):
    for m in LINK.finditer(line):
        raw = m.group(1).strip()
        # Markdown allows an optional title: [text](path "Title")
        target = raw.split()[0] if raw.split() else ""
        if not target or target.startswith(EXTERNAL):
            continue
        yield unquote(target.split("#")[0])


def main() -> int:
    quiet = "--quiet" in sys.argv
    bad, checked = [], 0

    for path in sorted(ROOT.rglob("*.md")):
        if SKIP_DIRS & set(path.parts):
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for target in targets(line):
                checked += 1
                if not (path.parent / target).exists():
                    bad.append((path.relative_to(ROOT), lineno, target))

    if not quiet or bad:
        print(f"linkcheck: {checked} relative link(s) checked, {len(bad)} unresolved")
    for rel, lineno, target in bad:
        print(f"  ✗ {rel}:{lineno} -> {target}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
