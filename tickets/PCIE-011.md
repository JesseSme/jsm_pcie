---
id: PCIE-011
title: "Implement scrambling and descrambling"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-004", "PCIE-005"]
spec_sections: ["4.2.3", "C.1"]
---

# PCIE-011 — Implement scrambling and descrambling

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-011 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2.3 — Data Scrambling](../specification/4/2/3/summary.md): direct pp. 168–169; follow child sections and PDF tables.
- [C.1 — Data Scrambling](../specification/C/1/summary.md): direct pp. 497–503; follow child sections and PDF tables.

Primary ownership: 3 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement specified LFSR polynomial, initial value, bit order and advancement rules in SV.
- [ ] Apply exact reset/advance/bypass behavior for COM, SKP, training ordered sets, data and disabled scrambling.
- [ ] Support identical symbol-boundary behavior under stalls in internal pipelines without pausing wire cadence.

## pyuvm verification

- [ ] Compare long randomized streams with independent Python LFSR model.
- [ ] Exercise COM reseed, SKP hold, ordered sets, data/control boundaries, reset and scrambling-disable negotiation.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Known Appendix C vectors and independent model match cycle by cycle.
- [ ] No scrambler state advances on prohibited symbols or misses required advances.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
