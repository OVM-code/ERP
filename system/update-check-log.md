# Update check log

> Enforces the once-a-day freshness throttle in `system/instructions.md` (advisory
> workflow, step 3). Before checking official sources for a stack, the assistant looks
> here for a row dated today covering that stack; if found, it skips the check. Append
> new rows at the bottom — don't rewrite history, this log is itself an audit trail.

| Date | Stack checked | Sources consulted | Result | Files touched |
|---|---|---|---|---|
| <!-- example: 2026-07-06 --> | <!-- e.g. Business Central + Aptean Food & Beverage --> | <!-- e.g. Microsoft Learn "what's new" BC 2026 wave 2 --> | <!-- "no changes" or short summary --> | <!-- knowledge file paths, or "—" --> |
| 2026-07-10 | Business Central (Aptean/Continia: partner-gated, not checked) | Microsoft Learn: whatsnew-update-28-0 / 28-1 / 28-3 | SaaS current = v28 (2026 wave 1); latest update 28.3 (July 2026). Relevant to our scenarios: (1) requisition-worksheet & item-journal **approvals now standard** — touches BS30.202 argumentation in the purchasing/planning knowledge files; (2) employee **expense reports + Expense Agent** in public preview — future GAP-killer for expense processes; (3) **external storage for document attachments** GA — relevant to Document Capture sizing; (4) Payables Agent processes mailbox invoices — watch: overlaps Continia DC positioning. Follow-ups: weave (1) into purchasing/planning knowledge at next touch; demo client's fictional "BC24" stack strings are anachronistic for a 2026 project (cosmetic, deferred). | `system/stack-versions.md` |
