---
id: PCIE-057
title: "Integrate chip top: pad ring, harness, test access and fabrication route"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-040", "PCIE-052"]
spec_sections: ["4.3", "6.6"]
---

# PCIE-057 — Integrate chip top: pad ring, harness, test access and fabrication route

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-057 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.3 — Electrical Sub-block](../specification/4/3/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [6.6 — PCI Express Reset - Rules](../specification/6/6/summary.md): direct pp. 316–319; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Identify a currently available SKY130 fabrication route and its harness, area, I/O and deadline constraints; record clearly if none is available.
- [ ] Integrate the hardened core into the chosen harness or pad frame with clock, reset (PERST#), power and I/O assignments that match the PCIE-003 chip architecture.
- [ ] Add test access: PHY-boundary loopback, pattern generator and checker, and status registers reachable through a slow interface, so the core can be exercised without a working 2.5 Gb/s link.
- [ ] Re-run full-chip DRC, LVS, STA and the route-specific precheck.

## pyuvm verification

- [ ] Run the integrated regression through the harness test interface and loopback paths.
- [ ] Confirm a broken loopback or misassigned pin is detected.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Integration passes route-specific prechecks or blockers are recorded.
- [ ] Test access lets silicon be evaluated without a host link.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
