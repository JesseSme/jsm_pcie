---
id: PCIE-008
title: "Design external RX clock recovery, deserialization and electrical controls"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P0
gate: baseline
depends_on: ["PCIE-003", "PCIE-006", "PCIE-046"]
spec_sections: ["4.3.1.8", "4.3.1.9", "4.3.4"]
---

# PCIE-008 — Design external RX clock recovery, deserialization and electrical controls

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-008 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [4.3.1.8 — Receiver Detection](../specification/4/3/1/8/summary.md): direct pp. 215–216; follow child sections and PDF tables.
- [4.3.1.9 — Electrical Idle](../specification/4/3/1/9/summary.md): direct pp. 216–217; follow child sections and PDF tables.
- [4.3.4 — Differential Receiver (RX) Input Specifications](../specification/4/3/4/summary.md): direct pp. 228–231; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Specify RX termination, differential input compatibility, CDR or justified oversampling, comma alignment and receive clock generation at full data rate.
- [ ] Design receiver-detection/electrical-idle control feedback and timeout behavior; include disconnected, powered-down and hot reset cases.
- [ ] Budget frequency offset and jitter tolerance; define lock loss and re-acquisition behavior.
- [ ] Document what is implementable with FPGA digital resources and what requires analog-capable pins or external parts.
- [ ] Treat the documented 1.2 Gb/s IDES8/10 rate as insufficient for direct 2.5 GT/s reception; evaluate a supported parallel/external recovery path using the same FPGA I/O specifications.
- [ ] Design the approved external receive conditioning, clock/data recovery and deserializer path, returning a supported parallel interface and recovered clock to the FPGA.
- [ ] Build on the PCIE-046 feasibility recommendation; derive the CDR reference from the PCIE-003 clock architecture and keep the supportable N_FTS and lock-time budget current for PCIE-017/031.

## pyuvm verification

- [ ] Drive recovered clock drift, polarity reversal, loss of signal, idle exit and false lock through pyuvm PHY model.
- [ ] Assert no packet delivery before symbol alignment and lock; verify fault-driven recovery.
- [ ] Verify deserializer bit ordering, comma/symbol alignment and reacquisition under recovered-clock phase changes; do not assume RX phase equals local TX phase.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Sweep input amplitude/common mode, jitter, phase, termination and idle detection thresholds; simulate detection loads and bias startup. Behavioral CDR results must be labeled assumptions until hardware characterization.

## Acceptance criteria

- [ ] Full-duplex feasibility decision includes RX and control feedback, not TX eye alone.
- [ ] Hardware-dependent work remains blocked if supported input sampling/recovery cannot be established.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
