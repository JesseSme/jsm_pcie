---
id: PCIE-056
title: "Verify gate-level ASIC netlist and RTL equivalence"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-042", "PCIE-055"]
spec_sections: ["2", "3", "4.2"]
---

# PCIE-056 — Verify gate-level ASIC netlist and RTL equivalence

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-056 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [2 — Transaction Layer Specification](../specification/2/summary.md): direct pp. 43–43; follow child sections and PDF tables.
- [3 — Data Link Layer Specification](../specification/3/summary.md): direct pp. 127–127; follow child sections and PDF tables.
- [4.2 — Logical Sub-block](../specification/4/2/summary.md): direct pp. 161–162; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Run formal equivalence between RTL and the synthesized and final netlists with eqy or another documented method, scoped to supported constructs.
- [ ] Run selected PCIE-042 pyuvm regressions on the post-route netlist with SDF back-annotation using a simulator that supports the SKY130 cell models and SDF; record simulator limitations.
- [ ] Check reset and X-propagation behavior on the gate-level netlist.

## pyuvm verification

- [ ] Repeat the enumeration-to-MMIO, replay and credit-starvation scenarios with reproducible seeds at gate level.
- [ ] Insert a netlist mutation and confirm equivalence or simulation detects it.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Equivalence passes for every checked stage or each unproven region is explained.
- [ ] Gate-level regressions agree with RTL results and limitations are recorded.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
