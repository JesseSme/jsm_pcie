---
id: PCIE-042
title: "Close digital protocol coverage and stress recovery"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-039", "PCIE-041"]
spec_sections: ["2", "3", "4.2", "5", "6", "7"]
---

# PCIE-042 — Close digital protocol coverage and stress recovery

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-042 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [2 — Transaction Layer Specification](../specification/2/summary.md): direct pp. 43–43; follow child sections and PDF tables.
- [3 — Data Link Layer Specification](../specification/3/summary.md): direct pp. 127–127; follow child sections and PDF tables.
- [4.2 — Logical Sub-block](../specification/4/2/summary.md): direct pp. 161–162; follow child sections and PDF tables.
- [5 — Power Management](../specification/5/summary.md): direct pp. 231–231; follow child sections and PDF tables.
- [6 — System Architecture](../specification/6/summary.md): direct pp. 273–273; follow child sections and PDF tables.
- [7 — Software Initialization and Configuration](../specification/7/summary.md): direct pp. 337–337; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Collect coverage by reviewed requirement ID, TLP class, register field, LTSSM transition, timer boundary and error class.
- [ ] Add long-run constrained-random traffic with independent scoreboards and reproducible seeds.
- [ ] Audit fairness/deadlock, credit conservation, replay wrap and repeated reset/power cycles.
- [ ] Review requirement-candidate dispositions and fill coverage gaps including PDF-only tables/diagrams.

## pyuvm verification

- [ ] Run deterministic boundary suite plus documented multi-seed soak; bound expected progress with watchdogs.
- [ ] Mutate representative CRC, credit and state-transition behavior to demonstrate monitors fail.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] All applicable reviewed baseline requirements link to passing checks or explicit justified waivers.
- [ ] No untriaged failure or unreviewed mandatory rule remains at completion.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
