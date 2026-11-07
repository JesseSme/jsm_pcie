"""Authored implementation work packages. Generated tickets must not be regenerated after claiming."""
TICKETS = []


def ticket(n, title, refs, deps, work, tests, accept, spice=None, gate='baseline', priority=None):
    TICKETS.append(dict(id=f'PCIE-{n:03}', title=title, refs=refs.split(),
                        dependencies=[f'PCIE-{d:03}' for d in deps], work=work.split('|'),
                        tests=tests.split('|'), acceptance=accept.split('|'),
                        spice=spice, gate=gate,
                        priority=priority or ('P0' if n <= 9 else 'P1')))


ticket(1, 'Freeze endpoint profile and audit normative applicability', '1 1.3.2.2 5.1.1 6 7', [],
       'Produce docs/endpoint-profile.md: Gen1 x1, one PCI Express Endpoint function, Type 0 header, VC0/TC0, 128-byte advertised MPS initially, 64-bit non-prefetchable memory BAR, MSI, fabric-owned TL/DL/logical PHY|Distinguish first L0 bring-up from complete baseline; L0s and PCI-PM obligations cannot be removed merely by disabling ASPM in a prototype|Review every section and candidate in specification/TRACEABILITY.csv; split applicable paragraphs into atomic reviewed requirements including table fields, conditions, device roles and implementation-note classification|Record optional capability omissions and required response behavior; identify missing normative companion specifications (PCI configuration, PM, MSI, CEM/form factor) without inventing their contents',
       'Define legal and forbidden endpoint transactions for the pyuvm scoreboard|Review each advertised capability against its planned test and implementation owner',
       'Profile and mandatory/optional matrix have source citations and no unexplained exclusions|Every candidate has an applicability disposition or an explicit tracked review item; later signoff requires no unresolved applicable rules')
ticket(2, 'Reproduce OSS CAD Suite, pyuvm and ngspice tool environment', '1.5.4.4', [],
       'Add reproducible launcher and dependency lock for cocotb plus pyuvm; use oss-cad-suite/bin/verilator as primary SV simulator and Icarus only for supported subsets|Discover bundled Python rather than assuming bin/python3; reconcile project Python >=3.14 with suite Python ABI and cocotb shared libraries|Record exact simulator, Python, cocotb, pyuvm and ngspice versions; add one documented command each for digital and analog smoke tests|Keep vendored oss-cad-suite and original specifications out of generated change sets',
       'Run a small SystemVerilog clock/reset DUT with a pyuvm test through cocotb and assert that reset changes observable state|Fail intentionally once to prove assertion failures propagate nonzero; restore passing test',
       'Fresh documented environment runs both smoke tests without hidden shell state|Commands, versions and logs are captured; no claim that preinstalled cocotb implies pyuvm availability',
       'Run ngspice -b on a known RC transient and compare measured settling time with analytic RC tolerance; exercise failure handling too.')
ticket(3, 'Resolve board and FPGA I/O feasibility before choosing a physical interface', '4.3 4.3.1.1 4.3.1.8 4.3.2.2', [1,2],
       'Identify exact FPGA, speed grade, package, board, bank voltages, pin mapping and available clocks; until supplied keep hardware approval blocked while digital work continues|Compare ordinary GPIO, dedicated I/O SERDES, native transceiver and external serializer/deserializer candidates using manufacturer data for both TX and RX|Budget 2.5 GT/s NRZ with 400 ps UI, arbitrary encoded data, recovered receive clock, jitter, termination, AC coupling, electrical idle and receiver detection|Evaluate multiphase interleaving or external mux circuitry as an experiment: require sustainable independent data throughput, lane timing, switching bandwidth and receive recovery; multiplying a clock alone is insufficient|Write a sourced go/no-go decision for requested I/O path; any native transceiver or external PHY fallback is a documented scope decision rather than silently replacing GPIO',
       'Define a PHY capability contract and pyuvm fault scenarios for loss of lock, detection failure and electrical idle|Compute encoded-data throughput and clock-to-pin budget independently of the RTL',
       'Every candidate is accepted or rejected with manufacturer limits and a full-duplex budget|No hardware-ready claim while the FPGA or receive solution remains unknown',
       'Sweep proposed output/mux circuits with realistic finite pin edge rates, package parasitics, skew and loads; compare eye opening to 400 ps UI. Reject ideal-source-only demonstrations.')
ticket(4, 'Create PHY boundary and cycle-accurate simulation contract', '1.5.4.4 4.1 4.2', [1],
       'Define fabric-side symbol interface, initially one 8-bit symbol plus K flag per 250 MHz logical cycle; do not label it PIPE compliant without implementing a specific PIPE revision|Separate logical PHY from PMA serialization/CDR through explicit TX/RX symbols, status, electrical-idle, receiver-detect, polarity, power state and lock controls|Define reset behavior, clock domains, backpressure constraints and latency; the physical stream cannot pause when fabric ready is low|Provide adapters for behavioral simulation and later board-specific hardware; avoid double 8b/10b encoding or scrambling in vendor PCS',
       'Use pyuvm driver/monitor agents for each direction; exercise lock loss, asynchronous reset, invalid symbols and idle transitions|Assert deterministic control handshakes and detect data loss under FIFO pressure',
       'Interface specification includes timing diagrams and all control acknowledgments|Simulation adapter can be implemented without deciding a board')
ticket(5, 'Build passive endpoint root-port BFM and independent reference models', '1.5 2.1 3.1 4.2', [2,4],
       'Build pyuvm root-port agent with sequence items for symbols, ordered sets, DLLPs and TLPs; separate active drivers from passive monitors|Implement independent Python packet/CRC/encoding reference models from cited equations and tables; do not import DUT algorithm code|Add deterministic seed handling, packet traces, timeout watchdogs, scoreboard and coverage export',
       'Self-check BFM encode/decode and known vectors without DUT; introduce bad CRC, bad sequence and bad framing vectors that must be detected|Run bidirectional randomized legal traffic with an explicit model contract',
       'Reference vectors carry source citations and expected bytes|Failures include seed, packet context, time and violated requirement ID')
ticket(6, 'Extract electrical limits and ngspice model assumptions', '4.3.1 4.3.2 4.3.3 4.3.4', [1,2],
       'Transcribe each applicable electrical table row, units, min/max, footnotes and measurement point into machine-readable limits with exact citations|Separate transmitter mask, receiver tolerance mask, measurement load and clock recovery measurement assumptions|Define ngspice-supported driver/receiver/package/channel models; if only IBIS is supplied document a validated conversion or alternate characterization rather than assuming native IBIS support|Assign confidence levels to ideal, behavioral, manufacturer and measured models; require PVT and model provenance',
       'Expose limit IDs in digital-to-analog waveform metadata and pyuvm pattern manifests|Check limit-table parsing catches missing units and contradictory min/max bounds',
       'All applicable Chapter 4.3 limits are captured or explicitly marked missing|Review source PDF tables visually; no fabricated compliance thresholds',
       'Provide parameterized differential source, coupling capacitors, termination and channel loads; verify units, DC bias and convergence at nominal conditions.')
ticket(7, 'Design and compare FPGA I/O serialization or external modulation experiments', '4.2.1.1 4.3.2.3 4.3.3', [3,6],
       'Produce candidate schematics/netlists and FPGA toggle schedules for ordinary I/O, I/O SERDES, and permitted external interleaving/mux paths|Map arbitrary 10-bit symbols to phase/data schedules with explicit setup/hold, duty cycle, phase noise and 2.5 GT/s throughput budgets|Include differential drive, amplitude control, de-emphasis, idle behavior and startup transients; do not substitute an RF carrier for PCIe baseband NRZ|Reject candidates that only generate a high-frequency periodic clock or depend on undocumented FPGA overclocking',
       'Export pyuvm-generated arbitrary 8b/10b streams, alternating symbols, long legal runs and compliance sequences to timestamped pin events|Round-trip expected serial bit order and verify every scheduled edge against source symbols',
       'Each experiment has executable netlist, pin schedule, documented assumptions and quantitative pass/fail|At least one candidate meets all modeled TX limits or the ordinary-I/O approach is explicitly rejected',
       'Run transient simulation with finite slew and package/trace effects; sweep mux skew, process/voltage/temperature assumptions and data patterns. Report eye mask violations, differential amplitude, de-emphasis and jitter.')
ticket(8, 'Establish receive sampling, clock recovery and electrical controls feasibility', '4.3.1.8 4.3.1.9 4.3.4', [3,6],
       'Specify RX termination, differential input compatibility, CDR or justified oversampling, comma alignment and receive clock generation at full data rate|Design receiver-detection/electrical-idle control feedback and timeout behavior; include disconnected, powered-down and hot reset cases|Budget frequency offset and jitter tolerance; define lock loss and re-acquisition behavior|Document what is implementable with FPGA digital resources and what requires analog-capable pins or external parts',
       'Drive recovered clock drift, polarity reversal, loss of signal, idle exit and false lock through pyuvm PHY model|Assert no packet delivery before symbol alignment and lock; verify fault-driven recovery',
       'Full-duplex feasibility decision includes RX and control feedback, not TX eye alone|Hardware-dependent work remains blocked if supported input sampling/recovery cannot be established',
       'Sweep input amplitude/common mode, jitter, phase, termination and idle detection thresholds; simulate detection loads and bias startup. Behavioral CDR results must be labeled assumptions until hardware characterization.')
ticket(9, 'Bridge digital patterns to ngspice and produce electrical evidence', '4.2.8 4.3.3.1 4.3.3.2 4.3.3.4', [5,6],
       'Create a converter from timestamped PHY bit/pin events to PWL sources with explicit units, finite rise/fall, bit order and simulator time origin|Create machine-readable analog results with source stream hash, seed, model hashes, corners and electrical limit IDs|Add eye folding using the specified measurement clock recovery method, mask checks and amplitude/jitter/de-emphasis measurements|Keep short transient eye checks distinct from statistically meaningful BER qualification',
       'Generate compliance patterns, legal high-transition and low-transition streams, TS1/TS2, SKP and idle exits using pyuvm|Verify PWL time spacing equals 400 ps per UI at nominal rate and recovered data matches source bits',
       'Regression exits nonzero for a deliberately degraded electrical corner and passes a known analytical fixture|Electrical reports identify unmodeled effects and never assert compliance from ideal eye plots alone',
       'Run ngspice transient batch regressions on all supported corners; set maximum timestep conservatively, initially <= UI/40, and demonstrate convergence by halving it.')
ticket(10, 'Implement 8b/10b encoder and decoder with running disparity', '4.2.1 B', [4,5],
       'Implement synthesizable SV encoder/decoder using Appendix B tables and specified serial bit ordering|Track TX/RX disparity, K symbols, comma detection, invalid codes and disparity errors|Define reset disparity and error interface to LTSSM/data link',
       'Exhaustively test all 256 data values and legal K symbols under both running disparities against independent table model|Decode all 1024 codewords per disparity; verify illegal/disparity errors, round-trip and back-to-back updates',
       'Every Appendix B mapping agrees with reference; illegal codes cannot silently become valid data|Lint and synthesis confirm bounded combinational logic and timing target')
ticket(11, 'Implement scrambling and descrambling', '4.2.3 C.1', [4,5],
       'Implement specified LFSR polynomial, initial value, bit order and advancement rules in SV|Apply exact reset/advance/bypass behavior for COM, SKP, training ordered sets, data and disabled scrambling|Support identical symbol-boundary behavior under stalls in internal pipelines without pausing wire cadence',
       'Compare long randomized streams with independent Python LFSR model|Exercise COM reseed, SKP hold, ordered sets, data/control boundaries, reset and scrambling-disable negotiation',
       'Known Appendix C vectors and independent model match cycle by cycle|No scrambler state advances on prohibited symbols or misses required advances')
ticket(12, 'Implement symbol framing and ordered-set parser/generator', '4.2.2 4.2.4.1 4.2.4.3 4.2.8', [10,11],
       'Implement STP/SDP/END/EDB framing, idle and TS1/TS2/FTS/SKP ordered sets for x1|Validate training fields, lane/link number PAD handling, consecutive-set recognition and malformed frames|Coordinate scrambling, encoding and packet arbitration without dropping or duplicating symbols',
       'Drive all legal packet/ordered-set boundaries and corrupt every ordered-set field class|Verify TS counters reset on broken consecutiveness and no malformed frame reaches TL',
       'Wire sequence matches source framing rules for TLP, DLLP and training traffic|All injected framing faults produce defined error/recovery behavior')
ticket(13, 'Implement clock domains, elastic buffering and SKP compensation', '4.2.7 4.2.4.8', [4,12],
       'Design async FIFOs and synchronized status/reset crossings for user, symbol and receive clocks|Implement x1 elasticity and SKP insertion/removal following source intervals and packet-boundary restrictions|Calculate FIFO depth for frequency offset, SSC assumptions, bursts and recovery latency; x1 does not need multilane deskew|Document overflow/underflow handling and avoid impossible physical-stream backpressure',
       'Use independent clocks with min/max permitted frequency offset and randomized reset phase|Scoreboard data preservation through SKP changes; test FIFO boundary pressure and lock loss',
       'No data loss/reorder under supported clock offsets|CDC/reset review and timing constraints cover every crossing')
ticket(14, 'Implement LTSSM Detect and Polling', '4.2.4 4.2.5 4.2.6.1 4.2.6.2', [4,12],
       'Implement endpoint/upstream-port Detect.Quiet/Active and Polling substates, receiver-detect handshakes and precise timers|Implement TS1/TS2 counting, polarity handling and compliance entry decisions|Parameterize simulation acceleration without changing production time units or off-by-one semantics',
       'Model no receiver, successful detection, detection timeout, reversed polarity, missing/corrupt TS sets and all Polling exits|Check each timer just before, on and after expiry and all count thresholds',
       'State transitions and emitted sets match source transition rules|Fast simulation and production timers are linked by checked conversion')
ticket(15, 'Implement LTSSM x1 Configuration and reach L0', '4.2.6.3 4.2.6.5 4.2.4.7', [14,13],
       'Implement upstream-port link/lane negotiation through Configuration substates with lane zero and width one|Handle peer width proposals, PAD values, polarity, TS2 completion and idle qualification|Expose trained width/speed and link-up only after valid L0 transition',
       'Run pyuvm root-port training from reset to L0 under valid and adversarial TS sequences|Test wrong lane/link numbers, broken consecutive sets, timeout fallback and repeated retraining',
       'Legal root-port BFM reaches x1 2.5 GT/s L0 repeatably|Invalid negotiation cannot falsely assert link-up')
ticket(16, 'Implement Recovery, Disabled, Loopback, Hot Reset and compliance modes', '4.2.6.4 4.2.6.9 4.2.6.10 4.2.6.11 4.2.8', [15],
       'Implement required Recovery lock/config/idle behavior and fallback; Gen1-only negotiation must never claim unsupported speed|Implement Disabled, endpoint loopback, Hot Reset and compliance state data paths and exit rules|Coordinate packet discard, scrambler reset, physical idle and DL state during transitions',
       'Inject symbol lock loss during traffic, directed recovery, peer Hot Reset, loopback requests and compliance entry|Verify stale packets never leak after retrain and legal traffic resumes with fresh DL initialization',
       'Each implemented LTSSM transition has positive and negative tests|Reset and recovery cannot deadlock ongoing DL/TL traffic')
ticket(17, 'Implement PHY L0s, L1 and L2 state behavior', '4.2.6.6 4.2.6.7 4.2.6.8 5.2', [16],
       'Implement independent TX/RX L0s entry/exit including idle and FTS; maintain appropriate higher-layer timers|Implement required software-PM L1 and L2/L3-ready control behavior and wake/reset paths with power manager|Define beacon support/applicability and hardware power/lock acknowledgments',
       'Enter RX L0s while TX stays active and vice versa; test FTS counts and exit latency|Exercise L1/L2 transitions with pending traffic, wake, failed lock and reset',
       'L0s support is retained for Rev1.1 baseline|All power transitions honor advertised exit latencies and specified timer behavior',
       'Use PCIE-009 with actual PHY candidate to check idle entry/exit transients and modeled relock latency; no analog proof from a purely logical status toggle.')
ticket(18, 'Implement DLLP codec and CRC16', '3.4', [5,12],
       'Implement ACK/NAK, InitFC1/2, UpdateFC and PM DLLP fields, reserved bits and CRC16|Route validated DLLPs to dedicated consumers; discard corrupted/unsupported packets per source|Arbitrate DLLP transmit requests with bounded latency requirements',
       'Use golden CRC vectors, random legal DLLPs and bit flips in every field including CRC|Test reserved encodings, truncated frames and concurrent PM/FC/ACK traffic',
       'Invalid CRC cannot change credits or acknowledge a TLP|All DLLP types in baseline encode/decode with exact byte order')
ticket(19, 'Implement Data Link state and flow-control initialization', '3.2 3.3 2.9', [15,18],
       'Implement DL_Inactive/Init/Active rules coordinated with LTSSM and link status|Implement VC0 InitFC phases for posted/non-posted/completion header and data credits|Prevent application TLP emission before DL_Up; clear state on link loss and repeat initialization',
       'Test asymmetric initialization, missing/corrupt InitFC, peer restart and link-down at every phase|Verify DL_Up transitions and credit establishment against independent model',
       'DL_Up only asserts after all required initialization conditions|Link loss reinitializes both credit and reliability state')
ticket(20, 'Implement LCRC, receive sequence checks and ACK/NAK policy', '3.5.3 3.5.1', [18,19],
       'Implement receive TLP LCRC and 12-bit sequence handling with modulo comparison and duplicate rejection|Generate ACK/NAK with specified latency, sequence values and timer rules|Handle EDB/nullified packets and error propagation without committing corrupted payloads',
       'Inject bad LCRC, sequence gaps, duplicates, wraparound, truncation, EDB and legal retransmissions|Check packets reach TL once only; measure ACK/NAK timer boundaries under heavy traffic',
       'No corrupt or duplicate TLP causes application-visible side effects|ACK/NAK content and deadlines match source rules')
ticket(21, 'Implement transmit retry buffer and replay controller', '3.5.2', [18,19],
       'Assign TX sequence numbers and LCRC; retain each sent TLP until valid acknowledgment|Implement replay timer/count, ACK/NAK processing, retry-buffer admission and recovery escalation|Handle sequence wrap, stale/invalid ACKs, link loss and concurrent enqueue/replay without double-credit charging',
       'Drop ACKs, inject NAKs and invalid ACK ranges, force timer expiry and wrap sequence space|Scoreboard replay byte identity, retirement order, bounded buffer use and eventual recovery',
       'Replay never loses an unacknowledged packet or retires one prematurely|Source retry limits/timers are checked at boundaries and lead to correct recovery')
ticket(22, 'Implement TLP header codec and validation', '2.1 2.2.1 2.2.2 2.2.3 2.2.4 2.2.5 2.2.6 2.2.7 2.2.9', [5],
       'Implement synthesizable packet types and serializers/parsers for 3DW/4DW memory, Type0 configuration, completion and supported messages|Validate format/type, length including zero encoding, payload alignment, byte enables, address routing, TD/EP, attributes and requester/completer IDs|Detect 4KB boundary and MPS/MRRS violations as applicable; preserve malformed/unsupported distinction|Centralize SV types with explicitly documented wire byte order',
       'Generate legal packet matrix and one-field mutations, 1DW/maximum lengths, unaligned byte enables and boundary addresses|Compare full emitted bytes and parsed fields with independent Python model',
       'Supported formats round-trip exactly|Illegal inputs are classified without out-of-range array accesses or partial application writes')
ticket(23, 'Implement receive classification and unsupported/malformed handling', '2.3.1 6.5.7', [22,20],
       'Classify posted, non-posted and completion TLPs; validate destination and endpoint capability before dispatch|Implement UR/CA/error-report behavior for unsupported requests and malformed packets with correct posted/non-posted distinctions|Reject locked requests as required for PCI Express Endpoint and avoid producing forbidden I/O or lock requests',
       'Send unsupported memory/config/message types, MRdLk, malformed headers and out-of-range BAR traffic|Check exact completion/error behavior and that invalid posted writes never mutate application state',
       'Every rejected request has source-backed disposition|No unsupported request path blocks valid traffic indefinitely')
ticket(24, 'Implement completer, read splitting and byte-enable semantics', '2.2.9 2.3.1.1', [22,23],
       'Build Cpl/CplD generator with completion status, byte count, lower address, IDs and tags|Split memory read responses by MPS/read completion boundary rules and preserve enabled-byte accounting|Handle zero-length and byte-disabled accesses without unintended side effects; prioritize completion resources to avoid deadlock',
       'Sweep lengths, byte enables, address alignment and completion boundaries; apply arbitrary application response latency|Reassemble split completions in independent scoreboard and check all headers/bytes',
       'Each supported non-posted request completes with correct data/status and within defined service bound|No completion exceeds negotiated limits or returns bytes from another request')
ticket(25, 'Implement requester tags, completion matching and timeout', '2.3.2 2.8 2.2.6.2', [22,24],
       'Implement optional application-facing memory read/write engine as a planned baseline feature; gate requests with Bus Master Enable|Allocate unique tags and support required 64-bit memory addressing; track requested byte ranges and split completion progress|Detect unexpected, duplicate, poisoned, failed and timed-out completions; retire tags safely and report errors|Keep requester resource allocation from starving completer responses',
       'Interleave split completions across tags, reverse response order where legal and exercise status failures|Test timeout boundaries, tag exhaustion, wrong requester/tag, BME disable and reset with requests outstanding',
       'No request tag is reused while outstanding|Exactly one terminal outcome per request and no transmit when BME forbids it')
ticket(26, 'Implement VC0 credits and transaction ordering', '2.4 2.5 2.6 6.3 D', [19,21,22],
       'Track posted/non-posted/completion header/data credit pools in correct units with wrap and infinite-credit encodings|Implement UpdateFC generation/consumption and buffering minimums; charge credits once for original transmissions, not replay|Apply required ordering matrix, relaxed ordering and TC-to-VC0 policy; reserve independent progress for completions|Document FIFO sizing and dependencies with bounded backpressure and no circular wait',
       'Starve each credit class independently, force counter wrap and test infinite-credit advertisement|Run producer/consumer ordering litmus tests and saturation with replay plus completion returns',
       'No transmission consumes unavailable credits; receive buffers cannot overrun legal advertised credits|Ordering scoreboard and bounded-progress checks pass under randomized backpressure')
ticket(27, 'Implement configuration Type0 header and BAR decoding', '7.1 7.2.2.2 7.3 7.4 7.5.1 7.5.2', [23,24],
       'Implement function-zero Type0 config read/write completer with correct BDF capture, byte enables and register attributes|Provide legal development identity parameters; avoid claiming assigned Vendor ID ownership|Implement 64-bit BAR sizing/probe and address masks, Memory Space Enable, Bus Master Enable, status W1C and reserved bits|Use a proposed 4KiB BAR0/BAR1 pair and unused BARs returning zero; exact resource profile is confirmed in PCIE-001',
       'Emulate BIOS/OS enumeration, BAR all-ones probing, relocation, byte writes and command gating|Attempt writes to RO/reserved/W1C fields and accesses to unsupported functions/routing types',
       'Host BFM enumerates one endpoint with consistent resource masks|No register access violates configured attributes and disabled memory decoding produces no side effects')
ticket(28, 'Implement PCI Express capability registers and live status', '7.8.1 7.8.2 7.8.3 7.8.4 7.8.5 7.8.6 7.8.7 7.8.8', [27,16,26],
       'Implement capability linked list and Rev1.1 endpoint Device/Link capabilities, control and status fields|Advertise only x1 Gen1 and implemented MPS, tags, latency and error controls; bind live status to actual state|Route control writes to real behavior, including retrain/power/error controls where endpoint-applicable|Audit all register rows against PDF and reset values; omit slot/root structures for endpoint role',
       'Walk capability list, verify no cycles/overlap and test each bit access attribute and reset value|Change negotiated controls under traffic and compare status updates to PHY/DL monitors',
       'No advertised capability lacks an implementation/test owner|Endpoint-inapplicable register fields follow specified reserved behavior')
ticket(29, 'Implement MSI generation and interrupt configuration', '6.1 7.7 2.2.8.1', [25,27],
       'Acquire referenced normative MSI register definition where Base1.1 delegates to companion spec; track any unresolved fields explicitly|Implement one-vector MSI capability, address/data programming, enable and documented pending-event behavior|Generate legal memory-write MSI with ordering and BME interactions; suppress legacy INTx when MSI enabled|Advertise no MSI-X; implement any applicable legacy INTx fallback or explicitly justify its absence from profile',
       'Program 32/64-bit MSI addresses and event sequences; test enable/disable, BME, backpressure and reset|Scoreboard address, data, event count and ordering relative to application writes',
       'One accepted event produces the documented interrupt transaction without duplication|Register layout is source-backed, not inferred from the Base1.1 cross-reference alone')
ticket(30, 'Implement required PCI-PM capability and device power states', '5.1 5.3 5.5 5.6 7.6', [17,18,27],
       'Obtain companion PCI-PM details referenced by section7.6 and record exact revision|Implement mandatory D0/D3hot and required link power protocol; advertise D1/D2/auxiliary wake only when physically supported|Coordinate transaction drain, config visibility, PME policy, PM DLLPs and L1/L2/L3-ready sequences|Separate optional ASPM L1 from software-PM obligations and document D3cold reset/retention behavior',
       'Write PM controls during outstanding posted/non-posted traffic, exercise PME enabling/status and allowed wake sources|Check drain/ack ordering, state access rules, reset retention and absent auxiliary power cases',
       'Mandatory PM transitions complete without packet loss or deadlock|Capabilities match board support and companion definitions are resolved')
ticket(31, 'Implement required ASPM L0s and conditional L1', '5.4 4.2.6.6 4.2.6.7', [17,28,30],
       'Implement mandatory L0s support, transmit idle entry policy, independent receive tolerance and FTS exit|Advertise measured/budgeted L0s exit latency and preserve higher-layer timer rules|Implement ASPM L1 only if explicitly selected and supported; otherwise advertise its absence while maintaining software-PM behavior',
       'Test all ASPM control settings and traffic arrival around idle-entry and exit boundaries|Ensure TX-disabled L0s entry still tolerates peer RX-direction L0s; verify idle deadline from source',
       'Rev1.1 L0s obligations are tested even if early bring-up disables ASPM|All advertised exit latencies bound observed behavior',
       'Replay idle/FTS patterns through PCIE-009 at hardware-model corners and validate electrical settle/relock budget.')
ticket(32, 'Implement baseline error reporting and poisoned-data policy', '2.7.2 6.2', [20,21,23,25,28],
       'Map correctable, non-fatal and fatal events to baseline status, Device Control gates and error messages|Implement poisoned-data propagation/discard policy and advisory non-fatal distinctions|Arbitrate simultaneous errors and avoid recursive error storms; preserve first useful diagnostic context|Audit endpoint-only applicability; root error interrupts and bridge mapping are excluded',
       'Inject bad LCRC, malformed/unsupported requests, unexpected completions, poison and completion/replay timeout|Sweep reporting enable bits and concurrent events; check status W1C and message suppression',
       'Each injected error has a deterministic source-cited response and no silent data corruption|Baseline behavior works without advertising optional AER')
ticket(33, 'Assess optional ECRC generation and checking', '2.2.3 2.7.1', [22,32],
       'Decide ECRC support separately from mandatory hop LCRC; record profile decision|If enabled implement digest placement, invariant-field CRC rules and generation/check enables; otherwise handle TD packets as required without false capability advertisement|Document effect on packet buffers and payload length accounting',
       'Test known ECRC vectors, invariant/mutable field mutations, bad digest, missing digest and back-to-back TD packets|Check advertised feature-disabled behavior as well as enabled mode',
       'Explicit implement-or-omit disposition with source citations|If implemented all ECRC fault and control combinations are covered', gate='conditional')
ticket(34, 'Assess optional AER and extended capability space', '7.9 7.10', [28,32],
       'Record decision on optional AER; if omitted ensure baseline reporting and extended-space reads remain correct|If enabled implement endpoint AER header/status/masks/severity/header log and first-error behavior with no root-only registers|Define linked-list layout and coherent logging under simultaneous errors',
       'Walk extended capability chain and test W1C/mask/severity/first-error cases with simultaneous injections|If omitted verify no false AER advertisement and baseline errors remain visible',
       'All optional-capability decisions are explicit|Advertised AER passes bit-attribute and fault-injection matrix', gate='conditional')
ticket(35, 'Implement reset domains and link-down cleanup', '6.6 2.9 4.2.4.5', [19,21,25,27,30],
       'Implement Fundamental Reset/PERST# and Hot Reset with exact per-register sticky/retained/reset attributes|Synchronize deassertion per clock domain and gate activity while clocks/PHY are not ready|Flush or fail pending requests, retry entries, credits, interrupts and application state according to reset type|Define link-down software-visible outcomes independently of full chip reset',
       'Assert resets at each LTSSM/DL phase and during config, MSI, replay and requester activity|Compare reset-value/retention matrix, ensure no stale completion and successful retraining afterward',
       'Every state element has a documented reset/retention owner|Random reset stress returns to enumerable operation without stale traffic')
ticket(36, 'Build endpoint memory application and request interface', '2.1.1.1 2.3 6.4', [24,25,27],
       'Provide a small SV BAR register/RAM application with version, scratch, counters and interrupt trigger|Define request/response valid-ready interfaces, byte strobes, 64-bit addresses, tags and error responses|Define side effects once per accepted write and application latency bounds; no specific DMA engine is required|Expose completion-safe resource partitioning and synchronization rules',
       'Read/write BAR using mixed sizes and byte enables while issuing requester traffic and interrupt triggers|Retry previously sent packets and verify side effects occur once; apply application backpressure',
       'Application supports end-to-end observable enumeration/MMIO/MSI demonstration|Bus handshakes cannot lose requests or starve mandatory completions')
ticket(37, 'Disposition out-of-profile topology and optional capabilities', '1.3 6.5 6.7 6.8 6.9 6.10 7.5.3 7.8.9 7.8.10 7.8.11 7.8.12 7.8.13 7.8.14 7.11 7.12 7.13 7.14 7.15 7.16 7.17 7.18 7.19 A', [1,27,28],
       'Review every mapped section for endpoint obligations before excluding root, switch, bridge, slot-controller, multi-function and isochronous implementation|Record optional VC expansion, DSN, power budgeting, vendor extensions and AER/ECRC decisions separately|Retain endpoint obligations for Set_Slot_Power_Limit reception, hot reset, error handling and default VC even when associated infrastructure is outside scope|Document unimplemented requests, messages, config offsets and capability-chain behavior',
       'Send root/bridge/slot-only controls and unsupported messages to endpoint; check required ignore/UR/error behavior|Verify all reserved config locations and absent capabilities respond as specified',
       'Every omitted feature has applicability rationale, source and negative-test owner|No entire chapter is excluded merely because some sections apply to switches')
ticket(38, 'Implement endpoint system messages and slot power-limit handling', '2.2.8 6.8 6.9', [22,23,28,30,32],
       'Decode supported PM, error and Set_Slot_Power_Limit messages and route to owning blocks|Implement captured slot power limit scale/value behavior and related capability status as applicable|Apply required ignore/UR policy to vendor-defined and ignored messages; do not generate unsupported messages|Arbitrate message TX with completion, MSI and memory traffic without violating ordering',
       'Inject each message family with legal/illegal routing, length and payload; test repeated power-limit updates|Check register reflection, PM/error routing and no unintended BAR side effects',
       'Every Rev1.1 endpoint message has an explicit tested disposition|Message traffic cannot deadlock completion or credit returns')
ticket(39, 'Integrate endpoint top and run enumeration-to-MMIO regression', '1.5 2 3 4 7', [16,26,28,29,30,31,32,35,36,38],
       'Connect SV logical PHY, DLL, TL, config, PM, reset and application through PCIE-004 interface|Define synthesis parameters and bounded storage with documented resource estimates|Add pyuvm root-port boot sequence through Detect, L0, DL initialization, config enumeration, BAR assignment and command enable',
       'Run memory reads/writes, MSI and requester completions concurrently with replay and credit starvation|Repeat complete startup from multiple seeds, peer reset, hot reset and link loss; check data and control scoreboards',
       'Single documented command demonstrates full digital endpoint behavior|No dropped, duplicated or reordered transaction outside permitted ordering rules')
ticket(40, 'Implement chosen board PHY adapter and timing constraints', '4.1 4.3 6.6', [3,7,8,9,39],
       'Implement FPGA-specific digital adapter, clock generation and dedicated I/O primitives only for approved feasible hardware path|Create pin assignments, I/O standards, generated clocks and timing/CDC constraints backed by board data|Avoid use of hard endpoint IP that would bypass planned core; document any PMA/PCS hard blocks and exact encoding ownership|If no GPIO solution passes feasibility, leave this ticket blocked with evidence until hardware scope is resolved',
       'Run adapter contract tests against behavioral PHY and vendor primitive models where available|Assert mapping of idle, detect, polarity, recovered clock and reset between core and pins',
       'All constraints correspond to actual part/package/board|Timing closure and digital tests pass without relaxing PCIe serial rate',
       'Replay implemented pin schedules using nonideal driver/channel models from PCIE-007/008/009. All source-cited modeled electrical limits must pass.')
ticket(41, 'Run synthesis, resource, timing and CDC signoff', '1.5.4 4.2 4.3.1.1', [39],
       'Add lint and synthesis targets for supported OSS CAD Suite tools; document vendor-tool dependency if selected FPGA needs it|Measure FIFO/BRAM/LUT/FF use, critical paths and 250 MHz symbol-domain feasibility or approved parallel equivalent|Run CDC/reset analysis and audit generated clocks, false paths and multi-cycle constraints|Separate board-independent synthesis from final board timing closure dependent on PCIE-040',
       'Run pyuvm regression on synthesizable top after lint fixes|Check post-synthesis reset/encoding/packet behavior where supported and flag unsupported primitives',
       'No inferred latches, unintended memories or unexplained unconstrained paths|Final hardware signoff waits for actual routed timing on approved board')
ticket(42, 'Close digital protocol coverage and stress recovery', '2 3 4.2 5 6 7', [39,41],
       'Collect coverage by reviewed requirement ID, TLP class, register field, LTSSM transition, timer boundary and error class|Add long-run constrained-random traffic with independent scoreboards and reproducible seeds|Audit fairness/deadlock, credit conservation, replay wrap and repeated reset/power cycles|Review requirement-candidate dispositions and fill coverage gaps including PDF-only tables/diagrams',
       'Run deterministic boundary suite plus documented multi-seed soak; bound expected progress with watchdogs|Mutate representative CRC, credit and state-transition behavior to demonstrate monitors fail',
       'All applicable reviewed baseline requirements link to passing checks or explicit justified waivers|No untriaged failure or unreviewed mandatory rule remains at completion')
ticket(43, 'Qualify electrical path across corners and expose limits of simulation', '4.3', [7,8,9,40],
       'Run final chosen driver/channel/RX model suite and archive configuration, plots and numerical margins|Audit mask measurement, de-emphasis, jitter transfer, idle, detect and receive tolerance at supported corners|Separate modeled results from hardware compliance; estimate BER evidence needed and plan equipment measurements|Reject circuit if compliant arbitrary-data TX/RX cannot be demonstrated; do not lower link speed and label it Gen1',
       'Generate all analog stimuli from pyuvm regression manifests including training, compliance and stress patterns|Correlate digital symbol events with analog decoded bits and lock/drop events',
       'Every applicable electrical requirement has a model result or explicit pending laboratory measurement|No full PCIe compliance claim from transient ngspice alone',
       'Batch all PVT/model corners; verify timestep convergence and reproducibility. Include deliberately bad channels and skew so limit checks are demonstrated to fail.')
ticket(44, 'Validate hardware bring-up and host interoperability', '1.4 4.3 6.6 7', [40,41,42,43],
       'Document safe board-specific programming, reset, refclock and test connections after physical feasibility approval|Verify real host enumeration, BAR probing/MMIO, MSI, power transitions and reset/recovery|Capture negotiated x1 Gen1 link status, host logs, error counters and measured physical evidence|Record host/platform and instrument limits; companion form-factor specification review is required before attachment',
       'Replay host-observed transactions as pyuvm regressions and add any interoperability corner cases|Compare real read/write/interrupt outcomes with simulation reference expectations',
       'Repeatable host demo and regression commands are documented|Outstanding compliance/electrical gaps are explicit; project completion is not confused with certified compliance',
       'Compare measured board waveforms with final ngspice predictions and update model parameters with provenance; rerun margins after fitting.')

# User-selected hardware and explicitly authorized fit-failure fallback. Keep the
# initial-plan generator consistent with the hand-maintained hardware profile.
TARGET_WORK = {
    3: ['Use Sipeed Tang Nano 20K with GW2AR-LV18QN88C8/I7 as the selected target; confirm board revision, actual bank rails, exposed differential pairs and clock routing from its schematic',
        'Record DS226-2.7E Table 3-17 limits: IDES/OSER 8/10-bit gearbox maximum 1200 Mbps; direct 2500 Mbps operation exceeds the documented rate, so evaluate external serialization and RX recovery without overclocking assumptions',
        'Separate core resource/timing fit from electrical feasibility; if the core cannot fit after documented optimization, the user authorizes a board-independent core using this devices I/O specifications as the electrical modeling target'],
    6: ['Capture Tang Nano 20K GW2AR-18 I/O limits and their datasheet revision alongside PCIe limits; retain them even if core resource fit fails, and do not infer board bank voltage from a device-supported I/O standard'],
    7: ['Constrain simulated FPGA pins to GW2AR-18 supported gearbox rates, finite edge times and selected-bank electrical limits; any 2.5 GT/s output must be generated by explicitly modeled external circuitry'],
    8: ['Treat the documented 1.2 Gb/s IDES8/10 rate as insufficient for direct 2.5 GT/s reception; evaluate a supported parallel/external recovery path using the same FPGA I/O specifications'],
    40: ['Target the Tang Nano 20K pinout and confirmed board revision; PCIE-041 provides the resource-fit decision before final board implementation',
         'If PCIE-041 documents inability to fit after optimization, close this conditional work only with a reviewed not-applicable hardware disposition and a retained I/O-reference simulation adapter; do not claim a working bitstream'],
    41: ['Attempt synthesis and place-and-route for GW2AR-LV18QN88C8/I7; report LUT4, FF, BSRAM, PLL, I/O and clock/timing use against actual available resources',
         'Try bounded storage and equivalent wider/slower fabric pipelines without removing mandatory endpoint behavior; record tool/device support separately from capacity or timing failure',
         'If the core cannot fit after documented optimization, activate the user-authorized I/O-reference fallback: continue the full digital core and pyuvm tests with GW2AR I/O-constrained ngspice models, preserving the failed-fit report'],
    43: ['Under the I/O-reference fallback, qualify modeled GW2AR pin schedules and external circuitry without requiring a board bitstream; retain all Gen1 electrical limits and report infeasible candidates honestly'],
    44: ['If the documented fit-failure fallback is active, record host interoperability and board measurements as not performed; a reviewed not-applicable disposition can close this conditional ticket, but cannot count as hardware verification'],
}
for task in TICKETS:
    number = int(task['id'][-3:])
    task['work'].extend(TARGET_WORK.get(number, []))
    if number == 3:
        task['work'][0] = 'Board selection is resolved; verify exact board revision, bank voltages, usable pin pairs, clocking and electrical models for the selected Tang Nano 20K'
        task['acceptance'][1] = 'No hardware-ready claim while pin routing, electrical levels or receive recovery remain unproven; board selection itself is no longer a blocker'
    if number in {40, 44}:
        task['gate'] = 'conditional'
        task['acceptance'] = [
            'For the hardware route, all preceding hardware criteria and tests pass with board evidence; for documented core fit failure, a signed not-applicable disposition identifies unperformed hardware checks and retained I/O-reference models',
            'Fallback is enabled only by a documented fit decision, not by a tool installation failure or an unsupported electrical assumption',
        ]
    if number == 40:
        task['work'][3] = 'If no physical I/O path passes feasibility, retain a failed electrical result and block hardware claims; the fit-failure fallback does not turn electrical failure into compliance'
        task['dependencies'].append('PCIE-041')
    if number == 41:
        task['acceptance'][1] = 'Report either actual routed timing/resource fit or a reviewed failed-fit decision activating I/O-reference fallback; never label an unplaced design hardware-ready'

# User-approved physical architecture: external raw-bit serialization and RX CDR.
PHYSICAL_WORK = {
    3: ['Freeze the external serializer/deserializer and control-interface contract under docs/physical-interface-decision.md; use four 625 Mb/s TX streams as the first candidate and justify any parallel-width change',
        'Select feasible external clocking, serializer, differential output, RX conditioning/CDR and deserializer candidates with explicit rate, voltage, jitter and select/capture timing budgets'],
    4: ['Keep scrambling and 8b/10b inside the FPGA and define an explicit continuous encoded-bit gearbox between the symbol interface and external parallel pins; four-bit transfers cross ten-bit symbol boundaries',
        'Specify external TX clock/data phase alignment, recovered RX clock domain, electrical controls and initialization handshakes without assuming a specific serializer chip'],
    7: ['Design the approved clocked external serialization path; start with four FPGA streams at 625 Mb/s into a 4:1 serializer and model the complete output stage',
        'Generate external capture/select timing through a justified clocking circuit rather than assuming high-speed mux select can be driven directly by ordinary FPGA logic'],
    8: ['Design the approved external receive conditioning, clock/data recovery and deserializer path, returning a supported parallel interface and recovered clock to the FPGA'],
    9: ['Model parallel FPGA pin events plus serializer clocks through the external circuit rather than replacing the circuit with an ideal 2.5 Gb/s source'],
    40: ['Implement the approved parallel-pin adapter and external-circuit control interface; preserve FPGA ownership of logical PHY coding and scrambling'],
}
for task in TICKETS:
    number = int(task['id'][-3:])
    task['work'].extend(PHYSICAL_WORK.get(number, []))
    if number == 3:
        task['title'] = 'Resolve external serializer/CDR interface feasibility for Tang Nano 20K'
        task['work'][1] = 'Evaluate supported FPGA parallel I/O modes and external serializer/deserializer circuits for both TX and RX; direct single-pair Gen1 GPIO and native-transceiver substitution are outside the approved direction'
        task['work'][4] = 'Write a sourced go/no-go decision for the external serialization/CDR path; a full external PHY that absorbs FPGA logical-PHY functions requires a separate architecture decision'
    if number == 7:
        task['title'] = 'Design external TX serializer, FPGA pin schedule and differential output'
        task['work'][0] = 'Produce candidate schematics/netlists and FPGA parallel toggle schedules for the approved external clocked serializer and output-stage architecture'
        task['tests'].append('Reconstruct arbitrary serial bits from four-way interleaving across 10-bit symbol boundaries, including training, resets and phase-alignment initialization; detect omitted, duplicated or permuted bits')
    if number == 8:
        task['title'] = 'Design external RX clock recovery, deserialization and electrical controls'
        task['tests'].append('Verify deserializer bit ordering, comma/symbol alignment and reacquisition under recovered-clock phase changes; do not assume RX phase equals local TX phase')

# The discrete route must be evaluated before full serializer integration.
ticket(45, 'Qualify solderable transistor serializer building blocks first',
       '4.2.1.1 4.3.2.2 4.3.3', [3,6,9],
       'Follow docs/discrete-transistor-serializer-plan.md as the required first route; evaluate RF NPN differential current-steering logic in solderable SMD packages before packaged serializer selection|Produce manufacturer/model provenance and package/bias tables; evaluate BFP420-class devices without treating transition frequency as guaranteed digital speed|Design transistor-labelled differential-pair, buffer, two-input mux, retiming latch and clock/divider cells with explicit bias, headroom, common mode and startup behavior|Create nonlinear ngspice fixtures with package/PCB/probe loads, finite FPGA edges and realistic fanout; qualify data and selector paths separately|Deliver an edge-by-edge phase/retiming budget for a three-mux 4:1 tree, plus coupon PCB/BOM/assembly and measurement plan; start with a laboratory differential clock while separately planning production reference clocking|Record quantitative pass/fail or a documented discrete-route rejection before proposing an IC alternative; no packaged serializer substitution without explicit user agreement',
       'Generate independent expected group/bit sequences and timestamped FPGA events through PCIE-009; compare sampled mux output and exercise persistent opposite inputs and phase boundaries|Cover all four-bit values, adjacent group transitions, 10-bit symbol boundary crossings, reset and deterministic phase restart; deliberately swap inputs or skew clocks to prove checker failure',
       'A reviewed discrete building-block design or quantitative rejection includes nonlinear models, transistor-labelled schematics, bias/stress/power results, phase margin, source IDs and reproducible commands|Solderable coupon plan includes package footprints, routed parasitic assumptions, supported clock/data interfaces and measurement loading|No fabricated part parameters, ideal zero-delay selectors or unsupported FPGA rate assumptions are used to claim success; no hardware claim from simulations alone',
       'Run DC/truth-table, loaded transition, fast select, latch/divider and mux corner studies. Sweep mismatch assumptions, bias, temperature, parasitics, duty cycle and phase skew; demonstrate timestep convergence from <=10 ps and report glitches, setup/hold aperture, swing, jitter and power. Archive pass and deliberately failing fixtures.')
for task in TICKETS:
    number = int(task['id'][-3:])
    if number == 3:
        task['work'].append('Freeze constraints for the discrete-transistor-first serializer evaluation in PCIE-045; collect models and interface requirements before committing to any packaged serializer')
        task['work'][4] = 'Freeze the external parallel/control interface and preliminary sourced clock/voltage/throughput budget; reserve transistor-cell qualification for PCIE-045 and full TX feasibility signoff for PCIE-007'
        task['acceptance'][0] = 'Every interface candidate has a sourced budget and documented unresolved cell/model assumptions; no discrete serializer success is asserted before PCIE-045/007 qualification'
    if number == 7:
        task['title'] = 'Integrate discrete-transistor TX serializer, FPGA schedule and output'
        task['dependencies'].append('PCIE-045')
        task['work'][0] = 'Integrate a solderable discrete-transistor clocked serializer only after PCIE-045 building-block evaluation, following docs/discrete-transistor-serializer-plan.md; record any rejected route without silently substituting an IC'
        task['work'].append('Use staggered branch retiming and qualified clock phase distribution; prevent first-stage update races through the final 2:1 mux, including group-boundary changes')
    if number == 6:
        task['work'].append('Qualify nonlinear RF transistor models and solderable package parasitics for PCIE-045; S-parameters alone are insufficient for large-signal switching evidence')

# Pre-implementation review refinements, 2026-11-07. Decide datapath width and
# reference clocking before RTL, plan RX feasibility before TX hardware spending,
# split the Python link partner into layers and exercise the open Gowin flow early.
REVIEW_WORK = {
    1: ['Freeze the fabric datapath width and logical clock before any RTL ticket starts. Proposed default: 16 bits per cycle (two symbols, each with a K flag) at 125 MHz. One 8-bit symbol at 250 MHz is unlikely to close timing on GW2AR-18 C8/I7 and may be kept only with synthesis evidence from a representative block. Changing width after RTL begins touches framing, CRC, DLLP and ordered-set logic in every layer',
        'Freeze the reference-clock policy. Section 4.3.1.1 requires both link ends to transmit within 600 ppm of each other, and host spread-spectrum clocking exceeds what SKP compensation can absorb against a free-running local oscillator. Default: derive the TX bit clock, CDR reference and FPGA gearbox clock from the host 100 MHz REFCLK; any separate-clock mode requires an explicit no-SSC host condition',
        'Before declaring companion specifications missing, record what Rev1.1 sections 7.5 (PCI-compatible registers), 7.6 (PCI-PM capability) and 7.7 (MSI/MSI-X capability) already define; list the remaining gaps per register field and which of PCIE-027/029/030 each gap blocks'],
    2: ['Use a uv-managed project environment with its own pinned cocotb and pyuvm instead of the suite bundled Python 3.11 cocotb; confirm cocotb support for the chosen interpreter and, if Python 3.14 is unsupported, lower requires-python to the newest supported version and record why',
        'Add a smoke build of a trivial design for Tang Nano 20K with the bundled open Gowin flow (yosys synth_gowin, nextpnr-himbaechel for GW2AR-18, gowin_pack) so device-database and toolchain problems surface before PCIE-041; record whether vendor Gowin EDA is also needed for timing signoff'],
    3: ['Own the reference-clock architecture under the PCIE-001 policy: route host REFCLK (or a documented equivalent) to the external serializer clock, CDR reference and FPGA PLL; budget DS226 section 3.4.7 PLL limits, jitter and phase relation. A free-running 27 MHz oscillator or MS5351 is acceptable only for bench experiments or an explicit no-SSC host',
        'Derive FPGA-side clocks from the PCIE-001 datapath decision; four 625 Mb/s outputs through 4:1 output serializers imply a 156.25 MHz parallel clock, so specify the ratio or asynchronous gearbox between it and the logical clock',
        'Budget every required board pin: TX data and clock, RX data and recovered clock, electrical-idle, receiver-detect and power controls, PERST#, REFCLK and any wake signal, against exposed Tang Nano 20K pins and differential-capable banks'],
    4: ['Specify alignment of STP, SDP, END, EDB, COM and ordered sets within the multi-symbol fabric word, including packets that start or end in any symbol position'],
    7: ['Derive the serializer bit clock and select phases from the PCIE-003 reference-clock architecture; a laboratory instrument clock is permitted only for coupon experiments',
        'Do not begin full-serializer PCB work until PCIE-046 records a receive-path recommendation; a working transmitter without a feasible receiver does not produce a link'],
    8: ['Build on the PCIE-046 feasibility recommendation; derive the CDR reference from the PCIE-003 clock architecture and keep the supportable N_FTS and lock-time budget current for PCIE-017/031'],
    12: ['Run an early open-flow synthesis of framing, 8b/10b and scrambling on GW2AR-18 and report achieved Fmax against the PCIE-001 logical clock; escalate a miss to the PCIE-001 datapath decision before more RTL depends on it'],
    13: ['Size elasticity for the PCIE-001/003 reference-clock policy; a free-running local clock against an SSC host violates the section 4.3.1.1 600 ppm requirement and is not a supported elastic-buffer operating case'],
    17: ['Advertise N_FTS and the Extended Synch behavior only within the receive relock budget recorded by PCIE-046/008; section 4.2.4.3 gives about 4 µs of FTS at N_FTS 255'],
    31: ['Derive advertised L0s exit latency from the PCIE-046/008 receive relock budget rather than from logical timing alone'],
    40: ['Implement the PCIE-003 reference-clock routing and constrain every derived clock and gearbox crossing'],
    41: ['Use the open flow validated in PCIE-002 (yosys, nextpnr-himbaechel, gowin_pack) for synthesis and place-and-route; cross-check timing with vendor Gowin EDA where the open timing model is not adequate for signoff, recording versions of both'],
    45: ['Do not purchase parts or fabricate coupons until PCIE-046 has recorded its receive-path recommendation, unless the user explicitly accepts that risk'],
}
REVIEW_TESTS = {
    4: ['Exercise packets and ordered sets starting and ending in every symbol position of the fabric word'],
    13: ['Include an out-of-tolerance clock-offset case that must report overflow or underflow rather than silently corrupt data'],
}
REVIEW_ACCEPT = {
    1: ['Datapath width, logical clock and reference-clock/SSC policy are recorded with rationale before any RTL ticket becomes ready'],
    2: ['Open Gowin flow produces a bitstream for the smoke design, or the missing device support is recorded as a toolchain blocker rather than a resource-fit result'],
    3: ['Reference-clock source, SSC policy and every derived clock have a documented frequency and jitter budget'],
}
for task in TICKETS:
    number = int(task['id'][-3:])
    task['work'].extend(REVIEW_WORK.get(number, []))
    task['tests'].extend(REVIEW_TESTS.get(number, []))
    task['acceptance'][len(task['acceptance']):] = REVIEW_ACCEPT.get(number, [])
    if number == 1:
        task['refs'].append('4.3.1.1')
    if number == 4:
        task['work'][0] = 'Define the fabric-side symbol interface at the width and clock frozen in PCIE-001 (proposed: two symbols plus K flags per 125 MHz cycle); do not label it PIPE compliant without implementing a specific PIPE revision'
    if number == 5:
        task['title'] = 'Build pyuvm framework, symbol-level root-port agent and PHY reference models'
        task['refs'] = '1.5 4.2 4.2.1 4.2.3 B C'.split()
        task['work'] = [
            'Build the shared pyuvm environment: configuration, deterministic seed handling, packet traces, timeout watchdogs, scoreboard base classes and coverage export reused by later tickets',
            'Build a symbol and ordered-set root-port agent at the PCIE-004 interface for data and K symbols, TS1/TS2, FTS, SKP and electrical-idle ordered sets; separate active drivers from passive monitors',
            'Implement independent Python 8b/10b (Appendix B) and scrambler (section 4.2.3, Appendix C) reference models from cited tables and equations; do not import DUT algorithm code',
            'Leave DLLP and data-link partner models to PCIE-047 and TLP/configuration models to PCIE-048 so PCIE-010/011 are not blocked behind a complete Python link partner',
        ]
        task['tests'] = [
            'Self-check 8b/10b and scrambler models against Appendix B/C vectors without a DUT; inject invalid codes and wrong disparity that must be detected',
            'Round-trip randomized symbol streams and ordered sets through the agent driver and monitor with an explicit model contract',
        ]
    if number == 18:
        task['dependencies'] = ['PCIE-012', 'PCIE-047']
    if number == 22:
        task['dependencies'] = ['PCIE-048']
    if number in {7, 8}:
        task['dependencies'].append('PCIE-046')
    if number == 41:
        task['work'][1] = 'Measure FIFO/BRAM/LUT/FF use, critical paths and logical-clock feasibility at the width and clock frozen in PCIE-001'

ticket(46, 'Assess external RX clock recovery feasibility before TX hardware spending',
       '4.2.4.3 4.2.6.6 4.3.1.1 4.3.1.8 4.3.4', [3,6],
       'Perform a paper and behavioral feasibility study of the approved external receive path: input conditioning and termination, CDR topology (discrete PLL or DLL, phase-picking oversampler or another justified approach), 2.5 Gb/s sampler and deserializer to a GW2AR-supported parallel width, and recovered-clock delivery to the FPGA'
       '|Budget CDR lock and relock time against protocol deadlines: L0s exit within the advertised N_FTS FTS ordered sets (section 4.2.4.3: about 4 µs at N_FTS 255), Polling and Recovery timers and electrical-idle exit; record the N_FTS and L0s exit latency the receive path can honestly support for PCIE-017/031'
       '|Budget jitter tolerance and frequency tracking against section 4.3.4 receiver limits under the PCIE-001/003 reference-clock and SSC policy'
       '|Identify candidate discrete or component building blocks with model provenance under the same model-quality rules as PCIE-045; a high-speed sampler or comparator without a trustworthy model is a blocker, not an assumption'
       '|Produce a go, no-go or unknown recommendation and report a no-go or unknown result to the user before money is spent on TX coupon fabrication',
       'Drive a behavioral CDR model with pyuvm-generated training, FTS and data streams; measure modeled lock time against the N_FTS budget and detect false lock|Deliberately exceed the jitter or frequency budget and confirm the checks fail',
       'Recommendation states supportable N_FTS, lock time, jitter tolerance and remaining unknowns with sources|Unresolved model or component gaps are explicit blockers, not passes',
       'Simulate the critical sampler and phase-detector front end with nonlinear models at the 400 ps UI where trustworthy models exist; label behavioral loop results as assumptions until hardware characterization.',
       priority='P0')
ticket(47, 'Build data-link partner models: DLLP, CRC, ACK/NAK replay and flow control',
       '3.1 3.3 3.4 3.5 2.6', [5],
       'Implement independent Python DLLP encode/decode for ACK/NAK, InitFC1/2, UpdateFC and PM DLLPs with CRC16 from section 3.4|Implement independent LCRC and 12-bit sequence-number references from section 3.5|Implement a root-port data-link partner: DL state, InitFC exchange, credit accounting, ACK/NAK generation with configurable delay, drop and corruption, and replay of its own TLPs|Attach the partner to the PCIE-005 symbol agent so PHY and data-link tickets share one stack',
       'Self-check CRC16 and LCRC against cited and hand-computed vectors; corrupt each field and confirm detection|Run partner-to-partner loopback in Python with injected loss, NAK and sequence wrap; check replay delivers each TLP exactly once',
       'Reference vectors carry source citations and expected bytes|Fault injection is controllable per packet and reproducible by seed')
ticket(48, 'Build TLP, configuration and enumeration reference models',
       '2.1 2.2 7.2 7.5', [5],
       'Implement independent Python TLP header build and parse for memory, configuration, completion and message types with explicit byte order|Implement a root-complex enumeration sequence: configuration reads and writes, BAR sizing, capability walk, command enable and MSI programming|Evaluate cocotbext-pcie (MIT licence) as a TLP-level root complex and enumeration model; adopt it only where it is independent of DUT code, pin its version in the PCIE-002 environment and record which Rev1.1 rules it does not model|Expose a TLP-level interface that transaction-layer tickets can use before PHY and data-link integration, and through PCIE-047 for full-stack tests',
       'Round-trip a legal TLP matrix and compare with hand-built byte vectors carrying source citations|Run enumeration against a minimal Python configuration-space model and confirm BAR sizing and capability walk',
       'Transaction-layer tickets can test against TLP-level models without waiting for PHY/DLL integration|Any third-party model version, licence and coverage gaps are recorded')
