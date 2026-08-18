# Videos

**Package convention (SOP as of 2026-08-16):** each video package gets its own subfolder here — the rendered asset(s) plus a `social-media-summaries.md` carrying the short/medium/long copy and hashtags for every cut in that package. Don't drop bare `.mp4` files directly in `videos/`; a package folder is one video's or one release's worth of content, not one file.

```
videos/
  intro/
    hydrotectonic-flood-model-vertical-180s.mp4
    hydrotectonic-flood-model-horizontal-300s.mp4
    social-media-summaries.md
  <next-package>/
    ...
    social-media-summaries.md
```

## Packages

- [`intro/`](intro/) — introductory narration covering the programme's core commitment, mechanism, water budget, and honest research standing. Two cuts: 180s vertical (TikTok/Shorts), 300s horizontal (YouTube long-form), both narrating over the three renders in [`../images/`](../images/) with the caption/headline text confined to a top band so it never overlaps the illustrative content.
- [`global-intro/`](global-intro/) — supersedes `intro/` as the front door to the programme, 2026-08-16. Introduces the layered mechanism (hydroplaning for lateral translation + localized subduction-channel viscosity reduction for vertical descent) as a single coherent pitch, drafted and approved in-chat before any build step per the video-narration skill's SOP. One cut: vertical only (~236s).
