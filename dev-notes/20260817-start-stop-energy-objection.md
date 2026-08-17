# Start/stop energy objection — the "car crash" term

**Status: resolved for F1/F2, open for F3.** Promoted to `02-theory/rheology/README.md` (§Energy-partition completeness check), `03-prediction/appraisal.md`. Code: `02-theory/rheology/code/energy_partition_bounds.py`.

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

**F3 — the harder finding, and it goes against the programme.** Holding impact heat within the model's own total dissipation allocation (5.75×10²³ J) affords only 0.01 to 1.38 Chicxulub-equivalent bodies. N_max exceeds one only under the cheapest cited Chicxulub estimate. The "swarm of large meteor impacts" language in the README and both video summary sets is not obviously compatible with the published thermal partition.

This was not part of the objection. It surfaced from the programme's own check, which is the intended function of declaring conditions before the run rather than after.

## Open

F3 needs one of: an explicit impactor-size budget consistent with the thermal allocation, a modeled partition of impact energy between terrestrial heat / ejecta / radiation to space (currently the calculation conservatively assumes all of it becomes heat), or a revision of the "swarm" framing toward fewer or smaller bodies. The founding research's threshold-crossing argument (lines 199–217, impacts as trigger rather than engine, "greatly reduces the impact-energy requirement") addresses what the trigger must *supply* and does not bound what a body of given size *deposits*, so it does not resolve this on its own.

Neither ROADMAP item 1 proper (heat **removal** capacity) nor the viscosity gate is touched by any of this. This work bounds heat *generation* terms only.
