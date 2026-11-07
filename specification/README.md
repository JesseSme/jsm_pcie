# PCI Express Revision 1.1 specification decomposition

Start with [chapter index](INDEX.md), [endpoint profile](../docs/endpoint-profile.md), and [ticket index](../tickets/INDEX.md).

The supplied files are **PCI Express Base Specification Revision 1.1, March 28, 2005**, rather than a later-generation specification. Gen1 signaling is the project target. The PDF contains 508 pages, and its printed page numbering agrees with PDF page numbering. The provided TXT is the verbatim extraction authority; the PDF is the visual authority for diagrams, tables and layout. Both original files remain unchanged. `manifest.json` records their SHA-256 hashes.

Section 1.1 lives in `1/1/`; section 4.2.6.3.1.2 lives in `4/2/6/3/1/2/`. Appendices use `A/` through `D/`. Non-numbered material is retained in `front-matter/` and `back-matter/`.

Every section has three separate files:

- `verbatim.md`: exact direct source text in a fenced block, including layout, line numbers, headers and form feeds. Children are stored separately; reading a parent's file alone does not read its descendants. A chapter may have only a heading before its first child.
- `summary.md`: topic, implementation relevance, a labelled extractive synopsis, verification owner and child navigation. Summaries are implementation guidance, not normative replacements. The source synopsis can contain table/diagram labels where those dominate the direct text.
- `requirements.md`: complete source paragraphs containing modal keywords, each with a stable section-local ID, TXT line, PDF page, modality and explicit unreviewed status. These candidates preserve surrounding conditions rather than pretending every occurrence of “may” is mandatory. `requirements.json` is the equivalent machine-readable dataset.

`TRACEABILITY.csv` assigns every section and every candidate to a primary ticket, with related tickets. Parent direct page ranges exclude child text. For the entire chapter, follow its child links. The initial applicability status is deliberately unreviewed: table rows, drawings, implicit conditions, implementation notes and referenced companion specifications need human/agent review. PCIE-001 and each owning implementation ticket must turn candidates into atomic reviewed requirements with implementation and test evidence. PCIE-042 forbids closing the baseline with unresolved applicable rules.

## Local-only specification text

The PCI-SIG specification is copyrighted and this repository is public. The source PDF/TXT and every file derived from their text (`verbatim.md`, `summary.md`, `requirements.md`, `requirements.json`) are git-ignored, as is `graphify-out/`. Only metadata is tracked: this README, `INDEX.md` (titles and pages), `manifest.json` (section boundaries and hashes) and `TRACEABILITY.csv` (ticket mapping and review dispositions). Never commit spec text, quoted requirement paragraphs or the knowledge graph.

In a fresh clone, place your licensed copies of `54321492-PCI-Express-Base-11.pdf` and `.txt` in the repository root; `manifest.json` records the SHA-256 hashes they must match. Then rebuild the local section files:

```sh
python3 tools/deconstruct_spec.py                    # verbatim text and requirement candidates
python3 tools/build_pcie_plan.py --summaries-only    # summaries; never touches tickets
python3 tools/deconstruct_spec.py --check
```

`python3 tools/tickets.py check` validates section references against `manifest.json`, so it passes without the local text. Ticket links into `specification/` resolve only after this local rebuild.

## Initial extraction

The initial extraction was local and deterministic:

```sh
python3 tools/deconstruct_spec.py
python3 tools/build_pcie_plan.py
python3 tools/deconstruct_spec.py --check
python3 tools/tickets.py check
```

The check reconstructs the complete TXT character-for-character from the fenced blocks, checks source hashes, hierarchy and table-of-contents page anchors. It does not prove that text extraction recovered PDF-only graphics. The supplied TXT differs from a fresh `pdftotext -layout` extraction, so regeneration deliberately uses the supplied TXT and never silently replaces it. The initial-plan builder refuses to overwrite claimed tickets; after work starts, maintain ticket states, summaries and dispositions directly rather than regenerating them.
