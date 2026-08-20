#!/usr/bin/env python3
"""
WP-HTF-0012 — Gruntfest thermal-stability check on the lateral detachment.

Component harvested from Baumgardner-style CPT per the 2026-08-19 inventory: the
Gruntfest (1963) shear-layer thermal-runaway criterion is a GENERAL stability result
for any shear zone, not mantle-specific and not Baumgardner's. Applied here to THIS
programme's own 15 km lateral detachment (WP-HTF-0003), not to his slab.

WHAT THIS TESTS THAT NOTHING ELSE HAS
  F7/F8 (heat_removal_capacity.py) bound heat flux at the SURFACE. They are silent
  about temperature INSIDE the shear zone, which is where a thermal runaway would
  occur if one occurs. This is that check.

RULE 1 INTEGRITY DISCLOSURE (see package.yaml `disclosure_scoping_already_done`)
  Two scoping passes were run conversationally on 2026-08-19 before this script
  existed, and the second corrected the first. This script does NOT claim clean
  pre-registration. What it does claim: the conditions below were fixed before THIS
  run, the transient limb is solved rather than approximated by min(), and the
  fault-scaling test (F13) was not part of either scoping pass.

FALSIFICATION CONDITIONS, fixed before this run
  F10  Gruntfest stability. Gr = Phi*h^2*E/(k*R*T^2) against the Frank-Kamenetskii
       slab critical value 0.878. FAIL (runaway) if Gr >= Gr_crit anywhere in the
       sourced thickness range under the conservative (rock-controlled) activation
       energy. A runaway is a genuine problem for the lateral mechanism and is to be
       reported plainly.
  F11  Peak temperature rise across the sourced thickness range, transient solution,
       not min(steady, adiabatic). FAIL if dT exceeds the granite solidus margin
       (~900 K above ambient) at any thickness the mechanism could plausibly claim.
  F12  Forbidding band. If F10/F11 pass, state the thickness band the mechanism
       REQUIRES. A stability result that forbids nothing is Tier 2 content (rule 24c).
  F13  Rival-scaling confrontation (rule 4a / rule 24a). Ordinary fault mechanics
       gives core thickness scaling with displacement, T = a*D^n. Extrapolate to this
       programme's continental displacement and compare against F12's required band.
       If the ordinary scaling predicts a thickness inside the F11 hot band or far
       above the F12 requirement, the mechanism owes an explicit claim of exemption.

SOURCED PARAMETERS (rule 2 confidence labels)
  q_surface     64-135 W/m^2      HIGH    F7, heat_removal_capacity.py, this repo
  kappa         1e-6 m^2/s        HIGH    standard rock thermal diffusivity
  k_therm       2.5 W/m/K         HIGH    standard crustal rock conductivity
  rho_c         2.7e6 J/m^3/K     HIGH    standard, rho ~2700 * c ~1000
  T_ambient     600-700 K         MEDIUM  15 km depth at ~25 K/km + surface; the
                                          detachment depth is WP-HTF-0003's result
  E_rock        200 kJ/mol        MEDIUM  representative crustal thermally-activated
                                          creep; carried as the CONSERVATIVE case
                                          because higher E* is MORE runaway-prone
  E_water       20 kJ/mol         MEDIUM  liquid-water viscosity activation energy;
                                          the mechanism's own claim is a fluid film,
                                          so this is the mechanism-consistent case
  h range       1e-3 to 1e2 m     MEDIUM  fault-zone field literature. Principal slip
                                          zones <1-5 mm; incremental slip in trenches
                                          "tens of cm or less"; fault cores mm to
                                          several m. PRIMARY NOT RETRIEVED - Torabi
                                          & Berg (2011) and Torabi et al. (2019,
                                          Geofluids 2918673) both returned HTTP 402
                                          on every mirror tried this session, same
                                          blocker class as Lee 2021 in WP-HTF-0005.
  T = a*D^n     n ~ 0.5-1.0       LOW     fault core thickness vs displacement power
                                          law; PSZ reported as ~1e-2 * D. Exponent
                                          NOT primary-sourced. LOW confidence is the
                                          honest label and F13 is read accordingly.

Deterministic, stdlib only, no fitted parameters. Re-run:
  python3 03-solutions-baseline/3.2-theory/kinematics/code/gruntfest_detachment_stability.py
"""

import math

# ---------------------------------------------------------------- constants
R_GAS   = 8.314          # J/mol/K
K_THERM = 2.5            # W/m/K
KAPPA   = 1.0e-6         # m^2/s
RHO_C   = 2.7e6          # J/m^3/K
YEAR    = 3.156e7        # s
GR_CRIT = 0.878          # Frank-Kamenetskii critical value, plane-parallel slab

Q_LO, Q_HI = 64.0, 135.0         # W/m^2, F7
T_AMB_LO, T_AMB_HI = 600.0, 700.0
E_ROCK  = 200e3          # J/mol, conservative
E_WATER = 20e3           # J/mol, mechanism-consistent
H_RANGE = [1e-3, 1e-2, 1e-1, 1.0, 8.0, 1e1, 1e2]   # m, half-thickness

# displacement this programme claims, for F13
D_CONT_LO, D_CONT_HI = 1.0e6, 3.0e6      # m, continental translation


def gruntfest(q, h, E, T):
    """Gr = Phi * h^2 * E / (k * R * T^2), Phi = q/h volumetric dissipation."""
    phi = q / h
    return phi * h * h * E / (K_THERM * R_GAS * T * T)


def dT_transient(q, h, t):
    """
    Temperature rise at the centre of a slab of half-width h, uniform volumetric
    heating Phi = q/h, zero-flux centre, fixed-T boundary, from t=0.
    Series solution; steady state is Phi*h^2/(2k), approached on t ~ h^2/kappa.
    """
    phi = q / h
    ss = phi * h * h / (2.0 * K_THERM)
    # eigenfunction series for the approach to steady state
    acc = 0.0
    for n in range(1, 200):
        lam = (2 * n - 1) * math.pi / (2 * h)
        acc += ((-1) ** (n + 1)) / ((2 * n - 1) ** 3) * math.exp(-KAPPA * lam * lam * t)
    return ss - (phi * h * h / K_THERM) * (16.0 / (math.pi ** 3)) * acc


def main():
    print("=" * 74)
    print("  WP-HTF-0012 — Gruntfest stability, lateral detachment")
    print("=" * 74)

    # ------------------------------------------------------------- F10
    print("\nF10 — Gruntfest number vs Frank-Kamenetskii critical value 0.878")
    print(f"{'h (m)':>8} {'Gr (rock,E=200k)':>20} {'Gr (water,E=20k)':>20} {'verdict':>12}")
    f10_fail = False
    for h in H_RANGE:
        gr_rock  = gruntfest(Q_HI, h, E_ROCK,  T_AMB_LO)   # worst case: max q, min T
        gr_water = gruntfest(Q_HI, h, E_WATER, T_AMB_LO)
        bad = gr_rock >= GR_CRIT
        f10_fail = f10_fail or bad
        print(f"{h:>8.3g} {gr_rock:>20.3e} {gr_water:>20.3e} {'RUNAWAY' if bad else 'stable':>12}")
    print(f"  F10: {'FAIL — runaway reached' if f10_fail else 'PASS — no runaway at any sourced thickness'}")

    # ------------------------------------------------------------- F11
    print("\nF11 — peak temperature rise, transient solution over the Flood year")
    print(f"{'h (m)':>8} {'dT @ q=64':>14} {'dT @ q=135':>14} {'t_diff':>14}")
    peak = 0.0
    for h in H_RANGE:
        d_lo = dT_transient(Q_LO, h, YEAR)
        d_hi = dT_transient(Q_HI, h, YEAR)
        peak = max(peak, d_hi)
        td = h * h / KAPPA
        td_s = f"{td/YEAR:.2g} yr" if td > YEAR else f"{td/86400:.2g} d"
        print(f"{h:>8.3g} {d_lo:>14.1f} {d_hi:>14.1f} {td_s:>14}")
    print(f"  peak dT over the range: {peak:.0f} K   (granite solidus margin ~900 K)")
    print(f"  F11: {'FAIL' if peak > 900 else 'PASS'}")

    # ------------------------------------------------------------- F12
    print("\nF12 — the forbidding band")
    h_fine = [10 ** (x / 20.0) for x in range(-60, 45)]
    worst_h = max(h_fine, key=lambda h: dT_transient(Q_HI, h, YEAR))
    print(f"  worst-case thickness  : {worst_h:.2f} m  (~sqrt(2*kappa*t) = {(2*KAPPA*YEAR)**0.5:.1f} m)")
    print(f"  worst-case dT         : {dT_transient(Q_HI, worst_h, YEAR):.0f} K")
    for limit in (100.0, 300.0):
        below = [h for h in h_fine if h < worst_h and dT_transient(Q_HI, h, YEAR) <= limit]
        above = [h for h in h_fine if h > worst_h and dT_transient(Q_HI, h, YEAR) <= limit]
        lo = max(below) if below else None
        hi = min(above) if above else None
        print(f"  to keep dT <= {limit:5.0f} K : h <= {lo:.3g} m  OR  h >= {hi:.3g} m")

    # ------------------------------------------------------------- F13
    print("\nF13 — confrontation with ordinary fault displacement-thickness scaling")
    print("  (rule 4a: the rival's own scaling, applied to this programme's displacement)")
    for n, label in ((1.0, "PSZ ~ 1e-2 * D"), (0.5, "T = a*D^0.5, a=1e-2")):
        for D in (D_CONT_LO, D_CONT_HI):
            t_pred = 1e-2 * D if n == 1.0 else 1e-2 * D ** 0.5
            print(f"  {label:24s} D={D:.1e} m -> T = {t_pred:.3g} m")
    print("  Earth's crustal thickness is ~3.5e4 m (continental).")
    print("  A linear PSZ~1e-2*D extrapolation exceeds the crust itself, so the")
    print("  ordinary scaling MUST break down at this displacement — it is calibrated")
    print("  on faults many orders of magnitude smaller. Reported as a confrontation")
    print("  the mechanism owes an answer to, NOT as a refutation. Exponent is LOW")
    print("  confidence (primary paywalled), so no verdict is drawn from its value.")

    print("\n" + "=" * 74)


if __name__ == "__main__":
    main()
