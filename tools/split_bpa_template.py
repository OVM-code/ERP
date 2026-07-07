#!/usr/bin/env python3
"""Split the Cegeka BPA template into per-domain files and build the scenario catalog.

Reads  : bpa/template/source-cegeka-process-model-3.01.md  (verbatim import of the
         Cegeka Process Model template)
Writes : bpa/template/domains/NN-<slug>.md   one file per top-level domain (## heading)
         bpa/template/catalog.json           machine-readable index of every domain and
                                             business scenario (BS/BC code), used by the
                                             BPA workflow and tools/build_bpa.py

Re-run this script whenever a new version of the template is imported. It is tolerant
of the known formatting quirks in the source document (codes written as "BS 95.002",
scenario titles appearing as bullets or inline paragraphs instead of headings).
"""

import json
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / "bpa" / "template" / "source-cegeka-process-model-3.01.md"
DOMAINS_DIR = REPO / "bpa" / "template" / "domains"
CATALOG = REPO / "bpa" / "template" / "catalog.json"

# BS/BC scenario codes: "BS25.202", "BS 95.002", "BC95.002.01", "BC 50.242.03", "BC70.24801"
CODE_RE = re.compile(r"\bB[SC]\s?\d{2}\.\d{3}(?:\.\d{2})?\b|\bBC\d{2}\.\d{5}\b")
HEADING_RE = re.compile(r"^(#{2,5})\s+(.*)$")
# malformed scenario line: "12.1.1BS 95.002 EDI framework ..." (no heading marker)
INLINE_SCENARIO_RE = re.compile(r"^(\d+(?:\.\d+){1,3})\s*(B[SC]\s?\d{2}\.\d{3}(?:\.\d{2})?)\s+(.+)$")
SECTION_NO_RE = re.compile(r"^(\d+(?:\.\d+){0,3})\.?\s+(.*)$")

# Domains that are entirely add-on chapters (matched on domain title, lowercased substring).
DOMAIN_ADDONS = {
    "cegeka 365": "cegeka-365",
    "progressus": "progressus",
    "dynaway": "dynaway",
    "continia": "continia",
}
# Inline add-on tags that appear in scenario titles.
TITLE_ADDONS = {
    "aptean": "aptean",
    "progressus": "progressus",
    "tasklet": "tasklet",
    "continia": "continia",
    "dynaway": "dynaway",
    "(dc)": "continia",
}


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text or "domain"


def normalize_code(raw: str) -> str:
    return raw.replace(" ", "")


def detect_addon(title: str, domain_title: str, in_tasklet: bool) -> str | None:
    lt = title.lower()
    for needle, addon in TITLE_ADDONS.items():
        if needle in lt:
            return addon
    ld = domain_title.lower()
    for needle, addon in DOMAIN_ADDONS.items():
        if needle in ld:
            return addon
    if in_tasklet:
        return "tasklet"
    return None


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    lines = text.splitlines()

    # The table of contents at the top also contains "## Inhoudsopgave"; the real body
    # starts at "## Inleiding". Everything before that is preamble (kept in 00-preamble).
    domains: list[dict] = []
    scenarios: list[dict] = []
    current = {"number": 0, "title": "Voorblad & inhoudsopgave", "lines": []}
    chunks = [current]
    body_started = False

    for line in lines:
        m = HEADING_RE.match(line)
        if m and m.group(1) == "##":
            title = m.group(2).strip()
            if title.lower().startswith("inleiding"):
                body_started = True
            if body_started:
                num_m = re.match(r"^(\d+)\.\s*(.*)$", title)
                number = int(num_m.group(1)) if num_m else 0
                clean_title = num_m.group(2).strip() if num_m else title
                current = {"number": number, "title": clean_title, "lines": [line]}
                chunks.append(current)
                continue
        current["lines"].append(line)

    DOMAINS_DIR.mkdir(parents=True, exist_ok=True)
    for old in DOMAINS_DIR.glob("*.md"):
        old.unlink()

    seen_files: set[str] = set()
    for chunk in chunks:
        number, title = chunk["number"], chunk["title"]
        fname = f"{number:02d}-{slugify(title)}.md"
        if fname in seen_files:  # duplicate domain numbers should not happen, but be safe
            fname = f"{number:02d}-{slugify(title)}-2.md"
        seen_files.add(fname)
        body = "\n".join(chunk["lines"]).strip() + "\n"
        (DOMAINS_DIR / fname).write_text(body, encoding="utf-8")
        domains.append({"number": number, "title": title, "file": f"domains/{fname}"})

        if number == 0:  # cover page / TOC / Inleiding: no scenario definitions here
            continue

        # -- scan chunk for scenarios --------------------------------------------------
        in_tasklet = False
        seen_codes: set[str] = set()
        for line in chunk["lines"]:
            hm = HEADING_RE.match(line)
            raw_title = None
            if hm and len(hm.group(1)) >= 3:
                raw_title = hm.group(2).strip()
            else:
                im = INLINE_SCENARIO_RE.match(line.strip())
                if im:
                    raw_title = f"{im.group(1)} {im.group(2)} {im.group(3)}"
                elif line.strip().startswith("- ") and CODE_RE.search(line):
                    cand = line.strip()[2:].strip()
                    if CODE_RE.match(cand):
                        raw_title = cand
            if raw_title is None:
                continue
            if hm and "tasklet" in raw_title.lower():
                in_tasklet = True
            elif hm and len(hm.group(1)) == 3:  # new ### section resets tasklet scope
                in_tasklet = "tasklet" in raw_title.lower()

            code_m = CODE_RE.search(raw_title)
            if not code_m:
                continue
            code = normalize_code(code_m.group(0))
            # strip leading section number and the code itself from the title
            title_part = raw_title
            sec_m = SECTION_NO_RE.match(title_part)
            section = None
            if sec_m and re.match(r"^\d+(\.\d+)+", sec_m.group(1)):
                section = sec_m.group(1)
                title_part = sec_m.group(2)
            title_part = CODE_RE.sub("", title_part).strip(" -–:")
            title_part = re.sub(r"\s{2,}", " ", title_part).strip()
            # strip Word review-comment artifacts that leaked into the source export
            title_part = re.sub(r"\s*Commented \[.*$", "", title_part).strip()
            # inline malformed lines carry trailing prose; cut at first sentence if long
            if len(title_part) > 90:
                title_part = title_part[:90].rsplit(" ", 1)[0] + "…"
            if code in seen_codes:  # keep the first (defining) occurrence per domain
                continue
            seen_codes.add(code)
            scenarios.append(
                {
                    "code": code,
                    "title": title_part,
                    "section": section,
                    "domain": number,
                    "domainTitle": title,
                    "addon": detect_addon(raw_title, title, in_tasklet),
                }
            )

    catalog = {
        "source": SOURCE.name,
        "model": "Cegeka Process Model 3.01",
        "domains": domains,
        "scenarios": scenarios,
    }
    CATALOG.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    uniq = len({s["code"] for s in scenarios})
    print(f"{len(domains)} domains -> {DOMAINS_DIR}")
    print(f"{len(scenarios)} scenario entries ({uniq} unique codes) -> {CATALOG}")


if __name__ == "__main__":
    sys.exit(main())
