---
id: PCIE-012
title: "Implement symbol framing and ordered-set parser/generator"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-010", "PCIE-011"]
spec_sections: ["4.2.2", "4.2.4.1", "4.2.4.3", "4.2.8"]
---

# PCIE-012 — Implement symbol framing and ordered-set parser/generator

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-012 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [4.2.2 — Framing and Application of Symbols to Lanes](../specification/4/2/2/summary.md): direct pp. 165–165; follow child sections and PDF tables.
- [4.2.4.1 — Training Sequence Ordered Sets](../specification/4/2/4/1/summary.md): direct pp. 170–173; follow child sections and PDF tables.
- [4.2.4.3 — Fast Training Sequence (FTS)](../specification/4/2/4/3/summary.md): direct pp. 173–174; follow child sections and PDF tables.
- [4.2.8 — Compliance Pattern](../specification/4/2/8/summary.md): direct pp. 211–213; follow child sections and PDF tables.

Primary ownership: 4 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement STP/SDP/END/EDB framing, idle and TS1/TS2/FTS/SKP ordered sets for x1.
- [ ] Validate training fields, lane/link number PAD handling, consecutive-set recognition and malformed frames.
- [ ] Coordinate scrambling, encoding and packet arbitration without dropping or duplicating symbols.
- [ ] Run an early open-flow synthesis of framing, 8b/10b and scrambling on GW2AR-18 and report achieved Fmax against the PCIE-001 logical clock; escalate a miss to the PCIE-001 datapath decision before more RTL depends on it.

## pyuvm verification

- [ ] Drive all legal packet/ordered-set boundaries and corrupt every ordered-set field class.
- [ ] Verify TS counters reset on broken consecutiveness and no malformed frame reaches TL.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Wire sequence matches source framing rules for TLP, DLLP and training traffic.
- [ ] All injected framing faults produce defined error/recovery behavior.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
