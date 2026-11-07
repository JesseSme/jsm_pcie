---
id: PCIE-008
title: "Qualify the extracted RX and deliver the receiver macro"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P0
gate: baseline
depends_on: ["PCIE-068", "PCIE-049", "PCIE-052", "PCIE-059"]
spec_sections: ["4.3.1.8", "4.3.1.9", "4.3.4"]
---

# PCIE-008 — Qualify the extracted RX and deliver the receiver macro

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-008 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.3.1.8 — Receiver Detection](../specification/4/3/1/8/summary.md): direct pp. 215–216; follow child sections and PDF tables.
- [4.3.1.9 — Electrical Idle](../specification/4/3/1/9/summary.md): direct pp. 216–217; follow child sections and PDF tables.
- [4.3.4 — Differential Receiver (RX) Input Specifications](../specification/4/3/4/summary.md): direct pp. 228–231; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Simulate the extracted RX with PCIE-049 clocks, PCIE-059 bias and PCIE-052 pad and package models across all corners; iterate where margins fail.
- [ ] Confirm section 4.3.4 receiver limits and the N_FTS/lock-time budget, and keep that budget current for PCIE-017/031 and PCIE-040.
- [ ] Deliver a DRC/LVS-clean macro with abstracts for PCIE-040.

## pyuvm verification

- [ ] Drive recovered clock drift, polarity reversal, loss of signal, idle exit and false lock through the pyuvm PHY model.
- [ ] Assert no packet delivery before symbol alignment and lock; verify fault-driven recovery.
- [ ] Verify deserializer bit ordering, comma/symbol alignment and reacquisition under recovered-clock phase changes; do not assume RX phase equals local TX phase.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Sweep input amplitude, common mode, jitter, frequency offset, termination and idle-detection thresholds on schematic and extracted netlists at all corners; simulate detection loads and bias startup; verify timestep convergence.

## Acceptance criteria

- [ ] Extracted RX macro meets modeled receiver limits and the lock-time budget at all corners, or the shortfall is quantified.
- [ ] Behavioral CDR results are labeled assumptions until extracted-layout evidence exists.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
