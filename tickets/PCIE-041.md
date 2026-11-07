---
id: PCIE-041
title: "Run lint, synthesis, CDC and reset signoff for the integrated core"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-039", "PCIE-050", "PCIE-051"]
spec_sections: ["1.5.4", "4.2", "4.3.1.1"]
---

# PCIE-041 — Run lint, synthesis, CDC and reset signoff for the integrated core

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-041 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [1.5.4 — Layer Functions and Services](../specification/1/5/4/summary.md): direct pp. 38–38; follow child sections and PDF tables.
- [4.2 — Logical Sub-block](../specification/4/2/summary.md): direct pp. 161–162; follow child sections and PDF tables.
- [4.3.1.1 — Clocking Dependencies](../specification/4/3/1/1/summary.md): direct pp. 213–213; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Add lint and Yosys synthesis targets with the SKY130 standard-cell library for the integrated core; record versions.
- [ ] Run CDC and reset-domain analysis for the logical, PLL-derived TX and recovered RX clocks; audit generated clocks, false paths and multicycle constraints for PCIE-055.
- [ ] Report pre-layout timing at all selected corners with OpenSTA and area estimates; try equivalent wider or slower pipelines without removing mandatory endpoint behavior.
- [ ] Escalate a pre-layout timing miss to the PCIE-001 datapath decision.

## pyuvm verification

- [ ] Run the pyuvm regression on the synthesizable top after lint fixes.
- [ ] Run the regression on the post-synthesis netlist with SKY130 functional cell models where the simulator supports them.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] No inferred latches, unintended memories or unexplained unconstrained paths.
- [ ] CDC constraints and reports are complete and handed to PCIE-055.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
