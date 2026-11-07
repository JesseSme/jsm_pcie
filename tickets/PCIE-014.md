---
id: PCIE-014
title: "Implement LTSSM Detect and Polling"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-004", "PCIE-012"]
spec_sections: ["4.2.4", "4.2.5", "4.2.6.1", "4.2.6.2"]
---

# PCIE-014 — Implement LTSSM Detect and Polling

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-014 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2.4 — Link Initialization and Training](../specification/4/2/4/summary.md): direct pp. 169–170; follow child sections and PDF tables.
- [4.2.5 — Link Training and Status State Machine (LTSSM) Descriptions](../specification/4/2/5/summary.md): direct pp. 177–177; follow child sections and PDF tables.
- [4.2.6.1 — Detect](../specification/4/2/6/1/summary.md): direct pp. 182–182; follow child sections and PDF tables.
- [4.2.6.2 — Polling](../specification/4/2/6/2/summary.md): direct pp. 184–184; follow child sections and PDF tables.

Primary ownership: 27 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement endpoint/upstream-port Detect.Quiet/Active and Polling substates, receiver-detect handshakes and precise timers.
- [ ] Implement TS1/TS2 counting, polarity handling and compliance entry decisions.
- [ ] Parameterize simulation acceleration without changing production time units or off-by-one semantics.

## pyuvm verification

- [ ] Model no receiver, successful detection, detection timeout, reversed polarity, missing/corrupt TS sets and all Polling exits.
- [ ] Check each timer just before, on and after expiry and all count thresholds.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] State transitions and emitted sets match source transition rules.
- [ ] Fast simulation and production timers are linked by checked conversion.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
