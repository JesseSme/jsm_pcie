---
id: PCIE-047
title: "Build data-link partner models: DLLP, CRC, ACK/NAK replay and flow control"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-005"]
spec_sections: ["3.1", "3.3", "3.4", "3.5", "2.6"]
---

# PCIE-047 — Build data-link partner models: DLLP, CRC, ACK/NAK replay and flow control

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-047 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [3.1 — Data Link Layer Overview](../specification/3/1/summary.md): direct pp. 127–129; follow child sections and PDF tables.
- [3.3 — Flow Control Initialization Protocol](../specification/3/3/summary.md): direct pp. 132–132; follow child sections and PDF tables.
- [3.4 — Data Link Layer Packets (DLLPs)](../specification/3/4/summary.md): direct pp. 136–136; follow child sections and PDF tables.
- [3.5 — Data Integrity](../specification/3/5/summary.md): direct pp. 141–141; follow child sections and PDF tables.
- [2.6 — Ordering and Receive Buffer Flow Control](../specification/2/6/summary.md): direct pp. 106–107; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement independent Python DLLP encode/decode for ACK/NAK, InitFC1/2, UpdateFC and PM DLLPs with CRC16 from section 3.4.
- [ ] Implement independent LCRC and 12-bit sequence-number references from section 3.5.
- [ ] Implement a root-port data-link partner: DL state, InitFC exchange, credit accounting, ACK/NAK generation with configurable delay, drop and corruption, and replay of its own TLPs.
- [ ] Attach the partner to the PCIE-005 symbol agent so PHY and data-link tickets share one stack.

## pyuvm verification

- [ ] Self-check CRC16 and LCRC against cited and hand-computed vectors; corrupt each field and confirm detection.
- [ ] Run partner-to-partner loopback in Python with injected loss, NAK and sequence wrap; check replay delivers each TLP exactly once.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Reference vectors carry source citations and expected bytes.
- [ ] Fault injection is controllable per packet and reproducible by seed.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
