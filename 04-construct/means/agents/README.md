# Agent Profiles

Reusable, harness-agnostic operating briefs for any **AI-aide** working this research programme — a Claude Code subagent, GPT, OlogosAI, a contributor's assistant. Each profile is a plain-markdown system prompt **bound to this repo's methodology**, not generic role text; load it as the aide's brief for that role.

Harvested from [TRT](https://github.com/jdlongmire/triadic-reality-theory)'s `0-program-methods/agents/` under WP-HTF-0001 and **adapted, not copied**. Three profiles transfer with their bindings re-pointed at this programme's surfaces. The fourth does not: TRT's Formalization-Agent is built around Lean proof obligations this programme has none of, and it was replaced by [Computation-Agent](computation-agent.md), bound instead to [`methods.md`](../../methods.md) rules 14–20. TRT's version also instructed a `Co-Authored-By` commit trailer, which is a banned attribution form here; the QA profile carries the HCAE rule in its place.

## Division of labour (load-bearing)

| Profile | Judges | Does **not** touch |
|---|---|---|
| [`qa-agent.md`](qa-agent.md) | the **machinery** — repo hygiene, links, scripts, structure, conventions | the *truth* of claims or validity of derivations |
| [`peer-review-agent.md`](peer-review-agent.md) | the **content** — belt claims, appraisal, discriminators, the paper | code, structure, committing |
| [`red-team-reviewer.md`](red-team-reviewer.md) | the **root node** — tries to break the rheology/heat gate and anything built on it | fixing what it breaks |
| [`computation-agent.md`](computation-agent.md) | **produces** deterministic scripts behind belt claims | whether the claim is true |
| [`rival-account-advocate.md`](rival-account-advocate.md) | **advocates** for a competing reconstruction — writes the rival's column at its genuine strength | CHFM's column; adjudicating the comparison |

They defer to each other: QA never adjudicates geology; Peer-Review never fixes code. All **recommend**; decision authority stays with JD.

**Rival-Account-Advocate is the odd one out and deliberately so.** The other four evaluate *this programme's* work. It argues *for someone else's*. That exists because [`../../methods.md`](../../methods.md) rule 4a — apply the same metric to the rival's account of the same evidence — is a discipline this programme has repeatedly failed at, and **a discipline that must be remembered is weaker than a role that cannot skip it.** If the rival's column is written by whoever is arguing for CHFM, "state the rival at its strongest" cannot be verified from inside.

**Its dispatch carries one hard constraint:** brief it on the **observable only**, never on CHFM's answer. An advocate shown the opposing account first writes a rebuttal, and a rebuttal is shaped by what it answers. The dispatcher owns that constraint — it is cheap to get wrong and expensive to detect afterwards.

## How to invoke (any harness)

- **Claude Code:** spawn an `Agent` with the profile file's contents as the prompt, plus the target (a diff, a claim, a section).
- **Any chat AI:** paste the profile as the system/opening message, then the target.
- **Automation:** read the profile as the agent's system prompt.

Always give the aide the profile, the specific target, and access to the repo. The profile tells it what to read next.

## Invocation triggers

| Trigger | Profile | NL phrasings |
|---|---|---|
| Before any commit of code or structure; at session-wrap; reviewing a diff for hygiene | **QA-Agent** | "QA this", "hygiene check" |
| Evaluating a claim or section's content; before accepting a contribution as progressive | **Peer-Review-Agent** | "peer-review X", "progressive or degenerating?" |
| Before accepting a conjecture as resolved; **before registering a discriminator**; before an appraisal moves toward *progressive* | **Red-Team-Reviewer** | "red-team this", "try to break it" |
| Working a computational item — a ROADMAP task, a bound, a belt number that needs reproducing | **Computation-Agent** | "compute this", "script the bound" |
| Building or extending the comparative evidence ledger; establishing whether the rival **equally satisfies** a proposed trace (condition 2) before registration; any belt statement of the rival's position with no cited source behind it | **Rival-Account-Advocate** | "write the deep-time column", "steelman the rival", "what does mainstream actually say here?" |

**Chaining:** a computation is *produced* by Computation-Agent → checked by QA-Agent (hygiene, reproducibility) → attacked by Red-Team-Reviewer (validity) → Peer-Review for label calibration. Nothing is accepted on one role's say-so, and all recommend while JD decides.

**Ledger chaining is different, and the ordering matters.** Rival-Account-Advocate writes the competing column **first and uncontaminated**, from the observable alone. Only then is CHFM's column set beside it. Red-Team-Reviewer may then attack *either*. Reversing that order produces a rival column shaped by what it was built to answer, which is the failure the profile's hard constraint exists to prevent.
