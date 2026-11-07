---
id: PCIE-039
title: "Integrate endpoint top and run enumeration-to-MMIO regression"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-016", "PCIE-026", "PCIE-028", "PCIE-029", "PCIE-030", "PCIE-031", "PCIE-032", "PCIE-035", "PCIE-036", "PCIE-038"]
spec_sections: ["1.5", "2", "3", "4", "7"]
---

# PCIE-039 — Integrate endpoint top and run enumeration-to-MMIO regression

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-039 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [1.5 — PCI Express Layering Overview](../specification/1/5/summary.md): direct pp. 36–37; follow child sections and PDF tables.
- [2 — Transaction Layer Specification](../specification/2/summary.md): direct pp. 43–43; follow child sections and PDF tables.
- [3 — Data Link Layer Specification](../specification/3/summary.md): direct pp. 127–127; follow child sections and PDF tables.
- [4 — Physical Layer Specification](../specification/4/summary.md): direct pp. 161–161; follow child sections and PDF tables.
- [7 — Software Initialization and Configuration](../specification/7/summary.md): direct pp. 337–337; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Connect SV logical PHY, DLL, TL, config, PM, reset and application through PCIE-004 interface.
- [ ] Define synthesis parameters and bounded storage with documented resource estimates.
- [ ] Add pyuvm root-port boot sequence through Detect, L0, DL initialization, config enumeration, BAR assignment and command enable.

## pyuvm verification

- [ ] Run memory reads/writes, MSI and requester completions concurrently with replay and credit starvation.
- [ ] Repeat complete startup from multiple seeds, peer reset, hot reset and link loss; check data and control scoreboards.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Single documented command demonstrates full digital endpoint behavior.
- [ ] No dropped, duplicated or reordered transaction outside permitted ordering rules.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
