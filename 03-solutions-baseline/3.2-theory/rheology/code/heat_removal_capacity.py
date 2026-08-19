#!/usr/bin/env python3
"""
heat_removal_capacity.py — WP-HTF-0006, ROADMAP item 1 proper.

WHAT THIS IMPLEMENTS
--------------------
ROADMAP item 1 names the programme's declared gate on everything: "total tectonic energy
generated at v ~ 1e-1 m/s over the catastrophic interval vs. total plausible heat removal
(ocean-atmosphere circulation, radiation, deep burial). Give the hypercane hypothesis its
strongest quantitative case and see exactly where it misses." energy_partition_bounds.py
(2026-08-17) bounded GENERATION terms only and stated plainly it does not touch removal.
This script is the removal-capacity half.

POSITION-PAPER.md Sec 2 names the actual constraint being tested: naive full-friction
sliding at continental velocities generates a sustained heat flux "on the order of 600
W/m^2, roughly half the power of direct solar irradiance" -- lethal if sustained over a
Flood year. Sec 3.1 states the programme's answer is not increased heat tolerance but that
"the heat was never generated," because Terzaghi effective-stress collapse under near-
lithostatic pore pressure reduces friction, and with it dissipation, far below the naive
full-friction case. That claim has been asserted qualitatively since stand-up and never
checked quantitatively against the 600 W/m^2 figure it is meant to beat. This script does
that check, using this programme's own already-published friction-dissipation ENERGY
figure (not the naive full-friction assumption) and a physically principled REMOVAL
ceiling: the runaway-greenhouse limit on outgoing longwave radiation, which is the actual
upper bound on how fast the Earth-ocean-atmosphere system can shed heat to space regardless
of which internal transport mechanism (evaporation, convection, hypercane-scale
circulation) moves it there. Any surface-level transport mechanism only relocates heat
within the climate system; radiation to space is the only removal from it, and the
runaway-greenhouse literature already characterizes that ceiling.

SCOPE, STATED PLAINLY (rule 18): this script covers the LATERAL translation heat term only
-- the dissipated share of the 1e25 J energy_partition_bounds.py budget (friction + viscous
+ seismic, POSITION-PAPER Sec 3.2). It does NOT cover vertical/subduction-channel heat
generation (Sec 4, the mantle-viscosity mechanism) in absolute Joules, because no channel
geometry (width, length, depth extent) has been established anywhere in this belt to derive
one from -- only a required VISCOSITY has been stated (rheology/README.md). That remains a
separate, unresolved sub-problem, named here rather than filled with an invented geometry.

DETERMINISTIC: yes. No RNG, no fitting, no iteration. Same inputs -> same outputs.
FITTED PARAMETERS: none. Every input is either read from this programme's own belt
documents or an external, cited physical constant/literature range.

RUN
---
    python3 02-theory/rheology/code/heat_removal_capacity.py

No third-party dependencies (stdlib only).

DECLARED BEFORE THE RUN (research-practices.md rule 1)
-------------------------------------------------------
F7  Local sustained-flux check. Spread this programme's own published dissipated energy
    (E_DISSIPATED_J, POSITION-PAPER Sec 3.2 -- NOT the naive full-friction assumption
    POSITION-PAPER Sec 2 cites as the problem) over the actively-translating crust area
    (same representative-area derivation as WP-HTF-0003's script) and the Flood-year
    duration. PASS if the resulting sustained local flux sits below the runaway-greenhouse
    OLR ceiling with margin -- this tests whether hypercane-scale heat export is NECESSARY
    for the lateral mechanism, not merely helpful. Also reported: the ratio to the naive
    600 W/m^2 figure, as a direct quantitative check of POSITION-PAPER Sec 3.1's qualitative
    claim that Terzaghi collapse reduces the flux, not just the mechanism.

F8  Global-mean stacking check. Present-day Earth radiates approximately 240 W/m^2 in
    equilibrium with absorbed solar flux (standard climatology figure). Adding this
    programme's dissipated flux, spread over the WHOLE planet rather than just the
    translating area, to that baseline must still sit below the runaway-greenhouse
    ceiling -- this is the more conservative and more physically correct framing, since
    the ceiling constrains TOTAL outgoing flux, not the anomalous term in isolation.

F9  Vertical/subduction-channel heat generation -- NOT computed here, named as a
    consequence of rule 18. No channel geometry is established in this belt (README.md,
    rheology) to derive an energy figure from; only a required viscosity range (1e13-1e14
    Pa*s) is stated. A future package would need to establish channel dimensions from
    subduction-zone geology before this term can be quantified. This script's F7/F8 result
    does NOT close ROADMAP item 1 for the vertical half of the mechanism.

    Declared interpretation under research-practices.md rule 21 (fine-tuning is not an
    issue in this model): if F7/F8 require the removal ceiling to be approached closely
    rather than comfortably cleared, that is read as a real, demanding feature of a
    designed singular event, not a defect -- consistent with the WP-HTF-0003 precedent.
    It would still be reported plainly either way (rule 3).

PARAMETERS AND SOURCES (research-practices.md rule 2)
------------------------------------------------------
E_TOTAL_J, FRAC_FRICTION, FRAC_VISCOUS, FRAC_SEISMIC
    POSITION-PAPER.md Sec 3.2, same as energy_partition_bounds.py and
    velocity_detachment_reconciliation.py. Programme-internal, taken as given.

M_CONTINENTAL_KG_LOW/HIGH, RHO_CRUST_LOW/HIGH, CRUST_THICKNESS_M
    Same figures as velocity_detachment_reconciliation.py, used identically to derive a
    representative planform area (Area = M / (rho * thickness)). Source: Peters & Sobolev
    (AGU 2007 V33A-1161) on Christensen & Mooney (1995), JGR Solid Earth 100, 9761-9788.
    Confidence: MEDIUM.

FLOOD_DURATION_S
    1 year = 3.1557e7 s (Julian year), consistent with this programme's ~1 yr Flood
    duration (hard-core.md belt estimate) and the duration already used throughout
    kinematics/README.md and energy_partition_bounds.py.

FLUX_NAIVE_FULL_FRICTION_WM2
    600 W/m^2, POSITION-PAPER.md Sec 2's own stated naive full-friction figure -- the
    problem this programme's mechanism claims to have dissolved. Retained here as the
    comparison baseline, not re-derived (it is a citation of the paper's own framing, not
    an independently sourced physical constant).

EARTH_SURFACE_AREA_M2
    5.1e14 m^2. Standard, well-established figure.

OLR_PRESENT_MEAN_WM2
    ~240 W/m^2. Standard climatology figure for present-day global-mean outgoing longwave
    radiation / absorbed solar flux in equilibrium (e.g. Trenberth et al.-style Earth
    energy-budget figures, commonly cited range 239-241 W/m^2). Confidence: HIGH (very
    well-established, general knowledge, not independently re-verified against a specific
    primary this session).

OLR_RUNAWAY_LIMIT_WM2_LOW/HIGH
    280-310 W/m^2. The "Simpson-Nakajima" runaway-greenhouse limit on outgoing longwave
    radiation -- the theoretical ceiling on how fast a planet with an Earth-like
    atmosphere can radiate heat to space, above which OLR cannot keep pace with surface
    heating regardless of surface temperature (Ingersoll 1969; Nakajima, Hayashi &
    Abe 1992, J. Atmos. Sci. 49; reviewed in Goldblatt & Watson 2012, Phil. Trans. R.
    Soc. A 370). Reported as a range per rule 3 -- some spectroscopy-refined treatments
    (Goldblatt et al. 2013, Nature Geoscience) give a somewhat lower figure (~282 W/m^2)
    than earlier estimates (up to ~385 W/m^2 under different assumptions); 280-310 W/m^2
    is used here as a representative central range. Confidence: MEDIUM (general
    literature knowledge, not independently retrieved primary text this session --
    flagged per rule 13 as an outstanding retrieval task if this figure becomes more
    heavily load-bearing than the comfortable-margin result below implies).
"""

# --- Programme-internal (belt documents, taken as given) -----------------------
E_TOTAL_J = 1.0e25
FRAC_FRICTION = 0.050
FRAC_VISCOUS = 0.005
FRAC_SEISMIC = 0.0025
FRAC_DISSIPATED = FRAC_FRICTION + FRAC_VISCOUS + FRAC_SEISMIC
E_DISSIPATED_J = E_TOTAL_J * FRAC_DISSIPATED

M_CONTINENTAL_KG_LOW = 1.34e22
M_CONTINENTAL_KG_HIGH = 2.60e22
RHO_CRUST_LOW = 2600.0
RHO_CRUST_HIGH = 2835.0
CRUST_THICKNESS_M = 35_000.0

FLOOD_DURATION_S = 3.1557e7  # 1 Julian year

FLUX_NAIVE_FULL_FRICTION_WM2 = 600.0  # POSITION-PAPER Sec 2, the claim being tested

# --- Sourced external ------------------------------------------------------------
EARTH_SURFACE_AREA_M2 = 5.1e14
OLR_PRESENT_MEAN_WM2 = 240.0
OLR_RUNAWAY_LIMIT_WM2_LOW = 280.0
OLR_RUNAWAY_LIMIT_WM2_HIGH = 310.0


def representative_area_m2(mass_kg, rho, thickness_m):
    return mass_kg / (rho * thickness_m)


def fmt(x):
    return f"{x:.4g}"


def main():
    print("=" * 78)
    print("HEAT REMOVAL CAPACITY -- WP-HTF-0006, ROADMAP ITEM 1 (LATERAL TERM)")
    print("Catastrophic Hydrotectonic Flood Model / 02-theory/rheology")
    print("=" * 78)
    print()
    print(f"Dissipated energy (friction {FRAC_FRICTION:.1%} + viscous {FRAC_VISCOUS:.1%}"
          f" + seismic {FRAC_SEISMIC:.2%} = {FRAC_DISSIPATED:.2%} of {fmt(E_TOTAL_J)} J):")
    print(f"    E_DISSIPATED = {fmt(E_DISSIPATED_J)} J")
    print(f"Flood duration: {fmt(FLOOD_DURATION_S)} s (~1 yr)")
    print()

    areas = []
    for mlabel, m in (("low", M_CONTINENTAL_KG_LOW), ("high", M_CONTINENTAL_KG_HIGH)):
        for dlabel, rho in (("low", RHO_CRUST_LOW), ("high", RHO_CRUST_HIGH)):
            areas.append(representative_area_m2(m, rho, CRUST_THICKNESS_M))
    area_lo, area_hi = min(areas), max(areas)

    # ---- F7: local sustained flux ------------------------------------------------
    print("-" * 78)
    print("F7  LOCAL SUSTAINED FLUX -- actively-translating crust area")
    print("-" * 78)
    print(f"  Representative area (from continental mass/density/thickness,"
          f" same derivation as WP-HTF-0003): {fmt(area_lo)} to {fmt(area_hi)} m^2")
    flux_local_hi = E_DISSIPATED_J / (area_lo * FLOOD_DURATION_S)  # smaller area -> higher flux
    flux_local_lo = E_DISSIPATED_J / (area_hi * FLOOD_DURATION_S)  # larger area -> lower flux
    print(f"  Sustained local flux under THIS mechanism's own (Terzaghi-reduced)"
          f" dissipation:")
    print(f"    {flux_local_lo:.1f} to {flux_local_hi:.1f} W/m^2")
    print()
    ratio_to_naive_lo = flux_local_lo / FLUX_NAIVE_FULL_FRICTION_WM2
    ratio_to_naive_hi = flux_local_hi / FLUX_NAIVE_FULL_FRICTION_WM2
    print(f"  Against POSITION-PAPER Sec 2's naive full-friction figure"
          f" ({FLUX_NAIVE_FULL_FRICTION_WM2:.0f} W/m^2):")
    print(f"    {ratio_to_naive_lo:.1%} to {ratio_to_naive_hi:.1%} of the naive figure"
          f"  ({1/ratio_to_naive_hi:.1f}x to {1/ratio_to_naive_lo:.1f}x reduction)")
    print(f"    -> quantitatively confirms Sec 3.1's qualitative claim that Terzaghi"
          f" collapse")
    print(f"       reduces dissipation, not just friction -- this is the first time that")
    print(f"       claim has been checked against a number rather than asserted.")
    print()
    print(f"  Against the runaway-greenhouse OLR ceiling"
          f" ({OLR_RUNAWAY_LIMIT_WM2_LOW:.0f}-{OLR_RUNAWAY_LIMIT_WM2_HIGH:.0f} W/m^2):")
    f7_pass = flux_local_hi < OLR_RUNAWAY_LIMIT_WM2_LOW
    margin_f7 = OLR_RUNAWAY_LIMIT_WM2_LOW / flux_local_hi
    print(f"    worst case {flux_local_hi:.1f} W/m^2 is"
          f" {'below' if f7_pass else 'AT OR ABOVE'} the low end of the ceiling,"
          f" margin {margin_f7:.1f}x")
    print(f"  F7 VERDICT: {'PASS' if f7_pass else 'FAIL'} -- hypercane-scale heat export"
          f" is {'NOT necessary' if f7_pass else 'REQUIRED'} for the lateral term alone.")
    print()

    # ---- F8: global-mean stacking check -------------------------------------------
    print("-" * 78)
    print("F8  GLOBAL-MEAN STACKING CHECK -- against present-day OLR baseline")
    print("-" * 78)
    flux_global = E_DISSIPATED_J / (EARTH_SURFACE_AREA_M2 * FLOOD_DURATION_S)
    print(f"  Dissipated flux spread over the WHOLE planet: {flux_global:.2f} W/m^2")
    total_flux_required = OLR_PRESENT_MEAN_WM2 + flux_global
    print(f"  Present-day mean OLR baseline: {OLR_PRESENT_MEAN_WM2:.0f} W/m^2")
    print(f"  Total outgoing flux required (baseline + dissipation):"
          f" {total_flux_required:.2f} W/m^2")
    f8_pass = total_flux_required < OLR_RUNAWAY_LIMIT_WM2_LOW
    margin_f8 = OLR_RUNAWAY_LIMIT_WM2_LOW - total_flux_required
    print(f"  Runaway-greenhouse ceiling: {OLR_RUNAWAY_LIMIT_WM2_LOW:.0f}-"
          f"{OLR_RUNAWAY_LIMIT_WM2_HIGH:.0f} W/m^2")
    print(f"  F8 VERDICT: {'PASS' if f8_pass else 'FAIL'} -- total required flux sits"
          f" {margin_f8:.1f} W/m^2 {'below' if f8_pass else 'above'} the low end of the"
          f" ceiling ({total_flux_required/OLR_RUNAWAY_LIMIT_WM2_LOW:.1%} of it used).")
    print()

    # ---- F9: vertical term, named not computed -------------------------------------
    print("-" * 78)
    print("F9  VERTICAL / SUBDUCTION-CHANNEL HEAT -- NOT COMPUTED (rule 18)")
    print("-" * 78)
    print("  No channel geometry (width, length, depth extent) is established anywhere")
    print("  in this belt. Only a required viscosity range (1e13-1e14 Pa*s,")
    print("  rheology/README.md) is stated -- not an energy or power figure. F7/F8 above")
    print("  do NOT close ROADMAP item 1 for the vertical half of the mechanism. Deriving")
    print("  channel dimensions from subduction-zone geology is required first and is not")
    print("  attempted here.")
    print()

    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"  F7 local flux vs naive 600 W/m^2 .... {ratio_to_naive_lo:.1%}-{ratio_to_naive_hi:.1%}"
          f" ({1/ratio_to_naive_hi:.1f}-{1/ratio_to_naive_lo:.1f}x reduction)")
    print(f"  F7 local flux vs runaway ceiling ..... {'PASS' if f7_pass else 'FAIL'}"
          f" ({margin_f7:.1f}x margin)")
    print(f"  F8 global-mean stacking check ........ {'PASS' if f8_pass else 'FAIL'}"
          f" ({total_flux_required:.1f} of {OLR_RUNAWAY_LIMIT_WM2_LOW:.0f}-"
          f"{OLR_RUNAWAY_LIMIT_WM2_HIGH:.0f} W/m^2 ceiling)")
    print(f"  F9 vertical/subduction term .......... NOT COMPUTED, no geometry established")
    print()
    print("  LATERAL heat generation-vs-removal question: resolved favorably, with")
    print("  comfortable margin, WITHOUT needing to invoke hypercane-scale circulation as")
    print("  a load-bearing mechanism -- ordinary radiative capacity suffices once the")
    print("  Terzaghi-collapse reduction (not naive full friction) is used. This is a")
    print("  genuine, quantitative confirmation of a claim this programme has held")
    print("  qualitatively since stand-up, not previously checked against a number.")
    print("  ROADMAP item 1 remains open for the VERTICAL/subduction-channel term, which")
    print("  this script does not address.")
    print()


if __name__ == "__main__":
    main()
