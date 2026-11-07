---
id: PCIE-040
title: "Implement chosen board PHY adapter and timing constraints"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: conditional
depends_on: ["PCIE-003", "PCIE-007", "PCIE-008", "PCIE-009", "PCIE-039", "PCIE-041"]
spec_sections: ["4.1", "4.3", "6.6"]
---

# PCIE-040 — Implement chosen board PHY adapter and timing constraints

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-040 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [4.1 — Introduction](../specification/4/1/summary.md): direct pp. 161–161; follow child sections and PDF tables.
- [4.3 — Electrical Sub-block](../specification/4/3/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [6.6 — PCI Express Reset - Rules](../specification/6/6/summary.md): direct pp. 316–319; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement FPGA-specific digital adapter, clock generation and dedicated I/O primitives only for approved feasible hardware path.
- [ ] Create pin assignments, I/O standards, generated clocks and timing/CDC constraints backed by board data.
- [ ] Avoid use of hard endpoint IP that would bypass planned core; document any PMA/PCS hard blocks and exact encoding ownership.
- [ ] If no physical I/O path passes feasibility, retain a failed electrical result and block hardware claims; the fit-failure fallback does not turn electrical failure into compliance.
- [ ] Target the Tang Nano 20K pinout and confirmed board revision; PCIE-041 provides the resource-fit decision before final board implementation.
- [ ] If PCIE-041 documents inability to fit after optimization, close this conditional work only with a reviewed not-applicable hardware disposition and a retained I/O-reference simulation adapter; do not claim a working bitstream.
- [ ] Implement the approved parallel-pin adapter and external-circuit control interface; preserve FPGA ownership of logical PHY coding and scrambling.
- [ ] Implement the PCIE-003 reference-clock routing and constrain every derived clock and gearbox crossing.

## pyuvm verification

- [ ] Run adapter contract tests against behavioral PHY and vendor primitive models where available.
- [ ] Assert mapping of idle, detect, polarity, recovered clock and reset between core and pins.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Replay implemented pin schedules using nonideal driver/channel models from PCIE-007/008/009. All source-cited modeled electrical limits must pass.

## Acceptance criteria

- [ ] For the hardware route, all preceding hardware criteria and tests pass with board evidence; for documented core fit failure, a signed not-applicable disposition identifies unperformed hardware checks and retained I/O-reference models.
- [ ] Fallback is enabled only by a documented fit decision, not by a tool installation failure or an unsupported electrical assumption.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
