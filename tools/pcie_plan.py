"""Authored work packages for the PCI Express Gen1 x1 endpoint on SkyWater SKY130.

Digital core plus on-chip SKY130 PHY; see docs/asic-target.md and docs/phy-architecture.md.
Generated tickets must not be regenerated after any ticket is claimed."""
TICKETS = []


def ticket(n, title, refs, deps, work, tests, accept, spice=None, gate='baseline', priority=None):
    TICKETS.append(dict(id=f'PCIE-{n:03}', title=title, refs=refs.split(),
                        dependencies=[f'PCIE-{d:03}' for d in deps], work=list(work),
                        tests=list(tests), acceptance=list(accept), spice=spice, gate=gate,
                        priority=priority or ('P0' if n <= 9 else 'P1')))


ticket(1, 'Freeze endpoint profile and audit normative applicability',
       '1 1.3.2.2 5.1.1 6 7 4.3.1.1', [],
       work=[
           'Produce docs/endpoint-profile.md: Gen1 x1, one PCI Express Endpoint function, Type 0 header, VC0/TC0, 128-byte advertised MPS initially, 64-bit non-prefetchable memory BAR, MSI, digital TL/DL/logical PHY with an on-chip SKY130 PMA',
           'Distinguish first L0 bring-up from complete baseline; L0s and PCI-PM obligations cannot be removed merely by disabling ASPM in a prototype',
           "Classify every section in specification/TRACEABILITY.csv as applicable, conditional or not applicable to the endpoint, with citations; detailed atomic requirements are written by each section's primary-owner ticket, not here",
           'Record optional capability omissions and required response behavior; identify missing normative companion specifications (PCI configuration, PM, MSI, CEM/form factor) without inventing their contents',
           'Freeze the digital datapath width and logical clock before any RTL ticket starts. Proposed default: 16 bits per cycle (two symbols, each with a K flag) at 125 MHz. One 8-bit symbol at 250 MHz is unlikely to close timing in SKY130 standard cells at the slow corner and may be kept only with synthesis evidence from a representative block. Changing width after RTL begins touches framing, CRC, DLLP and ordered-set logic in every layer',
           'Freeze the reference-clock policy. Section 4.3.1.1 requires both link ends to transmit within 600 ppm of each other, and host spread-spectrum clocking exceeds what SKP compensation can absorb against a free-running local oscillator. Default: derive the on-chip PLL serializer clock, CDR reference and digital clocks from the host 100 MHz REFCLK; any separate-clock mode requires an explicit no-SSC host condition',
           'Before declaring companion specifications missing, record what Rev1.1 sections 7.5 (PCI-compatible registers), 7.6 (PCI-PM capability) and 7.7 (MSI/MSI-X capability) already define; list the remaining gaps per register field and which of PCIE-027/029/030 each gap blocks',
       ],
       tests=[
           'Define legal and forbidden endpoint transactions for the pyuvm scoreboard',
           'Review each advertised capability against its planned test and implementation owner',
       ],
       accept=[
           'Profile and mandatory/optional matrix have source citations and no unexplained exclusions',
           'Every section has an applicability classification; candidate-level review is assigned to its primary-owner ticket and PCIE-042 confirms none remain unresolved',
           'Datapath width, logical clock and reference-clock/SSC policy are recorded with rationale before any RTL ticket becomes ready',
       ])


ticket(2, 'Reproduce OSS CAD Suite, pyuvm and ngspice tool environment',
       '1.5.4.4', [],
       work=[
           'Add reproducible launcher and dependency lock for cocotb plus pyuvm; use oss-cad-suite/bin/verilator as primary SV simulator and Icarus only for supported subsets',
           'Discover bundled Python rather than assuming bin/python3; reconcile project Python >=3.14 with suite Python ABI and cocotb shared libraries',
           'Record exact simulator, Python, cocotb, pyuvm and ngspice versions; add one documented command each for digital and analog smoke tests',
           'Keep vendored oss-cad-suite and original specifications out of generated change sets',
           'Use a uv-managed project environment with its own pinned cocotb and pyuvm instead of the suite bundled Python 3.11 cocotb; confirm cocotb support for the chosen interpreter and, if Python 3.14 is unsupported, lower requires-python to the newest supported version and record why',
       ],
       tests=[
           'Run a small SystemVerilog clock/reset DUT with a pyuvm test through cocotb and assert that reset changes observable state',
           'Fail intentionally once to prove assertion failures propagate nonzero; restore passing test',
       ],
       accept=[
           'Fresh documented environment runs both smoke tests without hidden shell state',
           'Commands, versions and logs are captured; no claim that preinstalled cocotb implies pyuvm availability',
       ],
       spice='Run ngspice -b on a known RC transient and compare measured settling time with analytic RC tolerance; exercise failure handling too.')


ticket(3, 'Freeze SKY130 chip architecture, clocking, pins and PHY partition',
       '4.3 4.3.1.1 4.3.1.8 4.3.2.2 6.6', [1, 2],
       work=[
           'Freeze docs/asic-target.md and docs/phy-architecture.md: digital core (transaction layer, data link layer and logical PHY including scrambling and 8b/10b) plus an on-chip SKY130 PMA (PLL, serializer, TX driver, RX front end, CDR and deserializer) on one die',
           'Own the reference-clock architecture under the PCIE-001 policy: host 100 MHz REFCLK input, PLL multiplication to the serializer clock, CDR reference and digital clocks; budget jitter, SSC tracking and phase relations',
           'Choose the PMA rate architecture (full-rate 2.5 GHz clocks, or half-rate 1.25 GHz clocks with a double-edge final stage) and the split of serializer/deserializer stages between standard cells and custom current-mode logic, as hypotheses for PCIE-045 to qualify',
           'Choose the digital-to-PMA parallel width consistent with the PCIE-001 datapath (proposed 20 encoded bits per 125 MHz cycle) and list the required PMA controls (electrical idle, receiver detect, polarity, lock, power states, reset); PCIE-004 owns the detailed interface contract and timing',
           'Budget chip pins (PCIe TX/RX pairs, REFCLK, PERST#, any wake signal, supplies, test access); select standard-cell library (sky130_fd_sc_hd by default), operating corners, supplies and a preliminary die area',
           'Record fabrication-route assumptions as unverified until PCIE-057; no fabrication commitment or cost is implied',
           'Define the digital-only fallback: if PCIE-045/046/007/008/049 reject the on-chip PHY, the chip proceeds as a digital core with PHY-boundary loopback and the PHY failure is reported, not hidden',
           'Assign every PHY support block an owner: bias and references (PCIE-059), REFCLK input receiver and PLL (PCIE-049), pads and ESD (PCIE-052)',
           'Record off-chip parts the PHY relies on: TX AC-coupling capacitors (receiver detection depends on them), any precision calibration resistor, REFCLK termination and supply decoupling; the PCIE-044 test board must provide them',
           'Decide beacon support for wake from L2 versus a WAKE# signal, because it affects both PCIE-017 and the PCIE-007 transmitter',
       ],
       tests=[
           'Define a PMA capability contract and pyuvm fault scenarios for loss of lock, detection failure and electrical idle',
           'Compute encoded-data throughput and clock budgets independently of the RTL',
       ],
       accept=[
           'Chip architecture, clocking, PMA rate architecture, pins and corners are recorded with sources and rationale',
           'No PHY feasibility is asserted before PCIE-045/046/007/008/049 evidence; the fallback boundary is explicit',
       ],
       spice='No circuit qualification here. Record circuit hypotheses, rates and budgets that PCIE-045, PCIE-049, PCIE-007 and PCIE-008 must confirm with SKY130 transistor-level simulation.')


ticket(4, 'Create PHY boundary and cycle-accurate simulation contract',
       '1.5.4.4 4.1 4.2', [1, 3],
       work=[
           'Define the digital symbol interface at the width and clock frozen in PCIE-001 (proposed: two symbols plus K flags per 125 MHz cycle); do not label it PIPE compliant without implementing a specific PIPE revision',
           'Own the detailed digital-to-PMA interface contract within the PCIE-003 architecture: signal list, widths, bit order, clocks, control acknowledgments and timing diagrams',
           'Separate logical PHY from PMA serialization/CDR through explicit TX/RX symbols, status, electrical-idle, receiver-detect, polarity, power state and lock controls',
           'Define reset behavior, clock domains, backpressure constraints and latency; the physical stream cannot pause when a digital consumer is not ready',
           'Provide a behavioral PMA model for digital simulation and the mixed-signal interface to the SKY130 PMA macros; scrambling and 8b/10b happen exactly once, in the digital core',
           'Define the encoded parallel interface to the on-chip serializer and from the deserializer (proposed 20 bits per 125 MHz cycle), with explicit bit order across 10-bit symbol boundaries',
           'Specify TX parallel-clock/data phase alignment to the PLL, the recovered RX clock domain, PMA control acknowledgments and initialization handshakes',
           'Specify alignment of STP, SDP, END, EDB, COM and ordered sets within the multi-symbol digital word, including packets that start or end in any symbol position',
       ],
       tests=[
           'Use pyuvm driver/monitor agents for each direction; exercise lock loss, asynchronous reset, invalid symbols and idle transitions',
           'Assert deterministic control handshakes and detect data loss under FIFO pressure',
           'Exercise packets and ordered sets starting and ending in every symbol position of the digital word',
       ],
       accept=[
           'Interface specification includes timing diagrams and all control acknowledgments',
           'Behavioral PMA model allows full digital verification before analog macros exist',
       ])


ticket(5, 'Build pyuvm framework, symbol-level root-port agent and PHY reference models',
       '1.5 4.2 4.2.1 4.2.3 B C', [2, 4],
       work=[
           'Build the shared pyuvm environment: configuration, deterministic seed handling, packet traces, timeout watchdogs, scoreboard base classes and coverage export reused by later tickets',
           'Build a symbol and ordered-set root-port agent at the PCIE-004 interface for data and K symbols, TS1/TS2, FTS, SKP and electrical-idle ordered sets; separate active drivers from passive monitors',
           'Implement independent Python 8b/10b (Appendix B) and scrambler (section 4.2.3, Appendix C) reference models from cited tables and equations; do not import DUT algorithm code',
           'Leave DLLP and data-link partner models to PCIE-047 and TLP/configuration models to PCIE-048 so PCIE-010/011 are not blocked behind a complete Python link partner',
       ],
       tests=[
           'Self-check 8b/10b and scrambler models against Appendix B/C vectors without a DUT; inject invalid codes and wrong disparity that must be detected',
           'Round-trip randomized symbol streams and ordered sets through the agent driver and monitor with an explicit model contract',
       ],
       accept=[
           'Reference vectors carry source citations and expected bytes',
           'Failures include seed, packet context, time and violated requirement ID',
       ])


ticket(6, 'Extract electrical limits and ngspice model assumptions',
       '4.3.1 4.3.2 4.3.3 4.3.4', [1, 2, 50],
       work=[
           'Transcribe each applicable electrical table row, units, min/max, footnotes and measurement point into machine-readable limits with exact citations',
           'Separate transmitter mask, receiver tolerance mask, measurement load and clock recovery measurement assumptions',
           'Define ngspice-supported driver/receiver/package/channel models; if only IBIS is supplied document a validated conversion or alternate characterization rather than assuming native IBIS support',
           'Assign confidence levels to ideal, behavioral, manufacturer and measured models; require PVT and model provenance',
           'Capture SKY130 device limits from the pinned PDK (supplies, breakdown, reliability and electromigration rules) alongside the PCIe limits, with PDK revision',
           'Qualify the pinned SKY130 ngspice device models, corners and mismatch data for PCIE-045, and define extracted-parasitic, pad and package model conventions',
       ],
       tests=[
           'Expose limit IDs in digital-to-analog waveform metadata and pyuvm pattern manifests',
           'Check limit-table parsing catches missing units and contradictory min/max bounds',
       ],
       accept=[
           'All applicable Chapter 4.3 limits are captured or explicitly marked missing',
           'Review source PDF tables visually; no fabricated compliance thresholds',
       ],
       spice='Provide parameterized differential source, coupling capacitors, termination and channel loads; verify units, DC bias and convergence at nominal conditions.')


ticket(7, 'Design on-chip SKY130 TX serializer and PCIe transmitter',
       '4.2.1.1 4.3.2.3 4.3.3', [3, 6, 45, 46, 49, 52, 59],
       work=[
           'Integrate qualified PCIE-045 cells into the complete TX path: parallel-to-serial tree from the PCIE-004 interface to 2.5 Gb/s, retiming, and clocks from the PCIE-049 PLL',
           'Design the TX driver per PCIE-006 section 4.3.3 limits: differential swing, -3.5 dB de-emphasis, common mode, termination (calibrated if needed), electrical idle and receiver detection',
           'Prevent serializer update races across parallel-word and group boundaries; record pipeline latency and the deterministic reset and phase start',
           'Lay out in Magic, extract parasitics and pass DRC/LVS; deliver a macro (GDS, LEF and timing abstract) for PCIE-040 integration',
           'If PCIE-003 selects beacon for wake from L2, generate it in the transmitter; otherwise record its absence',
           'Deliver preliminary TX macro abstracts (size, pin placement, supplies) early to the PCIE-060 loopback top and keep them current',
       ],
       tests=[
           'Drive the extracted TX netlist with pyuvm-generated 8b/10b streams, compliance patterns, electrical-idle entry/exit and receiver-detect sequences through PCIE-009',
           'Reconstruct serial bits from the output and detect omitted, duplicated or permuted bits across 10-bit symbol and parallel-word boundaries',
       ],
       accept=[
           'Extracted TX macro meets modeled PCIE-006 transmitter limits at all corners, or the shortfall is quantified',
           'DRC/LVS-clean macro with abstracts is delivered with reproducible commands',
       ],
       spice='Run schematic and extracted-layout transients at all PVT corners with SKY130 models plus pad, package and channel loads from PCIE-052; report eye mask, swing, de-emphasis, jitter, common mode, idle and detection behavior; verify timestep convergence.')


ticket(8, 'Design on-chip SKY130 receiver, clock and data recovery and deserializer',
       '4.3.1.8 4.3.1.9 4.3.4', [3, 6, 45, 46, 49, 59],
       work=[
           'Implement the RX path recommended by PCIE-046: termination and common mode, input amplifier or equalization if needed, samplers, CDR, deserializer to the PCIE-004 parallel interface and recovered-clock delivery',
           'Implement electrical-idle (squelch) detection, lock detection and loss-of-lock reporting through the PMA contract',
           'Meet section 4.3.4 receiver limits and the N_FTS/lock-time budget, and keep that budget current for PCIE-017/031',
           'Lay out in Magic, extract and pass DRC/LVS; deliver a macro with abstracts for PCIE-040',
           'Deliver preliminary RX macro abstracts (size, pin placement, supplies) early to the PCIE-060 loopback top and keep them current',
       ],
       tests=[
           'Drive recovered clock drift, polarity reversal, loss of signal, idle exit and false lock through the pyuvm PHY model',
           'Assert no packet delivery before symbol alignment and lock; verify fault-driven recovery',
           'Verify deserializer bit ordering, comma/symbol alignment and reacquisition under recovered-clock phase changes; do not assume RX phase equals local TX phase',
       ],
       accept=[
           'Extracted RX macro meets modeled receiver limits and the lock-time budget at all corners, or the shortfall is quantified',
           'Behavioral CDR results are labeled assumptions until extracted-layout or silicon evidence exists',
       ],
       spice='Sweep input amplitude, common mode, jitter, frequency offset, termination and idle-detection thresholds on schematic and extracted netlists at all corners; simulate detection loads and bias startup; verify timestep convergence.')


ticket(9, 'Bridge digital patterns to ngspice and produce electrical evidence',
       '4.2.8 4.3.3.1 4.3.3.2 4.3.3.4', [5, 6],
       work=[
           'Create a converter from timestamped PHY bit/pin events to PWL sources with explicit units, finite rise/fall, bit order and simulator time origin',
           'Create machine-readable analog results with source stream hash, seed, model hashes, corners and electrical limit IDs',
           'Add eye folding using the specified measurement clock recovery method, mask checks and amplitude/jitter/de-emphasis measurements',
           'Keep short transient eye checks distinct from statistically meaningful BER qualification',
           'Drive the PMA parallel interface and PLL clocks into the transistor-level serializer rather than replacing it with an ideal 2.5 Gb/s source',
       ],
       tests=[
           'Generate compliance patterns, legal high-transition and low-transition streams, TS1/TS2, SKP and idle exits using pyuvm',
           'Verify PWL time spacing equals 400 ps per UI at nominal rate and recovered data matches source bits',
       ],
       accept=[
           'Regression exits nonzero for a deliberately degraded electrical corner and passes a known analytical fixture',
           'Electrical reports identify unmodeled effects and never assert compliance from ideal eye plots alone',
       ],
       spice='Run ngspice transient batch regressions on all supported corners; set maximum timestep conservatively, initially <= UI/40, and demonstrate convergence by halving it.')


ticket(10, 'Implement 8b/10b encoder and decoder with running disparity',
       '4.2.1 B', [4, 5],
       work=[
           'Implement synthesizable SV encoder/decoder using Appendix B tables and specified serial bit ordering',
           'Track TX/RX disparity, K symbols, comma detection, invalid codes and disparity errors',
           'Define reset disparity and error interface to LTSSM/data link',
       ],
       tests=[
           'Exhaustively test all 256 data values and legal K symbols under both running disparities against independent table model',
           'Decode all 1024 codewords per disparity; verify illegal/disparity errors, round-trip and back-to-back updates',
       ],
       accept=[
           'Every Appendix B mapping agrees with reference; illegal codes cannot silently become valid data',
           'Lint and synthesis confirm bounded combinational logic and timing target',
       ])


ticket(11, 'Implement scrambling and descrambling',
       '4.2.3 C.1', [4, 5],
       work=[
           'Implement specified LFSR polynomial, initial value, bit order and advancement rules in SV',
           'Apply exact reset/advance/bypass behavior for COM, SKP, training ordered sets, data and disabled scrambling',
           'Support identical symbol-boundary behavior under stalls in internal pipelines without pausing wire cadence',
       ],
       tests=[
           'Compare long randomized streams with independent Python LFSR model',
           'Exercise COM reseed, SKP hold, ordered sets, data/control boundaries, reset and scrambling-disable negotiation',
       ],
       accept=[
           'Known Appendix C vectors and independent model match cycle by cycle',
           'No scrambler state advances on prohibited symbols or misses required advances',
       ])


ticket(12, 'Implement symbol framing and ordered-set parser/generator',
       '4.2.2 4.2.4.1 4.2.4.3 4.2.8', [10, 11],
       work=[
           'Implement STP/SDP/END/EDB framing, idle and TS1/TS2/FTS/SKP ordered sets for x1',
           'Validate training fields, lane/link number PAD handling, consecutive-set recognition and malformed frames',
           'Coordinate scrambling, encoding and packet arbitration without dropping or duplicating symbols',
       ],
       tests=[
           'Drive all legal packet/ordered-set boundaries and corrupt every ordered-set field class',
           'Verify TS counters reset on broken consecutiveness and no malformed frame reaches TL',
       ],
       accept=[
           'Wire sequence matches source framing rules for TLP, DLLP and training traffic',
           'All injected framing faults produce defined error/recovery behavior',
       ])


ticket(13, 'Implement clock domains, elastic buffering and SKP compensation',
       '4.2.7 4.2.4.8', [4, 12, 51],
       work=[
           'Design async FIFOs and synchronized status/reset crossings for user, symbol and receive clocks',
           'Implement x1 elasticity and SKP insertion/removal following source intervals and packet-boundary restrictions',
           'Calculate FIFO depth for frequency offset, SSC assumptions, bursts and recovery latency; x1 does not need multilane deskew',
           'Document overflow/underflow handling and avoid impossible physical-stream backpressure',
           'Size elasticity for the PCIE-001/003 reference-clock policy; a free-running local clock against an SSC host violates the section 4.3.1.1 600 ppm requirement and is not a supported elastic-buffer operating case',
           'Use the PCIE-051 technology-portable memory and synchronizer wrappers so simulation and SKY130 builds use identical RTL',
       ],
       tests=[
           'Use independent clocks with min/max permitted frequency offset and randomized reset phase',
           'Scoreboard data preservation through SKP changes; test FIFO boundary pressure and lock loss',
           'Include an out-of-tolerance clock-offset case that must report overflow or underflow rather than silently corrupt data',
       ],
       accept=[
           'No data loss/reorder under supported clock offsets',
           'CDC/reset review and timing constraints cover every crossing',
       ])


ticket(14, 'Implement LTSSM Detect and Polling',
       '4.2.4 4.2.5 4.2.6.1 4.2.6.2', [4, 12],
       work=[
           'Implement endpoint/upstream-port Detect.Quiet/Active and Polling substates, receiver-detect handshakes and precise timers',
           'Implement TS1/TS2 counting, polarity handling and compliance entry decisions',
           'Parameterize simulation acceleration without changing production time units or off-by-one semantics',
       ],
       tests=[
           'Model no receiver, successful detection, detection timeout, reversed polarity, missing/corrupt TS sets and all Polling exits',
           'Check each timer just before, on and after expiry and all count thresholds',
       ],
       accept=[
           'State transitions and emitted sets match source transition rules',
           'Fast simulation and production timers are linked by checked conversion',
       ])


ticket(15, 'Implement LTSSM x1 Configuration and reach L0',
       '4.2.6.3 4.2.6.5 4.2.4.7', [14, 13],
       work=[
           'Implement upstream-port link/lane negotiation through Configuration substates with lane zero and width one',
           'Handle peer width proposals, PAD values, polarity, TS2 completion and idle qualification',
           'Expose trained width/speed and link-up only after valid L0 transition',
       ],
       tests=[
           'Run pyuvm root-port training from reset to L0 under valid and adversarial TS sequences',
           'Test wrong lane/link numbers, broken consecutive sets, timeout fallback and repeated retraining',
       ],
       accept=[
           'Legal root-port BFM reaches x1 2.5 GT/s L0 repeatably',
           'Invalid negotiation cannot falsely assert link-up',
       ])


ticket(16, 'Implement Recovery, Disabled, Loopback, Hot Reset and compliance modes',
       '4.2.6.4 4.2.6.9 4.2.6.10 4.2.6.11 4.2.8', [15],
       work=[
           'Implement required Recovery lock/config/idle behavior and fallback; Gen1-only negotiation must never claim unsupported speed',
           'Implement Disabled, endpoint loopback, Hot Reset and compliance state data paths and exit rules',
           'Coordinate packet discard, scrambler reset, physical idle and DL state during transitions',
       ],
       tests=[
           'Inject symbol lock loss during traffic, directed recovery, peer Hot Reset, loopback requests and compliance entry',
           'Verify stale packets never leak after retrain and legal traffic resumes with fresh DL initialization',
       ],
       accept=[
           'Each implemented LTSSM transition has positive and negative tests',
           'Reset and recovery cannot deadlock ongoing DL/TL traffic',
       ])


ticket(17, 'Implement PHY L0s, L1 and L2 state behavior',
       '4.2.6.6 4.2.6.7 4.2.6.8 5.2', [16],
       work=[
           'Implement independent TX/RX L0s entry/exit including idle and FTS; maintain appropriate higher-layer timers',
           'Implement required software-PM L1 and L2/L3-ready control behavior and wake/reset paths with power manager',
           'Implement the beacon-versus-WAKE# decision frozen in PCIE-003, and hardware power/lock acknowledgments',
           'Make N_FTS, Extended Synch use and L0s exit latency build parameters; their final values must stay within the receive relock budget from PCIE-046/008 and are bound and checked in PCIE-040',
       ],
       tests=[
           'Enter RX L0s while TX stays active and vice versa; test FTS counts and exit latency',
           'Exercise L1/L2 transitions with pending traffic, wake, failed lock and reset',
       ],
       accept=[
           'L0s support is retained for Rev1.1 baseline',
           'All power transitions honor advertised exit latencies and specified timer behavior',
       ],
       spice='Use PCIE-009 with actual PHY candidate to check idle entry/exit transients and modeled relock latency; no analog proof from a purely logical status toggle.')


ticket(18, 'Implement DLLP codec and CRC16',
       '3.4', [12, 47],
       work=[
           'Implement ACK/NAK, InitFC1/2, UpdateFC and PM DLLP fields, reserved bits and CRC16',
           'Route validated DLLPs to dedicated consumers; discard corrupted/unsupported packets per source',
           'Arbitrate DLLP transmit requests with bounded latency requirements',
       ],
       tests=[
           'Use golden CRC vectors, random legal DLLPs and bit flips in every field including CRC',
           'Test reserved encodings, truncated frames and concurrent PM/FC/ACK traffic',
       ],
       accept=[
           'Invalid CRC cannot change credits or acknowledge a TLP',
           'All DLLP types in baseline encode/decode with exact byte order',
       ])


ticket(19, 'Implement Data Link state and flow-control initialization',
       '3.2 3.3 2.9', [15, 18],
       work=[
           'Implement DL_Inactive/Init/Active rules coordinated with LTSSM and link status',
           'Implement VC0 InitFC phases for posted/non-posted/completion header and data credits',
           'Prevent application TLP emission before DL_Up; clear state on link loss and repeat initialization',
       ],
       tests=[
           'Test asymmetric initialization, missing/corrupt InitFC, peer restart and link-down at every phase',
           'Verify DL_Up transitions and credit establishment against independent model',
       ],
       accept=[
           'DL_Up only asserts after all required initialization conditions',
           'Link loss reinitializes both credit and reliability state',
       ])


ticket(20, 'Implement LCRC, receive sequence checks and ACK/NAK policy',
       '3.5.3 3.5.1', [18, 19],
       work=[
           'Implement receive TLP LCRC and 12-bit sequence handling with modulo comparison and duplicate rejection',
           'Generate ACK/NAK with specified latency, sequence values and timer rules',
           'Handle EDB/nullified packets and error propagation without committing corrupted payloads',
       ],
       tests=[
           'Inject bad LCRC, sequence gaps, duplicates, wraparound, truncation, EDB and legal retransmissions',
           'Check packets reach TL once only; measure ACK/NAK timer boundaries under heavy traffic',
       ],
       accept=[
           'No corrupt or duplicate TLP causes application-visible side effects',
           'ACK/NAK content and deadlines match source rules',
       ])


ticket(21, 'Implement transmit retry buffer and replay controller',
       '3.5.2', [18, 19, 51],
       work=[
           'Assign TX sequence numbers and LCRC; retain each sent TLP until valid acknowledgment',
           'Implement replay timer/count, ACK/NAK processing, retry-buffer admission and recovery escalation',
           'Handle sequence wrap, stale/invalid ACKs, link loss and concurrent enqueue/replay without double-credit charging',
           'Use the PCIE-051 technology-portable memory and synchronizer wrappers so simulation and SKY130 builds use identical RTL',
       ],
       tests=[
           'Drop ACKs, inject NAKs and invalid ACK ranges, force timer expiry and wrap sequence space',
           'Scoreboard replay byte identity, retirement order, bounded buffer use and eventual recovery',
       ],
       accept=[
           'Replay never loses an unacknowledged packet or retires one prematurely',
           'Source retry limits/timers are checked at boundaries and lead to correct recovery',
       ])


ticket(22, 'Implement TLP header codec and validation',
       '2.1 2.2.1 2.2.2 2.2.3 2.2.4 2.2.5 2.2.6 2.2.7 2.2.9', [48],
       work=[
           'Implement synthesizable packet types and serializers/parsers for 3DW/4DW memory, Type0 configuration, completion and supported messages',
           'Validate format/type, length including zero encoding, payload alignment, byte enables, address routing, TD/EP, attributes and requester/completer IDs',
           'Detect 4KB boundary and MPS/MRRS violations as applicable; preserve malformed/unsupported distinction',
           'Centralize SV types with explicitly documented wire byte order',
       ],
       tests=[
           'Generate legal packet matrix and one-field mutations, 1DW/maximum lengths, unaligned byte enables and boundary addresses',
           'Compare full emitted bytes and parsed fields with independent Python model',
       ],
       accept=[
           'Supported formats round-trip exactly',
           'Illegal inputs are classified without out-of-range array accesses or partial application writes',
       ])


ticket(23, 'Implement receive classification and unsupported/malformed handling',
       '2.3.1 6.5.7', [22, 20],
       work=[
           'Classify posted, non-posted and completion TLPs; validate destination and endpoint capability before dispatch',
           'Implement UR/CA/error-report behavior for unsupported requests and malformed packets with correct posted/non-posted distinctions',
           'Reject locked requests as required for PCI Express Endpoint and avoid producing forbidden I/O or lock requests',
       ],
       tests=[
           'Send unsupported memory/config/message types, MRdLk, malformed headers and out-of-range BAR traffic',
           'Check exact completion/error behavior and that invalid posted writes never mutate application state',
       ],
       accept=[
           'Every rejected request has source-backed disposition',
           'No unsupported request path blocks valid traffic indefinitely',
       ])


ticket(24, 'Implement completer, read splitting and byte-enable semantics',
       '2.2.9 2.3.1.1', [22, 23],
       work=[
           'Build Cpl/CplD generator with completion status, byte count, lower address, IDs and tags',
           'Split memory read responses by MPS/read completion boundary rules and preserve enabled-byte accounting',
           'Handle zero-length and byte-disabled accesses without unintended side effects; prioritize completion resources to avoid deadlock',
       ],
       tests=[
           'Sweep lengths, byte enables, address alignment and completion boundaries; apply arbitrary application response latency',
           'Reassemble split completions in independent scoreboard and check all headers/bytes',
       ],
       accept=[
           'Each supported non-posted request completes with correct data/status and within defined service bound',
           'No completion exceeds negotiated limits or returns bytes from another request',
       ])


ticket(25, 'Implement requester tags, completion matching and timeout',
       '2.3.2 2.8 2.2.6.2', [22, 24],
       work=[
           'Implement optional application-facing memory read/write engine as a planned baseline feature; gate requests with Bus Master Enable',
           'Allocate unique tags and support required 64-bit memory addressing; track requested byte ranges and split completion progress',
           'Detect unexpected, duplicate, poisoned, failed and timed-out completions; retire tags safely and report errors',
           'Keep requester resource allocation from starving completer responses',
       ],
       tests=[
           'Interleave split completions across tags, reverse response order where legal and exercise status failures',
           'Test timeout boundaries, tag exhaustion, wrong requester/tag, BME disable and reset with requests outstanding',
       ],
       accept=[
           'No request tag is reused while outstanding',
           'Exactly one terminal outcome per request and no transmit when BME forbids it',
       ])


ticket(26, 'Implement VC0 credits and transaction ordering',
       '2.4 2.5 2.6 6.3 D', [19, 21, 22],
       work=[
           'Track posted/non-posted/completion header/data credit pools in correct units with wrap and infinite-credit encodings',
           'Implement UpdateFC generation/consumption and buffering minimums; charge credits once for original transmissions, not replay',
           'Apply required ordering matrix, relaxed ordering and TC-to-VC0 policy; reserve independent progress for completions',
           'Document FIFO sizing and dependencies with bounded backpressure and no circular wait',
       ],
       tests=[
           'Starve each credit class independently, force counter wrap and test infinite-credit advertisement',
           'Run producer/consumer ordering litmus tests and saturation with replay plus completion returns',
       ],
       accept=[
           'No transmission consumes unavailable credits; receive buffers cannot overrun legal advertised credits',
           'Ordering scoreboard and bounded-progress checks pass under randomized backpressure',
       ])


ticket(27, 'Implement configuration Type0 header and BAR decoding',
       '7.1 7.2.2.2 7.3 7.4 7.5.1 7.5.2', [23, 24],
       work=[
           'Implement function-zero Type0 config read/write completer with correct BDF capture, byte enables and register attributes',
           'Provide legal development identity parameters; avoid claiming assigned Vendor ID ownership',
           'Implement 64-bit BAR sizing/probe and address masks, Memory Space Enable, Bus Master Enable, status W1C and reserved bits',
           'Use a proposed 4KiB BAR0/BAR1 pair and unused BARs returning zero; exact resource profile is confirmed in PCIE-001',
       ],
       tests=[
           'Emulate BIOS/OS enumeration, BAR all-ones probing, relocation, byte writes and command gating',
           'Attempt writes to RO/reserved/W1C fields and accesses to unsupported functions/routing types',
       ],
       accept=[
           'Host BFM enumerates one endpoint with consistent resource masks',
           'No register access violates configured attributes and disabled memory decoding produces no side effects',
       ])


ticket(28, 'Implement PCI Express capability registers and live status',
       '7.8.1 7.8.2 7.8.3 7.8.4 7.8.5 7.8.6 7.8.7 7.8.8', [27, 16, 26],
       work=[
           'Implement capability linked list and Rev1.1 endpoint Device/Link capabilities, control and status fields',
           'Advertise only x1 Gen1 and implemented MPS, tags, latency and error controls; bind live status to actual state',
           'Route control writes to real behavior, including retrain/power/error controls where endpoint-applicable',
           'Audit all register rows against PDF and reset values; omit slot/root structures for endpoint role',
       ],
       tests=[
           'Walk capability list, verify no cycles/overlap and test each bit access attribute and reset value',
           'Change negotiated controls under traffic and compare status updates to PHY/DL monitors',
       ],
       accept=[
           'No advertised capability lacks an implementation/test owner',
           'Endpoint-inapplicable register fields follow specified reserved behavior',
       ])


ticket(29, 'Implement MSI generation and interrupt configuration',
       '6.1 7.7 2.2.8.1', [25, 27],
       work=[
           'Acquire referenced normative MSI register definition where Base1.1 delegates to companion spec; track any unresolved fields explicitly',
           'Implement one-vector MSI capability, address/data programming, enable and documented pending-event behavior',
           'Generate legal memory-write MSI with ordering and BME interactions; suppress legacy INTx when MSI enabled',
           'Advertise no MSI-X; implement any applicable legacy INTx fallback or explicitly justify its absence from profile',
       ],
       tests=[
           'Program 32/64-bit MSI addresses and event sequences; test enable/disable, BME, backpressure and reset',
           'Scoreboard address, data, event count and ordering relative to application writes',
       ],
       accept=[
           'One accepted event produces the documented interrupt transaction without duplication',
           'Register layout is source-backed, not inferred from the Base1.1 cross-reference alone',
       ])


ticket(30, 'Implement required PCI-PM capability and device power states',
       '5.1 5.3 5.5 5.6 7.6', [17, 18, 27],
       work=[
           'Obtain companion PCI-PM details referenced by section7.6 and record exact revision',
           'Implement mandatory D0/D3hot and required link power protocol; advertise D1/D2/auxiliary wake only when physically supported',
           'Coordinate transaction drain, config visibility, PME policy, PM DLLPs and L1/L2/L3-ready sequences',
           'Separate optional ASPM L1 from software-PM obligations and document D3cold reset/retention behavior',
       ],
       tests=[
           'Write PM controls during outstanding posted/non-posted traffic, exercise PME enabling/status and allowed wake sources',
           'Check drain/ack ordering, state access rules, reset retention and absent auxiliary power cases',
       ],
       accept=[
           'Mandatory PM transitions complete without packet loss or deadlock',
           'Capabilities match chip and system support and companion definitions are resolved',
       ])


ticket(31, 'Implement required ASPM L0s and conditional L1',
       '5.4 4.2.6.6 4.2.6.7', [17, 28, 30],
       work=[
           'Implement mandatory L0s support, transmit idle entry policy, independent receive tolerance and FTS exit',
           'Advertise measured/budgeted L0s exit latency and preserve higher-layer timer rules',
           'Implement ASPM L1 only if explicitly selected and supported; otherwise advertise its absence while maintaining software-PM behavior',
           'Keep advertised L0s exit latency a build parameter; PCIE-040 binds it to the PCIE-046/008 receive relock budget rather than to logical timing alone',
       ],
       tests=[
           'Test all ASPM control settings and traffic arrival around idle-entry and exit boundaries',
           'Ensure TX-disabled L0s entry still tolerates peer RX-direction L0s; verify idle deadline from source',
       ],
       accept=[
           'Rev1.1 L0s obligations are tested even if early bring-up disables ASPM',
           'All advertised exit latencies bound observed behavior',
       ],
       spice='Replay idle/FTS patterns through PCIE-009 at hardware-model corners and validate electrical settle/relock budget.')


ticket(32, 'Implement baseline error reporting and poisoned-data policy',
       '2.7.2 6.2', [20, 21, 23, 25, 28],
       work=[
           'Map correctable, non-fatal and fatal events to baseline status, Device Control gates and error messages',
           'Implement poisoned-data propagation/discard policy and advisory non-fatal distinctions',
           'Arbitrate simultaneous errors and avoid recursive error storms; preserve first useful diagnostic context',
           'Audit endpoint-only applicability; root error interrupts and bridge mapping are excluded',
       ],
       tests=[
           'Inject bad LCRC, malformed/unsupported requests, unexpected completions, poison and completion/replay timeout',
           'Sweep reporting enable bits and concurrent events; check status W1C and message suppression',
       ],
       accept=[
           'Each injected error has a deterministic source-cited response and no silent data corruption',
           'Baseline behavior works without advertising optional AER',
       ])


ticket(33, 'Assess optional ECRC generation and checking',
       '2.2.3 2.7.1', [22, 32],
       work=[
           'Decide ECRC support separately from mandatory hop LCRC; record profile decision',
           'If enabled implement digest placement, invariant-field CRC rules and generation/check enables; otherwise handle TD packets as required without false capability advertisement',
           'Document effect on packet buffers and payload length accounting',
       ],
       tests=[
           'Test known ECRC vectors, invariant/mutable field mutations, bad digest, missing digest and back-to-back TD packets',
           'Check advertised feature-disabled behavior as well as enabled mode',
       ],
       accept=[
           'Explicit implement-or-omit disposition with source citations',
           'If implemented all ECRC fault and control combinations are covered',
       ],
       gate='conditional')


ticket(34, 'Assess optional AER and extended capability space',
       '7.9 7.10', [28, 32],
       work=[
           'Record decision on optional AER; if omitted ensure baseline reporting and extended-space reads remain correct',
           'If enabled implement endpoint AER header/status/masks/severity/header log and first-error behavior with no root-only registers',
           'Define linked-list layout and coherent logging under simultaneous errors',
       ],
       tests=[
           'Walk extended capability chain and test W1C/mask/severity/first-error cases with simultaneous injections',
           'If omitted verify no false AER advertisement and baseline errors remain visible',
       ],
       accept=[
           'All optional-capability decisions are explicit',
           'Advertised AER passes bit-attribute and fault-injection matrix',
       ],
       gate='conditional')


ticket(35, 'Implement reset domains and link-down cleanup',
       '6.6 2.9 4.2.4.5', [19, 21, 25, 27, 30],
       work=[
           'Implement Fundamental Reset/PERST# and Hot Reset with exact per-register sticky/retained/reset attributes',
           'Synchronize deassertion per clock domain and gate activity while clocks/PHY are not ready',
           'Flush or fail pending requests, retry entries, credits, interrupts and application state according to reset type',
           'Define link-down software-visible outcomes independently of full chip reset',
       ],
       tests=[
           'Assert resets at each LTSSM/DL phase and during config, MSI, replay and requester activity',
           'Compare reset-value/retention matrix, ensure no stale completion and successful retraining afterward',
       ],
       accept=[
           'Every state element has a documented reset/retention owner',
           'Random reset stress returns to enumerable operation without stale traffic',
       ])


ticket(36, 'Build endpoint memory application and request interface',
       '2.1.1.1 2.3 6.4', [24, 25, 27],
       work=[
           'Provide a small SV BAR register/RAM application with version, scratch, counters and interrupt trigger',
           'Define request/response valid-ready interfaces, byte strobes, 64-bit addresses, tags and error responses',
           'Define side effects once per accepted write and application latency bounds; no specific DMA engine is required',
           'Expose completion-safe resource partitioning and synchronization rules',
       ],
       tests=[
           'Read/write BAR using mixed sizes and byte enables while issuing requester traffic and interrupt triggers',
           'Retry previously sent packets and verify side effects occur once; apply application backpressure',
       ],
       accept=[
           'Application supports end-to-end observable enumeration/MMIO/MSI demonstration',
           'Bus handshakes cannot lose requests or starve mandatory completions',
       ])


ticket(37, 'Disposition out-of-profile topology and optional capabilities',
       '1.3 6.5 6.7 6.8 6.9 6.10 7.5.3 7.8.9 7.8.10 7.8.11 7.8.12 7.8.13 7.8.14 7.11 7.12 7.13 7.14 7.15 7.16 7.17 7.18 7.19 A', [1, 27, 28],
       work=[
           'Review every mapped section for endpoint obligations before excluding root, switch, bridge, slot-controller, multi-function and isochronous implementation',
           'Record optional VC expansion, DSN, power budgeting, vendor extensions and AER/ECRC decisions separately',
           'Retain endpoint obligations for Set_Slot_Power_Limit reception, hot reset, error handling and default VC even when associated infrastructure is outside scope',
           'Document unimplemented requests, messages, config offsets and capability-chain behavior',
       ],
       tests=[
           'Send root/bridge/slot-only controls and unsupported messages to endpoint; check required ignore/UR/error behavior',
           'Verify all reserved config locations and absent capabilities respond as specified',
       ],
       accept=[
           'Every omitted feature has applicability rationale, source and negative-test owner',
           'No entire chapter is excluded merely because some sections apply to switches',
       ])


ticket(38, 'Implement endpoint system messages and slot power-limit handling',
       '2.2.8 6.8 6.9', [22, 23, 28, 30, 32],
       work=[
           'Decode supported PM, error and Set_Slot_Power_Limit messages and route to owning blocks',
           'Implement captured slot power limit scale/value behavior and related capability status as applicable',
           'Apply required ignore/UR policy to vendor-defined and ignored messages; do not generate unsupported messages',
           'Arbitrate message TX with completion, MSI and memory traffic without violating ordering',
       ],
       tests=[
           'Inject each message family with legal/illegal routing, length and payload; test repeated power-limit updates',
           'Check register reflection, PM/error routing and no unintended BAR side effects',
       ],
       accept=[
           'Every Rev1.1 endpoint message has an explicit tested disposition',
           'Message traffic cannot deadlock completion or credit returns',
       ])


ticket(39, 'Integrate endpoint top and run enumeration-to-MMIO regression',
       '1.5 2 3 4 7', [16, 26, 28, 29, 30, 31, 32, 35, 36, 38],
       work=[
           'Connect SV logical PHY, DLL, TL, config, PM, reset and application through PCIE-004 interface',
           'Define synthesis parameters and bounded storage with documented resource estimates',
           'Add pyuvm root-port boot sequence through Detect, L0, DL initialization, config enumeration, BAR assignment and command enable',
       ],
       tests=[
           'Run memory reads/writes, MSI and requester completions concurrently with replay and credit starvation',
           'Repeat complete startup from multiple seeds, peer reset, hot reset and link loss; check data and control scoreboards',
       ],
       accept=[
           'Single documented command demonstrates full digital endpoint behavior',
           'No dropped, duplicated or reordered transaction outside permitted ordering rules',
       ])


ticket(40, 'Integrate PHY macros and digital core into the mixed-signal top',
       '4.1 4.3 6.6', [7, 8, 49, 55, 59, 60],
       work=[
           'Integrate the hardened digital core and the PCIE-007/008/049 PMA macros in a mixed-signal top: macro placement, analog and digital supply separation, guard rings and power-domain boundaries',
           'Close timing on the digital-to-PMA parallel interfaces and the recovered-clock crossing using macro timing abstracts',
           'Verify the top with the PCIE-060 co-simulation method (digital RTL or gate level with behavioral or extracted PMA models) and record what each run covers',
           'Pass top-level DRC, LVS and antenna checks with documented waivers',
           'Bind N_FTS, Extended Synch use and L0s exit latency parameters to the PCIE-046/008 receive relock budget and verify them in co-simulation',
       ],
       tests=[
           'Run the PCIE-039 enumeration regression through behavioral PMA models connected at the integrated top',
           'Assert idle, detect, polarity, recovered clock and reset mapping between core and PMA macros',
       ],
       accept=[
           'Integrated top is DRC/LVS clean with waivers documented',
           'Digital-to-PMA interface timing closes at all corners',
       ],
       spice='Re-simulate the PMA macros with top-level supply, substrate and coupling parasitics where extractable; report any degradation against PCIE-007/008/049 results.')


ticket(41, 'Run lint, synthesis, CDC and reset signoff for the integrated core',
       '1.5.4 4.2 4.3.1.1', [39, 50, 51],
       work=[
           'Add lint and Yosys synthesis targets with the SKY130 standard-cell library for the integrated core; record versions',
           'Run CDC and reset-domain analysis for the logical, PLL-derived TX and recovered RX clocks; audit generated clocks, false paths and multicycle constraints for PCIE-055',
           'Report pre-layout timing at all selected corners with OpenSTA and area estimates; try equivalent wider or slower pipelines without removing mandatory endpoint behavior',
           'Escalate a pre-layout timing miss to the PCIE-001 datapath decision',
       ],
       tests=[
           'Run the pyuvm regression on the synthesizable top after lint fixes',
           'Run the regression on the post-synthesis netlist with SKY130 functional cell models where the simulator supports them',
       ],
       accept=[
           'No inferred latches, unintended memories or unexplained unconstrained paths',
           'CDC constraints and reports are complete and handed to PCIE-055',
       ])


ticket(42, 'Close digital protocol coverage and stress recovery',
       '2 3 4.2 5 6 7', [39, 41, 33, 34, 37],
       work=[
           'Collect coverage by reviewed requirement ID, TLP class, register field, LTSSM transition, timer boundary and error class',
           'Add long-run constrained-random traffic with independent scoreboards and reproducible seeds',
           'Audit fairness/deadlock, credit conservation, replay wrap and repeated reset/power cycles',
           'Review requirement-candidate dispositions and fill coverage gaps including PDF-only tables/diagrams',
       ],
       tests=[
           'Run deterministic boundary suite plus documented multi-seed soak; bound expected progress with watchdogs',
           'Mutate representative CRC, credit and state-transition behavior to demonstrate monitors fail',
       ],
       accept=[
           'All applicable reviewed baseline requirements link to passing checks or explicit justified waivers',
           'No untriaged failure or unreviewed mandatory rule remains at completion',
       ])


ticket(43, 'Qualify electrical path across corners and expose limits of simulation',
       '4.3', [7, 8, 9, 40, 49, 52],
       work=[
           'Run final chosen driver/channel/RX model suite and archive configuration, plots and numerical margins',
           'Audit mask measurement, de-emphasis, jitter transfer, idle, detect and receive tolerance at supported corners',
           'Separate modeled results from hardware compliance; estimate BER evidence needed and plan equipment measurements',
           'Reject circuit if compliant arbitrary-data TX/RX cannot be demonstrated; do not lower link speed and label it Gen1',
           'Under the PCIE-003 digital-only fallback, record the electrical path as not implemented rather than qualified',
       ],
       tests=[
           'Generate all analog stimuli from pyuvm regression manifests including training, compliance and stress patterns',
           'Correlate digital symbol events with analog decoded bits and lock/drop events',
       ],
       accept=[
           'Every applicable electrical requirement has a model result or explicit pending laboratory measurement',
           'No full PCIe compliance claim from transient ngspice alone',
       ],
       spice='Batch all PVT/model corners; verify timestep convergence and reproducibility. Include deliberately bad channels and skew so limit checks are demonstrated to fail.')


ticket(44, 'Validate silicon bring-up and host interoperability',
       '1.4 4.3 6.6 7', [58],
       work=[
           'Design or select a test board carrying the packaged chip with a PCIe edge connector or adapter, REFCLK, PERST#, supplies and test access, after reviewing the companion form-factor specification',
           'Bring up silicon through the test interface and PHY loopback before host attachment; then verify host enumeration, BAR/MMIO, MSI, power transitions and reset/recovery',
           'Measure TX eye, receiver tolerance, lock time and power against PCIE-043 predictions and update models with provenance',
           'Record host, platform and instrument limits; certified compliance is not implied',
       ],
       tests=[
           'Replay host-observed transactions as pyuvm regressions and add any interoperability corner cases',
           'Compare real read/write/interrupt outcomes with simulation reference expectations',
       ],
       accept=[
           'Repeatable bring-up and host demo commands are documented, or the ticket closes with a reviewed not-performed disposition if no silicon is fabricated',
           'Outstanding compliance and electrical gaps are explicit; project completion is not confused with certified compliance',
       ],
       spice='Compare measured board waveforms with final ngspice predictions and update model parameters with provenance; rerun margins after fitting.',
       gate='conditional')


ticket(45, 'Qualify SKY130 transistor-level PHY building blocks first',
       '4.2.1.1 4.3.2.2 4.3.3', [3, 6, 9, 50],
       work=[
           'Following docs/phy-architecture.md, design and qualify building blocks before full TX/RX integration: current-mode buffer, latch and 2:1 mux, clock divider, standard-cell-to-current-mode level conversion, sampler/comparator and a VCO candidate',
           'Use the pinned SKY130 ngspice models and corners; choose device flavors (1.8 V core, 3.3 V or other devices where needed) with documented reasons; transition frequency is not a guaranteed digital toggle rate',
           'Lay out each cell in Magic, pass DRC/LVS and simulate extracted netlists; schematic-only results do not qualify a cell',
           'Measure the maximum reliable rate of standard-cell serializer stages versus custom current-mode stages and report the partition evidence to PCIE-003/007/008',
           'Deliver an edge-by-edge timing budget for the final serializer stages, including retiming and race avoidance',
           'Record quantitative pass/fail or a documented rejection; a rejection is reported to the user under the PCIE-003 fallback, never silently worked around',
           'Qualify cells with ideal bias sources; PCIE-007/008/049 re-qualify them with the PCIE-059 bias circuits and record any difference',
       ],
       tests=[
           'Generate independent expected bit sequences through PCIE-009; compare sampled mux and latch outputs, exercising persistent opposite inputs and phase boundaries',
           'Cover all input combinations, adjacent transitions, reset and deterministic phase restart; deliberately swap inputs or skew clocks to prove checker failure',
       ],
       accept=[
           'Each cell has schematic, layout, DRC/LVS, extracted corner results, bias, power and timing margins with reproducible commands',
           'No ideal zero-delay selectors or unextracted results are used to claim success',
       ],
       spice='Run DC, loaded transition, fast select, latch/divider, sampler and VCO studies on schematic and extracted netlists across tt/ff/ss/sf/fs, temperature, supply and mismatch; demonstrate timestep convergence from <=10 ps and report glitches, setup/hold aperture, swing, jitter and power. Archive pass and deliberately failing fixtures.')


ticket(46, 'Assess on-chip CDR feasibility and lock-time budget before PHY layout',
       '4.2.4.3 4.2.6.6 4.3.1.1 4.3.1.8 4.3.4', [3, 6, 50],
       work=[
           'Study candidate SKY130 CDR architectures (PLL-based, bang-bang with phase interpolator, oversampling) at behavioral level and at transistor level for the critical sampler and phase-detector blocks',
           'Budget CDR lock and relock time against protocol deadlines: L0s exit within the advertised N_FTS FTS ordered sets (section 4.2.4.3: about 4 µs at N_FTS 255), Polling and Recovery timers and electrical-idle exit; record the N_FTS and L0s exit latency the receiver can honestly support for PCIE-017/031',
           'Budget jitter tolerance and frequency tracking against section 4.3.4 receiver limits under the PCIE-001/003 reference-clock and SSC policy',
           'Identify which receive blocks need transistor-level qualification in PCIE-045',
           'Produce a go, no-go or unknown recommendation and report a no-go or unknown result to the user before full PHY layout begins',
       ],
       tests=[
           'Drive a behavioral CDR model with pyuvm-generated training, FTS and data streams; measure modeled lock time against the N_FTS budget and detect false lock',
           'Deliberately exceed the jitter or frequency budget and confirm the checks fail',
       ],
       accept=[
           'Recommendation states supportable N_FTS, lock time, jitter tolerance and remaining unknowns with sources',
           'Unresolved model or component gaps are explicit blockers, not passes',
       ],
       spice='Simulate the critical sampler and phase-detector front end with nonlinear models at the 400 ps UI where trustworthy models exist; label behavioral loop results as assumptions until hardware characterization.',
       priority='P0')


ticket(47, 'Build data-link partner models: DLLP, CRC, ACK/NAK replay and flow control',
       '3.1 3.3 3.4 3.5 2.6', [5],
       work=[
           'Implement independent Python DLLP encode/decode for ACK/NAK, InitFC1/2, UpdateFC and PM DLLPs with CRC16 from section 3.4',
           'Implement independent LCRC and 12-bit sequence-number references from section 3.5',
           'Implement a root-port data-link partner: DL state, InitFC exchange, credit accounting, ACK/NAK generation with configurable delay, drop and corruption, and replay of its own TLPs',
           'Attach the partner to the PCIE-005 symbol agent so PHY and data-link tickets share one stack',
       ],
       tests=[
           'Self-check CRC16 and LCRC against cited and hand-computed vectors; corrupt each field and confirm detection',
           'Run partner-to-partner loopback in Python with injected loss, NAK and sequence wrap; check replay delivers each TLP exactly once',
       ],
       accept=[
           'Reference vectors carry source citations and expected bytes',
           'Fault injection is controllable per packet and reproducible by seed',
       ])


ticket(48, 'Build TLP, configuration and enumeration reference models',
       '2.1 2.2 7.2 7.5', [5],
       work=[
           'Implement independent Python TLP header build and parse for memory, configuration, completion and message types with explicit byte order',
           'Implement a root-complex enumeration sequence: configuration reads and writes, BAR sizing, capability walk, command enable and MSI programming',
           'Evaluate cocotbext-pcie (MIT licence) as a TLP-level root complex and enumeration model; adopt it only where it is independent of DUT code, pin its version in the PCIE-002 environment and record which Rev1.1 rules it does not model',
           'Expose a TLP-level interface that transaction-layer tickets can use before PHY and data-link integration, and through PCIE-047 for full-stack tests',
       ],
       tests=[
           'Round-trip a legal TLP matrix and compare with hand-built byte vectors carrying source citations',
           'Run enumeration against a minimal Python configuration-space model and confirm BAR sizing and capability walk',
       ],
       accept=[
           'Transaction-layer tickets can test against TLP-level models without waiting for PHY/DLL integration',
           'Any third-party model version, licence and coverage gaps are recorded',
       ])


ticket(49, 'Design on-chip PLL and clock distribution from the 100 MHz reference',
       '4.3.1.1 4.3.3 4.3.4', [3, 6, 45, 59],
       work=[
           'Design a SKY130 PLL from the host 100 MHz REFCLK to the PCIE-003 serializer clock (2.5 GHz full-rate or 1.25 GHz half-rate), the digital core clock and any CDR reference',
           'Own the REFCLK input receiver from pad to PLL; its electrical requirements (levels, jitter) are defined in the PCI Express CEM specification, not the Base specification, so obtain the matching CEM revision or record the gap as a blocker',
           'Budget output jitter against section 4.3.3 transmitter jitter limits, SSC tracking bandwidth and lock time; define lock detect and reset',
           'Design clock distribution and duty-cycle control to the serializer and deserializer',
           'Lay out, extract, pass DRC/LVS and deliver a macro with abstracts for PCIE-040',
           'Deliver preliminary PLL macro abstracts (size, pin placement, supplies) early to the PCIE-060 loopback top and keep them current',
       ],
       tests=[
           'Drive the PLL behavioral model with REFCLK including SSC and frequency offset through pyuvm; assert no TX traffic before lock and correct lock-loss handling',
           'Deliberately exceed the jitter or lock budget and confirm the checks fail',
       ],
       accept=[
           'PLL macro meets the clock and jitter budget at all corners with modeled results, or the shortfall is quantified',
           'Lock, reset and lock-loss behavior is defined and verified',
       ],
       spice='Simulate VCO, dividers, phase-frequency detector and charge pump at transistor level across corners; estimate jitter with a documented method; verify loop stability and lock using behavioral plus extracted blocks; verify timestep convergence.')


ticket(50, 'Reproduce SKY130 PDK, OpenROAD and OpenLane implementation environment',
       '1.5.4.4', [2],
       work=[
           'Install a pinned SKY130 PDK build with the PDK version manager used by the selected OpenLane release (volare or ciel); record the exact PDK commit and keep the PDK outside the repository',
           'Install OpenLane 2 (or LibreLane, its continuation) using Docker or Podman, which are available on this machine, or Nix; use classic OpenLane only if a fabrication harness requires it; record the exact release',
           'Install standalone OpenROAD and OpenSTA at the version bundled by the selected OpenLane release for interactive floorplan, timing and debug work; document any version difference',
           'Install signoff tools used by the flow (Magic, KLayout, netgen) and xschem for SKY130 schematics; keep OpenLane-bundled Yosys separate from oss-cad-suite Yosys and record both versions',
           'Add documented one-command launchers, git-ignore run directories and PDK caches, and record machine limits (16 cores, 14 GB RAM) that may constrain full-core runs',
       ],
       tests=[
           'Harden a trivial registered SystemVerilog block through the full flow and run a pyuvm test against both its RTL and its gate-level netlist',
           'Introduce a deliberate timing violation and an LVS mismatch once and confirm the flow reports failure',
       ],
       accept=[
           'Fresh documented environment hardens the smoke design to GDS with DRC, LVS and STA reports and no hidden shell state',
           'PDK, OpenLane, OpenROAD, Magic, KLayout, netgen and Yosys versions and exact commands are recorded',
       ],
       spice='Run SKY130 ngspice models on an inverter transient from the pinned PDK and compare propagation delay with the corresponding standard-cell Liberty data within a documented tolerance.')


ticket(51, 'Define technology wrappers for memories, synchronizers and clock gating',
       '4.2.7', [4],
       work=[
           'Define wrappers for single- and dual-port memories, multi-flop synchronizers, reset synchronizers and clock gating with behavioral and SKY130 implementations selected by build configuration',
           'Forbid technology primitives, initial-value registers used as reset, and simulation-only constructs in shared RTL; every state element gets an explicit reset or a documented no-reset rationale',
           'Document memory read latency, write-collision and reset semantics identically for both implementations',
           'Add lint targets that build the shared RTL for the behavioral and SKY130 configurations',
       ],
       tests=[
           'Run identical pyuvm wrapper tests against behavioral and SKY130 functional models',
           'Check synchronizer and FIFO pointer crossings with randomized clock ratios and confirm an injected missing-synchronizer fault is detected',
       ],
       accept=[
           'Shared RTL contains no technology primitives outside the wrappers',
           'Behavior of every wrapper is identical across implementations at the documented interface',
       ])


ticket(52, 'Design high-speed I/O pads, ESD protection and package model',
       '4.3.1.8 4.3.3 4.3.4', [3, 6, 50],
       work=[
           'Select or design pads for the PCIe TX/RX pairs and REFCLK with ESD protection whose capacitance and series resistance suit 2.5 Gb/s; standard SKY130 GPIO pads are not assumed adequate; the REFCLK input receiver circuit itself belongs to PCIE-049',
           'Model bond-wire or package, pad and ESD parasitics for PCIE-007/008/043 simulations, with provenance',
           'Check ESD structures against PDK rules and document protection as modeled, not certified',
           'Deliver pad cells with DRC/LVS and abstracts for PCIE-057',
       ],
       tests=[
           'Include pad and package model identifiers in PCIE-009 manifests so electrical results trace to the pad configuration',
           'Confirm a deliberately degraded pad model makes PCIE-043 limit checks fail',
       ],
       accept=[
           'Pad and package models used by PCIE-007/008/043 have documented provenance',
           'Pads pass DRC/LVS with abstracts delivered',
       ],
       spice='Simulate pad, ESD and package loading in transient with SKY130 models and extracted parasitics at corners; report the effect on the TX eye and the RX input.')


ticket(53, 'Select SKY130 memories and map endpoint buffers',
       '2.6 3.5.2', [50, 51],
       work=[
           'Compare OpenRAM-generated SKY130 SRAM macros, DFFRAM and flip-flop arrays for the retry buffer, receive credit buffers and other storage, using sizes documented by PCIE-021/026 and the PCIE-001 profile',
           'Record macro timing, area, port configuration, power pins and integration requirements; re-check sizes when PCIE-039 fixes final storage',
           'Implement the SKY130 memory-wrapper variants from PCIE-051 with the selected memories',
       ],
       tests=[
           'Run the PCIE-051 wrapper tests against the selected macro functional models, including read-during-write and reset behavior',
           'Exercise full-buffer and wrap conditions of the retry and credit buffers on the SKY130 memory configuration',
       ],
       accept=[
           'Each buffer has a selected implementation with timing and area evidence',
           'Macro behavior matches the shared wrapper contract',
       ])


ticket(54, 'Harden early PHY logic blocks in SKY130 to calibrate timing',
       '4.2.1 4.2.2 4.2.3', [12, 50],
       work=[
           'Harden the 8b/10b, scrambler and framing blocks with OpenLane as an early calibration of SKY130 timing at the PCIE-001 logical clock',
           'Report setup and hold slack at all selected corners, area and power; escalate a miss at the slow corner to the PCIE-001 datapath decision',
           'Record OpenLane configuration and flow settings as the starting point for full-core hardening',
       ],
       tests=[
           'Run the PCIE-010/011/012 pyuvm suites against the gate-level netlists of the hardened blocks',
           'Confirm a deliberately inserted functional mutation in the netlist is caught by the same suites',
       ],
       accept=[
           'Timing results at every corner are recorded with exact flow versions and configuration',
           'Gate-level behavior matches RTL under the existing suites',
       ])


ticket(55, 'Harden the full endpoint core with OpenLane and sign off physical checks',
       '1.5 4.2', [3, 41, 53, 54],
       work=[
           'Floorplan, power grid, placement, clock-tree synthesis for every clock domain, routing and fill for the integrated core with the selected memories',
           'Close static timing at all selected corners including hold and clock-domain crossing constraints, and confirm CDC constraints match PCIE-041 analysis',
           'Pass DRC (Magic and KLayout), LVS (netgen), antenna and IR-drop checks; record every waiver with justification',
           'Report area, utilization, power and per-domain timing; try documented flow and pipeline optimizations without removing mandatory endpoint behavior',
           'Deliver the hardened digital core as a macro with abstracts for PCIE-040',
       ],
       tests=[
           'Run the PCIE-039 integrated regression on the post-synthesis netlist',
           'Check reset, clock-domain and memory behavior where gate-level simulation differs from RTL',
       ],
       accept=[
           'Signoff reports are clean or carry justified waivers, with exact versions and commands',
           'Timing closes at all selected corners, or the failure and attempted optimizations are documented',
       ])


ticket(56, 'Verify gate-level ASIC netlist and RTL equivalence',
       '2 3 4.2', [42, 55],
       work=[
           'Run formal equivalence between RTL and the synthesized and final netlists with eqy or another documented method, scoped to supported constructs',
           'Run selected PCIE-042 pyuvm regressions on the post-route netlist with SDF back-annotation using a simulator that supports the SKY130 cell models and SDF; record simulator limitations',
           'Check reset and X-propagation behavior on the gate-level netlist',
       ],
       tests=[
           'Repeat the enumeration-to-MMIO, replay and credit-starvation scenarios with reproducible seeds at gate level',
           'Insert a netlist mutation and confirm equivalence or simulation detects it',
       ],
       accept=[
           'Equivalence passes for every checked stage or each unproven region is explained',
           'Gate-level regressions agree with RTL results and limitations are recorded',
       ])


ticket(57, 'Integrate chip top: pad ring, harness, test access and fabrication route',
       '4.3 6.6', [40, 52],
       work=[
           'Identify a currently available SKY130 fabrication route and its harness, area, I/O and deadline constraints; record clearly if none is available',
           'Integrate the hardened core into the chosen harness or pad frame with clock, reset (PERST#), power and I/O assignments that match the PCIE-003 chip architecture',
           'Add test access: PHY-boundary loopback, pattern generator and checker, and status registers reachable through a slow interface, so the core can be exercised without a working 2.5 Gb/s link',
           'Re-run full-chip DRC, LVS, STA and the route-specific precheck',
       ],
       tests=[
           'Run the integrated regression through the harness test interface and loopback paths',
           'Confirm a broken loopback or misassigned pin is detected',
       ],
       accept=[
           'Integration passes route-specific prechecks or blockers are recorded',
           'Test access lets silicon be evaluated without a host link',
       ])


ticket(58, 'Prepare ASIC tapeout signoff and post-silicon test plan',
       '4.3', [43, 56, 57],
       work=[
           'Assemble final GDS, signoff reports, versions, waivers and documentation for the chosen fabrication route',
           'Write a post-silicon bring-up and test plan: board, supplies, clocks, test interface, loopback, and later link tests',
           'Do not submit for fabrication or incur cost without explicit user approval',
       ],
       tests=[
           'Map each post-silicon test to its pre-silicon pyuvm counterpart and expected result',
           'Define pass/fail criteria for first-silicon bring-up',
       ],
       accept=[
           'Tapeout package is complete and reproducible from recorded commands',
           'Submission happens only after explicit user approval',
       ],
       gate='conditional')


ticket(59, 'Design bias, reference and termination-calibration circuits',
       '4.3.3 4.3.4', [3, 4, 6, 50],
       work=[
           'Design a SKY130 bias reference (bandgap or constant-transconductance bias) and the current distribution feeding current-mode logic, the PLL charge pump, TX driver and RX front end',
           'Design termination calibration if PCIE-007/008 need it, using an on-chip or off-chip precision reference recorded in PCIE-003',
           'Define power-up start-up, enable and settling behavior and report it to the PMA control contract in PCIE-004',
           'Lay out, extract, pass DRC/LVS and deliver a macro with abstracts for PCIE-007/008/049 and PCIE-040',
       ],
       tests=[
           'Model bias-ready and calibration-done handshakes in the behavioral PMA model and assert that no PMA block is enabled before them',
           'Deliberately delay start-up or skew calibration and confirm the checks fail',
       ],
       accept=[
           'Bias and calibration outputs meet their budgets at all corners on extracted layout, or the shortfall is quantified',
           'Start-up never latches into a zero-current state across corners and supply ramps',
       ],
       spice='Simulate bias and calibration circuits on schematic and extracted netlists across corners, temperature, supply ramps and mismatch; include start-up transients and supply sensitivity; verify timestep convergence.')


ticket(60, 'Build an early PHY loopback top with logical PHY and PMA placeholders',
       '4.2 4.2.6.10 4.3', [3, 13, 45, 54],
       work=[
           'Integrate the hardened logical-PHY blocks (8b/10b, scrambling, framing, elastic buffer) with behavioral PMA models and placeholder macro abstracts from PCIE-007/008/049/059 in a loopback test top',
           'Floorplan the top with analog macro placeholders, analog and digital supply domains and the digital-to-PMA interface; close timing on that interface with preliminary abstracts',
           'Select and set up the mixed-signal co-simulation method for PCIE-040 (for example ngspice d_cosim with Verilator) and record what it covers',
           'Swap qualified PCIE-045 cells or early PMA macros in as they become available; the same top must accept final macros by replacing abstracts, with final integration in PCIE-040',
           'Serve as the intermediate milestone between the verified digital core and the signed-off chip, and as a candidate first test chip',
       ],
       tests=[
           'Run TX-to-RX loopback of training sequences, SKP and random encoded data through behavioral and, where available, transistor-level PMA models',
           'Inject lock loss, polarity inversion and clock offset in loopback and confirm detection and recovery',
       ],
       accept=[
           'Loopback top passes DRC/LVS with placeholders and closes interface timing at all corners',
           'Co-simulation method is demonstrated on loopback traffic with documented coverage limits',
       ],
       spice='Co-simulate the loopback path with any available transistor-level PMA blocks and confirm decoded bits match the independent expected stream; label behavioral results as such.')
