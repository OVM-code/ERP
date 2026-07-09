#!/usr/bin/env python3
"""Cross-system quality gate for one client workspace.

Usage:
    python3 tools/check_client.py clients/<client-slug> [--strict]

Checks every pipeline stage that exists for the client:
  gates      uniform human gates between every pipeline step (docs/gates.md):
             requirements -> coverage -> BPA sign-off -> setup -> migration/test
             -> training/manual -> aftercare; approved output only, no approval
             with open directives
  BPA        build warnings (dry-run), via tools/build_bpa.py
  gaps/      FGD/TGD status gates: TGD requires its FGD approved; every BPA GAP
             has an FGD; TGD test plan covers all FGD acceptance criteria
  setup/     every in-scope BPA scenario appears in the setup plan or is
             explicitly deferred; codes exist in the catalog
  training/  session preps only reference in-scope scenarios
  manual/    build warnings (dry-run) + count of topics flagged 'review'
  language   English clients: no leftover Dutch glossary terms in client content

Exit codes: 0 ok · 1 errors · 2 only warnings (with --strict).
`python3 tools/check_client.py` is the definition of done for every stage — run it
after each authoring step and before every delivery.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_bpa as bb

REPO = Path(__file__).resolve().parent.parent
ERRORS: list[str] = []
WARNS: list[str] = []


def err(m: str) -> None:
    ERRORS.append(m)
    print(f"  ✗ {m}")


def warn(m: str) -> None:
    WARNS.append(m)
    print(f"  ! {m}")


def ok(m: str) -> None:
    print(f"  ✓ {m}")


STATUS_RE = re.compile(r"\|\s*Status\s*\|\s*\**([a-zA-Z ]+?)\**\s*(?:<!--.*?-->)?\s*\|", re.I)


def doc_status(path: Path) -> str | None:
    m = STATUS_RE.search(path.read_text(encoding="utf-8"))
    return m.group(1).strip().lower() if m else None


def gate_info(path: Path) -> tuple[str | None, int]:
    """(status, open directives) of a gated artifact. Status comes from the
    first `| Status | … |` row; open directives are unchecked `- [ ]` items in
    the `## Gate` section. Missing file -> (None, 0)."""
    if not path.exists():
        return None, 0
    text = path.read_text(encoding="utf-8")
    st = doc_status(path)
    m = re.search(r"^##+\s+Gate\b(.*?)(?=^##\s|\Z)", text, re.M | re.S)
    open_d = len(re.findall(r"^\s*-\s*\[ \]", m.group(1), re.M)) if m else 0
    return st, open_d


def run_build(script: str, client: Path, label: str) -> None:
    r = subprocess.run([sys.executable, str(REPO / "tools" / script), str(client),
                        "--dry-run", "--strict"], capture_output=True, text=True)
    tail = (r.stdout + r.stderr).strip().splitlines()
    if r.returncode == 0:
        ok(f"{label}: geen waarschuwingen")
    else:
        for line in tail:
            if line.strip().startswith("!"):
                warn(f"{label}: {line.strip().lstrip('! ')}")
        if r.returncode not in (0, 2):
            err(f"{label}: build faalt — {tail[-1] if tail else r.returncode}")


def bpa_scope(client: Path) -> tuple[set[str], set[str]]:
    """(in-scope codes, gap ids) from the client's BPA workspace."""
    codes: set[str] = set()
    gap_ids: set[str] = set()
    bpa = client / "bpa"
    cov = bpa / "coverage.md"
    if cov.exists():
        for row in bb.parse_coverage(cov.read_text(encoding="utf-8")):
            if row["scope"]:
                codes.add(row["code"])
    content = bpa / "content"
    head = re.compile(r"^(B[SC]\d{2}\.\d{3}(?:\.\d{2})?|BC\d{2}\.\d{5})\s*[-–—:]?\s*(.*)$")
    if content.is_dir():
        for f in content.glob("*.md"):
            _, blocks = bb.split_blocks(f.read_text(encoding="utf-8"), head)
            codes.update(b["key"] for b in blocks)
    gaps = bpa / "gaps.md"
    if gaps.exists():
        gap_ids = set(re.findall(r"^##\s+(GAP-\d+)", gaps.read_text(encoding="utf-8"), re.M))
    return codes, gap_ids


def check_gates(client: Path) -> None:
    """Uniform human gates between pipeline steps: the output of step N must be
    APPROVED (gate block: Status + Directieven) before step N+1's artifacts may
    exist. Approving with open directives is impossible. Guide: docs/gates.md."""
    bpa = client / "bpa"
    if not bpa.is_dir():
        return
    carriers = {
        "requirements": bpa / "requirements.md",
        "coverage": bpa / "coverage.md",
        "bpa": bpa / "approval.md",
        "setup": client / "setup" / "setup-plan.md",
        "migration": client / "migration" / "migration-plan.md",
        "test": client / "test" / "test-plan.md",
        "training": client / "training" / "trajectory.md",
        "manual": client / "manual" / "approval.md",
    }
    g = {name: gate_info(p) for name, p in carriers.items()}

    # approving with open directives is a contradiction
    for name, (st, od) in g.items():
        if st == "approved" and od:
            err(f"gate '{name}': status approved maar {od} open directief/directieven — "
                f"eerst toepassen/afvinken, dan goedkeuren")

    # carriers that exist but have no parseable gate status
    for name, p in carriers.items():
        if p.exists() and g[name][0] is None:
            warn(f"gate '{name}': {p.relative_to(client)} heeft geen gate-blok/Status — geldt als draft")

    def require(prereq: str, what: str) -> None:
        st = g[prereq][0]
        if st != "approved":
            err(f"gate: {what}, maar gate '{prereq}' is niet approved (status: {st or 'ontbreekt'})")

    # step N+1 artifacts present => gate N approved
    has_reqs = carriers["requirements"].exists() and \
        re.search(r"^##\s+REQ-\d+", carriers["requirements"].read_text(encoding="utf-8"), re.M)
    cov_rows = bb.parse_coverage(carriers["coverage"].read_text(encoding="utf-8")) \
        if carriers["coverage"].exists() else []
    content_files = [f for f in (bpa / "content").glob("*.md")] if (bpa / "content").is_dir() else []
    if has_reqs and cov_rows:
        require("requirements", "coverage.md bevat scope-rijen")
    if cov_rows and content_files:
        require("coverage", "content/ bevat scenariodocumentatie")
    if carriers["setup"].exists():
        require("bpa", "setup/setup-plan.md bestaat")
    if (client / "gaps").is_dir() and list((client / "gaps").glob("FGD-GAP-*.md")):
        require("bpa", "gaps/ bevat FGD's")
    if carriers["migration"].exists():
        require("setup", "migration/ is gestart")
    if carriers["test"].exists():
        require("setup", "test/ is gestart")
    if carriers["training"].exists():
        require("test", "training/ is gestart")
    chapters = [f for f in (client / "manual" / "chapters").glob("*.md")
                if f.name.lower() != "readme.md"] if (client / "manual" / "chapters").is_dir() else []
    if chapters:
        require("test", "manual/chapters/ bevat hoofdstukken")
    aftercare_live = False
    for name in ("issues.md", "crs.md"):
        p = client / "aftercare" / name
        if p.exists() and re.search(r"^##\s+(ISS|CR)-\d+", p.read_text(encoding="utf-8"), re.M):
            aftercare_live = True
    if aftercare_live:
        require("manual", "aftercare/ bevat registraties")

    line = " · ".join(f"{n}={st or '—'}" + (f" ({od} open)" if od else "")
                      for n, (st, od) in g.items() if carriers[n].exists())
    total_open = sum(od for _, od in g.values())
    if line:
        ok(f"gates: {line}" + (f" — {total_open} open directief/directieven" if total_open else ""))


def check_designs(client: Path, gap_ids: set[str]) -> None:
    gdir = client / "gaps"
    if not gdir.is_dir():
        if gap_ids:
            warn(f"gaps: {len(gap_ids)} GAP(s) in de BPA maar geen gaps/-map (nog geen FGD's)")
        return
    fgd_status: dict[str, str] = {}
    for f in sorted(gdir.glob("FGD-GAP-*.md")):
        gid = f.stem.replace("FGD-", "")
        st = doc_status(f)
        if st not in ("draft", "in review", "approved", "rejected"):
            err(f"{f.name}: Status ontbreekt of is geen geldig token (draft/in review/approved/rejected): {st!r}")
            st = "draft"
        fgd_status[gid] = st
        if gid not in gap_ids:
            warn(f"{f.name}: {gid} staat niet (meer) in de BPA gap register")
    for gid in sorted(gap_ids - set(fgd_status)):
        warn(f"gaps: {gid} heeft nog geen FGD")
    for f in sorted(gdir.glob("TGD-GAP-*.md")):
        gid = f.stem.replace("TGD-", "")
        st = fgd_status.get(gid)
        if st != "approved":
            err(f"{f.name}: TGD vereist een goedgekeurde FGD-{gid} (status is {st!r}) — menselijke reviewpoort")
            continue
        # acceptance-criteria coverage
        fgd_text = (gdir / f"FGD-{gid}.md").read_text(encoding="utf-8")
        acs = set(re.findall(r"\bAC-\d+\b", fgd_text))
        tgd_text = f.read_text(encoding="utf-8")
        missing = sorted(a for a in acs if a not in tgd_text)
        if missing:
            warn(f"{f.name}: testplan dekt FGD-criteria niet: {', '.join(missing)}")
        tst = doc_status(f)
        if tst not in ("draft", "in review", "approved"):
            err(f"{f.name}: Status ontbreekt of ongeldig: {tst!r}")
    # AL scaffolds only from approved TGDs (human gate #3)
    al_dir = gdir / "al"
    if al_dir.is_dir():
        for d in sorted(p for p in al_dir.iterdir() if p.is_dir()):
            tgd = gdir / f"TGD-{d.name}.md"
            tst = doc_status(tgd) if tgd.exists() else None
            if tst != "approved":
                err(f"gaps/al/{d.name}: scaffold vereist een goedgekeurde TGD-{d.name} (status {tst!r})")
            else:
                ok(f"gaps/al/{d.name}: scaffold met goedgekeurde TGD")
    if fgd_status:
        ok(f"gaps: {len(fgd_status)} FGD(s) — statussen {dict(sorted(fgd_status.items()))}")


def check_setup(client: Path, in_scope: set[str]) -> None:
    plan = client / "setup" / "setup-plan.md"
    if not plan.exists():
        return
    text = plan.read_text(encoding="utf-8")
    codes_in_plan = set(bb.CODE_RE.findall(text))
    catalog = json.loads(bb.CATALOG_PATH.read_text(encoding="utf-8"))
    cat_codes = {s["code"] for s in catalog["scenarios"]}
    missing = sorted(in_scope - codes_in_plan)
    if missing:
        err(f"setup-plan: in-scope scenario's ontbreken (fase of 'Uitgesteld'): {', '.join(missing)}")
    unknown = sorted(c for c in codes_in_plan if c not in cat_codes)
    if unknown:
        warn(f"setup-plan: onbekende codes: {', '.join(unknown)}")
    st = doc_status(plan)
    if st == "approved" and ("TBD" in text or "<bv." in text):
        warn("setup-plan: status approved maar bevat nog TBD/placeholderteksten")
    if not missing:
        ok(f"setup-plan: dekt alle {len(in_scope)} in-scope scenario's (status: {st})")


def check_training(client: Path, in_scope: set[str]) -> None:
    tdir = client / "training"
    if not tdir.is_dir():
        return
    n = 0
    for f in sorted((tdir / "sessions").glob("S*.md")) if (tdir / "sessions").is_dir() else []:
        if f.stem.startswith("S00"):
            continue
        n += 1
        for code in set(bb.CODE_RE.findall(f.read_text(encoding="utf-8"))):
            if code not in in_scope:
                warn(f"training/{f.name}: {code} is niet in scope van de BPA")
    traj = tdir / "trajectory.md"
    if traj.exists():
        for code in set(bb.CODE_RE.findall(traj.read_text(encoding="utf-8"))):
            if code not in in_scope:
                warn(f"training/trajectory.md: {code} is niet in scope van de BPA")
        ok(f"training: trajectory + {n} sessievoorbereiding(en) gecontroleerd")


def check_test(client: Path, in_scope: set[str]) -> None:
    tdir = client / "test"
    if not tdir.is_dir():
        return
    scripts_dir = tdir / "scripts"
    text_all = ""
    n_scripts = 0
    covered: set[str] = set()
    for f in sorted(scripts_dir.glob("*.md")) if scripts_dir.is_dir() else []:
        if f.name.lower() == "readme.md":
            continue
        t = f.read_text(encoding="utf-8")
        text_all += t
        n_scripts += len(re.findall(r"^##\s+TS-", t, re.M))
        for code in bb.CODE_RE.findall(t):
            covered.add(code)
            if code not in in_scope:
                warn(f"test/{f.name}: {code} is niet in scope van de BPA")
    missing = sorted(in_scope - covered)
    plan = tdir / "test-plan.md"
    st = doc_status(plan) if plan.exists() else None
    if missing:
        (err if st == "approved" else warn)(
            f"test: in-scope scenario's zonder testscript: {', '.join(missing)}")
    # every approved FGD's acceptance criteria must be referenced by a script
    for f in sorted((client / "gaps").glob("FGD-GAP-*.md")) if (client / "gaps").is_dir() else []:
        if doc_status(f) != "approved":
            continue
        for ac in sorted(set(re.findall(r"\bAC-\d+\b", f.read_text(encoding="utf-8")))):
            if ac not in text_all:
                warn(f"test: {f.stem} {ac} wordt door geen enkel script gedekt")
    # open high-severity defects block an approved plan
    defects = tdir / "defects.md"
    if defects.exists() and st == "approved":
        dt = defects.read_text(encoding="utf-8")
        for m in re.finditer(r"^##\s+(DEF-\d+)(.*?)(?=^##\s|\Z)", dt, re.M | re.S):
            block = m.group(2)
            if re.search(r"Severity:\*\*\s*hoog", block) and re.search(r"Status:\*\*\s*open", block):
                err(f"test: {m.group(1)} (severity hoog) staat open terwijl het testplan approved is")
    if not missing and n_scripts:
        ok(f"test: {n_scripts} script(s) dekken alle {len(in_scope)} in-scope scenario's (plan: {st})")


def check_migration(client: Path) -> None:
    mdir = client / "migration"
    plan = mdir / "migration-plan.md"
    if not plan.exists():
        return
    text = plan.read_text(encoding="utf-8")
    n = 0
    for m in re.finditer(r"`entities/([\w\-]+\.md)`", text):
        n += 1
        wb = mdir / "entities" / m.group(1)
        if not wb.exists():
            err(f"migration: workbook entities/{m.group(1)} staat in het plan maar bestaat niet")
            continue
        wt = wb.read_text(encoding="utf-8")
        for section in ("Veldmapping", "Schoningsregels", "Validatiechecklist"):
            if section not in wt:
                warn(f"migration/entities/{m.group(1)}: sectie '{section}' ontbreekt")
    if n == 0:
        warn("migration: geen entiteiten met workbook-verwijzing in het plan")
    else:
        ok(f"migration: {n} entiteit(en) met workbook gecontroleerd (plan: {doc_status(plan)})")


def check_aftercare(client: Path) -> None:
    adir = client / "aftercare"
    if not adir.is_dir():
        return
    crs = adir / "crs.md"
    if crs.exists():
        t = crs.read_text(encoding="utf-8")
        for m in re.finditer(r"^##\s+(CR-\d+)(.*?)(?=^##\s|\Z)", t, re.M | re.S):
            cid, block = m.group(1), m.group(2)
            sm = re.search(r"Status:\*\*\s*([a-z ]+)", block)
            st = sm.group(1).strip() if sm else None
            if st not in ("requested", "quoted", "approved", "delivered", "rejected"):
                err(f"aftercare/crs.md: {cid} heeft geen geldig statustoken ({st!r})")
            if st == "delivered" and not re.search(r"BPA-versie na levering:\*\*\s*\S*\d", block):
                warn(f"aftercare/crs.md: {cid} is delivered maar zonder BPA-versiebump")
    issues = adir / "issues.md"
    if issues.exists():
        t = issues.read_text(encoding="utf-8")
        for m in re.finditer(r"^##\s+(ISS-\d+)(.*?)(?=^##\s|\Z)", t, re.M | re.S):
            iid, block = m.group(1), m.group(2)
            if re.search(r"Status:\*\*\s*(opgelost|gesloten)", block):
                if not (bb.CODE_RE.search(block) or "n.v.t." in block):
                    warn(f"aftercare/issues.md: {iid} is opgelost zonder scenario-/handleidingverwijzing (voedingsregel)")
    ok("aftercare: registers gecontroleerd")


def check_language(client: Path) -> None:
    """English deliverables must not contain Dutch glossary terms."""
    def lang_of(cfg_file: Path) -> str:
        try:
            return json.loads(cfg_file.read_text(encoding="utf-8-sig")).get("language", "nl")
        except Exception:
            return "nl"

    glossary = json.loads((REPO / "bpa" / "terminology" / "bc-terms.json").read_text(encoding="utf-8"))
    nl_terms = [t["nl"] for t in glossary["terms"]
                if t["nl"].lower() != t["en"].lower() and len(t["nl"]) >= 5 and " " not in t["nl"]]
    pattern = re.compile(r"\b(" + "|".join(map(re.escape, sorted(nl_terms, key=len, reverse=True))) + r")\b", re.I)

    targets = []
    if (client / "bpa" / "bpa-config.json").exists() and lang_of(client / "bpa" / "bpa-config.json") == "en":
        targets += list((client / "bpa" / "content").glob("*.md")) + \
                   [client / "bpa" / p for p in ("requirements.md", "intro.md", "gaps.md")]
    if (client / "manual" / "manual-config.json").exists() and lang_of(client / "manual" / "manual-config.json") == "en":
        targets += list((client / "manual" / "chapters").glob("*.md")) + [client / "manual" / "intro.md"]
    hits = 0
    for f in targets:
        if not f.exists():
            continue
        for m in pattern.finditer(f.read_text(encoding="utf-8")):
            hits += 1
            if hits <= 20:
                warn(f"terminologie: NL-term '{m.group(0)}' in {f.relative_to(client)} — gebruik de EN-term uit bc-terms.json")
    if targets and not hits:
        ok("terminologie: geen Nederlandse glossariumtermen in Engelse content")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("client")
    ap.add_argument("--strict", action="store_true", help="ook waarschuwingen doen falen (exit 2)")
    ap.add_argument("--log", action="store_true",
                    help="resultaat toevoegen aan clients/<slug>/checks.log.jsonl (telemetrie)")
    args = ap.parse_args()
    client = Path(args.client).resolve()
    if not client.is_dir():
        print(f"error: {client} bestaat niet", file=sys.stderr)
        return 1

    print(f"check_client: {client.name}")
    if (client / "bpa").is_dir():
        run_build("build_bpa.py", client, "BPA")
    if (client / "manual").is_dir():
        run_build("build_manual.py", client, "manual")
    in_scope, gap_ids = bpa_scope(client)
    check_gates(client)
    check_designs(client, gap_ids)
    check_setup(client, in_scope)
    check_test(client, in_scope)
    check_migration(client)
    check_training(client, in_scope)
    check_aftercare(client)
    check_language(client)

    print(f"resultaat: {len(ERRORS)} fout(en), {len(WARNS)} waarschuwing(en)")
    if args.log:
        import datetime
        entry = {"date": datetime.datetime.now().isoformat(timespec="seconds"),
                 "errors": len(ERRORS), "warnings": len(WARNS),
                 "detail": ERRORS + WARNS}
        with open(client / "checks.log.jsonl", "a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    if ERRORS:
        return 1
    if WARNS and args.strict:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
