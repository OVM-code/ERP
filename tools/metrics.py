#!/usr/bin/env python3
"""Pipeline telemetry from what already exists: git history + persisted check logs.

Usage:
    python3 tools/metrics.py clients/<slug>        # one client
    python3 tools/metrics.py --all                 # every client folder

Reports per stage workspace (bpa, setup, gaps, migration, test, training, manual,
aftercare, commercial):
  - cycle time: days between first and last commit touching the workspace
  - activity: number of commits
  - last check_client result (from clients/<slug>/checks.log.jsonl, written by
    check_client --log)

These are the "stage cycle time" and "validator failure rate" KPIs from
docs/operations.md; estimate accuracy and reuse ratio come from the harvest skill
and pack attribution lines respectively. Stdlib only.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STAGES = ["bpa", "setup", "gaps", "migration", "test", "training", "manual",
          "aftercare", "commercial", "decisions"]


def git_dates(path: Path) -> list[str]:
    r = subprocess.run(["git", "log", "--format=%aI", "--", str(path)],
                       capture_output=True, text=True, cwd=REPO)
    return [l for l in r.stdout.splitlines() if l]


def client_metrics(client: Path) -> None:
    print(f"\n== {client.name} ==")
    print(f"{'stage':<12}{'commits':>8}{'first':>12}{'last':>12}{'cycle(d)':>10}")
    for st in STAGES:
        p = client / st
        if not p.exists():
            continue
        dates = git_dates(p)
        if not dates:
            print(f"{st:<12}{'0':>8}{'—':>12}{'—':>12}{'—':>10}")
            continue
        first, last = datetime.fromisoformat(dates[-1]), datetime.fromisoformat(dates[0])
        print(f"{st:<12}{len(dates):>8}{first.date().isoformat():>12}"
              f"{last.date().isoformat():>12}{(last - first).days:>10}")
    log = client / "checks.log.jsonl"
    if log.exists():
        runs = [json.loads(l) for l in log.read_text(encoding="utf-8").splitlines() if l.strip()]
        if runs:
            latest = runs[-1]
            fails = sum(1 for r in runs if r.get("errors", 0) > 0)
            print(f"checks: {len(runs)} run(s) · laatste: {latest.get('date')} "
                  f"({latest.get('errors')} fouten, {latest.get('warnings')} warn) · "
                  f"{fails} run(s) met fouten")
    else:
        print("checks: geen log — draai check_client met --log om validatorhistoriek op te bouwen")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("client", nargs="?", help="clients/<slug>")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    if args.all:
        for c in sorted((REPO / "clients").iterdir()):
            if c.is_dir() and not c.name.startswith("_template"):
                client_metrics(c)
    elif args.client:
        client_metrics(Path(args.client).resolve())
    else:
        ap.print_help()
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
