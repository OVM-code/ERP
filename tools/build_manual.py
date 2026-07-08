#!/usr/bin/env python3
"""Compile a client's user manual into one interactive HTML file.

Usage:
    python3 tools/build_manual.py clients/<client-slug> [-o out.html] [--strict] [--dry-run]

Reads (under clients/<slug>/manual/):
    manual-config.json   name, title, language, version, use_bpa_processes
    intro.md             introduction chapter
    chapters/NN-*.md     '# <n>. Chapter title' + '## <CODE> Topic' blocks
                         CODE = BS/BC scenario code (links into the BPMN flows) or
                         MAN-xxx for general topics (login, navigation, …)

Topic metadata (bullets directly under the heading):
    - **Bron:**  bpa | docs: <url> (<BC version>) | bpa + docs: <url> | review
    - **Rol:**   <roles, free text>

Source → colour in the viewer: bpa=blue, docs=purple, review=red (consultant must
review). Topics marked 'review' are auto-collected into a review register (the
viewer's GAPs tab, relabelled). Reuses the BPA viewer and, when
use_bpa_processes=true, the client's BPMN flows for chapters whose number matches a
BPA domain.
"""

from __future__ import annotations

import argparse
import datetime
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_bpa as bb  # md_to_html, split_blocks, load_processes, CATALOG_PATH, VIEWER

TOPIC_HEAD = re.compile(r"^(B[SC]\d{2}\.\d{3}(?:\.\d{2})?|BC\d{2}\.\d{5}|MAN-\d+)\s*[-–—:]?\s*(.*)$")

LABELS = {
    "nl": {
        "intro": "Inleiding", "gaps": "Te reviewen", "search": "Zoek onderwerp of code…",
        "otherScenarios": "Alle onderwerpen in dit hoofdstuk",
        "legendStandard": "Gebaseerd op de BPA", "legendAddon": "Officiële documentatie",
        "legendWorkaround": "Werkafspraak", "legendGap": "Te reviewen door consultant",
        "legendNone": "Niet uitgewerkt",
        "domainDocOnly": "Voor dit hoofdstuk is geen processtroom; de onderwerpen staan hieronder.",
        "fit": {"standard": "Uit de BPA", "addon": "Officiële documentatie",
                "workaround": "Werkafspraak", "gap": "Te reviewen ⚠", "none": "—"},
    },
    "en": {
        "intro": "Introduction", "gaps": "To review", "search": "Search topic or code…",
        "otherScenarios": "All topics in this chapter",
        "legendStandard": "Based on the BPA", "legendAddon": "Official documentation",
        "legendWorkaround": "Agreed practice", "legendGap": "To be reviewed by consultant",
        "legendNone": "Not covered",
        "domainDocOnly": "This chapter has no process flow; its topics are listed below.",
        "fit": {"standard": "From the BPA", "addon": "Official documentation",
                "workaround": "Agreed practice", "gap": "To review ⚠", "none": "—"},
    },
}

SOURCE_FIT = {"bpa": "standard", "docs": "addon", "review": "gap", "afspraak": "workaround",
              "practice": "workaround"}


def parse_source(raw: str):
    """'bpa' | 'docs: <url> (BC24)' | 'bpa + docs: <url>' | 'review' -> (fit, url)."""
    v = (raw or "").strip()
    lv = v.lower()
    url_m = re.search(r"https?://\S+", v)
    url = url_m.group(0).rstrip(").,") if url_m else None
    if not v:
        return "gap", url  # unstated source = must be reviewed
    if lv.startswith("review"):
        return "gap", url
    if "docs" in lv:
        if url is None:
            bb.warn(f"bron 'docs' zonder URL: {raw!r} — voeg de Learn-link toe")
        return "addon", url
    for k, fit in SOURCE_FIT.items():
        if lv.startswith(k):
            return fit, url
    bb.warn(f"onbekende bron {raw!r} — gemarkeerd als 'review'")
    return "gap", url


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("client")
    ap.add_argument("-o", "--output")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    client_dir = Path(args.client).resolve()
    man_dir = client_dir / "manual"
    if not man_dir.is_dir():
        print(f"error: {man_dir} bestaat niet", file=sys.stderr)
        return 1
    slug = client_dir.name

    cfg_path = man_dir / "manual-config.json"
    try:
        cfg = json.loads(cfg_path.read_text(encoding="utf-8-sig")) if cfg_path.exists() else {}
    except json.JSONDecodeError as e:
        print(f"error: {cfg_path}: {e}", file=sys.stderr)
        return 1
    language = cfg.get("language", "nl")
    lab = LABELS.get(language, LABELS["nl"])

    catalog = json.loads(bb.CATALOG_PATH.read_text(encoding="utf-8"))
    cat_by_code = {}
    for s in catalog["scenarios"]:
        cat_by_code.setdefault(s["code"], s)

    scenarios: dict[str, dict] = {}
    domains: list[dict] = []
    review: list[dict] = []

    chapters = sorted((man_dir / "chapters").glob("*.md")) if (man_dir / "chapters").is_dir() else []
    if not chapters:
        bb.warn("geen hoofdstukken gevonden in manual/chapters/")
    for f in chapters:
        preamble, blocks = bb.split_blocks(f.read_text(encoding="utf-8"), TOPIC_HEAD)
        h1 = re.search(r"^#\s+(\d+)\.\s*(.*)$", preamble, re.M)
        if not h1:
            bb.warn(f"{f.name}: verwacht '# <n>. Hoofdstuktitel' bovenaan — overgeslagen")
            continue
        num, title = int(h1.group(1)), h1.group(2).strip()
        preamble = re.sub(r"^#\s+.*$", "", preamble, count=1, flags=re.M).strip()
        codes = []
        for b in blocks:
            code = b["key"]
            fit, url = parse_source(b["meta"].get("bron") or b["meta"].get("source") or "")
            if code.startswith(("BS", "BC")) and code not in cat_by_code:
                bb.warn(f"{f.name}: {code} staat niet in de catalogus")
            body = b["body"]
            if url:
                src_line = {"nl": "Gebaseerd op officiële documentatie", "en": "Based on official documentation"}[language if language in ("nl", "en") else "nl"]
                body += f"\n\n> {src_line}: {url}"
            scenarios[code] = {
                "code": code,
                "title": b["title"] or (cat_by_code.get(code, {}).get("title", code)),
                "section": cat_by_code.get(code, {}).get("section"),
                "domain": num,
                "fit": fit,
                "addon": None,
                "gap": code if fit == "gap" else None,
                "requirements": [],
                "html": bb.md_to_html(body),
            }
            codes.append(code)
            if fit == "gap":
                note = b["meta"].get("review") or b["meta"].get("toelichting") or ""
                review.append({
                    "id": code, "title": b["title"] or code, "scenarios": [code],
                    "html": bb.md_to_html(note) if note else "",
                })
        domains.append({"number": num, "title": title,
                        "intro_html": bb.md_to_html(preamble) if preamble else "",
                        "process": None, "scenarios": codes})

    # attach the client's BPA process flows to matching chapters
    if cfg.get("use_bpa_processes", True):
        procs = bb.load_processes(client_dir / "bpa")
        for d in domains:
            if d["number"] in procs:
                d["process"] = procs[d["number"]]
    domains.sort(key=lambda d: d["number"])

    intro_path = man_dir / "intro.md"
    intro_html = bb.md_to_html(intro_path.read_text(encoding="utf-8")) if intro_path.exists() else ""

    default_title = {"nl": "Gebruikershandleiding", "en": "User manual"}.get(language, "User manual")
    data = {
        "client": {
            "name": cfg.get("name", slug),
            "title": cfg.get("title", default_title),
            "period": cfg.get("period", ""),
            "language": language,
            "intro_html": intro_html,
            "labels": {**lab, **cfg.get("labels", {})},
        },
        "meta": {"model": "", "version": cfg.get("version", ""),
                 "stack": cfg.get("stack", {}),
                 "generated": datetime.date.today().isoformat()},
        "domains": domains,
        "scenarios": scenarios,
        "coverage": [],       # tab hidden
        "requirements": [],   # tab hidden
        "gaps": review,       # relabelled "Te reviewen"
    }

    tpl = (bb.VIEWER / "template.html").read_text(encoding="utf-8")
    css = bb.branding_css() + (bb.VIEWER / "viewer.css").read_text(encoding="utf-8")
    js = (bb.VIEWER / "viewer.js").read_text(encoding="utf-8")
    if cfg.get("accentColor"):
        css += f'\n:root {{ --accent: {cfg["accentColor"]}; }}\n'
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out_html = (tpl
                .replace("__BPA_LANG__", language)
                .replace("__BPA_TITLE__", html.escape(f"{data['client']['title']} — {data['client']['name']}"))
                .replace("/*__BPA_CSS__*/", css)
                .replace("/*__BPA_DATA__*/ null", payload)
                .replace("/*__BPA_JS__*/", js))

    out_path = Path(args.output) if args.output else man_dir / "output" / f"Manual-{slug}.html"
    if not args.dry_run:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out_html, encoding="utf-8")

    print(("gecontroleerd (dry-run): " if args.dry_run else "Handleiding gebouwd: ") + str(out_path))
    print(f"  {len(domains)} hoofdstukken · {len(scenarios)} onderwerpen · "
          f"{len(review)} te reviewen door consultant")
    if bb.WARNINGS:
        print(f"  {len(bb.WARNINGS)} waarschuwing(en)")
        if args.strict:
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
