# Citation Validation

The audit trail for every external source this programme's belt docs and position paper actually rely on. Modeled on the citation-validation-report pattern already established in JD's prior slice ([`global-flood-hydrotectonic-model`](https://github.com/jdlongmire/global-flood-hydrotectonic-model)`/theory/literature/CITATION_VALIDATION_REPORT.md`), adapted to this programme's actual state: confidence is reported honestly per source, not uniformly claimed.

**What this file is not:** a PDF archive. Full-text redistribution of copyrighted third-party journal content (CRSQ, Journal of Creation, Nature) is not undertaken here, matching the prior repo's own established practice of citing and verifying rather than archiving. The one source with a license permitting reuse (Fei et al. 2017, *Science Advances*, open access) has its relied-upon passages excerpted in [`sources/fei-et-al-2017-excerpts.md`](sources/fei-et-al-2017-excerpts.md) rather than the full paper reproduced.

## Summary

| Source | Confidence | Primary text obtained? | Used in |
|---|---|---|---|
| Fei et al. 2017 | HIGH | Yes (PMC5462500) | `rheology/README.md`, `discriminators.md`, position paper §4.2 |
| Oard & Klevberg 2022 | HIGH | Yes (CRSQ 58:204–219, full PDF) | `stratigraphy/README.md`, position paper §6.2 |
| Doyle 2017 | HIGH (text) / MEDIUM (relevance) | Yes (*Journal of Creation* 31(3):5–7, full PDF) | `dev-notes/20260816-boundary-search-literature.md` |
| Pearson et al. 2014 | MEDIUM | No — identity confirmed, exact figures not pulled from primary text | `water-ledger/README.md`, position paper §5.1 |
| USGS water inventory | HIGH | Yes — figures matched exactly against usgs.gov/water-science-school | `water-ledger/README.md`, position paper §5.1 |
| Vardiman (ICR), canopy figures | MEDIUM | No — WebSearch-sourced, not a primary-document pull | `water-ledger/README.md`, position paper §5.3 |
| Dillow 1981 | MEDIUM | No — WebSearch-sourced, not a primary-document pull | `water-ledger/README.md`, position paper §5.3 |
| Biek & Gonzalez 2001 | LOW (secondary) | No — cited only via Oard & Klevberg 2022's own citation of it, not independently checked | position paper §6.2 |
| Whitcomb & Morris 1961 | Background only | Not applicable — general reference, no specific figure drawn from it | position paper §9 |
| Longmire 2025 (*Global Flood Hydrotectonics* v2.5) | Self-authored, directly accessible | N/A | source of hydroplaning mechanism, Darcy-flow figures, energy budget — see internal-inconsistency note below |
| Longmire (draft), DFM | Self-authored, directly accessible | N/A | `hard-core.md` commitment 4 |
| Mainstream mantle-viscosity baselines (10²⁰–10²¹ Pa·s present-day, ~10¹⁹ Pa·s partial-melt floor) | As stated in the initial research transcript | Not independently re-verified against a specific named paper | `rheology/README.md` |

## Detail

### Fei et al. 2017 — HIGH confidence

Fei, H., Yamazaki, D., Sakurai, M., Miyajima, N., Ohfuji, H., Katsura, T., & Yamamoto, T. (2017). A nearly water-saturated mantle transition zone inferred from mineral viscosity. *Science Advances*, 3(6), e1603024. DOI: [10.1126/sciadv.1603024](https://doi.org/10.1126/sciadv.1603024).

Retrieved 2026-08-16 via PMC5462500 (science.org returns HTTP 403 to automated fetch; PMC, the AAAS open-access mirror, does not). Relied-upon passages excerpted in [`sources/fei-et-al-2017-excerpts.md`](sources/fei-et-al-2017-excerpts.md), including the authors' own stated caveats. A full-PDF archive attempt failed (CDN link surfaced by the fetch tool did not resolve, HTTP 404); not re-attempted since the excerpts were pulled from the successful HTML fetch, not the failed PDF attempt.

### Oard & Klevberg 2022 — HIGH confidence

Oard, M.J., & Klevberg, P. (2022). Petrified Ideas of the Williston Basin, Part II: Fossil Wood. *Creation Research Society Quarterly*, 58(3), 204–219.

Retrieved 2026-08-16, full text read directly from `crsq.creationresearch.org/id/eprint/1282/1/Petrified%20Ideas%20of%20the%20Williston%20Basin%E2%80%94Part%20II:%20Fossil%20Wood.pdf`. The field-evidence claim used (no soil profile beneath petrified stumps at Fort Union Group/Theodore Roosevelt National Park, contra Biek & Gonzalez 2001's paleosol interpretation) is a direct quote, not a paraphrase — see `dev-notes/20260816-boundary-search-literature.md` for the exact passages. Not archived in this repo (copyright); re-fetch from the URL above to re-verify.

### Doyle 2017 — HIGH confidence on text, MEDIUM on relevance

Doyle, S. (2017). Do 'laterite' soils take a million years to form? *Journal of Creation*, 31(3), 5–7.

Retrieved 2026-08-16, full text read directly from `dl0.creation.com/articles/p116/c11696/j31_3_5-7.pdf`. Confidence on the text itself is HIGH (primary source, fully read); confidence on its *relevance* to this programme's paleosol-timescale question is MEDIUM, because the mechanism it discusses (lateral transport forming laterite deposits) is a different question from in-situ pedogenesis rate, and the paper's own conclusion is modest ("more work clearly needs to be done"). Not archived in this repo (copyright).

### Pearson et al. 2014 — MEDIUM confidence

Pearson, D.G., et al. (2014). Hydrous mantle transition zone indicated by ringwoodite included within diamond. *Nature*, 507, 221–224.

Paper identity confirmed correct (real, correctly characterized, matches the natural-diamond-inclusion claim), but the exact water-content figure (~1.4–1.5 wt%) was not independently pulled from primary text this session — carried forward from the original research-transcript audit. *Nature* is not open access; a primary-text pull, if wanted, would need to go through an institutional or paid route rather than automated fetch.

### USGS water inventory — HIGH confidence

United States Geological Survey, Water Science School. 1 ocean equivalent (OE) = 1.338 × 10⁹ km³ ocean + 2.34 × 10⁷ km³ groundwater.

Figures matched exactly against usgs.gov/water-science-school in the original research audit. Public domain (US government work) — no redistribution concern were archival wanted, though the figures are simple enough that citing the source page directly is sufficient.

### Vardiman (ICR) and Dillow (1981) — MEDIUM confidence

Canopy-ceiling figures (Vardiman's ~20 in / 51 cm precipitable-water habitability limit; Dillow's original ~40 ft / 12.2 m proposal and its corrected 1,144°C surface-temperature implication) are WebSearch-sourced characterizations, not primary-document pulls. Used in `water-ledger/README.md`'s vapor-canopy section and position paper §5.3. Worth a primary-source pull if this becomes load-bearing beyond its current supporting role (the canopy is already established as a non-source; these figures only bound how thoroughly that conclusion was checked).

### Biek & Gonzalez 2001 — LOW confidence (secondary)

Cited only as Oard & Klevberg (2022) cite it — the mainstream interpretation their field evidence disputes. Not independently retrieved or checked against its own primary text.

### Longmire 2025, *Global Flood Hydrotectonics* v2.5 — self-authored source, internal inconsistency noted

Source of the hydroplaning mechanism (Section 3), the Darcy-flow water-supply calculation (Section 3.3), and the energy-budget partitioning (Section 3.2), all directly accessible at [`jdlongmire/global-flood-hydrotectonic-model`](https://github.com/jdlongmire/global-flood-hydrotectonic-model). Not a third-party source requiring external verification, but its own internal lateral-velocity and detachment-depth figures were checked against each other and found inconsistent (documented in `02-theory/kinematics/README.md` and position paper §3.4) — recorded here so the inconsistency is traceable from the citation ledger, not only from the belt doc that found it.

## What remains open

- Pearson et al. 2014's exact figure has not been checked against *Nature*'s own primary text.
- Vardiman and Dillow figures rest on WebSearch characterization, not primary documents.
- Biek & Gonzalez 2001 has not been independently retrieved.
- Mainstream mantle-viscosity baseline figures (10²⁰–10²¹ Pa·s present, ~10¹⁹ Pa·s partial-melt floor) trace to the initial research transcript, not to a specific named paper checked directly by this programme.

None of these gaps currently affects a HIGH-confidence claim; they affect MEDIUM-confidence supporting figures. Closing them is future work, not a blocker on anything currently stated as settled.
