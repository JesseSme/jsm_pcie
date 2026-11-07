---
id: PCIE-060
title: "Build an early PHY loopback top with logical PHY and PMA placeholders"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-003", "PCIE-013", "PCIE-045", "PCIE-054"]
spec_sections: ["4.2", "4.2.6.10", "4.3"]
---

# PCIE-060 — Build an early PHY loopback top with logical PHY and PMA placeholders

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-060 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [4.2 — Logical Sub-block](../specification/4/2/summary.md): direct pp. 161–162; follow child sections and PDF tables.
- [4.2.6.10 — Loopback](../specification/4/2/6/10/summary.md): direct pp. 207–207; follow child sections and PDF tables.
- [4.3 — Electrical Sub-block](../specification/4/3/summary.md): direct pp. 213–213; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Integrate the hardened logical-PHY blocks (8b/10b, scrambling, framing, elastic buffer) with behavioral PMA models and placeholder macro abstracts from PCIE-064/066/068 and PCIE-059 in a loopback test top.
- [ ] Floorplan the top with analog macro placeholders, analog and digital supply domains and the digital-to-PMA interface; close timing on that interface with preliminary abstracts.
- [ ] Select and set up the mixed-signal co-simulation method for PCIE-040 (for example ngspice d_cosim with Verilator) and record what it covers.
- [ ] Swap qualified PCIE-045 cells or early PMA macros in as they become available; the same top must accept final macros by replacing abstracts, with final integration in PCIE-040.
- [ ] Serve as the intermediate milestone between the verified digital core and the signed-off chip, and as a candidate first test chip.

## pyuvm verification

- [ ] Run TX-to-RX loopback of training sequences, SKP and random encoded data through behavioral and, where available, transistor-level PMA models.
- [ ] Inject lock loss, polarity inversion and clock offset in loopback and confirm detection and recovery.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Co-simulate the loopback path with any available transistor-level PMA blocks and confirm decoded bits match the independent expected stream; label behavioral results as such.

## Acceptance criteria

- [ ] Loopback top passes DRC/LVS with placeholders and closes interface timing at all corners.
- [ ] Co-simulation method is demonstrated on loopback traffic with documented coverage limits.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
