---
id: PCIE-040
title: "Integrate PHY macros and digital core into the mixed-signal top"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-007", "PCIE-008", "PCIE-049", "PCIE-055", "PCIE-059", "PCIE-060"]
spec_sections: ["4.1", "4.3", "6.6"]
---

# PCIE-040 — Integrate PHY macros and digital core into the mixed-signal top

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-040 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.1 — Introduction](../specification/4/1/summary.md): direct pp. 161–161; follow child sections and PDF tables.
- [4.3 — Electrical Sub-block](../specification/4/3/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [6.6 — PCI Express Reset - Rules](../specification/6/6/summary.md): direct pp. 316–319; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Integrate the hardened digital core and the PCIE-007/008/049 PMA macros in a mixed-signal top: macro placement, analog and digital supply separation, guard rings and power-domain boundaries.
- [ ] Close timing on the digital-to-PMA parallel interfaces and the recovered-clock crossing using macro timing abstracts.
- [ ] Verify the top with the PCIE-060 co-simulation method (digital RTL or gate level with behavioral or extracted PMA models) and record what each run covers.
- [ ] Pass top-level DRC, LVS and antenna checks with documented waivers.
- [ ] Bind N_FTS, Extended Synch use and L0s exit latency parameters to the PCIE-046/008 receive relock budget and verify them in co-simulation.

## pyuvm verification

- [ ] Run the PCIE-039 enumeration regression through behavioral PMA models connected at the integrated top.
- [ ] Assert idle, detect, polarity, recovered clock and reset mapping between core and PMA macros.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Re-simulate the PMA macros with top-level supply, substrate and coupling parasitics where extractable; report any degradation against PCIE-007/008/049 results.

## Acceptance criteria

- [ ] Integrated top is DRC/LVS clean with waivers documented.
- [ ] Digital-to-PMA interface timing closes at all corners.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
