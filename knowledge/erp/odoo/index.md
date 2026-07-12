# Odoo — functional area index

> **Scope:** Odoo 19 Enterprise (Odoo Online, Odoo.sh or on-premise)
> Standard capabilities only — add-on overlays live in `knowledge/addons/`.
> Community edition differences are flagged inline per decision (**Community edition:** lines).
> Belgian localization (l10n_be) specifics are woven in where they change a decision —
> this knowledge base serves Belgian SME implementations.
> Odoo ships one major release per year (typically October): re-review these files after each release.

| Area | File | Covers |
|---|---|---|
| Cross-cutting foundations | [general-setup.md](general-setup.md) | Edition & hosting, company structure, module scope, customization policy, sequences, analytic plans, users & approvals, data migration, integrations |
| Finance | [finance.md](finance.md) | Belgian localization, MAR chart of accounts, journals, VAT & fiscal positions, Peppol e-invoicing, continental vs anglo-saxon, banking (CODA/SEPA), fixed assets, close |
| Sales | [sales.md](sales.md) | Customer master data, pricelists, quotation flow, invoicing policy, delivery methods, sales teams & CRM boundary, portal, returns |
| Purchasing | [purchasing.md](purchasing.md) | Vendor master data & pricelists, RFQ/PO flow, approvals, replenishment triggers, bill control & 3-way matching, OCR, landed costs, dropshipping |
| Inventory | [inventory.md](inventory.md) | Product design, costing methods per category, valuation, UoM, lot/serial tracking, routes & rules, reordering, counting |
| Warehouse | [warehouse.md](warehouse.md) | Warehouse & location design, inbound/outbound steps ladder, putaway & removal strategies, batch picking, barcode, transfers |
| Manufacturing | [manufacturing.md](manufacturing.md) | MO flow & complexity ladder, BoM design, work centers & work orders, consumption, MPS & planning, subcontracting, costing, quality, PLM |
| Projects & Service | [projects-service.md](projects-service.md) | Compact: scope decisions for Projects, service invoicing, timesheets, Helpdesk/Field Service/Planning |

**Reading order for a full implementation:** general-setup → finance → inventory →
sales/purchasing → warehouse → manufacturing → projects-service. The edition/hosting
choice, the fiscal localization package, costing methods and the analytic-plan
architecture constrain almost everything downstream — settle those first.

**Cross-ERP note:** area names deliberately mirror
[Business Central](../business-central/index.md) so options can be compared
decision-by-decision when a client (or acquisition target) weighs one system against
the other, or migrates between them.
