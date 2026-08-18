#!/usr/bin/env python3
"""
energy_partition_bounds.py — completeness check on the published energy partition.

WHAT THIS IMPLEMENTS
--------------------
The programme's published energy account (POSITION-PAPER.md Section 3.2, ported from
Longmire 2025 v2.5) partitions ~1e25 J of gravitational potential energy as:

    94.2% residual PE | 5.0% friction | 0.5% viscous | 0.25% seismic

That partition covers the GPE release only. Two energy terms in the mechanism as
stated are NOT in it:

    (A) Bulk kinetic energy of the moving continental mass. The energy that must be
        dissipated when motion stops. Raised as an external objection (2026-08-17):
        "you need energy to start the move, and an equal and opposite amount to stop
        it. Reduce friction and you still have to deal with the car crash."

    (B) Impact-trigger energy. POSITION-PAPER Figure 1 / Section 2 make a swarm of
        large impacts the initiating event. The founding research is explicit that
        impacts are a threshold crossing, not a displacement engine
        (research/GPT-hydrotectonic-flood-model.md line 199), which bounds how much
        impact energy the mechanism REQUIRES but not how much it DEPOSITS.

This script computes both terms against the published partition and derives the
ceilings they impose. It is an accounting check on terms already implied by the
stated mechanism, not a new physical model.

DETERMINISTIC: yes. No RNG, no fitting, no iteration. Same inputs -> same outputs.
FITTED PARAMETERS: none. Every input is either sourced (see PARAMETERS) or read
directly from the programme's own belt documents.

RUN
---
    python3 02-theory/rheology/code/energy_partition_bounds.py

No third-party dependencies (stdlib only).

DECLARED BEFORE THE RUN (research-practices.md rule 1)
-------------------------------------------------------
F1  KE-negligibility. For the omission of term (A) from Section 3.2 to be harmless,
    bulk KE at the programme's own stated velocity (9-40 cm/s, kinematics/README.md)
    must be <= 1% of the friction allocation. If KE instead EXCEEDS the friction
    allocation, Section 3.2 is incomplete as published and must be revised.

F2  Velocity ceiling. There exists v_max at which KE alone consumes the entire 1e25 J
    budget, leaving nothing for the 94.2% residual-PE term the partition requires.
    Any kinematic revision proposing v > v_max is refuted by energy conservation on
    the programme's own numbers, independent of any other argument.

F3  Survivable bulk-heating bound. Total energy deposited as ocean heat, from ALL
    sources (tectonic dissipation plus impacts), must keep the ocean below the upper
    thermal limit of marine life. If the model's own dissipation allocation plus a
    plausible impactor swarm fits inside that bound with margin, bulk ocean heating
    is not the binding constraint on the mechanism and the objection class that
    targets it fails generally, not just in the instance.

F3_CONTROL  REFUTED FRAMING, retained per research-practices.md rules 6 and 11.
    The first version of F3 (2026-08-17, superseded same day) asked whether impact
    energy fits inside the model's own 5.75% dissipation allocation, and reported a
    tension: only 0.01-1.38 Chicxulub-equivalents affordable. It died on two counts.
      (1) Category error. The 5.75% allocation is a partition of the GPE RELEASE.
          It is not a global thermal budget, and impacts are a separate energy input
          to the system rather than a competing claim on the tectonic partition.
      (2) Empirically falsified premise. It assumed all deposited impact energy
          becomes terrestrial heat. The one swarm member that can actually be
          observed refutes this: Chicxulub's dominant global thermal signature was
          net COOLING (dust and sulfate aerosol loading; surface air temperature fell
          by as much as ~26 K, sub-freezing for years), followed by modest CO2
          greenhouse warming of 1-5 K. Not bulk ocean heating.
    Kept in the code below, labeled, so the reader can see what was ruled out.

WHAT THIS DOES NOT RESOLVE (research-practices.md rule 12)
-----------------------------------------------------------
- Heat REMOVAL capacity. ROADMAP item 1 proper (radiation, ocean-atmosphere
  circulation, hypercane transport) is untouched here. This script bounds heat
  GENERATION terms only.
- The rheology/viscosity gate. The residual 3-4 orders of magnitude for vertical
  subduction (rheology/README.md) is unaffected.
- The 1e25 J budget and its 94.2/5.0/0.5/0.25 split are IMPORTED from Longmire 2025
  v2.5 and taken as given. This script checks the partition for completeness, not
  for correctness. If the underlying budget is wrong, every ratio here moves with it.
- Vertical/subduction energetics. Lateral translation only.
- The disposition of impact energy between terrestrial heat, ejecta, and radiation
  to space is NOT modeled. F3 assumes the conservative limit (all deposited energy
  becomes terrestrial heat) and is therefore an upper bound on the constraint's
  severity, not a best estimate.

PARAMETERS AND SOURCES (research-practices.md rule 2)
------------------------------------------------------
Confidence labels: HIGH (verified primary) / MEDIUM (secondary with specifics) /
LOW (paraphrase) / UNCERTAIN.

E_TOTAL_J, PARTITION
    POSITION-PAPER.md Section 3.2. Programme-internal; imported from Longmire (2025),
    Global Flood Hydrotectonics v2.5. Confidence: internal, not independently
    verified here.

V_STATED_MIN/MAX
    kinematics/README.md, "this programme's existing continental-velocity figure
    (~9-40 cm/s)". Programme-internal.

V_SOURCE_DISPUTED
    30 m/s. The source document's own worked force balance, which POSITION-PAPER
    Section 3.4 records as inconsistent with its own summary claim and traceable to
    a unit-conversion error (30 m/s reported as "108 m/hr"; correct conversion is
    108,000 m/hr). Retained here as a NEGATIVE CONTROL per research-practices.md
    rule 11 -- kept and labeled, not deleted.

M_CONTINENTAL_KG_LOW/HIGH
    Continental crust mass. Estimates genuinely disagree by roughly a factor of two
    depending on how "continental" is bounded (emergent land vs. including submerged
    margins) and which density model is used: reported values span ~1.34e22 to
    ~2.6e22 kg, against a total-crust (oceanic + continental) figure of ~2.77e22 kg.
    Density estimates in the same sources span ~2600 to ~2835 kg/m3. Reported as a
    RANGE rather than a point value per research-practices.md rule 3.
    Sources: CRUST2.0-based mass/composition estimates (Peters & Sobolev, AGU 2007
    V33A-1161); Christensen, N.I. & Mooney, W.D. (1995), "Seismic velocity structure
    and composition of the continental crust: A global view," JGR Solid Earth 100,
    9761-9788, doi:10.1029/95JB00259 -- the standard velocity-density reference the
    later mass estimates rest on. Confidence: MEDIUM (secondary summaries with
    specific figures; neither primary read in full for this script).

E_CHICXULUB_J_LOW/HIGH
    Chicxulub impactor kinetic energy. Also genuinely disputed: a comprehensive
    multi-model assessment gives 1.3e24 to 5.8e25 J, while commonly cited single
    figures sit near 1e23 and 4.18e23 J. The full span is carried rather than a
    convenient value picked.
    Source: Durand-Manterola, H.J. & Cordero-Tercero, G. (2014), "Assessments of the
    energy, mass and size of the Chicxulub impactor," arXiv:1403.6391.
    Confidence: MEDIUM (abstract-level figures; full text not read for this script).
    NOTE (JD, 2026-08-17): in this programme's model Chicxulub is a MEMBER of the
    initiating swarm, not an external yardstick. That makes it an observational
    anchor rather than a hypothetical: whatever a swarm member does thermally,
    Chicxulub is a worked example of it in the actual record.

DT_OCEAN_LETHAL_LOW/HIGH
    Ocean warming above present that would exceed the upper thermal limit of marine
    life. Measured upper lethal temperatures: 37-41 C for subtidal ectotherms under
    rapid (1 C/hr) heating, falling to ~35.4-40 C under chronic heating; intertidal
    organisms tolerate 41-52 C. Against a present mean sea-surface temperature near
    16 C, that is a headroom of roughly 20-24 K before widespread marine lethality.
    Carried as a range; the LOW end is used for the binding test.
    Source: Nguyen, K.D.T. et al. (2011), "Upper temperature limits of tropical
    marine ectotherms: global warming implications," PLoS ONE 6(12): e29340.
    Confidence: MEDIUM (specific figures from the paper's reported ranges; full text
    not read for this script). This is a bulk-ocean survivability proxy only -- it
    says nothing about atmospheric, radiative, or aerosol effects, which for impacts
    are the dominant terms (see F4).

M_OCEAN_KG, C_WATER
    1.4e21 kg, 4200 J/(kg K). USGS-consistent and the same values used by the
    external critic whose objection prompted this, so the comparison is on their
    own numbers. Confidence: HIGH.
"""

# --- Programme-internal (belt documents) ---------------------------------------
E_TOTAL_J = 1.0e25              # POSITION-PAPER Sec 3.2
FRAC_RESIDUAL_PE = 0.942
FRAC_FRICTION = 0.050
FRAC_VISCOUS = 0.005
FRAC_SEISMIC = 0.0025

V_STATED_MIN = 0.09             # m/s, kinematics/README.md
V_STATED_MAX = 0.40             # m/s
V_SOURCE_DISPUTED = 30.0        # m/s, NEGATIVE CONTROL (see docstring)

# --- Sourced external ----------------------------------------------------------
M_CONTINENTAL_KG_LOW = 1.34e22
M_CONTINENTAL_KG_HIGH = 2.60e22
E_CHICXULUB_J_LOW = 1.3e24
E_CHICXULUB_J_HIGH = 5.8e25
E_CHICXULUB_J_COMMON = 4.18e23  # commonly cited single figure
M_OCEAN_KG = 1.4e21
C_WATER = 4200.0
DT_OCEAN_LETHAL_LOW = 20.0      # K above present, marine survivability proxy
DT_OCEAN_LETHAL_HIGH = 24.0

# --- Declared thresholds (fixed before the run) --------------------------------
F1_KE_FRACTION_OF_FRICTION = 0.01   # KE must be <= 1% of friction allocation

FRAC_DISSIPATED = FRAC_FRICTION + FRAC_VISCOUS + FRAC_SEISMIC   # 0.0575
E_FRICTION_J = E_TOTAL_J * FRAC_FRICTION
E_DISSIPATED_J = E_TOTAL_J * FRAC_DISSIPATED


def kinetic_energy(mass_kg, v_ms):
    return 0.5 * mass_kg * v_ms ** 2


def v_ceiling(mass_kg, energy_budget_j):
    """Velocity at which bulk KE alone consumes energy_budget_j."""
    return (2.0 * energy_budget_j / mass_kg) ** 0.5


def ocean_delta_t(energy_j):
    """Temperature rise if energy_j is deposited in the present ocean."""
    return energy_j / (M_OCEAN_KG * C_WATER)


def fmt(x):
    return f"{x:.3g}"


def main():
    masses = (("low", M_CONTINENTAL_KG_LOW), ("high", M_CONTINENTAL_KG_HIGH))

    print("=" * 78)
    print("ENERGY PARTITION COMPLETENESS CHECK")
    print("Catastrophic Hydrotectonic Flood Model / 02-theory/rheology")
    print("=" * 78)
    print()
    print("Published partition (POSITION-PAPER Sec 3.2), budget E = "
          f"{fmt(E_TOTAL_J)} J:")
    print(f"  residual PE {FRAC_RESIDUAL_PE:6.3%}  = {fmt(E_TOTAL_J*FRAC_RESIDUAL_PE)} J")
    print(f"  friction    {FRAC_FRICTION:6.3%}  = {fmt(E_FRICTION_J)} J")
    print(f"  viscous     {FRAC_VISCOUS:6.3%}  = {fmt(E_TOTAL_J*FRAC_VISCOUS)} J")
    print(f"  seismic     {FRAC_SEISMIC:6.3%}  = {fmt(E_TOTAL_J*FRAC_SEISMIC)} J")
    print(f"  -> total dissipated {FRAC_DISSIPATED:.3%} = {fmt(E_DISSIPATED_J)} J")
    print()

    # ---- TERM (A): bulk kinetic energy ----------------------------------------
    print("-" * 78)
    print("TERM (A)  BULK KINETIC ENERGY -- the 'stopping energy' / car-crash term")
    print("-" * 78)
    print(f"Continental crust mass carried as a range: {fmt(M_CONTINENTAL_KG_LOW)}"
          f" to {fmt(M_CONTINENTAL_KG_HIGH)} kg (sources disagree ~2x; see header)")
    print()
    for label, v in (("stated min", V_STATED_MIN),
                     ("stated max", V_STATED_MAX),
                     ("DISPUTED (negative control)", V_SOURCE_DISPUTED)):
        print(f"  v = {v:>6.2f} m/s  [{label}]")
        for mlabel, m in masses:
            ke = kinetic_energy(m, v)
            print(f"      M {mlabel:>4}: KE = {fmt(ke):>10} J"
                  f" | {ke/E_FRICTION_J:>10.3%} of friction alloc"
                  f" | {ke/E_TOTAL_J:>10.3%} of budget"
                  f" | ocean dT = {fmt(ocean_delta_t(ke))} K")
        print()

    # F1 verdict at the worst case within the stated velocity band
    ke_worst = kinetic_energy(M_CONTINENTAL_KG_HIGH, V_STATED_MAX)
    f1_ratio = ke_worst / E_FRICTION_J
    f1_pass = f1_ratio <= F1_KE_FRACTION_OF_FRICTION
    print(f"F1 [KE-negligibility, declared threshold: KE <= "
          f"{F1_KE_FRACTION_OF_FRICTION:.0%} of friction allocation]")
    print(f"   worst case in stated band: {f1_ratio:.3%} of friction allocation")
    print(f"   VERDICT: {'PASS' if f1_pass else 'FAIL'}"
          f"  -- omission of term (A) from Sec 3.2 is"
          f" {'harmless' if f1_pass else 'NOT harmless'}")
    print()

    # ---- F2: velocity ceilings ------------------------------------------------
    print("-" * 78)
    print("TERM (A) cont.  F2  VELOCITY CEILINGS IMPOSED BY THE BUDGET")
    print("-" * 78)
    print("  v at which bulk KE alone consumes the stated allocation:")
    for blabel, budget in (("friction allocation", E_FRICTION_J),
                           ("total dissipated", E_DISSIPATED_J),
                           ("ENTIRE budget", E_TOTAL_J)):
        lo = v_ceiling(M_CONTINENTAL_KG_HIGH, budget)
        hi = v_ceiling(M_CONTINENTAL_KG_LOW, budget)
        print(f"    {blabel:>20}: v_max = {lo:6.2f} to {hi:6.2f} m/s")
    print()
    vmax_lo = v_ceiling(M_CONTINENTAL_KG_HIGH, E_TOTAL_J)
    vmax_hi = v_ceiling(M_CONTINENTAL_KG_LOW, E_TOTAL_J)
    print(f"F2 [absolute ceiling: v_max = {vmax_lo:.1f} to {vmax_hi:.1f} m/s]")
    print(f"   The disputed source figure {V_SOURCE_DISPUTED} m/s falls"
          f" {'INSIDE' if vmax_lo <= V_SOURCE_DISPUTED <= vmax_hi else 'outside'}"
          f" that band.")
    print("   FORBIDS: any kinematic revision proposing v above this ceiling,"
          " on energy")
    print("   conservation alone. Independent of the unit-conversion argument"
          " already")
    print("   recorded in POSITION-PAPER Sec 3.4.")
    print()

    # ---- TERM (B): impact energy, tested against survivability ----------------
    print("-" * 78)
    print("TERM (B)  F3  SURVIVABLE BULK-HEATING BOUND")
    print("-" * 78)
    print("Chicxulub is a MEMBER of the initiating swarm in this model, not an")
    print("external yardstick -- so it is an observational anchor, not a"
          " hypothetical.")
    print()
    e_lethal_lo = M_OCEAN_KG * C_WATER * DT_OCEAN_LETHAL_LOW
    e_lethal_hi = M_OCEAN_KG * C_WATER * DT_OCEAN_LETHAL_HIGH
    print(f"Ocean energy uptake reaching the marine upper thermal limit"
          f" (+{DT_OCEAN_LETHAL_LOW:.0f} to +{DT_OCEAN_LETHAL_HIGH:.0f} K):")
    print(f"    {fmt(e_lethal_lo)} to {fmt(e_lethal_hi)} J")
    print()
    print("Against that bound:")
    print(f"    entire GPE budget          {fmt(E_TOTAL_J):>9} J"
          f"  -> dT = {fmt(ocean_delta_t(E_TOTAL_J)):>9} K"
          f"  ({E_TOTAL_J/e_lethal_lo:6.2%} of bound)")
    print(f"    model's dissipated share   {fmt(E_DISSIPATED_J):>9} J"
          f"  -> dT = {fmt(ocean_delta_t(E_DISSIPATED_J)):>9} K"
          f"  ({E_DISSIPATED_J/e_lethal_lo:6.2%} of bound)")
    for elabel, e in (("1x Chicxulub (common)", E_CHICXULUB_J_COMMON),
                      ("1x Chicxulub (assess lo)", E_CHICXULUB_J_LOW),
                      ("1x Chicxulub (assess hi)", E_CHICXULUB_J_HIGH)):
        print(f"    {elabel:<26} {fmt(e):>9} J"
              f"  -> dT = {fmt(ocean_delta_t(e)):>9} K"
              f"  ({e/e_lethal_lo:6.2%} of bound)")
    print()
    n_survivable_common = e_lethal_lo / E_CHICXULUB_J_COMMON
    n_survivable_asslo = e_lethal_lo / E_CHICXULUB_J_LOW
    n_survivable_asshi = e_lethal_lo / E_CHICXULUB_J_HIGH
    print("Swarm size affordable within the survivability bound"
          " (bulk heating only):")
    print(f"    at {fmt(E_CHICXULUB_J_COMMON)} J/body: {n_survivable_common:8.1f}"
          " bodies")
    print(f"    at {fmt(E_CHICXULUB_J_LOW)} J/body: {n_survivable_asslo:8.1f}"
          " bodies")
    print(f"    at {fmt(E_CHICXULUB_J_HIGH)} J/body: {n_survivable_asshi:8.1f}"
          " bodies")
    print()
    f3_pass = (E_DISSIPATED_J + E_CHICXULUB_J_LOW) < e_lethal_lo
    print(f"F3 VERDICT: {'PASS' if f3_pass else 'FAIL'} -- bulk ocean heating is"
          " NOT the binding constraint.")
    print(f"   The ocean's thermal mass is {e_lethal_lo/E_TOTAL_J:.1f}x the"
          " ENTIRE gravitational")
    print("   budget. Tectonic dissipation plus a multi-body swarm fits with"
          " large margin")
    print("   except at the highest single-impactor estimate. The objection"
          " class that")
    print("   targets bulk ocean heating fails generally, not just in the"
          " instance.")
    print()

    # ---- F3_CONTROL: refuted framing, retained per rules 6 and 11 --------------
    print("-" * 78)
    print("F3_CONTROL  [REFUTED FRAMING -- RETAINED, NOT DELETED]")
    print("-" * 78)
    print("Superseded 2026-08-17, same day it was written. Asked whether impact")
    print("energy fits inside the model's own 5.75% dissipation allocation:")
    for elabel, e in (("commonly cited", E_CHICXULUB_J_COMMON),
                      ("assessment low", E_CHICXULUB_J_LOW),
                      ("assessment high", E_CHICXULUB_J_HIGH)):
        print(f"    E_chicx = {fmt(e):>9} J [{elabel:>15}]"
              f"  ->  N_max = {E_DISSIPATED_J/e:8.2f}")
    print()
    print("  DIED ON: (1) category error -- the 5.75% figure partitions the GPE")
    print("  RELEASE, it is not a global thermal budget, and impacts are a"
          " separate")
    print("  input rather than a competing claim on it. (2) empirically"
          " falsified")
    print("  premise -- it assumed full thermalization into the ocean, but the"
          " one")
    print("  swarm member in the observational record shows the opposite:")
    print("  Chicxulub's dominant global signature was net COOLING (dust and"
          " sulfate")
    print("  aerosols, surface air temperature down as much as ~26 K,"
          " sub-freezing for")
    print("  years), then CO2 greenhouse warming of only 1-5 K.")
    print()

    # ---- F4: what actually binds ----------------------------------------------
    print("-" * 78)
    print("F4  WHAT ACTUALLY BINDS THE SWARM -- stated open, not computed here")
    print("-" * 78)
    print("Bulk thermal energy does not constrain swarm size (F3). The real"
          " limits on")
    print("how many Chicxulub-class bodies the model can absorb are"
          " radiative and")
    print("climatic, not calorimetric:")
    print("    - aerosol/dust loading and the resulting shading (a COOLING"
          " excursion,")
    print("      the opposite sign to the objection's assumption)")
    print("    - CO2 and sulfate injection from carbonate/evaporite target rock")
    print("    - ejecta re-entry radiation")
    print("    - survivability of the biota the narrative requires to come"
          " through")
    print("  Stating the rival at its strongest (research-practices.md rule 4):"
          " the")
    print("  mainstream account has ONE such impact driving a mass extinction."
          " A swarm")
    print("  is by construction a larger perturbation, and that is the real"
          " cost the")
    print("  model has to price -- in climate response, not in joules.")
    print("  REQUIRES: a modeled aerosol/radiative response. Not attempted"
          " here.")
    print()

    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"  F1 KE-negligibility ......... {'PASS' if f1_pass else 'FAIL'}")
    print(f"  F2 velocity ceiling ......... {vmax_lo:.1f}-{vmax_hi:.1f} m/s"
          " (new constraint on the belt)")
    print(f"  F3 survivable heating ....... {'PASS' if f3_pass else 'FAIL'}"
          f" (bound is {e_lethal_lo/E_TOTAL_J:.1f}x the entire GPE budget)")
    print("  F3_CONTROL .................. refuted framing, retained labeled")
    print("  F4 climatic bound ........... OPEN, requires an aerosol/radiative"
          " model")
    print()
    print("  The external objection does not land on either limb. The stopping"
          " term is")
    print("  ~3 orders below the friction term (F1), and bulk ocean heating has"
          " over an")
    print("  order of magnitude of headroom against the entire budget (F3). The"
          " genuine")
    print("  open cost of the impact swarm is climatic, and it is named rather"
          " than")
    print("  quantified (F4).")
    print()


if __name__ == "__main__":
    main()
