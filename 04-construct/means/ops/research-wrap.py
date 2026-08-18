#!/usr/bin/env python3
"""research-wrap — end-of-session hygiene gate for this research programme.

Ported from TRT's script of the same name under WP-HTF-0001. A pass/fail gate
run at the session transition: don't claim a session done if any check FAILs.

Two of TRT's gates have no counterpart here and are deliberately absent rather
than stubbed: the Lean core typecheck (no formalization) and the traceability
acyclicity/freshness build (no claim registry). In their place this repo gates
on what actually broke here — link integrity, after two hand-done renumber
sweeps broke cross-references on 2026-08-17 — and on the attribution invariant.

Usage:  python3 04-construct/means/ops/research-wrap.py
Exit code is nonzero if any gate check FAILs.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
results = []


def run(cmd, shell=False):
    try:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True,
                           timeout=120, shell=shell)
        return r.returncode, (r.stdout or "").strip(), (r.stderr or "").strip()
    except Exception as e:  # noqa: BLE001
        return 1, "", str(e)


def add(level, label, detail=""):
    results.append((level, label, detail))


def main() -> int:
    print("=" * 70)
    print("  Catastrophic Hydrotectonic Flood Model  |  research-wrap")
    print("=" * 70)

    # 1. Working tree clean
    _, porc, _ = run(["git", "status", "--porcelain"])
    if porc:
        add("FAIL", "uncommitted changes",
            f"{len(porc.splitlines())} file(s) — commit before wrapping:\n    "
            + "\n    ".join(porc.splitlines()[:20]))
    else:
        add("PASS", "working tree clean")

    # 2. Unpushed commits
    _, ahead, _ = run(["git", "rev-list", "--count", "origin/main..HEAD"])
    if ahead.isdigit() and int(ahead):
        add("WARN", "unpushed commits", f"{ahead} ahead of origin/main — push if intended")
    else:
        add("PASS", "synced with origin/main")

    # 3. Link integrity — the check this repo earned the hard way
    rc, out, _ = run(["python3", "04-construct/means/ops/linkcheck.py", "--quiet"])
    if rc == 0:
        add("PASS", "link integrity", "all relative links resolve")
    else:
        add("FAIL", "link integrity", out.splitlines()[0] if out else "unresolved links")

    # 4. Attribution invariant — no model or supplier byline anywhere.
    # Anchored at line start so that *documenting* the banned forms (this file,
    # the QA profile, mode.md) is not itself flagged. The rule targets a work
    # product claiming a model as its author, not prose naming the rule.
    rc, hits, _ = run(
        r"grep -rIn --exclude-dir=.git -iE "
        r"'^[[:space:]]*(co-authored-by:|generated (with|by) (claude|gpt|gemini|chatgpt)|"
        r"(\*\*)?(author|analyst|reviewer|validator|prepared by)(\*\*)?[[:space:]]*:[[:space:]]*"
        r"(\*\*)?[[:space:]]*(claude|gpt-|opus|sonnet|haiku|gemini))' . || true", shell=True)
    if hits.strip():
        add("FAIL", "attribution", "model/supplier byline found:\n    "
            + "\n    ".join(hits.splitlines()[:5]))
    else:
        add("PASS", "attribution", "no model or supplier byline")

    # 5. Work packages parse and carry required fields
    try:
        import yaml  # noqa: PLC0415
        required = {"id", "title", "scope", "authority_boundary",
                    "actions", "verification", "disposition", "status"}
        bad = []
        for p in sorted((ROOT / "05-work-packages").glob("WP-*/package.yaml")):
            d = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
            missing = required - set(d)
            if missing:
                bad.append(f"{p.parent.name}: missing {sorted(missing)}")
        if bad:
            add("FAIL", "work-package schema", "\n    ".join(bad))
        else:
            add("PASS", "work-package schema", "all packages carry required fields")
    except ImportError:
        add("WARN", "work-package schema", "pyyaml unavailable — not checked")

    # 6. Cited computations still run
    script = ROOT / "03-solutions-baseline/3.2-theory/rheology/code/energy_partition_bounds.py"
    if script.exists():
        rc, _, err = run(["python3", str(script.relative_to(ROOT))])
        if rc == 0:
            add("PASS", "computations reproduce", script.name)
        else:
            add("FAIL", "computations reproduce",
                f"{script.name} exited {rc}: {(err.splitlines() or [''])[-1]}")

    # 7. GitHub-safe math
    rc, hits, _ = run(r"grep -rn '\operatorname' --include='*.md' . | grep -v '`' || true",
                      shell=True)
    if hits.strip():
        add("FAIL", "math-lint", "use \\mathrm:\n    " + "\n    ".join(hits.splitlines()[:5]))
    else:
        add("PASS", "math-lint", "no \\operatorname in committed math")

    # --- Session journal reminder ---
    # ':!*README.md' excludes the directory's own README: adding it is not
    # writing a session entry, and counting it as one made the check lie on
    # the very first run.
    _, recent, _ = run("git log -1 --since='12 hours ago' --name-only --pretty=format: "
                       "-- 04-construct/means/sessions ':!*README.md' || true", shell=True)
    if recent.strip():
        add("PASS", "session journal", "entry touched recently")
    else:
        add("WARN", "session journal",
            "append an entry to 04-construct/means/sessions/ before wrapping")

    # --- Report ---
    print()
    icon = {"PASS": "✓", "WARN": "⚠", "FAIL": "✗", "INFO": "·"}
    for level, label, detail in results:
        print(f"  [{icon[level]}] {level:4} {label}" + (f" — {detail}" if detail else ""))

    fails = [r for r in results if r[0] == "FAIL"]
    warns = [r for r in results if r[0] == "WARN"]
    print("\n" + "=" * 70)
    if fails:
        print(f"  RESULT: FAIL — {len(fails)} blocking issue(s), {len(warns)} warning(s). Not wrapped.")
        print("=" * 70)
        return 1
    print(f"  RESULT: PASS — {len(warns)} warning(s). Safe to wrap.")
    print("  Then: append the session journal + update the appraisal as needed.")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
