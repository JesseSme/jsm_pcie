# Planning validation

The planning artifacts were checked locally on 2026-11-07. No endpoint RTL was implemented, no endpoint pyuvm regression was executed, and no candidate FPGA circuit was qualified in ngspice. Those are work items in the backlog.

| Check | Result |
|---|---|
| `python3 tools/deconstruct_spec.py --check` | PASS: all 498 section fragments reconstruct the supplied TXT exactly; original TXT/PDF hashes match; hierarchy and 257 TOC page anchors agree |
| `python3 tools/tickets.py check` | PASS: 45 tickets after the discrete-transistor planning refinement, required metadata/source links/handoff fields and acyclic dependencies |
| `python3 tools/tickets.py ready` | PCIE-001 and PCIE-002 are the initial ready tasks |
| Markdown local-link scan | PASS: generated specification, ticket, profile and navigation targets exist |
| Traceability cross-check | PASS: all 498 sections and all 637 unique keyword candidate IDs have primary ticket assignments; no candidate is duplicated or missing |
| Heading review | PASS: sibling numbering is consecutive; wrapped titles are preserved; title parentheses balance |
| Isolated temporary Git claim exercise | PASS: successful claim signs metadata/history and creates correct branch; unmet dependencies and duplicate claims fail; failed branch creation restores ticket; operation releases lock |
| `graphify update .` | PASS after excluding bundled toolchain with `.graphifyignore`; graph/report/HTML regenerated. Graphify warned that optional `pypdf` was unavailable; chapter extraction uses the supplied TXT and does not depend on it |

The first graph update was stopped because it scanned the bundled OSS CAD Suite. The final update completed with the toolchain excluded. Initial planning tickets remain unclaimed and `todo`; the claim exercise used a disposable repository under `/tmp` and did not create a branch or commit in this repository.

These checks establish document preservation, navigation, traceability and ticket-tool behavior. They do not constitute normative review of every extracted candidate, verification of the future endpoint, or proof that ordinary FPGA I/O can support a complete 2.5 GT/s link. The tickets explicitly require that further work and its evidence.

After the user selected Tang Nano 20K, the profile, agent instructions, authored backlog and generated tickets were updated together. Ticket metadata/dependency checks, exact source reconstruction and local-link checks passed again. Additional checks confirmed PCIE-040/044 are conditional on the hardware route, PCIE-040 depends on the PCIE-041 fit decision, and all affected ticket ownership/status fields remain unclaimed/todo. The selected-board I/O rates were checked in manufacturer DS226-2.7E; actual board revision, schematic pin/rail details, synthesis fit and electrical simulations remain future ticket work.

The user subsequently accepted external TX serialization and RX clock recovery/deserialization as the physical-interface direction. The accepted decision is in `physical-interface-decision.md`; profile, AGENTS.md and the authored/generated tickets agree. Checks passed for exact source reconstruction, ticket dependencies, local links, retained hardware fallback gates and unchanged ticket ownership. The backlog now explicitly tests interleaving across 10-bit symbol boundaries and requires external serializer clock/capture timing. Four 625 Mb/s TX streams are the initial feasibility candidate; no component, schematic or electrical test result has been approved by this planning update.

The next user refinement requires a solderable discrete-transistor plan first. `discrete-transistor-serializer-plan.md` supplies the construction sequence, transistor topology proposal, clock/retiming requirements, model requirements, staged coupon layout/assembly plan and pyuvm/ngspice checks. PCIE-045 was added before PCIE-007 full integration; PCIE-003 establishes interface constraints before cell qualification. The 45-ticket dependency graph and exact source reconstruction pass. No transistor schematic, simulation or PCB has yet been implemented; device candidates remain subject to model and circuit qualification.

## Pre-implementation review update, 2026-11-07

A review before implementation added the following to the authored plan in `tools/pcie_plan.py`; tickets were regenerated while none were claimed.

- PCIE-001 now freezes the fabric datapath width and logical clock (proposed 16 bits at 125 MHz instead of 8 bits at 250 MHz) and the reference-clock/SSC policy (section 4.3.1.1, 600 ppm) before RTL starts, and checks what sections 7.5–7.7 already define before treating companion specifications as missing.
- PCIE-002 adds a uv-managed cocotb/pyuvm environment and a Tang Nano 20K smoke build with the bundled open Gowin flow. PCIE-003 owns the reference-clock architecture, derived FPGA clocks and a full board pin budget. PCIE-012 adds an early Fmax check; PCIE-041 uses the open flow, cross-checked with vendor timing where needed.
- New PCIE-046 assesses RX clock-recovery feasibility, including relock time against N_FTS/L0s (section 4.2.4.3), before TX parts are bought or coupons fabricated. PCIE-007/008 depend on it; PCIE-017/031 bound advertised N_FTS and L0s exit latency by its budget.
- PCIE-005 is narrowed to the shared pyuvm framework, symbol-level agent and 8b/10b/scrambler models. New PCIE-047 (DLLP, CRC, ACK/NAK replay and flow-control partner) and PCIE-048 (TLP, configuration and enumeration models, with a cocotbext-pcie evaluation) carry the rest; PCIE-018 now depends on PCIE-012/047 and PCIE-022 on PCIE-048.
- Workflow: `tools/tickets.py claim` now commits only the signed ticket on `main` before branching and refuses to run off `main`; `done` means reviewed and merged into `main`. Validation uses explicit checks that survive `python -O`, and `tools/build_pcie_plan.py` refuses to overwrite reviewed traceability rows.

Regeneration left all 498 section summaries byte-identical; `TRACEABILITY.csv` changed only in its `related_tickets` column. The claim flow was exercised in a disposable repository: claim committed on `main`, branch created, and refusals for unmet dependencies, duplicate claims, off-`main` claims, existing branches and tracked changes.

## Public-repository hygiene, 2026-11-07

Because the GitHub repository is public, the PCI-SIG PDF/TXT, all spec-derived text in `specification/` and `graphify-out/` are git-ignored; only `specification/README.md`, `INDEX.md`, `manifest.json` and `TRACEABILITY.csv` (metadata) remain tracked. The pushed history was checked and contains only `README.md`, so no specification content had been published. `tools/tickets.py check` now validates section references against `manifest.json`, `tools/deconstruct_spec.py` reports missing local sources clearly, and `tools/build_pcie_plan.py --summaries-only` rebuilds local summaries without touching tickets. A simulated fresh clone passed `tickets.py check`; `--summaries-only` reproduced all 498 summaries byte-identically.
