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

They defer to each other: QA never adjudicates geology; Peer-Review never fixes code. All **recommend**; decision authority stays with JD.

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

**Chaining:** a computation is *produced* by Computation-Agent → checked by QA-Agent (hygiene, reproducibility) → attacked by Red-Team-Reviewer (validity) → Peer-Review for label calibration. Nothing is accepted on one role's say-so, and all four recommend while JD decides.
