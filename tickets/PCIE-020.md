---
id: PCIE-020
title: "Implement LCRC, receive sequence checks and ACK/NAK policy"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-018", "PCIE-019"]
spec_sections: ["3.5.3", "3.5.1"]
---

# PCIE-020 — Implement LCRC, receive sequence checks and ACK/NAK policy

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-020 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [3.5.3 — LCRC and Sequence Number (TLP Receiver)](../specification/3/5/3/summary.md): direct pp. 153–153; follow child sections and PDF tables.
- [3.5.1 — Introduction](../specification/3/5/1/summary.md): direct pp. 141–141; follow child sections and PDF tables.

Primary ownership: 4 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement receive TLP LCRC and 12-bit sequence handling with modulo comparison and duplicate rejection.
- [ ] Generate ACK/NAK with specified latency, sequence values and timer rules.
- [ ] Handle EDB/nullified packets and error propagation without committing corrupted payloads.

## pyuvm verification

- [ ] Inject bad LCRC, sequence gaps, duplicates, wraparound, truncation, EDB and legal retransmissions.
- [ ] Check packets reach TL once only; measure ACK/NAK timer boundaries under heavy traffic.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] No corrupt or duplicate TLP causes application-visible side effects.
- [ ] ACK/NAK content and deadlines match source rules.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
