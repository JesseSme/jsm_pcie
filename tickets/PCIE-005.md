---
id: PCIE-005
title: "Build pyuvm framework, symbol-level root-port agent and PHY reference models"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P0
gate: baseline
depends_on: ["PCIE-002", "PCIE-004"]
spec_sections: ["1.5", "4.2", "4.2.1", "4.2.3", "B", "C"]
---

# PCIE-005 — Build pyuvm framework, symbol-level root-port agent and PHY reference models

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-005 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [1.5 — PCI Express Layering Overview](../specification/1/5/summary.md): direct pp. 36–37; follow child sections and PDF tables.
- [4.2 — Logical Sub-block](../specification/4/2/summary.md): direct pp. 161–162; follow child sections and PDF tables.
- [4.2.1 — Symbol Encoding](../specification/4/2/1/summary.md): direct pp. 162–162; follow child sections and PDF tables.
- [4.2.3 — Data Scrambling](../specification/4/2/3/summary.md): direct pp. 168–169; follow child sections and PDF tables.
- [B — Symbol Encoding](../specification/B/summary.md): direct pp. 487–497; follow child sections and PDF tables.
- [C — Physical Layer Appendix](../specification/C/summary.md): direct pp. 497–497; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Build the shared pyuvm environment: configuration, deterministic seed handling, packet traces, timeout watchdogs, scoreboard base classes and coverage export reused by later tickets.
- [ ] Build a symbol and ordered-set root-port agent at the PCIE-004 interface for data and K symbols, TS1/TS2, FTS, SKP and electrical-idle ordered sets; separate active drivers from passive monitors.
- [ ] Implement independent Python 8b/10b (Appendix B) and scrambler (section 4.2.3, Appendix C) reference models from cited tables and equations; do not import DUT algorithm code.
- [ ] Leave DLLP and data-link partner models to PCIE-047 and TLP/configuration models to PCIE-048 so PCIE-010/011 are not blocked behind a complete Python link partner.

## pyuvm verification

- [ ] Self-check 8b/10b and scrambler models against Appendix B/C vectors without a DUT; inject invalid codes and wrong disparity that must be detected.
- [ ] Round-trip randomized symbol streams and ordered sets through the agent driver and monitor with an explicit model contract.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Reference vectors carry source citations and expected bytes.
- [ ] Failures include seed, packet context, time and violated requirement ID.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
