# Zenodo Submission Checklist — Global Hydrotectonic Flood Model Position Paper

**Published 2026-08-16.** DOI: [10.5281/zenodo.21972859](https://doi.org/10.5281/zenodo.21972859) (concept DOI 10.5281/zenodo.21972858). Record: https://zenodo.org/record/21972859. Submitted via the Zenodo REST API (deposition created, PDF uploaded, metadata set, published) using a token JD provided by email; the manual walkthrough below is kept as the record of what was actually done, field for field, not as still-pending instructions.

## Pre-flight

- [x] PDF rendered from `POSITION-PAPER.md` via pandoc/xelatex — `hydrotectonic-flood-model-position-paper-v0.1.pdf` (11 pages, this folder)
- [x] Figures verified rendering correctly in the PDF (checked pages 3 and 5 directly)
- [x] Math notation (Terzaghi effective-stress equation, Q_required/Q_available) verified rendering correctly, not as raw LaTeX
- [x] Citations checked against `research/citation-validation.md` — HIGH-confidence claims traced to primary text; MEDIUM-confidence figures disclosed as such in the paper itself, not smoothed over
- [ ] Final proofread of the PDF pass (JD)

## Upload

**URL:** https://zenodo.org/deposit/new (ORCID login available)

1. Upload Type: Publication → Preprint, Open Access
2. Upload `hydrotectonic-flood-model-position-paper-v0.1.pdf`
3. Copy fields from `ZENODO_METADATA.txt` in this folder — title, authors/ORCID, description, version (0.1), date (2026-08-16), license (CC BY 4.0), keywords, subjects, related identifiers
4. **This is a new deposit, not a new version of an existing concept DOI** — this paper carries its own hard core (Genesis-historical commitments, DFM) that the related hydroplaning-mechanism paper (10.5281/zenodo.17684983) never did. Confirmed with JD 2026-08-16.
5. Related identifiers: link both directions — this deposit references 10.5281/zenodo.17684983 (hydroplaning mechanism source) and the GitHub repo; consider also linking back from that record's own metadata if Zenodo's edit flow allows it easily.

## Actual DOI

```
10.5281/zenodo.21972859
```

Citable as:
```
Longmire, J.D., 2026. The Global Hydrotectonic Flood Model: A Layered Mechanism for
Rapid Continental Reorganization. Zenodo. https://doi.org/10.5281/zenodo.21972859
```

## After publication

- [x] Update `00-program-methods/POSITION-PAPER.md`'s own header with the real DOI
- [x] Update `README.md` to link the published DOI
- [x] Save the DOI/submission confirmation somewhere durable (this checklist)
- [ ] Update `research/citation-validation.md`'s self-reference, if it needs one for this paper's own DOI

## Known, disclosed as-is (not blockers, but visible once this is permanent)

- Section 3.4's internal velocity/detachment-depth inconsistency is unresolved and stated plainly in the paper — a deliberate choice per JD, not an oversight to fix before publishing. A future v0.2 (new Zenodo version under the same concept DOI, once this exists) can close it later.
- Two open questions (vertical-subduction magnitude, stratigraphic timing) are the paper's own stated frontier, not resolved by this draft.

## Common issues to avoid (carried from the sibling paper's own checklist)

- Uploading without testing PDF rendering — done, see Pre-flight above
- Using a restrictive license — CC BY 4.0 matches the sibling paper, keeps later journal submission open
- Not saving the DOI/confirmation after submission
- Skipping the final proofread pass
