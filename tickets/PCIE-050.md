---
id: PCIE-050
title: "Reproduce SKY130 PDK, OpenROAD and OpenLane implementation environment"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-002"]
spec_sections: ["1.5.4.4"]
---

# PCIE-050 — Reproduce SKY130 PDK, OpenROAD and OpenLane implementation environment

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-050 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [1.5.4.4 — Inter-Layer Interfaces](../specification/1/5/4/4/summary.md): direct pp. 40–40; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Install a pinned SKY130 PDK build with the PDK version manager used by the selected OpenLane release (volare or ciel); record the exact PDK commit and keep the PDK outside the repository.
- [ ] Install OpenLane 2 (or LibreLane, its continuation) using Docker or Podman, which are available on this machine, or Nix; use classic OpenLane only if a fabrication harness requires it; record the exact release.
- [ ] Install standalone OpenROAD and OpenSTA at the version bundled by the selected OpenLane release for interactive floorplan, timing and debug work; document any version difference.
- [ ] Install signoff tools used by the flow (Magic, KLayout, netgen) and xschem for SKY130 schematics; keep OpenLane-bundled Yosys separate from oss-cad-suite Yosys and record both versions.
- [ ] Add documented one-command launchers, git-ignore run directories and PDK caches, and record machine limits (16 cores, 14 GB RAM) that may constrain full-core runs.

## pyuvm verification

- [ ] Harden a trivial registered SystemVerilog block through the full flow and run a pyuvm test against both its RTL and its gate-level netlist.
- [ ] Introduce a deliberate timing violation and an LVS mismatch once and confirm the flow reports failure.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Run SKY130 ngspice models on an inverter transient from the pinned PDK and compare propagation delay with the corresponding standard-cell Liberty data within a documented tolerance.

## Acceptance criteria

- [ ] Fresh documented environment hardens the smoke design to GDS with DRC, LVS and STA reports and no hidden shell state.
- [ ] PDK, OpenLane, OpenROAD, Magic, KLayout, netgen and Yosys versions and exact commands are recorded.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
