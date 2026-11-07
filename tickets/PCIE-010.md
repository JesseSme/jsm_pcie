---
id: PCIE-010
title: "Implement 8b/10b encoder and decoder with running disparity"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-004", "PCIE-005"]
spec_sections: ["4.2.1", "B"]
---

# PCIE-010 — Implement 8b/10b encoder and decoder with running disparity

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-010 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, ngspice netlists/models and PCB evidence as specified by the ticket.

## Source evidence

- [4.2.1 — Symbol Encoding](../specification/4/2/1/summary.md): direct pp. 162–162; follow child sections and PDF tables.
- [B — Symbol Encoding](../specification/B/summary.md): direct pp. 487–497; follow child sections and PDF tables.

Primary ownership: 4 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement synthesizable SV encoder/decoder using Appendix B tables and specified serial bit ordering.
- [ ] Track TX/RX disparity, K symbols, comma detection, invalid codes and disparity errors.
- [ ] Define reset disparity and error interface to LTSSM/data link.

## pyuvm verification

- [ ] Exhaustively test all 256 data values and legal K symbols under both running disparities against independent table model.
- [ ] Decode all 1024 codewords per disparity; verify illegal/disparity errors, round-trip and back-to-back updates.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Every Appendix B mapping agrees with reference; illegal codes cannot silently become valid data.
- [ ] Lint and synthesis confirm bounded combinational logic and timing target.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
