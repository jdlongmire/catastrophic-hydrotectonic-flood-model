# 05-work-packages/

Authored **work packages** for coherent multi-step delivery.

```text
05-work-packages/<slug>/package.yaml
```

Convention adopted from [`mxm-assistant-001`](https://github.com/ologos-repos/mxm-assistant-001)'s
`05-work-packages/`, whose `ADR-MXM-META-0001` declares the VWMM structural convention
(`00-meta-model` … `05-work-packages`, zero-padded) the org-wide standard going forward
(CA, 2026-08-07). This repo adopts it via `WP-HTF-0001`.

## Required fields

| Field | Meaning |
|---|---|
| `id` | Stable id (e.g. `WP-HTF-0001`) |
| `title` | Short name |
| `scope` | In / out of scope |
| `authority_boundary` | What is allowed without re-asking |
| `actions` | Planned actions (list) |
| `verification` | How done is proven |
| `disposition` | open / approve / merge / defer / cancel |
| `status` | proposed \| approved \| in_progress \| done \| cancelled |

## Research-programme adaptation

Two fields carry extra meaning here, inherited from TRT's PI-planning practice:

- **`commitment: committed \| stretch`.** A *committed* package is bounded and mechanical; it
  will land. A *stretch* package is a research attempt, and **the commitment is to run it to a
  recorded resolution, not to a positive result.** A recorded refutation closes a stretch
  package successfully. This is deliberate: it prevents the failure recorded on 2026-08-17,
  where a refutation was logged as a cost against the programme rather than as completed work.
- **`authority_boundary`** is where [`research-practices.md`](../00-program-methods/research-practices.md)
  rule 11 becomes structural rather than habitual. Belt commitments, Tier 3 registrations, and
  appraisal verdicts are JD's; a package that would touch them says so here.
