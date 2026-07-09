#!/usr/bin/env python3
"""Business Process Catalog — the standing, evidence-based register of business
processes that consultants have, at some point, deemed settable-up with standard
Business Central (plus frequently used add-on processes).

The catalog is decoupled from the per-client freshness check: it refreshes at
most once a month (see bpa/catalog/refresh-log.md and the /catalog-refresh
skill) and is the input that client BPA scenario-mapping starts from. It also
*challenges* the Cegeka template: the reconciliation report lists what the
template claims without evidence, what went stale, and what the template lacks.

Usage:
    python3 tools/catalog.py seed        # create/sync catalog from template + harvest evidence
    python3 tools/catalog.py reconcile   # (re)write bpa/catalog/vs-template-report.md
    python3 tools/catalog.py check       # validate (used by tools/doctor.py); exit 1 on problems

`seed` is idempotent: template structure (titles, sections, domains) is synced,
but status / evidence / last_verified / notes curated by refreshes are kept.

NUMBERING INVARIANT: the BS/BC scenario numbering of the original Cegeka BPA
template is the master — the cost model (pricing/effort-baselines.json) and all
client workspaces key on these codes, so the catalog NEVER renumbers or reuses
them. New scenarios discovered by a refresh enter only as `status: candidate`
(in_template: false) and must be flagged in system/reviews/register.md; they get
a real template number only when a human approves adding them to the template.
`check` enforces both rules.

Python stdlib only — no dependencies.
"""

from __future__ import annotations

import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_bpa as bb  # parse_coverage, split_blocks, parse_fit, CODE_RE

REPO = Path(__file__).resolve().parent.parent
TEMPLATE_CATALOG = REPO / "bpa" / "template" / "catalog.json"
CATALOG_DIR = REPO / "bpa" / "catalog"
CATALOG = CATALOG_DIR / "catalog.json"
DOC_URL_MAP = CATALOG_DIR / "doc-url-map.json"
REPORT = CATALOG_DIR / "vs-template-report.md"
REFRESH_LOG = CATALOG_DIR / "refresh-log.md"
CLIENTS = REPO / "clients"

STALE_MONTHS = 12  # verified entries older than this are reported as stale


def is_demo(slug: str) -> bool:
    return slug.startswith("_")


# ------------------------------------------------------------------ evidence harvest
def harvest_evidence() -> dict[str, list[str]]:
    """Collect per-scenario evidence from every client workspace and the
    expertise layer. Demo clients count as illustration, not verification."""
    ev: dict[str, list[str]] = {}

    def add(code: str, source: str) -> None:
        ev.setdefault(code, [])
        if source not in ev[code]:
            ev[code].append(source)

    if CLIENTS.is_dir():
        for client in sorted(CLIENTS.iterdir()):
            if not client.is_dir() or client.name == "_template":
                continue
            slug = client.name
            tag = f"client:{slug}" + (" (demo)" if is_demo(slug) else "")
            cov = client / "bpa" / "coverage.md"
            if cov.exists():
                for row in bb.parse_coverage(cov.read_text(encoding="utf-8")):
                    if row["scope"] and row["fit"] and row["fit"] != "none":
                        add(row["code"], f"{tag} · {row['fit']}")
            content = client / "bpa" / "content"
            if content.is_dir():
                head = re.compile(r"^(B[SC]\d{2}\.\d{3}(?:\.\d{2})?|BC\d{2}\.\d{5})\s*[-–—:]?\s*(.*)$")
                for f in sorted(content.glob("*.md")):
                    _, blocks = bb.split_blocks(f.read_text(encoding="utf-8"), head)
                    for b in blocks:
                        fit, _, _ = bb.parse_fit(b["meta"].get("invulling") or b["meta"].get("fit") or "")
                        if fit != "none":
                            add(b["key"], f"{tag} · {fit}")
            decisions = client / "decisions"
            if decisions.is_dir():
                for f in sorted(decisions.glob("SDR-*.md")):
                    for code in set(bb.CODE_RE.findall(f.read_text(encoding="utf-8"))):
                        add(code, f"sdr:{slug}/{f.stem}" + (" (demo)" if is_demo(slug) else ""))

    lessons = REPO / "expertise" / "lessons-learned.md"
    if lessons.exists():
        text = lessons.read_text(encoding="utf-8")
        for m in re.finditer(r"^##\s+(LL-\d+)", text, re.M):
            block_start = m.end()
            nxt = text.find("\n## ", block_start)
            block = text[block_start: nxt if nxt >= 0 else len(text)]
            for code in set(bb.CODE_RE.findall(block)):
                add(code, f"ll:{m.group(1)}")
    return ev


def real_evidence(entry: dict) -> list[str]:
    """Evidence that verifies (excludes template import and demo material)."""
    return [e for e in entry.get("evidence", [])
            if not e.startswith("template:") and "(demo)" not in e]


def apply_doc_url(entry: dict, docmap: dict) -> None:
    """Two-tier documentation URL per scenario (review requirement):
    - 'specific': the exact page a verification actually consulted (from
      docs:<url> evidence) — always wins, upgrades a topic URL;
    - 'topic': curated official landing page per add-on/domain from
      bpa/catalog/doc-url-map.json — every scenario has at least this;
    - 'none': no official public docs exist (Cegeka-internal layer, GAPs)."""
    specific = next((e[5:] for e in entry.get("evidence", []) if e.startswith("docs:")), None)
    if specific:
        entry["doc_url"] = specific
        entry["doc_url_level"] = "specific"
        return
    if entry.get("doc_url") and entry.get("doc_url_level") == "specific":
        return  # manually curated specific URL survives
    url = None
    addon = entry.get("addon")
    if addon and docmap.get("addons", {}).get(addon):
        url = docmap["addons"][addon]
    if url is None:
        url = docmap.get("domains", {}).get(str(entry.get("domain")))
    entry["doc_url"] = url
    entry["doc_url_level"] = "topic" if url else "none"


# ------------------------------------------------------------------ seed
def seed() -> int:
    template = json.loads(TEMPLATE_CATALOG.read_text(encoding="utf-8"))
    tpl_by_code: dict[str, dict] = {}
    for s in template["scenarios"]:
        tpl_by_code.setdefault(s["code"], s)

    existing: dict[str, dict] = {}
    version = 0
    if CATALOG.exists():
        cur = json.loads(CATALOG.read_text(encoding="utf-8"))
        version = cur.get("version", 0)
        existing = {e["code"]: e for e in cur.get("scenarios", [])}

    tpl_version = template.get("model", "Cegeka Process Model")
    evidence = harvest_evidence()
    docmap = json.loads(DOC_URL_MAP.read_text(encoding="utf-8")) if DOC_URL_MAP.exists() else {}
    scenarios: list[dict] = []

    for code, t in tpl_by_code.items():
        e = existing.get(code, {
            "code": code,
            "status": "unverified",
            "evidence": [f"template:{tpl_version}"],
            "last_verified": None,
            "notes": "",
        })
        # template is the structure master; refreshes own the curation fields
        e["title"] = t["title"]
        e["section"] = t.get("section")
        e["domain"] = t.get("domain")
        e["addon"] = t.get("addon")
        e["fulfilment"] = "addon" if t.get("addon") else e.get("fulfilment", "standard")
        e["in_template"] = True
        for src in evidence.get(code, []):
            if src not in e["evidence"]:
                e["evidence"].append(src)
        if e["status"] == "unverified" and real_evidence(e):
            e["status"] = "verified"
            e.setdefault("last_verified", None)
            if not e["last_verified"]:
                e["last_verified"] = datetime.date.today().strftime("%Y-%m")
        apply_doc_url(e, docmap)
        scenarios.append(e)

    # catalog-only entries: keep — they are either candidates (template gaps)
    # or retired scenarios kept for history
    for code, e in existing.items():
        if code in tpl_by_code:
            continue
        e["in_template"] = False
        if e.get("status") not in ("candidate", "retired"):
            e["status"] = "retired"
            e["notes"] = (e.get("notes", "") + " Niet (meer) in de template.").strip()
        apply_doc_url(e, docmap)
        scenarios.append(e)

    scenarios.sort(key=lambda s: (s.get("domain") or 99, s.get("section") or "zz", s["code"]))
    out = {
        "version": version + 1,
        "updated": datetime.date.today().isoformat(),
        "source": ("Evidence-based Business Process Catalog — seeded from "
                   f"{tpl_version} and curated by monthly refreshes "
                   "(see bpa/catalog/README.md)"),
        "model": tpl_version,
        "domains": [d for d in template.get("domains", []) if d.get("number", 0) > 0],
        "scenarios": scenarios,
    }
    CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    CATALOG.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    n_ver = sum(1 for s in scenarios if s["status"] == "verified")
    urls = {"specific": 0, "topic": 0, "none": 0}
    for s in scenarios:
        urls[s.get("doc_url_level") or "none"] = urls.get(s.get("doc_url_level") or "none", 0) + 1
    print(f"catalogus geschreven: {CATALOG.relative_to(REPO)} (v{out['version']})")
    print(f"  {len(scenarios)} scenario's · {n_ver} verified · "
          f"{sum(1 for s in scenarios if s['status'] == 'unverified')} unverified · "
          f"{sum(1 for s in scenarios if not s['in_template'])} niet in template")
    print(f"  documentatie-URL's: {urls['specific']} specifiek · {urls['topic']} topic · {urls['none']} geen")
    return 0


# ------------------------------------------------------------------ reconcile
def months_ago(ym: str | None) -> int | None:
    if not ym:
        return None
    try:
        y, m = int(ym[:4]), int(ym[5:7])
    except ValueError:
        return None
    today = datetime.date.today()
    return (today.year - y) * 12 + (today.month - m)


def reconcile() -> int:
    if not CATALOG.exists():
        print("error: catalogus ontbreekt — draai eerst: python3 tools/catalog.py seed", file=sys.stderr)
        return 1
    cat = json.loads(CATALOG.read_text(encoding="utf-8"))
    scen = cat["scenarios"]
    dom_title = {d["number"]: d["title"] for d in cat.get("domains", [])}

    unverified = [s for s in scen if s["status"] == "unverified" and s.get("in_template")]
    stale = [s for s in scen if s["status"] == "verified"
             and (months_ago(s.get("last_verified")) or 0) > STALE_MONTHS]
    candidates = [s for s in scen if s["status"] == "candidate"]
    retired = [s for s in scen if s["status"] == "retired"]
    frequent_addon = [s for s in scen if s.get("addon") and len(real_evidence(s)) >= 2]

    by_dom: dict[int, list[dict]] = {}
    for s in unverified:
        by_dom.setdefault(s.get("domain") or 0, []).append(s)

    L: list[str] = []
    L.append("# Catalogus ↔ template — reconciliatierapport")
    L.append("")
    L.append(f"> Gegenereerd door `python3 tools/catalog.py reconcile` op {datetime.date.today().isoformat()} "
             f"(catalogus v{cat.get('version')}, {len(scen)} scenario's).")
    L.append("> Dit rapport *daagt de template uit*: het toont wat de template claimt zonder bewijs,")
    L.append("> wat verouderd is en wat er ontbreekt. Wijzigingen aan `bpa/template/` die hieruit")
    L.append("> volgen lopen via `/review-system` — niets wordt automatisch aangepast.")
    L.append("")
    L.append("## Samenvatting")
    L.append("")
    L.append("| Categorie | Aantal | Actie |")
    L.append("|---|---|---|")
    L.append(f"| Template-claims zonder bewijs (unverified) | {len(unverified)} | verifiëren bij volgende refresh of eerste klantgebruik |")
    L.append(f"| Verified maar > {STALE_MONTHS} mnd niet herbevestigd (stale) | {len(stale)} | herverifiëren tegen actuele BC-release |")
    L.append(f"| In catalogus, niet in template (candidates) | {len(candidates)} | voorstel: toevoegen aan template |")
    L.append(f"| Retired (uit template verdwenen / niet meer haalbaar) | {len(retired)} | controleren of klanten ze nog gebruiken |")
    L.append(f"| Add-on-scenario's met ≥ 2 echte gebruiken | {len(frequent_addon)} | kandidaat vaste catalogus-kern |")
    urls = {"specific": 0, "topic": 0, "none": 0}
    for s in scen:
        urls[s.get("doc_url_level") or "none"] = urls.get(s.get("doc_url_level") or "none", 0) + 1
    L.append(f"| Documentatie-URL's: specifiek / topic / geen | {urls['specific']} / {urls['topic']} / {urls['none']} | topic-URL's worden specifiek bij verificatie |")
    L.append("")

    L.append("## A. Template-claims zonder bewijs")
    L.append("")
    L.append("Scenario's die alleen op de template-import steunen — geen enkele klant, SDR of")
    L.append("les bevestigt ze, en geen refresh heeft ze tegen officiële bronnen gecheckt.")
    L.append("")
    for dom in sorted(by_dom):
        items = by_dom[dom]
        codes = " · ".join(f"`{s['code']}`" for s in items)
        L.append(f"- **{dom}. {dom_title.get(dom, '?')}** ({len(items)}): {codes}")
    L.append("")

    L.append(f"## B. Stale (> {STALE_MONTHS} maanden niet herbevestigd)")
    L.append("")
    if stale:
        L.append("| Code | Scenario | Laatst geverifieerd |")
        L.append("|---|---|---|")
        for s in sorted(stale, key=lambda x: x.get("last_verified") or ""):
            L.append(f"| `{s['code']}` | {s['title']} | {s.get('last_verified')} |")
    else:
        L.append("Geen.")
    L.append("")

    L.append("## C. Niet in de template (kandidaten & retired)")
    L.append("")
    L.append("De template-nummering is de master — het kostenmodel (`pricing/effort-baselines.json`)")
    L.append("en alle klantworkspaces verwijzen op code. **Nieuwe nummers** (candidates) worden pas")
    L.append("echte template-codes na menselijke goedkeuring via `/review-system`; tot dan moeten ze")
    L.append("in `system/reviews/register.md` geflagd staan (afgedwongen door `catalog.py check`).")
    L.append("")
    if candidates or retired:
        L.append("| Code | Scenario | Status | Notities |")
        L.append("|---|---|---|---|")
        for s in candidates + retired:
            L.append(f"| `{s['code']}` | {s.get('title', '?')} | {s['status']} | {s.get('notes', '')} |")
    else:
        L.append("Geen — template en catalogus dekken elkaar volledig.")
    L.append("")

    L.append("## D. Veelgebruikte add-on-scenario's (≥ 2 echte gebruiken)")
    L.append("")
    if frequent_addon:
        L.append("| Code | Scenario | Add-on | Bewijs |")
        L.append("|---|---|---|---|")
        for s in frequent_addon:
            L.append(f"| `{s['code']}` | {s['title']} | {s['addon']} | {len(real_evidence(s))}× |")
    else:
        L.append("Nog geen — verschijnt zodra ≥ 2 echte klanten hetzelfde add-on-scenario gebruiken.")
    L.append("")

    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"rapport geschreven: {REPORT.relative_to(REPO)}")
    print(f"  {len(unverified)} zonder bewijs · {len(stale)} stale · "
          f"{len(candidates)} kandidaten · {len(retired)} retired")
    return 0


# ------------------------------------------------------------------ check
def check() -> int:
    problems: list[str] = []
    warnings: list[str] = []
    if not CATALOG.exists():
        print("catalogus ontbreekt — draai: python3 tools/catalog.py seed", file=sys.stderr)
        return 1
    try:
        cat = json.loads(CATALOG.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"catalog.json ongeldig: {e}", file=sys.stderr)
        return 1
    template = json.loads(TEMPLATE_CATALOG.read_text(encoding="utf-8"))
    tpl_codes = {s["code"] for s in template["scenarios"]}
    seen = set()
    valid_status = {"unverified", "verified", "stale", "candidate", "retired"}
    candidates: list[str] = []
    for s in cat.get("scenarios", []):
        code = s.get("code", "?")
        if code in seen:
            problems.append(f"dubbele code: {code}")
        seen.add(code)
        if s.get("status") not in valid_status:
            problems.append(f"{code}: ongeldige status {s.get('status')!r}")
        if not isinstance(s.get("evidence"), list) or not s["evidence"]:
            problems.append(f"{code}: evidence ontbreekt")
        if s.get("status") == "verified" and not s.get("last_verified"):
            problems.append(f"{code}: verified zonder last_verified")
        if s.get("status") == "verified" and s.get("doc_url_level") != "specific":
            problems.append(f"{code}: verified maar zonder specifieke documentatie-URL "
                            "(verificatie vereist een geraadpleegde bron)")
        # numbering invariant: template numbering is the master (cost model keys on it)
        if s.get("in_template") and code not in tpl_codes:
            problems.append(f"{code}: in_template maar bestaat niet in de template-catalogus — "
                            "nummering mag nooit afwijken van de template (kostenmodel!)")
        if not s.get("in_template") and code in tpl_codes:
            problems.append(f"{code}: in_template=false maar het nummer bestaat in de template — "
                            "hergebruik van template-nummers is verboden")
        if s.get("status") == "candidate":
            candidates.append(code)
    # every new (candidate) number must be flagged for human review
    if candidates:
        register = (REPO / "system" / "reviews" / "register.md")
        reg_text = register.read_text(encoding="utf-8") if register.exists() else ""
        for code in candidates:
            if code not in reg_text:
                problems.append(f"{code}: candidate (nieuw nummer) maar niet geregistreerd voor "
                                "review in system/reviews/register.md — nieuwe nummers raken het "
                                "kostenmodel en vereisen menselijke goedkeuring")
    # cost model sanity: specific codes in the baselines must exist in the template
    baselines = REPO / "pricing" / "effort-baselines.json"
    if baselines.exists():
        try:
            fit = json.loads(baselines.read_text(encoding="utf-8")).get("fit_days", {})
            for key in fit:
                if key == "default":
                    continue
                if "." in key and key not in tpl_codes:
                    warnings.append(f"kostenmodel: {key} staat in effort-baselines.json maar niet "
                                    "in de template-catalogus")
                elif "." not in key and not any(c.startswith(key) for c in tpl_codes):
                    warnings.append(f"kostenmodel: prefix {key} matcht geen enkele template-code")
        except json.JSONDecodeError:
            warnings.append("pricing/effort-baselines.json is geen geldig JSON")
    if not REFRESH_LOG.exists():
        problems.append("bpa/catalog/refresh-log.md ontbreekt")
    for w in warnings:
        print(f"  ! {w}", file=sys.stderr)
    if problems:
        for p in problems[:20]:
            print(f"  ✗ {p}", file=sys.stderr)
        print(f"{len(problems)} probleem/problemen", file=sys.stderr)
        return 1
    n_url = sum(1 for s in cat.get("scenarios", []) if s.get("doc_url"))
    print(f"catalogus ok: {len(seen)} scenario's, versie {cat.get('version')}, "
          f"bijgewerkt {cat.get('updated')} · {n_url}/{len(seen)} met documentatie-URL")
    return 0


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "seed":
        return seed()
    if cmd == "reconcile":
        return reconcile()
    if cmd == "check":
        return check()
    print(__doc__.split("Usage:")[1].split("`seed`")[0], file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
