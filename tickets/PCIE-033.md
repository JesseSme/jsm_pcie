---
id: PCIE-033
title: "Assess optional ECRC generation and checking"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: conditional
depends_on: ["PCIE-022", "PCIE-032"]
spec_sections: ["2.2.3", "2.7.1"]
---

# PCIE-033 — Assess optional ECRC generation and checking

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-033 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [2.2.3 — TLP Digest Rules](../specification/2/2/3/summary.md): direct pp. 52–52; follow child sections and PDF tables.
- [2.7.1 — ECRC Rules](../specification/2/7/1/summary.md): direct pp. 117–121; follow child sections and PDF tables.

Primary ownership: 1 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Decide ECRC support separately from mandatory hop LCRC; record profile decision.
- [ ] If enabled implement digest placement, invariant-field CRC rules and generation/check enables; otherwise handle TD packets as required without false capability advertisement.
- [ ] Document effect on packet buffers and payload length accounting.

## pyuvm verification

- [ ] Test known ECRC vectors, invariant/mutable field mutations, bad digest, missing digest and back-to-back TD packets.
- [ ] Check advertised feature-disabled behavior as well as enabled mode.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Explicit implement-or-omit disposition with source citations.
- [ ] If implemented all ECRC fault and control combinations are covered.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
