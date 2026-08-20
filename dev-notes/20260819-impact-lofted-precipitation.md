# Impact-lofted precipitation — replacing CPT's geysers with the swarm

**2026-08-19, JD-directed.** *"My model doesn't need the vast geysers of CPT sending water up into
the atmosphere, the meteor swarm impacting the water rich crust could have been a significant
mechanism for that."*

Checked quantitatively rather than accepted. The substitution holds with a large margin, and it
produces one genuinely forbidding result plus two new constraints the mechanism now owes.

**Status: scoping arithmetic, not a result.** Loft height and coupling fraction are stipulated.
`WP-HTF-0013` sources them and registers the forbidding claim properly. Belt content landed in
[`../03-solutions-baseline/3.2-theory/water-ledger/README.md`](../03-solutions-baseline/3.2-theory/water-ledger/README.md)
§Precipitation mechanism, with the swarm-timing constraint cross-referenced at F4 in
[`../03-solutions-baseline/3.2-theory/rheology/README.md`](../03-solutions-baseline/3.2-theory/rheology/README.md).

## Why this needed checking rather than agreeing

The claim looked like a free substitution — swap one lofting mechanism for another the model already
carries. Two things made it worth a check. First, the mechanism it replaces (Baumgardner's supersonic
steam jets) was found on 2026-08-19 to fail an enthalpy ceiling by an order of magnitude, so if the
substitute also failed, the model would be left with no precipitation mechanism at all and would not
have noticed. Second, "the swarm can do it" is a capacity claim, and capacity claims are exactly the
class this programme has been wrong about before by asserting rather than computing.

## The vapor ceiling — the one forbidding result

Condensing water vapor releases $L_v = 2.26\times10^6$ J/kg, which must be radiated to space. At the
same runaway-greenhouse ceiling F7/F8 already use (300 W/m², upper end of the 280–310 range), 40 days
permits $1.04\times10^9$ J/m², buying **459 kg/m² ≈ 0.46 m of rain, total**.

**This is stronger and more general than the vapor-canopy finding already in the ledger.** That
finding rejected a canopy as a *reservoir*, on habitability grounds — a claim about where water was
stored. This is a claim about the *phase transition*, so it binds regardless of reservoir:

> No vapor-mediated mechanism can supply more than ~0.46 m of the 40-day rain.

It constrains rival Flood models as much as this one, which is why it is worth registering formally
rather than leaving as an aside. It is also **exactly the constraint Baumgardner names against his own
field** — *"explanations that involve the condensation of water vapor fail because, even assuming
ideal black body conditions, radiation is incapable of removing the latent heat of condensation to
space at a sufficient rate"* (ICC 2003, p.11) — and the reason he reached for entrainment rather than
condensation. This programme reaches the same conclusion independently and gets a better mechanism
out of it.

## Why ballistic lofting works

| | J/kg |
|---|---|
| Loft liquid seawater to 50 km ($gh$) | $4.9\times10^5$ |
| Vaporise it ($c_p\Delta T + L_v$) | $2.6\times10^6$ |

**5× cheaper per kilogram, and no condensation penalty at all** — the water never leaves the liquid
phase, so the ceiling above simply does not apply to it. Same escape Baumgardner used (entrained
liquid, not condensed vapor), reached through a mechanism this programme already holds.

## Capacity — not the binding constraint

Using F3's own affordable swarm sizes, total swarm energy is ~$1.2\times10^{26}$ J across **all three**
of F3's cases. That is a robustness property worth naming: F3 solved for body count against the
survivability bound, so the *total* is insensitive to the disputed Chicxulub energy range
(Durand-Manterola & Cordero-Tercero's $1.3\times10^{24}$–$5.8\times10^{25}$ J vs. commonly cited
figures near $4\times10^{23}$ J). The precipitation result therefore does not inherit that dispute.

| Coupling into water lofting | Rain-equivalent |
|---|---|
| 1% | ~4.7 m |
| 10% | ~47 m |

Against a 40-day benchmark near 100 mm/day (~4 m), **1% suffices.** The margin is large enough that
better sourcing is unlikely to overturn the conclusion — but a stipulated parameter carrying a belt
claim is what rule 2 exists to prevent, so `WP-HTF-0013` sources it regardless.

## Two constraints the mechanism now owes

**1. Swarm temporal distribution.** Ballistically lofted water returns in **1.5–5 minutes** (apex
10–100 km, launch velocity 443–1400 m/s). That is a deluge, not sustained rain. Forty days of rain
requires the swarm spread across 40 days.

This is the **first constraint the belt carries on swarm timing rather than swarm size**. F4 named
the binding limits as radiative and climatic and left them uncomputed; this one is neither, and comes
from a different direction entirely.

**No conflict with the simultaneous-swarm radiometric assumption** ([`../03-solutions-baseline/3.2-theory/stratigraphy/README.md`](../03-solutions-baseline/3.2-theory/stratigraphy/README.md)
§Radiometric): 40 days is ~$10^{-7}$ Myr. "Simultaneous" there means indistinguishable in apparent
age, and a 40-day spread is seven orders of magnitude inside that. Checked rather than assumed,
because a timing constraint arriving after a simultaneity assumption is exactly the shape of an
inconsistency that gets absorbed silently.

**2. The precipitation was saline.** Ballistically lofted seawater falls as brine. Stated before a
critic reaches it. Two consequences, pulling opposite ways, both recorded:

- **Potentially a discriminator.** Ordinary historical geology has no reason to expect a globally
  synchronous saline-precipitation episode; this mechanism requires one. Bears on evaporite
  distribution and brine-signature deposits. **Not registered** — no defined sample, no failure
  condition, and registering it now would repeat the error `discriminators.md` §What does not count
  exists to prevent.
- **A tension with the salinity-refugia section.** That section predicts transient freshwater
  reservoirs and low-salinity geochemistry. Those refugia are sourced from *continental discharge*,
  not rain, so this is not a contradiction — but a mechanism raining brine globally while producing
  freshwater refugia locally owes an account of the coexistence, and does not have one.

## What this settles about the CPT harvest

The steam-jet component was recorded as "leave behind" in
[`20260819-baumgardner-cpt-comparison.md`](20260819-baumgardner-cpt-comparison.md) because it fails
an enthalpy ceiling. **That is not a loss.** This programme never needed it; the substitute is
cheaper, avoids the condensation ceiling by construction, and is observationally anchored rather than
hypothetical, because Chicxulub is a declared swarm member (F3) rather than a proposed process.

That is the clearest instance so far of the component-harvest posture working as intended: a CPT
component was examined, found to fail, and its absence turned out to cost this programme nothing
because its own architecture already covered the function.
