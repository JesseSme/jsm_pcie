---
id: PCIE-028
title: "Implement PCI Express capability registers and live status"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-027", "PCIE-016", "PCIE-026"]
spec_sections: ["7.8.1", "7.8.2", "7.8.3", "7.8.4", "7.8.5", "7.8.6", "7.8.7", "7.8.8"]
---

# PCIE-028 — Implement PCI Express capability registers and live status

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-028 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [7.8.1 — PCI Express Capability List Register (Offset 00h)](../specification/7/8/1/summary.md): direct pp. 364–365; follow child sections and PDF tables.
- [7.8.2 — PCI Express Capabilities Register (Offset 02h)](../specification/7/8/2/summary.md): direct pp. 365–367; follow child sections and PDF tables.
- [7.8.3 — Device Capabilities Register (Offset 04h)](../specification/7/8/3/summary.md): direct pp. 367–372; follow child sections and PDF tables.
- [7.8.4 — Device Control Register (Offset 08h)](../specification/7/8/4/summary.md): direct pp. 372–378; follow child sections and PDF tables.
- [7.8.5 — Device Status Register (Offset 0Ah)](../specification/7/8/5/summary.md): direct pp. 378–380; follow child sections and PDF tables.
- [7.8.6 — Link Capabilities Register (Offset 0Ch)](../specification/7/8/6/summary.md): direct pp. 380–383; follow child sections and PDF tables.
- [7.8.7 — Link Control Register (Offset 10h)](../specification/7/8/7/summary.md): direct pp. 383–388; follow child sections and PDF tables.
- [7.8.8 — Link Status Register (Offset 12h)](../specification/7/8/8/summary.md): direct pp. 388–390; follow child sections and PDF tables.

Primary ownership: 9 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement capability linked list and Rev1.1 endpoint Device/Link capabilities, control and status fields.
- [ ] Advertise only x1 Gen1 and implemented MPS, tags, latency and error controls; bind live status to actual state.
- [ ] Route control writes to real behavior, including retrain/power/error controls where endpoint-applicable.
- [ ] Audit all register rows against PDF and reset values; omit slot/root structures for endpoint role.

## pyuvm verification

- [ ] Walk capability list, verify no cycles/overlap and test each bit access attribute and reset value.
- [ ] Change negotiated controls under traffic and compare status updates to PHY/DL monitors.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] No advertised capability lacks an implementation/test owner.
- [ ] Endpoint-inapplicable register fields follow specified reserved behavior.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
