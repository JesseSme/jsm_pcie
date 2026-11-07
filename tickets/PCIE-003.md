---
id: PCIE-003
title: "Resolve external serializer/CDR interface feasibility for Tang Nano 20K"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P0
gate: baseline
depends_on: ["PCIE-001", "PCIE-002"]
spec_sections: ["4.3", "4.3.1.1", "4.3.1.8", "4.3.2.2"]
---

# PCIE-003 — Resolve external serializer/CDR interface feasibility for Tang Nano 20K

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-003 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [4.3 — Electrical Sub-block](../specification/4/3/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [4.3.1.1 — Clocking Dependencies](../specification/4/3/1/1/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [4.3.1.8 — Receiver Detection](../specification/4/3/1/8/summary.md): direct pp. 215–216; follow child sections and PDF tables.
- [4.3.2.2 — Jitter and BER](../specification/4/3/2/2/summary.md): direct pp. 219–219; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Board selection is resolved; verify exact board revision, bank voltages, usable pin pairs, clocking and electrical models for the selected Tang Nano 20K.
- [ ] Evaluate supported FPGA parallel I/O modes and external serializer/deserializer circuits for both TX and RX; direct single-pair Gen1 GPIO and native-transceiver substitution are outside the approved direction.
- [ ] Budget 2.5 GT/s NRZ with 400 ps UI, arbitrary encoded data, recovered receive clock, jitter, termination, AC coupling, electrical idle and receiver detection.
- [ ] Evaluate multiphase interleaving or external mux circuitry as an experiment: require sustainable independent data throughput, lane timing, switching bandwidth and receive recovery; multiplying a clock alone is insufficient.
- [ ] Freeze the external parallel/control interface and preliminary sourced clock/voltage/throughput budget; reserve transistor-cell qualification for PCIE-045 and full TX feasibility signoff for PCIE-007.
- [ ] Use Sipeed Tang Nano 20K with GW2AR-LV18QN88C8/I7 as the selected target; confirm board revision, actual bank rails, exposed differential pairs and clock routing from its schematic.
- [ ] Record DS226-2.7E Table 3-17 limits: IDES/OSER 8/10-bit gearbox maximum 1200 Mbps; direct 2500 Mbps operation exceeds the documented rate, so evaluate external serialization and RX recovery without overclocking assumptions.
- [ ] Separate core resource/timing fit from electrical feasibility; if the core cannot fit after documented optimization, the user authorizes a board-independent core using this devices I/O specifications as the electrical modeling target.
- [ ] Freeze the external serializer/deserializer and control-interface contract under docs/physical-interface-decision.md; use four 625 Mb/s TX streams as the first candidate and justify any parallel-width change.
- [ ] Select feasible external clocking, serializer, differential output, RX conditioning/CDR and deserializer candidates with explicit rate, voltage, jitter and select/capture timing budgets.
- [ ] Freeze constraints for the discrete-transistor-first serializer evaluation in PCIE-045; collect models and interface requirements before committing to any packaged serializer.
- [ ] Own the reference-clock architecture under the PCIE-001 policy: route host REFCLK (or a documented equivalent) to the external serializer clock, CDR reference and FPGA PLL; budget DS226 section 3.4.7 PLL limits, jitter and phase relation. A free-running 27 MHz oscillator or MS5351 is acceptable only for bench experiments or an explicit no-SSC host.
- [ ] Derive FPGA-side clocks from the PCIE-001 datapath decision; four 625 Mb/s outputs through 4:1 output serializers imply a 156.25 MHz parallel clock, so specify the ratio or asynchronous gearbox between it and the logical clock.
- [ ] Budget every required board pin: TX data and clock, RX data and recovered clock, electrical-idle, receiver-detect and power controls, PERST#, REFCLK and any wake signal, against exposed Tang Nano 20K pins and differential-capable banks.

## pyuvm verification

- [ ] Define a PHY capability contract and pyuvm fault scenarios for loss of lock, detection failure and electrical idle.
- [ ] Compute encoded-data throughput and clock-to-pin budget independently of the RTL.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Sweep proposed output/mux circuits with realistic finite pin edge rates, package parasitics, skew and loads; compare eye opening to 400 ps UI. Reject ideal-source-only demonstrations.

## Acceptance criteria

- [ ] Every interface candidate has a sourced budget and documented unresolved cell/model assumptions; no discrete serializer success is asserted before PCIE-045/007 qualification.
- [ ] No hardware-ready claim while pin routing, electrical levels or receive recovery remain unproven; board selection itself is no longer a blocker.
- [ ] Reference-clock source, SSC policy and every derived clock have a documented frequency and jitter budget.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
