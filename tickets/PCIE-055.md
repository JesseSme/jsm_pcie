---
id: PCIE-055
title: "Harden the full endpoint core with OpenLane and sign off physical checks"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-003", "PCIE-041", "PCIE-053", "PCIE-054"]
spec_sections: ["1.5", "4.2"]
---

# PCIE-055 — Harden the full endpoint core with OpenLane and sign off physical checks

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-055 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [1.5 — PCI Express Layering Overview](../specification/1/5/summary.md): direct pp. 36–37; follow child sections and PDF tables.
- [4.2 — Logical Sub-block](../specification/4/2/summary.md): direct pp. 161–162; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Floorplan, power grid, placement, clock-tree synthesis for every clock domain, routing and fill for the integrated core with the selected memories.
- [ ] Close static timing at all selected corners including hold and clock-domain crossing constraints, and confirm CDC constraints match PCIE-041 analysis.
- [ ] Pass DRC (Magic and KLayout), LVS (netgen), antenna and IR-drop checks; record every waiver with justification.
- [ ] Report area, utilization, power and per-domain timing; try documented flow and pipeline optimizations without removing mandatory endpoint behavior.
- [ ] Deliver the hardened digital core as a macro with abstracts for PCIE-040.

## pyuvm verification

- [ ] Run the PCIE-039 integrated regression on the post-synthesis netlist.
- [ ] Check reset, clock-domain and memory behavior where gate-level simulation differs from RTL.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Signoff reports are clean or carry justified waivers, with exact versions and commands.
- [ ] Timing closes at all selected corners, or the failure and attempted optimizations are documented.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
