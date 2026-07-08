# Catalog refresh log

> Enforces the **once-a-month** freshness throttle for the Business Process
> Catalog (`bpa/catalog/catalog.json`). Before refreshing, look here for a row
> covering the **current month**; if found, skip the refresh. This is deliberately
> decoupled from the per-client daily check in `system/update-check-log.md`: the
> catalog is a standing asset, not client work. Append rows at the bottom — this
> log is an audit trail, never rewrite it.
>
> Refresh = `/catalog-refresh` skill: sync structure (`tools/catalog.py seed`),
> verify entries against official sources, update statuses/evidence, regenerate
> the reconciliation report, draft template changes for human review.

| Month | Scope checked | Sources consulted | Result | Entries touched |
|---|---|---|---|---|
| <!-- example: 2026-07 --> | <!-- e.g. domains 2, 4, 10 (BC 2026 wave 1) --> | <!-- e.g. Microsoft Learn what's new; Aptean release notes --> | <!-- "no changes" or short summary --> | <!-- codes, or "—" --> |
