---
id: PCIE-065
title: "Design SKY130 TX serializer and driver schematics"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-003", "PCIE-006", "PCIE-045", "PCIE-046"]
spec_sections: ["4.2.1.1", "4.3.2.3", "4.3.3"]
---

# PCIE-065 — Design SKY130 TX serializer and driver schematics

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-065 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2.1.1 — Serialization and De-serialization of Data](../specification/4/2/1/1/summary.md): direct pp. 162–163; follow child sections and PDF tables.
- [4.3.2.3 — De-emphasis](../specification/4/3/2/3/summary.md): direct pp. 219–220; follow child sections and PDF tables.
- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Design xschem schematics for the serializer tree from the PCIE-004 interface to 2.5 Gb/s using qualified PCIE-045 cells, with retiming and race-free group updates.
- [ ] Design the TX driver schematic per PCIE-006 section 4.3.3 limits: swing, -3.5 dB de-emphasis, common mode, termination, electrical idle and receiver detection; add beacon only if PCIE-003 selects it.
- [ ] Simulate the complete TX schematic with behavioral PLL clocks and preliminary pad and package loads across corners with an explicit parasitic margin, documented so the layout phase can check it.
- [ ] Provide preliminary TX size and pin estimates to PCIE-060.

## pyuvm verification

- [ ] Drive the TX schematic with pyuvm-generated 8b/10b streams through PCIE-009 and reconstruct serial bits across 10-bit symbol and parallel-word boundaries.
- [ ] Swap one serializer input once and confirm the checker fails.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Run schematic transients across PVT with preliminary pad, package and channel loads; report eye, swing, de-emphasis, jitter, idle and detection behavior; verify timestep convergence.

## Acceptance criteria

- [ ] Schematic TX meets transmitter limits across corners, with the parasitic margin documented.
- [ ] Electrical idle, receiver detection and de-emphasis are demonstrated at schematic level.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
