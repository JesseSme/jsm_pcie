---
id: PCIE-041
title: "Run synthesis, resource, timing and CDC signoff"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-039"]
spec_sections: ["1.5.4", "4.2", "4.3.1.1"]
---

# PCIE-041 — Run synthesis, resource, timing and CDC signoff

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-041 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [1.5.4 — Layer Functions and Services](../specification/1/5/4/summary.md): direct pp. 38–38; follow child sections and PDF tables.
- [4.2 — Logical Sub-block](../specification/4/2/summary.md): direct pp. 161–162; follow child sections and PDF tables.
- [4.3.1.1 — Clocking Dependencies](../specification/4/3/1/1/summary.md): direct pp. 213–213; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Add lint and synthesis targets for supported OSS CAD Suite tools; document vendor-tool dependency if selected FPGA needs it.
- [ ] Measure FIFO/BRAM/LUT/FF use, critical paths and logical-clock feasibility at the width and clock frozen in PCIE-001.
- [ ] Run CDC/reset analysis and audit generated clocks, false paths and multi-cycle constraints.
- [ ] Separate board-independent synthesis from final board timing closure dependent on PCIE-040.
- [ ] Attempt synthesis and place-and-route for GW2AR-LV18QN88C8/I7; report LUT4, FF, BSRAM, PLL, I/O and clock/timing use against actual available resources.
- [ ] Try bounded storage and equivalent wider/slower fabric pipelines without removing mandatory endpoint behavior; record tool/device support separately from capacity or timing failure.
- [ ] If the core cannot fit after documented optimization, activate the user-authorized I/O-reference fallback: continue the full digital core and pyuvm tests with GW2AR I/O-constrained ngspice models, preserving the failed-fit report.
- [ ] Use the open flow validated in PCIE-002 (yosys, nextpnr-himbaechel, gowin_pack) for synthesis and place-and-route; cross-check timing with vendor Gowin EDA where the open timing model is not adequate for signoff, recording versions of both.

## pyuvm verification

- [ ] Run pyuvm regression on synthesizable top after lint fixes.
- [ ] Check post-synthesis reset/encoding/packet behavior where supported and flag unsupported primitives.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] No inferred latches, unintended memories or unexplained unconstrained paths.
- [ ] Report either actual routed timing/resource fit or a reviewed failed-fit decision activating I/O-reference fallback; never label an unplaced design hardware-ready.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
