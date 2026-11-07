---
id: PCIE-026
title: "Implement VC0 credits and transaction ordering"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-019", "PCIE-021", "PCIE-022"]
spec_sections: ["2.4", "2.5", "2.6", "6.3", "D"]
---

# PCIE-026 — Implement VC0 credits and transaction ordering

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-026 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [2.4 — Transaction Ordering](../specification/2/4/summary.md): direct pp. 95–95; follow child sections and PDF tables.
- [2.5 — Virtual Channel (VC) Mechanism](../specification/2/5/summary.md): direct pp. 100–103; follow child sections and PDF tables.
- [2.6 — Ordering and Receive Buffer Flow Control](../specification/2/6/summary.md): direct pp. 106–107; follow child sections and PDF tables.
- [6.3 — Virtual Channel Support](../specification/6/3/summary.md): direct pp. 298–298; follow child sections and PDF tables.
- [D — Request Dependencies](../specification/D/summary.md): direct pp. 503–506; follow child sections and PDF tables.

Primary ownership: 29 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Track posted/non-posted/completion header/data credit pools in correct units with wrap and infinite-credit encodings.
- [ ] Implement UpdateFC generation/consumption and buffering minimums; charge credits once for original transmissions, not replay.
- [ ] Apply required ordering matrix, relaxed ordering and TC-to-VC0 policy; reserve independent progress for completions.
- [ ] Document FIFO sizing and dependencies with bounded backpressure and no circular wait.

## pyuvm verification

- [ ] Starve each credit class independently, force counter wrap and test infinite-credit advertisement.
- [ ] Run producer/consumer ordering litmus tests and saturation with replay plus completion returns.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] No transmission consumes unavailable credits; receive buffers cannot overrun legal advertised credits.
- [ ] Ordering scoreboard and bounded-progress checks pass under randomized backpressure.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
