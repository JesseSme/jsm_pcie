# Project instructions for agents

## Objective and scope

Build a complete PCI Express **Gen1 x1 endpoint** on the **SkyWater SKY130** process,
using the supplied **PCI Express Base Specification Revision 1.1**. The digital core
(transaction layer, data link layer, logical PHY) is synthesizable SystemVerilog
hardened with **OpenLane and OpenROAD**; the PHY (PLL, serializer, transmitter,
receiver, CDR, deserializer) is designed at transistor level **on the same die**.
Digital verification uses **pyuvm through cocotb** with the local OSS CAD Suite.
Circuit verification uses **ngspice with SKY130 models**.

Preserve the approved architecture and user decisions below. A functioning training
sequence or MMIO demonstration is a milestone; it does not replace the complete
endpoint obligations. Do not drop mandatory power management, replay, flow control,
configuration, reset or error behavior to make a prototype appear complete.

## Read first and find the authoritative information

Read these before implementing a ticket:

1. [Endpoint profile](docs/endpoint-profile.md): scope and proposed protocol defaults.
2. [ASIC target](docs/asic-target.md): SKY130 process, flows, ticket map and digital-only fallback.
3. [PHY architecture](docs/phy-architecture.md): on-chip PMA partition, proposed rates and method.
4. [Ticket workflow](tickets/README.md), [ticket index](tickets/INDEX.md), and the selected ticket's full source references and dependency evidence.

Source authority and traceability:

- **The repository is public and the PCI-SIG specification is copyrighted.** The source
  PDF/TXT, all spec-derived text under `specification/` and `graphify-out/` are
  git-ignored and must never be committed, force-added or quoted at length in tracked
  files; cite section and page instead. See [specification/README.md](specification/README.md)
  for rebuilding the local files in a fresh clone.
- Original `54321492-PCI-Express-Base-11.txt` and `.pdf` files must remain unchanged.
  Use the supplied TXT for verbatim text; check the PDF for figures, table geometry,
  footnotes and ambiguous extraction. Keep source revision, section and page citations.
- [Specification index](specification/INDEX.md) follows numeric directory hierarchy:
  section 4.2.6 is in `specification/4/2/6/`. A parent's `verbatim.md` contains
  only its direct text; read relevant child sections too.
- `summary.md` is guidance, not normative authority. `requirements.md` and
  `requirements.json` contain unreviewed keyword candidates, not an exhaustive
  approved compliance checklist. Review device applicability, exceptions, tables,
  diagrams, conditions and the distinction between must/should/may.
- [Traceability](specification/TRACEABILITY.csv) assigns section/candidate review
  owners. Turn applicable candidates into atomic requirements and link each to
  implementation, test and evidence. Cite keyword-free rules and PDF-only details too.
- Identify missing companion specifications explicitly. Do not invent MSI, PCI-PM,
  configuration or form-factor definitions that the Base specification delegates.

## Repository layout

Keep planning and generated source material separate from implementation:

| Location | Purpose |
|---|---|
| `specification/` | Local-only source decomposition, summaries and candidates; tracked metadata: README, INDEX, manifest and traceability |
| `tickets/` | Authoritative file-based work queue, ownership, status and evidence |
| `docs/` | Architecture decisions and design rationale; `docs/superseded/` holds the retired FPGA plans for history only |
| `tools/` | Specification/ticket tooling and reproducible automation |
| `src/jsm_pcie/` | Existing Python package; preserve its role when adding tools |
| `oss-cad-suite/` | Bundled third-party toolchain; do not edit its implementation |
| `graphify-out/` | Generated knowledge graph; local-only and git-ignored because it contains spec text |

As implementation is introduced, place synthesizable modules in `rtl/`, pyuvm and
cocotb infrastructure in `verification/`, PHY schematics, layouts, netlists and
ngspice fixtures in `analog/`, and OpenLane/OpenROAD configurations, constraints,
SKY130 wrappers and chip-top integration in `asic/sky130/`. Keep the SKY130 PDK
install, flow run directories and GDS outputs outside Git.
Respect any more specific instructions in those directories. Record exact commands
and generated-output locations in the owning ticket; do not scatter undocumented
scripts or commit large simulator waveforms and build caches by default.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

## PCIe work ownership and agent handoff

Before starting implementation, read [tickets/README.md](tickets/README.md),
[tickets/INDEX.md](tickets/INDEX.md), and [docs/endpoint-profile.md](docs/endpoint-profile.md).
The file-based tickets are the authoritative work queue. The scope is a single-lane
Gen1 PCI Express endpoint on SKY130: a digital core plus an on-chip PHY. PHY
feasibility must not be assumed from ideal sources or schematic-only simulation.

The user-selected target is the **SkyWater SKY130 process with an on-chip PHY**
(2026-11-07). Read [docs/asic-target.md](docs/asic-target.md) and
[docs/phy-architecture.md](docs/phy-architecture.md). The earlier Tang Nano 20K
FPGA target, external serializer and discrete-transistor board plan are retired;
`docs/superseded/` is history, not guidance.

The PHY follows a transistor-level, building-blocks-first method. Each analog block
has schematic, layout and qualification tickets (see [docs/asic-target.md](docs/asic-target.md)).
PCIE-045 qualifies SKY130 cells on extracted layout, PCIE-046 assesses CDR feasibility and lock time
before PHY layout, PCIE-059 supplies bias and references, then PCIE-049 (PLL and
REFCLK receiver), PCIE-007 (TX), PCIE-008 (RX) and PCIE-052 (pads, ESD, package)
integrate. PCIE-060 joins logical PHY and PMA early in a loopback top. If these reject the on-chip PHY with quantitative
evidence, the documented digital-only fallback applies: keep every mandatory protocol
obligation, record the PHY rejection and unmet electrical requirements, report it to
the user, and never call the result a working PCIe endpoint.

Technology-specific memories, synchronizers, reset synchronizers and clock gates
live only behind the PCIE-051 wrappers; shared RTL has no initial-value resets or
technology primitives. Timing signoff covers every selected corner, not only typical.
Never submit a design for fabrication or incur cost without explicit user approval.
[docs/fabrication-routes.md](docs/fabrication-routes.md) records the shuttle options checked on
2026-11-07; re-verify them before relying on dates, prices or pad options.

An agent **must sign a ticket and create its own branch before implementation**:

1. On an up-to-date `main`, run `python3 tools/tickets.py ready`, select one unowned
   ticket, and read its prerequisites, source chapters, tests and acceptance criteria.
   All dependencies must be `done` on `main`. Do not take another owner's ticket.
2. With a clean tracked working tree and planning baseline committed, run
   `python3 tools/tickets.py claim PCIE-NNN --agent <unique-agent-id>` on `main`.
   This signs owner/time/base commit and history, sets `active`, commits only that
   ticket on `main`, and creates/switches to `ticket/pcie-nnn/<unique-agent-id>`.
   If the commit fails the signature is rolled back. Never carry unrelated user edits
   onto a ticket branch.
3. Push `main` so the claim is visible before implementation. Independent clones must
   pull `main` before claiming. Use separate worktrees for simultaneous branches, run
   claims from the worktree that has `main` checked out, and do not switch branches
   under another running agent.
4. Implement the claimed scope and keep the ticket's evidence and handoff section
   current. Record actual pyuvm commands, versions, seeds, results and requirement
   coverage. Run ngspice where the ticket calls for it; protocol-only tickets explain
   why electrical simulation is not their correctness check.
5. Append signed UTC history for state changes. Missing hardware, tools or normative
   definitions are explicit blockers. Preserve ownership/history on handoff; a replacement
   agent must sign an agreed transfer and create its own branch.
6. Before `review`, satisfy acceptance checks, update requirement dispositions and run
   `python3 tools/tickets.py check`, relevant tests, and `graphify update .` for code
   changes. Record any graph/tool failure. Set `done` only after a signed review verifies
   evidence and dependency integration, then merge the ticket branch into `main` and push;
   `done` means merged into `main`. Never mark unexecuted verification as passed.

Use specification chapter `verbatim.md` files and the source PDF as authority;
`summary.md` is guidance, and `requirements.md` contains unreviewed extraction
candidates until the owning ticket reviews conditions, tables and device applicability.
Do not regenerate initial tickets after claiming work or overwrite another agent's
status/evidence. Optional omissions need a source-cited disposition and absence tests;
mandatory endpoint behavior cannot be deferred to make a demonstration appear complete.

## SystemVerilog implementation rules

- Keep transaction, data-link, logical-PHY, PMA-interface and application
  responsibilities explicit. Scrambling and 8b/10b remain in the digital core; the
  on-chip serializer carries raw encoded bits and must not encode them a second time.
- Use explicit widths, signedness, units and byte/bit order. Derive timer and FIFO
  parameters from source-cited limits. Handle modulo sequence/credit counters,
  wraparound and infinite-credit encodings intentionally.
- Use clear sequential/combinational separation, complete combinational assignments,
  and defined reset behavior. Avoid inferred latches and simulation-only constructs
  in synthesizable modules. Keep technology primitives behind the PCIE-051 wrappers.
- Specify ready/valid handshakes, latency and backpressure boundaries. A physical
  serial stream cannot pause because an internal consumer is not ready; account for
  buffering, credit advertisement and overflow behavior.
- Identify every clock domain and reset crossing. Use appropriate synchronization
  and asynchronous FIFOs; synchronize reset release. Do not sample recovered-clock
  signals directly in the core clock domain without a justified crossing.
- Gen1 remains 2.5 GT/s, 400 ps per serial bit. The proposed PMA interface carries
  20 encoded bits per 125 MHz cycle; preserve encoded bit order across ten-bit symbol
  and parallel-word boundaries.
- Advertised configuration/capability fields must match implemented behavior.
  Optional omissions need explicit applicability and unsupported/absence tests.
  The supplied Rev1.1's mandatory L0s support is part of the complete baseline.

## Verification and evidence

For digital changes, use the owning ticket's pyuvm plan with independent Python
reference models, passive monitors and scoreboards. Do not derive expected results
by importing the DUT algorithm. Include meaningful legal, boundary and fault cases:
CRC and sequence errors, replay, credit exhaustion, timer expiry, reset, lock loss,
malformed requests and power transitions as relevant. Use deterministic seeds and
bounded progress/watchdog checks. Confirm that injected faults fail the checks.

Use `oss-cad-suite/bin/verilator` as the initial primary SV simulator. Use Icarus
only for supported subsets. PCIE-002 establishes the compatible Python/cocotb/pyuvm
environment: the project's Python requirement and bundled simulator Python ABI may
differ. Do not assume pyuvm is installed or a simulator integration is working
because a binary exists. Capture tool versions and actual executed commands.

For circuit changes, follow [docs/phy-architecture.md](docs/phy-architecture.md) and
PCIE-006/009/045:

- Use the pinned SKY130 ngspice models; record model, corner, temperature, supply and
  mismatch settings. Qualify cells on extracted layout, not schematic alone.
- Include pad, ESD, package, channel and measurement loading from PCIE-052. Check
  device voltage stress, electromigration, power and select-path timing as well as
  data-path bandwidth.
- Evaluate retiming/latch races and clock generation explicitly. Do not replace the
  serializer, PLL or CDR with an ideal 2.5 Gb/s source when claiming feasibility.
- Run DC, truth-table, transient and justified corner studies with timestep
  convergence. Use pyuvm-generated bit/pin manifests and compare analog output
  bits against the independent expected stream. Preserve deliberately failing cases.
- Distinguish modeled feasibility from silicon measurements, BER qualification,
  host interoperability and certified compliance. An eye plot or a transistor's
  transition-frequency rating alone does not prove a working PCIe endpoint.

Run checks appropriate to the change. For planning/specification changes, available
checks are:

```sh
python3 tools/tickets.py check
python3 tools/deconstruct_spec.py --check
```

The first validates ticket metadata, source references and dependency cycles. The
second checks source hashes, heading anchors and exact TXT reconstruction. Also
check any Markdown links and architecture/dependency consistency that changed.
These checks do not run endpoint pyuvm or electrical regressions. The extraction
and initial-plan generators overwrite generated material; do not run them after
ticket ownership/evidence work begins. Maintain lifecycle changes directly.

Before handoff, record changed files, reviewed requirement IDs, exact commands,
versions, seeds, observed results, coverage or numerical margins, unexecuted checks,
limitations and a precise next action in the ticket. Run relevant lint, synthesis,
timing, CDC, DRC and LVS checks for RTL and layout changes as they become available. Update the
knowledge graph after code changes. Never mark unavailable verification as passed.

## Preserve user work and distinguish decisions from results

Inspect the working tree before edits. Preserve unrelated files, uncommitted changes,
ticket claims and the bundled toolchain. Stage only the files for the task; do not
use broad staging, reset or cleanup commands that sweep in user work.

Carry out routine work within the claimed scope without asking to reconfirm already
accepted decisions. Record unresolved requirements or feasibility limits honestly.
Changing the on-chip PHY direction, absorbing logical-PHY functions into a third-party
PHY or hard IP, or replacing the SKY130 target requires a documented architecture
proposal and explicit user agreement. The digital-only fallback in
[docs/asic-target.md](docs/asic-target.md) is pre-authorized but must be reported to
the user when triggered, with its evidence rules applied and unperformed physical
tests labeled.
