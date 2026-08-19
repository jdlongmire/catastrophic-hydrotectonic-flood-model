# Cryosphere — Ice Cores and Glaciation

**New belt file, 2026-08-18.** Before this, the appraisal recorded ice cores as "no position" and
glaciation as a structural mechanism (N2 Ice age, phase schema) with no initial condition and no
quantitative content. Both move here to **candidate mechanism identified** — see
[`../../3.3-prediction/appraisal.md`](../../3.3-prediction/appraisal.md) and
[`../../../dev-notes/20260818-dfm-boundary-conditions-gap-ledger.md`](../../../dev-notes/20260818-dfm-boundary-conditions-gap-ledger.md)
§§2–3 for the full derivation. `forbids: none` throughout this file — Tier 2 construction per
[`research-practices.md`](../../../04-construct/methods.md) rule 10. Nothing here is quantitatively
tested.

## Ice cores

**The prior implicit framing was the wrong question.** Squeezing 100,000+ alleged annual layers
into a 6,000-year post-Flood window is not what this programme needs to attempt, because the
hard core and phase schema already permit a pre-Flood polar cryosphere existing for the full
~50–60 ka creation-to-Fall interval (P1 Antediluvian, [`../stratigraphy/README.md`](../stratigraphy/README.md)
§Phase schema). A four-phase ice chronology follows directly:

$$I_{pre} \rightarrow I_{Flood} \rightarrow I_{post\text{-}Flood\ Ice\ Age} \rightarrow I_{modern}$$

$I_{pre}$ can contain genuine annual layers accumulated over tens of thousands of years — nothing
here needs reinterpreting as non-annual by construction. The Flood ($I_{Flood}$) disrupts or
destroys some fraction of the pre-Flood cryosphere by mechanisms not yet specified (this is open
work, not modeled). $I_{post\text{-}Flood\ Ice\ Age}$ is the phase schema's existing N2 — a
second, high-accumulation glacial regime, structurally distinct from $I_{pre}$. $I_{modern}$ is
actualistic (N3).

**The research question this reframes to:** not "how do we compress the record," but can extant
ice cores be partitioned, physically and chronologically, among $I_{pre}$, the catastrophic
transition, accelerated post-Flood accumulation, and later ordinary accumulation — a
core-by-core attribution problem rather than a global compression problem.

**The hard discriminator is unchanged by this reframe, and should not be read as weakened by
it.** A demonstrably continuous sequence, independently annualized by internal markers (seasonal
chemistry, dust, volcanic tephra, cosmogenic isotopes) and external synchronization (orbital
parameters, geomagnetic excursions, known eruptions), whose length exceeds the total chronology
available to it under this model's own partition — $I_{pre}$'s ~50–60 ka plus whatever fraction
of the transition and post-Flood regimes genuinely applies to that specific core — still fails
the model if found. Reframing where annual layers are permitted to live changes what the test
measures; it does not remove the test.

**State: candidate mechanism identified (four-phase chronology). Core-specific chronology and
mass-balance modeling absent.** No physical mechanism for how much of $I_{pre}$ survives the
Flood transition is specified. No named ice cores have been checked against this partition.

## Glaciation — the post-Flood Ice Age's initial condition has changed

The existing N2 Ice age content (Oard's warm-ocean/aerosol-cooled-continent mechanism, singular
on structural grounds, [`../stratigraphy/README.md`](../stratigraphy/README.md) §Phase schema)
implicitly asked the post-Flood Ice Age to build ice mass from nothing. Introducing a pre-Flood
polar cryosphere on a lower-relief supercontinent
([`../../../dev-notes/20260817-initial-conditions-topography-biodiversity.md`](../../../dev-notes/20260817-initial-conditions-topography-biodiversity.md))
gives a different initial-value problem:

$$\text{stable polar glaciation} \rightarrow \text{Flood disruption} \rightarrow \text{warm ocean + atmospheric loading} \rightarrow \text{expanded post-Flood glaciation} \rightarrow \text{deglaciation}$$

**The calculation this licenses, not yet run**, needs as inputs: surviving/preexisting ice mass;
ocean temperature after the catastrophe; evaporation and moisture transport; aerosol forcing;
accumulation rate; ablation; ice-sheet flow; maximum ice volume; deglaciation energy and
meltwater budget. None of these terms exist anywhere in this repo. The closest existing
quantitative content is the rheology gate's thermal work
([`../rheology/README.md`](../rheology/README.md) F1–F3) — but that bounds *tectonic* heat
generation against the friction/PE partition, a different energy budget entirely from the
atmosphere-ocean-cryosphere balance this needs.

**State: structural mechanism and initial conditions specified; coupled climate/ice
mass-energy calculation absent.** Unlike the rheology gate (ROADMAP item 1), this calculation
is not currently gated on anything else in this programme — it is a distinct, reachable
computation once someone commits to running it, following the same discipline as
[`../rheology/code/energy_partition_bounds.py`](../rheology/code/energy_partition_bounds.py):
falsification conditions declared before the run, sourced parameters, deterministic and
re-runnable.

## Layering note

The pre-Flood polar cryosphere's *existence* and extent are DFM boundary conditions (initial
state at deployment), not something this programme derives — see
[`../../3.1-hypothesis/hard-core.md`](../../3.1-hypothesis/hard-core.md)'s third disclosure.
What belongs to this programme specifically is the *transition* — how the Flood-year mechanics
already modeled elsewhere in this belt (translation, orogeny, hydrology) interact with an
existing cryosphere — and the *post-Flood relaxation* calculation named above, which is this
programme's own N2 content, not upstream or downstream.

**Source:** [`../../../dev-notes/20260818-dfm-boundary-conditions-gap-ledger.md`](../../../dev-notes/20260818-dfm-boundary-conditions-gap-ledger.md) §§2–3, capturing a 2026-08-18 thread with JD. No new external literature retrieved for this file.
