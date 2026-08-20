# mode.md — the doorway

**Read this first.** Model-agnostic; no harness assumed. This file orients an AI-aide or a human contributor in one page and routes to everything else. It does not restate the programme's content — it says where the content is and what discipline governs touching it.

## What this is

**An alternative forensic inference model for reconstructing Earth history from the geological observational record — carrying a specific physical mechanism.** Both halves are load-bearing, and the second is where the programme can be wrong.

Structured as a **Lakatosian research programme** and evaluated against a **Popperian** standard. Not a completed theory and not presented as one.

### The inference-model half

The rock, fossil, isotopic, geomorphological and geophysical observations are the **data**. Neither deep time nor this programme is the data — both are reconstructions built on top by an inference model ([`methods.md`](04-construct/methods.md) rule 23):

$$\text{Observation} \longrightarrow \text{Inference Model} \longrightarrow \text{Historical Reconstruction}$$

So the programme does **not** have to show that conventional geology cannot accommodate an observation. Usually it can, and conceding that is rule 27's L1. The question is whether an observation *uniquely identifies* its historical reconstruction. **This cuts both ways**: this programme's own results are equally reconstructions, and the F-series are conditional consistency checks on its *own* historical inputs, not measurements.

### The mechanism half — and why the self-description needs it

An inference framework alone cannot be quantitatively wrong. This programme asserts specific dynamics: continental hydroplaning at **9–40 cm/s** on a **15 km detachment** under Terzaghi-collapsed pore pressure, and localized runaway subduction for the vertical leg. Those claims carry numbers, have scripts behind them, and can fail on their own terms — F7, F8 and F10–F13 are physics, not framework comparison.

**Describing the programme as only an inference model would hand it a retreat** — *"we merely offer a framework"* — precisely when a mechanism claim failed. The mechanism is what makes this refutable, and per rule 26 the **translation term is its non-subsumable content**: what CHFM claims that generic flood catastrophism does not.

### Objective, stated at two levels so it can be failed

| Level | Claim | Whose |
|---|---|---|
| **Family** | A catastrophic reconstruction is causally sufficient for observation $E$ | Shared with every other Flood model |
| **CHFM** | **Hydrotectonic translation is what makes it sufficient — and where it is not sufficient, say so** | This programme's alone |

The trailing clause is not decoration. An objective that cannot be failed is not an objective.

**Standing verdict: too early to appraise. No discriminator yet evaluated against data.** Any session that ends with that sentence still true has not failed — but any session that quietly changes it without an evaluated discriminator has.

*Recalibrated wording, 2026-08-19 — no standard relaxed.* This line previously read *"unappraised. Zero discriminators evaluated."* It led with a count that reads as a verdict on the **model** when it is a description of its **age**, on a scorecard the rival is never handed ([`methods.md`](04-construct/methods.md) rule 4a). The programme is days from stand-up and Lakatos's framework has no "failing" category for a programme this young. The substantive fact is unchanged and is the one that governs: **no trace has yet been checked that picks this programme out from its competitors.** Two registered exclusions (E1, E2) now exist and are real evidential products under rule 24(b), but neither is a smoking gun and neither moves the verdict.

## The one thing to understand before contributing

A Lakatosian programme has a **hard core** that is immune *by decision*, not by demonstration, and a **protective belt** that absorbs pressure. That structure is legitimate methodology, and it is also exactly how a programme degenerates if nobody watches. So this repo keeps the watch explicit:

- [`appraisal.md`](03-solutions-baseline/3.3-prediction/appraisal.md) is a standing, dated self-audit answering *progressive or degenerating*, including entries against the programme's own interest.
- [`discriminators.md`](03-solutions-baseline/3.3-prediction/discriminators.md) holds candidates that must **forbid** an observation the rival account does not equally forbid, with the failure condition frozen **before** evaluation. Candidates checked and killed are retained, not deleted.
- **A recorded refutation is a completed result, not a cost.** This is structural: see the `commitment: stretch` semantics in [`05-work-packages/README.md`](05-work-packages/README.md). It is written down because the programme once logged a refutation against itself and had to issue the correction the same day.

## Where things are

| Need | Read |
|---|---|
| Structure and why it is this shape | [`00-meta-model/`](00-meta-model/) |
| The plan — positive heuristic, objectives | [`01-strategic-baseline/`](01-strategic-baseline/) |
| Requirements, interfaces, verification | [`02-systems-baseline/`](02-systems-baseline/) — mostly stubs, honestly labelled |
| **The programme itself** — core, belt, predictions | [`03-solutions-baseline/`](03-solutions-baseline/) |
| How it reasons; how work gets done; agents and ops | [`04-construct/`](04-construct/) |
| Committed and stretch work | [`05-work-packages/`](05-work-packages/) |
| The published paper and its DOI record | [`paper/`](paper/) |
| Working discussion, resolved and open | [`dev-notes/`](dev-notes/) |
| Founding transcript and citation ledger | [`research/`](research/) |

## Working rules that bite most often

Full set in [`methods.md`](04-construct/methods.md); these four cause the most rework when skipped.

- **Rule 8 — search both literatures** (mainstream *and* creationist: *Journal of Creation*, CRSQ, ARJ, ICR) before recording a verdict. Violated twice; a cost was written into the appraisal that the creationist literature directly contradicted.
- **Rule 10 — retrodiction is expected Tier 2 work.** Tag `forbids: none`. The four discriminator conditions govern **Tier 3 only**; applying them to interpretive work is a tier error.
- **Rule 11 — surface a flipped result *before* writing the verdict down.**
- **Rule 13 — record access failures** (URL, status, date) where the claim lives, and escalate via the direct PDF path rather than the HTML landing page.

## Session lifecycle

```
python3 04-construct/means/ops/research-start.py   # orientation, read-only
...work...
python3 04-construct/means/ops/research-wrap.py    # hygiene gate; nonzero exit = not wrapped
```

Then append a session entry to [`04-construct/means/sessions/`](04-construct/means/sessions/).

Four agent profiles live in [`04-construct/means/agents/`](04-construct/means/agents/) — QA, Peer-Review, Red-Team, Computation. Reach for the one whose trigger fires; that README carries the dispatch table.

## Authority

**JD Longmire decides.** Belt commitments, Tier 3 registrations, appraisal verdicts, and the progressive-versus-degenerating call are his — every work package's `authority_boundary` names where its own edge lies. An AI-aide proposes, drafts, computes, and refutes; it does not move a verdict.

## Attribution

Work products carry the single provenance line **`Human-Curated, AI-Enabled (HCAE)`** and no model or supplier attribution in any form — no `Co-Authored-By` trailer, no "generated with" line, no model-signed confidence rating.
