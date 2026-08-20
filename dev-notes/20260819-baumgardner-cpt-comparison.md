# Baumgardner's catastrophic plate tectonics — read against this programme

**2026-08-19.** JD-directed research pass on John R. Baumgardner's CPT, prompted by his
observation that *"his subduction model which led to a prediction that was verified will be
helpful."* Both primary ICC papers were retrieved and text-extracted, not read through
secondary summaries. This note records what CPT actually claims, grades its headline
prediction against this programme's own discriminator standard
([`../03-solutions-baseline/3.3-prediction/discriminators.md`](../03-solutions-baseline/3.3-prediction/discriminators.md)
§What counts), and states what is and is not transferable here.

Name note: **Baumgardner**, not Baumgartner. Los Alamos geophysicist, author of the TERRA
mantle-convection code, which has also been used in mainstream geodynamics work.

## Primary sources retrieved

| Source | Status |
|---|---|
| Baumgardner (2003), *Catastrophic Plate Tectonics: The Physics Behind the Genesis Flood*, Proc. 5th ICC, 113–126 | Full text extracted, read. Confidence **HIGH** |
| Baumgardner (1994), *Runaway Subduction as the Driving Mechanism for the Genesis Flood*, Proc. 3rd ICC | Full text extracted, read. Confidence **HIGH** |
| Schouten, Gebraad, Noe et al. (2024), *Full-waveform inversion reveals diverse origins of lower mantle positive wave speed anomalies*, **Sci. Rep. 14:26708**, doi:10.1038/s41598-024-77399-2 | Abstract retrieved verbatim (nature.com behind an IdP redirect; abstract obtained via an indexing mirror). Full text **not** read. Confidence **HIGH** on abstract content, **MEDIUM** on body |
| Austin, Baumgardner, Humphreys, Snelling, Vardiman & Wise (1994), *Catastrophic Plate Tectonics: A Global Flood Model of Earth History* | Secondary summary only. Confidence **MEDIUM** |
| ICR / AiG popular articles claiming prediction-then-confirmation | Read. See §Novelty below — they supply **no** paper, year, or citation for the prediction claim. Confidence **LOW** on their framing |

## What CPT actually claims

**Mechanism.** Arrhenius temperature dependence of silicate viscosity, $\eta \propto e^{E^*/RT}$,
gives thermal runaway when the viscous-heating time constant falls well below the thermal-diffusion
time of the layer (Gruntfest 1963). Baumgardner adds two laboratory-measured deformation-rate
weakening regimes on olivine: **dislocation (power-law) creep**, strength $\propto \dot\gamma^{-2/3}$,
and **plastic yield**, strength $\propto \dot\gamma^{-1}$. His claim: combined, these "reduce the
silicate strength by ten or more orders of magnitude without the material ever reaching its melting
temperature."

**Numbers, from the 2003 paper directly.**

| Quantity | Value |
|---|---|
| Pre-runaway viscosity, mid-mantle | $3\times10^{24}$ Pa·s |
| Pre-runaway upper mantle / asthenosphere | $5\times10^{20}$ Pa·s |
| **During runaway** | **$10^{13}$–$10^{18}$ Pa·s** (~$10^9$-fold drop) |
| 2D domain | 11560 × 2890 km |
| Timescale | snapshots at 5.0, 12.5, **20 days** |
| 3D spherical run | Pangea initial state, ~120 km resolution, 15 and 25 days |
| Illustrative plate speed | 10 m/s (his own worked example) |

The 2003 paper is the one that matters technically: W.-S. Yang's matrix-dependent-transfer
multigrid solver carried runaway to completion for the first time and allowed plastic yield to be
included at all. The 1994 paper says outright that at the equivalent point "the computation crashes."

**Two admissions worth carrying, both in his own words.** The 3D run does not start from a
pre-Flood Earth: *"it represents a state roughly mid-way into the actual Flood cataclysm
corresponding to the early Mesozoic point in the record."* And on triggering: *"the initial state
from which the runaway emerged was built into the Earth as God originally formed it. In fact, I
believe this almost certainly had to have been the case."* That is a designed-initial-condition
move, stated openly — structurally the same class of move as DFM's $R_0$
([`../03-solutions-baseline/3.1-hypothesis/hard-core.md`](../03-solutions-baseline/3.1-hypothesis/hard-core.md)
third disclosure), which is worth noting *before* anyone treats it as a gotcha against him.

## Heat disposal — and where it fails

CPT's answer to cooling newly formed ocean lithosphere is **supersonic steam jets at spreading
centres exceeding Earth's escape velocity**, exporting heat as kinetic energy: 1 kg of steam at
14 km/s carries ~$10^8$ J, enough to cool 140 kg of rock by 1000 K; ~1000–1500 m of seawater
does the job.

**His internal arithmetic reproduces exactly** (independently recomputed: $9.8\times10^7$ J/kg,
138 kg). The mechanism fails a check the paper does not run. A nozzle converts at most the working
fluid's specific enthalpy into directed kinetic energy, $v_{max} = \sqrt{2h}$. Steam at 1500–3000 K
carries $h \approx 4.5$–$7.5\times10^6$ J/kg, giving $v_{max} \approx$ **3.0–3.9 km/s**. Escape
velocity requires $6.3\times10^7$ J/kg; his 14 km/s requires $9.8\times10^7$ J/kg — **an order of
magnitude more energy per kilogram than the steam contains**. Separately, 1000–1500 m of seawater
is **27–41% of the present ocean**, permanently lost to space.

## The prediction, graded against this programme's own standard

The claim JD flagged. From the 2003 paper: a ring of cold dense rock at the base of the mantle
beneath the Pacific perimeter, correlating with inferred Mesozoic subduction; hot "toothpaste"
blobs beneath Africa and the central Pacific; density contrast 3–4%, converted to **3000–4000 K**;
and the argument that *"such a huge temperature contrast would not be expected if the cold upper
boundary layer rock had taken 100 million years or more to reach the bottom of the mantle."*

Graded on `discriminators.md` §What counts:

**Condition 4 (states its failure condition first) — novelty is weak.** The 1994 paper *cites*
existing tomographic support rather than predicting it. ICR and AiG date the prediction to
"the 1980s"; both were checked and neither supplies a paper, a year, or any citation. The nearest
genuinely novel item is whole-mantle slab penetration through the 660 km discontinuity, confirmed
1997 — but whole-mantle convection was a live *mainstream* position at the time, and Baumgardner
himself co-authored in the mainstream literature on it. **Shared corroboration, not discriminating
corroboration**, which by this programme's own standard contributes nothing to progressiveness.

**Condition 2 (the rival permits it) — fails, and the framing below needs one correction stated first.**

> **Rule 23b correction, 2026-08-19.** The paragraph that follows originally read as though the thermal-diffusion calculation *observationally refuted* Baumgardner. It does not, and cannot. The sinking rate (1–5 cm/yr) and the transit duration (58–289 Myr) are the rival's **reconstruction**, not readings off an instrument — what is observed is seismic wave speed. What the calculation legitimately shows is that **the rival's own account accommodates cold lower-mantle slabs**, which is exactly what condition 2 asks and is sufficient to fail the candidate. The verdict stands; the epistemic framing did not. Corrected forward per rule 6 rather than rewritten. Slab thermal
equilibration is $\tau \approx L^2/\kappa$. At $\kappa = 10^{-6}$ m²/s a 100 km slab stays thermally
distinct for **79 Myr**, a 200 km slab for **317 Myr**. Whole-mantle transit at ordinary 1–5 cm/yr
sinking rates takes **58–289 Myr**. The slab arrives at the core-mantle boundary still cold *under
ordinary tectonics*. Deep time predicts cold lower-mantle slabs too, so the observation separates
nothing, and Baumgardner's "would not be expected" is simply wrong.

**The quantitative form is self-defeating.** His arithmetic is right — 3–4% density at
$\alpha = 10^{-5}$/K does give 3000–4000 K. But his own paper states slabs run *"some 1000 K or
more"* colder than surrounding mantle, and a slab cannot become colder than it started. A 3500 K
cold-to-hot contrast therefore needs the hot side ~2200–2500 K **above** ambient, far above the
mantle solidus. It cannot be a thermal feature under **either** chronology. The load-bearing move
is his explicit assumption that the two regions have *"a similar chemical composition"* — and that
is precisely the assumption mainstream dropped in concluding the LLSVPs are thermochemical piles,
on independent evidence (sharp edges, $V_s$/$V_p$ anticorrelation, normal-mode density constraints).
Not an ad hoc rescue; stated at strength per rule 4.

## The 2024 result — the genuinely strong item, and it cuts both ways

Schouten et al. (2024) applied **global full-waveform inversion**, which is far less dependent on
source-receiver geometry than travel-time tomography. From the abstract, verbatim:

> "Many of these previously undetected anomalies are situated below major oceans and continental
> interiors, with no geologic record of subduction, such as beneath the western Pacific Ocean.
> Moreover, we find no statistically significant correlation positive anomalies as imaged using
> full-waveform inversion and past subduction."

Authors' proposed alternatives run to delamination, small-scale convection, and compositional
heterogeneity. That is mainstream seismologists reporting that the slab-graveyard reading of
lower-mantle fast anomalies does not survive a better imaging method — a real, current,
primary-sourced anomaly in the rival's own literature, which is exactly the rule 12 target class.

**But it dissolves Baumgardner's argument along with the mainstream one, and this must be recorded
rather than skipped.** His 1994/2003 case *rested on* the correlation — *"the location of this ring
correlates closely with the locations inferred for much of the subducted ocean floor."* CPT is a
subduction model. A result finding no statistically significant correlation between these anomalies
and past subduction removes the very correlation he pointed at. ICR citing this paper as CPT
confirmation is selective; it is an anomaly for **anyone** whose account of these structures is
"subducted slabs," CPT included.

## What transfers to this programme

**1. The rheology gate may be a category mismatch, not only a magnitude one.**
[`../03-solutions-baseline/3.2-theory/rheology/README.md`](../03-solutions-baseline/3.2-theory/rheology/README.md)
requires $10^{13}$–$10^{14}$ Pa·s and reports being 3–4 orders short via Fei et al. (2017). But Fei
is a **static** laboratory law — water content in ringwoodite at fixed state. Baumgardner's
weakening is an **emergent output of a dynamical instability**: heating feeds weakening feeds faster
deformation feeds more heating, and his published runaway range ($10^{13}$–$10^{18}$ Pa·s) *reaches
the bottom of this programme's requirement*. A runaway's terminal viscosity cannot be obtained by
looking up a static coefficient, and this gate has only ever been benchmarked against static
coefficients. **This does not close the gate** — it identifies that the comparison class may be
wrong, which is a distinct and cheaper thing to check.

**2. A quantified differentiator this programme was not previously claiming.** Independently
computed here: whole-mantle recycling of ocean lithosphere ($3.1\times10^{14}$ m² × 100 km ×
3300 kg/m³, ~2% density excess, 2890 km descent) releases ~$5.8\times10^{28}$ J — against
$3.5\times10^{27}$ J to boil the present ocean, so **5–17× ocean-vaporisation energy**. This
programme's budget is $10^{25}$ J. **CPT's heat problem is roughly 5,800× this programme's**,
because CPT moves the whole mantle and this mechanism moves crustal blocks on a 15 km detachment
(`WP-HTF-0003`). Related: `WP-HTF-0006`'s F8 global-mean stacking check is precisely the
calculation CPT's defence skips — Baumgardner's *"no evidence of extreme temperatures... because
the rate of deformational heating is proportional to the viscosity"* is a **local rate** argument at
fixed strain rate, and does not touch the integrated budget, which is set by gravitational potential
energy release and is independent of rheology.

**3. A critique of CPT that should NOT be repeated.** The Matsumura/NCSE line that lowering
viscosity "removes the heat source the model needs" is confused: dissipation at fixed stress is
$\tau^2/\eta$, which *rises* as viscosity falls, and the driver is buoyancy, not frictional heat.
Recorded here so this programme does not inherit a bad objection while making a good one. The
associated "thermal diffusivity would need to increase 10,000-fold" claim could not be traced to a
primary calculation — secondary attribution only, **UNCERTAIN**.

**4. The transferable item is the template plus a dataset — not the datum.** Baumgardner's
cold-slab claim is the closest thing in the CPT literature to a temporally-novel quantitative
discriminator in *shape*: a rate claim generating a present-day observable. This programme already
has the analogous candidate — **discriminator 4** (seismic texture discontinuity, chaotic reworked
0–200 km lithosphere vs. coherent mantle >400 km), carried since 2026-08-16 as "ported; not yet
checked against actual tomographic datasets." Schouten et al.'s FWI model is public
(Zenodo record 13991965, 19 GB supplementary) and FWI is specifically the method whose lower
geometry-dependence makes a depth-localized texture claim testable, where travel-time tomography's
smoothing would blur the predicted discontinuity into nothing. `WP-HTF-0011` is seeded against this.

**5. The sharpest point — this differentiates CHFM from CPT, in CHFM's favour.** This programme's
mechanism is shallow lithoplaning on a 15 km detachment, which predicts the deep mantle is largely
**undisturbed**. CPT predicts the deep mantle is full of recently-subducted pre-Flood ocean floor.
Schouten's "no correlation with subduction" damages the second and is neutral-to-favourable for the
first. That is an intra-family discriminator, and it is the kind of claim that would *forbid*
something — which is what
[`../03-solutions-baseline/3.3-prediction/appraisal.md`](../03-solutions-baseline/3.3-prediction/appraisal.md)
keeps logging as absent.

**Caveat flagged before it can be quietly skipped:** Schouten et al.'s focus is the **lower**
mantle, while discriminator 4's boundary sits at 200–400 km. Whether that model's shallow
resolution supports the test is an open question and is written into `WP-HTF-0011` as a
pre-registered third outcome, not assumed away.

## Correction, same day — the harvest is component-level, not package-level

**JD, 2026-08-19:** *"I'm not trying to adopt his entire model but to harvest the components that are
useful to mine."* The framing in §What transfers item 3 above — that adopting his route "would
reimport a budget three orders of magnitude larger" — is package-shaped and wrong as a general
statement. **The ~5.8×10²⁸ J travels with whole-mantle overturn, not with the components.** Kept
above rather than rewritten, per rule 6; corrected here.

The separable inventory, stated properly:

| Component | Verdict |
|---|---|
| **Gruntfest (1963) shear-layer runaway criterion** | **Take.** A general stability result for *any* shear zone, not mantle-specific and not his. Applies directly to this programme's 15 km detachment — `WP-HTF-0012` |
| **Kirby (1983) olivine deformation map** (Arrhenius + dislocation creep $\dot\gamma^{-2/3}$ + plastic yield $\dot\gamma^{-1}$) | **Take.** Laboratory mineral physics Baumgardner *applied*, did not produce. What mainstream contests is his claim that mantle conditions reach the runaway criterion, not the law |
| **The envelope insight** — heating concentrates in the mechanical boundary layer *surrounding* the moving block, not in the block | **Take.** Geometric, no mantle assumptions. This programme's detachment *is* an envelope |
| Yang's matrix-dependent-transfer multigrid solver | Separable but low value — this programme runs scalar budget calculations, not FEM |
| Gravitational PE from emplaced density contrast as the energy source; designed initial condition | **Already held** — convergent, not borrowed. His open statement that the initial state was *"built into the Earth as God originally formed it"* is worth citing as precedent that a CPT-family figure makes the same move |
| **Whole-mantle overturn architecture** | **Leave.** This is what carries the 5.8×10²⁸ J |
| **Supersonic steam-jet cooling** | **Leave.** Fails the enthalpy ceiling above by an order of magnitude in energy per kilogram |
| **Deep cold-slab prediction** | **Leave.** Fails discriminator condition 2 on the thermal-diffusion check above |
| **Accelerated nuclear decay** (he cites Humphreys/RATE) | **Leave.** This programme's DFM $R_0$ route avoids it and is the better position |

**The harvest payoff is a calculation on this programme's own mechanism, not a borrowed claim.**
Applying Gruntfest to the lateral detachment tests something F7/F8 never touched: those bound flux at
the *surface*, and say nothing about temperature *inside* the shear zone, which is where a runaway
would occur. It also closes standing open business — [`20260816-heat-problem-clarification.md`](20260816-heat-problem-clarification.md)
has been marked open since 2026-08-16 on exactly this question, and its §2 pushback is correct about
volumetric dissipation and incorrect about temperature. Seeded as `WP-HTF-0012`; the load-bearing
input is a shear-zone thickness the belt has never stated, now named in
[`../03-solutions-baseline/3.2-theory/kinematics/README.md`](../03-solutions-baseline/3.2-theory/kinematics/README.md).

## Status

**Tier 2 conceptual work plus verification of external claims. `forbids: none` in itself.**
Nothing here was tested against data; what it does is identify one testable path
(`WP-HTF-0011`), one possible category error in an existing gate, and one quantified differentiator.
The appraisal verdict is unchanged: unappraised, zero discriminators evaluated.
