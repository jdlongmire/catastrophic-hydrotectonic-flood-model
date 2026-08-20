# Images

Illustrative renders of belt content. **Illustration is not evidence** — a visualization can make a mechanism look resolved when the underlying physics isn't. Where an image states a number, it is checked against the audited research the same way any other belt claim would be; discrepancies are recorded here rather than silently absorbed.

## `initial-supercontinental-crust-model.png`

Cross-section of the pre-Flood water-rich porous crust — pore water, fracture water, fault-zone water, interstitial water, hydrothermal fluids down to the ~30–40 km crust-mantle transition. Matches [`../../03-solutions-baseline/3.2-theory/water-ledger/README.md`](../../03-solutions-baseline/3.2-theory/water-ledger/README.md); no numerical claims to check.

## `initial-meteor-event.png`

Five-panel sequence: multiple impacts → energy deposition → crustal shock/fracturing → pore-pressure surge → hydrotectonic failure. Matches the mechanism as actually stated in the source research — impacts as threshold-crossing triggers, not literal displacement engines ("the collective meteoritic event provides the trigger; the water-rich porous crust provides the mechanism"). **Does not bear on the rheology gate** ([`../../03-solutions-baseline/3.2-theory/rheology/README.md`](../../03-solutions-baseline/3.2-theory/rheology/README.md)): it renders the qualitative failure sequence, not whether the required 10¹³–10¹⁴ Pa·s viscosity collapse is physically reachable. Treat as illustration of mechanism, not as progress on the gating open problem.

## `hydrotectonic-breakup-sequence.png` — revised, filed 2026-08-19

**Supersedes `continental-shift.png` and `continental-shift-cropped.png`**, both moved to [`archive/`](archive/) rather than deleted, per [`research-practices.md`](../../04-construct/methods.md) rules 6 and 17 — superseded work is kept and labelled, not removed.

Five-panel mechanism sequence (pre-impact supercontinent → impact disruption → hydrotectonic failure → rapid plate transport → post-catastrophic relaxation) over a six-frame continental-positions timeline with per-phase bullets.

**What the revision fixes — both of the predecessor's flagged defects:**

- **Naming.** States **"Supercontinent (Pangaea)"**, matching the 2026-08-19 retirement of "Araratia" ([`../../dev-notes/20260819-retire-araratia.md`](../../dev-notes/20260819-retire-araratia.md)). The predecessor displayed the retired term and was flagged stale on that point the same day.
- **Pacing.** The predecessor's panel 2 showed near-complete rifting into continent-shaped blocks at "Days to Weeks," ahead of peak transport at "Months to ~1 Year." The revision front-loads far less: "Impact Onset / Fracturing & Initial Rifting" at days-to-weeks, "Early Dispersion" at weeks-to-months, "Peak Transport" at months-to-a-year. Consistent with the model's own relaxation profile.

**Velocity — improved, not fully resolved.** The predecessor stated a hard range of ~0.01–0.1 m/s, whose ceiling sat at or below the research floor of 9–40 cm/s — the discrepancy that forced the crop. The revision states **"~cm–dm/s"** as an order of magnitude, which does accommodate 0.09–0.406 m/s when read as order-of-magnitude (0.4 m/s being 4 dm/s) in a way the old hard range could not. **Still not the belt figure itself**: [`../../03-solutions-baseline/3.2-theory/kinematics/README.md`](../../03-solutions-baseline/3.2-theory/kinematics/README.md) derives 9–40 cm/s specifically, and a future render should state that. Recorded as a residual, materially reduced from the predecessor's outright conflict.

**Three discrepancies flagged rather than absorbed:**

- **Trigger drawn as a single impact.** Panel 2 renders one cataclysmic impact. The belt commits to an impact **swarm** — F3/F4 in [`../../03-solutions-baseline/3.2-theory/rheology/README.md`](../../03-solutions-baseline/3.2-theory/rheology/README.md), with Chicxulub a declared member, and as of 2026-08-19 a requirement that the swarm be **temporally distributed across the 40 days** ([`../../03-solutions-baseline/3.2-theory/water-ledger/README.md`](../../03-solutions-baseline/3.2-theory/water-ledger/README.md) §Precipitation mechanism). This is a **regression against a sibling figure**: `initial-meteor-event.png` correctly renders multiple impacts. Correct on the next render.
- **"Pore pressure exceeds lithostatic stress"** (panel 2) overshoots the derived requirement. `WP-HTF-0003` solves a pore-pressure ratio of λ = 0.999995 to 0.9999996 — approaching lithostatic from *below*, not exceeding it. Panel 1's "near lithostatic" is correct; panel 2 is not, and the two disagree with each other.
- **Subduction is depicted as accomplished.** "Subduction on all major margins," "subduction recycles crust." The vertical/subduction half of the mechanism is the **open rheology gate**, still 3–4 orders of magnitude short. Same caveat this README already applies to `initial-meteor-event.png`: **illustration of a mechanism, not progress against the gating open problem.**

**Timescales check out.** ~50,000 yr pre-impact interval (belt: ~50–60 kyr creation-to-Fall); one-year catastrophic phase; ~6,000 yr post-Flood relaxation with exponential velocity decay, matching the belt's $v(t) = v_0 e^{-t/\tau} + v_\infty$.

**Verdict: viable and an improvement on what it replaces.** Filed as the figure of record for the breakup sequence. Three items for the next render: multiple impactors, the pore-pressure wording, and the specific 9–40 cm/s figure.

## `archive/` — superseded, retained

- **`continental-shift.png`** — the predecessor infographic. Displays the retired name "Araratia" and the conflicting ~0.01–0.1 m/s velocity range. Kept as the record of what was audited on 2026-08-16 and what the 2026-08-19 revision was measured against.
- **`continental-shift-cropped.png`** — the paper-use derivative created 2026-08-16 (JD-directed) with the disputed displacement-statistics row cropped out, formerly Figure 3 in the position paper. The crop was a workaround for the velocity conflict; the revision addresses that conflict directly, so the derivative has no remaining use. Its real cost is now recoverable: the displacement distances (2,000–6,000 km average, 8,000–12,000+ km maximum) that were lost with the cropped row and are consistent with the research could be restored on a future render.

## Use in the position paper, 2026-08-16

`initial-meteor-event.png` (Figure 1) and `initial-supercontinental-crust-model.png` (Figure 2) are embedded in [`../../paper/POSITION-PAPER.md`](../../paper/POSITION-PAPER.md) — neither carries a numerical claim needing reconciliation.

`continental-shift.png` (now archived) was initially held out of the paper entirely (JD-directed) because its velocity figure conflicts with the research figure *and* with the paper's Section 3.4 discussion of the hydroplaning source's internal velocity inconsistency. **Resolved, 2026-08-16, JD-directed:** `continental-shift-cropped.png` — a derivative with the bottom displacement-statistics row (the panel carrying the disputed velocity figure) cropped out — is now embedded as Figure 3. The breakup-sequence and continental-positions-through-time content above that row carries no numerical claim needing reconciliation; the displacement-*distance* figures (2,000–6,000 km average, 8,000–12,000+ km maximum), which are consistent with the research, were in that same removed row and are no longer shown — a real loss, traded for removing the disputed velocity line, since the row could not be split further without reconstructing the panel. The source `continental-shift.png` is untouched and remains the file of record; `continental-shift-cropped.png` is a paper-use derivative only. Revisit both once the velocity/detachment-depth reconciliation (`../../02-theory/kinematics/README.md`) is actually done — at that point the original panel could potentially be corrected and restored rather than cropped.

**Superseded 2026-08-19.** The paragraph above records the 2026-08-16 state and is kept as the dated record of it, per rule 6. It is no longer current: `continental-shift-cropped.png` is **no longer Figure 3** and both `continental-shift` files are archived. Figure 3 in [`../../paper/POSITION-PAPER.md`](../../paper/POSITION-PAPER.md) is now `hydrotectonic-breakup-sequence.png`, with its caption rewritten to state what the revision fixed and the two residual mismatches it still carries. The "revisit once the velocity/detachment-depth reconciliation is actually done" condition was met — `WP-HTF-0003` closed it 2026-08-18 — and the revision is that revisit.
