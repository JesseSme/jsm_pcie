---
id: PCIE-059
title: "Design bias, reference and termination-calibration circuits"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-003", "PCIE-004", "PCIE-006", "PCIE-050"]
spec_sections: ["4.3.3", "4.3.4"]
---

# PCIE-059 — Design bias, reference and termination-calibration circuits

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-059 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.
- [4.3.4 — Differential Receiver (RX) Input Specifications](../specification/4/3/4/summary.md): direct pp. 228–231; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Design a SKY130 bias reference (bandgap or constant-transconductance bias) and the current distribution feeding current-mode logic, the PLL charge pump, TX driver and RX front end.
- [ ] Design termination calibration if PCIE-007/008 need it, using an on-chip or off-chip precision reference recorded in PCIE-003.
- [ ] Define power-up start-up, enable and settling behavior and report it to the PMA control contract in PCIE-004.
- [ ] Lay out, extract, pass DRC/LVS and deliver a macro with abstracts for PCIE-007/008/049 and PCIE-040.

## pyuvm verification

- [ ] Model bias-ready and calibration-done handshakes in the behavioral PMA model and assert that no PMA block is enabled before them.
- [ ] Deliberately delay start-up or skew calibration and confirm the checks fail.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Simulate bias and calibration circuits on schematic and extracted netlists across corners, temperature, supply ramps and mismatch; include start-up transients and supply sensitivity; verify timestep convergence.

## Acceptance criteria

- [ ] Bias and calibration outputs meet their budgets at all corners on extracted layout, or the shortfall is quantified.
- [ ] Start-up never latches into a zero-current state across corners and supply ramps.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
