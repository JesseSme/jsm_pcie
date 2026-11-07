---
id: PCIE-013
title: "Implement clock domains, elastic buffering and SKP compensation"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-004", "PCIE-012"]
spec_sections: ["4.2.7", "4.2.4.8"]
---

# PCIE-013 — Implement clock domains, elastic buffering and SKP compensation

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-013 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [4.2.7 — Clock Tolerance Compensation](../specification/4/2/7/summary.md): direct pp. 210–210; follow child sections and PDF tables.
- [4.2.4.8 — Lane-to-Lane De-skew](../specification/4/2/4/8/summary.md): direct pp. 176–176; follow child sections and PDF tables.

Primary ownership: 4 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Design async FIFOs and synchronized status/reset crossings for user, symbol and receive clocks.
- [ ] Implement x1 elasticity and SKP insertion/removal following source intervals and packet-boundary restrictions.
- [ ] Calculate FIFO depth for frequency offset, SSC assumptions, bursts and recovery latency; x1 does not need multilane deskew.
- [ ] Document overflow/underflow handling and avoid impossible physical-stream backpressure.
- [ ] Size elasticity for the PCIE-001/003 reference-clock policy; a free-running local clock against an SSC host violates the section 4.3.1.1 600 ppm requirement and is not a supported elastic-buffer operating case.

## pyuvm verification

- [ ] Use independent clocks with min/max permitted frequency offset and randomized reset phase.
- [ ] Scoreboard data preservation through SKP changes; test FIFO boundary pressure and lock loss.
- [ ] Include an out-of-tolerance clock-offset case that must report overflow or underflow rather than silently corrupt data.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] No data loss/reorder under supported clock offsets.
- [ ] CDC/reset review and timing constraints cover every crossing.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
