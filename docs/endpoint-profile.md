# Proposed PCIe Gen1 x1 FPGA endpoint profile

User-confirmed scope: a complete **digital** PCIe endpoint, synthesizable SystemVerilog in an FPGA, initially one lane. The user has approved slower parallel FPGA I/O feeding external TX serialization and external RX clock recovery/deserialization; see the [accepted physical-interface decision](physical-interface-decision.md). pyuvm verifies digital behavior using the repository OSS CAD Suite; ngspice evaluates proposed pin-toggling circuits, signals and board/channel assumptions. The present change creates specifications and a backlog, not endpoint RTL.

Proposed defaults, to be frozen with cited requirements in PCIE-001:

| Area | Initial design decision |
|---|---|
| Hardware | User-selected Tang Nano 20K, GW2AR-LV18QN88C8/I7; [target and fallback policy](hardware-target.md) |
| Physical interface | Approved external serialization/CDR/deserialization; initial TX candidate is four 625 Mb/s streams into a clocked 4:1 serializer; parts and final parallel width require feasibility evidence |
| Serializer implementation | First plan/evaluate solderable discrete RF transistors under [construction plan](discrete-transistor-serializer-plan.md), PCIE-045 before PCIE-007; no packaged serializer is selected |
| Protocol | Supplied Base Rev. 1.1, Gen1 2.5 GT/s, x1, PCI Express Endpoint role (not legacy endpoint) |
| Functions | One function, Type0 configuration, 4KiB configuration address space with only implemented capabilities populated |
| Traffic | VC0, TC0; explicit unsupported TC policy; posted/non-posted/completion pools |
| Payload | Advertise 128-byte MPS initially; required request/completion handling still follows actual source rules |
| Resources | One proposed 4KiB, 64-bit non-prefetchable BAR using BAR0/BAR1; other BARs unused |
| Application | Small register/RAM target and generic memory requester interface; requester supports 64-bit addressing and BME gating |
| Interrupts | One-vector MSI; MSI-X omitted; decide any applicable legacy INTx policy from normative sources |
| Integrity | Mandatory DLLP CRC/LCRC/replay; optional ECRC and AER explicitly assessed in conditional tickets |
| Power | Required Rev1.1 L0s and software PCI-PM obligations; optional ASPM L1 assessed separately |
| Logical PHY | Proposed: two symbols, each with a K flag, per 125 MHz logical cycle (16-bit datapath) before 8b/10b serialization. One 8-bit symbol per 250 MHz cycle is unlikely to close timing on GW2AR-18 C8/I7 and needs synthesis evidence to keep. PCIE-001 freezes the width before any RTL, because changing it later affects framing, CRC, DLLP and ordered-set logic in every layer |
| Reference clock | Proposed: derive the TX bit clock, CDR reference and FPGA gearbox clocks from the host 100 MHz REFCLK. Section 4.3.1.1 requires both link ends within 600 ppm, which a free-running local oscillator cannot meet against a spread-spectrum host. PCIE-001 freezes the policy; PCIE-003 owns the clock architecture |
| Simulator | OSS CAD Suite Verilator primary; pyuvm through cocotb, with independent Python reference models |
| Electrical | ngspice transient models with nonideal I/O, package, channel and load; model confidence and measurement points recorded |

The FPGA/board target is now selected. Exact board revision, usable pins/bank rails, clock routing, resource fit and full-duplex physical feasibility still require verification. If the core cannot fit after documented optimization, the user authorizes the complete board-independent digital core with Tang Nano 20K/GW2AR I/O specifications retained as the electrical simulation reference. See [hardware target](hardware-target.md) for the decision and evidence rules. **400 ps per serial bit** follows from 2.5 GT/s. After 8b/10b, nominal decoded capacity is 2 Gb/s (250 MB/s) per direction before protocol overhead. This is a full-duplex link with a separate receive pair, not just a clock output.

A fast clock alone does not serialize arbitrary data at that rate. Passive modulation cannot add missing independent data throughput; an active external multiplexer/interleaver would itself need adequate switching bandwidth, timing, electrical levels and power-up behavior. The receive path also needs data recovery, symbol alignment and suitable termination. These are feasibility questions, not assumed working solutions. PCIE-003/007/008 require quantitative experiments and can reject ordinary-I/O candidates.

As external architectural reference, Altera's [PCI Express transceiver documentation](https://docs.altera.com/r/docs/683621/current/l-and-h-tile-transceiver-phy-user-guide/pci-express-pipe) describes a fabric MAC/data-link/transaction layer with transceiver PHY at the Gen1 rate. For the selected target, use [Gowin DS226](https://cdn.gowinsemi.com.cn/DS226E.pdf) rather than importing another vendor's capabilities: its documented 8/10-bit I/O gearbox limit is 1.2 Gb/s, below Gen1. External serialization/recovery remains an experiment requiring evidence.

The digital architecture keeps the PMA boundary explicit so protocol implementation can proceed against a behavioral PHY while external serialization and receive-circuit experiments run. Scrambling and 8b/10b remain in the FPGA. Native transceivers or an external PHY that absorbs logical-PHY functions would change this approved partition and need a separate recorded architecture decision. Do not silently replace the intended implementation with a hard endpoint IP core.

Verification is split by what each tool can establish. pyuvm checks symbols, packets, credit/ordering/replay conservation, configuration, interrupts, errors, reset and power behavior. Digital pattern manifests supply ngspice stimuli; ngspice checks modeled waveform limits and circuit feasibility. Ideal voltage sources, a plotted eye, or a short error-free waveform cannot demonstrate hardware BER or full PCIe compliance. PCIE-043/044 require model qualification, measurements and host interoperability.

Environment observed during planning: `oss-cad-suite/bin/verilator` reports 5.055 development; Icarus reports 14.0 development; ngspice is at `/usr/bin/ngspice`. Tool binaries were inspected, but no endpoint or pyuvm regression has yet run. PCIE-002 establishes a reproducible compatible Python/cocotb/pyuvm environment rather than assuming the project's Python requirement matches bundled simulator libraries.

The Base specification references companion definitions for PCI configuration, MSI, PCI-PM and physical form factors. These files were not supplied separately. Relevant tickets must obtain or identify authoritative definitions and leave unresolved rules explicit rather than inventing register layouts or board requirements.
