---
id: PCIE-058
title: "Assemble the verified core signoff and integration package"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-040", "PCIE-042", "PCIE-043", "PCIE-056"]
spec_sections: ["1.5.4.4", "4.3", "6.6"]
---

# PCIE-058 — Assemble the verified core signoff and integration package

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-058 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [1.5.4.4 — Inter-Layer Interfaces](../specification/1/5/4/4/summary.md): direct pp. 40–40; follow child sections and PDF tables.
- [4.3 — Electrical Sub-block](../specification/4/3/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [6.6 — PCI Express Reset - Rules](../specification/6/6/summary.md): direct pp. 316–319; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Collect signoff evidence for the core macro: static timing at all corners, DRC, LVS and antenna (PCIE-040/055), gate-level and equivalence results (PCIE-056), electrical qualification (PCIE-043) and protocol coverage closure (PCIE-042).
- [ ] Deliver core views: GDS, LEF, timing abstracts, gate-level netlist, RTL and behavioral models, and pin and interface documentation.
- [ ] Write the integration guide: interface timing, clocks and resets, supplies, pad/ESD/package and off-chip requirements from PCIE-003/052, loopback and test modes, and known limitations.
- [ ] Produce a verification summary linking every reviewed requirement to passing checks or justified waivers, and list what cannot be verified without silicon.

## pyuvm verification

- [ ] Re-run the full regression and signoff flow from a clean checkout with the recorded commands and confirm identical results.
- [ ] Confirm the delivered behavioral model passes the same core-boundary interface tests as the RTL.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Re-run the PCIE-043 electrical regression from a clean checkout and confirm the archived margins.

## Acceptance criteria

- [ ] Every signoff check passes or carries a justified waiver, reproducible from recorded commands.
- [ ] The integration guide states every requirement an integrator must meet for the verified results to hold.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
