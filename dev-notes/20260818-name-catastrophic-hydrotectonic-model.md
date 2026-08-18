# Candidate rename — "Catastrophic Hydrotectonic Model"

**Status: open.** JD is considering it, has not landed on it. Using it as a session title only for now (`devops - catastrophic-hydrotectonic-model-20260818-02`). Nothing in the repo, the DOI, or the published paper has been changed. Captured here so the consideration survives the session rather than living in a chat transcript.

## The candidate

Current name, everywhere: **Hydrotectonic Flood Model** (`jdlongmire/hydrotectonic-flood-model`). Candidate: **Catastrophic Hydrotectonic Model**. Two changes in one, worth separating before either gets decided:

1. **Adding "catastrophic."**
2. **Dropping "flood."**

## What "catastrophic" would do

"Catastrophic" is not a neutral intensifier in this literature. **Catastrophic Plate Tectonics (CPT)** is the established Baumgardner-lineage term for the rival-adjacent model family, and this programme already engages it by name in three places: `02-theory/rheology/README.md` (the runaway-subduction feedback is described as consistent with Baumgardner-style proposals), `dev-notes/20260816-heat-problem-clarification.md` (which distinguishes the CPT-style viscous-dissipation problem from the vapor-canopy latent-heat problem), and JD's own predecessor paper title — *"A Solution to the Heat Problem in Catastrophic Plate Tectonics"* (10.5281/zenodo.17684983).

**The upside is real positioning.** The name would locate the programme inside the recognized catastrophist family rather than as an unaffiliated one-off, and it advertises the shared commitment honestly: this is a catastrophist model, and it says so in its title.

**The cost is that it imports the objection.** The CPT heat critique is, right now, this programme's own gating open problem — `02-theory/rheology/README.md` states the required 6–8 order-of-magnitude transient-viscosity drop and explicitly does *not* show the feedback can reach it, and the heat-problem dev-note remains **open** on which heat problem the programme has actually sidestepped. Taking "catastrophic" into the title makes the unpaid CPT-family bill part of the programme's name before the bill is paid. That may be exactly the right honest move, or it may be premature branding; it is JD's call, not a structural one.

There is a narrower reading worth putting on the table: the predecessor paper's framing was *a solution to the heat problem in CPT*, which positions this work as CPT's repair rather than CPT's member. If that is the intent, a name that says "catastrophic" without qualification understates it — the differentia is the hydraulic/hydroplaning mechanism, which the current name already carries in "hydrotectonic."

## What dropping "flood" would cost

The hard core is Genesis-historical (`01-hypothesis/hard-core.md`); the programme is a Flood reconstruction, and "Flood" in the title is what makes the scope legible to both audiences it has to reach — the creationist literature it argues within, and the mainstream literature it cites against. "Catastrophic Hydrotectonic Model" is mechanism-only and would read, to someone encountering it cold, as a general tectonics proposal. A third option preserves both: **Catastrophic Hydrotectonic Flood Model**, at the cost of a four-word name.

## Cost of executing the rename

Measured, not estimated:

- **44 occurrences** of the repo slug `hydrotectonic-flood-model` across **19 files**.
- **27 files** mention "hydrotectonic" as a word (title lines, prose, the position paper).
- **DOI 10.5281/zenodo.21972859**, published 2026-08-16, whose metadata and reference list name both the repo URL and the title. GitHub serves redirects from an old slug after a rename, so existing links would not hard-break. Whether the *published* Zenodo metadata can be edited in place (as opposed to requiring a new version) I have not verified against the live record — check before assuming either way.
- A **third name already exists in the lineage**: `jdlongmire/global-flood-hydrotectonic-model`, the predecessor repo cited in the position paper's references. A second rename compounds the discoverability cost of the first.

## Recommended sequencing, if JD lands on yes

Do it **immediately after WP-HTF-0001, as its own work package — not inside it.** WP-HTF-0001's scope bar is explicit: moves and relinks only, no content change, and "if a content change looks necessary mid-move, it stops and becomes its own package." A rename is content. But 0001 builds the scripted link-repair machinery (mandatory-scripted, because two hand sweeps on 2026-08-17 broke cross-references), and a rename sweep is that same machinery pointed at a different mapping table. Running the rename right after 0001 reuses the tooling while the scope boundary stays clean.

If JD lands on **no**, this note stays as the record of why the current name was kept, which is worth as much as the record of a change.

## Disposition

Open. Nothing renamed. Session title only. Decision is JD's; the three separable questions are (1) add "catastrophic"? (2) keep "flood"? (3) rename the repo slug and the published title, or only the display title?
