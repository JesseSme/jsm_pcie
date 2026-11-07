---
id: PCIE-021
title: "Implement transmit retry buffer and replay controller"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-018", "PCIE-019"]
spec_sections: ["3.5.2"]
---

# PCIE-021 — Implement transmit retry buffer and replay controller

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-021 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [3.5.2 — LCRC, Sequence Number, and Retry Management (TLP Transmitter)](../specification/3/5/2/summary.md): direct pp. 141–142; follow child sections and PDF tables.

Primary ownership: 2 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Assign TX sequence numbers and LCRC; retain each sent TLP until valid acknowledgment.
- [ ] Implement replay timer/count, ACK/NAK processing, retry-buffer admission and recovery escalation.
- [ ] Handle sequence wrap, stale/invalid ACKs, link loss and concurrent enqueue/replay without double-credit charging.

## pyuvm verification

- [ ] Drop ACKs, inject NAKs and invalid ACK ranges, force timer expiry and wrap sequence space.
- [ ] Scoreboard replay byte identity, retirement order, bounded buffer use and eventual recovery.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Replay never loses an unacknowledged packet or retires one prematurely.
- [ ] Source retry limits/timers are checked at boundaries and lead to correct recovery.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
