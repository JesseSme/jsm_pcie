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

## SKY130 ASIC track, 2026-11-07

At the user's request, an additive ASIC track was planned in `docs/asic-target.md` and tickets PCIE-049 to PCIE-058 (SkyWater SKY130 PDK, OpenLane 2/LibreLane, OpenROAD, Magic/KLayout/netgen). PCIE-052 (on-chip PHY), PCIE-057 (harness and fabrication route) and PCIE-058 (tapeout) are conditional. PCIE-013 and PCIE-021 now depend on PCIE-051 portable wrappers. The key open question for PCIE-049 is the ASIC physical interface, because SKY130 general-purpose pads are expected to be far slower than the FPGA route's 625 Mb/s streams. No ASIC tools were installed by this planning change: Docker and Podman were present; Nix, OpenROAD, OpenLane, Magic, netgen, KLayout and xschem were not. `tickets.py check` passed for 58 tickets; the 498 section summaries were unchanged.

## Retarget to SKY130 with an on-chip PHY, 2026-11-07

At the user's direction the FPGA target was dropped and the project now targets the SkyWater SKY130 process. Asked where the 2.5 Gb/s circuits should live, the user chose an on-chip SKY130 PHY with a digital-only fallback. `tools/pcie_plan.py` was rewritten as a single-layer plan (previous layered version and tickets backed up outside the repository before the change); ticket IDs were kept so protocol tickets 005 and 010–039, 042, 047 and 048 keep their numbers. Repurposed tickets: PCIE-003 chip architecture, clocking and pins; 007 on-chip TX; 008 on-chip RX/CDR; 040 mixed-signal top; 041 lint/synthesis/CDC signoff in SKY130; 043 on-chip electrical qualification; 044 silicon bring-up (conditional); 045 SKY130 transistor-level building blocks; 046 on-chip CDR feasibility; 049 PLL; 052 high-speed pads, ESD and package; 057 chip top (now baseline). New docs: `asic-target.md` (rewritten) and `phy-architecture.md`; the Tang Nano 20K, external-serializer and discrete-transistor documents moved to `docs/superseded/` with a banner. `tickets.py check` passed for 58 tickets with no residual FPGA references in generated tickets.

## Soundness-review fixes, 2026-11-07

A review of the retargeted plan found structural gaps, which were fixed in `tools/pcie_plan.py` before any ticket was claimed:

- PCIE-003 sets the PHY architecture and PCIE-004 now depends on it and owns the detailed digital-to-PMA contract (previously both defined it).
- Missing dependencies added: PCIE-007 on PCIE-052 (pad/package loads); PCIE-007/008/049 on new PCIE-059; PCIE-042 on PCIE-033/034/037 so optional-feature decisions gate coverage closure. PCIE-017/031 now keep N_FTS, Extended Synch and L0s exit latency as parameters that PCIE-040 binds to the receive relock budget.
- PCIE-001 now classifies applicability per section; candidate-level requirement review belongs to each section's primary-owner ticket.
- New PCIE-059 (bias, references, termination calibration) and PCIE-060 (early PHY loopback top, co-simulation method, intermediate milestone at dependency depth 8 instead of 20 for the full mixed-signal top).
- REFCLK input receiver assigned to PCIE-049, with the CEM specification recorded as a required input; off-chip AC-coupling capacitors and other board parts recorded in PCIE-003; the beacon-versus-WAKE# decision moved to PCIE-003 for both PCIE-017 and PCIE-007; ticket template no longer mentions PCB evidence.

`tickets.py check` passes for 60 tickets; a dependency scan shows no remaining backward references other than intended forward hand-offs.

## Analog ticket split and fabrication-route check, 2026-11-07

The four large analog tickets were split into schematic, layout/extraction and qualification phases. The original IDs remain the final qualification and macro-delivery tickets so downstream dependencies are unchanged: building blocks 061 → 062 → 045, PLL and REFCLK receiver 063 → 064 → 049, TX 065 → 066 → 007, RX 067 → 068 → 008. Layout tickets deliver preliminary abstracts to the PCIE-060 loopback top.

Fabrication routes were checked against primary sources and recorded in `docs/fabrication-routes.md`: ChipFoundry chipIgnite (next commitment 2027-03-20 for CI2705; Caravel, Caravan with bare pads, OpenFrame), Cadence's SKY130 aggregation (custom pad ring, bare die, no run after the 2026-01-16 deadline published), SkyWater direct MPW and Tiny Tapeout. PCIE-003, 050, 052, 057 and 058 now reference those findings. `tickets.py check` passes for 68 tickets.
