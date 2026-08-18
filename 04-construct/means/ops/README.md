# ops/

Session lifecycle and repository tooling.

| Script | What it does |
|---|---|
| `research-start.py` | orientation briefing — VCS, standing verdict, work packages, open dev-notes, link integrity. Read-only. |
| `research-wrap.py` | hygiene gate — clean tree, links resolve, attribution invariant, package schema, computations reproduce. Nonzero exit means not wrapped. |
| `linkcheck.py` | verifies every relative link resolves. Gated at wrap. |
| `relink.py` | repairs relative links after a structural move, driven by git's own rename map. `--labels` also fixes path-shaped link labels. |
| `rename_sweep.py` | classifier-first name substitution — classifies every occurrence by role and substitutes only live references. |

`research-start.py` and `research-wrap.py` are ported from [TRT](https://github.com/jdlongmire/triadic-reality-theory) under WP-HTF-0001, re-pointed at this tree. Checks bound to machinery this programme lacks (Lean, the traceability build) are **absent rather than stubbed green** — see [`../../../traceability/README.md`](../../../traceability/README.md) for why that matters.

`relink.py` and `rename_sweep.py` were written for specific refactors but are kept rather than deleted: both hand-done renumber sweeps on 2026-08-17 broke cross-references, and the next mass edit should reach for a classifier and a dry run rather than a `sed`.
