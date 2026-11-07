---
id: PCIE-017
title: "Implement PHY L0s, L1 and L2 state behavior"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-016"]
spec_sections: ["4.2.6.6", "4.2.6.7", "4.2.6.8", "5.2"]
---

# PCIE-017 — Implement PHY L0s, L1 and L2 state behavior

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-017 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2.6.6 — L0s](../specification/4/2/6/6/summary.md): direct pp. 201–201; follow child sections and PDF tables.
- [4.2.6.7 — L1](../specification/4/2/6/7/summary.md): direct pp. 204–204; follow child sections and PDF tables.
- [4.2.6.8 — L2](../specification/4/2/6/8/summary.md): direct pp. 205–205; follow child sections and PDF tables.
- [5.2 — Link State Power Management](../specification/5/2/summary.md): direct pp. 232–237; follow child sections and PDF tables.

Primary ownership: 16 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement independent TX/RX L0s entry/exit including idle and FTS; maintain appropriate higher-layer timers.
- [ ] Implement required software-PM L1 and L2/L3-ready control behavior and wake/reset paths with power manager.
- [ ] Implement the beacon-versus-WAKE# decision frozen in PCIE-003, and hardware power/lock acknowledgments.
- [ ] Make N_FTS, Extended Synch use and L0s exit latency build parameters; their final values must stay within the receive relock budget from PCIE-046/008 and are bound and checked in PCIE-040.

## pyuvm verification

- [ ] Enter RX L0s while TX stays active and vice versa; test FTS counts and exit latency.
- [ ] Exercise L1/L2 transitions with pending traffic, wake, failed lock and reset.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Use PCIE-009 with actual PHY candidate to check idle entry/exit transients and modeled relock latency; no analog proof from a purely logical status toggle.

## Acceptance criteria

- [ ] L0s support is retained for Rev1.1 baseline.
- [ ] All power transitions honor advertised exit latencies and specified timer behavior.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
