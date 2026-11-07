---
id: PCIE-052
title: "Design high-speed I/O pads, ESD protection and package model"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-003", "PCIE-006", "PCIE-050"]
spec_sections: ["4.3.1.8", "4.3.3", "4.3.4"]
---

# PCIE-052 — Design high-speed I/O pads, ESD protection and package model

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-052 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.3.1.8 — Receiver Detection](../specification/4/3/1/8/summary.md): direct pp. 215–216; follow child sections and PDF tables.
- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.
- [4.3.4 — Differential Receiver (RX) Input Specifications](../specification/4/3/4/summary.md): direct pp. 228–231; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Select or design pads for the PCIe TX/RX pairs and REFCLK with ESD protection whose capacitance and series resistance suit 2.5 Gb/s; standard SKY130 GPIO pads are not assumed adequate; the REFCLK input receiver circuit itself belongs to PCIE-049.
- [ ] Model bond-wire or package, pad and ESD parasitics for PCIE-007/008/043 simulations, with provenance.
- [ ] Check ESD structures against PDK rules and document protection as modeled, not certified.
- [ ] Deliver pad cells with DRC/LVS and abstracts for PCIE-057.

## pyuvm verification

- [ ] Include pad and package model identifiers in PCIE-009 manifests so electrical results trace to the pad configuration.
- [ ] Confirm a deliberately degraded pad model makes PCIE-043 limit checks fail.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Simulate pad, ESD and package loading in transient with SKY130 models and extracted parasitics at corners; report the effect on the TX eye and the RX input.

## Acceptance criteria

- [ ] Pad and package models used by PCIE-007/008/043 have documented provenance.
- [ ] Pads pass DRC/LVS with abstracts delivered.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
