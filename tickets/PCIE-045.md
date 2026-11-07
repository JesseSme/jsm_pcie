---
id: PCIE-045
title: "Qualify extracted SKY130 PHY building blocks"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-062"]
spec_sections: ["4.2.1.1", "4.3.2.2", "4.3.3"]
---

# PCIE-045 — Qualify extracted SKY130 PHY building blocks

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-045 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2.1.1 — Serialization and De-serialization of Data](../specification/4/2/1/1/summary.md): direct pp. 162–163; follow child sections and PDF tables.
- [4.3.2.2 — Jitter and BER](../specification/4/3/2/2/summary.md): direct pp. 219–219; follow child sections and PDF tables.
- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Simulate every extracted PCIE-062 cell across all corners, temperature, supply and mismatch; iterate schematic or layout where margins fail.
- [ ] Deliver an edge-by-edge timing budget for the final serializer stages, including retiming and race avoidance, and report the standard-cell/current-mode partition evidence to PCIE-003/007/008.
- [ ] Qualify cells with ideal bias sources; PCIE-007/008/049 re-qualify them with the PCIE-059 bias circuits and record any difference.
- [ ] Record quantitative pass/fail or a documented rejection; a rejection is reported to the user under the PCIE-003 fallback, never silently worked around.

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
