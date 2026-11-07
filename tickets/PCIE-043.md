---
id: PCIE-043
title: "Qualify electrical path across corners and expose limits of simulation"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-007", "PCIE-008", "PCIE-009", "PCIE-040", "PCIE-049", "PCIE-052"]
spec_sections: ["4.3"]
---

# PCIE-043 — Qualify electrical path across corners and expose limits of simulation

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-043 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.3 — Electrical Sub-block](../specification/4/3/summary.md): direct pp. 213–213; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Run final chosen driver/channel/RX model suite and archive configuration, plots and numerical margins.
- [ ] Audit mask measurement, de-emphasis, jitter transfer, idle, detect and receive tolerance at supported corners.
- [ ] Separate modeled results from hardware compliance; estimate BER evidence needed and plan equipment measurements.
- [ ] Reject circuit if compliant arbitrary-data TX/RX cannot be demonstrated; do not lower link speed and label it Gen1.
- [ ] Under the PCIE-003 digital-only fallback, record the electrical path as not implemented rather than qualified.

## pyuvm verification

- [ ] Generate all analog stimuli from pyuvm regression manifests including training, compliance and stress patterns.
- [ ] Correlate digital symbol events with analog decoded bits and lock/drop events.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Batch all PVT/model corners; verify timestep convergence and reproducibility. Include deliberately bad channels and skew so limit checks are demonstrated to fail.

## Acceptance criteria

- [ ] Every applicable electrical requirement has a model result or explicit pending laboratory measurement.
- [ ] No full PCIe compliance claim from transient ngspice alone.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
