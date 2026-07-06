# Business Central — functional area index

> **Scope:** Microsoft Dynamics 365 Business Central (SaaS, current version)
> Standard capabilities only — add-on overlays live in `knowledge/addons/`.
> BC has two release waves per year (April & October): re-review these files after each wave.

| Area | File | Covers |
|---|---|---|
| Cross-cutting foundations | [general-setup.md](general-setup.md) | Company strategy, number series, dimensions, users & approvals, data migration, integrations |
| Finance | [finance.md](finance.md) | G/L setup, chart of accounts, all posting groups, VAT, currencies, banking & payments, fixed assets |
| Sales | [sales.md](sales.md) | Sales & receivables setup, customer master data, pricing, order flows, shipping, prepayments |
| Purchasing | [purchasing.md](purchasing.md) | Purchases & payables setup, vendor master data, requisition flows, approvals, over-receipt |
| Inventory | [inventory.md](inventory.md) | Costing methods, item design, UoM, item tracking, SKUs, replenishment, counting |
| Warehouse | [warehouse.md](warehouse.md) | Location design, warehouse complexity ladder, bins, document flows, transfers |
| Manufacturing | [manufacturing.md](manufacturing.md) | Assembly vs production, BOMs/routings, flushing, planning, subcontracting, costing |
| Projects & Service | [projects-service.md](projects-service.md) | Compact: scope decisions for Projects (jobs/WIP) and Service Management |

**Reading order for a full implementation:** general-setup → finance → inventory →
sales/purchasing → warehouse → manufacturing → projects-service. Posting-group and
dimension decisions constrain almost everything downstream.
