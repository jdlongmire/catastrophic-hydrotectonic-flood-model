# Research Practices

> **Tier 0.** Working rules. Short, and each one exists because of a specific failure mode — inherited from [CAC](https://github.com/jdlongmire/creation-actualization-cosmology)/[FCD](https://github.com/jdlongmire/creation-cosmology-programmes)/[TRT](https://github.com/jdlongmire/triadic-reality-theory)'s `research-practices.md`, adapted here with an explicit computational-work section this programme didn't previously have.

## General

1. **Declare before you test.** Falsification conditions, thresholds, and what a result would need to show are fixed *before* the computation runs. A criterion set after seeing the output is an accommodation whatever it's labeled — see [`03-prediction/discriminators.md`](../03-prediction/discriminators.md) condition 4.

2. **Primary sources, or an explicit mark.** Every physical constant, empirical figure, or cited result carries a confidence label — HIGH (verified primary), MEDIUM (secondary with specifics), LOW (paraphrase), UNCERTAIN — matching the source discipline already applied when auditing the initial research and the visualization set. A number without a source is not yet usable in a claim.

3. **Report disputes, do not smooth them.** Where a figure is contested in the literature (e.g. the range of proposed vapor-canopy depths, competing mantle-viscosity estimates), state the range and the disagreement rather than picking the value that's convenient.

4. **State the rival at its strongest.** Ordinary historical geology's account of the same observation gets its best form, not a weak one — an accommodation or discriminator claim that doesn't do this isn't assessable.

5. **Ask what the step forbids.** At every belt step, computational or not. If the answer is "nothing," it's coherence work, and it's logged as such in `03-prediction/appraisal.md`.

6. **Record refuted variants of your own.** A superseded calculation stays in the repository with the reason it died, rather than being deleted. A belt that shows no casualties is not a belt.

7. **No model or supplier attribution.** The only provenance mark on any artifact here is `Human-Curated, AI-Enabled (HCAE)`.

8. **Search both literatures before recording any verdict.** On any question where a "requires time," "requires slow process," or "requires quiet conditions" identification is doing the work, the creationist technical literature — *Journal of Creation*, *Creation Research Society Quarterly*, *Answers Research Journal*, ICR — is searched **before** a conclusion is written into the belt or the appraisal, not after. Read the **primary**, not a summary of it. Apply the same confidence labels (rule 2) and the same dispute-reporting (rule 3) as to any other source: a creationist paper is a source of interpretive alternatives to be evaluated, not an authority that ends inquiry, and reporting one as more settled than its own author does is the mirror-image of the failure this rule exists to prevent — always carry what the author concedes.

   *Why this rule exists.* It has fired twice. The founding research declared three candidate boundaries dead on paleosol, coal and reef evidence; the correction was that Oard & Klevberg (2022) dispute the paleosol *identification* in the field, in the formation immediately above K-Pg. Then on 2026-08-17 a "cost" against the programme was written into `03-prediction/appraisal.md` on the strength of a single mainstream-phrased search, asserting that deep-tier *Zoophycos* requires a stable substrate — when Woodmorappe (2006) is a dedicated treatment of that exact objection, addresses that exact ichnogenus, and states the opposite. Both failures had the same shape: a mainstream identification treated as the settled fact of the matter when it was a contested interpretation.

9. **Fold external results into this model's own framing, and say what it adds.** Adopting a result from the wider creationist literature is not citation, it is integration, and it carries three obligations. State the result in this programme's own vocabulary and tier structure. Say explicitly what it does for the hydrotectonic framing specifically — whether it supplies a mechanism the belt lacked, removes a constraint, or merely coexists. And say what this model contributes *back* that the source did not have, if anything, since that is where the programme earns its keep rather than borrowing. Worked example: Woodmorappe's PPLC hypothesis requires alternating deposition and rapid lithification but supplies no mechanism for the alternation; hydroplaning under near-lithostatic pore pressure is inherently episodic at local scale and is a candidate for exactly that, which is a contribution back rather than a borrowing (see [`../02-theory/stratigraphy/README.md`](../02-theory/stratigraphy/README.md) §Trace fossils).

10. **Retrodiction is the expected mode while the belt is being built — label it, do not avoid it.** This programme is in its interpretive-construction phase: the work of building a coherent alternative reading of the evidence under the hard core's framing. Explaining an already-known observation is legitimate and expected work here, and Lakatos's own methodology requires that budding programmes be treated leniently rather than held to the standard of a mature one. **What is required is the label, not abstention:** belt entries that explain existing evidence are tagged `forbids: none`, so the appraisal can later distinguish accommodation from forbidding content without slowing the construction down now. The strict four-condition standard in [`../03-prediction/discriminators.md`](../03-prediction/discriminators.md) governs **Tier 3 claims only** — it is not a filter on Tier 2 interpretive work, and applying it there is a tier error.

    *Why this rule exists.* On 2026-08-17 an interpretive observation of JD's — that a catastrophic flood would produce a fuzzy boundary horizon — was escalated into a discriminator proposal, judged by the Tier 3 conditions, killed, and logged as a cost. Three steps, none of them what was actually being done. The Tier 2 content was sound and simply needed recording as belt material.

11. **Surface a flipped result before writing it down.** When a check reverses the expected outcome of work in progress, bring the finding back before committing a verdict to the belt or the appraisal. The check itself is never optional — rule 1 requires it — but a result that changes the direction of a claim is a decision point for the principal, not a conclusion to be executed unilaterally.

## Computational work — scripts & notebooks

This section was written *before* the programme's first script existed, so the discipline was in place rather than retrofitted. The first computational work landed 2026-08-17 — [`../02-theory/rheology/code/energy_partition_bounds.py`](../02-theory/rheology/code/energy_partition_bounds.py), an energy-partition completeness check — and exercised rules 12–18 including the negative-control rule, which retains a refuted framing rather than deleting it. [ROADMAP](ROADMAP.md) item 1 proper (heat *removal* capacity) is still open; that script bounds generation terms only.

12. **Notebooks are drafts; scripts are the record.** Exploratory work can happen in a notebook. A number that lands in a belt README or an appraisal claim must be reproducible from a plain, deterministic script — a figure cited from a notebook cell that isn't independently re-runnable isn't yet citable.

13. **State the model, the source, and the run command in the file's own header.** Every script's docstring states: what physical model it implements, the verified primary source for any parameter it uses (with the specific equation or figure, not just "the literature"), whether it's deterministic, and the exact command to reproduce it. A script that can't be re-run by someone else from its own header isn't finished.

14. **No fitted parameters without saying so, explicitly.** If a script tunes a value to match a target output, the header says so in plain language. "No fitted parameters" is a claim that has to be true, not an aspiration — say it only when it's checked.

15. **Negative controls stay, and stay labeled.** A comparison calculation that turns out to be the wrong test (like the wrong-comparison $\dot\gamma$ control TRT's `coadmissibility_ratedep.py` keeps rather than deletes) remains in the code, explicitly marked as a control, so a reader can see what was ruled out and why — not just what worked.

16. **Say what the result does *not* resolve.** A script closing one sub-question states plainly what it leaves open, so a green run against one narrow claim isn't read as the whole gate closing. The rheology gate in particular ([`02-theory/rheology/README.md`](../02-theory/rheology/README.md)) has several sub-parts (energy budget, heat-removal capacity, feedback-loop magnitude) — a script addressing one doesn't close the others.

17. **Co-locate code with the belt claim it supports.** `02-theory/<topic>/code/`, not a monolithic top-level `scripts/` folder — the same pattern TRT uses (`3-prediction/<test>/code/`). Keeps the path from a README claim to the calculation behind it short and obvious.

18. **Commit code with the doc it grounds, in the same commit.** A script and the README/appraisal claim citing its output land together — never a claim first with the code to follow, and never code with no claim pointing at it.

## GitHub-safe math (for any derivations in prose)

- `\mathrm`, not `\operatorname`.
- `\lvert` / `\rvert` for absolute values, not bare `|` — Kramdown reads a pipe as a table delimiter and strips it from inline math.
