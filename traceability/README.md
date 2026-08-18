# traceability/

**Not instantiated.** This directory is a placeholder with a stated intent, not a
working system, and `research-start.py` reports it as such rather than as a
passing check.

## What belongs here

[TRT](https://github.com/jdlongmire/triadic-reality-theory) carries the machinery
this programme would port: `claims/` (one YAML per claim, schema-validated),
`schemas/claim.schema.yaml`, `scripts/build.py` (validates every claim, verifies
the `depends_on` dependency graph is **acyclic**, regenerates reports), and
`generated/` (built reports, gated as fresh at session-wrap).

## Why it matters here specifically

This programme's belt has real coupling — [`WP-HTF-0002`](../05-work-packages/WP-HTF-0002-mosa-belt-interfaces/package.yaml)
exists to declare that dependency graph and prove it acyclic, and the 2026-08-17
coupling chain is the concrete case it must represent. A claim registry is also
what would let the standing question *"what would overturn this?"* be answered
mechanically rather than by re-reading the belt.

Until then, dependency structure lives in prose in the belt READMEs, and the
circularity discipline in [`methodology.md`](../04-construct/methodology.md) is
applied by hand.

## Do not

Do not add a stub `build.py` that exits 0. A green check that verifies nothing is
worse than an honest absence — the wrap gate would then report traceability
passing while nothing is traced.
