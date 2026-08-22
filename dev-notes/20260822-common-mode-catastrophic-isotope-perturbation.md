# Common-Mode Catastrophic Isotope Perturbation Hypothesis

**Status: captured, analysis open.** JD offered this "for consideration" — not yet steelmanned against the rival, not yet checked for an evaluability gap on its own proposed discriminator. Pointer added to [`../03-solutions-baseline/3.2-theory/stratigraphy/README.md`](../03-solutions-baseline/3.2-theory/stratigraphy/README.md).

## The hypothesis (JD, 2026-08-22)

A single global tectono-hydrothermal catastrophe imposes a common forcing event on radiometric systems worldwide, while producing heterogeneous apparent ages because different rocks and minerals respond differently to that event:

$$\text{Global catastrophe} \rightarrow \text{tectonic + thermal + hydrothermal forcing} \rightarrow \text{isotopic disturbance} \rightarrow \text{structured radiometric age distribution}$$

The global event supplies common forcing through heating, extreme fluid circulation, pressure changes, deformation, recrystallization, dissolution/reprecipitation, and elemental transport. Each sample's isotopic response then depends on its local conditions:

$$R_i = f(E_G, I_i, T_i, P_i, F_i, \phi_i, D_i, C_i)$$

— $E_G$ the global event, $I_i$ the inherited isotope state, $T/P$ the thermal-pressure history, $F$ fluid flux, $\phi$ permeability, $D$ diffusion behavior, $C$ mineral-specific closure/retentivity.

One event therefore need not produce one radiometric age. It could produce: essentially unaffected minerals retaining inherited signatures; partially reset systems producing discordant ages; completely reset systems recording the disturbance; mixed domains containing inherited and altered isotope populations; isotope gain or loss through hydrothermal transport; and, under demonstrated circumstances, apparently concordant secondary ages.

JD's stated basis: several components are already established experimentally and observationally — hydrothermal/metamorphic events alter isotope systems; one event affects different grains differently; different chronometers have different resistance to resetting; discordance can preserve the signature of a later alteration event; hydrothermal alteration can sometimes produce apparently concordant secondary U-Pb ages. The extension is the scale — one *global* event as the common forcing term.

Stated as a named hypothesis:

> **Common-Mode Catastrophic Isotope Perturbation Hypothesis:** A globally extensive tectono-hydrothermal catastrophe produced a temporally correlated disturbance of radiometric systems, with local geological and mineralogical boundary conditions transforming that common forcing into the observed mixture of concordance, discordance, inheritance, partial resetting, and apparent-age distributions.

**Deliberately assumes ordinary decay rates.** It asks whether conventional isotope chemistry, diffusion, fluid transport, recrystallization, and open-system behavior can explain some significant portion of the apparent deep-time chronology before reaching for something as radical as accelerated nuclear decay.

**JD's stated strongest test:** analyze the disturbance rather than filtering it out. Raw discordant U-Pb data from geographically separated rocks should contain statistically recoverable common-mode structure correlated with independent evidence of thermal and hydrothermal disturbance, if the hypothesis is correct.

**JD's stated scope, narrowed explicitly:** not "radiometric dating is unreliable." Rather — "some portion of what is conventionally interpreted as a sequence of widely separated geological events may instead represent heterogeneous isotopic responses to a common catastrophic event."

## Where this sits in the existing belt

- **Generalizes the 2026-08-17 assumption.** [`20260817-radiometric-residuals-simultaneous-swarm.md`](20260817-radiometric-residuals-simultaneous-swarm.md) captured "simultaneous swarm → similar residuals" and left two problems open: (1) *similar* residuals explain coherence within one event but cannot produce the column's ordered spread (Job A vs. Job B), and (2) excess argon is K-Ar/Ar-Ar-specific with no stated purchase on U-Pb/Rb-Sr/Sm-Nd concordance. This hypothesis replaces "similar" with a per-sample response function $f(E_G, I_i, T_i, P_i, F_i, \phi_i, D_i, C_i)$ — structurally capable of producing *ordered*, not merely coherent, variation if the local variables (burial depth, distance from forcing source, thermal history) themselves vary systematically with stratigraphic position, and is stated generically enough to apply across chronometer systems rather than being tied to argon retention specifically. Whether it actually resolves either problem, or merely restates them as free parameters in $f$, is unchecked.
- **A candidate structural form for $H$.** The stratigraphy README's DFM formulation, $R_{now} = F(R_0, \lambda, t, H)$ (added 2026-08-18), left the Flood-year perturbation term $H$ unspecified beyond naming it. This hypothesis proposes decomposing $H$ into a common global forcing $E_G$ plus a per-sample response function over local boundary conditions — a materially more specific proposal than anything currently on record for $H$, and one that stays inside the layering already drawn in [`hard-core.md`](../03-solutions-baseline/3.1-hypothesis/hard-core.md) (line 36): $R_0$ is DFM's problem, this programme's stake is $H$.
- **Ordinary-decay-rate framing matches the existing disclosure.** Hard-core's DFM disclosure already notes this programme does not inherit accelerated decay's heat-generation problem. This hypothesis's explicit commitment to test ordinary decay first, before reaching for anything radical, is consistent with that stated posture rather than introducing a new one.

## What's not yet done here

- **Rival not yet steelmanned (rule 4).** Thermal/hydrothermal overprinting and its geochronological signatures are an established, well-studied phenomenon in mainstream geochronology — Pb-loss trajectories, discordia chords anchored on a lower intercept at the disturbance age, U-Pb "resetting ages" are standard interpretive tools, not something the standard model lacks an account for. The open question is whether the proposed discriminator (statistically recoverable common-mode structure across geographically separated, independently-dated disturbance events) forbids anything the standard model doesn't already predict, or whether it describes a pattern the standard model treats as expected and already explains locally (event-by-event) rather than globally (one common $E_G$).
- **Discriminator evaluability unchecked (rule 5 / Cleland smoking-gun standard, per [`20260819-forensic-genre-cleland.md`](20260819-forensic-genre-cleland.md)).** "Statistically recoverable common-mode structure ... correlated with independent evidence of thermal and hydrothermal disturbance" needs a defined sample and a stated recovery method before it is a discriminator rather than a research direction. No dataset has been identified.
- **Problems 1 and 2 from the sibling note are addressed structurally, not resolved.** The response function's generality is exactly what would need to be cashed out against real multi-system, multi-locality data to show it produces the *specific* ordered, concordant pattern observed, rather than being general enough to fit any pattern after the fact — the same ad-hoc-tuning risk the $R_0$ discussion already flags for DFM's initialization problem.

## Open

- Steelman the mainstream discordia/Pb-loss/resetting-age literature before treating "common-mode structure in discordant U-Pb data" as a novel prediction.
- Identify whether a real dataset exists — geographically separated discordant U-Pb results with independent, dated thermal/hydrothermal disturbance evidence — that could actually be tested against this hypothesis, or whether the discriminator fails condition 3 (no defined sample) the way the non-K-Pg impact-horizon discriminator did in [`20260817-radiometric-residuals-simultaneous-swarm.md`](20260817-radiometric-residuals-simultaneous-swarm.md).
- Decide the relationship between this note, the 2026-08-17 note, and the DFM $H$ formulation — supersede, sit alongside, or merge into one stated position.
