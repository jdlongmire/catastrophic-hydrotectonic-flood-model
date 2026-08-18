# Water Ledger

Belt content: a four-reservoir water-mass balance (ocean, surface/crustal, atmospheric, deep mantle) conserved across pre-Flood, Flood-year, and present states, without requiring a different total terrestrial water inventory than observed today — only a different partitioning.

**From the initial research:** using USGS present-day figures (1 OE = 1.338×10⁹ km³ ocean; 2.34×10⁷ km³ groundwater, both verified 2026-08-16), a pre-Flood crustal-water excess of 0.05–0.15 OE is proposed, partitioned across upward discharge / deep transport / retention (illustrative 50/30/20 split). Deep-transported water is directed toward the mantle transition zone, where wadsleyite/ringwoodite are established water hosts (Pearson et al. 2014 natural ringwoodite inclusion, ~1.4 wt%, verified).

**Explicitly not core, explicitly not measured:** the excess magnitude, the partition coefficients, and the resulting mantle-water inventory are all stated in the initial research as hypothesis parameters. No independent constraint has been proposed for any of them yet.

## Supply-rate check, 2026-08-16 — ported from JD's prior slice

A gap this ledger didn't previously address: does the crustal "sponge" actually stay saturated under load during the collapse, or does it drain faster than it's resupplied? Ported from [`jdlongmire/global-flood-hydrotectonic-model`](https://github.com/jdlongmire/global-flood-hydrotectonic-model) Appendix F (Darcy flow calculations): comparing consolidation-drainage demand (~5×10⁵ m³/s, from Terzaghi consolidation theory at 1% compression) against fracture-network supply (~4×10⁸ m³/s, Darcy's law through a channeled-porosity architecture, k ~10⁻⁸ m²) gives roughly an **800:1 excess supply capacity**. The porous zone does not run dry mid-collapse under these stipulated parameters. This is a real, checkable flow-rate calculation, not a restatement of reservoir size — it answers a different question than the OE totals above (whether the water gets there fast enough, not how much there is).

**Caveat carried over honestly:** the porous-zone parameters (thickness 1–5 km, porosity 0.1–0.3, channel permeability 10⁻¹⁰–10⁻⁸ m²) are stipulated for the source repo's Stage 1 architecture, not independently measured or yet checked against this programme's own crustal model. The 800:1 ratio is robust to an order of magnitude of parameter uncertainty (per the source's own sensitivity table), but the parameters themselves are imported, not derived here.

## Atmospheric water-vapor canopy — added 2026-08-16

An inferred pre-Flood atmospheric vapor canopy, $W_{A,0}$, is added as a fifth term: $W_T = W_{O,0} + W_{S,0} + W_{C,0} + W_{A,0} + W_{M,0}$.

This isn't new to Flood geology — it's one of its oldest, most quantitatively developed proposals (Whitcomb & Morris 1961; Dillow 1981; Vardiman, ICR), and it has a well-documented, self-imposed physical ceiling that any figure adopted here has to be checked against rather than assumed away.

**The ceiling, verified 2026-08-16:** modern global mean precipitable water is ~25 mm, giving the present atmosphere's commonly-cited inventory of ~12,900 km³ (≈9.6×10⁻⁶ OE — negligible, and not what a "canopy" would add on top). Two benchmark canopy depths span the range actually proposed in the literature:

| Model | Precipitable water | Volume | OE | Outcome |
|---|---|---|---|---|
| Vardiman's habitability limit | ~20 in (51 cm) | ~2.6×10⁵ km³ | ~1.9×10⁻⁴ OE | The largest canopy Vardiman's own climate modeling found compatible with a livable surface — larger canopies drove surface temperature past habitability |
| Dillow (1981), original | ~40 ft (12.2 m) | ~6.2×10⁶ km³ | ~4.7×10⁻³ OE | Dillow's own corrected greenhouse calculation put resulting surface temperature at 1,144°C — uninhabitable |

**The honest reading:** across the full range the vapor-canopy literature itself has proposed, the canopy cannot contribute materially to the water budget without becoming thermodynamically uninhabitable. At the only surface-habitable scale (Vardiman's ceiling), it adds ~1.9×10⁻⁴ OE — roughly 0.1–0.4% of the crustal-water excess (0.05–0.15 OE) already carrying this ledger's mass balance. It does not change the existing partition meaningfully in either direction.

**Why include it anyway:** as a named initial condition it's a legitimate belt hypothesis, and the ledger should account for every reservoir directed to be in $S_0$ rather than omit one. But it shouldn't be leaned on as a Flood-water *source* — which is also ICR's own conclusion: "the ejection of water and vapor into the atmosphere during catastrophic events of the Genesis Flood seems to be a better explanation... than from the collapse of a pre-Flood vapor canopy." That is, the water source the canopy's own proponents ultimately preferred over the canopy itself is the mechanism this programme already has — crustal/deep-mantle water release via hydrotectonic failure.

**Thermal cross-reference:** the greenhouse ceiling above is an independent thermal constraint, related to but distinct from the rheology/heat-budget gate ([`../rheology/README.md`](../rheology/README.md)) — one is atmospheric-radiative, the other tectonic-mechanical, but both are "how much energy can this system tolerate before it becomes physically impossible" tests.

**Open:** what specific $W_{A,0}$ value (bounded above by ~1.9×10⁻⁴ OE for habitability) this programme adopts is undetermined — currently a bounded placeholder, not a chosen figure.

**Visualization:** [`initial-supercontinental-crust-model.png`](../../../assets/images/initial-supercontinental-crust-model.png) renders the pre-Flood water-rich crustal cross-section this ledger draws on. No numerical claims to check against it.

## Salinity refugia — preservation of pre-Flood freshwater reservoirs (JD, 2026-08-17)

`forbids: none` — **belt/interpretive content** per [`research-practices.md`](../../../04-construct/methods.md) rule 10. Discriminator candidate flagged at the end, not registered.

JD's addition: the non-uniformity of the flood-water column (see [`../kinematics/README.md`](../kinematics/README.md) §Hydraulic consequences) could preserve some of the massive freshwater reservoirs that pre-existed the Flood, rather than homogenising everything into one mixed body.

**A gap in this ledger it exposes.** Everything above is a **mass** balance across four (now five) reservoirs. **It carries no salinity dimension at all.** Yet the Flood's aquatic outcome depends on salinity distribution, not just total water mass. This section opens that dimension; quantifying it is open work.

**The problem it addresses.** Aquatic organisms were not on the ark — Genesis 7:22 restricts the ark's cargo and the corresponding death to what was "on dry land." Both obligate freshwater and stenohaline marine biota therefore had to survive *in the water*, and a single fully-mixed global water body has one intermediate salinity that is hostile to both. This is a long-recognised problem in flood geology, not one this programme is raising against itself.

**The standard answer in the creationist literature** (searched per rule 8; Answers in Genesis, creation.com; confidence **MEDIUM**, secondary-level, primaries not retrieved) has three limbs: **layered waters** — fresh and salt water differ in density and do not mix instantly, so pockets and layers spanning very fresh to very salty would persist even amid the catastrophe; **euryhalinity** — many freshwater species tolerate salt water and vice versa, as public aquaria exploit routinely, provided salinity changes slowly enough; and **pre-Flood physiology** — less genetically degenerate organisms with wider osmoregulatory range.

**What this model contributes back** (rule 9). The general literature asserts layering as a plausibility. This programme can supply a **mechanism** for it, which is the difference between an assertion and a belt claim. A non-uniform water column over translating continents produces spatially varying shear, and stratified-flow physics says mixing is governed by the local Richardson number, with density fields breaking into patches and layers each carrying a *different local* Ri. Patchy, spatially variable stratification is therefore the expected state of a non-uniform sheared system rather than a special condition that has to be argued for. Freshwater lenses in the modern ocean spread laterally as gravity currents and sit above haloclines that actively inhibit vertical mixing — the same behaviour, observed. Confidence **MEDIUM** on the stratified-mixing figures (secondary summaries).

**The tension with vigorous sorting, and its partial resolution.** The hydraulic section in kinematics emphasises energetic conditions — entrainment, traction transport, accelerated sorting. Strong shear destroys stratification (low Ri), so the two sections pull against each other and that should be said plainly rather than left for a critic. Two things reduce the conflict. First, non-uniformity means *spatially variable* energy by definition: high-energy zones do the sorting, low-energy zones retain stratification, and the model needs both simultaneously in different places rather than one everywhere. Second, and more structurally, the two phenomena occupy **different parts of the water column** — sediment entrainment and sorting happen at the bed, while a buoyant freshwater lens sits at the surface. They are naturally vertically separated. That is a partial resolution, not a complete one: a translating continent shears the whole column to some degree, so vertical separation reduces the conflict without eliminating it.

**This is a constraint the model now owes, not a free resource.** Requiring both regimes at once converts a qualitative appeal into a quantitative obligation: state the Ri criterion (conventionally Ri > 0.25 for stability against shear instability), and show that the model's own shear field admits regions satisfying it alongside the high-shear regions the sorting argument needs. Not attempted here.

**Discriminator candidate, flagged not registered.** If freshwater refugia persisted *during* the catastrophe, freshwater and marine indicators should appear as **contemporaneous lateral facies** within flood-year strata. Ordinary historical geology explains freshwater/marine interfingering by transgression–regression cycles, i.e. as **time-separated** rather than coeval. The two accounts therefore differ on whether such juxtapositions are synchronous. Needs a defined sample, an operational test for contemporaneity that does not presuppose either chronology, and its failure condition fixed in advance. Gated like the rest of Tier 3.

**Source:** [`../../../research/GPT-hydrotectonic-flood-model.md`](../../../research/GPT-hydrotectonic-flood-model.md), lines ~285–464. The atmospheric-canopy term is new content, not in the source research. The salinity-refugia section is likewise new content, JD-directed 2026-08-17.
