---
id: PCIE-049
title: "Qualify the extracted PLL and deliver the clock macro"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-064", "PCIE-059"]
spec_sections: ["4.3.1.1", "4.3.3", "4.3.4"]
---

# PCIE-049 — Qualify the extracted PLL and deliver the clock macro

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-049 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.3.1.1 — Clocking Dependencies](../specification/4/3/1/1/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.
- [4.3.4 — Differential Receiver (RX) Input Specifications](../specification/4/3/4/summary.md): direct pp. 228–231; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Simulate the extracted PLL and REFCLK receiver with the PCIE-059 bias circuits across all corners; iterate where margins fail.
- [ ] Confirm output jitter against section 4.3.3 transmitter jitter limits, SSC tracking and lock time; define lock detect and reset behavior.
- [ ] Design and verify clock distribution and duty-cycle control to the serializer and deserializer.
- [ ] Deliver a DRC/LVS-clean macro with GDS, LEF and timing abstracts for PCIE-040.

## pyuvm verification

- [ ] Drive the PLL behavioral model with REFCLK including SSC and frequency offset through pyuvm; assert no TX traffic before lock and correct lock-loss handling.
- [ ] Deliberately exceed the jitter or lock budget and confirm the checks fail.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Simulate VCO, dividers, phase-frequency detector and charge pump at transistor level across corners; estimate jitter with a documented method; verify loop stability and lock using behavioral plus extracted blocks; verify timestep convergence.

## Acceptance criteria

- [ ] PLL macro meets the clock and jitter budget at all corners with modeled results, or the shortfall is quantified.
- [ ] Lock, reset and lock-loss behavior is defined and verified.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
