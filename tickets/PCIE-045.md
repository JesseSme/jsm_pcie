---
id: PCIE-045
title: "Qualify SKY130 transistor-level PHY building blocks first"
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

# PCIE-045 — Qualify SKY130 transistor-level PHY building blocks first

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-045 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2.1.1 — Serialization and De-serialization of Data](../specification/4/2/1/1/summary.md): direct pp. 162–163; follow child sections and PDF tables.
- [4.3.2.2 — Jitter and BER](../specification/4/3/2/2/summary.md): direct pp. 219–219; follow child sections and PDF tables.
- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Following docs/phy-architecture.md, design and qualify building blocks before full TX/RX integration: current-mode buffer, latch and 2:1 mux, clock divider, standard-cell-to-current-mode level conversion, sampler/comparator and a VCO candidate.
- [ ] Use the pinned SKY130 ngspice models and corners; choose device flavors (1.8 V core, 3.3 V or other devices where needed) with documented reasons; transition frequency is not a guaranteed digital toggle rate.
- [ ] Lay out each cell in Magic, pass DRC/LVS and simulate extracted netlists; schematic-only results do not qualify a cell.
- [ ] Measure the maximum reliable rate of standard-cell serializer stages versus custom current-mode stages and report the partition evidence to PCIE-003/007/008.
- [ ] Deliver an edge-by-edge timing budget for the final serializer stages, including retiming and race avoidance.
- [ ] Record quantitative pass/fail or a documented rejection; a rejection is reported to the user under the PCIE-003 fallback, never silently worked around.
- [ ] Qualify cells with ideal bias sources; PCIE-007/008/049 re-qualify them with the PCIE-059 bias circuits and record any difference.

## pyuvm verification

- [ ] Generate independent expected bit sequences through PCIE-009; compare sampled mux and latch outputs, exercising persistent opposite inputs and phase boundaries.
- [ ] Cover all input combinations, adjacent transitions, reset and deterministic phase restart; deliberately swap inputs or skew clocks to prove checker failure.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Run DC, loaded transition, fast select, latch/divider, sampler and VCO studies on schematic and extracted netlists across tt/ff/ss/sf/fs, temperature, supply and mismatch; demonstrate timestep convergence from <=10 ps and report glitches, setup/hold aperture, swing, jitter and power. Archive pass and deliberately failing fixtures.

## Acceptance criteria

- [ ] Each cell has schematic, layout, DRC/LVS, extracted corner results, bias, power and timing margins with reproducible commands.
- [ ] No ideal zero-delay selectors or unextracted results are used to claim success.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
