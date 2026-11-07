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
depends_on: ["PCIE-001", "PCIE-003"]
spec_sections: ["1.5.4.4", "4.1", "4.2"]
---

# PCIE-004 — Create PHY boundary and cycle-accurate simulation contract

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-004 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [1.5.4.4 — Inter-Layer Interfaces](../specification/1/5/4/4/summary.md): direct pp. 40–40; follow child sections and PDF tables.
- [4.1 — Introduction](../specification/4/1/summary.md): direct pp. 161–161; follow child sections and PDF tables.
- [4.2 — Logical Sub-block](../specification/4/2/summary.md): direct pp. 161–162; follow child sections and PDF tables.

Primary ownership: 13 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Define the digital symbol interface at the width and clock frozen in PCIE-001 (proposed: two symbols plus K flags per 125 MHz cycle); do not label it PIPE compliant without implementing a specific PIPE revision.
- [ ] Own the detailed digital-to-PMA interface contract within the PCIE-003 architecture: signal list, widths, bit order, clocks, control acknowledgments and timing diagrams.
- [ ] Separate logical PHY from PMA serialization/CDR through explicit TX/RX symbols, status, electrical-idle, receiver-detect, polarity, power state and lock controls.
- [ ] Define reset behavior, clock domains, backpressure constraints and latency; the physical stream cannot pause when a digital consumer is not ready.
- [ ] Provide a behavioral PMA model for digital simulation and the mixed-signal interface to the SKY130 PMA macros; scrambling and 8b/10b happen exactly once, in the digital core.
- [ ] Define the encoded parallel interface to the on-chip serializer and from the deserializer (proposed 20 bits per 125 MHz cycle), with explicit bit order across 10-bit symbol boundaries.
- [ ] Specify TX parallel-clock/data phase alignment to the PLL, the recovered RX clock domain, PMA control acknowledgments and initialization handshakes.
- [ ] Specify alignment of STP, SDP, END, EDB, COM and ordered sets within the multi-symbol digital word, including packets that start or end in any symbol position.

## pyuvm verification

- [ ] Use pyuvm driver/monitor agents for each direction; exercise lock loss, asynchronous reset, invalid symbols and idle transitions.
- [ ] Assert deterministic control handshakes and detect data loss under FIFO pressure.
- [ ] Exercise packets and ordered sets starting and ending in every symbol position of the digital word.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Interface specification includes timing diagrams and all control acknowledgments.
- [ ] Behavioral PMA model allows full digital verification before analog macros exist.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
