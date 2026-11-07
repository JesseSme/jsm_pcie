---
id: PCIE-023
title: "Implement receive classification and unsupported/malformed handling"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-022", "PCIE-020"]
spec_sections: ["2.3.1", "6.5.7"]
---

# PCIE-023 — Implement receive classification and unsupported/malformed handling

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-023 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [2.3.1 — Request Handling Rules](../specification/2/3/1/summary.md): direct pp. 81–87; follow child sections and PDF tables.
- [6.5.7 — PCI Express Endpoints](../specification/6/5/7/summary.md): direct pp. 316–316; follow child sections and PDF tables.

Primary ownership: 2 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Classify posted, non-posted and completion TLPs; validate destination and endpoint capability before dispatch.
- [ ] Implement UR/CA/error-report behavior for unsupported requests and malformed packets with correct posted/non-posted distinctions.
- [ ] Reject locked requests as required for PCI Express Endpoint and avoid producing forbidden I/O or lock requests.

## pyuvm verification

- [ ] Send unsupported memory/config/message types, MRdLk, malformed headers and out-of-range BAR traffic.
- [ ] Check exact completion/error behavior and that invalid posted writes never mutate application state.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Every rejected request has source-backed disposition.
- [ ] No unsupported request path blocks valid traffic indefinitely.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
