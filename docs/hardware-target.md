# Tang Nano 20K hardware target and I/O-reference fallback

User-selected target: **Sipeed Tang Nano 20K**, with **GW2AR-LV18QN88C8/I7**. If the complete digital core cannot fit, the user authorizes continuing with this device's I/O specifications as the electrical reference while the complete SystemVerilog core remains board-independent. Board selection is resolved; fit and link feasibility are not yet established.

The user has also approved the [external serialization architecture](physical-interface-decision.md): parallel FPGA I/O, external TX serialization and external RX clock recovery/deserialization. The initial TX candidate uses four streams at 625 Mb/s; the exact components and parallel width remain subject to feasibility checks. Direct Gen1 transmission through a single FPGA I/O pair is not the implementation plan.

The [Sipeed board description](https://wiki.sipeed.com/hardware/en/tang/tang-nano-20k/nano-20k.html) identifies the FPGA, 20,736 LUT4s, 15,552 flip-flops, 46 BSRAM blocks, two PLLs, a 27 MHz oscillator and an MS5351 clock generator. These are planning constraints, not an achieved resource/timing result. Record exact part marking and board revision before assigning pins.

Primary references checked on 2026-11-07:

- [Gowin DS226-2.7E, 2026-07-31](https://cdn.gowinsemi.com.cn/DS226E.pdf): I/O modes in section 2.4, DC limits in section 3.3, gearbox rates in Table 3-17 (printed p.37, PDF p.46), and PLL limits in section 3.4.7. Archive the version/hash used when building models; the URL may change revision.
- [Gowin GW2AR documentation index](https://www.gowinsemi.com/en/document/main/database/1846/): obtain package-specific UG115/UG229 pinout data and applicable I/O primitive documentation.
- [Sipeed schematic directory](https://dl.sipeed.com/shareURL/TANG/Nano_20K/2_Schematic) and [board datasheet directory](https://dl.sipeed.com/shareURL/TANG/Nano_20K/1_Datasheet): retrieve the actual board-revision documents before identifying bank rails, shared peripherals, connector pairs, loading or routing. Their download-directory listings were not sufficient to verify these details during this update.

The device datasheet lists maximum 1:8/1:10 receive and 8:1/10:1 transmit gearbox rates of **1200 Mbps**. Gen1 needs **2500 Mbps per direction**. Therefore direct single-pair operation at Gen1 rate exceeds the documented gearbox rate. This comparison does not prove an external serializer/deserializer architecture impossible; it makes that architecture a separate full-duplex feasibility study. Multiple slower FPGA pins can supply an external serializer only if data throughput, pin availability, phase alignment, electrical levels and timing all check out. A fast clock output cannot replace these requirements.

Spec section 4.3.1.1 requires both link ends to transmit within 600 ppm of each other. Against a host using spread-spectrum clocking, the board's 27 MHz oscillator or MS5351 cannot meet this as a free-running source, so the default plan derives transmit and gearbox clocks from the host 100 MHz REFCLK (PCIE-001 policy, PCIE-003 architecture). The bundled open Gowin flow (yosys, nextpnr-himbaechel, gowin_pack) is exercised in PCIE-002 and used for fit in PCIE-041.

Do not assume an on-chip PCIe transceiver, recovered clock, PCIe-capable 100 MHz reference path or accessible suitable differential pair from the presence of HDMI, a clock generator or an LVDS mode. DS226's `PCI` I/O-standard name is not evidence of PCI Express support. Verify the exact primitive, package and schematic. Model finite FPGA slew, skew, supported rates and electrical levels in ngspice; ideal sources at unsupported rates are not a device model.

Two distinct outcomes are permitted:

| Outcome | Required evidence | Completion boundary |
|---|---|---|
| Board implementation | Synthesis and routed fit/timing on the selected part, valid pin/clock assignments, viable external circuitry where needed, passing digital/electrical checks and real host tests | PCIE-040 and PCIE-044 must execute their hardware checks |
| I/O-reference fallback after core fit failure | Reproducible failed-fit reports, attempted resource/pipeline optimizations, reviewed fit decision, complete board-independent digital verification and device-constrained electrical models | PCIE-040/044 may receive signed not-applicable hardware dispositions; missing bitstream/host measurements remain explicitly unperformed |

PCIE-041 records the fit decision. Tool setup problems are not proof of insufficient FPGA resources. Fallback cannot remove mandatory endpoint features or assume faster FPGA I/O; it does not waive any Gen1 signaling requirement. If external circuitry cannot satisfy TX/RX electrical requirements, report that result as infeasible rather than calling the simulated design a working physical endpoint. No alternate FPGA is selected automatically.

PCIE-003 owns target/pin/PHY feasibility, PCIE-006 the limit/model table, PCIE-007/008 TX/RX experiments, PCIE-009 the waveform bridge, PCIE-041 resource/timing fit, and PCIE-043 final electrical evidence. Native hardware tests remain conditional on a viable fit and physical interface.
