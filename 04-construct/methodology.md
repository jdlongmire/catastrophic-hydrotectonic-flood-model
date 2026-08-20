# Methodology

> **Tier 0.** How this programme is run. The apparatus, not the content.

This programme is organized as a **Lakatosian research programme** evaluated against a **Popperian** standard, inheriting the apparatus developed in [CAC](https://github.com/jdlongmire/creation-actualization-cosmology), [FCD](https://github.com/jdlongmire/creation-cosmology-programmes), and [TRT](https://github.com/jdlongmire/triadic-reality-theory): the hard core is held immune by the negative heuristic; refutation is aimed at the protective belt; the programme's status is judged by whether it generates content that forbids something, not by how much it explains.

## Stand-up state (2026-08-16)

This programme stands up **prose-first**. There is, as yet, no mechanized claims registry (`traceability/claims/*.yaml`), no `ops/*.py` build gates, and no generated progressiveness report. The discipline those tools enforce in the sibling programmes — every claim carries a role; an accommodation states what it forbids (`none` is a legitimate and expected answer); no claim escapes ledger classification — is applied by hand for now, in [`../03-solutions-baseline/3.3-prediction/appraisal.md`](../03-solutions-baseline/3.3-prediction/appraisal.md).

Mechanize once there is enough claim volume that hand-auditing becomes the weaker discipline rather than the honest one. That threshold is a judgment call, not a fixed count; a reasonable trigger is the first time a belt revision is proposed without an obvious place to check it against prior commitments.

**Refinement discussion has its own home, separate from settled content.** [`../dev-notes/`](../dev-notes/) captures technical back-and-forth on the model as it happens — a claim gets checked, a distinction gets drawn, a question stays open pending an answer — before it's resolved enough to promote into the belt, the hard core, or an appraisal log entry. Keeping this separate from `02-theory/` and `03-prediction/` matters for the same reason the appraisal ledger records degenerating moves plainly: an in-progress discussion that gets written directly into settled-looking belt content reads as more resolved than it is.

**Computational rigor is not deferred, even though the traceability layer is.** The first real quantitative work (ROADMAP item 1, the rheology/heat-budget test) will involve scripts, and possibly notebooks, before any mechanized claims registry exists. [`research-practices.md`](methods.md) states the discipline for that work now, in advance of the first script — reproducibility, sourced parameters, no undisclosed fitting, refuted attempts kept and labeled — the same standard already proven out in TRT's `3-prediction/co-admissibility-conjecture/code/`.

## Genre: this is forensic science, and that determines the shape of a valid test

Added 2026-08-19, JD-directed (*"This is a forensics exercise and model"*), grounded in **Cleland, C.E. (2001), "Historical science, experimental science, and the scientific method," *Geology* 29(11):987–990** — primary retrieved and read in full, confidence **HIGH**. Full research capture in [`../dev-notes/20260819-forensic-genre-cleland.md`](../dev-notes/20260819-forensic-genre-cleland.md).

This programme and its rival are both **historical/forensic reconstructions of an unobserved past**, not experimental sciences. Cleland's argument, in a mainstream geology journal: *"When it comes to testing hypotheses, historical science is not inferior to classical experimental science. Traditional accounts of the scientific method cannot be used to support the superiority of experimental work."*

The difference in method tracks a real feature of nature — the **asymmetry of overdetermination**. Because causation runs one way in time, *"localized present events overdetermine their causes."* A past event leaves far more traces than are needed to establish it. So the historical method is not controlled repetition but **Chamberlin's multiple working hypotheses plus a search for a smoking gun**: *"a trace that picks out one of the competing hypotheses as providing a better causal explanation for the currently available traces than the others."*

**Two consequences bind this programme.**

**Pre-registration is not the genre's standard.** Cleland's paradigm smoking gun — the Alvarez K-Pg iridium anomaly — *"was not predicted in advance of its discovery."* Sometimes *"one just gets lucky and stumbles over a smoking gun."* A programme in this genre is not failing by not having pre-registered predictions.

**The genre's actual failure mode is sharper, and this programme is subject to it.** *"Failure to search for a smoking gun deprives a historical hypothesis of empirical grounding, turning it into a dreaded just-so story."* The obligation is the **search** — for traces that discriminate among a stated hypothesis set. That is not weaker than falsificationism; it is a different discipline with a real and nameable failure state, and it is the one this programme must not enter.

**Applies to both accounts, per [`methods.md`](methods.md) rule 4a.** Deep-time historical geology is forensic in exactly the same sense, held to exactly the same smoking-gun standard, and enjoys exactly the same latitude.

## The progressive/degenerating standard, inherited without weakening

A research programme is **progressive** if it predicts novel facts and some are corroborated; **degenerating** if it only accommodates facts post hoc, however elegant the accommodation. Accommodation of an already-known fact contributes nothing to progressiveness. This is the standard the sibling programmes hold themselves to, and it is not relaxed here because the subject matter — terrestrial geology rather than cosmology — is *more* empirically exposed, not less: every belt claim is checkable against an existing, extensively studied rock record, which is a harder environment for a programme to survive in than cosmological structure formation.

## What the initial research already shows, read against this standard

The founding transcript ([`../research/GPT-hydrotectonic-flood-model.md`](../research/GPT-hydrotectonic-flood-model.md)) makes three belt revisions in sequence — the catastrophic-phase onset moved from a Cambrian default, through Permian-Triassic and Triassic-Jurassic candidates, to Cretaceous-Paleogene, and finally to an unspecified diachronous propagation front — each triggered by a class of evidence (paleosols, then persistence of stable terrestrial features past every tested boundary) that the prior position couldn't absorb. Read individually, each revision is legitimate MSRP: belt content is supposed to move under pressure. Read as a sequence with **zero forbidding content added at any step**, it is the textbook degenerating-shift signature, and [`../03-solutions-baseline/3.3-prediction/appraisal.md`](../03-solutions-baseline/3.3-prediction/appraisal.md) records it as such rather than smoothing it into "the model matured."

The transcript also names its own gating problem without closing it: the transient mantle viscosity required for continental translation at the required Flood-year rate (~10¹³–10¹⁴ Pa·s) is roughly five to six orders of magnitude below any viscosity invoked anywhere in mainstream geodynamics, including the most extreme partial-melt weak-zone estimates (~10¹⁹ Pa·s floor). Nothing else in the belt matters until this is addressed — see [`../03-solutions-baseline/3.3-prediction/discriminators.md`](../03-solutions-baseline/3.3-prediction/discriminators.md).
