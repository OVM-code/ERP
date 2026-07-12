# Sharing the Business Central edition

This folder builds the **shareable BC-only edition** of the ERP Setup Assistant:
the full working system (BC knowledge, Aptean overlay, platform files, Copilot
Studio kit, blank client/expertise templates) with **everything else stripped** —
no Odoo knowledge, no real client data, no real lessons learned, ever.

## How to publish an update

```bash
share/export-bc-edition.sh --push
```

Builds `build/bc-edition/` and pushes it as one commit to the distribution repo
(`OVM-code/erp-bc` by default; override with `BC_EDITION_REPO=<url>`). Run it
whenever the BC knowledge changed and you want recipients to get the update.
Without `--push` it only builds locally so you can inspect the result.

## Safety model (why this can't leak)

- **Allowlist, not blocklist**: the script copies only named paths. New folders
  in the main repo never ship unless explicitly added to the script.
- **Odoo guard**: after filtering, any case-insensitive `odoo` match anywhere in
  the output aborts the export.
- **Client-data guard**: only `clients/_template` ships; any other client folder
  or real `SDR-*` file aborts the export. `expertise/lessons-learned.md` and
  `system/update-check-log.md` are replaced by the pristine templates kept in
  `share/bc-edition/` — your real lessons and check history never leave.
- **Exact-match stripping**: Odoo mentions in shared platform files (README,
  instructions, intake template, Copilot instructions, extension guide) are
  removed by exact-string replacement. If a source file changes and a pattern
  stops matching, the export **fails loudly** instead of shipping the mention —
  update the replacement table in `export-bc-edition.sh` when that happens.

## Maintenance rules

- Edited `system/instructions.md`, `README.md`, the intake template, the Copilot
  instructions, or `docs/adding-an-erp-or-addon.md`? If your edit touches an
  Odoo mention, the next export will abort until you update the script's
  replacement table. That's by design.
- `share/bc-edition/README.md` is the *curated* README of the shared edition —
  when the main README changes materially, update it too.
- The distribution repo is **read-only for recipients**: they fork/copy it to
  work, and pull to receive updates. Don't hand out write access.
