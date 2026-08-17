# Start/stop energy objection — the "car crash" term

**Status: resolved for F1/F2/F3, open for F4 and one belt commitment.** Promoted to `02-theory/rheology/README.md` (§Energy-partition completeness check), `03-prediction/appraisal.md`. Code: `02-theory/rheology/code/energy_partition_bounds.py`. F3's first version was refuted the same day it was written and is retained in the code as `F3_CONTROL` — see §The correction below.

## The objection

External, 2026-08-17, following the heat-budget exchange:

> It seems to me that you have three issues when moving anything around on a surface: (i) The energy required to get things moving (ii) The energy lost due to friction during the move (iii) The energy needed to stop the move.
>
> It also seems to me that you think that the heat problem is predominantly a function of (ii), and think that if you can find a way to remove the friction, then the issue is solved. This is simply not correct. You need energy to start the move, and an equal and opposite amount of energy to stop it. Friction is the loss in the middle of this. Reduce friction and you still have to deal with the car crash.

## Why this needed a calculation rather than an answer

The objection is well-formed and it identified something real: the published partition in `POSITION-PAPER.md` §3.2 (94.2 / 5.0 / 0.5 / 0.25) is a partition **of the gravitational potential energy release**, and nothing else. A grep of the whole repository found no kinetic-energy accounting anywhere — two passing mentions of momentum and one bare phase label ("initial failure → accelerating redistribution → v_max → deceleration," `research/GPT-hydrotectonic-flood-model.md` line 530, which is making a stratigraphic-phasing point, not an energy one). Likewise no impact-energy figure exists anywhere in the repo despite the impact swarm being the initiating event (Figure 1).

So the honest position before running anything was: the objection targets a genuine gap in the documentation, and whether it targets a gap in the *physics* was unknown. That is a calculation, not a rebuttal.

`02-theory/rheology/code/` was empty (`.gitkeep` only) before this, so this is the programme's first computational work, landing under the discipline `research-practices.md` §Computational work laid down in advance for exactly this moment.

## What was found

**F1 — the objection does not land.** Bulk KE of the moving continental mass at the programme's own 9–40 cm/s is 0.011% to 0.416% of the friction allocation, against a threshold of 1% declared before the run. Roughly three orders of magnitude below the term it was claimed to dominate. The reason is structural rather than lucky: KE scales as $v^2$ while dissipation scales with distance traveled, and this mechanism is slow motion over thousands of kilometers, which is precisely the regime where path-integrated dissipation swamps endpoint kinetic energy.

**The "equal and opposite" framing is also wrong on its own terms.** It assumes a ballistic picture — spend energy accelerating, coast, spend it again braking. This is a gravity-driven, continuously dissipative system running near terminal velocity, where KE stops accumulating and nothing is banked to be repaid. The everyday parallel is exact rather than rhetorical: Terzaghi effective stress, which this model runs on, is the foundation of slope-stability analysis, and a rain-triggered landslide is this mechanism at small scale. Nobody argues the rain had to supply the landslide's energy.

**F2 — a new internal constraint fell out.** Requiring bulk KE to stay within the budget gives a hard ceiling of 27.7–38.6 m/s, and 6.2–8.6 m/s within the friction allocation. This independently refutes the source document's disputed 30 m/s figure: at 30 m/s, KE is 60–117% of the *entire* 10²⁵ J budget, leaving nothing for the 94.2% residual-PE term. That figure was already rejected on a unit-conversion argument (`../02-theory/kinematics/README.md`); it now fails a second, unrelated test. Worth noting the reverse implication — the velocity reconciliation still open in ROADMAP is now load-bearing against an external objection, not merely an internal tidiness item.

**F3, first version — wrong, and superseded the same day.** It held impact heat against the model's own 5.75×10²³ J dissipation allocation and reported a tension: only 0.01 to 1.38 Chicxulub-equivalents affordable. See the correction below. Retained in the code as `F3_CONTROL` per rules 6 and 11.

## The correction — JD, same day

> In my model Chicxulub was part of the swarm.

Chicxulub is a swarm **member**, not an external yardstick. That reframing broke the first F3 open on two counts.

**Category error.** The 5.75% figure partitions the **GPE release**. It is not a global thermal budget, and impacts are a separate energy input to the system rather than a competing claim on the tectonic partition. The sub-1 K claim answers "does the tectonic mechanism cook the planet," which is a narrower question than "what is the flood year's total thermal load." Testing impact energy against it was comparing the wrong two things.

**Empirically falsified premise.** The first F3 assumed deposited impact energy becomes ocean heat. Because Chicxulub is a swarm member, that assumption is checkable against the actual record rather than argued — and it fails. Chicxulub's dominant global thermal signature was net **cooling**: dust and sulfate aerosol loading drove surface air temperature down by as much as ~26 K with sub-freezing conditions for years, followed by CO₂ greenhouse warming of only 1 to 5 K. The one impact we can observe did not deliver its energy as bulk ocean heat.

**Revised F3: PASS, with large margin.** Tested against marine survivability (+20 to +24 K above present, from measured upper thermal limits of marine ectotherms) rather than against the tectonic partition: the survivability bound is 1.18–1.41×10²⁶ J, which is **11.8× the entire gravitational budget**. The whole budget deposited in the ocean warms it 1.7 K. The model's dissipated share warms it 0.098 K. Swarm sizes affordable on bulk heating alone: 281 bodies at the commonly cited Chicxulub energy, 90 at the assessment low, 2 at the assessment high.

The useful generalization: bulk ocean heating is not the binding constraint on this mechanism at all. The entire objection class that targets it — including the original Everest-column heat-budget critique that started this thread — fails generally rather than in the instance.

## Open

**F4, the real cost of the swarm.** Since thermal energy does not bind swarm size, the limits are radiative and climatic: aerosol/dust shading (running *opposite* in sign to what the objection assumed), CO₂ and sulfate injection from carbonate and evaporite target rock, ejecta re-entry radiation, and survivability of the biota the narrative requires to come through. Stating the rival at its strongest: mainstream geology has **one** such impact driving a mass extinction, so a swarm is by construction a larger perturbation. That is the genuine price the model has to pay, and it is denominated in climate response, not joules. Needs a modeled aerosol/radiative response.

**K-Pg inside the catastrophic interval — a belt commitment awaiting JD's call.** If Chicxulub is a swarm member, K-Pg falls inside the flood interval. `../02-theory/stratigraphy/README.md` and POSITION-PAPER §6.2 currently carry K-Pg as one of three tested-and-rejected candidate boundaries with no positive candidate standing. These cannot both hold. The founding research saw the tension from the other side (lines 857–869): K-Pg is "the strongest candidate if we weight your cosmological-impact forcing heavily" and is the only boundary with "an actual crater and ejecta system." Deliberately not written into the belt here — the inference is clear but it is a belt commitment, and inferring it in silently is the exact failure the appraisal log exists to catch.

Neither ROADMAP item 1 proper (heat **removal** capacity) nor the viscosity gate is touched by any of this. This work bounds heat *generation* terms only.
