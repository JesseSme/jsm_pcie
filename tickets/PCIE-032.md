---
id: PCIE-032
title: "Implement baseline error reporting and poisoned-data policy"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-020", "PCIE-021", "PCIE-023", "PCIE-025", "PCIE-028"]
spec_sections: ["2.7.2", "6.2"]
---

# PCIE-032 — Implement baseline error reporting and poisoned-data policy

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-032 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [2.7.2 — Error Forwarding](../specification/2/7/2/summary.md): direct pp. 121–121; follow child sections and PDF tables.
- [6.2 — Error Signaling and Logging](../specification/6/2/summary.md): direct pp. 278–278; follow child sections and PDF tables.

Primary ownership: 37 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Map correctable, non-fatal and fatal events to baseline status, Device Control gates and error messages.
- [ ] Implement poisoned-data propagation/discard policy and advisory non-fatal distinctions.
- [ ] Arbitrate simultaneous errors and avoid recursive error storms; preserve first useful diagnostic context.
- [ ] Audit endpoint-only applicability; root error interrupts and bridge mapping are excluded.

## pyuvm verification

- [ ] Inject bad LCRC, malformed/unsupported requests, unexpected completions, poison and completion/replay timeout.
- [ ] Sweep reporting enable bits and concurrent events; check status W1C and message suppression.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Each injected error has a deterministic source-cited response and no silent data corruption.
- [ ] Baseline behavior works without advertising optional AER.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
