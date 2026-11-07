---
id: PCIE-003
title: "Freeze SKY130 chip architecture, clocking, pins and PHY partition"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P0
gate: baseline
depends_on: ["PCIE-001", "PCIE-002"]
spec_sections: ["4.3", "4.3.1.1", "4.3.1.8", "4.3.2.2", "6.6"]
---

# PCIE-003 — Freeze SKY130 chip architecture, clocking, pins and PHY partition

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-003 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.3 — Electrical Sub-block](../specification/4/3/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [4.3.1.1 — Clocking Dependencies](../specification/4/3/1/1/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [4.3.1.8 — Receiver Detection](../specification/4/3/1/8/summary.md): direct pp. 215–216; follow child sections and PDF tables.
- [4.3.2.2 — Jitter and BER](../specification/4/3/2/2/summary.md): direct pp. 219–219; follow child sections and PDF tables.
- [6.6 — PCI Express Reset - Rules](../specification/6/6/summary.md): direct pp. 316–319; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Freeze docs/asic-target.md and docs/phy-architecture.md: digital core (transaction layer, data link layer and logical PHY including scrambling and 8b/10b) plus an on-chip SKY130 PMA (PLL, serializer, TX driver, RX front end, CDR and deserializer) on one die.
- [ ] Own the reference-clock architecture under the PCIE-001 policy: host 100 MHz REFCLK input, PLL multiplication to the serializer clock, CDR reference and digital clocks; budget jitter, SSC tracking and phase relations.
- [ ] Choose the PMA rate architecture (full-rate 2.5 GHz clocks, or half-rate 1.25 GHz clocks with a double-edge final stage) and the split of serializer/deserializer stages between standard cells and custom current-mode logic, as hypotheses for PCIE-045 to qualify.
- [ ] Choose the digital-to-PMA parallel width consistent with the PCIE-001 datapath (proposed 20 encoded bits per 125 MHz cycle) and list the required PMA controls (electrical idle, receiver detect, polarity, lock, power states, reset); PCIE-004 owns the detailed interface contract and timing.
- [ ] Budget chip pins (PCIe TX/RX pairs, REFCLK, PERST#, any wake signal, supplies, test access); select standard-cell library (sky130_fd_sc_hd by default), operating corners, supplies and a preliminary die area.
- [ ] Take area and pad assumptions from docs/fabrication-routes.md (checked 2026-11-07): about 10-15 mm² user area on ChipFoundry harnesses, or a 3.588 x 5.188 mm full-custom box on the Cadence aggregation route; PCIE-057 re-verifies and chooses the route, and no commitment or cost is implied.
- [ ] Define the digital-only fallback: if PCIE-045/046/007/008/049 reject the on-chip PHY, the chip proceeds as a digital core with PHY-boundary loopback and the PHY failure is reported, not hidden.
- [ ] Assign every PHY support block an owner: bias and references (PCIE-059), REFCLK input receiver and PLL (PCIE-049), pads and ESD (PCIE-052).
- [ ] Record off-chip parts the PHY relies on: TX AC-coupling capacitors (receiver detection depends on them), any precision calibration resistor, REFCLK termination and supply decoupling; the PCIE-044 test board must provide them.
- [ ] Decide beacon support for wake from L2 versus a WAKE# signal, because it affects both PCIE-017 and the PCIE-007 transmitter.

## pyuvm verification

- [ ] Define a PMA capability contract and pyuvm fault scenarios for loss of lock, detection failure and electrical idle.
- [ ] Compute encoded-data throughput and clock budgets independently of the RTL.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No circuit qualification here. Record circuit hypotheses, rates and budgets that PCIE-045, PCIE-049, PCIE-007 and PCIE-008 must confirm with SKY130 transistor-level simulation.

## Acceptance criteria

- [ ] Chip architecture, clocking, PMA rate architecture, pins and corners are recorded with sources and rationale.
- [ ] No PHY feasibility is asserted before PCIE-045/046/007/008/049 evidence; the fallback boundary is explicit.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
