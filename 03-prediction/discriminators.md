# Discriminators — the critical path

> **Tier 3.** This directory holds claims that *forbid* something. It currently holds none. This file states what a discriminator would have to look like here, names the two live candidates, and names the gate everything else sits behind.

## Why this is the critical path

The belt (kinematics, rheology, water ledger, stratigraphy) can all be built out further and leave the programme exactly where it is: coherent, elaborate, and forbidding nothing. Only a discriminator changes the programme's Lakatosian status.

## What counts

A discriminator is a claim, stated **before** evaluation, that:

1. **Forbids** — some observation is inconsistent with it.
2. **The rival (ordinary historical geology) permits it**, or forbids a different observation. A claim both accounts forbid discriminates nothing.
3. **Is evaluable** against existing or reachable data, against a defined sample.
4. **States its failure condition first.**

## The gate: the rheology / heat-budget problem

Nothing below is reachable in a way that survives scrutiny until the programme can show that transient mantle viscosity in the 10¹³–10¹⁴ Pa·s range is physically achievable during the catastrophic interval, via some quantified combination of water-weakening and thermal feedback — or concedes it isn't, which would itself be a real result. Every kinematic claim in the initial research (continental velocities ~10⁻¹ m/s, slab descent to transition-zone depths within the Flood year) is conditioned on this. Checked against current geodynamic literature (2026-08-16), and against the model's own specified mechanism (water content in ringwoodite/wadsleyite, not partial melt): the largest documented water-specific viscosity reduction on the correct mineral (Fei et al. 2017, ~3.5 orders of magnitude, anhydrous→water-saturated ringwoodite) narrows the gap from a standard transition-zone baseline to roughly 3–4 orders of magnitude short of the requirement — down from the 5–6 orders found when the requirement was compared against an unrelated partial-melt floor (~10¹⁹ Pa·s). See [`../02-theory/rheology/README.md`](../02-theory/rheology/README.md) and [`../dev-notes/20260816-water-weakening-mechanism.md`](../dev-notes/20260816-water-weakening-mechanism.md). This is not a preliminary to the discriminator hunt. It is the discriminator hunt, stated precisely: a real, correctly-targeted mechanism narrows the gap; whether the remaining 3–4 orders can be reached — via thermal feedback, strain-rate localization, or an effect not yet in the literature — is still what determines whether the programme's core mechanism is physically excluded, regardless of how the stratigraphy comes out.

## Where to hunt

### 1. Ecological-province co-occurrence → stratigraphic co-occurrence

The initial research's strongest candidate. If stratigraphic ordering is produced primarily by progressive geographic destruction of ecological provinces — rather than hydrodynamic sorting, or, on the rival account, temporal succession — then taxa that co-occurred geographically/ecologically before the catastrophe should co-occur stratigraphically more often than taxa separated by habitat geography, controlling for transport and preservation. This has real discriminating content: ordinary historical geology's explanation for stratigraphic ordering is temporal succession, not geographic-province destruction order, so the two accounts make different structural predictions about *which* co-occurrences should be strong. Needs: an operational definition of "ecological province" from the pre-catastrophic record, a defined statistical test, and the failure condition (what co-occurrence pattern would falsify it) written down before the formations are checked.

### 2. Cross-basin coherent propagation front

The initial research's own proposed "next decisive analysis": strip ages from several well-characterized basins on different continents, identify the last persistent pre-catastrophic surface and the onset of high-energy catastrophic sedimentation in each, and test whether the onsets compose into one geographically coherent, ~1-year-bounded propagation field. Currently zero specified content — no candidate geometry, no proposed initiating location committed to beyond "maybe Chicxulub, maybe not." Promotion to a real discriminator requires actually proposing a geometry and a rule for what a basin's data would have to show to break it, before checking basins against it.

### 3. MTZ hydration spatial correlation — not yet a discriminator

The initial research cites an already-known pattern (subducted-slab regions run colder, more wadsleyite-enriched, somewhat more hydrated) and treats it as support. That's accommodation of an existing observation, not a prediction — it was known before the claim was made, and the rival account (ordinary subduction over conventional timescales) predicts the same correlation. This clears the bar only if it can be sharpened into something the rival wouldn't also expect — e.g. a specific quantitative relationship, or hydration in a location/pattern that a gradual multi-hundred-million-year subduction history would not produce but a single catastrophic-year event would.

### 4. Seismic texture discontinuity at the lithoplaning/undisturbed-mantle boundary — 2026-08-16, ported

If lateral translation was hydroplaning-driven and confined to the shallow lithosphere (per the mechanism reframe in [`../02-theory/kinematics/README.md`](../02-theory/kinematics/README.md)), tomography should show a texture discontinuity between chaotic, reworked upper lithosphere (0–200 km) and coherent, undisturbed deep mantle (>400 km) — a real structural signature, not a compatibility claim. Ordinary plate tectonics over geological time predicts smoother, gradational structure, not a sharp discontinuity at that depth. Ported from JD's prior slice; not yet checked against actual tomographic datasets here.

### 5. Fluid-dominated detachment fabric — 2026-08-16, ported

Large-scale detachment horizons should show predominantly fluid-related fabrics with minimal pseudotachylite (frictional melt) — expected under near-lithostatic pore pressure (friction collapsed, so little frictional heating to produce melt). The rival account (ordinary tectonics, or a dry catastrophic-friction model) predicts the opposite: significant pseudotachylite from sustained high-friction sliding. Not yet checked against field exposures.

### 6. Basin-margin megabreccia signature — 2026-08-16, ported

Chaotic megabreccia at basin boundaries with multi-lithology mixing, fluid-flow textures, and rapid-emplacement signatures — a specific depositional signature distinguishing rapid hydroplaning-driven emplacement from slow accumulation. Not yet checked against a defined sample of basin margins.

**Confidence on 4–6:** these are stated as candidate discriminators in the source document with real `forbids` content, but none has been run against actual data yet — same status as discriminators 1–3 above (real candidates, unevaluated).

## Checked and rejected — kept, not deleted

### K-Pg boundary ichnofabric vs. physical sedimentary structure (proposed and killed 2026-08-17)

Proposed on the reasoning that the *kind* of disturbance in the K-Pg boundary clay should discriminate: biogenic mixing (ichnofabric — burrows, mottling, cross-cutting traces) implies substrate stability and favours the rival, while hydraulic reworking (grading, sorting, traction lamination, rip-up clasts) favours catastrophic deposition. The sample looked ideal — the boundary clay is among the most intensively sampled horizons in geology.

**Killed on checking the literature before registering it.** A dedicated body of work already answers the question, and against the proposal: at the Caravaca section (SE Spain) the boundary layer is cross-cut vertically by *Zoophycos* and *Chondrites* and penetrated laterally by *Chondrites*, with a trace-fossil assemblage running continuously into the uppermost Maastrichtian (Rodríguez-Tovar & Uchman 2008, *Geobios*); Alegret et al. (2015, *Terra Nova*) is titled "How bioturbation obscured the Cretaceous–Palaeogene boundary record."

Fails **condition 4** (the evaluation predates the claim, so registering it would be retrodiction) and, fatally, **condition 2** — both accounts permit bioturbation, so the observation discriminates nothing. Full analysis, including what the programme legitimately retains and the unpaid cost it does not, in [`../dev-notes/20260817-ichnofabric-discriminator-checked-failed.md`](../dev-notes/20260817-ichnofabric-discriminator-checked-failed.md).

**A cost recorded here on 2026-08-17 was withdrawn the same day.** The original entry asserted that deep-tier *Zoophycos* requires a stable substrate over a meaningful interval and therefore counted against a catastrophic reading. That was reached from mainstream sources only. Woodmorappe (2006), *Journal of Creation* 20(2):113–122 — a dedicated treatment of this exact objection, read in primary — states that "*Zoophycos* is no longer considered as a slowly-constructed ichnofossil," addresses *Chondrites* by name as well, documents burrowing rates of centimetres to tens of centimetres in seconds to minutes with entire beds overturned in under a day, and proposes Penecontemporaneous Partially Lithified Crusts (PPLCs) as a mechanism for simultaneous bioturbation of superposed horizons. The withdrawal and Woodmorappe's own conceded limitations are in the dev-note.

**What survives is narrower and better posed:** not "can *Zoophycos* form quickly" but Woodmorappe's own stated challenge — whether thick, superposed intervals at high ichnofabric index can form in the available time. **And a new candidate became visible only by reading that literature:** PPLC predicts penecontemporaneous lithification fronts interleaved with bioturbated horizons, which ordinary geology does not. That is potentially a real forbidding claim with a defined sample, and is listed as open work.

## What does not count

- Citing a pattern already documented in the literature as though the model predicted it. **The rejected candidate above is the worked example** — it looked like a clean discriminator right up until the check showed the answer was already published.
- "The model is compatible with X." Compatibility forbids nothing.
- A retrodiction of a fact the stratigraphic mapping was revised to accommodate — this is precisely how the three boundary-redraws in the initial research should not be repeated.
