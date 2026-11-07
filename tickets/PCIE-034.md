---
id: PCIE-034
title: "Assess optional AER and extended capability space"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: conditional
depends_on: ["PCIE-028", "PCIE-032"]
spec_sections: ["7.9", "7.10"]
---

# PCIE-034 — Assess optional AER and extended capability space

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-034 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [7.9 — PCI Express Extended Capabilities](../specification/7/9/summary.md): direct pp. 401–402; follow child sections and PDF tables.
- [7.10 — Advanced Error Reporting Capability](../specification/7/10/summary.md): direct pp. 403–405; follow child sections and PDF tables.

Primary ownership: 16 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Record decision on optional AER; if omitted ensure baseline reporting and extended-space reads remain correct.
- [ ] If enabled implement endpoint AER header/status/masks/severity/header log and first-error behavior with no root-only registers.
- [ ] Define linked-list layout and coherent logging under simultaneous errors.

## pyuvm verification

- [ ] Walk extended capability chain and test W1C/mask/severity/first-error cases with simultaneous injections.
- [ ] If omitted verify no false AER advertisement and baseline errors remain visible.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] All optional-capability decisions are explicit.
- [ ] Advertised AER passes bit-attribute and fault-injection matrix.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
