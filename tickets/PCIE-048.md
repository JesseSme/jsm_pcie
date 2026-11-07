---
id: PCIE-048
title: "Build TLP, configuration and enumeration reference models"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-005"]
spec_sections: ["2.1", "2.2", "7.2", "7.5"]
---

# PCIE-048 — Build TLP, configuration and enumeration reference models

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-048 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [2.1 — Transaction Layer Overview](../specification/2/1/summary.md): direct pp. 43–44; follow child sections and PDF tables.
- [2.2 — Transaction Layer Protocol - Packet Definition](../specification/2/2/summary.md): direct pp. 47–47; follow child sections and PDF tables.
- [7.2 — PCI Express Configuration Mechanisms](../specification/7/2/summary.md): direct pp. 338–339; follow child sections and PDF tables.
- [7.5 — PCI-Compatible Configuration Registers](../specification/7/5/summary.md): direct pp. 349–349; follow child sections and PDF tables.

Primary ownership: 0 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement independent Python TLP header build and parse for memory, configuration, completion and message types with explicit byte order.
- [ ] Implement a root-complex enumeration sequence: configuration reads and writes, BAR sizing, capability walk, command enable and MSI programming.
- [ ] Evaluate cocotbext-pcie (MIT licence) as a TLP-level root complex and enumeration model; adopt it only where it is independent of DUT code, pin its version in the PCIE-002 environment and record which Rev1.1 rules it does not model.
- [ ] Expose a TLP-level interface that transaction-layer tickets can use before PHY and data-link integration, and through PCIE-047 for full-stack tests.

## pyuvm verification

- [ ] Round-trip a legal TLP matrix and compare with hand-built byte vectors carrying source citations.
- [ ] Run enumeration against a minimal Python configuration-space model and confirm BAR sizing and capability walk.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Transaction-layer tickets can test against TLP-level models without waiting for PHY/DLL integration.
- [ ] Any third-party model version, licence and coverage gaps are recorded.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
