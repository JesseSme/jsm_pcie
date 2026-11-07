---
id: PCIE-009
title: "Bridge digital patterns to ngspice and produce electrical evidence"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P0
gate: baseline
depends_on: ["PCIE-005", "PCIE-006"]
spec_sections: ["4.2.8", "4.3.3.1", "4.3.3.2", "4.3.3.4"]
---

# PCIE-009 — Bridge digital patterns to ngspice and produce electrical evidence

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-009 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2.8 — Compliance Pattern](../specification/4/2/8/summary.md): direct pp. 211–213; follow child sections and PDF tables.
- [4.3.3.1 — Transmitter Compliance Eye Diagrams](../specification/4/3/3/1/summary.md): direct pp. 225–226; follow child sections and PDF tables.
- [4.3.3.2 — Eye Measurement Clock Recovery Function](../specification/4/3/3/2/summary.md): direct pp. 226–227; follow child sections and PDF tables.
- [4.3.3.4 — Compliance Test and Measurement Load](../specification/4/3/3/4/summary.md): direct pp. 227–228; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Create a converter from timestamped PHY bit/pin events to PWL sources with explicit units, finite rise/fall, bit order and simulator time origin.
- [ ] Create machine-readable analog results with source stream hash, seed, model hashes, corners and electrical limit IDs.
- [ ] Add eye folding using the specified measurement clock recovery method, mask checks and amplitude/jitter/de-emphasis measurements.
- [ ] Keep short transient eye checks distinct from statistically meaningful BER qualification.
- [ ] Drive the PMA parallel interface and PLL clocks into the transistor-level serializer rather than replacing it with an ideal 2.5 Gb/s source.

## pyuvm verification

- [ ] Generate compliance patterns, legal high-transition and low-transition streams, TS1/TS2, SKP and idle exits using pyuvm.
- [ ] Verify PWL time spacing equals 400 ps per UI at nominal rate and recovered data matches source bits.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Run ngspice transient batch regressions on all supported corners; set maximum timestep conservatively, initially <= UI/40, and demonstrate convergence by halving it.

## Acceptance criteria

- [ ] Regression exits nonzero for a deliberately degraded electrical corner and passes a known analytical fixture.
- [ ] Electrical reports identify unmodeled effects and never assert compliance from ideal eye plots alone.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
