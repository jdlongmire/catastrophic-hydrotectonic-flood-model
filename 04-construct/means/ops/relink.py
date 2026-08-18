#!/usr/bin/env python3
"""relink — repair relative links after a structural move.

Mandatory-scripted step of WP-HTF-0001. Both hand-done renumber sweeps on
2026-08-17 broke cross-references; the VWMM refactor moved essentially every
file in the tree, so hand-repair was not an option.

The rename map is taken from git itself (`git diff --cached --name-status -M`),
not hand-written. That matters: git records what actually moved, so the repair
cannot drift from the moves it is repairing.

For each markdown file, every relative link is resolved against the file's OLD
location, mapped through the rename map, and rewritten as a path relative to
the file's NEW location. Links that already resolve are left untouched, which
makes the script idempotent and keeps the diff to genuine repairs.

    python3 04-construct/means/ops/relink.py           # dry run
    python3 04-construct/means/ops/relink.py --apply
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]
LINK = re.compile(r"(!?\[[^\]]*\]\()([^)]+)(\))")
# Many links here are labelled with the path itself: [`02-theory/x.md`](02-theory/x.md).
# After a move the target is repaired but the label still displays the old path,
# which is worse than a broken link — it reads as authoritative and is wrong.
LABELLED = re.compile(r"(!?\[)(`?)([^`\]]+)(`?)(\]\()([^)\s]+)(\))")
EXTERNAL = ("http://", "https://", "mailto:", "doi:", "ftp://", "#")


def rename_map() -> dict[str, str]:
    """old repo-relative path -> new repo-relative path, straight from git."""
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-status", "-M"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    m = {}
    for line in out.splitlines():
        parts = line.split("\t")
        if parts[0].startswith("R") and len(parts) == 3:
            m[parts[1]] = parts[2]
    return m


def map_path(p: str, renames: dict[str, str]) -> str | None:
    """Map an old repo-relative path (file or directory) to its new location."""
    if p in renames:
        return renames[p]
    # Directory: find any renamed file beneath it and strip the shared suffix.
    prefix = p.rstrip("/") + "/"
    for old, new in renames.items():
        if old.startswith(prefix):
            suffix = old[len(prefix):]
            if new.endswith(suffix):
                return new[: -len(suffix)].rstrip("/")
    return None


def rewrite(new_path: Path, old_rel: str, renames: dict[str, str], apply: bool):
    """Repair links in one file. Returns list of (old_target, new_target)."""
    text = new_path.read_text(encoding="utf-8")
    old_dir = os.path.dirname(old_rel)
    new_dir = new_path.parent.relative_to(ROOT).as_posix()
    fixes = []

    def sub(m):
        head, raw, tail = m.group(1), m.group(2).strip(), m.group(3)
        bits = raw.split()
        target, title = bits[0], (" " + " ".join(bits[1:]) if len(bits) > 1 else "")
        if not target or target.startswith(EXTERNAL):
            return m.group(0)
        frag = ""
        if "#" in target:
            target, frag = target.split("#", 1)
            frag = "#" + frag
        if not target:
            return m.group(0)
        # Already resolves from the new location — leave it alone.
        if (new_path.parent / unquote(target)).exists():
            return m.group(0)
        # Resolve against where this file used to live, then map.
        old_target = os.path.normpath(os.path.join(old_dir, unquote(target)))
        mapped = map_path(old_target, renames)
        if mapped is None:
            # The target did not move — but this file did, so the relative path
            # between them still changed. Point at the target where it still is.
            # (dev-notes/ and research/ stay at root by design; every belt doc
            # that moved deeper into the baseline links out to them.)
            if (ROOT / old_target).exists():
                mapped = old_target
            else:
                return m.group(0)
        rel = os.path.relpath(mapped, new_dir or ".")
        if target.endswith("/") and not rel.endswith("/"):
            rel += "/"
        fixes.append((target, rel))
        return f"{head}{rel}{frag}{title}{tail}"

    new_text = LINK.sub(sub, text)
    if apply and new_text != text:
        new_path.write_text(new_text, encoding="utf-8")
    return fixes


def relabel(new_path: Path, apply: bool):
    """Update path-shaped link labels to match the target they point at.

    Only fires when the label is a path that no longer resolves, the target
    does resolve, and both name the same file. A label that is prose, a DOI,
    or a deliberately different string is left alone.
    """
    text = new_path.read_text(encoding="utf-8")
    fixes = []

    def sub(m):
        obr, tick1, label, tick2, mid, target, cbr = m.groups()
        if "/" not in label or target.startswith(EXTERNAL) or label == target:
            return m.group(0)
        bare = target.split("#")[0]
        if not (new_path.parent / unquote(bare)).exists():
            return m.group(0)
        if (new_path.parent / unquote(label)).exists():
            return m.group(0)
        if label.rstrip("/").split("/")[-1] != bare.rstrip("/").split("/")[-1]:
            return m.group(0)
        fixes.append((label, bare))
        return f"{obr}{tick1}{bare}{tick2}{mid}{target}{cbr}"

    new_text = LABELLED.sub(sub, text)
    if apply and new_text != text:
        new_path.write_text(new_text, encoding="utf-8")
    return fixes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--labels", action="store_true",
                    help="also update path-shaped link labels to match their targets")
    args = ap.parse_args()

    if args.labels:
        total = 0
        for path in sorted(ROOT.rglob("*.md")):
            if ".git" in path.parts:
                continue
            fixes = relabel(path, args.apply)
            if fixes:
                print(f"{path.relative_to(ROOT).as_posix()}  ({len(fixes)})")
                for old_l, new_l in fixes:
                    print(f"    {old_l}  ->  {new_l}")
                total += len(fixes)
        print(f"\n{'relabelled' if args.apply else 'would relabel'} {total} link label(s)")
        if not args.apply:
            print("dry run — nothing written. re-run with --apply")
        return 0

    renames = rename_map()
    reverse = {new: old for old, new in renames.items()}
    total = 0

    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        # A file that did not move still needs repair: its targets moved.
        old_rel = reverse.get(rel, rel)
        fixes = rewrite(path, old_rel, renames, args.apply)
        if fixes:
            print(f"{rel}  ({len(fixes)})")
            for old_t, new_t in fixes:
                print(f"    {old_t}  ->  {new_t}")
            total += len(fixes)

    print(f"\n{'repaired' if args.apply else 'would repair'} {total} link(s)"
          f" across {len(renames)} recorded rename(s)")
    if not args.apply:
        print("dry run — nothing written. re-run with --apply")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
