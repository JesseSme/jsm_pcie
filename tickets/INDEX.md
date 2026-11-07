# Ticket index

Generated initial backlog; no tickets are claimed or implemented. See [workflow](README.md).

| Ticket | Gate | Dependencies |
|---|---|---|
| [PCIE-001 — Freeze endpoint profile and audit normative applicability](PCIE-001.md) | baseline | none |
| [PCIE-002 — Reproduce OSS CAD Suite, pyuvm and ngspice tool environment](PCIE-002.md) | baseline | none |
| [PCIE-003 — Freeze SKY130 chip architecture, clocking, pins and PHY partition](PCIE-003.md) | baseline | PCIE-001, PCIE-002 |
| [PCIE-004 — Create PHY boundary and cycle-accurate simulation contract](PCIE-004.md) | baseline | PCIE-001, PCIE-003 |
| [PCIE-005 — Build pyuvm framework, symbol-level root-port agent and PHY reference models](PCIE-005.md) | baseline | PCIE-002, PCIE-004 |
| [PCIE-006 — Extract electrical limits and ngspice model assumptions](PCIE-006.md) | baseline | PCIE-001, PCIE-002, PCIE-050 |
| [PCIE-007 — Design on-chip SKY130 TX serializer and PCIe transmitter](PCIE-007.md) | baseline | PCIE-003, PCIE-006, PCIE-045, PCIE-046, PCIE-049, PCIE-052, PCIE-059 |
| [PCIE-008 — Design on-chip SKY130 receiver, clock and data recovery and deserializer](PCIE-008.md) | baseline | PCIE-003, PCIE-006, PCIE-045, PCIE-046, PCIE-049, PCIE-059 |
| [PCIE-009 — Bridge digital patterns to ngspice and produce electrical evidence](PCIE-009.md) | baseline | PCIE-005, PCIE-006 |
| [PCIE-010 — Implement 8b/10b encoder and decoder with running disparity](PCIE-010.md) | baseline | PCIE-004, PCIE-005 |
| [PCIE-011 — Implement scrambling and descrambling](PCIE-011.md) | baseline | PCIE-004, PCIE-005 |
| [PCIE-012 — Implement symbol framing and ordered-set parser/generator](PCIE-012.md) | baseline | PCIE-010, PCIE-011 |
| [PCIE-013 — Implement clock domains, elastic buffering and SKP compensation](PCIE-013.md) | baseline | PCIE-004, PCIE-012, PCIE-051 |
| [PCIE-014 — Implement LTSSM Detect and Polling](PCIE-014.md) | baseline | PCIE-004, PCIE-012 |
| [PCIE-015 — Implement LTSSM x1 Configuration and reach L0](PCIE-015.md) | baseline | PCIE-014, PCIE-013 |
| [PCIE-016 — Implement Recovery, Disabled, Loopback, Hot Reset and compliance modes](PCIE-016.md) | baseline | PCIE-015 |
| [PCIE-017 — Implement PHY L0s, L1 and L2 state behavior](PCIE-017.md) | baseline | PCIE-016 |
| [PCIE-018 — Implement DLLP codec and CRC16](PCIE-018.md) | baseline | PCIE-012, PCIE-047 |
| [PCIE-019 — Implement Data Link state and flow-control initialization](PCIE-019.md) | baseline | PCIE-015, PCIE-018 |
| [PCIE-020 — Implement LCRC, receive sequence checks and ACK/NAK policy](PCIE-020.md) | baseline | PCIE-018, PCIE-019 |
| [PCIE-021 — Implement transmit retry buffer and replay controller](PCIE-021.md) | baseline | PCIE-018, PCIE-019, PCIE-051 |
| [PCIE-022 — Implement TLP header codec and validation](PCIE-022.md) | baseline | PCIE-048 |
| [PCIE-023 — Implement receive classification and unsupported/malformed handling](PCIE-023.md) | baseline | PCIE-022, PCIE-020 |
| [PCIE-024 — Implement completer, read splitting and byte-enable semantics](PCIE-024.md) | baseline | PCIE-022, PCIE-023 |
| [PCIE-025 — Implement requester tags, completion matching and timeout](PCIE-025.md) | baseline | PCIE-022, PCIE-024 |
| [PCIE-026 — Implement VC0 credits and transaction ordering](PCIE-026.md) | baseline | PCIE-019, PCIE-021, PCIE-022 |
| [PCIE-027 — Implement configuration Type0 header and BAR decoding](PCIE-027.md) | baseline | PCIE-023, PCIE-024 |
| [PCIE-028 — Implement PCI Express capability registers and live status](PCIE-028.md) | baseline | PCIE-027, PCIE-016, PCIE-026 |
| [PCIE-029 — Implement MSI generation and interrupt configuration](PCIE-029.md) | baseline | PCIE-025, PCIE-027 |
| [PCIE-030 — Implement required PCI-PM capability and device power states](PCIE-030.md) | baseline | PCIE-017, PCIE-018, PCIE-027 |
| [PCIE-031 — Implement required ASPM L0s and conditional L1](PCIE-031.md) | baseline | PCIE-017, PCIE-028, PCIE-030 |
| [PCIE-032 — Implement baseline error reporting and poisoned-data policy](PCIE-032.md) | baseline | PCIE-020, PCIE-021, PCIE-023, PCIE-025, PCIE-028 |
| [PCIE-033 — Assess optional ECRC generation and checking](PCIE-033.md) | conditional | PCIE-022, PCIE-032 |
| [PCIE-034 — Assess optional AER and extended capability space](PCIE-034.md) | conditional | PCIE-028, PCIE-032 |
| [PCIE-035 — Implement reset domains and link-down cleanup](PCIE-035.md) | baseline | PCIE-019, PCIE-021, PCIE-025, PCIE-027, PCIE-030 |
| [PCIE-036 — Build endpoint memory application and request interface](PCIE-036.md) | baseline | PCIE-024, PCIE-025, PCIE-027 |
| [PCIE-037 — Disposition out-of-profile topology and optional capabilities](PCIE-037.md) | baseline | PCIE-001, PCIE-027, PCIE-028 |
| [PCIE-038 — Implement endpoint system messages and slot power-limit handling](PCIE-038.md) | baseline | PCIE-022, PCIE-023, PCIE-028, PCIE-030, PCIE-032 |
| [PCIE-039 — Integrate endpoint top and run enumeration-to-MMIO regression](PCIE-039.md) | baseline | PCIE-016, PCIE-026, PCIE-028, PCIE-029, PCIE-030, PCIE-031, PCIE-032, PCIE-035, PCIE-036, PCIE-038 |
| [PCIE-040 — Integrate PHY macros and digital core into the mixed-signal top](PCIE-040.md) | baseline | PCIE-007, PCIE-008, PCIE-049, PCIE-055, PCIE-059, PCIE-060 |
| [PCIE-041 — Run lint, synthesis, CDC and reset signoff for the integrated core](PCIE-041.md) | baseline | PCIE-039, PCIE-050, PCIE-051 |
| [PCIE-042 — Close digital protocol coverage and stress recovery](PCIE-042.md) | baseline | PCIE-039, PCIE-041, PCIE-033, PCIE-034, PCIE-037 |
| [PCIE-043 — Qualify electrical path across corners and expose limits of simulation](PCIE-043.md) | baseline | PCIE-007, PCIE-008, PCIE-009, PCIE-040, PCIE-049, PCIE-052 |
| [PCIE-044 — Validate silicon bring-up and host interoperability](PCIE-044.md) | conditional | PCIE-058 |
| [PCIE-045 — Qualify SKY130 transistor-level PHY building blocks first](PCIE-045.md) | baseline | PCIE-003, PCIE-006, PCIE-009, PCIE-050 |
| [PCIE-046 — Assess on-chip CDR feasibility and lock-time budget before PHY layout](PCIE-046.md) | baseline | PCIE-003, PCIE-006, PCIE-050 |
| [PCIE-047 — Build data-link partner models: DLLP, CRC, ACK/NAK replay and flow control](PCIE-047.md) | baseline | PCIE-005 |
| [PCIE-048 — Build TLP, configuration and enumeration reference models](PCIE-048.md) | baseline | PCIE-005 |
| [PCIE-049 — Design on-chip PLL and clock distribution from the 100 MHz reference](PCIE-049.md) | baseline | PCIE-003, PCIE-006, PCIE-045, PCIE-059 |
| [PCIE-050 — Reproduce SKY130 PDK, OpenROAD and OpenLane implementation environment](PCIE-050.md) | baseline | PCIE-002 |
| [PCIE-051 — Define technology wrappers for memories, synchronizers and clock gating](PCIE-051.md) | baseline | PCIE-004 |
| [PCIE-052 — Design high-speed I/O pads, ESD protection and package model](PCIE-052.md) | baseline | PCIE-003, PCIE-006, PCIE-050 |
| [PCIE-053 — Select SKY130 memories and map endpoint buffers](PCIE-053.md) | baseline | PCIE-050, PCIE-051 |
| [PCIE-054 — Harden early PHY logic blocks in SKY130 to calibrate timing](PCIE-054.md) | baseline | PCIE-012, PCIE-050 |
| [PCIE-055 — Harden the full endpoint core with OpenLane and sign off physical checks](PCIE-055.md) | baseline | PCIE-003, PCIE-041, PCIE-053, PCIE-054 |
| [PCIE-056 — Verify gate-level ASIC netlist and RTL equivalence](PCIE-056.md) | baseline | PCIE-042, PCIE-055 |
| [PCIE-057 — Integrate chip top: pad ring, harness, test access and fabrication route](PCIE-057.md) | baseline | PCIE-040, PCIE-052 |
| [PCIE-058 — Prepare ASIC tapeout signoff and post-silicon test plan](PCIE-058.md) | conditional | PCIE-043, PCIE-056, PCIE-057 |
| [PCIE-059 — Design bias, reference and termination-calibration circuits](PCIE-059.md) | baseline | PCIE-003, PCIE-004, PCIE-006, PCIE-050 |
| [PCIE-060 — Build an early PHY loopback top with logical PHY and PMA placeholders](PCIE-060.md) | baseline | PCIE-003, PCIE-013, PCIE-045, PCIE-054 |
