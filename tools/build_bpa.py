#!/usr/bin/env python3
"""Compile a client's Business Process Analysis into one interactive HTML file.

Usage:
    python3 tools/build_bpa.py clients/<client-slug> [-o output.html]

Reads (all under clients/<slug>/bpa/):
    bpa-config.json        client name, period, language, accent colour, …
    intro.md               the "Inleiding" chapter (client-specific)
    requirements.md        ## REQ-xxx blocks extracted from workshops/transcripts
    coverage.md            scope matrix table (scenario | scope | invulling | note)
    content/*.md           enriched BPA documentation per domain (## BSxx.xxx blocks)
    gaps.md                ## GAP-x blocks (maatwerk register)
    processes/*.process.json  client process flows; falls back to bpa/processes/

Plus the shared assets:
    bpa/template/catalog.json  scenario catalog (codes, titles, domains, add-on flags)
    bpa/processes/*.process.json standard flows (fallback)
    bpa/viewer/{template.html,viewer.css,viewer.js}

Writes:
    clients/<slug>/bpa/output/BPA-<slug>.html  (self-contained, offline, shareable)

Python stdlib only — no dependencies.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CATALOG_PATH = REPO / "bpa" / "template" / "catalog.json"
STD_PROCESSES = REPO / "bpa" / "processes"
VIEWER = REPO / "bpa" / "viewer"
BRANDING = REPO / "bpa" / "branding"


def branding_css() -> str:
    """Cegeka design tokens + logo data-URIs, prepended to the viewer CSS so the
    built HTML stays fully self-contained (see bpa/branding/README.md)."""
    import base64
    parts = []
    tokens = BRANDING / "tokens.css"
    if tokens.exists():
        parts.append(tokens.read_text(encoding="utf-8"))
    logos = []
    for prop, fname in (("--cg-logo-dark", "cegeka-logo-dark.png"),
                        ("--cg-logo-white", "cegeka-logo-white.png")):
        f = BRANDING / fname
        if f.exists():
            b64 = base64.b64encode(f.read_bytes()).decode("ascii")
            logos.append(f'  {prop}: url("data:image/png;base64,{b64}");')
    if logos:
        parts.append(":root {\n" + "\n".join(logos) + "\n}")
    return "\n".join(parts) + ("\n" if parts else "")

CODE_RE = re.compile(r"\bB[SC]\d{2}\.\d{3}(?:\.\d{2})?\b|\bBC\d{2}\.\d{5}\b")
WARNINGS: list[str] = []


def warn(msg: str) -> None:
    WARNINGS.append(msg)
    print(f"  ! {msg}", file=sys.stderr)


# --------------------------------------------------------------------------- markdown
INLINE_RULES = [
    (re.compile(r"`([^`]+)`"), lambda m: f"<code>{html.escape(m.group(1))}</code>"),
    (re.compile(r"\*\*([^*]+)\*\*"), r"<strong>\1</strong>"),
    (re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])"), r"<em>\1</em>"),
    (re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)"), r'<a href="\2" target="_blank" rel="noopener">\1</a>'),
]


def md_inline(text: str) -> str:
    out = html.escape(text, quote=False)
    for rule, repl in INLINE_RULES:
        out = rule.sub(repl, out)
    return out


def md_to_html(md: str) -> str:
    """Small CommonMark-ish renderer: headings, lists (2 levels), tables,
    blockquotes, hr, paragraphs, inline bold/italic/code/links."""
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    para: list[str] = []
    lists: list[str] = []  # stack of open list tags
    in_quote = False

    def flush_para() -> None:
        if para:
            out.append("<p>" + md_inline(" ".join(para)) + "</p>")
            para.clear()

    def close_lists(depth: int = 0) -> None:
        while len(lists) > depth:
            out.append(f"</{lists.pop()}>")

    def close_quote() -> None:
        nonlocal in_quote
        if in_quote:
            out.append("</blockquote>")
            in_quote = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # table block
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|?\s*$", lines[i + 1]) and "-" in lines[i + 1]:
            flush_para(); close_lists(); close_quote()
            header = [md_inline(c.strip()) for c in stripped.strip("|").split("|")]
            out.append("<table><thead><tr>" + "".join(f"<th>{c}</th>" for c in header) + "</tr></thead><tbody>")
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [md_inline(c.strip()) for c in lines[i].strip().strip("|").split("|")]
                out.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
                i += 1
            out.append("</tbody></table>")
            continue

        m_h = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        m_ul = re.match(r"^(\s*)[-*+]\s+(.*)$", line)
        m_ol = re.match(r"^(\s*)\d+[.)]\s+(.*)$", line)

        if not stripped:
            flush_para(); close_lists(); close_quote()
        elif m_h:
            flush_para(); close_lists(); close_quote()
            level = len(m_h.group(1))
            out.append(f"<h{level}>{md_inline(m_h.group(2))}</h{level}>")
        elif re.match(r"^(-{3,}|\*{3,}|_{3,})$", stripped):
            flush_para(); close_lists(); close_quote()
            out.append("<hr>")
        elif stripped.startswith(">"):
            flush_para(); close_lists()
            if not in_quote:
                out.append("<blockquote>")
                in_quote = True
            out.append("<p>" + md_inline(stripped.lstrip("> ").strip()) + "</p>")
        elif m_ul or m_ol:
            flush_para(); close_quote()
            indent, item = (m_ul or m_ol).group(1), (m_ul or m_ol).group(2)
            depth = 2 if len(indent) >= 2 else 1
            tag = "ul" if m_ul else "ol"
            while len(lists) > depth:
                out.append(f"</{lists.pop()}>")
            while len(lists) < depth:
                lists.append(tag)
                out.append(f"<{tag}>")
            out.append(f"<li>{md_inline(item)}</li>")
        else:
            if in_quote:
                out.append("<p>" + md_inline(stripped) + "</p>")
            elif lists and out and out[-1].endswith("</li>"):
                # continuation line of a wrapped list item
                out[-1] = out[-1][: -len("</li>")] + " " + md_inline(stripped) + "</li>"
            else:
                close_lists()
                para.append(stripped)
        i += 1

    flush_para(); close_lists(); close_quote()
    return "\n".join(out)


# --------------------------------------------------------------------------- parsing
META_LINE = re.compile(r"^\s*[-*]\s+\*\*([^:*]+):?\*\*:?\s*(.*)$")


def split_blocks(md: str, heading_re: re.Pattern) -> tuple[str, list[dict]]:
    """Split a markdown file into (preamble, [{key, title, meta{}, body}]) on ## headings
    matching heading_re. Metadata bullets (- **Field:** value) directly under a heading
    are lifted out of the body."""
    lines = md.replace("\r\n", "\n").split("\n")
    preamble: list[str] = []
    blocks: list[dict] = []
    cur: dict | None = None
    meta_zone = False
    for line in lines:
        m = re.match(r"^##\s+(.*)$", line.strip())
        hm = heading_re.match(m.group(1).strip()) if m else None
        if hm:
            cur = {"key": hm.group(1), "title": (hm.group(2) or "").strip(" -–—:"), "meta": {}, "body": []}
            blocks.append(cur)
            meta_zone = True
            continue
        if cur is None:
            preamble.append(line)
            continue
        if meta_zone:
            mm = META_LINE.match(line)
            if mm:
                cur["meta"][mm.group(1).strip().lower().rstrip(":")] = mm.group(2).strip()
                continue
            if line.strip():
                meta_zone = False
        cur["body"].append(line)
    for b in blocks:
        b["body"] = "\n".join(b["body"]).strip()
    return "\n".join(preamble).strip(), blocks


def parse_fit(raw: str) -> tuple[str, str | None, str | None]:
    """'standaard' | 'standard' | 'add-on: Aptean' | 'workaround' | 'gap: GAP-2'
    -> (fit, addon, gap)"""
    v = (raw or "").strip()
    lv = v.lower()
    if not v:
        return "none", None, None
    if lv.startswith(("gap", "maatwerk")):
        gm = re.search(r"GAP-\d+", v, re.I)
        return "gap", None, (gm.group(0).upper() if gm else None)
    if lv.startswith(("add-on", "addon", "add on", "isv")):
        name = re.sub(r"^(add[- ]?on|isv)\s*:?", "", v, flags=re.I).strip() or None
        return "addon", name, None
    if lv.startswith("workaround"):
        return "workaround", None, None
    if lv.startswith(("standaard", "standard")):
        return "standard", None, None
    warn(f"onbekende invulling '{raw}' — behandeld als 'standard'")
    return "standard", None, None


def parse_codes(raw: str) -> list[str]:
    return CODE_RE.findall(raw or "")


def parse_coverage(md: str) -> list[dict]:
    """Parse the coverage matrix table. Expected columns:
    | Code | Scenario | Domein | Scope | Invulling | Toelichting |"""
    rows = []
    for line in md.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 4 or not CODE_RE.match(cells[0]):
            continue
        code = cells[0]
        title = cells[1] if len(cells) > 1 else ""
        dom_m = re.search(r"\d+", cells[2]) if len(cells) > 2 else None
        scope_raw = cells[3].lower() if len(cells) > 3 else ""
        in_scope = any(t in scope_raw for t in ("in", "ja", "yes", "x", "✓")) and "uit" not in scope_raw and "nee" not in scope_raw and "niet" not in scope_raw
        fit, addon, gap = parse_fit(cells[4]) if len(cells) > 4 and cells[4] not in ("", "—", "-") else ("none", None, None)
        rows.append({
            "code": code,
            "title": title,
            "domain": int(dom_m.group(0)) if dom_m else None,
            "scope": in_scope,
            "fit": fit if in_scope else None,
            "addon": addon,
            "gap": gap,
            "note": cells[5] if len(cells) > 5 else "",
        })
    return rows


# --------------------------------------------------------------------------- build
def load_processes(client_bpa: Path) -> dict[int, dict]:
    """Client processes win; standard flows are the fallback."""
    procs: dict[int, dict] = {}
    for src in (STD_PROCESSES, client_bpa / "processes"):
        if not src.is_dir():
            continue
        for f in sorted(src.glob("*.process.json")):
            try:
                p = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                warn(f"{f}: ongeldig JSON ({e}) — overgeslagen")
                continue
            procs[p["domain"]] = p
    return procs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("client", help="path to the client folder, e.g. clients/acme-food")
    ap.add_argument("-o", "--output", help="output HTML path (default: <client>/bpa/output/BPA-<slug>.html)")
    ap.add_argument("--strict", action="store_true", help="exit non-zero if any warning was raised")
    ap.add_argument("--dry-run", action="store_true", help="validate only, write nothing")
    args = ap.parse_args()

    client_dir = Path(args.client).resolve()
    bpa_dir = client_dir / "bpa"
    if not bpa_dir.is_dir():
        print(f"error: {bpa_dir} bestaat niet — is dit een clientmap met een bpa/ workspace?", file=sys.stderr)
        return 1
    slug = client_dir.name

    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    cat_by_code: dict[str, dict] = {}
    for s in catalog["scenarios"]:
        cat_by_code.setdefault(s["code"], s)
    cat_domains = {d["number"]: d["title"] for d in catalog["domains"] if d["number"] > 0}

    cfg_path = bpa_dir / "bpa-config.json"
    cfg = {}
    if cfg_path.exists():
        try:
            cfg = json.loads(cfg_path.read_text(encoding="utf-8-sig"))
        except json.JSONDecodeError as e:
            print(f"error: {cfg_path} is geen geldig JSON: {e}", file=sys.stderr)
            return 1
    client_name = cfg.get("name", slug)
    language = cfg.get("language", "nl")

    # ---- requirements -------------------------------------------------------------
    requirements: list[dict] = []
    req_path = bpa_dir / "requirements.md"
    if req_path.exists():
        _, blocks = split_blocks(req_path.read_text(encoding="utf-8"),
                                 re.compile(r"^(REQ-\d+)\s*[-–—:]?\s*(.*)$"))
        seen_req = set()
        for b in blocks:
            if b["key"] in seen_req:
                warn(f"requirements.md: {b['key']} komt meermaals voor")
            seen_req.add(b["key"])
            requirements.append({
                "id": b["key"],
                "title": b["title"],
                "source": b["meta"].get("bron") or b["meta"].get("source") or "",
                "scenarios": parse_codes(b["meta"].get("scenario's") or b["meta"].get("scenarios") or ""),
                "html": md_to_html(b["body"]),
            })

    # ---- gaps ---------------------------------------------------------------------
    gaps: list[dict] = []
    gaps_path = bpa_dir / "gaps.md"
    if gaps_path.exists():
        _, blocks = split_blocks(gaps_path.read_text(encoding="utf-8"),
                                 re.compile(r"^(GAP-\d+)\s*[-–—:]?\s*(.*)$"))
        seen_gap = set()
        for b in blocks:
            if b["key"] in seen_gap:
                warn(f"gaps.md: {b['key']} komt meermaals voor")
            seen_gap.add(b["key"])
            gaps.append({
                "id": b["key"],
                "title": b["title"],
                "scenarios": parse_codes(b["meta"].get("scenario's") or b["meta"].get("scenarios") or ""),
                "html": md_to_html(b["body"]),
            })
    gap_ids = {g["id"] for g in gaps}

    # ---- content (scenario documentation per domain) --------------------------------
    scenarios: dict[str, dict] = {}
    domain_intro: dict[int, str] = {}
    domain_title: dict[int, str] = {}
    domain_order: dict[int, list[str]] = {}
    content_dir = bpa_dir / "content"
    scen_head = re.compile(r"^(B[SC]\d{2}\.\d{3}(?:\.\d{2})?|BC\d{2}\.\d{5})\s*[-–—:]?\s*(.*)$")
    for f in sorted(content_dir.glob("*.md")) if content_dir.is_dir() else []:
        text = f.read_text(encoding="utf-8")
        preamble, blocks = split_blocks(text, scen_head)
        # domain number: from "# <n>. Title" in preamble, else from filename NN-…
        dom = None
        h1 = re.search(r"^#\s+(\d+)\.\s*(.*)$", preamble, re.M)
        if h1:
            dom = int(h1.group(1))
            domain_title[dom] = h1.group(2).strip()
            preamble = re.sub(r"^#\s+.*$", "", preamble, count=1, flags=re.M).strip()
        else:
            fm = re.match(r"^(\d+)", f.stem)
            if fm:
                dom = int(fm.group(1))
        if dom is None:
            warn(f"{f.name}: domeinnummer niet gevonden (verwacht '# <n>. Titel' of bestandsnaam 'NN-…') — overgeslagen")
            continue
        if preamble:
            domain_intro[dom] = md_to_html(preamble)
        for b in blocks:
            code = b["key"]
            cat = cat_by_code.get(code)
            if not cat:
                warn(f"{f.name}: {code} staat niet in de template-catalogus (typfout?)")
            if code in scenarios:
                warn(f"{f.name}: {code} is al gedocumenteerd in een ander blok/bestand — laatste wint")
            fit, addon, gap = parse_fit(b["meta"].get("invulling") or b["meta"].get("fit") or "standard")
            if fit == "addon" and not addon and cat and cat.get("addon"):
                addon = cat["addon"]
            if gap and gap not in gap_ids:
                warn(f"{f.name}: {code} verwijst naar {gap} maar die staat niet in gaps.md")
            reqs = parse_codes_req(b["meta"].get("requirements") or "")
            scenarios[code] = {
                "code": code,
                "title": b["title"] or (cat["title"] if cat else code),
                "section": cat["section"] if cat else None,
                "domain": dom,
                "fit": fit,
                "addon": addon or (cat.get("addon") if cat else None),
                "gap": gap,
                "requirements": reqs,
                "html": md_to_html(b["body"]),
            }
            domain_order.setdefault(dom, []).append(code)

    # requirements <-> scenarios: make links symmetric
    for r in requirements:
        for code in r["scenarios"]:
            if code in scenarios and r["id"] not in scenarios[code]["requirements"]:
                scenarios[code]["requirements"].append(r["id"])
    for code, s in scenarios.items():
        for rid in s["requirements"]:
            r = next((x for x in requirements if x["id"] == rid), None)
            if r is None:
                warn(f"{code} verwijst naar {rid} maar die staat niet in requirements.md")
            elif code not in r["scenarios"]:
                r["scenarios"].append(code)
    for g in gaps:
        for code in list(g["scenarios"]):
            if code in scenarios and scenarios[code]["gap"] is None:
                scenarios[code]["gap"] = g["id"]
    for code, s in scenarios.items():
        if s["gap"]:
            g = next((x for x in gaps if x["id"] == s["gap"]), None)
            if g and code not in g["scenarios"]:
                g["scenarios"].append(code)

    # ---- coverage -------------------------------------------------------------------
    coverage: list[dict] = []
    cov_path = bpa_dir / "coverage.md"
    if cov_path.exists():
        coverage = parse_coverage(cov_path.read_text(encoding="utf-8"))
    cov_codes = {c["code"] for c in coverage}
    for c in coverage:
        if c["domain"] is None:
            cat = cat_by_code.get(c["code"])
            c["domain"] = cat["domain"] if cat else 0
        if not c["title"]:
            cat = cat_by_code.get(c["code"])
            c["title"] = cat["title"] if cat else c["code"]
        if c["scope"] and c["code"] not in scenarios:
            warn(f"coverage: {c['code']} is 'in scope' maar heeft geen documentatie in content/")
        if c["scope"] and c["fit"] in (None, "none") and c["code"] in scenarios:
            c["fit"] = scenarios[c["code"]]["fit"]
    for code, s in sorted(scenarios.items()):
        if code not in cov_codes:
            coverage.append({
                "code": code, "title": s["title"], "domain": s["domain"], "scope": True,
                "fit": s["fit"], "addon": s["addon"], "gap": s["gap"], "note": "",
            })
    coverage.sort(key=lambda c: (c["domain"] if c["domain"] is not None else 99,
                                 cat_by_code.get(c["code"], {}).get("section") or "zz",
                                 c["code"]))

    # ---- processes ------------------------------------------------------------------
    procs = load_processes(bpa_dir)

    # ---- domains: everything with documentation or in-scope coverage -----------------
    domain_numbers = sorted(set(list(domain_order.keys()) +
                                [c["domain"] for c in coverage if c["scope"] and c["domain"]]))
    domains = []
    for dom in domain_numbers:
        proc = procs.get(dom)
        domains.append({
            "number": dom,
            "title": domain_title.get(dom) or cat_domains.get(dom, f"Domein {dom}"),
            "intro_html": domain_intro.get(dom, ""),
            "process": proc,
            "scenarios": domain_order.get(dom, []),
        })

    # ---- intro ----------------------------------------------------------------------
    intro_path = bpa_dir / "intro.md"
    intro_html = md_to_html(intro_path.read_text(encoding="utf-8")) if intro_path.exists() else ""

    import datetime
    data = {
        "client": {
            "name": client_name,
            "title": cfg.get("title", "Business Process Analyse"),
            "period": cfg.get("period", ""),
            "language": language,
            "intro_html": intro_html,
            "labels": cfg.get("labels", {}),
        },
        "meta": {
            "model": catalog.get("model", ""),
            "version": cfg.get("version", ""),
            "stack": cfg.get("stack", {}),
            "generated": datetime.date.today().isoformat(),
        },
        "domains": domains,
        "scenarios": scenarios,
        "coverage": coverage,
        "requirements": requirements,
        "gaps": gaps,
    }

    # ---- assemble -------------------------------------------------------------------
    tpl = (VIEWER / "template.html").read_text(encoding="utf-8")
    css = branding_css() + (VIEWER / "viewer.css").read_text(encoding="utf-8")
    js = (VIEWER / "viewer.js").read_text(encoding="utf-8")
    if cfg.get("accentColor"):
        css += f'\n:root {{ --accent: {cfg["accentColor"]}; }}\n'
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out_html = (tpl
                .replace("__BPA_LANG__", cfg.get("language", "nl"))
                .replace("__BPA_TITLE__", html.escape(f"{data['client']['title']} — {client_name}"))
                .replace("/*__BPA_CSS__*/", css)
                .replace("/*__BPA_DATA__*/ null", payload)
                .replace("/*__BPA_JS__*/", js))

    out_path = Path(args.output) if args.output else bpa_dir / "output" / f"BPA-{slug}.html"
    if not args.dry_run:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out_html, encoding="utf-8")

    in_scope = sum(1 for c in coverage if c["scope"])
    print(("gecontroleerd (dry-run): " if args.dry_run else "BPA gebouwd: ") + str(out_path))
    print(f"  {len(domains)} domeinen · {len(scenarios)} gedocumenteerde scenario's · "
          f"{in_scope} in scope · {len(requirements)} requirements · {len(gaps)} gaps")
    if WARNINGS:
        print(f"  {len(WARNINGS)} waarschuwing(en) — zie hierboven")
        if args.strict:
            return 2
    return 0


def parse_codes_req(raw: str) -> list[str]:
    return re.findall(r"REQ-\d+", raw or "")


if __name__ == "__main__":
    sys.exit(main())
