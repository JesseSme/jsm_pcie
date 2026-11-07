# SKY130 implementation target

Status: **selected by the user, 2026-11-07.** The project targets the SkyWater SKY130 process with an on-chip PHY. **The deliverable is a fully verified ASIC core** (digital core plus PHY macros, signed off as one hard macro), **not a taped-out chip**. This replaces the earlier Tang Nano 20K FPGA target, its external serializer architecture and the discrete-transistor board serializer plan; those documents are kept for history in [superseded/](superseded/). PCIE-003 freezes the details below with evidence; until then they are proposals.

## Scope

- **Process:** SkyWater SKY130 open PDK (Apache 2.0), standard-cell library `sky130_fd_sc_hd` by default. Pin the exact PDK commit (PCIE-050).
- **Digital flow:** OpenLane 2 (or LibreLane, its continuation) for RTL-to-GDS, running OpenROAD internally; standalone OpenROAD/OpenSTA for interactive work; Yosys synthesis with the SKY130 library.
- **Custom/analog flow:** xschem schematics, ngspice with SKY130 models, Magic layout and extraction, netgen LVS, KLayout DRC cross-checks.
- **Core content:** the digital endpoint core and the on-chip PMA macros ([PHY architecture](phy-architecture.md)) integrated as one hard macro with PMA loopback and status visibility. Pads, ESD and the pad ring are outside the core; PCIE-052 models them as the environment the core must work in, and the integration guide states the limits an integrator must meet.
- **Out of scope:** tapeout, fabrication, packaging, test boards, silicon measurement and host interoperability on hardware.
- **RTL rules:** technology-specific memories, synchronizers, reset synchronizers and clock gates sit behind the PCIE-051 wrappers. Mandatory endpoint behavior is never dropped to save area or close timing.

## Ticket map

| Area | Tickets |
|---|---|
| Profile, architecture, environment | PCIE-001, 002, 003, 004, 050 |
| Protocol stack and verification models | PCIE-005, 010–039, 042, 047, 048 |
| On-chip PHY | Building blocks 061 schematic → 062 layout → 045 qualification; 046 CDR feasibility; 059 bias/references/calibration; PLL and REFCLK receiver 063 → 064 → 049; TX 065 → 066 → 007; RX 067 → 068 → 008; 052 pad/ESD/package/channel models, 006/009/043 electrical limits, stimulus bridge and qualification |
| Digital implementation | PCIE-051 wrappers, 053 memories, 054 early hardening, 041 logic signoff, 055 physical hardening, 056 gate level and equivalence |
| Core integration and signoff | PCIE-060 early PHY loopback top (intermediate milestone, co-simulation method), PCIE-040 integrated core macro, PCIE-058 signoff and integration package (the deliverable) |

## Milestones

1. **Verified digital core:** protocol stack through PCIE-042 against behavioral PMA models.
2. **PHY loopback top (PCIE-060):** hardened logical PHY with PMA placeholders and early cells, loopback traffic, floorplan and co-simulation method. Reached long before the full core.
3. **Verified ASIC core (the goal):** integrated core macro (PCIE-040), electrical qualification (PCIE-043), gate-level and equivalence (PCIE-056) and the signoff and integration package (PCIE-058).

## Digital-only fallback

If PCIE-045, 046, 049, 007 or 008 reject the on-chip PHY with quantitative evidence, the deliverable becomes the verified digital endpoint core with its PHY interface and behavioral PMA model. The fallback:

- keeps every mandatory protocol obligation and its verification;
- records the PHY rejection, the evidence and the electrical requirements left unmet, rather than hiding them;
- cannot be described as a working PCIe endpoint, since no host link is possible;
- is reported to the user when triggered; it is not a silent substitution.

## Evidence rules

- Record PDK commit, tool versions, flow configuration and exact commands for every run. Do not commit PDK installs, flow run directories or GDS outputs.
- Timing closes at every selected corner, or the failure and attempted optimizations are documented. Typical-corner results alone are not signoff.
- Custom cells are qualified on extracted layout, not schematic alone. SKY130 foundry models are the device-model authority; record model and corner names.
- Gate-level, equivalence and extracted-layout results are distinct from silicon measurements; the signoff package lists what cannot be verified without silicon. Tapeout is out of scope and no fabrication cost is incurred.
- Machine limits (16 cores, 14 GB RAM observed on 2026-11-07) may constrain full-core runs; record resource failures as such, not as design failures.
