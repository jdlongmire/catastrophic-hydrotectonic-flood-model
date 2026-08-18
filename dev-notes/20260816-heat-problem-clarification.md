# Heat problem clarification

**Status: open.** Pending JD's answer on which problem he meant. Not yet promoted anywhere.

## The claim

JD: "the heat problem that has traditionally plagued the other models is not such an issue here."

## Why this needed unpacking before agreeing or editing anything

"The heat problem" names two genuinely different physical problems in this literature, and they land completely differently on this programme. Affirming the claim without distinguishing them would have risked either quietly endorsing something unearned, or missing a real point JD had in mind.

### 1. The condensation / latent-heat problem — sidestepped here, genuinely

The traditional critique of vapor-canopy models: condensing enough atmospheric water vapor to produce a global deluge releases enormous latent heat. This model was never exposed to that critique, because the water is sourced mostly from crustal/mantle reservoirs, not atmospheric condensation — and the canopy itself was already found (see [`../03-solutions-baseline/3.2-theory/water-ledger/README.md`](../03-solutions-baseline/3.2-theory/water-ledger/README.md)) to be a negligible contributor (~0.1–0.4% of the budget at the only habitable canopy depth), not the water source. If this is what JD meant, the claim is correct and worth stating formally in the water-ledger writeup.

### 2. The viscous-dissipation / rheological heat problem — NOT shown to be avoided

The problem traditionally leveled at Baumgardner-style catastrophic plate tectonics: sustaining the stress and strain rate needed for rapid subduction releases heat as a direct mechanical consequence, not a separate add-on. This is the problem `02-theory/rheology/README.md` and `03-prediction/discriminators.md` currently name as the programme's gating open problem.

Pushback offered: localizing the deformation to crustal/upper-mantle shear zones rather than requiring Baumgardner-style whole-mantle overturn does not obviously defuse this. Viscous dissipation per unit volume is roughly stress times strain rate. Using the numbers already in the research (τ ~ 10⁸ Pa, v/h ~ 3×10⁻⁶ s⁻¹), that works out to roughly hundreds of watts per cubic meter — around eight orders of magnitude above normal radiogenic heat production. Concentrating the same total displacement work into a smaller volume doesn't reduce that flux; it may raise the local peak. On this reading, the mechanical requirement (10¹³–10¹⁴ Pa·s transient viscosity) *is* the heat problem, restated, not a separate issue that's been solved by localization.

**Nothing here is a finished calculation.** This is order-of-magnitude reasoning from numbers already in the belt, not the actual heat-budget quantification ROADMAP item 1 calls for. It's a reason to hold the appraisal verdict where it is, not a proof that JD's framing is wrong.

## Open question

Which problem did JD mean — (1), (2), or a specific mechanism not covered by either framing above (e.g., something about how localized water-driven weakening changes the heat-removal pathway rather than the heat-generation rate)? Answer determines whether this promotes to the water-ledger README (if 1) or requires the actual ROADMAP item 1 calculation before the rheology gate's status can move (if 2).
