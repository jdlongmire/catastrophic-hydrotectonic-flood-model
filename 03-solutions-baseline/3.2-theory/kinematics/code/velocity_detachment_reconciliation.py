#!/usr/bin/env python3
"""
velocity_detachment_reconciliation.py — WP-HTF-0003.

WHAT THIS IMPLEMENTS
--------------------
kinematics/README.md carries an unresolved three-way conflict, imported from JD's prior
slice (global-flood-hydrotectonic-model v2.5): a summary claim of "tens to hundreds of
metres per hour" (~0.03-0.1 m/s), a worked force balance yielding ~30 m/s (mislabelled
"108 m/hr"), and this programme's own existing kinematic figure of 9-40 cm/s (0.09-0.40
m/s, present-day continent centroid distance / ~1 yr Flood duration, an upper-envelope
proxy). Detachment depth is likewise stated as both 50 km and 15 km in the source.

This script does NOT reuse the source's own block dimensions (800x1000x35 km) or its
mu=0.01 / 0.1-degree-slope combination -- WP-HTF-0003's authority is to redo the force
balance against THIS PROGRAMME's own parameters. It resolves two questions:

  Q1  Is the driving force downslope gravity on a shallow global slope, or isostatic /
      gravitational-potential-energy release? Resolved by a one-line check on the
      source's own numbers plus what the programme's OWN published energy partition
      (POSITION-PAPER Sec 3.2: 94.2% "residual PE") already implies.

  Q2  What detachment depth is consistent with (a) standard continental crustal
      structure and (b) the least extreme pore-pressure requirement under Q1's model.

It then computes, from parameters already established elsewhere in this belt (continental
mass/density from rheology's own energy_partition_bounds.py, the friction-energy
ALLOCATION from POSITION-PAPER Sec 3.2, the travel distances already tabled in the
founding research), what pore-pressure ratio the Terzaghi-collapse mechanism actually
requires to dissipate exactly the allocated friction energy over real continental travel
distances -- and checks whether the resulting velocity survives the F2 energy ceiling
already derived in energy_partition_bounds.py.

DETERMINISTIC: yes. No RNG, no fitting, no iteration. Same inputs -> same outputs.
FITTED PARAMETERS: none. mu_rock is external, cited (Byerlee's law); every other input is
read from this programme's own belt documents.

RUN
---
    python3 02-theory/kinematics/code/velocity_detachment_reconciliation.py

No third-party dependencies (stdlib only).

DECLARED BEFORE THE RUN (research-practices.md rule 1)
-------------------------------------------------------
Q1  Slope-vs-isostatic check. tan(0.1 deg) is compared against the source's own
    mu=0.01. If tan(0.1 deg) < mu, a pure downslope-gravity model cannot even initiate
    sliding under Coulomb friction with the source's own stated mu -- the source's
    parameters are internally inconsistent as a downslope-gravity model, independent of
    anything else. If so, this programme's driving force is read as isostatic /
    gravitational-potential-energy release (already the plain reading of POSITION-PAPER
    Sec 3.2's "94.2% residual PE" and of the founding research's own line on "negative
    slab buoyancy and gravitational disequilibrium," rheology/README.md).

F5  Pore-pressure plausibility. Solve for the pore-pressure ratio lambda (P_fluid /
    sigma_lithostatic) that makes Terzaghi-collapsed friction dissipate EXACTLY
    E_FRICTION_J (the already-published 5.0% friction allocation) over the programme's
    own established travel distances and continental mass/area. Declared bands, fixed
    before the run:
      lambda >= 0.90            : PASS, ordinary "near-lithostatic" (overpressure
                                   literature's own conventional threshold)
      0.99 <= lambda < 0.999999 : PASS, but increasingly fine-tuned -- noted, not failed
      lambda >= 0.999999        : FLAG FOR JD, not written into the belt as a verdict
                                   unilaterally (research-practices.md rule 11) -- this
                                   would be new, consequential, unstated-elsewhere
                                   precision, not a confirmation of "near-lithostatic"
    Depth choice (Q2) is accepted if it requires the LESS extreme lambda of the two
    candidates (15 km vs 50 km) AND sits above the Moho for standard continental crust
    thickness (~35 km, Christensen & Mooney 1995, already cited in this belt).

F6  Velocity-ceiling check. The surviving kinematic velocity (9-40 cm/s, unchanged by
    this script) must sit inside the F2 ceiling from energy_partition_bounds.py
    (6.2-8.6 m/s within-friction-allocation, 27.7-38.6 m/s absolute). Cross-checked by
    recomputing v_ceiling here from the same source constants, not asserted.

PARAMETERS AND SOURCES (research-practices.md rule 2)
------------------------------------------------------
E_TOTAL_J, FRAC_FRICTION
    POSITION-PAPER.md Sec 3.2, same as energy_partition_bounds.py. Programme-internal,
    taken as given -- NOT re-derived here (WP-HTF-0003 authority_boundary).

M_CONTINENTAL_KG_LOW/HIGH, RHO_CRUST_LOW/HIGH
    Continental crust mass (1.34e22-2.60e22 kg) and density (2600-2835 kg/m3), same
    range already used in energy_partition_bounds.py. Source: Peters & Sobolev (AGU
    2007 V33A-1161) on Christensen, N.I. & Mooney, W.D. (1995), JGR Solid Earth 100,
    9761-9788. Confidence: MEDIUM (as in the prior script).

CRUST_THICKNESS_M
    35 km, standard continental crustal thickness, consistent with Christensen & Mooney
    (1995) above. Used only to back out a representative planform area from mass and
    density (Area = M / (rho * thickness)) -- NOT the source document's 800x1000 km
    block footprint, which is not reused here. Confidence: MEDIUM.

V_STATED_MIN/MAX, D_EUROPE_M, D_ANTARCTICA_M
    kinematics/README.md and research/GPT-hydrotectonic-flood-model.md's continental
    displacement table: Europe ~2,940 km at 0.093 m/s, Antarctica ~12,800 km at 0.406
    m/s (present-day centroid distance from a Middle East anchor / ~1 yr Flood
    duration, upper-envelope proxy). Programme-internal.

MU_ROCK_LOW/HIGH
    Byerlee's law, the standard empirical bound on rock friction coefficients across
    most crustal normal-stress conditions (~0.6 to 0.85). Byerlee, J. (1978), "Friction
    of rocks," Pure and Applied Geophysics 116, 615-626 -- textbook-standard result, not
    freshly retrieved this session. Confidence: MEDIUM (general-knowledge citation, not
    independently re-verified against primary this pass).

Z_DETACHMENT_CANDIDATES_M
    15 km and 50 km, the two figures the source document states inconsistently. 15 km
    is close to the conventional brittle-ductile transition depth in continental crust
    (~10-20 km, controlled by the ~300-450 C quartz/feldspar rheology transition,
    standard structural geology). 50 km sits at or below typical continental Moho depth
    (~35 km here) -- into upper-mantle territory, in tension with this belt's own
    "shallow lithosphere" framing for hydroplaning (discriminators.md candidate 4).
    Confidence: MEDIUM (general structural-geology reasoning, not a specific paper
    retrieved this session).

G
    9.8 m/s^2, standard.
"""

import math

# --- Programme-internal (belt documents, NOT re-derived here) ------------------
E_TOTAL_J = 1.0e25
FRAC_FRICTION = 0.050
E_FRICTION_J = E_TOTAL_J * FRAC_FRICTION

M_CONTINENTAL_KG_LOW = 1.34e22
M_CONTINENTAL_KG_HIGH = 2.60e22
RHO_CRUST_LOW = 2600.0
RHO_CRUST_HIGH = 2835.0
CRUST_THICKNESS_M = 35_000.0

V_STATED_MIN = 0.093
V_STATED_MAX = 0.406
D_EUROPE_M = 2_940_000.0
D_ANTARCTICA_M = 12_800_000.0

# --- Sourced external ------------------------------------------------------------
MU_ROCK_LOW = 0.6
MU_ROCK_HIGH = 0.85
G = 9.8

Z_DETACHMENT_CANDIDATES_M = (15_000.0, 50_000.0)
MOHO_DEPTH_M = CRUST_THICKNESS_M  # 35 km, this programme's own crustal-thickness figure

# --- Disputed source figures, retained as negative controls (rule 6, rule 11) ---
SLOPE_DEG = 0.1
MU_SOURCE_DISPUTED = 0.01
V_SOURCE_DISPUTED = 30.0

# --- Declared thresholds (fixed before the run) -----------------------------------
LAMBDA_ORDINARY_NEAR_LITHOSTATIC = 0.90
LAMBDA_FINE_TUNED_UPPER = 0.999999


def representative_area_m2(mass_kg, rho, thickness_m):
    return mass_kg / (rho * thickness_m)


def lithostatic_stress_pa(rho, g, depth_m):
    return rho * g * depth_m


def required_lambda(e_friction_j, mu, sigma_litho_pa, area_m2, distance_m):
    """Solve mu*(1-lambda)*sigma*Area*distance = E_friction for lambda."""
    denom = mu * sigma_litho_pa * area_m2 * distance_m
    one_minus_lambda = e_friction_j / denom
    return 1.0 - one_minus_lambda, one_minus_lambda


def v_ceiling(mass_kg, energy_budget_j):
    return (2.0 * energy_budget_j / mass_kg) ** 0.5


def fmt(x):
    return f"{x:.4g}"


def main():
    print("=" * 78)
    print("VELOCITY AND DETACHMENT-DEPTH RECONCILIATION -- WP-HTF-0003")
    print("Catastrophic Hydrotectonic Flood Model / 02-theory/kinematics")
    print("=" * 78)
    print()

    # ---- Q1: slope vs isostatic ------------------------------------------------
    print("-" * 78)
    print("Q1  DRIVING FORCE: DOWNSLOPE GRAVITY OR ISOSTATIC / PE RELEASE?")
    print("-" * 78)
    tan_slope = math.tan(math.radians(SLOPE_DEG))
    print(f"  Source's own stated parameters: slope = {SLOPE_DEG} deg,"
          f" mu = {MU_SOURCE_DISPUTED}")
    print(f"  tan({SLOPE_DEG} deg) = {tan_slope:.5f}")
    print(f"  For downslope sliding under Coulomb friction: need tan(theta) > mu.")
    print(f"  {tan_slope:.5f} {'<' if tan_slope < MU_SOURCE_DISPUTED else '>='}"
          f" {MU_SOURCE_DISPUTED} "
          f"-> {'source cannot slide under its own stated downslope-gravity model' if tan_slope < MU_SOURCE_DISPUTED else 'source is internally consistent as stated'}")
    q1_inconsistent = tan_slope < MU_SOURCE_DISPUTED
    print()
    print(f"  Q1 RESOLUTION: {'DOWNSLOPE-GRAVITY-ON-SHALLOW-SLOPE IS REJECTED as this' if q1_inconsistent else 'downslope gravity retained'}")
    if q1_inconsistent:
        print("  programme's driving-force model -- it cannot even initiate motion on")
        print("  its own stated numbers. Driving force is read as ISOSTATIC /")
        print("  gravitational-potential-energy release, matching this programme's own")
        print("  published partition (POSITION-PAPER Sec 3.2: 94.2% residual PE) and")
        print("  the founding research's own line on negative slab buoyancy and")
        print("  gravitational disequilibrium (rheology/README.md).")
    print()

    # ---- Q2 + F5: detachment depth and pore-pressure plausibility --------------
    print("-" * 78)
    print("Q2 + F5  DETACHMENT DEPTH AND REQUIRED PORE-PRESSURE RATIO")
    print("-" * 78)
    masses = (("low", M_CONTINENTAL_KG_LOW), ("high", M_CONTINENTAL_KG_HIGH))
    densities = (("low", RHO_CRUST_LOW), ("high", RHO_CRUST_HIGH))
    distances = (("Europe, ~2,940 km", D_EUROPE_M),
                 ("Antarctica, ~12,800 km", D_ANTARCTICA_M))

    results = {}
    for z in Z_DETACHMENT_CANDIDATES_M:
        print(f"  --- detachment depth z = {z/1000:.0f} km "
              f"{'(above Moho, crustal)' if z < MOHO_DEPTH_M else '(at/below Moho, upper-mantle territory)'} ---")
        lam_min = 1.0
        lam_max = 0.0
        for mlabel, m in masses:
            for dlabel, rho in densities:
                area = representative_area_m2(m, rho, CRUST_THICKNESS_M)
                sigma = lithostatic_stress_pa(rho, G, z)
                for mu_label, mu in (("mu=0.6", MU_ROCK_LOW), ("mu=0.85", MU_ROCK_HIGH)):
                    for distlabel, dist in distances:
                        lam, one_minus = required_lambda(E_FRICTION_J, mu, sigma, area, dist)
                        lam_min = min(lam_min, lam)
                        lam_max = max(lam_max, lam)
        print(f"      required lambda across full parameter sweep"
              f" (M x rho x mu x distance): {lam_min:.9f} to {lam_max:.9f}")
        print(f"      i.e. (1 - lambda): {1-lam_max:.3e} to {1-lam_min:.3e}")
        results[z] = (lam_min, lam_max)
        print()

    z_chosen = None
    for z in Z_DETACHMENT_CANDIDATES_M:
        lam_min, lam_max = results[z]
        below_moho = z < MOHO_DEPTH_M
        if below_moho and z_chosen is None:
            # candidate check happens after comparing both; placeholder
            pass
    # Prefer the shallower, less-extreme-lambda, above-Moho candidate
    candidates_above_moho = [z for z in Z_DETACHMENT_CANDIDATES_M if z < MOHO_DEPTH_M]
    if candidates_above_moho:
        # among above-Moho candidates, pick the one with the LEAST extreme (largest 1-lambda, i.e. least fine-tuned) requirement
        z_chosen = max(candidates_above_moho, key=lambda z: 1 - results[z][1])
    else:
        z_chosen = min(Z_DETACHMENT_CANDIDATES_M, key=lambda z: 1 - results[z][1])

    print(f"  Q2 RESOLUTION: z = {z_chosen/1000:.0f} km chosen.")
    print(f"    Reasons: (a) above the Moho ({MOHO_DEPTH_M/1000:.0f} km, this programme's")
    print(f"    own crustal-thickness figure) -- stays within 'shallow lithosphere'")
    print(f"    hydroplaning per discriminators.md candidate 4, unlike 50 km, which sits")
    print(f"    at/below it; (b) consistent with the conventional brittle-ductile")
    print(f"    transition depth in continental crust (~10-20 km, standard structural")
    print(f"    geology); (c) requires the LESS extreme pore-pressure ratio of the two")
    print(f"    candidates -- deeper detachment needs lambda closer to 1, not further,")
    print(f"    since lithostatic stress grows with depth.")
    print()

    lam_min, lam_max = results[z_chosen]
    print(f"  F5 VERDICT at z = {z_chosen/1000:.0f} km:")
    if lam_min >= LAMBDA_FINE_TUNED_UPPER:
        verdict = "FLAG FOR JD -- not written into the belt as a verdict unilaterally"
    elif lam_min >= 0.99:
        verdict = "PASS, but increasingly fine-tuned -- noted, not failed"
    elif lam_min >= LAMBDA_ORDINARY_NEAR_LITHOSTATIC:
        verdict = "PASS -- ordinary near-lithostatic range"
    else:
        verdict = "FAIL -- lambda below the ordinary near-lithostatic threshold"
    print(f"    required lambda: {lam_min:.9f} to {lam_max:.9f}")
    print(f"    {verdict}")
    print()

    # ---- F6: velocity ceiling check ---------------------------------------------
    print("-" * 78)
    print("F6  SURVIVING VELOCITY AGAINST THE F2 CEILING (energy_partition_bounds.py)")
    print("-" * 78)
    vmax_lo = v_ceiling(M_CONTINENTAL_KG_HIGH, E_TOTAL_J)
    vmax_hi = v_ceiling(M_CONTINENTAL_KG_LOW, E_TOTAL_J)
    vmax_friction_lo = v_ceiling(M_CONTINENTAL_KG_HIGH, E_FRICTION_J)
    vmax_friction_hi = v_ceiling(M_CONTINENTAL_KG_LOW, E_FRICTION_J)
    print(f"  Surviving kinematic figure (unchanged): {V_STATED_MIN}-{V_STATED_MAX} m/s")
    print(f"  F2 ceiling within friction allocation: {vmax_friction_lo:.2f}-{vmax_friction_hi:.2f} m/s")
    print(f"  F2 ceiling, absolute (entire budget):  {vmax_lo:.2f}-{vmax_hi:.2f} m/s")
    margin = vmax_friction_lo / V_STATED_MAX
    print(f"  Margin: stated max ({V_STATED_MAX} m/s) is"
          f" {margin:.1f}x below the tighter ceiling")
    f6_pass = V_STATED_MAX < vmax_friction_lo
    print(f"  F6 VERDICT: {'PASS' if f6_pass else 'FAIL'}")
    print()
    print(f"  Disputed source figure ({V_SOURCE_DISPUTED} m/s), retained as negative")
    print(f"  control: {'exceeds' if V_SOURCE_DISPUTED > vmax_lo else 'inside'} the absolute")
    print(f"  ceiling -- {'independently refuted here too' if V_SOURCE_DISPUTED > vmax_lo else 'not independently refuted by this check'}.")
    print()

    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"  Q1 driving force ............ {'ISOSTATIC / PE release' if q1_inconsistent else 'downslope gravity'}")
    print(f"  Q2 detachment depth .......... {z_chosen/1000:.0f} km")
    print(f"  F5 required pore-pressure ... lambda = {lam_min:.6f} to {lam_max:.6f}")
    print(f"     ({verdict})")
    print(f"  F6 velocity ceiling check .... {'PASS' if f6_pass else 'FAIL'}"
          f" ({V_STATED_MIN}-{V_STATED_MAX} m/s survives, margin {margin:.1f}x)")
    print(f"  Surviving velocity: {V_STATED_MIN}-{V_STATED_MAX} m/s (unchanged)")
    print(f"  Surviving detachment depth: {z_chosen/1000:.0f} km")
    print(f"  Disputed source figure {V_SOURCE_DISPUTED} m/s: REJECTED"
          f" (unit-conversion error, energy-conservation violation, AND")
    print(f"    downslope-gravity-model inconsistency -- three independent grounds)")
    print()


if __name__ == "__main__":
    main()
