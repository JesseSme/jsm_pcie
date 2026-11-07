---
id: PCIE-061
title: "Design SKY130 PHY building-block schematics"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-003", "PCIE-006", "PCIE-009", "PCIE-050"]
spec_sections: ["4.2.1.1", "4.3.2.2", "4.3.3"]
---

# PCIE-061 — Design SKY130 PHY building-block schematics

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-061 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2.1.1 — Serialization and De-serialization of Data](../specification/4/2/1/1/summary.md): direct pp. 162–163; follow child sections and PDF tables.
- [4.3.2.2 — Jitter and BER](../specification/4/3/2/2/summary.md): direct pp. 219–219; follow child sections and PDF tables.
- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Design xschem schematics for the PHY building blocks in docs/phy-architecture.md: current-mode buffer, latch and 2:1 mux, clock divider, standard-cell-to-current-mode level conversion, sampler/comparator and a VCO candidate.
- [ ] Size devices with the pinned SKY130 models and choose device flavors (1.8 V core, 3.3 V or others) with documented reasons; transition frequency is not a guaranteed toggle rate.
- [ ] Simulate each schematic across corners with ideal bias sources with an explicit parasitic margin, documented so the layout phase can check it; estimate the reliable rate of standard-cell versus current-mode serializer stages.
- [ ] Hand sized schematics and preliminary area estimates to PCIE-062.

## pyuvm verification

- [ ] Generate independent expected bit sequences through PCIE-009 and compare sampled mux, latch and divider schematic outputs, exercising persistent opposite inputs and phase boundaries.
- [ ] Deliberately swap inputs or skew clocks once to prove the checker fails.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Run DC, transient, fast-select, divider, sampler and VCO studies on schematics across tt/ff/ss/sf/fs, temperature, supply and mismatch with timestep convergence from <=10 ps; archive passing and deliberately failing fixtures.

## Acceptance criteria

- [ ] Every cell meets its budget at schematic level across corners, with the parasitic margin documented.
- [ ] Schematics, testbenches and commands are reproducible.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
