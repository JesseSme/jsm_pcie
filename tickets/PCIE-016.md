---
id: PCIE-016
title: "Implement Recovery, Disabled, Loopback, Hot Reset and compliance modes"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-015"]
spec_sections: ["4.2.6.4", "4.2.6.9", "4.2.6.10", "4.2.6.11", "4.2.8"]
---

# PCIE-016 — Implement Recovery, Disabled, Loopback, Hot Reset and compliance modes

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-016 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2.6.4 — Recovery](../specification/4/2/6/4/summary.md): direct pp. 197–197; follow child sections and PDF tables.
- [4.2.6.9 — Disabled](../specification/4/2/6/9/summary.md): direct pp. 206–207; follow child sections and PDF tables.
- [4.2.6.10 — Loopback](../specification/4/2/6/10/summary.md): direct pp. 207–207; follow child sections and PDF tables.
- [4.2.6.11 — Hot Reset](../specification/4/2/6/11/summary.md): direct pp. 209–210; follow child sections and PDF tables.
- [4.2.8 — Compliance Pattern](../specification/4/2/8/summary.md): direct pp. 211–213; follow child sections and PDF tables.

Primary ownership: 10 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement required Recovery lock/config/idle behavior and fallback; Gen1-only negotiation must never claim unsupported speed.
- [ ] Implement Disabled, endpoint loopback, Hot Reset and compliance state data paths and exit rules.
- [ ] Coordinate packet discard, scrambler reset, physical idle and DL state during transitions.

## pyuvm verification

- [ ] Inject symbol lock loss during traffic, directed recovery, peer Hot Reset, loopback requests and compliance entry.
- [ ] Verify stale packets never leak after retrain and legal traffic resumes with fresh DL initialization.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Each implemented LTSSM transition has positive and negative tests.
- [ ] Reset and recovery cannot deadlock ongoing DL/TL traffic.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
