---
id: PCIE-027
title: "Implement configuration Type0 header and BAR decoding"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-023", "PCIE-024"]
spec_sections: ["7.1", "7.2.2.2", "7.3", "7.4", "7.5.1", "7.5.2"]
---

# PCIE-027 — Implement configuration Type0 header and BAR decoding

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-027 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [7.1 — Configuration Topology](../specification/7/1/summary.md): direct pp. 337–338; follow child sections and PDF tables.
- [7.2.2.2 — PCI Express Device Requirements](../specification/7/2/2/2/summary.md): direct pp. 343–344; follow child sections and PDF tables.
- [7.3 — Configuration Transaction Rules](../specification/7/3/summary.md): direct pp. 345–345; follow child sections and PDF tables.
- [7.4 — Configuration Register Types](../specification/7/4/summary.md): direct pp. 348–349; follow child sections and PDF tables.
- [7.5.1 — Type 0/1 Common Configuration Space](../specification/7/5/1/summary.md): direct pp. 349–351; follow child sections and PDF tables.
- [7.5.2 — Type 0 Configuration Space Header](../specification/7/5/2/summary.md): direct pp. 356–357; follow child sections and PDF tables.

Primary ownership: 26 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement function-zero Type0 config read/write completer with correct BDF capture, byte enables and register attributes.
- [ ] Provide legal development identity parameters; avoid claiming assigned Vendor ID ownership.
- [ ] Implement 64-bit BAR sizing/probe and address masks, Memory Space Enable, Bus Master Enable, status W1C and reserved bits.
- [ ] Use a proposed 4KiB BAR0/BAR1 pair and unused BARs returning zero; exact resource profile is confirmed in PCIE-001.

## pyuvm verification

- [ ] Emulate BIOS/OS enumeration, BAR all-ones probing, relocation, byte writes and command gating.
- [ ] Attempt writes to RO/reserved/W1C fields and accesses to unsupported functions/routing types.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Host BFM enumerates one endpoint with consistent resource masks.
- [ ] No register access violates configured attributes and disabled memory decoding produces no side effects.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
