---
id: PCIE-029
title: "Implement MSI generation and interrupt configuration"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-025", "PCIE-027"]
spec_sections: ["6.1", "7.7", "2.2.8.1"]
---

# PCIE-029 — Implement MSI generation and interrupt configuration

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-029 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [6.1 — Interrupt and PME Support](../specification/6/1/summary.md): direct pp. 273–273; follow child sections and PDF tables.
- [7.7 — MSI and MSI-X Capability Structures](../specification/7/7/summary.md): direct pp. 363–363; follow child sections and PDF tables.
- [2.2.8.1 — INTx Interrupt Signaling - Rules](../specification/2/2/8/1/summary.md): direct pp. 66–70; follow child sections and PDF tables.

Primary ownership: 11 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Acquire referenced normative MSI register definition where Base1.1 delegates to companion spec; track any unresolved fields explicitly.
- [ ] Implement one-vector MSI capability, address/data programming, enable and documented pending-event behavior.
- [ ] Generate legal memory-write MSI with ordering and BME interactions; suppress legacy INTx when MSI enabled.
- [ ] Advertise no MSI-X; implement any applicable legacy INTx fallback or explicitly justify its absence from profile.

## pyuvm verification

- [ ] Program 32/64-bit MSI addresses and event sequences; test enable/disable, BME, backpressure and reset.
- [ ] Scoreboard address, data, event count and ordering relative to application writes.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] One accepted event produces the documented interrupt transaction without duplication.
- [ ] Register layout is source-backed, not inferred from the Base1.1 cross-reference alone.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
