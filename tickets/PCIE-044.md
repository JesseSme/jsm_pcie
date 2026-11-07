---
id: PCIE-044
title: "Validate hardware bring-up and host interoperability"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: conditional
depends_on: ["PCIE-040", "PCIE-041", "PCIE-042", "PCIE-043"]
spec_sections: ["1.4", "4.3", "6.6", "7"]
---

# PCIE-044 — Validate hardware bring-up and host interoperability

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-044 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [1.4 — PCI Express Fabric Topology Configuration](../specification/1/4/summary.md): direct pp. 35–36; follow child sections and PDF tables.
- [4.3 — Electrical Sub-block](../specification/4/3/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [6.6 — PCI Express Reset - Rules](../specification/6/6/summary.md): direct pp. 316–319; follow child sections and PDF tables.
- [7 — Software Initialization and Configuration](../specification/7/summary.md): direct pp. 337–337; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Document safe board-specific programming, reset, refclock and test connections after physical feasibility approval.
- [ ] Verify real host enumeration, BAR probing/MMIO, MSI, power transitions and reset/recovery.
- [ ] Capture negotiated x1 Gen1 link status, host logs, error counters and measured physical evidence.
- [ ] Record host/platform and instrument limits; companion form-factor specification review is required before attachment.
- [ ] If the documented fit-failure fallback is active, record host interoperability and board measurements as not performed; a reviewed not-applicable disposition can close this conditional ticket, but cannot count as hardware verification.

## pyuvm verification

- [ ] Replay host-observed transactions as pyuvm regressions and add any interoperability corner cases.
- [ ] Compare real read/write/interrupt outcomes with simulation reference expectations.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Compare measured board waveforms with final ngspice predictions and update model parameters with provenance; rerun margins after fitting.

## Acceptance criteria

- [ ] For the hardware route, all preceding hardware criteria and tests pass with board evidence; for documented core fit failure, a signed not-applicable disposition identifies unperformed hardware checks and retained I/O-reference models.
- [ ] Fallback is enabled only by a documented fit decision, not by a tool installation failure or an unsupported electrical assumption.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
