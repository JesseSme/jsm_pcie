# Proposed PCIe Gen1 x1 SKY130 endpoint profile

User-confirmed scope: a complete PCI Express **Gen1 x1 endpoint** implemented on the **SkyWater SKY130** process. A synthesizable SystemVerilog digital core (transaction layer, data link layer and logical PHY) is hardened with OpenLane/OpenROAD, and an **on-chip SKY130 PHY** (PLL, serializer, transmitter, receiver, clock and data recovery, deserializer) is designed at transistor level on the same die. See [ASIC target](asic-target.md) and [PHY architecture](phy-architecture.md). pyuvm verifies digital behavior using the repository OSS CAD Suite; ngspice with SKY130 models evaluates the PHY circuits. The present change creates specifications and a backlog, not endpoint RTL or circuits.

Proposed defaults, to be frozen with cited requirements in PCIE-001 and PCIE-003:

| Area | Initial design decision |
|---|---|
| Process | SkyWater SKY130 open PDK, `sky130_fd_sc_hd` standard cells by default; exact PDK commit pinned in PCIE-050 |
| Implementation flow | OpenLane 2 (or LibreLane) with OpenROAD for the digital core; Magic, KLayout, netgen and xschem for custom PHY cells |
| Physical layer | On-chip SKY130 PMA: PLL from 100 MHz REFCLK, serializer and TX driver with de-emphasis, electrical idle and receiver detection; RX termination, CDR, deserializer and idle detection. Digital-only fallback if the PHY is rejected with evidence |
| PHY method | Transistor-level building blocks qualified first (PCIE-045), CDR feasibility before layout (PCIE-046), then PLL/TX/RX integration (PCIE-049/007/008) |
| Protocol | Supplied Base Rev. 1.1, Gen1 2.5 GT/s, x1, PCI Express Endpoint role (not legacy endpoint) |
| Functions | One function, Type0 configuration, 4KiB configuration address space with only implemented capabilities populated |
| Traffic | VC0, TC0; explicit unsupported TC policy; posted/non-posted/completion pools |
| Payload | Advertise 128-byte MPS initially; required request/completion handling still follows actual source rules |
| Resources | One proposed 4KiB, 64-bit non-prefetchable BAR using BAR0/BAR1; other BARs unused |
| Application | Small register/RAM target and generic memory requester interface; requester supports 64-bit addressing and BME gating |
| Interrupts | One-vector MSI; MSI-X omitted; decide any applicable legacy INTx policy from normative sources |
| Integrity | Mandatory DLLP CRC/LCRC/replay; optional ECRC and AER explicitly assessed in conditional tickets |
| Power | Required Rev1.1 L0s and software PCI-PM obligations; optional ASPM L1 assessed separately |
| Logical PHY | Proposed: two symbols, each with a K flag, per 125 MHz cycle (16-bit datapath), giving 20 encoded bits per cycle to the serializer. One 8-bit symbol per 250 MHz cycle is unlikely to close timing in SKY130 standard cells at the slow corner and needs synthesis evidence to keep. PCIE-001 freezes the width before any RTL |
| Reference clock | Proposed: the on-chip PLL derives serializer, CDR-reference and digital clocks from the host 100 MHz REFCLK. Section 4.3.1.1 requires both link ends within 600 ppm, which a free-running local oscillator cannot meet against a spread-spectrum host |
| Simulator | OSS CAD Suite Verilator primary; pyuvm through cocotb, with independent Python reference models |
| Electrical | ngspice with pinned SKY130 models on schematic and extracted layout, with pad, package and channel models; model confidence and measurement points recorded |

**400 ps per serial bit** follows from 2.5 GT/s. After 8b/10b, nominal decoded capacity is 2 Gb/s (250 MB/s) per direction before protocol overhead. This is a full-duplex link with a separate receive pair. The PHY is the main technical risk: SKY130 is a 130 nm process, so current-mode logic, careful clocking and extracted-layout simulation are expected to be necessary for the 2.5 Gb/s stages. These are feasibility questions; PCIE-045/046/049/007/008 can reject the on-chip PHY with evidence, which triggers the digital-only fallback described in [ASIC target](asic-target.md).

The digital architecture keeps the PMA boundary explicit so protocol implementation proceeds against a behavioral PMA model while the analog work runs. Scrambling and 8b/10b stay in the digital core and happen exactly once. Do not substitute a third-party hard PCIe IP block for the planned core.

Verification is split by what each tool can establish. pyuvm checks symbols, packets, credit/ordering/replay conservation, configuration, interrupts, errors, reset and power behavior. Digital pattern manifests supply ngspice stimuli; ngspice checks modeled waveform limits and circuit feasibility. Ideal voltage sources, a plotted eye, or a short error-free waveform cannot demonstrate silicon BER or PCIe compliance. PCIE-043/044 separate modeled results from silicon measurements and host interoperability.

Environment observed during planning: `oss-cad-suite/bin/verilator` reports 5.055 development; Icarus reports 14.0 development; ngspice is `/usr/bin/ngspice` (ngspice-47). Docker and Podman are present; the SKY130 PDK, OpenLane, OpenROAD, Magic, KLayout, netgen and xschem are not yet installed (PCIE-050). No endpoint or pyuvm regression has run yet.

The Base specification references companion definitions for PCI configuration, MSI, PCI-PM and physical form factors. These files were not supplied separately. Relevant tickets must obtain or identify authoritative definitions and leave unresolved rules explicit rather than inventing register layouts or board requirements.
