---
id: PCIE-035
title: "Implement reset domains and link-down cleanup"
status: todo
owner: null
branch: null
claimed_at: null
base_commit: null
priority: P1
gate: baseline
depends_on: ["PCIE-019", "PCIE-021", "PCIE-025", "PCIE-027", "PCIE-030"]
spec_sections: ["6.6", "2.9", "4.2.4.5"]
---

# PCIE-035 — Implement reset domains and link-down cleanup

## Agent handoff and scope

Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. Claim with `python3 tools/tickets.py claim PCIE-035 --agent <unique-agent-id>` before editing implementation. Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. Implement digital logic in synthesizable SystemVerilog; PHY circuits require schematics, layout, extracted ngspice results and macro abstracts as specified by the ticket.

## Source evidence

- [6.6 — PCI Express Reset - Rules](../specification/6/6/summary.md): direct pp. 316–319; follow child sections and PDF tables.
- [2.9 — Link Status Dependencies](../specification/2/9/summary.md): direct pp. 124–124; follow child sections and PDF tables.
- [4.2.4.5 — Reset](../specification/4/2/4/5/summary.md): direct pp. 174–174; follow child sections and PDF tables.

Primary ownership: 4 sections; [section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. Source references above also include shared prerequisites.

## Deliverables and behavior

- [ ] Implement Fundamental Reset/PERST# and Hot Reset with exact per-register sticky/retained/reset attributes.
- [ ] Synchronize deassertion per clock domain and gate activity while clocks/PHY are not ready.
- [ ] Flush or fail pending requests, retry entries, credits, interrupts and application state according to reset type.
- [ ] Define link-down software-visible outcomes independently of full core reset.

## pyuvm verification

- [ ] Assert resets at each LTSSM/DL phase and during config, MSI, replay and requester activity.
- [ ] Compare reset-value/retention matrix, ensure no stale completion and successful retraining afterward.
- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.

## ngspice verification

No ticket-local circuit simulation is required: these are protocol, control or planning rules. Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; ngspice cannot establish digital packet correctness.

## Acceptance criteria

- [ ] Every state element has a documented reset/retention owner.
- [ ] Random reset stress returns to enumerable operation without stale traffic.
- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.
- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.

## Evidence and handoff

Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.

## Claim history

No claims yet.
