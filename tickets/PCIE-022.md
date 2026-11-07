---
id: PCIE-022
title: "Implement TLP header codec and validation"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-048"]
spec_sections: ["2.1", "2.2.1", "2.2.2", "2.2.3", "2.2.4", "2.2.5", "2.2.6", "2.2.7", "2.2.9"]
---

# PCIE-022 — Implement TLP header codec and validation

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-022 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [2.1 — Transaction Layer Overview](../specification/2/1/summary.md): direct pp. 43–44; follow child sections and PDF tables.
- [2.2.1 — Common Packet Header Fields](../specification/2/2/1/summary.md): direct pp. 47–50; follow child sections and PDF tables.
- [2.2.2 — TLPs with Data Payloads - Rules](../specification/2/2/2/summary.md): direct pp. 50–52; follow child sections and PDF tables.
- [2.2.3 — TLP Digest Rules](../specification/2/2/3/summary.md): direct pp. 52–52; follow child sections and PDF tables.
- [2.2.4 — Routing and Addressing Rules](../specification/2/2/4/summary.md): direct pp. 52–52; follow child sections and PDF tables.
- [2.2.5 — First/Last DW Byte Enables Rules](../specification/2/2/5/summary.md): direct pp. 55–57; follow child sections and PDF tables.
- [2.2.6 — Transaction Descriptor](../specification/2/2/6/summary.md): direct pp. 57–57; follow child sections and PDF tables.
- [2.2.7 — Memory, I/O, and Configuration Request Rules](../specification/2/2/7/summary.md): direct pp. 62–65; follow child sections and PDF tables.
- [2.2.9 — Completion Rules](../specification/2/2/9/summary.md): direct pp. 76–78; follow child sections and PDF tables.

Primary ownership: 25 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement synthesizable packet types and serializers/parsers for 3DW/4DW memory, Type0 configuration, completion and supported messages.
- [ ] Validate format/type, length including zero encoding, payload alignment, byte enables, address routing, TD/EP, attributes and requester/completer IDs.
- [ ] Detect 4KB boundary and MPS/MRRS violations as applicable; preserve malformed/unsupported distinction.
- [ ] Centralize SV types with explicitly documented wire byte order.

## pyuvm verification

- [ ] Generate legal packet matrix and one-field mutations, 1DW/maximum lengths, unaligned byte enables and boundary addresses.
- [ ] Compare full emitted bytes and parsed fields with independent Python model.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Supported formats round-trip exactly.
- [ ] Illegal inputs are classified without out-of-range array accesses or partial application writes.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
