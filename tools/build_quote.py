#!/usr/bin/env python3
"""Generate a quote annex from a client's BPA coverage × effort baselines.

Usage:
    python3 tools/build_quote.py clients/<slug> [--rate 950] [--strict]

Reads:  clients/<slug>/bpa/coverage.md (+ gaps.md for sizes, training/trajectory.md
        for module count, migration/migration-plan.md for entity count)
        pricing/effort-baselines.json
Writes: clients/<slug>/commercial/quote-annex.md

The annex IS the coverage matrix, priced — what the client signs equals what the
pipeline builds. Baselines are seeds until calibrated from actuals (see the
harvest skill); the annex prints the baseline version so nobody mistakes seed
numbers for measured ones.
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_bpa as bb

REPO = Path(__file__).resolve().parent.parent


def days_for(code: str, fit: str, table: dict) -> float:
    fit = "standard" if fit in (None, "none", "gap") else fit
    best = table.get("default", {})
    best_len = 0
    for prefix, row in table.items():
        if prefix != "default" and code.startswith(prefix) and len(prefix) > best_len and fit in row:
            best, best_len = row, len(prefix)
    return best.get(fit, table.get("default", {}).get(fit, 0.5))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("client")
    ap.add_argument("--rate", type=float, default=950.0, help="blended day rate (EUR)")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    client = Path(args.client).resolve()
    bl = json.loads((REPO / "pricing" / "effort-baselines.json").read_text(encoding="utf-8"))

    cov_path = client / "bpa" / "coverage.md"
    if not cov_path.exists():
        print("error: geen coverage.md — bouw eerst de BPA-scope", file=sys.stderr)
        return 1
    rows = [r for r in bb.parse_coverage(cov_path.read_text(encoding="utf-8")) if r["scope"]]

    # gap sizes from gaps.md (Inschatting: S/M/L)
    gap_sizes: dict[str, str] = {}
    gaps_path = client / "bpa" / "gaps.md"
    if gaps_path.exists():
        for m in re.finditer(r"^##\s+(GAP-\d+)(.*?)(?=^##\s|\Z)",
                             gaps_path.read_text(encoding="utf-8"), re.M | re.S):
            sm = re.search(r"Inschatting:\*\*\s*([SML])\b", m.group(2))
            gap_sizes[m.group(1)] = sm.group(1) if sm else "M"

    lines = []
    scen_days = 0.0
    domains = set()
    for r in rows:
        d = days_for(r["code"], r["fit"], bl["fit_days"])
        scen_days += d
        domains.add(r["domain"])
        lines.append((r["code"], r["title"], r["fit"] or "standard", d))

    gap_days = sum(bl["gap_days"].get(sz, bl["gap_days"]["M"]) for sz in gap_sizes.values())

    # module / entity counts
    modules = 0
    traj = client / "training" / "trajectory.md"
    if traj.exists():
        modules = len(re.findall(r"^\|\s*M\d+\s*\|", traj.read_text(encoding="utf-8"), re.M))
    entities = 0
    mig = client / "migration" / "migration-plan.md"
    if mig.exists():
        entities = len(re.findall(r"`entities/[\w\-]+\.md`", mig.read_text(encoding="utf-8")))

    sf, fx = bl["stage_factors"], bl["fixed_days"]
    analysis = fx["analysis_workshops_per_domain"] * len(domains)
    setup = scen_days * sf["setup_execution"]
    testing = scen_days * sf["testing_support"]
    training = modules * sf["training_per_module_days"]
    migration = entities * sf["migration_per_entity_days"]
    cutover = fx["cutover_support"]
    subtotal = analysis + scen_days + gap_days + setup + testing + training + migration + cutover
    pm = subtotal * sf["project_management"]
    total = subtotal + pm
    R = args.rate

    def row(label, days_, note=""):
        return f"| {label} | {days_:.1f} | € {days_ * R:,.0f} | {note} |".replace(",", " ")

    out = [
        f"# Quote annex — {client.name}",
        "",
        f"> Gegenereerd {datetime.date.today().isoformat()} uit de BPA-scopematrix × "
        f"effort-baselines **{bl['version']}** · dagtarief € {R:,.0f}".replace(",", " "),
        "> ⚠ Baselines zijn seeds tot ze gekalibreerd zijn met werkelijke uren — dit is een startpunt voor de offerte, geen offerte.",
        "",
        "## Samenvatting",
        "",
        "| Blok | Dagen | Bedrag | Toelichting |",
        "|---|---|---|---|",
        row("Analyse (workshops + BPA)", analysis, f"{len(domains)} domeinen"),
        row("Inrichting scenario's (specificatie in de BPA)", scen_days, f"{len(rows)} scenario's in scope"),
        row("Maatwerk (GAPs, FGD→TGD→build)", gap_days,
            ", ".join(f"{g}={s}" for g, s in sorted(gap_sizes.items())) or "geen"),
        row("Setup-uitvoering (incl. checkpoints)", setup, f"factor {sf['setup_execution']}"),
        row("Testbegeleiding (scripts + rondes + gate)", testing, f"factor {sf['testing_support']}"),
        row("Training", training, f"{modules} modules"),
        row("Migratiebegeleiding (workbooks + CP1–CP3)", migration, f"{entities} entiteiten, client-run"),
        row("Cutover-ondersteuning", cutover, ""),
        row("Projectleiding", pm, f"factor {sf['project_management']}"),
        f"| **Totaal** | **{total:.1f}** | **€ {total * R:,.0f}** | |".replace(",", " "),
        "",
        "## Detail per scenario",
        "",
        "| Code | Scenario | Invulling | Dagen |",
        "|---|---|---|---|",
    ]
    out += [f"| {c} | {t} | {f} | {d:.1f} |" for c, t, f, d in lines]
    out += ["", "> Buiten scope: zie de scopematrix in de BPA — wat daar niet in staat, zit niet in dit budget. Wijzigingen lopen via het CR-register."]

    dest = client / "commercial" / "quote-annex.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Quote annex: {dest}")
    print(f"  {len(rows)} scenario's · {len(gap_sizes)} gaps · {total:.1f} dagen · € {total * R:,.0f}".replace(",", " "))
    if bb.WARNINGS and args.strict:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
