---
id: PCIE-018
title: "Implement DLLP codec and CRC16"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-012", "PCIE-047"]
spec_sections: ["3.4"]
---

# PCIE-018 — Implement DLLP codec and CRC16

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-018 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [3.4 — Data Link Layer Packets (DLLPs)](../specification/3/4/summary.md): direct pp. 136–136; follow child sections and PDF tables.

Primary ownership: 2 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement ACK/NAK, InitFC1/2, UpdateFC and PM DLLP fields, reserved bits and CRC16.
- [ ] Route validated DLLPs to dedicated consumers; discard corrupted/unsupported packets per source.
- [ ] Arbitrate DLLP transmit requests with bounded latency requirements.

## pyuvm verification

- [ ] Use golden CRC vectors, random legal DLLPs and bit flips in every field including CRC.
- [ ] Test reserved encodings, truncated frames and concurrent PM/FC/ACK traffic.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Invalid CRC cannot change credits or acknowledge a TLP.
- [ ] All DLLP types in baseline encode/decode with exact byte order.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
