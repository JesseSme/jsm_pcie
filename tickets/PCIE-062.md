---
id: PCIE-062
title: "Lay out and extract the SKY130 PHY building blocks"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-061"]
spec_sections: ["4.2.1.1", "4.3.2.2", "4.3.3"]
---

# PCIE-062 — Lay out and extract the SKY130 PHY building blocks

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-062 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2.1.1 — Serialization and De-serialization of Data](../specification/4/2/1/1/summary.md): direct pp. 162–163; follow child sections and PDF tables.
- [4.3.2.2 — Jitter and BER](../specification/4/3/2/2/summary.md): direct pp. 219–219; follow child sections and PDF tables.
- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Lay out the PCIE-061 SKY130 PHY building blocks schematics in Magic with symmetric differential routing, guard rings and well ties; pass DRC (Magic and KLayout) and LVS (netgen).
- [ ] Extract parasitic netlists with documented extraction settings and the known limits of the open extraction flow.
- [ ] Re-run the typical-corner PCIE-061 testbenches on extracted netlists as a smoke check and report the gap to schematic results.
- [ ] Record cell sizes and pin locations for the PCIE-060 loopback top.

## pyuvm verification

- [ ] Re-run the PCIE-061 bit-sequence checks on extracted netlists at the typical corner.
- [ ] Confirm an intentionally broken layout connection is caught by LVS.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Simulate extracted netlists at the typical corner with the schematic-phase testbenches and report delay, swing, jitter and power changes versus schematic; verify timestep convergence.

## Acceptance criteria

- [ ] Layout is DRC/LVS clean with extracted netlists and extraction settings recorded.
- [ ] Typical-corner extracted results are compared with schematic results and the gap is explained.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
