---
id: PCIE-015
title: "Implement LTSSM x1 Configuration and reach L0"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-014", "PCIE-013"]
spec_sections: ["4.2.6.3", "4.2.6.5", "4.2.4.7"]
---

# PCIE-015 — Implement LTSSM x1 Configuration and reach L0

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-015 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [4.2.6.3 — Configuration](../specification/4/2/6/3/summary.md): direct pp. 186–186; follow child sections and PDF tables.
- [4.2.6.5 — L0](../specification/4/2/6/5/summary.md): direct pp. 199–201; follow child sections and PDF tables.
- [4.2.4.7 — Link Width and Lane Sequence Negotiation](../specification/4/2/4/7/summary.md): direct pp. 175–175; follow child sections and PDF tables.

Primary ownership: 20 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement upstream-port link/lane negotiation through Configuration substates with lane zero and width one.
- [ ] Handle peer width proposals, PAD values, polarity, TS2 completion and idle qualification.
- [ ] Expose trained width/speed and link-up only after valid L0 transition.

## pyuvm verification

- [ ] Run pyuvm root-port training from reset to L0 under valid and adversarial TS sequences.
- [ ] Test wrong lane/link numbers, broken consecutive sets, timeout fallback and repeated retraining.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Legal root-port BFM reaches x1 2.5 GT/s L0 repeatably.
- [ ] Invalid negotiation cannot falsely assert link-up.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
