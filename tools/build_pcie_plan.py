#!/usr/bin/env python3
"""Build initial documentation/tickets. Refuses to overwrite claimed work."""
import argparse
import csv
import io
import json
import os
import re
from pathlib import Path

from deconstruct_spec import OUT, ROOT, load_sections
from pcie_plan import TICKETS

PRIMARY = {
    '1': 1, '1.5': 4, '2': 22, '2.2.8': 38, '2.3': 23,
    '2.3.1.1': 24, '2.3.2': 25, '2.4': 26, '2.5': 26, '2.6': 26,
    '2.7': 32, '2.7.1': 33, '2.8': 25, '2.9': 19,
    '3': 19, '3.4': 18, '3.5': 20, '3.5.2': 21,
    '4': 4, '4.2': 12, '4.2.1': 10, '4.2.3': 11,
    '4.2.4': 14, '4.2.4.3': 17, '4.2.4.5': 35,
    '4.2.4.7': 15, '4.2.4.8': 13,
    '4.2.5': 14, '4.2.6': 14, '4.2.6.3': 15,
    '4.2.6.4': 16, '4.2.6.5': 15, '4.2.6.6': 17,
    '4.2.6.7': 17, '4.2.6.8': 17, '4.2.6.9': 16,
    '4.2.6.10': 16, '4.2.6.11': 16, '4.2.7': 13,
    '4.2.8': 12, '4.3': 6, '5': 30, '5.4': 31,
    '6': 37, '6.1': 29, '6.2': 32, '6.3': 26, '6.4': 36,
    '6.5': 37, '6.6': 35, '6.8': 38, '6.9': 38,
    '7': 27, '7.5.3': 37, '7.6': 30, '7.7': 29,
    '7.8': 28, '7.9': 34, '7.10': 34, '7.11': 37,
    '7.12': 37, '7.13': 37, '7.14': 37, '7.15': 37,
    '7.16': 37, '7.17': 37, '7.18': 37, '7.19': 37,
    'A': 37, 'B': 10, 'C': 11, 'D': 26,
}
for n in range(9, 15):
    PRIMARY[f'7.8.{n}'] = 37

CONTEXT = {
    1: 'Establish the PCI Express Endpoint role and separate mandatory endpoint behavior from root-complex, bridge and switch context.',
    4: 'Define explicit layer services and a replaceable physical interface so fabric logic can be verified before board selection.',
    6: 'Translate electrical requirements, measurement fixtures and footnotes into sourced limits. These constrain the hardware path even though implementation work is digital SystemVerilog.',
    10: 'Map bytes and control symbols to valid 10-bit codes, with running disparity and receive error detection; serial bit order is observable behavior.',
    11: 'Maintain the exact scrambler state evolution across data, special symbols, training and reset; independent reference vectors are essential.',
    12: 'Preserve the prescribed symbol and ordered-set structure at the physical stream boundary, including packet delimiters and training patterns.',
    13: 'Maintain lossless symbol transport across clock differences using correctly bounded buffering and SKP handling.',
    14: 'Train the upstream-facing endpoint port with specified sets, counts, timers and fallback paths; descriptive state text must be read alongside transition rules.',
    15: 'Negotiate lane zero and a one-lane Gen1 link; assert link-up only after all required training conditions.',
    16: 'Recover and reset link operation with required special modes and clean transitions back to operational traffic.',
    17: 'Coordinate physical idle and wake behavior with independent transmit/receive low-power states and higher-layer obligations.',
    18: 'Encode and validate link-local control packets before ACK, power or flow-control state can change.',
    19: 'Coordinate link availability and credit initialization so transaction traffic starts and stops at the correct boundaries.',
    20: 'Validate received packet integrity and sequence, reject duplicates and issue timely link acknowledgments.',
    21: 'Retain transmitted packets until acknowledged and replay reliably under loss, corruption, timeout and sequence wrap.',
    22: 'Specify packet fields, addressing, payload, routing and byte-enable constraints. Validate field combinations before dispatching transactions.',
    23: 'Classify requests and enforce endpoint handling rules, with explicit unsupported, malformed and error paths.',
    24: 'Return correctly formed completions, including split reads and byte accounting across payload and address boundaries.',
    25: 'Match completions to outstanding requester state, preserve tag ownership and terminate requests safely on timeout or errors.',
    26: 'Maintain credit conservation, ordering and independent forward progress for posted, non-posted and completion traffic in VC0.',
    27: 'Support host enumeration through Type0 configuration, correctly attributed registers and 64-bit BAR resource decoding.',
    28: 'Advertise capabilities truthfully and couple writable controls and live status to actual endpoint behavior.',
    29: 'Support programmed message-signaled interrupts and define applicability of PME and legacy mechanisms for the endpoint profile.',
    30: 'Provide required software power management and coordinate device states, link protocols, wake and reset retention.',
    31: 'Implement mandatory Rev1.1 L0s behavior and distinguish optional ASPM L1 from software-controlled power-state requirements.',
    32: 'Classify, signal and log errors with the correct enable controls and packet-specific responses; prevent silent corruption.',
    33: 'Decide optional end-to-end digest support separately from mandatory link CRC and implement its control/error behavior if advertised.',
    34: 'Decide optional extended error capabilities explicitly while maintaining required baseline status and errors.',
    35: 'Apply fundamental/hot reset and link-down behavior consistently across retained registers, protocol state and application traffic.',
    36: 'Expose a verifiable application interface with observable memory effects and explicit synchronization and completion behavior.',
    37: 'Review applicability before omitting optional or infrastructure features. Preserve endpoint-facing obligations and test absence/unsupported behavior.',
    38: 'Handle endpoint system messages and power-limit updates with the correct routing, register effects and unsupported-message policy.',
}


def primary(sid):
    matches = [(p, n) for p, n in PRIMARY.items() if sid == p or sid.startswith(p + '.')]
    return max(matches, key=lambda p: len(p[0]))[1] if matches else 1


def related(sid, ref):
    return sid == ref or sid.startswith(ref + '.') or ref.startswith(sid + '.')


def synopsis(raw, header_lines):
    # Extractive synopsis, deliberately labelled; no generated paraphrase of normative rules.
    lines = raw.splitlines()[header_lines:]
    clean = []
    for line in lines:
        line = re.sub(r'^\s*(?:5|10|15|20|25|30|35|40|45|50)\s+', '', line).strip()
        if not line or 'PCI EXPRESS BASE SPECIFICATION' in line or re.fullmatch(r'\d+', line):
            continue
        if len(line) > 35 and re.search(r'[a-z]{3}', line):
            clean.append(line)
        if len(' '.join(clean)) > 550:
            break
    return ' '.join(clean) if clean else 'This section contains structural, tabular or graphical material; inspect the verbatim text and referenced PDF.'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--summaries-only', action='store_true',
                        help='only rebuild the local, git-ignored specification summaries; never touches tickets')
    args = parser.parse_args()
    tickets = ROOT / 'tickets'
    tickets.mkdir(exist_ok=True)
    for p in ([] if args.summaries_only else tickets.glob('PCIE-*.md')):
        header = p.read_text().split('---')[1]
        if 'owner: null' not in header or 'status: todo' not in header:
            raise SystemExit(f'Refusing to overwrite ticket lifecycle changes: {p}')
    trace = OUT / 'TRACEABILITY.csv'
    if trace.is_file() and not args.summaries_only:
        for row in csv.DictReader(io.StringIO(trace.read_text())):
            if row['applicability'] != 'pending-review' or row['review_status'] != 'unreviewed':
                raise SystemExit(f"Refusing to overwrite reviewed traceability row: {row['section']} {row['candidate_id']}")
    text, sections, _ = load_sections()
    reqs = json.loads((OUT / 'requirements.json').read_text())
    by_id = {s['id']: s for s in sections}
    counts = {}
    for r in reqs:
        counts[r['section']] = counts.get(r['section'], 0) + 1
    for s in sections:
        folder = OUT / s['path']
        sid = s['id']
        num = primary(sid)
        task = next(t for t in TICKETS if t['id'] == f'PCIE-{num:03}')
        link = Path(os.path.relpath(tickets / (task['id'] + '.md'), folder)).as_posix()
        children = [c for c in sections if '.' in c['id'] and c['id'].rsplit('.', 1)[0] == sid]
        content = (f"# {sid} — {s['title']}\n\n"
                   f"Source: Rev. 1.1, PDF/printed pp. {s['page_start']}–{s['page_end']} (direct text).\n\n"
                   f"## Structured summary\n\nTopic: **{s['title']}**.\n\n"
                   f"{CONTEXT.get(num, CONTEXT[1])}\n\n"
                   f"Extractive synopsis of the direct text (line numbers and headers omitted; read the full source for conditions):\n\n"
                   f"> {synopsis(text[s['start']:s['end']], s.get('header_lines', 0))}\n\n"
                   f"## Implementation and verification\n\n"
                   f"Primary review/implementation owner: [{task['id']} — {task['title']}]({link}). "
                   f"The ticket defines SystemVerilog deliverables, pyuvm stimulus/checks and ngspice applicability. "
                   f"Ownership includes applicability review; it does not imply every rule concerns this endpoint.\n\n"
                   f"Direct-text keyword candidates: **{counts.get(sid, 0)}**, all initially unreviewed. "
                   f"See [requirements](requirements.md) and [verbatim text](verbatim.md). "
                   f"Extracted paragraphs are source evidence; tables, diagrams, child sections and referenced specifications also constrain implementation.\n\n")
        if children:
            content += '## Child sections\n\n'
            for c in children:
                content += f"- [{c['id']} — {c['title']}]({c['id'].split('.')[-1]}/summary.md)\n"
        (folder / 'summary.md').write_text(content)
    if args.summaries_only:
        print(f'Rebuilt {len(sections)} specification summaries; tickets and traceability untouched.')
        return
    for t in TICKETS:
        selected = [s for s in sections if primary(s['id']) == int(t['id'][-3:])]
        content = (f"---\nid: {t['id']}\ntitle: {json.dumps(t['title'])}\nstatus: todo\nowner: null\n"
                   f"branch: null\nclaimed_at: null\nbase_commit: null\npriority: {t['priority']}\n"
                   f"gate: {t['gate']}\ndepends_on: {json.dumps(t['dependencies'])}\n"
                   f"spec_sections: {json.dumps(t['refs'])}\n---\n\n# {t['id']} — {t['title']}\n\n"
                   "## Agent handoff and scope\n\n"
                   "Read [workflow](README.md), [profile](../docs/endpoint-profile.md), and repository AGENTS.md. "
                   f"Claim with `python3 tools/tickets.py claim {t['id']} --agent <unique-agent-id>` before editing implementation. "
                   "Do not begin until dependencies are done; conditional dependencies require a reviewed disposition. "
                   "Implement digital logic in synthesizable SystemVerilog; external circuits require schematics, "
                   "ngspice netlists/models and PCB evidence as specified by the ticket.\n\n"
                   "## Source evidence\n\n")
        for ref in t['refs']:
            if ref not in by_id:
                raise ValueError((t['id'], 'Missing source', ref))
            s = by_id[ref]
            content += f"- [{ref} — {s['title']}](../specification/{s['path']}/summary.md): direct pp. {s['page_start']}–{s['page_end']}; follow child sections and PDF tables.\n"
        content += (f"\nPrimary ownership: {len(selected)} sections; "
                    "[section/candidate traceability](../specification/TRACEABILITY.csv) lists exact IDs. "
                    "Source references above also include shared prerequisites.\n\n## Deliverables and behavior\n\n")
        content += ''.join(f'- [ ] {w}.\n' for w in t['work'])
        content += '\n## pyuvm verification\n\n'
        content += ''.join(f'- [ ] {v}.\n' for v in t['tests'])
        content += ('- [ ] Use independent expected results, bounded watchdogs and reproducible seeds; record reviewed requirement IDs, functional coverage and exact command.\n'
                    '\n## ngspice verification\n\n')
        content += (t['spice'] if t['spice'] else
                    'No ticket-local circuit simulation is required: these are protocol, control or planning rules. '
                    'Verify them in pyuvm/review. Any change to physical pin timing, clocks, idle, detection or signal levels '
                    'must provide pattern manifests to PCIE-009 and re-run the applicable electrical cases in PCIE-043; '
                    'ngspice cannot establish digital packet correctness.') + '\n\n'
        content += '## Acceptance criteria\n\n'
        content += ''.join(f'- [ ] {v}.\n' for v in t['acceptance'])
        content += ('- [ ] Reviewed requirements have implementation/test links and dispositions; relevant checks pass and limitations are recorded.\n'
                    '- [ ] Update graph with `graphify update .` after code changes; record any tool failure explicitly.\n'
                    '\n## Evidence and handoff\n\n'
                    'Implementation files: pending. Commands/versions/seeds: pending. Results/coverage: pending. '
                    'Requirement dispositions: pending. Remaining limitations: pending. Next action: satisfy dependencies and claim ticket.\n\n'
                    '## Claim history\n\nNo claims yet.\n')
        (tickets / (t['id'] + '.md')).write_text(content)
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(['section', 'title', 'source_page_start', 'source_page_end', 'candidate_id',
                     'primary_ticket', 'related_tickets', 'applicability', 'review_status'])
    for s in sections:
        linked = [t['id'] for t in TICKETS if any(related(s['id'], r) for r in t['refs'])]
        for r in [r for r in reqs if r['section'] == s['id']] or [None]:
            writer.writerow([s['id'], s['title'], s['page_start'], s['page_end'], r['id'] if r else '',
                             f"PCIE-{primary(s['id']):03}", ';'.join(linked), 'pending-review', 'unreviewed'])
    (OUT / 'TRACEABILITY.csv').write_text(buf.getvalue())
    idx = '# Ticket index\n\nGenerated initial backlog; no tickets are claimed or implemented. See [workflow](README.md).\n\n'
    idx += '| Ticket | Gate | Dependencies |\n|---|---|---|\n'
    for t in TICKETS:
        idx += f"| [{t['id']} — {t['title']}]({t['id']}.md) | {t['gate']} | {', '.join(t['dependencies']) or 'none'} |\n"
    (tickets / 'INDEX.md').write_text(idx)
    print(f"Generated {len(TICKETS)} tickets, {len(sections)} summaries and section/candidate traceability.")


if __name__ == '__main__':
    main()
