# SKY130 implementation target

Status: **selected by the user, 2026-11-07.** The project targets the SkyWater SKY130 process with an on-chip PHY. This replaces the earlier Tang Nano 20K FPGA target, its external serializer architecture and the discrete-transistor board serializer plan; those documents are kept for history in [superseded/](superseded/). PCIE-003 freezes the details below with evidence; until then they are proposals.

## Scope

- **Process:** SkyWater SKY130 open PDK (Apache 2.0), standard-cell library `sky130_fd_sc_hd` by default. Pin the exact PDK commit (PCIE-050).
- **Digital flow:** OpenLane 2 (or LibreLane, its continuation) for RTL-to-GDS, running OpenROAD internally; standalone OpenROAD/OpenSTA for interactive work; Yosys synthesis with the SKY130 library.
- **Custom/analog flow:** xschem schematics, ngspice with SKY130 models, Magic layout and extraction, netgen LVS, KLayout DRC cross-checks.
- **Chip content:** one die with the digital endpoint core, the on-chip PMA ([PHY architecture](phy-architecture.md)), high-speed pads with ESD, a pad ring or harness, and slow test access including PHY-boundary loopback.
- **RTL rules:** technology-specific memories, synchronizers, reset synchronizers and clock gates sit behind the PCIE-051 wrappers. Mandatory endpoint behavior is never dropped to save area or close timing.

## Ticket map

| Area | Tickets |
|---|---|
| Profile, architecture, environment | PCIE-001, 002, 003, 004, 050 |
| Protocol stack and verification models | PCIE-005, 010–039, 042, 047, 048 |
| On-chip PHY | Building blocks 061 schematic → 062 layout → 045 qualification; 046 CDR feasibility; 059 bias/references/calibration; PLL and REFCLK receiver 063 → 064 → 049; TX 065 → 066 → 007; RX 067 → 068 → 008; 052 pads/ESD/package, 006/009/043 electrical limits, stimulus bridge and qualification |
| Digital implementation | PCIE-051 wrappers, 053 memories, 054 early hardening, 041 logic signoff, 055 physical hardening, 056 gate level and equivalence |
| Chip integration | PCIE-060 early PHY loopback top (intermediate milestone, co-simulation method), PCIE-040 mixed-signal top, 057 pad ring, harness, test access and fabrication route |
| Tapeout and silicon (conditional) | PCIE-058 tapeout package, 044 silicon bring-up and host interoperability |

## Milestones

1. **Verified digital core:** protocol stack through PCIE-042 against behavioral PMA models.
2. **PHY loopback top (PCIE-060):** hardened logical PHY with PMA placeholders and early cells, loopback traffic, floorplan and co-simulation method. Reached long before the full core; a candidate first test chip.
3. **Signed-off chip:** mixed-signal top (PCIE-040), chip top (PCIE-057) and electrical qualification (PCIE-043).
4. **Tapeout and silicon (conditional):** PCIE-058 and PCIE-044, only with explicit user approval.

## Digital-only fallback

If PCIE-045, 046, 049, 007 or 008 reject the on-chip PHY with quantitative evidence, the chip proceeds as a digital endpoint core with its PHY boundary exercised through on-chip loopback and slow test access. The fallback:

- keeps every mandatory protocol obligation and its verification;
- records the PHY rejection, the evidence and the electrical requirements left unmet, rather than hiding them;
- cannot be described as a working PCIe endpoint, since no host link is possible;
- is reported to the user when triggered; it is not a silent substitution.

## Evidence rules

- Record PDK commit, tool versions, flow configuration and exact commands for every run. Do not commit PDK installs, flow run directories or GDS outputs.
- Timing closes at every selected corner, or the failure and attempted optimizations are documented. Typical-corner results alone are not signoff.
- Custom cells are qualified on extracted layout, not schematic alone. SKY130 foundry models are the device-model authority; record model and corner names.
- Gate-level, equivalence and extracted-layout results are distinct from silicon measurements. No fabrication submission or cost is incurred without explicit user approval.
- Fabrication-route availability changes over time. [Fabrication routes](fabrication-routes.md) records what was available on 2026-11-07; PCIE-057 re-verifies before choosing.
- Machine limits (16 cores, 14 GB RAM observed on 2026-11-07) may constrain full-core runs; record resource failures as such, not as design failures.
