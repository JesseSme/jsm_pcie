---
id: PCIE-007
title: "Design on-chip SKY130 TX serializer and PCIe transmitter"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P0
gate: baseline
depends_on: ["PCIE-003", "PCIE-006", "PCIE-045", "PCIE-046", "PCIE-049", "PCIE-052", "PCIE-059"]
spec_sections: ["4.2.1.1", "4.3.2.3", "4.3.3"]
---

# PCIE-007 — Design on-chip SKY130 TX serializer and PCIe transmitter

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-007 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2.1.1 — Serialization and De-serialization of Data](../specification/4/2/1/1/summary.md): direct pp. 162–163; follow child sections and PDF tables.
- [4.3.2.3 — De-emphasis](../specification/4/3/2/3/summary.md): direct pp. 219–220; follow child sections and PDF tables.
- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Integrate qualified PCIE-045 cells into the complete TX path: parallel-to-serial tree from the PCIE-004 interface to 2.5 Gb/s, retiming, and clocks from the PCIE-049 PLL.
- [ ] Design the TX driver per PCIE-006 section 4.3.3 limits: differential swing, -3.5 dB de-emphasis, common mode, termination (calibrated if needed), electrical idle and receiver detection.
- [ ] Prevent serializer update races across parallel-word and group boundaries; record pipeline latency and the deterministic reset and phase start.
- [ ] Lay out in Magic, extract parasitics and pass DRC/LVS; deliver a macro (GDS, LEF and timing abstract) for PCIE-040 integration.
- [ ] If PCIE-003 selects beacon for wake from L2, generate it in the transmitter; otherwise record its absence.
- [ ] Deliver preliminary TX macro abstracts (size, pin placement, supplies) early to the PCIE-060 loopback top and keep them current.

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
