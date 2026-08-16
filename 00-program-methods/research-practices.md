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

## Computational work — scripts & notebooks

Nothing in this programme has needed code yet. This section is written *before* that work starts, per [ROADMAP](ROADMAP.md) item 1 (the rheology/heat-budget quantification) — the first real computational task — so the discipline is in place before the first script, not retrofitted after.

8. **Notebooks are drafts; scripts are the record.** Exploratory work can happen in a notebook. A number that lands in a belt README or an appraisal claim must be reproducible from a plain, deterministic script — a figure cited from a notebook cell that isn't independently re-runnable isn't yet citable.

9. **State the model, the source, and the run command in the file's own header.** Every script's docstring states: what physical model it implements, the verified primary source for any parameter it uses (with the specific equation or figure, not just "the literature"), whether it's deterministic, and the exact command to reproduce it. A script that can't be re-run by someone else from its own header isn't finished.

10. **No fitted parameters without saying so, explicitly.** If a script tunes a value to match a target output, the header says so in plain language. "No fitted parameters" is a claim that has to be true, not an aspiration — say it only when it's checked.

11. **Negative controls stay, and stay labeled.** A comparison calculation that turns out to be the wrong test (like the wrong-comparison $\dot\gamma$ control TRT's `coadmissibility_ratedep.py` keeps rather than deletes) remains in the code, explicitly marked as a control, so a reader can see what was ruled out and why — not just what worked.

12. **Say what the result does *not* resolve.** A script closing one sub-question states plainly what it leaves open, so a green run against one narrow claim isn't read as the whole gate closing. The rheology gate in particular ([`02-theory/rheology/README.md`](../02-theory/rheology/README.md)) has several sub-parts (energy budget, heat-removal capacity, feedback-loop magnitude) — a script addressing one doesn't close the others.

13. **Co-locate code with the belt claim it supports.** `02-theory/<topic>/code/`, not a monolithic top-level `scripts/` folder — the same pattern TRT uses (`3-prediction/<test>/code/`). Keeps the path from a README claim to the calculation behind it short and obvious.

14. **Commit code with the doc it grounds, in the same commit.** A script and the README/appraisal claim citing its output land together — never a claim first with the code to follow, and never code with no claim pointing at it.

## GitHub-safe math (for any derivations in prose)

- `\mathrm`, not `\operatorname`.
- `\lvert` / `\rvert` for absolute values, not bare `|` — Kramdown reads a pipe as a table delimiter and strips it from inline math.
