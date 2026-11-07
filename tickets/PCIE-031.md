---
id: PCIE-031
title: "Implement required ASPM L0s and conditional L1"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-017", "PCIE-028", "PCIE-030"]
spec_sections: ["5.4", "4.2.6.6", "4.2.6.7"]
---

# PCIE-031 — Implement required ASPM L0s and conditional L1

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-031 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [5.4 — Native PCI Express Power Management Mechanisms](../specification/5/4/summary.md): direct pp. 253–253; follow child sections and PDF tables.
- [4.2.6.6 — L0s](../specification/4/2/6/6/summary.md): direct pp. 201–201; follow child sections and PDF tables.
- [4.2.6.7 — L1](../specification/4/2/6/7/summary.md): direct pp. 204–204; follow child sections and PDF tables.

Primary ownership: 10 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement mandatory L0s support, transmit idle entry policy, independent receive tolerance and FTS exit.
- [ ] Advertise measured/budgeted L0s exit latency and preserve higher-layer timer rules.
- [ ] Implement ASPM L1 only if explicitly selected and supported; otherwise advertise its absence while maintaining software-PM behavior.
- [ ] Derive advertised L0s exit latency from the PCIE-046/008 receive relock budget rather than from logical timing alone.

## pyuvm verification

- [ ] Test all ASPM control settings and traffic arrival around idle-entry and exit boundaries.
- [ ] Ensure TX-disabled L0s entry still tolerates peer RX-direction L0s; verify idle deadline from source.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Replay idle/FTS patterns through PCIE-009 at hardware-model corners and validate electrical settle/relock budget.

## Acceptance criteria

- [ ] Rev1.1 L0s obligations are tested even if early bring-up disables ASPM.
- [ ] All advertised exit latencies bound observed behavior.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
