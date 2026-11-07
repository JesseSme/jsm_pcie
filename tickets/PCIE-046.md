---
id: PCIE-046
title: "Assess external RX clock recovery feasibility before TX hardware spending"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P0
gate: baseline
depends_on: ["PCIE-003", "PCIE-006"]
spec_sections: ["4.2.4.3", "4.2.6.6", "4.3.1.1", "4.3.1.8", "4.3.4"]
---

# PCIE-046 — Assess external RX clock recovery feasibility before TX hardware spending

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-046 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [4.2.4.3 — Fast Training Sequence (FTS)](../specification/4/2/4/3/summary.md): direct pp. 173–174; follow child sections and PDF tables.
- [4.2.6.6 — L0s](../specification/4/2/6/6/summary.md): direct pp. 201–201; follow child sections and PDF tables.
- [4.3.1.1 — Clocking Dependencies](../specification/4/3/1/1/summary.md): direct pp. 213–213; follow child sections and PDF tables.
- [4.3.1.8 — Receiver Detection](../specification/4/3/1/8/summary.md): direct pp. 215–216; follow child sections and PDF tables.
- [4.3.4 — Differential Receiver (RX) Input Specifications](../specification/4/3/4/summary.md): direct pp. 228–231; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Perform a paper and behavioral feasibility study of the approved external receive path: input conditioning and termination, CDR topology (discrete PLL or DLL, phase-picking oversampler or another justified approach), 2.5 Gb/s sampler and deserializer to a GW2AR-supported parallel width, and recovered-clock delivery to the FPGA.
- [ ] Budget CDR lock and relock time against protocol deadlines: L0s exit within the advertised N_FTS FTS ordered sets (section 4.2.4.3: about 4 µs at N_FTS 255), Polling and Recovery timers and electrical-idle exit; record the N_FTS and L0s exit latency the receive path can honestly support for PCIE-017/031.
- [ ] Budget jitter tolerance and frequency tracking against section 4.3.4 receiver limits under the PCIE-001/003 reference-clock and SSC policy.
- [ ] Identify candidate discrete or component building blocks with model provenance under the same model-quality rules as PCIE-045; a high-speed sampler or comparator without a trustworthy model is a blocker, not an assumption.
- [ ] Produce a go, no-go or unknown recommendation and report a no-go or unknown result to the user before money is spent on TX coupon fabrication.

## pyuvm verification

- [ ] Drive a behavioral CDR model with pyuvm-generated training, FTS and data streams; measure modeled lock time against the N_FTS budget and detect false lock.
- [ ] Deliberately exceed the jitter or frequency budget and confirm the checks fail.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

Simulate the critical sampler and phase-detector front end with nonlinear models at the 400 ps UI where trustworthy models exist; label behavioral loop results as assumptions until hardware characterization.

## Acceptance criteria

- [ ] Recommendation states supportable N_FTS, lock time, jitter tolerance and remaining unknowns with sources.
- [ ] Unresolved model or component gaps are explicit blockers, not passes.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
