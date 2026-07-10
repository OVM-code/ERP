# Stack version registry

The knowledge base and every deliverable must state **which software version they
describe**. This file tracks the versions the system currently knows; each client
pins their own versions in `clients/<slug>/bpa/bpa-config.json` → `stack`.

## How versions are used

1. **Client configs pin versions.** Example:
   ```json
   "stack": {
     "bc": "BC24 (2024 wave 1), SaaS current",
     "aptean-fnb": "verify at kickoff",
     "continia-dc": "verify at kickoff"
   }
   ```
   Builds stamp the stack into the deliverable; "current" means *the version at the
   last freshness check*, so record the concrete version as soon as it is known.
2. **The freshness check (advisory workflow step 3) covers deliverable work too.**
   Before enriching BPA content, drafting an FGD/TGD, or writing manual chapters,
   check `system/update-check-log.md` for a today-entry for the client's stack; if
   none, check the official release notes ("what's new" on Microsoft Learn for BC,
   vendor portals for add-ons) for changes relevant to the domains in scope, then
   log it. SaaS clients are auto-upgraded twice a year — a BPA written in the spring
   wave may be delivered in the autumn wave.
3. **Version-dependent terminology and behaviour** get a note in
   `bpa/terminology/bc-terms.json` (terminology) or the knowledge file (behaviour),
   e.g. *Job → Project rename in BC24*.
4. **Manual chapters must cite the version** of the official documentation they are
   based on (`docs:` source line, see `docs/manual.md`).

## Currently tracked

| Product | Version(s) covered by knowledge/content | Last verified | Notes |
|---|---|---|---|
| Business Central | SaaS current = **v28, 2026 release wave 1** (updates 28.0–28.3, July 2026) | 2026-07-10 (`update-check-log.md`) | terminology follows BC24+ ("Project", "Demand Forecast"); wave-1-2026 items relevant to our scenarios: requisition-worksheet/item-journal approvals now standard, expense reports + Expense Agent in preview, external storage for document attachments GA |
| Aptean Food & Beverage ERP | current AppSource release | see `update-check-log.md` | partner-gated docs — verify module behaviour per client licence |
| Continia Document Capture / Document Output | current AppSource release | see `update-check-log.md` | |
| Cegeka 365 / EDI framework | per Cegeka release | — | internal product; verify with product team |

Maintenance: when a release note changes anything the knowledge base or a template
flow describes, make the small targeted edit, update `Last reviewed` stamps, and add
a row to `system/update-check-log.md` — same routine as knowledge freshness.
