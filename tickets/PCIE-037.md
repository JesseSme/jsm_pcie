---
id: PCIE-037
title: "Disposition out-of-profile topology and optional capabilities"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-001", "PCIE-027", "PCIE-028"]
spec_sections: ["1.3", "6.5", "6.7", "6.8", "6.9", "6.10", "7.5.3", "7.8.9", "7.8.10", "7.8.11", "7.8.12", "7.8.13", "7.8.14", "7.11", "7.12", "7.13", "7.14", "7.15", "7.16", "7.17", "7.18", "7.19", "A"]
---

# PCIE-037 — Disposition out-of-profile topology and optional capabilities

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-037 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [1.3 — PCI Express Fabric Topology](../specification/1/3/summary.md): direct pp. 30–30; follow child sections and PDF tables.
- [6.5 — Locked Transactions](../specification/6/5/summary.md): direct pp. 313–313; follow child sections and PDF tables.
- [6.7 — PCI Express Hot-Plug Support](../specification/6/7/summary.md): direct pp. 319–319; follow child sections and PDF tables.
- [6.8 — Power Budgeting Capability](../specification/6/8/summary.md): direct pp. 330–331; follow child sections and PDF tables.
- [6.9 — Slot Power Limit Control](../specification/6/9/summary.md): direct pp. 331–334; follow child sections and PDF tables.
- [6.10 — Root Complex Topology Discovery](../specification/6/10/summary.md): direct pp. 334–337; follow child sections and PDF tables.
- [7.5.3 — Type 1 Configuration Space Header](../specification/7/5/3/summary.md): direct pp. 357–358; follow child sections and PDF tables.
- [7.8.9 — Slot Capabilities Register (Offset 14h)](../specification/7/8/9/summary.md): direct pp. 390–392; follow child sections and PDF tables.
- [7.8.10 — Slot Control Register (Offset 18h)](../specification/7/8/10/summary.md): direct pp. 392–396; follow child sections and PDF tables.
- [7.8.11 — Slot Status Register (Offset 1Ah)](../specification/7/8/11/summary.md): direct pp. 396–398; follow child sections and PDF tables.
- [7.8.12 — Root Control Register (Offset 1Ch)](../specification/7/8/12/summary.md): direct pp. 398–400; follow child sections and PDF tables.
- [7.8.13 — Root Capabilities Register (Offset 1 Eh)](../specification/7/8/13/summary.md): direct pp. 400–400; follow child sections and PDF tables.
- [7.8.14 — Root Status Register (Offset 20h)](../specification/7/8/14/summary.md): direct pp. 400–401; follow child sections and PDF tables.
- [7.11 — Virtual Channel Capability](../specification/7/11/summary.md): direct pp. 419–421; follow child sections and PDF tables.
- [7.12 — Device Serial Number Capability](../specification/7/12/summary.md): direct pp. 434–435; follow child sections and PDF tables.
- [7.13 — PCI Express Root Complex Link Declaration Capability](../specification/7/13/summary.md): direct pp. 437–438; follow child sections and PDF tables.
- [7.14 — PCI Express Root Complex Internal Link Control Capability](../specification/7/14/summary.md): direct pp. 444–444; follow child sections and PDF tables.
- [7.15 — Power Budgeting Capability](../specification/7/15/summary.md): direct pp. 450–450; follow child sections and PDF tables.
- [7.16 — PCI Express Root Complex Event Collector Endpoint Association Capability](../specification/7/16/summary.md): direct pp. 454–455; follow child sections and PDF tables.
- [7.17 — Multi-Function Virtual Channel Capability](../specification/7/17/summary.md): direct pp. 456–457; follow child sections and PDF tables.
- [7.18 — Vendor-Specific Capability](../specification/7/18/summary.md): direct pp. 469–470; follow child sections and PDF tables.
- [7.19 — RCRB Header Capability](../specification/7/19/summary.md): direct pp. 472–472; follow child sections and PDF tables.
- [A — Isochronous Applications](../specification/A/summary.md): direct pp. 475–475; follow child sections and PDF tables.

Primary ownership: 128 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Review every mapped section for endpoint obligations before excluding root, switch, bridge, slot-controller, multi-function and isochronous implementation.
- [ ] Record optional VC expansion, DSN, power budgeting, vendor extensions and AER/ECRC decisions separately.
- [ ] Retain endpoint obligations for Set_Slot_Power_Limit reception, hot reset, error handling and default VC even when associated infrastructure is outside scope.
- [ ] Document unimplemented requests, messages, config offsets and capability-chain behavior.

## pyuvm verification

- [ ] Send root/bridge/slot-only controls and unsupported messages to endpoint; check required ignore/UR/error behavior.
- [ ] Verify all reserved config locations and absent capabilities respond as specified.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Every omitted feature has applicability rationale, source and negative-test owner.
- [ ] No entire chapter is excluded merely because some sections apply to switches.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
