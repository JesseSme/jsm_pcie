---
id: PCIE-044
title: "Validate silicon bring-up and host interoperability"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: conditional
depends_on: ["PCIE-058"]
spec_sections: ["1.4", "4.3", "6.6", "7"]
---

# PCIE-044 — Validate silicon bring-up and host interoperability

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-044 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [1.4 — PCI Express Fabric Topology Configuration](../specification/1/4/summary.md): direct pp. 35–36; follow child sections and PDF tables.
- [4.3 — Electrical Sub-block](../specification/4/3/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [6.6 — PCI Express Reset - Rules](../specification/6/6/summary.md): direct pp. 316–319; follow child sections and PDF tables.
- [7 — Software Initialization and Configuration](../specification/7/summary.md): direct pp. 337–337; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Design or select a test board carrying the packaged chip with a PCIe edge connector or adapter, REFCLK, PERST#, supplies and test access, after reviewing the companion form-factor specification.
- [ ] Bring up silicon through the test interface and PHY loopback before host attachment; then verify host enumeration, BAR/MMIO, MSI, power transitions and reset/recovery.
- [ ] Measure TX eye, receiver tolerance, lock time and power against PCIE-043 predictions and update models with provenance.
- [ ] Record host, platform and instrument limits; certified compliance is not implied.

## pyuvm verification

- [ ] Replay host-observed transactions as pyuvm regressions and add any interoperability corner cases.
- [ ] Compare real read/write/interrupt outcomes with simulation reference expectations.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Compare measured board waveforms with final ngspice predictions and update model parameters with provenance; rerun margins after fitting.

## Acceptance criteria

- [ ] Repeatable bring-up and host demo commands are documented, or the ticket closes with a reviewed not-performed disposition if no silicon is fabricated.
- [ ] Outstanding compliance and electrical gaps are explicit; project completion is not confused with certified compliance.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
