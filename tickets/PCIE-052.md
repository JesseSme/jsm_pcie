---
id: PCIE-052
title: "Define pad, ESD, package and channel models for PHY verification"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-003", "PCIE-006", "PCIE-050"]
spec_sections: ["4.3.1.8", "4.3.3", "4.3.4"]
---

# PCIE-052 — Define pad, ESD, package and channel models for PHY verification

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-052 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.3.1.8 — Receiver Detection](../specification/4/3/1/8/summary.md): direct pp. 215–216; follow child sections and PDF tables.
- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.
- [4.3.4 — Differential Receiver (RX) Input Specifications](../specification/4/3/4/summary.md): direct pp. 228–231; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Define the electrical environment the PHY macros drive and receive through: representative high-speed pad and ESD capacitance and resistance, bond-wire or package parasitics, AC-coupling capacitors and channel, with documented provenance and ranges.
- [ ] Provide a nominal and a worst-case integrator environment so PCIE-007/008/043 results state which environment they assume.
- [ ] Specify the pad and package limits an integrator must meet for the verified results to hold; these go into the PCIE-058 integration guide.
- [ ] Pad cells, ESD design and a pad ring are outside the core and are not designed here.

## pyuvm verification

- [ ] Include pad and package model identifiers in PCIE-009 manifests so electrical results trace to the pad configuration.
- [ ] Confirm a deliberately degraded pad model makes PCIE-043 limit checks fail.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Simulate the pad, ESD, package and channel models in transient with SKY130 driver and receiver loads at corners; report the effect on the TX eye and the RX input for the nominal and worst-case environments.

## Acceptance criteria

- [ ] Pad, ESD, package and channel models used by PCIE-007/008/043 have documented provenance and ranges.
- [ ] Integrator pad and package requirements are stated quantitatively.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
