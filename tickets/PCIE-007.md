---
id: PCIE-007
title: "Qualify the extracted TX and deliver the transmitter macro"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P0
gate: baseline
depends_on: ["PCIE-066", "PCIE-049", "PCIE-052", "PCIE-059"]
spec_sections: ["4.2.1.1", "4.3.2.3", "4.3.3"]
---

# PCIE-007 — Qualify the extracted TX and deliver the transmitter macro

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-007 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2.1.1 — Serialization and De-serialization of Data](../specification/4/2/1/1/summary.md): direct pp. 162–163; follow child sections and PDF tables.
- [4.3.2.3 — De-emphasis](../specification/4/3/2/3/summary.md): direct pp. 219–220; follow child sections and PDF tables.
- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Simulate the extracted TX with PCIE-049 clocks, PCIE-059 bias and PCIE-052 pad and package models across all corners; iterate where margins fail.
- [ ] Record pipeline latency and the deterministic reset and phase start for PCIE-004 and PCIE-040.
- [ ] Deliver a DRC/LVS-clean macro with GDS, LEF and timing abstract for PCIE-040.

## pyuvm verification

- [ ] Drive the extracted TX netlist with pyuvm-generated 8b/10b streams, compliance patterns, electrical-idle entry/exit and receiver-detect sequences through PCIE-009.
- [ ] Reconstruct serial bits from the output and detect omitted, duplicated or permuted bits across 10-bit symbol and parallel-word boundaries.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Run schematic and extracted-layout transients at all PVT corners with SKY130 models plus pad, package and channel loads from PCIE-052; report eye mask, swing, de-emphasis, jitter, common mode, idle and detection behavior; verify timestep convergence.

## Acceptance criteria

- [ ] Extracted TX macro meets modeled PCIE-006 transmitter limits at all corners, or the shortfall is quantified.
- [ ] DRC/LVS-clean macro with abstracts is delivered with reproducible commands.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
