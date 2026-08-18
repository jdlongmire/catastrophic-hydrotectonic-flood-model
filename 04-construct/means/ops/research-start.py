#!/usr/bin/env python3
"""research-start — orientation briefing for a research session on this programme.

Ported from TRT's script of the same name under WP-HTF-0001 and re-pointed at
this repo's VWMM tree. Checks bound to machinery this programme does not have
(a traceability build, an OPN-* claim registry, Lean) are not faked green —
they report "not instantiated" and say where that is tracked.

Usage:  python3 04-construct/means/ops/research-start.py
Read-only. Never mutates the repo.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def run(cmd, shell=False):
    try:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True,
                           timeout=60, shell=shell)
        return r.returncode, (r.stdout or "").strip(), (r.stderr or "").strip()
    except Exception as e:  # noqa: BLE001
        return 1, "", str(e)


def hdr(t):
    print("\n" + "=" * 70 + f"\n  {t}\n" + "=" * 70)


def main():
    print("=" * 70)
    print("  Catastrophic Hydrotectonic Flood Model  |  research-start")
    print("=" * 70)

    # --- VCS ---
    hdr("[VCS]")
    _, branch, _ = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    _, porcelain, _ = run(["git", "status", "--porcelain"])
    clean = "clean" if not porcelain else f"{len(porcelain.splitlines())} uncommitted change(s)"
    print(f"  branch: {branch}   working tree: {clean}")
    _, ahead, _ = run(["git", "rev-list", "--count", "origin/main..HEAD"])
    _, behind, _ = run(["git", "rev-list", "--count", "HEAD..origin/main"])
    if ahead.isdigit() and int(ahead):
        print(f"  ⚠ {ahead} commit(s) ahead of origin/main (unpushed)")
    if behind.isdigit() and int(behind):
        print(f"  ⚠ {behind} commit(s) behind origin/main (pull)")
    _, log, _ = run(["git", "log", "-5", "--oneline"])
    print("  recent commits:")
    for ln in log.splitlines():
        print(f"    {ln}")

    # --- Standing verdict: the number that matters most ---
    hdr("[Appraisal verdict]")
    appraisal = ROOT / "03-solutions-baseline/3.3-prediction/appraisal.md"
    if appraisal.exists():
        for ln in appraisal.read_text(encoding="utf-8").splitlines():
            s = ln.strip()
            if s.startswith("**") and any(k in s for k in ("ppraised", "rogressive", "egenerating")):
                print(f"  {s}")
                break
    disc = ROOT / "03-solutions-baseline/3.3-prediction/discriminators.md"
    if disc.exists():
        text = disc.read_text(encoding="utf-8")
        n = text.count("\n### ")
        killed = text.count("killed")
        print(f"  discriminator candidates registered: {n} (checked-and-rejected entries retained: {killed})")

    # --- Work packages ---
    hdr("[Work packages]")
    pkgs = sorted((ROOT / "05-work-packages").glob("WP-*/package.yaml"))
    for p in pkgs:
        status = disposition = "?"
        for ln in p.read_text(encoding="utf-8").splitlines():
            if ln.startswith("status:"):
                status = ln.split(":", 1)[1].strip()
            elif ln.startswith("disposition:"):
                disposition = ln.split(":", 1)[1].strip()[:58]
        print(f"  {p.parent.name:44} {status:10} {disposition}")
    pi = sorted((ROOT / "01-strategic-baseline/1.3-objectives-krs").glob("PI-*.md"))
    if pi:
        print(f"  active plan: {pi[-1].relative_to(ROOT)}")

    # --- Open dev-notes ---
    hdr("[Dev-notes still open]")
    notes = sorted((ROOT / "dev-notes").glob("*.md"))
    any_open = False
    for n in notes:
        if n.name.lower() == "readme.md":
            continue
        head = "\n".join(n.read_text(encoding="utf-8").splitlines()[:6])
        if "Status: open" in head or "Status:** open" in head or "**Open**" in head:
            print(f"  ◯ {n.name}")
            any_open = True
    if not any_open:
        print("  (none flagged open in their header)")

    # --- Link integrity ---
    hdr("[Link integrity]")
    rc, out, _ = run(["python3", "04-construct/means/ops/linkcheck.py", "--quiet"])
    print(f"  {out or 'all relative links resolve'}")

    # --- Not instantiated ---
    hdr("[Not instantiated]")
    print("  traceability/ — README only; claim registry + acyclicity build not built")
    print("    (TRT carries the machinery this would port from; tracked as follow-on)")

    # --- Last session ---
    hdr("[Last session]")
    sess = [s for s in sorted((ROOT / "04-construct/means/sessions").glob("*.md"))
            if s.name.lower() != "readme.md"]
    if sess:
        last = sess[-1]
        print(f"  {last.relative_to(ROOT)}")
        grab = False
        for ln in last.read_text(encoding="utf-8").splitlines():
            if ln.lower().startswith("## carry"):
                grab = True
            if grab:
                print(f"    {ln}")
    else:
        print("  (no session journal entries yet — see sessions/README.md)")

    print("\n" + "=" * 70)
    print("  Ready. Read deeper as the task demands (roadmap, methodology, methods).")
    print("=" * 70)


if __name__ == "__main__":
    main()
