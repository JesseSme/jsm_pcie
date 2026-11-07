---
id: PCIE-067
title: "Design SKY130 receiver, CDR and deserializer schematics"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-003", "PCIE-006", "PCIE-045", "PCIE-046"]
spec_sections: ["4.3.1.8", "4.3.1.9", "4.3.4"]
---

# PCIE-067 — Design SKY130 receiver, CDR and deserializer schematics

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-067 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.3.1.8 — Receiver Detection](../specification/4/3/1/8/summary.md): direct pp. 215–216; follow child sections and PDF tables.
- [4.3.1.9 — Electrical Idle](../specification/4/3/1/9/summary.md): direct pp. 216–217; follow child sections and PDF tables.
- [4.3.4 — Differential Receiver (RX) Input Specifications](../specification/4/3/4/summary.md): direct pp. 228–231; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Design xschem schematics for the RX path recommended by PCIE-046: termination and common mode, input amplifier or equalization if needed, samplers, CDR and deserializer to the PCIE-004 interface.
- [ ] Design electrical-idle (squelch) detection, lock detection and loss-of-lock reporting.
- [ ] Simulate the RX schematic with a behavioral PLL reference and preliminary pad and package loads with an explicit parasitic margin, documented so the layout phase can check it; measure lock time against the N_FTS budget and jitter tolerance.
- [ ] Provide preliminary RX size and pin estimates to PCIE-060.

## pyuvm verification

- [ ] Drive the RX schematic with pyuvm-generated streams including drift, polarity reversal and idle exit through PCIE-009; compare recovered bits with the independent stream.
- [ ] Inject excessive jitter once and confirm the checks fail.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Sweep input amplitude, common mode, jitter, frequency offset and idle-detection thresholds on the schematic across corners; verify timestep convergence.

## Acceptance criteria

- [ ] Schematic RX meets receiver limits and the lock-time budget across corners, with the parasitic margin documented.
- [ ] Behavioral parts of the CDR loop are labeled as assumptions.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
