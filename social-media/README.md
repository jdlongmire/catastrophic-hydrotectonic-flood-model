# Social Media

Long-form written distribution content, distinct from [`../assets/videos/`](../assets/videos/)'s per-package promo copy. That folder carries short/medium/long *teaser* copy tied to a specific rendered video; this folder carries standalone articles meant to be read on their own — Substack pieces first, other platforms as they come up.

## Structure

```
social-media/
  substack/     full article drafts and published copies, one file per piece
  <platform>/   add as needed — same convention, own subfolder
```

## Convention

- One file per article/post, `YYYYMMDD-slug.md` — same chronological-sort convention as [`../dev-notes/`](../dev-notes/), for the same reason (plain directory listing sorts in order).
- An article draws on the programme's belt docs and position paper rather than restating research from scratch — cite `00-program-methods/POSITION-PAPER.md` or the specific belt doc a claim traces to, the same discipline the video narration and the paper itself already follow.
- Once a piece is actually published (Substack, elsewhere), note the live URL and publish date at the top of its file — mirrors how `00-program-methods/publishing/` records the real DOI once a Zenodo submission goes live, not just the staged draft.
- Register and voice follow `meta-harness/mind.md`'s Register One (informal — conversational but substantive, minimal scaffolding, no headers/tables in body) unless a specific piece calls for Register Two.

## Source of record

Facts, figures, and open-question framing here should trace back to the position paper and belt docs, not diverge from them. If an article's claim and a belt doc's claim disagree, the belt doc is authoritative and the article is due for a correction — same rule the position paper itself states about its own relationship to the belt.
