---
id: PCIE-002
title: "Reproduce OSS CAD Suite, pyuvm and ngspice tool environment"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P0
gate: baseline
depends_on: []
spec_sections: ["1.5.4.4"]
---

# PCIE-002 — Reproduce OSS CAD Suite, pyuvm and ngspice tool environment

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-002 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [1.5.4.4 — Inter-Layer Interfaces](../specification/1/5/4/4/summary.md): direct pp. 40–40; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Add reproducible launcher and dependency lock for cocotb plus pyuvm; use oss-cad-suite/bin/verilator as primary SV simulator and Icarus only for supported subsets.
- [ ] Discover bundled Python rather than assuming bin/python3; reconcile project Python >=3.14 with suite Python ABI and cocotb shared libraries.
- [ ] Record exact simulator, Python, cocotb, pyuvm and ngspice versions; add one documented command each for digital and analog smoke tests.
- [ ] Keep vendored oss-cad-suite and original specifications out of generated change sets.
- [ ] Use a uv-managed project environment with its own pinned cocotb and pyuvm instead of the suite bundled Python 3.11 cocotb; confirm cocotb support for the chosen interpreter and, if Python 3.14 is unsupported, lower requires-python to the newest supported version and record why.
- [ ] Add a smoke build of a trivial design for Tang Nano 20K with the bundled open Gowin flow (yosys synth_gowin, nextpnr-himbaechel for GW2AR-18, gowin_pack) so device-database and toolchain problems surface before PCIE-041; record whether vendor Gowin EDA is also needed for timing signoff.

## pyuvm verification

- [ ] Run a small SystemVerilog clock/reset DUT with a pyuvm test through cocotb and assert that reset changes observable state.
- [ ] Fail intentionally once to prove assertion failures propagate nonzero; restore passing test.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Run ngspice -b on a known RC transient and compare measured settling time with analytic RC tolerance; exercise failure handling too.

## Acceptance criteria

- [ ] Fresh documented environment runs both smoke tests without hidden shell state.
- [ ] Commands, versions and logs are captured; no claim that preinstalled cocotb implies pyuvm availability.
- [ ] Open Gowin flow produces a bitstream for the smoke design, or the missing device support is recorded as a toolchain blocker rather than a resource-fit result.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
