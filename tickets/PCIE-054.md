---
id: PCIE-054
title: "Harden early PHY logic blocks in SKY130 to calibrate timing"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-012", "PCIE-050"]
spec_sections: ["4.2.1", "4.2.2", "4.2.3"]
---

# PCIE-054 — Harden early PHY logic blocks in SKY130 to calibrate timing

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-054 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2.1 — Symbol Encoding](../specification/4/2/1/summary.md): direct pp. 162–162; follow child sections and PDF tables.
- [4.2.2 — Framing and Application of Symbols to Lanes](../specification/4/2/2/summary.md): direct pp. 165–165; follow child sections and PDF tables.
- [4.2.3 — Data Scrambling](../specification/4/2/3/summary.md): direct pp. 168–169; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Harden the 8b/10b, scrambler and framing blocks with OpenLane as an early calibration of SKY130 timing at the PCIE-001 logical clock.
- [ ] Report setup and hold slack at all selected corners, area and power; escalate a miss at the slow corner to the PCIE-001 datapath decision.
- [ ] Record OpenLane configuration and flow settings as the starting point for full-core hardening.

## pyuvm verification

- [ ] Run the PCIE-010/011/012 pyuvm suites against the gate-level netlists of the hardened blocks.
- [ ] Confirm a deliberately inserted functional mutation in the netlist is caught by the same suites.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Timing results at every corner are recorded with exact flow versions and configuration.
- [ ] Gate-level behavior matches RTL under the existing suites.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
