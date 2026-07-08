#!/usr/bin/env python3
"""Health check for a fresh clone — run first on any new machine or GitHub account.

    python3 tools/doctor.py

Proves the system is intact and functional after cloning: Python version, required
files, tool modules compile, the scenario catalog and process flows parse, the
Copilot copy is within its size limit, the skills are present, and the demo client
builds + validates cleanly. Pure Python stdlib — no packages, no Node, no network.
(Node/Playwright are only used by the maintainers to browser-verify the viewer; a
clone that only *uses* the system never needs them.)

Exit 0 = healthy (warnings allowed), 1 = something is broken.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OK, WARN, FAIL = [], [], []


def ok(m: str) -> None:
    OK.append(m); print(f"  ✓ {m}")


def warn(m: str) -> None:
    WARN.append(m); print(f"  ! {m}")


def fail(m: str) -> None:
    FAIL.append(m); print(f"  ✗ {m}")


def check_python() -> None:
    v = sys.version_info
    (ok if v >= (3, 8) else fail)(f"Python {v.major}.{v.minor}.{v.micro} (vereist: 3.8+)")


def check_paths() -> None:
    required = [
        "system/instructions.md", "CLAUDE.md", "README.md",
        "copilot-studio/agent-instructions.md",
        "bpa/template/catalog.json", "bpa/terminology/bc-terms.json",
        "bpa/viewer/template.html", "bpa/viewer/viewer.css", "bpa/viewer/viewer.js",
        "pricing/effort-baselines.json",
        "tools/build_bpa.py", "tools/build_manual.py", "tools/build_quote.py",
        "tools/check_client.py", "tools/split_bpa_template.py", "tools/metrics.py",
        "clients/_template", "system/reviews/register.md",
    ]
    missing = [p for p in required if not (REPO / p).exists()]
    if missing:
        for p in missing:
            fail(f"ontbreekt: {p}")
    else:
        ok(f"alle {len(required)} kernpaden aanwezig")


def check_tools_compile() -> None:
    import py_compile
    tools = sorted((REPO / "tools").glob("*.py"))
    broken = []
    for t in tools:
        try:
            py_compile.compile(str(t), doraise=True)
        except py_compile.PyCompileError as e:
            broken.append(f"{t.name}: {e}")
    if broken:
        for b in broken:
            fail(f"compileert niet — {b}")
    else:
        ok(f"alle {len(tools)} tools/*.py compileren")


def check_catalog() -> None:
    p = REPO / "bpa" / "template" / "catalog.json"
    if not p.exists():
        return
    try:
        cat = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(f"catalog.json ongeldig: {e}"); return
    n = len(cat.get("scenarios", []))
    (ok if n > 100 else warn)(f"catalog: {n} scenario's, {len(cat.get('domains', []))} domeinen")


def check_processes() -> None:
    procs = sorted((REPO / "bpa" / "processes").glob("*.process.json"))
    bad = []
    for f in procs:
        try:
            json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            bad.append(f"{f.name}: {e}")
    if bad:
        for b in bad:
            fail(f"processtroom ongeldig — {b}")
    else:
        ok(f"alle {len(procs)} standaard processtromen parsen")


def check_copilot_limit() -> None:
    p = REPO / "copilot-studio" / "agent-instructions.md"
    if not p.exists():
        return
    text = p.read_text(encoding="utf-8")
    m = re.search(r"<!-- BEGIN INSTRUCTIONS -->(.*)<!-- END INSTRUCTIONS -->", text, re.S)
    if not m:
        warn("Copilot-instructies: markers niet gevonden"); return
    n = len(m.group(1).strip())
    (ok if n <= 8000 else fail)(f"Copilot-instructies: {n}/8000 tekens")


def check_skills() -> None:
    skills = sorted((REPO / ".claude" / "skills").glob("*/SKILL.md")) \
        if (REPO / ".claude" / "skills").is_dir() else []
    names = [s.parent.name for s in skills]
    (ok if skills else warn)(f"skills: {len(skills)} aanwezig ({', '.join(names) or 'geen'})")


def check_demo() -> None:
    demo = REPO / "clients" / "_demo-bakkerij-florax"
    if not demo.is_dir():
        warn("demo-client afwezig — overgeslagen (fresh instance?)"); return
    r = subprocess.run([sys.executable, str(REPO / "tools" / "check_client.py"), str(demo)],
                       capture_output=True, text=True)
    if r.returncode == 0:
        ok("demo-client bouwt + valideert schoon (end-to-end rooktest)")
    else:
        tail = (r.stdout + r.stderr).strip().splitlines()[-3:]
        fail("demo-client check faalt: " + " | ".join(tail))


def check_privacy() -> None:
    """Warn (never fail) about real client folders before cloning outward."""
    real = [c.name for c in (REPO / "clients").iterdir()
            if c.is_dir() and c.name != "_template" and not c.name.startswith("_demo")]
    if real:
        warn(f"echte clientmappen aanwezig ({', '.join(real)}) — controleer/verwijder "
             f"vóór klonen naar een minder vertrouwd account (privacy)")
    else:
        ok("geen echte clientdata (alleen _template + demo) — veilig te klonen")


def main() -> int:
    print("doctor: health check van de ERP-methodologie\n")
    for fn in (check_python, check_paths, check_tools_compile, check_catalog,
               check_processes, check_copilot_limit, check_skills, check_demo,
               check_privacy):
        fn()
    print(f"\nresultaat: {len(OK)} ok, {len(WARN)} waarschuwing(en), {len(FAIL)} fout(en)")
    if FAIL:
        print("  ✗ kloon is NIET gezond — los bovenstaande fouten op")
        return 1
    print("  ✓ kloon is gezond en klaar voor gebruik")
    return 0


if __name__ == "__main__":
    sys.exit(main())
