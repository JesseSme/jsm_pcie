---
id: PCIE-006
title: "Extract electrical limits and ngspice model assumptions"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P0
gate: baseline
depends_on: ["PCIE-001", "PCIE-002"]
spec_sections: ["4.3.1", "4.3.2", "4.3.3", "4.3.4"]
---

# PCIE-006 — Extract electrical limits and ngspice model assumptions

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-006 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [4.3.1 — Electrical Sub-Block Requirements](../specification/4/3/1/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [4.3.2 — Electrical Signal Specifications](../specification/4/3/2/summary.md): direct pp. 217–218; follow child sections and PDF tables.
- [4.3.3 — Differential Transmitter (TX) Output Specifications](../specification/4/3/3/summary.md): direct pp. 222–225; follow child sections and PDF tables.
- [4.3.4 — Differential Receiver (RX) Input Specifications](../specification/4/3/4/summary.md): direct pp. 228–231; follow child sections and PDF tables.

Primary ownership: 24 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Transcribe each applicable electrical table row, units, min/max, footnotes and measurement point into machine-readable limits with exact citations.
- [ ] Separate transmitter mask, receiver tolerance mask, measurement load and clock recovery measurement assumptions.
- [ ] Define ngspice-supported driver/receiver/package/channel models; if only IBIS is supplied document a validated conversion or alternate characterization rather than assuming native IBIS support.
- [ ] Assign confidence levels to ideal, behavioral, manufacturer and measured models; require PVT and model provenance.
- [ ] Capture Tang Nano 20K GW2AR-18 I/O limits and their datasheet revision alongside PCIe limits; retain them even if core resource fit fails, and do not infer board bank voltage from a device-supported I/O standard.
- [ ] Qualify nonlinear RF transistor models and solderable package parasitics for PCIE-045; S-parameters alone are insufficient for large-signal switching evidence.

## pyuvm verification

- [ ] Expose limit IDs in digital-to-analog waveform metadata and pyuvm pattern manifests.
- [ ] Check limit-table parsing catches missing units and contradictory min/max bounds.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Provide parameterized differential source, coupling capacitors, termination and channel loads; verify units, DC bias and convergence at nominal conditions.

## Acceptance criteria

- [ ] All applicable Chapter 4.3 limits are captured or explicitly marked missing.
- [ ] Review source PDF tables visually; no fabricated compliance thresholds.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
