---
id: PCIE-019
title: "Implement Data Link state and flow-control initialization"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-015", "PCIE-018"]
spec_sections: ["3.2", "3.3", "2.9"]
---

# PCIE-019 — Implement Data Link state and flow-control initialization

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-019 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [3.2 — Data Link Control and Management State Machine](../specification/3/2/summary.md): direct pp. 129–130; follow child sections and PDF tables.
- [3.3 — Flow Control Initialization Protocol](../specification/3/3/summary.md): direct pp. 132–132; follow child sections and PDF tables.
- [2.9 — Link Status Dependencies](../specification/2/9/summary.md): direct pp. 124–124; follow child sections and PDF tables.

Primary ownership: 9 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement DL_Inactive/Init/Active rules coordinated with LTSSM and link status.
- [ ] Implement VC0 InitFC phases for posted/non-posted/completion header and data credits.
- [ ] Prevent application TLP emission before DL_Up; clear state on link loss and repeat initialization.

## pyuvm verification

- [ ] Test asymmetric initialization, missing/corrupt InitFC, peer restart and link-down at every phase.
- [ ] Verify DL_Up transitions and credit establishment against independent model.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] DL_Up only asserts after all required initialization conditions.
- [ ] Link loss reinitializes both credit and reliability state.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
