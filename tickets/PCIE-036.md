---
id: PCIE-036
title: "Build endpoint memory application and request interface"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-024", "PCIE-025", "PCIE-027"]
spec_sections: ["2.1.1.1", "2.3", "6.4"]
---

# PCIE-036 — Build endpoint memory application and request interface

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-036 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [2.1.1.1 — Memory Transactions](../specification/2/1/1/1/summary.md): direct pp. 45–45; follow child sections and PDF tables.
- [2.3 — Handling of Received TLPs](../specification/2/3/summary.md): direct pp. 78–81; follow child sections and PDF tables.
- [6.4 — Device Synchronization](../specification/6/4/summary.md): direct pp. 312–313; follow child sections and PDF tables.

Primary ownership: 1 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Provide a small SV BAR register/RAM application with version, scratch, counters and interrupt trigger.
- [ ] Define request/response valid-ready interfaces, byte strobes, 64-bit addresses, tags and error responses.
- [ ] Define side effects once per accepted write and application latency bounds; no specific DMA engine is required.
- [ ] Expose completion-safe resource partitioning and synchronization rules.

## pyuvm verification

- [ ] Read/write BAR using mixed sizes and byte enables while issuing requester traffic and interrupt triggers.
- [ ] Retry previously sent packets and verify side effects occur once; apply application backpressure.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Application supports end-to-end observable enumeration/MMIO/MSI demonstration.
- [ ] Bus handshakes cannot lose requests or starve mandatory completions.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
