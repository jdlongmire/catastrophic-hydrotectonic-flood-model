# Kinematics

Belt content: continental and slab displacement rates required to reconstruct present geometry from a Pangaea-type $S_0$ — the pre-Flood supercontinent, named **"Araratia"** in the visualization set and adopted 2026-08-16 as this programme's standing term for it — within the Flood year, and post-Flood relaxation.

**From the initial research:** order-of-magnitude continental velocities ~10⁻¹ m/s and slab-descent velocities ~10⁻² m/s, derived using present-day centroid distances from a Middle East anchor as an upper-envelope proxy — explicitly not a reconstructed plate-motion field. Post-Flood relaxation was modeled as $v(t) = v_0 e^{-t/\tau} + v_\infty$ rather than constant velocity, since >99.99% of large-scale displacement must occur in the Flood year for present plate velocities to emerge naturally from the 6,000-year relaxation window.

## Mechanism reframe, 2026-08-16 — hydroplaning as the lateral-translation driver

JD's prior slice ([`jdlongmire/global-flood-hydrotectonic-model`](https://github.com/jdlongmire/global-flood-hydrotectonic-model), v2.5) proposes continental hydroplaning — Terzaghi effective-stress collapse under near-lithostatic pore pressure — as the mechanism for bulk lateral translation, distinct from the vertical subduction question ([`../rheology/README.md`](../rheology/README.md)). Ported here as the layered model's lateral half; see `hard-core.md`'s belt table.

**Velocity reconciliation — checked, not resolved.** The source repo's own figures don't agree with each other, so nothing is silently carried forward:

- Stated summary claim: "tens to hundreds of meters per hour" (~0.03–0.1 m/s).
- The source's own worked force-balance calculation (800×1000×35 km block, 0.1° slope, friction collapsed to μ=0.01): a ≈ 0.03 m/s² over ~15 min gives **v ≈ 30 m/s** — which that document itself mislabels "108 m/hr" (30 m/s × 3600 s/hr = 108,000 m/hr, not 108). Correctly converted, the calculation's own output is ~1,000× faster than the summary claim it's meant to support.
- This program's existing continental-velocity figure (~9–40 cm/s, above) sits between the two: 3–15× faster than the "tens-hundreds m/hr" summary, but 75–300× slower than the calculation's literal (mislabeled) output.
- Detachment depth is also inconsistent in the source: the README states ~50 km, the driving-force calculation uses 15 km.

**Open, gating any further kinematic claim:** redo the force-balance calculation against this programme's own block parameters and the Flood-year displacement budget already established here, pick one detachment depth, and check the result against the existing 9–40 cm/s figure rather than importing either source number as-is.

**Open (ROADMAP item 2):** replace the anchor-distance proxy with an actual Pangaea-fit paleomagnetic reconstruction (Euler poles). The current "no primary kinematic impossibility" conclusion is only as strong as the crude proxy behind it.

**Visualization vs. research — flagged discrepancy.** [`continental-shift.png`](../../04-visualization-assets/images/continental-shift.png) states catastrophic-phase plate velocities as ~0.01–0.1 m/s; the research above derives ~0.093–0.406 m/s. The image's ceiling sits at or below the research's floor. The research figure is authoritative until reconciled — see [`../../04-visualization-assets/images/README.md`](../../04-visualization-assets/images/README.md).

**Source:** [`../../research/GPT-hydrotectonic-flood-model.md`](../../research/GPT-hydrotectonic-flood-model.md), lines ~27–127.
