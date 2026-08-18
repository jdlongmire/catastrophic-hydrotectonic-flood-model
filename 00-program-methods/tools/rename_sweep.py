#!/usr/bin/env python3
"""Programme rename sweep — WP-HTF-0007.

Substitutes the programme's name across the repo. Classifier-first by design:
the string "hydrotectonic-flood-model" appears in four distinct roles and only
one of them may change, so this script assigns every occurrence to a role,
prints the plan, and substitutes nothing until told to apply.

Scripted rather than hand-edited because both hand-done renumber sweeps on
2026-08-17 broke cross-references (research-practices rule spirit; WP-HTF-0001
carries the same mandate for its path moves).

    python3 rename_sweep.py            # dry run — classify and report
    python3 rename_sweep.py --apply    # substitute the RENAME class only
"""

import argparse
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]

OLD_SLUG, NEW_SLUG = "hydrotectonic-flood-model", "catastrophic-hydrotectonic-flood-model"
OLD_NAME, NEW_NAME = "Hydrotectonic Flood Model", "Catastrophic Hydrotectonic Flood Model"

# Occurrences matching these patterns are records, not live references.
# Order matters only for reporting; a hit on any one of them is a LEAVE.
LEAVE_PATTERNS = [
    ("founding-transcript", re.compile(r"GPT-" + re.escape(OLD_SLUG))),
    ("predecessor-repo", re.compile(r"global-flood-hydrotectonic-model")),
    ("published-artifact", re.compile(re.escape(OLD_SLUG) + r"-(?:position-paper|vertical|horizontal)")),
    ("published-artifact", re.compile(r"global-" + re.escape(OLD_SLUG) + r"-vertical")),
    # The published paper's title. Its change is gated on the open Zenodo
    # decision in WP-HTF-0007, so the title string is a record until then —
    # while the repository URL on the same page is a live reference and does
    # get rewritten. Hence a pattern, not a whole-file exclusion.
    ("published-title", re.compile(r"Global " + re.escape(OLD_NAME))),
    # Already renamed. Without this, "Catastrophic Hydrotectonic Flood Model"
    # contains OLD_NAME and would be rewritten to "Catastrophic Catastrophic
    # Hydrotectonic Flood Model" — and the slug likewise. Makes the sweep
    # idempotent, so a second run is a no-op rather than a corruption.
    ("already-renamed", re.compile(re.escape(NEW_NAME))),
    ("already-renamed", re.compile(re.escape(NEW_SLUG))),
]

# Whole files that are dated records of what was done or published. Their prose
# is left verbatim even where it names the programme: correct forward, do not
# rewrite the record.
LEAVE_FILES = {
    "00-program-methods/publishing/ZENODO_METADATA.txt",
    "00-program-methods/publishing/ZENODO_SUBMISSION_CHECKLIST.md",
    "dev-notes/20260818-name-catastrophic-hydrotectonic-model.md",
    "04-visualization-assets/videos/intro/social-media-summaries.md",
    "04-visualization-assets/videos/global-intro/social-media-summaries.md",
}
LEAVE_DIRS = ("research/", "social-media/")

# Self-referential: this tool and its work package quote both the old and new
# names deliberately, as the record of what was changed and why.
LEAVE_FILES |= {
    "00-program-methods/tools/rename_sweep.py",
    "05-work-packages/WP-HTF-0007-name-change/package.yaml",
}

TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".py", ".cff", ".json"}


def repo_files():
    for p in sorted(REPO.rglob("*")):
        if not p.is_file() or ".git" in p.parts:
            continue
        if p.suffix.lower() in TEXT_SUFFIXES:
            yield p


def classify(line, start, end):
    """Return (role, is_rename) for one occurrence at [start,end) in line."""
    for role, pat in LEAVE_PATTERNS:
        for m in pat.finditer(line):
            if m.start() <= start and end <= m.end():
                return role, False
    return "live-reference", True


def scan():
    plan, leave = [], []
    for path in repo_files():
        rel = path.relative_to(REPO).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if OLD_SLUG not in text and OLD_NAME not in text:
            continue

        file_is_record = rel in LEAVE_FILES or rel.startswith(LEAVE_DIRS)

        for lineno, line in enumerate(text.splitlines(), 1):
            for pat, kind in ((re.escape(OLD_SLUG), "slug"), (re.escape(OLD_NAME), "name")):
                for m in re.finditer(pat, line):
                    role, rename = classify(line, m.start(), m.end())
                    if file_is_record:
                        role, rename = "dated-record", False
                    (plan if rename else leave).append((rel, lineno, kind, role, line.strip()[:100]))
    return plan, leave


SUBST = {OLD_SLUG: NEW_SLUG, OLD_NAME: NEW_NAME}
# Slug alternative first so the longer, more specific match wins where both
# could apply. Every match is re-classified against the original line before
# it is substituted, so a single pass cannot touch a LEAVE occurrence.
COMBINED = re.compile("|".join(re.escape(k) for k in (OLD_SLUG, OLD_NAME)))


def apply(plan):
    """Substitute only occurrences classified as live references."""
    touched = {rel for rel, *_ in plan}
    for rel in sorted(touched):
        path = REPO / rel
        out = []
        for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
            def sub(m, _line=line):
                _role, rename = classify(_line, m.start(), m.end())
                return SUBST[m.group(0)] if rename else m.group(0)

            out.append(COMBINED.sub(sub, line))
        path.write_text("".join(out), encoding="utf-8")
    return touched


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    plan, leave = scan()

    print(f"RENAME ({len(plan)}):")
    for rel, lineno, kind, _role, snippet in plan:
        print(f"  {rel}:{lineno} [{kind}] {snippet}")

    counts = {}
    for _rel, _ln, _k, role, _s in leave:
        counts[role] = counts.get(role, 0) + 1
    print(f"\nLEAVE ({len(leave)}):")
    for role, n in sorted(counts.items()):
        print(f"  {role}: {n}")

    if not args.apply:
        print("\ndry run — nothing written. re-run with --apply")
        return 0

    touched = apply(plan)
    print(f"\napplied to {len(touched)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
