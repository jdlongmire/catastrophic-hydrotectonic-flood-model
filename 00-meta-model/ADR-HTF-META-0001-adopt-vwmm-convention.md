# ADR-HTF-META-0001 — Adopt the VWMM structural convention

- **Status:** Proposed (JD's to accept — see *Authority* below)
- **Date:** 2026-08-18
- **Package:** [`WP-HTF-0001`](../05-work-packages/WP-HTF-0001-vwmm-refactor/package.yaml)
- **Supersedes:** the ad-hoc `00-program-methods` / `01-hypothesis` / `02-theory` / `03-prediction` tier layout used from stand-up (2026-08-16) to this refactor

## Context

This programme was stood up on a four-tier layout inherited from its sibling programmes (CAC, FCD, TRT): a Tier-0 methods directory plus one directory per rung of the Lakatosian ladder. That layout served its purpose and encoded a real distinction — hard core, protective belt, prediction — that any replacement must preserve.

Separately, [`mxm-assistant-001`](https://github.com/ologos-repos/mxm-assistant-001)'s `ADR-MXM-META-0001` (2026-08-07) declares the **VWMM** convention (`00-meta-model` … `05-work-packages`, zero-padded) the org-wide structural standard going forward. This repo already adopted one half of that standard when `05-work-packages/` was framed on 2026-08-17; the tree itself remained on the old layout, so the repo was internally inconsistent — a work-package directory from one convention sitting beside tiers from another.

## Decision

Adopt the VWMM convention in full. The Lakatosian ladder is **preserved as sub-numbering inside the solutions baseline** rather than as top-level directories, so nothing the old layout encoded is lost:

| Was | Now | Note |
|---|---|---|
| `01-hypothesis/hard-core.md` | `03-solutions-baseline/3.1-hypothesis/` | the hard core, immune by decision |
| `02-theory/{kinematics,rheology,stratigraphy,water-ledger}/` | `03-solutions-baseline/3.2-theory/` | the protective belt |
| `03-prediction/{appraisal,discriminators}.md` | `03-solutions-baseline/3.3-prediction/` | the appraisal and the Tier 3 candidates |
| `00-program-methods/research-practices.md` | `04-construct/methods.md` | the 20 working rules |
| `00-program-methods/METHODOLOGY.md` | `04-construct/methodology.md` | the Popper/Lakatos apparatus |
| `00-program-methods/ROADMAP.md` | `01-strategic-baseline/1.2-strategy/roadmap.md` | the positive heuristic is strategy |
| `05-work-packages/PI-01.md` | `01-strategic-baseline/1.3-objectives-krs/PI-01.md` | PI-01 anticipated this move in its own header |

## Deviations from the convention, and why

WP-HTF-0001's mapping was silent on four files. Each call is recorded here rather than left to be inferred from the tree.

**1. `04-visualization-assets/` → `assets/`.** A genuine collision: the old tree's `04-` was visualization assets, the new tree's `04-` is the construct. Assets moved out of the numbered space entirely rather than being renumbered, because they are not a baseline — they are material the baselines cite. They now sit unnumbered alongside the other working directories (`dev-notes/`, `research/`, `social-media/`), which is what they always were.

**2. `POSITION-PAPER.md` + `publishing/` → `paper/`.** The position paper consolidates the hard core, both mechanisms, the water budget, the open questions and the discriminators — it spans all three solution tiers. Filing it under any one of 3.1/3.2/3.3 would misrepresent its scope, so it sits at `paper/` with the submission record that produced its DOI. This deviates from TRT, which files its paper under `1-hypothesis/paper/`; the deviation is deliberate and the reason is scope, not preference.

**3. `METHODOLOGY.md` → `04-construct/methodology.md`, not a 5M filename.** The construct directory is nominally the 5M+1 surface. Rather than force `methodology.md` into `mind.md` and invent `mission.md` / `morals.md` / `memory.md` to complete a set, the two files that genuinely exist keep their own names: `methodology.md` (how the programme reasons — the Lakatosian apparatus) and `methods.md` (how work is done — the 20 rules). **The other 5M surfaces are not instantiated and no placeholder pretends otherwise.**

**4. `tools/rename_sweep.py` → `04-construct/means/ops/`.** Programme tooling belongs with the operational layer, not beside the methods prose.

## What did not move

`dev-notes/`, `research/`, and `social-media/` stay at the root. They are deliberately outside the numbered apparatus: `research/` is the founding transcript and its sources, `dev-notes/` is working discussion that graduates into the belt or stays open, `social-media/` is published derivative copy. Numbering them would imply they are baselines.

## Consequences

**Gained.** One convention across the repo. Work packages, PI planning and the baselines now share a spine, and the `02-systems-baseline/` skeleton gives requirements, interfaces and verification somewhere to land — `2.5-verification/` in particular now has a home for the discriminator conditions, which previously existed only inside `discriminators.md`.

**Cost, stated plainly.** Every external link into this repo's old paths is broken, including any link in the position paper's own published PDF, which is immutable. GitHub does not redirect moved *paths* the way it redirects a renamed repo. This is a real cost of the refactor and it is not recoverable; it is accepted because the alternative is carrying two conventions indefinitely.

**Empty scaffolding.** `02-systems-baseline/` and most of `01-strategic-baseline/` are stubs. A stub that says "not yet instantiated" is honest; a stub that reads as though content exists is not, and the directory READMEs are written accordingly.

## Verification

Recorded at the time of the move:

- `linkcheck.py`: **0 unresolved relative links** across the tree (109 were broken immediately after the moves; all repaired by script).
- Link repair was **scripted, driven by git's own rename map** (`relink.py`), not hand-edited — both hand-done renumber sweeps on 2026-08-17 broke cross-references, which is why the package made scripting mandatory.
- All 29 renames recorded by git at **R100** (100% similarity), which is independent evidence that the moves changed no file content.
- Content diff outside link targets: **empty**, confirming the package's "moves and relinks only" scope bar held.

## Authority

WP-HTF-0001's `authority_boundary` authorizes the structural moves, the link repair, and the authoring of this ADR without re-asking. **It does not authorize accepting it.** Status stays *Proposed* until JD accepts.
