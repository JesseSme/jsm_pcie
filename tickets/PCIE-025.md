---
id: PCIE-025
title: "Implement requester tags, completion matching and timeout"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-022", "PCIE-024"]
spec_sections: ["2.3.2", "2.8", "2.2.6.2"]
---

# PCIE-025 — Implement requester tags, completion matching and timeout

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-025 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [2.3.2 — Completion Handling Rules](../specification/2/3/2/summary.md): direct pp. 93–95; follow child sections and PDF tables.
- [2.8 — Completion Timeout Mechanism](../specification/2/8/summary.md): direct pp. 123–124; follow child sections and PDF tables.
- [2.2.6.2 — Transaction Descriptor – Transaction ID Field](../specification/2/2/6/2/summary.md): direct pp. 58–60; follow child sections and PDF tables.

Primary ownership: 2 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement optional application-facing memory read/write engine as a planned baseline feature; gate requests with Bus Master Enable.
- [ ] Allocate unique tags and support required 64-bit memory addressing; track requested byte ranges and split completion progress.
- [ ] Detect unexpected, duplicate, poisoned, failed and timed-out completions; retire tags safely and report errors.
- [ ] Keep requester resource allocation from starving completer responses.

## pyuvm verification

- [ ] Interleave split completions across tags, reverse response order where legal and exercise status failures.
- [ ] Test timeout boundaries, tag exhaustion, wrong requester/tag, BME disable and reset with requests outstanding.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] No request tag is reused while outstanding.
- [ ] Exactly one terminal outcome per request and no transmit when BME forbids it.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
