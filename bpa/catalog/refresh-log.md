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
| <!-- example: 2026-01 --> | <!-- e.g. domains 2, 4, 10 (BC 2026 wave 1) --> | <!-- e.g. Microsoft Learn what's new; Aptean release notes --> | <!-- "no changes" or short summary --> | <!-- codes, or "—" --> |
| 2026-07 | domains 2, 4, 6, 10, 12, 15 (demo-client scope + planning) | Microsoft Learn (BC docs: sales, pricing, order promising, intercompany, approvals, recurring/prepayment, returns, items/SKU/variants/tracking, counting, blocking, purchases, Belgian VAT, cash flow, MPS/MRP); Continia docs + product pages (Document Capture, Document Output, Peppol) | 47 scenario's verified; 1 template challenge: BS95.002 EDI framework is geen standaard BC → REV-001 (open) | BS25.101/102/104/200–208/211–216/219/220/222/237/328 · BS50.100/101/102/104/115/200/201 · BS45.200 · BS30.200/201/202 + BC30.201.01/02, BC30.202.01 · BS65.009/111/200/204/255 + BC65.009.01 · BS65.253/254/256/257 · notes op BS95.002 (+subs) |
