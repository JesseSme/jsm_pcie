---
id: PCIE-024
title: "Implement completer, read splitting and byte-enable semantics"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-022", "PCIE-023"]
spec_sections: ["2.2.9", "2.3.1.1"]
---

# PCIE-024 — Implement completer, read splitting and byte-enable semantics

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-024 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [2.2.9 — Completion Rules](../specification/2/2/9/summary.md): direct pp. 76–78; follow child sections and PDF tables.
- [2.3.1.1 — Data Return for Read Requests](../specification/2/3/1/1/summary.md): direct pp. 87–93; follow child sections and PDF tables.

Primary ownership: 1 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Build Cpl/CplD generator with completion status, byte count, lower address, IDs and tags.
- [ ] Split memory read responses by MPS/read completion boundary rules and preserve enabled-byte accounting.
- [ ] Handle zero-length and byte-disabled accesses without unintended side effects; prioritize completion resources to avoid deadlock.

## pyuvm verification

- [ ] Sweep lengths, byte enables, address alignment and completion boundaries; apply arbitrary application response latency.
- [ ] Reassemble split completions in independent scoreboard and check all headers/bytes.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Each supported non-posted request completes with correct data/status and within defined service bound.
- [ ] No completion exceeds negotiated limits or returns bytes from another request.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
