---
id: PCIE-038
title: "Implement endpoint system messages and slot power-limit handling"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-022", "PCIE-023", "PCIE-028", "PCIE-030", "PCIE-032"]
spec_sections: ["2.2.8", "6.8", "6.9"]
---

# PCIE-038 — Implement endpoint system messages and slot power-limit handling

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-038 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [2.2.8 — Message Request Rules](../specification/2/2/8/summary.md): direct pp. 65–66; follow child sections and PDF tables.
- [6.8 — Power Budgeting Capability](../specification/6/8/summary.md): direct pp. 330–331; follow child sections and PDF tables.
- [6.9 — Slot Power Limit Control](../specification/6/9/summary.md): direct pp. 331–334; follow child sections and PDF tables.

Primary ownership: 11 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Decode supported PM, error and Set_Slot_Power_Limit messages and route to owning blocks.
- [ ] Implement captured slot power limit scale/value behavior and related capability status as applicable.
- [ ] Apply required ignore/UR policy to vendor-defined and ignored messages; do not generate unsupported messages.
- [ ] Arbitrate message TX with completion, MSI and memory traffic without violating ordering.

## pyuvm verification

- [ ] Inject each message family with legal/illegal routing, length and payload; test repeated power-limit updates.
- [ ] Check register reflection, PM/error routing and no unintended BAR side effects.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Every Rev1.1 endpoint message has an explicit tested disposition.
- [ ] Message traffic cannot deadlock completion or credit returns.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
