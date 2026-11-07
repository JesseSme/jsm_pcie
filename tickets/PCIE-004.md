---
id: PCIE-004
title: "Create PHY boundary and cycle-accurate simulation contract"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P0
gate: baseline
depends_on: ["PCIE-001"]
spec_sections: ["1.5.4.4", "4.1", "4.2"]
---

# PCIE-004 — Create PHY boundary and cycle-accurate simulation contract

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-004 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [1.5.4.4 — Inter-Layer Interfaces](../specification/1/5/4/4/summary.md): direct pp. 40–40; follow child sections and PDF tables.
- [4.1 — Introduction](../specification/4/1/summary.md): direct pp. 161–161; follow child sections and PDF tables.
- [4.2 — Logical Sub-block](../specification/4/2/summary.md): direct pp. 161–162; follow child sections and PDF tables.

Primary ownership: 13 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Define the fabric-side symbol interface at the width and clock frozen in PCIE-001 (proposed: two symbols plus K flags per 125 MHz cycle); do not label it PIPE compliant without implementing a specific PIPE revision.
- [ ] Separate logical PHY from PMA serialization/CDR through explicit TX/RX symbols, status, electrical-idle, receiver-detect, polarity, power state and lock controls.
- [ ] Define reset behavior, clock domains, backpressure constraints and latency; the physical stream cannot pause when fabric ready is low.
- [ ] Provide adapters for behavioral simulation and later board-specific hardware; avoid double 8b/10b encoding or scrambling in vendor PCS.
- [ ] Keep scrambling and 8b/10b inside the FPGA and define an explicit continuous encoded-bit gearbox between the symbol interface and external parallel pins; four-bit transfers cross ten-bit symbol boundaries.
- [ ] Specify external TX clock/data phase alignment, recovered RX clock domain, electrical controls and initialization handshakes without assuming a specific serializer chip.
- [ ] Specify alignment of STP, SDP, END, EDB, COM and ordered sets within the multi-symbol fabric word, including packets that start or end in any symbol position.

## pyuvm verification

- [ ] Use pyuvm driver/monitor agents for each direction; exercise lock loss, asynchronous reset, invalid symbols and idle transitions.
- [ ] Assert deterministic control handshakes and detect data loss under FIFO pressure.
- [ ] Exercise packets and ordered sets starting and ending in every symbol position of the fabric word.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Interface specification includes timing diagrams and all control acknowledgments.
- [ ] Simulation adapter can be implemented without deciding a board.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
