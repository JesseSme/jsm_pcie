---
id: PCIE-058
title: "Prepare ASIC tapeout signoff and post-silicon test plan"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: conditional
depends_on: ["PCIE-043", "PCIE-056", "PCIE-057"]
spec_sections: ["4.3"]
---

# PCIE-058 — Prepare ASIC tapeout signoff and post-silicon test plan

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-058 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.3 — Electrical Sub-block](../specification/4/3/summary.md): direct pp. 213–213; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Assemble final GDS, signoff reports, versions, waivers and documentation for the chosen fabrication route.
- [ ] Confirm the chosen route's submission format (GDS or OASIS), required DRC deck (open tools or Cadence Pegasus), legal agreement, price and commitment deadline well before tapeout.
- [ ] Write a post-silicon bring-up and test plan: board, supplies, clocks, test interface, loopback, and later link tests.
- [ ] Do not submit for fabrication or incur cost without explicit user approval.

## pyuvm verification

- [ ] Map each post-silicon test to its pre-silicon pyuvm counterpart and expected result.
- [ ] Define pass/fail criteria for first-silicon bring-up.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Tapeout package is complete and reproducible from recorded commands.
- [ ] Submission happens only after explicit user approval.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
