---
id: PCIE-053
title: "Select SKY130 memories and map endpoint buffers"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-050", "PCIE-051"]
spec_sections: ["2.6", "3.5.2"]
---

# PCIE-053 — Select SKY130 memories and map endpoint buffers

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-053 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [2.6 — Ordering and Receive Buffer Flow Control](../specification/2/6/summary.md): direct pp. 106–107; follow child sections and PDF tables.
- [3.5.2 — LCRC, Sequence Number, and Retry Management (TLP Transmitter)](../specification/3/5/2/summary.md): direct pp. 141–142; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Compare OpenRAM-generated SKY130 SRAM macros, DFFRAM and flip-flop arrays for the retry buffer, receive credit buffers and other storage, using sizes documented by PCIE-021/026 and the PCIE-001 profile.
- [ ] Record macro timing, area, port configuration, power pins and integration requirements; re-check sizes when PCIE-039 fixes final storage.
- [ ] Implement the SKY130 memory-wrapper variants from PCIE-051 with the selected memories.

## pyuvm verification

- [ ] Run the PCIE-051 wrapper tests against the selected macro functional models, including read-during-write and reset behavior.
- [ ] Exercise full-buffer and wrap conditions of the retry and credit buffers on the SKY130 memory configuration.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Each buffer has a selected implementation with timing and area evidence.
- [ ] Macro behavior matches the shared wrapper contract.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
