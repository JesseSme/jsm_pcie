---
id: PCIE-045
title: "Qualify solderable transistor serializer building blocks first"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-003", "PCIE-006", "PCIE-009"]
spec_sections: ["4.2.1.1", "4.3.2.2", "4.3.3"]
---

# PCIE-045 — Qualify solderable transistor serializer building blocks first

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-045 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [4.2.1.1 — Serialization and De-serialization of Data](../specification/4/2/1/1/summary.md): direct pp. 162–163; follow child sections and PDF tables.
- [4.3.2.2 — Jitter and BER](../specification/4/3/2/2/summary.md): direct pp. 219–219; follow child sections and PDF tables.
- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Follow docs/discrete-transistor-serializer-plan.md as the required first route; evaluate RF NPN differential current-steering logic in solderable SMD packages before packaged serializer selection.
- [ ] Produce manufacturer/model provenance and package/bias tables; evaluate BFP420-class devices without treating transition frequency as guaranteed digital speed.
- [ ] Design transistor-labelled differential-pair, buffer, two-input mux, retiming latch and clock/divider cells with explicit bias, headroom, common mode and startup behavior.
- [ ] Create nonlinear ngspice fixtures with package/PCB/probe loads, finite FPGA edges and realistic fanout; qualify data and selector paths separately.
- [ ] Deliver an edge-by-edge phase/retiming budget for a three-mux 4:1 tree, plus coupon PCB/BOM/assembly and measurement plan; start with a laboratory differential clock while separately planning production reference clocking.
- [ ] Record quantitative pass/fail or a documented discrete-route rejection before proposing an IC alternative; no packaged serializer substitution without explicit user agreement.
- [ ] Do not purchase parts or fabricate coupons until PCIE-046 has recorded its receive-path recommendation, unless the user explicitly accepts that risk.

## pyuvm verification

- [ ] Generate independent expected group/bit sequences and timestamped FPGA events through PCIE-009; compare sampled mux output and exercise persistent opposite inputs and phase boundaries.
- [ ] Cover all four-bit values, adjacent group transitions, 10-bit symbol boundary crossings, reset and deterministic phase restart; deliberately swap inputs or skew clocks to prove checker failure.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Run DC/truth-table, loaded transition, fast select, latch/divider and mux corner studies. Sweep mismatch assumptions, bias, temperature, parasitics, duty cycle and phase skew; demonstrate timestep convergence from <=10 ps and report glitches, setup/hold aperture, swing, jitter and power. Archive pass and deliberately failing fixtures.

## Acceptance criteria

- [ ] A reviewed discrete building-block design or quantitative rejection includes nonlinear models, transistor-labelled schematics, bias/stress/power results, phase margin, source IDs and reproducible commands.
- [ ] Solderable coupon plan includes package footprints, routed parasitic assumptions, supported clock/data interfaces and measurement loading.
- [ ] No fabricated part parameters, ideal zero-delay selectors or unsupported FPGA rate assumptions are used to claim success; no hardware claim from simulations alone.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
