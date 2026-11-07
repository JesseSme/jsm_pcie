---
id: PCIE-063
title: "Design PLL and REFCLK receiver schematics"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-003", "PCIE-006", "PCIE-045"]
spec_sections: ["4.3.1.1", "4.3.3", "4.3.4"]
---

# PCIE-063 — Design PLL and REFCLK receiver schematics

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-063 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.3.1.1 — Clocking Dependencies](../specification/4/3/1/1/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.
- [4.3.4 — Differential Receiver (RX) Input Specifications](../specification/4/3/4/summary.md): direct pp. 228–231; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Design xschem schematics for the REFCLK input receiver, VCO, dividers, phase-frequency detector, charge pump and loop filter using qualified PCIE-045 cells, targeting the PCIE-003 clock plan (2.5 GHz full-rate or 1.25 GHz half-rate).
- [ ] Obtain REFCLK electrical requirements (levels, jitter) from the matching PCI Express CEM specification, which the Base specification does not define, or record the gap as a blocker.
- [ ] Verify loop stability, lock time and SSC tracking with behavioral loop models plus transistor-level blocks with an explicit parasitic margin, documented so the layout phase can check it; estimate jitter with a documented method.
- [ ] Provide preliminary PLL size and pin estimates to PCIE-060.

## pyuvm verification

- [ ] Drive the PLL behavioral model with REFCLK including SSC and frequency offset through pyuvm; assert no TX traffic before lock and correct lock-loss handling.
- [ ] Deliberately exceed the jitter or lock budget and confirm the checks fail.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Simulate VCO, dividers, phase-frequency detector and charge pump at transistor level across corners, and the closed loop with behavioral plus transistor-level blocks; verify timestep convergence.

## Acceptance criteria

- [ ] Schematic PLL meets the clock, jitter and lock budget across corners, with the parasitic margin documented.
- [ ] REFCLK requirements are sourced from the CEM specification or recorded as a blocker.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
