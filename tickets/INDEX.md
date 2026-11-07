# Ticket index

Generated initial backlog; no tickets are claimed or implemented. See [workflow](README.md).

| Ticket | Gate | Dependencies |
|---|---|---|
| [PCIE-001 — Freeze endpoint profile and audit normative applicability](PCIE-001.md) | baseline | none |
| [PCIE-002 — Reproduce OSS CAD Suite, pyuvm and ngspice tool environment](PCIE-002.md) | baseline | none |
| [PCIE-003 — Resolve external serializer/CDR interface feasibility for Tang Nano 20K](PCIE-003.md) | baseline | PCIE-001, PCIE-002 |
| [PCIE-004 — Create PHY boundary and cycle-accurate simulation contract](PCIE-004.md) | baseline | PCIE-001 |
| [PCIE-005 — Build pyuvm framework, symbol-level root-port agent and PHY reference models](PCIE-005.md) | baseline | PCIE-002, PCIE-004 |
| [PCIE-006 — Extract electrical limits and ngspice model assumptions](PCIE-006.md) | baseline | PCIE-001, PCIE-002 |
| [PCIE-007 — Integrate discrete-transistor TX serializer, FPGA schedule and output](PCIE-007.md) | baseline | PCIE-003, PCIE-006, PCIE-045, PCIE-046 |
| [PCIE-008 — Design external RX clock recovery, deserialization and electrical controls](PCIE-008.md) | baseline | PCIE-003, PCIE-006, PCIE-046 |
| [PCIE-009 — Bridge digital patterns to ngspice and produce electrical evidence](PCIE-009.md) | baseline | PCIE-005, PCIE-006 |
| [PCIE-010 — Implement 8b/10b encoder and decoder with running disparity](PCIE-010.md) | baseline | PCIE-004, PCIE-005 |
| [PCIE-011 — Implement scrambling and descrambling](PCIE-011.md) | baseline | PCIE-004, PCIE-005 |
| [PCIE-012 — Implement symbol framing and ordered-set parser/generator](PCIE-012.md) | baseline | PCIE-010, PCIE-011 |
| [PCIE-013 — Implement clock domains, elastic buffering and SKP compensation](PCIE-013.md) | baseline | PCIE-004, PCIE-012 |
| [PCIE-014 — Implement LTSSM Detect and Polling](PCIE-014.md) | baseline | PCIE-004, PCIE-012 |
| [PCIE-015 — Implement LTSSM x1 Configuration and reach L0](PCIE-015.md) | baseline | PCIE-014, PCIE-013 |
| [PCIE-016 — Implement Recovery, Disabled, Loopback, Hot Reset and compliance modes](PCIE-016.md) | baseline | PCIE-015 |
| [PCIE-017 — Implement PHY L0s, L1 and L2 state behavior](PCIE-017.md) | baseline | PCIE-016 |
| [PCIE-018 — Implement DLLP codec and CRC16](PCIE-018.md) | baseline | PCIE-012, PCIE-047 |
| [PCIE-019 — Implement Data Link state and flow-control initialization](PCIE-019.md) | baseline | PCIE-015, PCIE-018 |
| [PCIE-020 — Implement LCRC, receive sequence checks and ACK/NAK policy](PCIE-020.md) | baseline | PCIE-018, PCIE-019 |
| [PCIE-021 — Implement transmit retry buffer and replay controller](PCIE-021.md) | baseline | PCIE-018, PCIE-019 |
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
| [PCIE-040 — Implement chosen board PHY adapter and timing constraints](PCIE-040.md) | conditional | PCIE-003, PCIE-007, PCIE-008, PCIE-009, PCIE-039, PCIE-041 |
| [PCIE-041 — Run synthesis, resource, timing and CDC signoff](PCIE-041.md) | baseline | PCIE-039 |
| [PCIE-042 — Close digital protocol coverage and stress recovery](PCIE-042.md) | baseline | PCIE-039, PCIE-041 |
| [PCIE-043 — Qualify electrical path across corners and expose limits of simulation](PCIE-043.md) | baseline | PCIE-007, PCIE-008, PCIE-009, PCIE-040 |
| [PCIE-044 — Validate hardware bring-up and host interoperability](PCIE-044.md) | conditional | PCIE-040, PCIE-041, PCIE-042, PCIE-043 |
| [PCIE-045 — Qualify solderable transistor serializer building blocks first](PCIE-045.md) | baseline | PCIE-003, PCIE-006, PCIE-009 |
| [PCIE-046 — Assess external RX clock recovery feasibility before TX hardware spending](PCIE-046.md) | baseline | PCIE-003, PCIE-006 |
| [PCIE-047 — Build data-link partner models: DLLP, CRC, ACK/NAK replay and flow control](PCIE-047.md) | baseline | PCIE-005 |
| [PCIE-048 — Build TLP, configuration and enumeration reference models](PCIE-048.md) | baseline | PCIE-005 |
