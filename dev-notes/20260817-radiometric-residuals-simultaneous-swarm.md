# Radiometric residuals from a simultaneous swarm

**Status: captured, analysis open.** A load-bearing belt assumption that existed nowhere in the repository before this note. Pointer added to `02-theory/stratigraphy/README.md`. Not yet promoted to a belt commitment — two problems below need answers first, and one possible discriminator needs an evaluability check.

## The assumption (JD, 2026-08-17)

> And remember the Mount St Helens impact on radiometric dating — part of my assumptions is that the meteor swarm all happened at the same time and thus would have similar radiometric residuals and accounts for the K-Pg boundary and the geologic column just with a different chronology than the standard model.

Unpacked into its parts, since they carry different evidential weight:

1. **The Mount St Helens datum.** Austin, S.A. (1996), "Excess Argon within Mineral Concentrates from the New Dacite Lava Dome at Mount St. Helens Volcano," *Creation Ex Nihilo Technical Journal* 10(3):335–343. Dacite that solidified on the lava dome in 1986 gave a whole-rock K-Ar age of 0.35 ± 0.05 Ma, with mineral concentrates from the same rock ranging 0.34 ± 0.06 Ma (feldspar-glass) to 2.8 ± 0.6 Ma (pyroxene). Interpreted as excess argon occluded in phenocrysts within the magma chamber and retained through emplacement. Confidence **MEDIUM** — figures consistent across multiple secondary reports of the paper; primary not read in full.
2. **Simultaneity.** The swarm is a single event, not a sequence spread over deep time.
3. **Similar residuals.** Simultaneity implies the swarm's products carry comparable radiometric anomalies.
4. **Explanatory scope.** Those residuals account for the K-Pg boundary *and* the geologic column, under a different chronology than the standard model.

This connects directly to the belt commitment flagged in [`20260817-start-stop-energy-objection.md`](20260817-start-stop-energy-objection.md): Chicxulub-in-the-swarm places K-Pg inside the catastrophic interval, and this note supplies the mechanism by which that could be reconciled with the column's apparent ages.

## The rival at its strongest (research-practices.md rule 4)

The Mount St Helens result has a substantial mainstream answer that has to be stated in full, not gestured at, because part of it bears directly on the extension in §3–4 above.

- **Method applied outside its validated range.** The samples went to a laboratory whose stated K-Ar detection floor is approximately 2 Ma. All but one of the reported results fall below that floor, so the measurements sit inside the analytical noise the method itself declares.
- **Phenocryst and xenocryst contamination is a known, screened-for phenomenon.** Inherited argon in phenocrysts is documented in the mainstream literature; geochronologists treat impure mineral fractions as unusable rather than as evidence against the method.
- **The strongest form, and the one that matters most here: the discordance is itself the diagnostic.** A single rock yielding 0.34 Ma on one fraction and 2.8 Ma on another is, to a geochronologist, a contaminated sample announcing itself. Spread across mineral fractions is precisely the internal error-detection signal the method relies on. The result demonstrates that misapplied K-Ar *fails detectably*, which is a weaker conclusion than "K-Ar ages are unreliable."

None of this makes excess argon unreal. It does mean the datum supports "K-Ar can be badly wrong on young volcanic rock with inherited argon, and says so when it is" rather than "apparent ages across the column are residuals."

## Problem 1 — "similar" and "ordered" pull in opposite directions

This is the sharper of the two problems, and it is internal rather than borrowed from the rival.

"Similar residuals" is doing two different jobs in the assumption, and they are not compatible:

- **Job A: explaining coherence within one event.** Why do the products of a single catastrophic episode date consistently with each other? Similar residuals answer this well, and it genuinely supports reading K-Pg as a real, coherent marker horizon rather than a time plane.
- **Job B: explaining the ordered spread across the column.** Cambrian at ~540 Ma, K-Pg at ~66 Ma — a factor of eight, monotonically ordered with stratigraphic position. Similar residuals predict a *flat* apparent-age profile. They cannot produce an ordered gradient, because similarity is the opposite of the systematic variation the column displays.

Job B needs residuals that vary systematically with stratigraphic position — burial depth, thermal history, distance from impact-generated melt, or some other ordering variable. That is a substantially stronger and more specific claim than the one stated, and it needs its own mechanism. As written, the assumption delivers Job A and leaves Job B unaddressed.

## Problem 2 — inter-system concordance

Excess argon is a K-Ar / Ar-Ar mechanism specifically. It has no obvious purchase on:

- **U-Pb**, which carries its own internal cross-check (two decay chains, concordia)
- **Rb-Sr** and **Sm-Nd** isochrons, different chemistry, different closure temperatures, different half-lives

The column's radiometric framework rests substantially on *agreement between* systems that fail in unrelated ways. A mechanism that perturbs argon retention does not obviously perturb uranium-lead. For the assumption to carry Job B, it needs either a common mechanism across systems or a separate account per system.

## Where this genuinely helps the programme

Recorded because it is a real gain, not a consolation. §6.2 and [`../03-solutions-baseline/3.2-theory/stratigraphy/README.md`](../03-solutions-baseline/3.2-theory/stratigraphy/README.md) reject three candidate boundaries on the grounds that paleosols, coal, and reefs recur *above* each of them. That test was conducted using the standard model's stratigraphic assignments. If the column's apparent chronology is residual-derived, then "above the boundary" does not mean "after the flood" in the sense the test assumed, and the rejection may be **mis-specified rather than correct**. This does not vindicate any of the three candidates, but it weakens the negative case against them further than the Oard & Klevberg field dispute alone did, and it partly rehabilitates K-Pg specifically — which is the boundary the founding research already called "the strongest candidate if we weight your cosmological-impact forcing heavily" and the only one with "an actual crater and ejecta system" (lines 857–869).

## Possible discriminator — needs an evaluability check first

Asking what this forbids (rule 5), there is a candidate with real discriminating content:

**If the swarm was simultaneous, impact markers at widely separated stratigraphic levels should share a common geochemical fingerprint.** Same swarm, related parent bodies, comparable impactor composition. Standard geology permits iridium anomalies, shocked quartz, and spherule layers at various levels but expects them to be *unrelated events with independent signatures*. A common fingerprint across horizons the standard model separates by tens of millions of years is something the rival account forbids and this one requires.

**The check that has to come first, and it is not favorable so far.** A search for well-established impact-marker horizons at major boundaries *other than* K-Pg did not return them. What it returned was debate about the vertical distribution of iridium and shocked quartz *within* the K-Pg interval itself — concentrations peaking in a carbonaceous claystone above the boundary claystone, with remobilization by bioturbation and slumping actively disputed. That is a different phenomenon from multi-horizon impact markers, and it does not support the discriminator.

So before this can be registered in `03-prediction/discriminators.md`, someone has to establish that a testable inventory of non-K-Pg impact horizons exists at all. If it does not, the discriminator has no defined sample and fails condition 3 of the programme's own standard. That check has not been done.

## Open

- Supply an ordering mechanism for Job B, or narrow the assumption's stated scope to Job A.
- Address inter-system concordance, or state explicitly that the claim is confined to K-Ar / Ar-Ar.
- Run the non-K-Pg impact-horizon inventory check before proposing the discriminator.
- Decide the K-Pg belt commitment flagged in the sibling dev-note, which this assumption bears on directly.
