#!/usr/bin/env python3
"""Split the supplied layout text without losing a character. No external packages."""
import argparse
import bisect
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '54321492-PCI-Express-Base-11.txt'
PDF = SOURCE.with_suffix('.pdf')
OUT = ROOT / 'specification'
ROOT_PAGES = {'1': 27, '2': 43, '3': 127, '4': 161, '5': 231,
              '6': 273, '7': 337, 'A': 475, 'B': 487, 'C': 497, 'D': 503}
HEADING = re.compile(r'^ *(?:(?:5|10|15|20|25|30|35|40|45|50) +)?'
                     r'(?P<id>[1-7A-D](?:\.\d+)*)\. +(?P<title>[A-Za-z].*)$')
MODAL = re.compile(r'\b(must(?: not)?|shall(?: not)?|required|permitted|may|optional|should(?: not)?)\b', re.I)
# Wrapped titles verified in the supplied Rev1.1 layout. An indentation-only
# heuristic mistakes indented bullets immediately below some headings for titles.
WRAPPED = set('2.2 2.4.2 2.4.3 3.2 3.2.1 3.3.1 3.5.2 4.2.1.2 4.2.5 '
              '5.3.1 5.3.2 5.4 5.6 6.1.9 6.2.3.2.1 6.2.4.1 6.2.4.2 '
              '6.2.5 6.2.8.1 6.5.2 6.8.1 7.9.2 7.10.1 7.10.7 7.12.1 '
              '7.13 7.13.1 7.14 7.14.1 7.15.1 7.16 7.16.1 7.16.2 '
              '7.18.1 7.19.1 A.2 A.2.1'.split()) - {'3.3.1'}


def load_sections():
    text = SOURCE.read_text()
    pages = [0] + [m.end() for m in re.finditer('\f', text)]
    page_of = lambda n: bisect.bisect_right(pages, n)
    sections = []
    offset = 0
    lines = text.splitlines(keepends=True)
    for index, line in enumerate(lines):
        m = HEADING.match(line.rstrip('\n\r'))
        page = page_of(offset)
        if m and 27 <= page < 507:
            sid = m['id']
            if '.' in sid or ROOT_PAGES.get(sid) == page:
                # Root headings are unique; numbered list items are not chapters.
                if not any(s['id'] == sid for s in sections):
                    title = m['title'].strip()
                    header_lines = 1
                    # Wrapped headings are indented beyond the numeric section label;
                    # prose returns to the body margin. Preserve raw text separately.
                    for following in (lines[index+1:index+4] if sid in WRAPPED else []):
                        indent = len(following) - len(following.lstrip(' '))
                        if not following.strip() or indent < m.start('id') + len(sid):
                            break
                        title += ' ' + following.strip()
                        header_lines += 1
                    sections.append(dict(id=sid, title=title, start=offset, header_lines=header_lines))
        offset += len(line)
    assert [s['id'] for s in sections if '.' not in s['id']] == list(ROOT_PAGES)
    ids = {s['id'] for s in sections}
    for s in sections:
        if '.' in s['id']:
            assert s['id'].rsplit('.', 1)[0] in ids, s
    # Contents entries act as an independent check on the detected body headings.
    toc = []
    for page in text.split('\f')[2:9]:
        for line in page.splitlines():
            m = re.match(r'^\s*([1-7A-D](?:\.\d+)*)\.\s+.*?\.{2,}\s*(\d+)\s*$', line)
            if m:
                sid, p = m.groups()
                toc.append(sid)
                assert sid in ids, ('Missing TOC section', sid)
                found = next(s for s in sections if s['id'] == sid)
                assert page_of(found['start']) == int(p), (sid, 'TOC page mismatch')
    sections.insert(0, dict(id='front-matter', title='Front matter, contents and introductory material', start=0))
    sections.append(dict(id='back-matter', title='Acknowledgements', start=pages[506]))
    for i, s in enumerate(sections):
        s['end'] = sections[i+1]['start'] if i+1 < len(sections) else len(text)
        s['page_start'], s['page_end'] = page_of(s['start']), page_of(s['end'] - 1)
        s['path'] = s['id'].replace('.', '/')
        s['sha256'] = hashlib.sha256(text[s['start']:s['end']].encode()).hexdigest()
    return text, sections, toc


def candidates(raw, section, text):
    """Retain complete layout paragraphs and mark them unreviewed, never invent shall rules."""
    result = []
    for m in re.finditer(r'\S[^\f]*?(?=\n[ \t]*\n|\f|\Z)', raw, re.S):
        block = m.group()
        modal = MODAL.findall(block)
        if not modal:
            continue
        pos = section['start'] + m.start()
        result.append(dict(id=f"REQ-{section['id']}-{len(result)+1:03}",
                           section=section['id'], status='unreviewed-candidate',
                           source_line=text.count('\n', 0, pos)+1,
                           page=text.count('\f', 0, pos)+1,
                           modalities=sorted(set(x.lower() for x in modal)), text=block))
    return result


def generate():
    text, sections, toc = load_sections()
    OUT.mkdir(exist_ok=True)
    requirements = []
    for s in sections:
        folder = OUT / s['path']
        folder.mkdir(parents=True, exist_ok=True)
        raw = text[s['start']:s['end']]
        relpdf = Path(__import__('os').path.relpath(PDF, folder)).as_posix()
        meta = (f"# {s['id']} — {s['title']}\n\n"
                f"Source: PCI Express Base Specification Rev. 1.1 (2005-03-28), "
                f"PDF/printed pages {s['page_start']}–{s['page_end']}. "
                f"[PDF]({relpdf}#page={s['page_start']}).\n\n"
                f"This file contains only this section's direct text; child sections have their own folders. "
                f"Layout, line numbers, page headers and form-feed page breaks are retained. "
                f"Figures and table geometry must be checked in the PDF.\n\n")
        (folder / 'verbatim.md').write_text(meta + '```text\n' + raw + '\n```\n')
        reqs = candidates(raw, s, text)
        requirements.extend(reqs)
        content = (f"# Extracted requirement candidates — {s['id']}\n\n"
                   "These are source paragraphs containing normative or advisory keywords, not an approved "
                   "atomic compliance checklist. Tables, diagrams, implicit constraints and keyword-free rules "
                   "also require review. Preserve conditions, exceptions, device roles and footnotes when "
                   "splitting candidates into verified requirements. `may`, `should` and `must` differ. "
                   "Implementation notes are not automatically normative. Candidate IDs are stable for this source hash.\n\n")
        for r in reqs:
            content += (f"## {r['id']}\n\nStatus: `{r['status']}`. Source page {r['page']}, "
                        f"TXT line {r['source_line']}. Modalities: {', '.join(r['modalities'])}.\n\n"
                        f"```text\n{r['text']}\n```\n\n")
        if not reqs:
            content += "No keyword candidates in the direct text. This does not establish that the section has no requirements.\n"
        (folder / 'requirements.md').write_text(content)
    manifest = dict(source=SOURCE.name, pdf=PDF.name,
                    source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                    pdf_sha256=hashlib.sha256(PDF.read_bytes()).hexdigest(),
                    pdf_pages=508, toc_entries_checked=len(toc), sections=sections)
    (OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    (OUT / 'requirements.json').write_text(json.dumps(requirements, indent=2, ensure_ascii=False) + '\n')
    idx = '# Specification chapter index\n\nEach entry has `verbatim.md`, `summary.md`, and `requirements.md`. Parent text excludes child text.\n\n'
    for s in sections:
        idx += f"- [{s['id']} — {s['title']}]({s['path']}/summary.md) (pp. {s['page_start']}–{s['page_end']}, direct text)\n"
    (OUT / 'INDEX.md').write_text(idx)
    print(f"Generated {len(sections)} sections; {len(requirements)} requirement candidates; {len(toc)} TOC entries checked.")


def validate():
    text, expected, _ = load_sections()
    manifest = json.loads((OUT / 'manifest.json').read_text())
    assert manifest['sections'] == expected
    assert manifest['source_sha256'] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    assert manifest['pdf_sha256'] == hashlib.sha256(PDF.read_bytes()).hexdigest()
    recovered = []
    for s in expected:
        folder = OUT / s['path']
        body = (folder / 'verbatim.md').read_text().split('```text\n', 1)[1].rsplit('\n```\n', 1)[0]
        assert hashlib.sha256(body.encode()).hexdigest() == s['sha256'], s['id']
        assert (folder / 'summary.md').exists(), s['id']
        assert (folder / 'requirements.md').exists(), s['id']
        recovered.append(body)
    assert ''.join(recovered) == text, 'Source round trip failed'
    print(f"PASS: {len(expected)} sections, exact full-text round trip, source hashes and TOC page checks.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    missing = [p.name for p in (SOURCE, PDF) if not p.is_file()]
    if missing:
        raise SystemExit(f'Missing local specification source {missing}. The PCI-SIG files are copyrighted and '
                         'not in the public repository; place your licensed copies in the repository root.')
    validate() if args.check else generate()
