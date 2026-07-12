#!/usr/bin/env bash
# Export the shareable Business Central edition of this repo.
#
#   share/export-bc-edition.sh [--push]
#
# Builds a filtered copy of the system in build/bc-edition/ containing ONLY:
#   - Business Central knowledge (+ Aptean F&B add-on overlay)
#   - the platform files (instructions, templates, docs, Copilot Studio kit)
#   - BLANK client/expertise structure (templates only)
# and strips every Odoo reference from the shared platform files.
#
# Hard guarantees, enforced below (the export FAILS LOUDLY rather than leak):
#   1. No Odoo content: any case-insensitive "odoo" match in the output aborts.
#   2. No client data: only clients/_template ships; any SDR or intake beyond
#      the templates aborts. expertise/lessons-learned.md and
#      system/update-check-log.md are replaced by pristine templates from
#      share/bc-edition/ — real lessons and check history never leave.
#
# --push publishes build/bc-edition to the distribution repo (append commit,
# recipients just `git pull`). The distribution repo is read-only for
# recipients; they fork/copy it to work.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/build/bc-edition"
REPO_URL="${BC_EDITION_REPO:-git@github.com:OVM-code/erp-bc.git}"

cd "$ROOT"
rm -rf "$OUT"
mkdir -p "$OUT"

# ---- 1. Copy the allowlist (never copy the repo root wholesale) ------------
tar cf - \
  CLAUDE.md \
  system/instructions.md \
  knowledge/erp/business-central \
  knowledge/addons/aptean-food-beverage \
  knowledge/_templates \
  clients/_template \
  expertise/README.md \
  copilot-studio \
  docs \
  | tar xf - -C "$OUT"

# ---- 2. Replace curated files with their BC-edition versions ---------------
cp share/bc-edition/README.md            "$OUT/README.md"
cp share/bc-edition/lessons-learned.md   "$OUT/expertise/lessons-learned.md"
cp share/bc-edition/update-check-log.md  "$OUT/system/update-check-log.md"

# ---- 3. Strip Odoo references from shared platform files -------------------
# Exact-match replacements: if the source text changed and a pattern no longer
# matches, the export aborts — update this table alongside the source files.
python3 - "$OUT" <<'PYEOF'
import sys, pathlib
out = pathlib.Path(sys.argv[1])

REPLACEMENTS = {
    "system/instructions.md": [
        ("(e.g. `business-central/`, `odoo/`)",
         "(e.g. `business-central/`)"),
        ("the Odoo release\n  notes / odoo.com documentation for Odoo, the vendor's release",
         "the vendor's release"),
    ],
    "copilot-studio/agent-instructions.md": [
        ("; Odoo\nrelease notes / odoo.com documentation for Odoo; the",
         "; the"),
    ],
    "clients/_template/intake.md": [
        ("| ERP system + version | <e.g. Business Central SaaS, current — or Odoo 19> |",
         "| ERP system + version | <e.g. Business Central SaaS, current> |"),
        ("| Edition & hosting (Odoo: decisive) | <e.g. Odoo Enterprise on Odoo.sh / Community on-premise; BC: SaaS vs on-prem> |",
         "| Edition & hosting | <e.g. SaaS vs on-premise> |"),
    ],
    "docs/adding-an-erp-or-addon.md": [
        ("The Business Central + Aptean content was the first instance; Odoo\n(`knowledge/erp/odoo/`) is the second. The same structure",
         "The Business Central + Aptean content is the first instance. The same structure"),
    ],
    # The share/ kit itself must not be visible in the shared edition:
    "CLAUDE.md": [
        ("- `share/` — export kit for the shareable BC-only edition (strips Odoo + client data;\n"
         "  distribution repo: `OVM-code/erp-bc`). If you edit a file the export filters\n"
         "  (README, instructions, intake template, Copilot instructions, extension guide),\n"
         "  the export may abort until its replacement table in `share/export-bc-edition.sh`\n"
         "  is updated — that is intentional leak protection.\n",
         ""),
    ],
    "docs/maintenance.md": [
        ("### 4. Per BC knowledge update you want to share (~1 min)\n"
         "If you distribute the Business Central edition (`share/README.md`), run\n"
         "`share/export-bc-edition.sh --push` after committing BC knowledge changes. The\n"
         "export is allowlisted and guarded — it refuses to ship Odoo content or client\n"
         "data. Recipients pull the update from the distribution repo.\n\n",
         ""),
    ],
}

for rel, pairs in REPLACEMENTS.items():
    p = out / rel
    text = p.read_text()
    for old, new in pairs:
        if old not in text:
            sys.exit(f"EXPORT ABORTED: pattern not found in {rel}:\n---\n{old}\n---\n"
                     "The source file changed — update share/export-bc-edition.sh.")
        text = text.replace(old, new)
    p.write_text(text)
print("replacements applied")
PYEOF

# ---- 4. Guards --------------------------------------------------------------
if grep -ril "odoo" "$OUT" >/dev/null 2>&1; then
  echo "EXPORT ABORTED: Odoo references remain in the output:" >&2
  grep -rin "odoo" "$OUT" >&2
  exit 1
fi
extra_clients=$(find "$OUT/clients" -mindepth 1 -maxdepth 1 ! -name '_template' | wc -l)
if [ "$extra_clients" -ne 0 ]; then
  echo "EXPORT ABORTED: client folders beyond _template in output." >&2
  exit 1
fi
if find "$OUT" -name 'SDR-*' ! -name 'SDR-000-template.md' | grep -q .; then
  echo "EXPORT ABORTED: real SDR files in output." >&2
  exit 1
fi

echo "BC edition built at: $OUT"

# ---- 5. Optional publish -----------------------------------------------------
if [ "${1:-}" = "--push" ]; then
  TMP="$(mktemp -d)"
  trap 'rm -rf "$TMP"' EXIT
  if git clone --depth 1 "$REPO_URL" "$TMP" 2>/dev/null; then
    :
  else
    git init -q -b main "$TMP"
    git -C "$TMP" remote add origin "$REPO_URL"
  fi
  # Base the new export on the remote's main regardless of the remote's HEAD;
  # start an orphan main only if the remote has no main yet (first export).
  if git -C "$TMP" fetch -q --depth 1 origin main 2>/dev/null; then
    git -C "$TMP" checkout -qB main FETCH_HEAD
  else
    git -C "$TMP" checkout -qB main
  fi
  find "$TMP" -mindepth 1 -maxdepth 1 ! -name '.git' -exec rm -rf {} +
  tar cf - -C "$OUT" . | tar xf - -C "$TMP"
  git -C "$TMP" add -A
  if git -C "$TMP" diff --cached --quiet; then
    echo "No changes since last export — nothing pushed."
  else
    git -C "$TMP" commit -qm "BC edition export $(date +%Y-%m-%d)"
    git -C "$TMP" push -u origin main
    echo "Pushed to $REPO_URL"
  fi
fi
