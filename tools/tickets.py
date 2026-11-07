#!/usr/bin/env python3
"""Small stdlib-only ticket reader, validator and exclusive claim operation."""
import argparse
import datetime
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TICKETS = ROOT / 'tickets'
STATES = {'todo', 'active', 'blocked', 'review', 'done', 'deferred'}
REQUIRED_KEYS = ['id', 'title', 'status', 'owner', 'branch', 'claimed_at', 'base_commit',
                 'gate', 'depends_on', 'spec_sections']


def require(condition, message):
    # Explicit checks rather than assert, so validation still runs under python -O.
    if not condition:
        raise SystemExit(f'FAIL: {message}')


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True).strip()


def read(path):
    text = path.read_text()
    header = text.split('---', 2)[1]
    data = {}
    for line in header.splitlines():
        if ':' not in line:
            continue
        k, v = line.split(':', 1)
        v = v.strip()
        try:
            data[k] = json.loads(v)
        except json.JSONDecodeError:
            data[k] = v
    return data, text


def all_tickets():
    return {p.stem: (p, *read(p)) for p in sorted(TICKETS.glob('PCIE-*.md'))}


def validate():
    tickets = all_tickets()
    require(tickets, 'no tickets found')
    sections = {s['id'] for s in json.loads((ROOT / 'specification' / 'manifest.json').read_text())['sections']}
    for tid, (path, d, text) in tickets.items():
        missing = [k for k in REQUIRED_KEYS if k not in d]
        require(not missing, f'{tid}: missing front-matter keys {missing}')
        require(d['id'] == tid, f'{tid}: id field is {d["id"]!r}')
        require(d['status'] in STATES, f'{tid}: unknown status {d["status"]!r}')
        require(d['gate'] in {'baseline', 'conditional'}, f'{tid}: unknown gate {d["gate"]!r}')
        unknown = set(d['depends_on']) - tickets.keys()
        require(not unknown, f'{tid}: unknown dependencies {sorted(unknown)}')
        require(tid not in d['depends_on'], f'{tid}: depends on itself')
        for ref in d['spec_sections']:
            require(ref in sections, f'{tid}: unknown specification section {ref}')
        if d['status'] in {'active', 'review', 'done'}:
            empty = [k for k in ['owner', 'branch', 'claimed_at', 'base_commit'] if not d[k]]
            require(not empty, f'{tid}: status {d["status"]} but {empty} unset')
        for heading in ['Deliverables and behavior', 'pyuvm verification', 'ngspice verification',
                        'Acceptance criteria', 'Evidence and handoff', 'Claim history']:
            require(f'## {heading}' in text, f'{tid}: missing section "## {heading}"')
    visited, active = set(), set()

    def visit(tid):
        require(tid not in active, f'dependency cycle at {tid}')
        if tid in visited:
            return
        active.add(tid)
        for dep in tickets[tid][1]['depends_on']:
            visit(dep)
        active.remove(tid)
        visited.add(tid)
    for tid in tickets:
        visit(tid)
    print(f'PASS: {len(tickets)} tickets, metadata, source links, required handoff sections, acyclic dependencies.')


def current_branch():
    return git('branch', '--show-current')


def claim(tid, agent, base_branch):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}', agent):
        raise SystemExit('Agent ID must use 1–64 letters, numbers, underscores or hyphens.')
    path = TICKETS / f'{tid}.md'
    if not re.fullmatch(r'PCIE-\d{3}', tid) or not path.is_file():
        raise SystemExit('Unknown ticket ID.')
    common = Path(git('rev-parse', '--git-common-dir'))
    if not common.is_absolute():
        common = ROOT / common
    # Shared across worktrees of this repository; no stale lock is deleted automatically.
    lock = common / 'pcie-ticket-claim.lock'
    try:
        fd = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        raise SystemExit(f'Another claim is in progress. Inspect {lock}; do not remove a live lock.')
    try:
        with os.fdopen(fd, 'w') as f:
            f.write(json.dumps(dict(ticket=tid, agent=agent, pid=os.getpid())))
        # Require durable ticket history, and avoid carrying unrelated tracked edits into a branch.
        rel = str(path.relative_to(ROOT))
        git('ls-files', '--error-unmatch', rel)
        # Claims are committed on the shared base branch so every checkout of it sees ownership.
        if current_branch() != base_branch:
            raise SystemExit(f'Claim from the {base_branch} branch (currently on {current_branch() or "detached HEAD"}). '
                             'Dependencies count as done only after they are merged there.')
        if git('diff', '--name-only') or git('diff', '--cached', '--name-only'):
            raise SystemExit('Tracked changes exist. Preserve/commit them before claiming; nothing was changed.')
        d, original = read(path)
        if d['status'] != 'todo' or d['owner'] is not None:
            raise SystemExit('Ticket is already owned or is not todo. Coordinate an explicit reassignment.')
        for dep in d['depends_on']:
            if read(TICKETS / f'{dep}.md')[0]['status'] != 'done':
                raise SystemExit(f'Dependency {dep} is not done. Nothing was changed.')
        branch = f'ticket/{tid.lower()}/{agent}'
        if subprocess.run(['git', '-C', str(ROOT), 'rev-parse', '--verify', '--quiet', f'refs/heads/{branch}'],
                          capture_output=True).returncode == 0:
            raise SystemExit(f'Branch {branch} already exists. Nothing was changed.')
        base = git('rev-parse', 'HEAD')
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        replacement = original
        for key, value in dict(status='active', owner=agent, branch=branch,
                               claimed_at=now, base_commit=base).items():
            replacement = re.sub(rf'^{key}:.*$', f'{key}: {json.dumps(value)}', replacement, count=1, flags=re.M)
        replacement += f'\n- {now}: {agent} signed {tid}; branch `{branch}`; base `{base}`.\n'
        # Sign and commit only this ticket on the base branch, then branch from that commit.
        # Roll back the signature if the commit fails.
        path.write_text(replacement)
        try:
            subprocess.run(['git', '-C', str(ROOT), 'commit', '--quiet', '-m', f'Claim {tid} for {agent}',
                            '--', rel], check=True)
        except (OSError, subprocess.CalledProcessError):
            path.write_text(original)
            raise
        try:
            subprocess.run(['git', '-C', str(ROOT), 'switch', '-c', branch], check=True)
        except (OSError, subprocess.CalledProcessError):
            raise SystemExit(f'Claim committed on {base_branch}, but creating {branch} failed. '
                             f'Create it manually with: git switch -c {branch}')
        print(f'Claimed {tid} as {agent}: claim committed on {base_branch}, now on {branch}. '
              f'Push {base_branch} so other checkouts see the claim.')
    finally:
        lock.unlink()


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('check')
    sub.add_parser('list')
    sub.add_parser('ready')
    c = sub.add_parser('claim')
    c.add_argument('ticket')
    c.add_argument('--agent', required=True)
    c.add_argument('--base', default='main', help='shared branch that records claims (default: main)')
    args = parser.parse_args()
    if args.command == 'check':
        validate()
    elif args.command == 'claim':
        claim(args.ticket, args.agent, args.base)
    else:
        if current_branch() != 'main':
            print(f'Note: reading ticket status on {current_branch() or "detached HEAD"}, not main; '
                  'work counts as done only once merged into main.', file=sys.stderr)
        tickets = all_tickets()
        for tid, (_, d, _) in tickets.items():
            ready = d['status'] == 'todo' and all(tickets[x][1]['status'] == 'done' for x in d['depends_on'])
            if args.command == 'list' or ready:
                print(f"{tid} {d['status']:8} {d['owner'] or '-':16} {d['title']}")


if __name__ == '__main__':
    main()
