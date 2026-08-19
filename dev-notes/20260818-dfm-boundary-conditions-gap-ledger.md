# DFM boundary-conditions gap ledger — drafting record

**Status: conceptual capture, not belt content by itself.** This note is the full drafting
record for WP-HTF-0009. Individual items are promoted into `02-theory/` with `forbids: none`
tags where the thread produced real structural content; this file is the trail showing where
each promoted item came from and, as importantly, what did *not* get promoted.

**Origin.** Two-stage exchange, 2026-08-18. An external interlocutor's structured critique
(radiometric/ice-core/paleomagnetic/stratigraphic/biological closure, demanding quantitative
simultaneous constraint closure) was answered against the belt as it actually stood — which
conceded most of the critique's specific points, since the appraisal's own verdict already said
so. JD then supplied a second pass: not a rebuttal, but a structured account of what that
exchange had actually changed in the *state* of eight gap items, plus a layering point about
where this programme's explanatory burden should stop.

## The three-state model — JD's framing, adopted as the standard for this note

$$\text{Gap} \rightarrow \text{Candidate mechanism identified} \rightarrow \text{Quantitatively tested}$$

This matters because the honest description of what happened is narrower than it might sound.
**Nothing below reaches the third state.** Several items move from the first state to the
second. That is real — a defined research question is worth more than an undefined one — but
it is conceptual reorientation, not empirical closure, and this note says so at every item
rather than once at the top and then drifting.

Per [`research-practices.md`](../04-construct/methods.md) rule 10, everything here is Tier 2
interpretive/structural work and is tagged `forbids: none` wherever it lands in the belt. Per
rule 5, the appraisal is unaffected — ask what each step forbids, and the answer throughout is
"nothing yet."

## 1. Radiometric — broaden beyond excess-argon to the DFM $R_0$ question

**Where this stood:** `02-theory/stratigraphy/README.md` §Radiometric interpretation captured
only the Mount St Helens excess-argon/simultaneous-swarm-residual hypothesis (Austin 1996),
already flagged as too narrow and blocked on two problems (similarity predicts a flat
apparent-age profile, not the column's ordered spread; excess argon is K-Ar/Ar-Ar specific with
no stated purchase on U-Pb/Rb-Sr/Sm-Nd concordance).

**What this thread adds.** The excess-argon hypothesis is one candidate mechanism inside a
larger, more fundamental question this programme had not stated at all: DFM's own formulation,

$$R_{now} = F(R_0, \lambda, t, H)$$

DFM does not require accelerated decay (so it does not inherit accelerated decay's heat
burden — a different problem from this programme's own rheology heat budget, but the same
family of objection). What it needs instead is a coherent **initialized isotopic state $R_0$**
that need not itself have been produced by antecedent decay, since creation is read as a
functionally mature deployment (hard-core commitment 4).

**The reframed research question:** can a coherent initialized $R_0$, followed by ~50–60 ka
pre-Flood history, catastrophic Flood-system perturbation, and ~5–6 ka post-Flood history,
reproduce the observed multi-system isotopic relationships — specifically **concordance**
across U-Pb, Pb-Pb, Rb-Sr, Sm-Nd, Lu-Hf, K-Ar/Ar-Ar and other systems, with independent
half-lives and different chemical behaviors?

This is harder than the excess-argon question and also the actually relevant one: if
reproducing concordance requires individually tuned $R_0$ per mineral or specimen, the proposal
is ad hoc; if a compact initialization rule generates the observed relationships across systems
with independent decay constants, that is a real result. **No such inventory exists.** The
required work is a constraint inventory across the named systems — not attempted here.

**State change: "K-Ar candidate only" → "DFM initialization hypothesis identified; multi-system
quantitative formulation absent."** The excess-argon material is not withdrawn — it remains a
narrower candidate that may still explain the K-Pg-specific datum — but it is no longer the
programme's whole stated radiometric position.

**Layering note.** $R_0$ itself is DFM's variable, not Hydrotectonic's — see §9 below. What
belongs in *this* repo is whether the Flood-year perturbation ($H$ in the formula) is
consistent with whatever $R_0$-plus-history DFM eventually proposes, not deriving $R_0$ itself.

## 2. Ice cores — no longer conceptually empty

**Where this stood:** nothing. The appraisal and belt were silent on ice cores entirely; the
phase schema draft flagged an "ice-core flag noted" without content.

**What this thread adds.** The programme already permits a pre-Flood polar cryosphere — nothing
in the hard core or belt forbids it, and P1 Antediluvian (stratigraphy phase schema) covers
tens of thousands of years of stable pre-Flood conditions. That licenses a four-phase ice
chronology:

$$I_{pre} \rightarrow I_{Flood} \rightarrow I_{post\text{-}Flood\ Ice\ Age} \rightarrow I_{modern}$$

**This changes the question rather than answering it.** The prior implicit framing — squeeze
100,000+ alleged annual layers into 6,000 years — is not what this programme needs to do,
because $I_{pre}$ can legitimately carry genuine annual layers over the ~50–60 ka pre-Flood
interval. Nothing here needs reinterpreting as non-annual by construction. The Flood disrupts
or destroys some fraction of $I_{pre}$; $I_{post\text{-}Flood\ Ice\ Age}$ is a second,
high-accumulation glacial regime (N2, already in the phase schema); $I_{modern}$ is actualistic.

**The question becomes:** can extant cores be partitioned, physically and chronologically,
among $I_{pre}$, a catastrophic transition zone, accelerated post-Flood accumulation, and later
ordinary accumulation — rather than asking every layer in every core to be sub-annual.

**The hard discriminator is unchanged and is the interlocutor's own framing, not weakened by
this reframe:** a demonstrably continuous, independently-annualized sequence (seasonal
chemistry, dust, tephra, cosmogenic isotopes) whose total length exceeds the total chronology
this model can supply for it — $I_{pre}$'s ~50–60 ka plus whatever fraction of the transition
and post-Flood regimes applies to that specific core — still fails the model if found.
Reframing where the annual layers are allowed to live does not remove the test; it changes what
the test is measuring.

**State change: "No position" → "Phase architecture defined ($I_{pre}/I_{Flood}/I_{post\text{-}
Flood}/I_{modern}$); core-specific chronology and mass-balance modeling absent."** New home:
[`02-theory/cryosphere/README.md`](../03-solutions-baseline/3.2-theory/cryosphere/README.md).

## 3. Glaciation — the initial condition has changed

**Where this stood:** N2 Ice age in the phase schema (`stratigraphy/README.md`) — single ~700
yr relaxation event, Oard's warm-ocean/aerosol-cooled-continent mechanism, no ice mass, no
energy balance.

**What this thread adds.** The post-Flood Ice Age is not being asked to build ice from nothing.
Introducing pre-Flood polar ice caps on a low-relief supercontinent (already implied by §2 and
by the existing "lower supercontinental relief" addition to $S_0$, `20260817-initial-conditions-
topography-biodiversity.md`) gives a different initial-value problem:

$$\text{stable polar glaciation} \rightarrow \text{Flood disruption} \rightarrow \text{warm ocean + atmospheric loading} \rightarrow \text{expanded post-Flood glaciation} \rightarrow \text{deglaciation}$$

**The calculation this licenses, not yet run**, needs: surviving/preexisting ice mass, ocean
temperature after the catastrophe, evaporation and moisture transport, aerosol forcing,
accumulation rate, ablation, ice-sheet flow, maximum ice volume, and deglaciation
energy/meltwater budget. None of these terms exist anywhere in this repo yet — the closest
existing content is the rheology gate's thermal work (F1–F3, `rheology/README.md`), which
bounds *tectonic* heat, not the atmosphere-ocean-cryosphere energy balance this needs.

**State change: "Structural mechanism, no initial condition" → "Structural mechanism and
initial conditions specified; coupled climate/ice mass-energy calculation absent."** Content
lands alongside ice cores in the new `02-theory/cryosphere/README.md`, since the two share an
initial-condition and are naturally one calculation once attempted.

## 4. Stratigraphy — the 50–60 ka interval changes the burden

**Where this stood:** the phase schema (adopted 2026-08-17) already reframes the Flood boundary
as diachronous, $t_C(x)$, but the belt's working posture still leaned toward treating most rock
as needing a Flood-year explanation, with pre-Flood/post-Flood time used narrowly (paleosols,
Zoophycos construction, coal).

**What this thread adds — probably the largest single item here.** Made explicit and general:
Hydrotectonic does not need to explain the *entire* sedimentary record inside the Flood year.
Three depositional regimes, not one:

$$G_{pre} + G_{Flood} + G_{post}$$

with the pre-Flood interval alone (~50–60 ka, hard-core commitment 4's belt estimate) supplying
room for reef construction, soils, erosion, river systems, ecological succession, fossilization,
sedimentation, and genuine annual varves — before any catastrophic mechanism is invoked — and
~5–6 ka post-Flood for substantial further development.

**Illustrative rate arithmetic** (order-of-magnitude only, not sourced to a specific formation;
flagged for a real reef-accretion literature check before this becomes more than illustration):
at 1 mm/yr, 60 ka permits ~60 m (~197 ft) of accumulation; at 10 mm/yr, 60 ka permits ~600 m
(~1,969 ft). Measured/reconstructed reef accretion rates in the literature are, on inspection,
sufficient to generate very substantial structures inside that window — this specific claim is
unverified here and needs primary sourcing (rule 2) before it carries any weight in the belt.

**The reframe this licenses:** stop treating the geological column primarily as a binary
(Flood deposit? yes/no) and instead partition it:

$$D(x) = \{D_{pre}, D_{Flood}, D_{post}\}$$

This makes $t_C(x)$ considerably more powerful than the 2026-08-17 draft stated it — the Flood
transition need not correspond to one universal lithostratigraphic boundary *and* large
fractions of column thickness on either side of it can be ordinary-process time rather than
catastrophic-interval time, which is a different and stronger claim than "the boundary is
diachronous" alone.

**State change:** the phase schema already moved this once (2026-08-17); this thread moves it
again, from "diachronous boundary, three depositional regimes not yet made explicit as a
partition function" to "explicit $D(x)$ partition concept, no formation-by-formation
$D_{pre}/D_{Flood}/D_{post}$ assignment done, and the reef-accretion-rate claim specifically
needs sourcing." Promoted into `stratigraphy/README.md` as a new section; ROADMAP item 3
(assign formations, date-stamp the schema) already covers the mechanical follow-through.

## 5. Varves — explicit three-regime model

**Where this stood:** `stratigraphy/README.md` §Rhythmites already carries a salinity-refugia/
pycnocline-trapping reading for Flood-interval lamination, with the Oard–Whitmore GRF dispute
reported at strength and the appraisal's own caution that reinterpreting every chronometer
risks an unfalsifiable moving target (ROADMAP item 3 raised in priority partly for this reason).

**What this thread adds.** §4's $G_{pre}/G_{Flood}/G_{post}$ partition applied specifically to
laminated sequences:

$$L_{pre} = \text{genuine annual varves over tens of thousands of years}$$
$$L_{Flood} = \text{rapid event/subannual rhythmites}$$
$$L_{post} = \text{post-Flood annual/seasonal accumulation}$$

**Why this is worth recording as a distinct addition rather than folded silently into §Rhythmites:**
it removes a burden the existing section was implicitly carrying — the prior framing risked
reading as though *every* lamination in the record needed a catastrophic explanation, which is
both unnecessary and is exactly the kind of move the appraisal's moving-target caution warns
against. $L_{pre}$ can be conventional annual varves without cost to the model; only $L_{Flood}$
needs the rapid-lamination mechanism (Berthault, Mount St Helens, PPLC).

**The discriminator sharpens rather than changes:** does a particular laminated sequence
contain independently demonstrated annual cycles (seasonal proxies, cross-basin correlation)
that, on this model's own $D(x)$ partition, exceed the chronology available to whichever regime
that sequence is assigned to — not "exceed 6,000 years" flatly. This is testable sequence by
sequence and is a genuine sharpening of the existing §Rhythmites discussion, not a new
mechanism.

**State change: "Chronometer reinterpreted as rapid lamination" (single mode) → "Three-regime
model — most lamination is ordinary, only $L_{Flood}$ needs the rapid mechanism."** This is a
narrowing of the model's own claim, which is the right direction for the appraisal's moving-
target concern. Promoted as an explicit addition to `stratigraphy/README.md` §Rhythmites.

## 6. Freshwater ecology — a new Hydrotectonic subproblem

**Where this stood:** `water-ledger/README.md` §Salinity refugia already states a mechanism
(non-uniform water column, local Richardson-number stratification) and flags an unregistered
discriminator (freshwater/marine indicators as contemporaneous lateral facies vs. ordinary
geology's time-separated transgression-regression reading).

**What this thread adds — sharper predictions, not a new mechanism.** Making explicit that
global inundation does not imply instantaneous hydrological homogeneity, given moving
continental blocks, differential subsidence, large freshwater discharge, and changing basin
connectivity:

$$W(x,t) = f(D, S, T, Q, C, B)$$

(depth, salinity, temperature, discharge, sediment concentration, basin connectivity — all
varying continuously). This is the same claim already in the belt, stated as a function rather
than prose, plus a sharper list of what the model should predict, worth recording because it
converts the existing discriminator from one prediction (contemporaneous facies) into five
specific correlated observables the fossil/sediment record could show together at a genuine
refugium: coherent freshwater ecosystems; independent low-salinity geochemistry; nearby or
adjacent marine conditions; relatively abrupt environmental boundaries; evidence of temporary
basin isolation. A site showing several of these *together*, rather than any one alone, is a
better test than the single-predicate version already in the belt.

**State change: "Mechanism stated, one discriminator flagged" → same state, sharpened
prediction set.** This does not move from Gap to Candidate — it was already Candidate — but the
prediction is now specific enough to be closer to registrable once ROADMAP item 2 (paleocurrent/
motion-vector reconstruction) and a defined sample exist. Promoted as an extension to
`water-ledger/README.md` §Salinity refugia.

## 7. Fossil succession — coupled ecological-hydraulic sorting, forward-model framing

**Where this stood:** `discriminators.md` candidate 1 (ecological-province co-occurrence) is
the initial research's strongest candidate, already stated as a multivariate sorting function
in that document. `kinematics/README.md` separately develops the hydraulic-sorting mechanism
(entrainment under a moving bed, 9–40 cm/s).

**What this thread adds.** Naming the full multivariate form explicitly and, more importantly,
naming the *method* that would actually test it:

$$R_f = f(E_c, H, Q, S, \rho, B, v, t)$$

(initial ecological province, habitat, discharge, salinity, density, basin geometry,
transport velocity, time). The addition worth recording is not the variable list — candidate 1
already implies most of it — but the **forward-model framing**: start with a plausible
pre-Flood ecological geography, impose the modeled catastrophe, and ask what fossil
distribution results, rather than starting from the observed column and constructing a sorting
explanation for it after the fact. The second approach is retrodiction by construction; the
first is a real prediction with a failure mode.

**This is not yet attempted and is a substantially larger undertaking than anything else in
this note** — it requires the Euler-pole reconstruction (ROADMAP item 2), the hydraulic-coupling
magnitude candidate 1 and the kinematics section both currently leave undetermined, and an
actual ecological-province map, none of which exist.

**State change: "Sorting function named, no test method" → "Sorting function named, forward-
model test method specified, no input data or coupled simulation exists."** Recorded as an
addendum to `discriminators.md` candidate 1 rather than a new candidate — it sharpens how
candidate 1 would be evaluated, it does not add new forbidding content on its own.

## 8. Biology — no longer conceptually empty

**Where this stood:** the appraisal states plainly that nothing exists on biology.
`20260817-initial-conditions-topography-biodiversity.md` flagged "rich biodiversity as
functionally-mature deployment" as an open, unexplored extension of hard-core commitment 4, with
no literature check and no specified claim.

**What this thread adds — an explicit historical architecture:**

$$\text{designed initial biodiversity} \rightarrow 50\text{–}60\text{ ka diversification} \rightarrow \text{Fall ecological transition} \rightarrow \text{continued diversification} \rightarrow \text{Flood bottleneck/filter} \rightarrow 5\text{–}6\text{ ka radiation}$$

with an explicit pre-Fall ecological reading: ordinary non-human death, decomposition, nutrient
cycling, and speciation are permitted; predation, harmful parasitism, and pathogenic
exploitation are excluded pre-Fall. (This is a theological/biological claim inherited from
commitment 4's DFM import, not derived here — flagged for whoever eventually formalizes it that
it needs its own sourcing pass, separate from this note.)

**Why this reframes the problem rather than solving it.** The prior implicit burden — generate
observed biodiversity from a bottleneck in ~4,500 years — is not what this architecture asks.
The actual research problem is whether observed mutation, recombination, selection, population
dynamics, and speciation rates can generate the required diversification delta across **two**
windows: ~50–60 ka pre-Flood (unconstrained by a bottleneck) and the post-Flood bottleneck-to-
radiation window (~5–6 ka, constrained by a small founding population per kind). That is a
large, well-defined quantitative population-genetics project. It has not been started.

**Layering note, sharper here than anywhere else in this ledger.** Most of this architecture is
not Hydrotectonic's to own. Designed initial biodiversity and the pre-Fall ecological reading
are DFM's variables (parallel to $R_0$ in §1). The 50–60 ka pre-Flood and 5–6 ka post-Flood
diversification-rate modeling belongs upstream (DFM) and downstream (Post-Flood Recovery
Models) respectively, per §9. **What is actually Hydrotectonic's job is narrower: the
bottleneck/filter mechanism itself** — survival through the catastrophic transition (which
organisms, how many founders, by what physical mechanism they cross F1–F4) — since that is the
one piece of this architecture that depends on the Flood-year mechanics this repo actually
models (habitat destruction timing, refugia per §6, translation/deposition per the phase
schema).

**State change: "Nothing exists" → "Historical architecture specified; population-genetics
quantification absent; and most of the architecture belongs to sibling programmes, not this
one."** New file: [`02-theory/biology/README.md`](../03-solutions-baseline/3.2-theory/biology/README.md),
scoped narrowly per the layering note rather than absorbing the full architecture.

## 9. The layering point — where Hydrotectonic's burden actually stops

**Not one of the eight gap items — a structural correction that applies across all of them.**

The programme has been carrying explanatory burden that belongs one level upstream. The
architecture, stated explicitly for the first time here though implicit in hard-core.md's
existing DFM disclosure (commitment 4, "second disclosure" paragraph):

$$\text{Methodological Designism} \rightarrow \text{Designed Functional Maturity (DFM)} \rightarrow \text{Hydrotectonic Programme} \rightarrow \text{Post-Flood Recovery Models}$$

DFM supplies initialization, chronology, and biological starting conditions ($R_0$, initial
biodiversity, the pre-Flood cryosphere, the 50–60 ka figure itself). Hydrotectonic's job is
narrower and, properly scoped, harder: given those upstream boundary conditions, is the
proposed catastrophic transition from the DFM initial/pre-Flood state to the post-Flood state
physically possible. Post-Flood Recovery Models (glaciation/deglaciation relaxation, tectonic
relaxation, ecological radiation) sit downstream, consuming Hydrotectonic's output state as
their own initial condition.

**What this changes in practice.** Several ROADMAP items proposed elsewhere in this note (the
$R_0$ multi-system inventory in §1; most of the population-genetics work in §8) are not this
repo's work to schedule — they are DFM's or Post-Flood Recovery's, and Hydrotectonic's own
ROADMAP should track them as *dependencies to consume*, not *items to execute*. This is
recorded in `ROADMAP.md` explicitly, split by which programme owns each new item, rather than
left implicit and re-discovered as scope creep later.

**Not a hard-core change.** hard-core.md commitment 4 already imports DFM; this section makes
the downstream chain explicit and draws the scope boundary that follows from it. It is
documentation of an existing commitment's implications, not a new one.

## What did not get promoted

- The reef-accretion-rate literature claim in §4 is illustrative arithmetic only, not sourced —
  flagged, not carried into the belt as a supported figure.
- The pre-Fall no-predation/no-harmful-parasitism reading in §8 is carried as DFM's claim,
  inherited, not independently sourced here.
- Nothing in this note is registered as a Tier 3 discriminator. Several items sharpen existing
  flagged-not-registered candidates (§6, §7); none newly satisfies discriminators.md's four
  conditions.
- The verdict in `appraisal.md` does not change. See the log entry dated alongside this note.

**Source:** this thread, 2026-08-18 (external interlocutor exchange, then JD directly). No
external literature retrieved for this note specifically; where an existing belt document is
extended, its own sourcing stands; where new claims are illustrative or inherited, that is
stated at the item rather than implied.
