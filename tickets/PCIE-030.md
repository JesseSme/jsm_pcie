---
id: PCIE-030
title: "Implement required PCI-PM capability and device power states"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-017", "PCIE-018", "PCIE-027"]
spec_sections: ["5.1", "5.3", "5.5", "5.6", "7.6"]
---

# PCIE-030 — Implement required PCI-PM capability and device power states

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-030 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [5.1 — Overview](../specification/5/1/summary.md): direct pp. 231–232; follow child sections and PDF tables.
- [5.3 — PCI-PM Software Compatible Mechanisms](../specification/5/3/summary.md): direct pp. 237–237; follow child sections and PDF tables.
- [5.5 — Auxiliary Power Support](../specification/5/5/summary.md): direct pp. 269–269; follow child sections and PDF tables.
- [5.6 — Power Management System Messages and DLLPs](../specification/5/6/summary.md): direct pp. 270–273; follow child sections and PDF tables.
- [7.6 — PCI Power Management Capability Structure](../specification/7/6/summary.md): direct pp. 361–363; follow child sections and PDF tables.

Primary ownership: 28 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Obtain companion PCI-PM details referenced by section7.6 and record exact revision.
- [ ] Implement mandatory D0/D3hot and required link power protocol; advertise D1/D2/auxiliary wake only when physically supported.
- [ ] Coordinate transaction drain, config visibility, PME policy, PM DLLPs and L1/L2/L3-ready sequences.
- [ ] Separate optional ASPM L1 from software-PM obligations and document D3cold reset/retention behavior.

## pyuvm verification

- [ ] Write PM controls during outstanding posted/non-posted traffic, exercise PME enabling/status and allowed wake sources.
- [ ] Check drain/ack ordering, state access rules, reset retention and absent auxiliary power cases.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Mandatory PM transitions complete without packet loss or deadlock.
- [ ] Capabilities match chip and system support and companion definitions are resolved.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
