---
id: PCIE-001
title: "Freeze endpoint profile and audit normative applicability"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P0
gate: baseline
depends_on: []
spec_sections: ["1", "1.3.2.2", "5.1.1", "6", "7", "4.3.1.1"]
---

# PCIE-001 — Freeze endpoint profile and audit normative applicability

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-001 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [1 — Introduction](../specification/1/summary.md): direct pp. 27–27; follow child sections and PDF tables.
- [1.3.2.2 — PCI Express Endpoint Rules](../specification/1/3/2/2/summary.md): direct pp. 32–32; follow child sections and PDF tables.
- [5.1.1 — Statement of Requirements](../specification/5/1/1/summary.md): direct pp. 232–232; follow child sections and PDF tables.
- [6 — System Architecture](../specification/6/summary.md): direct pp. 273–273; follow child sections and PDF tables.
- [7 — Software Initialization and Configuration](../specification/7/summary.md): direct pp. 337–337; follow child sections and PDF tables.
- [4.3.1.1 — Clocking Dependencies](../specification/4/3/1/1/summary.md): direct pp. 213–213; follow child sections and PDF tables.

Primary ownership: 15 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Produce docs/endpoint-profile.md: Gen1 x1, one PCI Express Endpoint function, Type 0 header, VC0/TC0, 128-byte advertised MPS initially, 64-bit non-prefetchable memory BAR, MSI, digital TL/DL/logical PHY with an on-chip SKY130 PMA.
- [ ] Distinguish first L0 bring-up from complete baseline; L0s and PCI-PM obligations cannot be removed merely by disabling ASPM in a prototype.
- [ ] Classify every section in specification/TRACEABILITY.csv as applicable, conditional or not applicable to the endpoint, with citations; detailed atomic requirements are written by each section's primary-owner ticket, not here.
- [ ] Record optional capability omissions and required response behavior; identify missing normative companion specifications (PCI configuration, PM, MSI, CEM/form factor) without inventing their contents.
- [ ] Freeze the digital datapath width and logical clock before any RTL ticket starts. Proposed default: 16 bits per cycle (two symbols, each with a K flag) at 125 MHz. One 8-bit symbol at 250 MHz is unlikely to close timing in SKY130 standard cells at the slow corner and may be kept only with synthesis evidence from a representative block. Changing width after RTL begins touches framing, CRC, DLLP and ordered-set logic in every layer.
- [ ] Freeze the reference-clock policy. Section 4.3.1.1 requires both link ends to transmit within 600 ppm of each other, and host spread-spectrum clocking exceeds what SKP compensation can absorb against a free-running local oscillator. Default: derive the on-chip PLL serializer clock, CDR reference and digital clocks from the host 100 MHz REFCLK; any separate-clock mode requires an explicit no-SSC host condition.
- [ ] Before declaring companion specifications missing, record what Rev1.1 sections 7.5 (PCI-compatible registers), 7.6 (PCI-PM capability) and 7.7 (MSI/MSI-X capability) already define; list the remaining gaps per register field and which of PCIE-027/029/030 each gap blocks.

## pyuvm verification

- [ ] Define legal and forbidden endpoint transactions for the pyuvm scoreboard.
- [ ] Review each advertised capability against its planned test and implementation owner.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Profile and mandatory/optional matrix have source citations and no unexplained exclusions.
- [ ] Every section has an applicability classification; candidate-level review is assigned to its primary-owner ticket and PCIE-042 confirms none remain unresolved.
- [ ] Datapath width, logical clock and reference-clock/SSC policy are recorded with rationale before any RTL ticket becomes ready.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
