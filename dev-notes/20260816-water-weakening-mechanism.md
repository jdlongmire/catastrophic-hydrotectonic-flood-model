# Water-weakening mechanism — narrowing the rheology gap

**Status: resolved.** Promoted to `02-theory/rheology/README.md`, `03-prediction/discriminators.md`, `03-prediction/appraisal.md`.

## The claim

JD: "the model proposes a lower viscosity in the past due to the water filled porous levels." Pushback on the prior framing ("beyond the softest material ever proposed in mainstream geodynamics") for failing to credit the model's own specified mechanism — water content, not an unexplained number pulled from an unrelated regime.

## Why this needed checking, not just accepting

The prior "10¹⁹ Pa·s floor, 5–6 orders short" figure was benchmarked against **partial-melt** subduction-channel weak zones — a different weakening mechanism (melt fraction, upper mantle wedge), not water content, and not the transition-zone minerals (ringwoodite/wadsleyite) this model's own water-ledger already specifies as the deep reservoir. Comparing the requirement to the wrong mechanism understated the model's actual case. Worth verifying against the literature on the *correct* mechanism before revising anything.

## What was found (WebSearch, 2026-08-16)

- **Fei et al. 2017, *Science Advances*, "A nearly water-saturated mantle transition zone inferred from mineral viscosity"** — measured dislocation mobility (inversely related to viscosity) in **ringwoodite** specifically, the mineral this model already names. Anhydrous ringwoodite → bridgmanite-equivalent mobility: ~2 orders of magnitude. Bridgmanite → fully water-saturated ringwoodite: ~1.5 orders further. **Anhydrous → water-saturated ringwoodite, combined: ~3.5 orders of magnitude reduction.**
- Karato-type mantle-wedge hydration studies: typically 1–2 orders of magnitude, up to ~4 orders at 200–400 km depth under specific stress conditions — olivine-specific, not the transition-zone minerals this model needs, but consistent in direction and rough magnitude.
- A single olivine-aggregate experiment at 300 MPa found a factor of ~140 (≈2.15 orders) from water content alone.

**Confidence: HIGH, upgraded 2026-08-16.** Original pass was search-result summaries only (Science.org returned HTTP 403 on direct fetch). Primary full text obtained via the PMC open-access copy (Science Advances is AAAS open-access; PMC5462500) — the ~2 orders (anhydrous ringwoodite → bridgmanite) and ~1.5 orders (bridgmanite → water-saturated ringwoodite) figures are confirmed as direct quotes from the paper itself, not a secondary paraphrase. Fei et al.'s own stated water-content conclusion: *"ringwoodite in the MTZ should contain 1 to 2 wt % water. The MTZ should thus be nearly water-saturated globally"* — and, accounting for their own stated uncertainty band, *"if the one-half order of magnitude uncertainty in mantle viscosity is considered, the MTZ must contain at least 1 to 2 wt % water to fit the viscosity profile."*

**Caveats the authors themselves state, worth carrying into any formal citation:**
- The water-saturation inference is best constrained *"under the regions that have experienced postglacial rebound"* — global extrapolation is the authors' own inference, not a direct global measurement.
- Water solubility in ringwoodite decreases with increasing temperature, which could limit storage capacity beyond what's modeled.
- The authors acknowledge unresolved discrepancies with independent electrical-conductivity studies of the transition zone: *"the exact reasons for these discrepancies are unclear and remain unknown."*
- Their own experimental temperature-measurement uncertainty (~50 K) alone propagates to roughly a factor-of-two uncertainty in the dislocation-mobility estimate.

## The calculation

Starting from a standard transition-zone viscosity baseline (~10²¹ Pa·s, typical postglacial-rebound-constrained estimate) and stacking the largest *documented, water-specific* effect on the *correct mineral* (~3.5 orders, Fei et al.): ~10¹⁷–10¹⁸ Pa·s. The model requires 10¹³–10¹⁴ Pa·s. **Residual gap: ~3–4 orders of magnitude** — smaller than the 5–6 orders previously stated, because the earlier comparison used the wrong mechanism's floor.

## Disposition

Genuine improvement on two axes at once, not a rhetorical softening:

- **More accurate.** The requirement is now checked against a real, correctly-targeted, mainstream-documented mechanism (water content in ringwoodite) instead of an unrelated partial-melt regime.
- **More honest about what the model has going for it.** Water-weakening is a specific, cited, quantified lever moving in exactly the direction the model needs — not an unexplained ask dressed up as a bare confession.
- **Still genuinely open.** Even the most extreme documented water-saturation effect, on the correct mineral, does not close the gap on its own. The remaining ~3–4 orders is the actual open question — some combination of thermal feedback, strain-rate localization, or an effect not yet quantified in the literature. ROADMAP item 1 (the heat-budget quantification) still stands as the programme's first real computational task.

## Downstream

This also corrects the tone problem flagged earlier in the video narration (`dev-notes` cross-reference: the "beyond the softest material ever proposed" line implicitly treated the requirement as unexplained rather than crediting the model's own mechanism). Narration copy update proposed separately for JD's review per the draft-and-approve SOP.
