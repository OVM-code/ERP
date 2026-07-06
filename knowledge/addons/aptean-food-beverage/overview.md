# Aptean Food & Beverage ERP — Add-on Overview

> **Add-on:** Aptean Food & Beverage ERP (Business Central embedded)
> **Base ERP:** Microsoft Dynamics 365 Business Central
> **Last reviewed:** 2026-07

## What it is

Aptean Food & Beverage ERP is a food-industry vertical solution **embedded in Microsoft Dynamics 365 Business Central** — it is not an external system with an interface, but a set of Aptean extensions installed on top of a standard BC tenant. It descends from several long-standing BC/NAV food products that Aptean acquired and has been converging: **Foodware 365** (SI Foodware), **bcFood**, **JustFood**, **Drink-IT** (beverage) and **LINKFRESH** (fresh produce). On AppSource the BC-embedded product is published under the Foodware365 publisher; Aptean's own documentation portal (fnbdocs.apteancloud.com) documents the extensions as a family of modules with three-letter codes (LMT, CAW, QCL, PRM, TMT, LOG, …).

The practical consequence for an implementation: **everything standard BC does still applies** — finance, dimensions, posting groups, standard sales/purchase flows are untouched — and the Aptean layer adds food-specific behaviour on top: deeper lot control, expiry/shelf-life logic, catch weight, quality checks, process manufacturing, trade agreements/rebates, and delivery logistics.

## Which client profiles need it

| Profile | Why standard BC is not enough |
|---|---|
| Food manufacturers (bakery, dairy, prepared foods, ingredients) | Batch/recipe manufacturing with yield, co-products, allergens; BC's discrete BOM model fights the process reality |
| Meat, fish & protein processors | Catch weight (sell by kg, handle by box/carcass), carcass disassembly (one input, many outputs), heavy traceability |
| Fresh produce packers/traders | Grower settlements, harvest/commodity planning, short shelf life, FEFO, LINKFRESH-heritage functionality |
| Food & beverage distributors | Trade agreements/rebates/promotions, delivery routes and trips, SSCC/GS1 pallet labelling, mobile scanning |
| Beverage producers (Drink-IT heritage) | Promotions/conditions, empties/returnables, excise-adjacent flows |

Clients who are food-adjacent but don't need lot-level expiry control, catch weight or rebate settlement (e.g. a simple dry-goods wholesaler) can often run standard BC plus one or two small ISV apps — don't sell the full vertical reflexively. The Aptean layer earns its cost when **two or more** of the module areas below are genuinely needed.

## Module map (this knowledge layer)

| Module file | Aptean extensions covered | One-line description |
|---|---|---|
| [Lot management & traceability](lot-management-traceability.md) | Lot Management (LMT), Expiration Management (EXM) | Lot numbering profiles, lot attributes/quality data per lot, expiry & minimum-shelf-life logic, FEFO, farm-to-fork tracing and recall management |
| [Catch weight](catch-weight.md) | Catch Weight (CAW) | Dual unit of measure (units + actual weight) through purchase, inventory, production, sales and invoicing, with tolerances and scale capture |
| [Quality control](quality-control.md) | Quality Control (QCL) + Quality Control app (QCA), CoA reporting (REP) | Quality plans, triggered quality checks (inbound/production/outbound/recurring), holds/blocking, Certificates of Analysis |
| [Food manufacturing](food-manufacturing.md) | Process Manufacturing (PRM), Shop Floor Production app (SFP/SFPBC), OEE (APMOEE), Product Specifications (PRS) | Batch-size BOMs/recipes, yield & process weight change, co-/by-products with cost apportionment, unplanned output/consumption, shop-floor registration, allergen/spec management |
| [Trade & pricing](trade-and-pricing.md) | Trade Management (TMT), promotions/conditions (SPC), Commodity (COM) + Commodity Harvest Planning (CHP) + Contract Management, commissions (GRR) | Trade plans (price rules + accruals), rebates and trade statements, broker commissions/royalties, promotions, commodity/market & contract pricing |
| [Logistics & planning](logistics-and-planning.md) | Logistics (LOG), Transport (TRA), TMS integration, License Plating (LPL), SSCC (SSC), Mobile Warehouse (MWR), Advanced Warehouse Management (AWM) | Route planning worksheets, transport orders/trips, load handling, licence plates and SSCC/GS1 labelling, mobile scanning, forecasting extensions |

Modules ship as separate BC extensions on a common Aptean foundation layer; you can deploy a subset, but watch the documented integrations (e.g. Quality Control triggers from Shop Floor Production; Warehouse Management recording vendor lot numbers for Lot Management; AWM integration with Process Manufacturing and Production Cost Apportionment).

## Licensing / edition notes

- **Platform licensing is unchanged:** users still need Business Central licences (Essentials or Premium). Anything touching production orders — i.e. the food manufacturing module — requires **BC Premium** per standard Microsoft rules.
- The Aptean layer is **subscription-licensed via Aptean/its partner channel** on top of BC. The product includes a License & Subscription Management (LIM) extension in the tenant that tracks subscription status of the installed Aptean extensions.
- Editions: Aptean still markets edition names from the acquired products (bcFood Edition, Foodware 365 Edition, JustFood Edition, Drink-IT Edition, LINKFRESH Edition) while converging functionality onto the shared extension set documented at fnbdocs.apteancloud.com. Which edition/extension set a client gets affects available modules — confirm with Aptean/the reselling partner during scoping.
- A separate **Enterprise Edition** exists on Dynamics 365 Finance & Operations — that is a different product line and is **not** covered by this layer.

> ⚠️ Verify against current Aptean documentation — pricing, packaging and edition convergence change frequently; written from Aptean public materials as of 2026-07.

## How this layer works

The base knowledge in `../../erp/business-central/` describes standard BC setup decisions (finance, sales, purchasing, inventory, warehouse, manufacturing, general-setup). Each module file in this folder does two things, in this order:

1. **Changes to standard setup decisions** — for each standard BC decision the module modifies, it states how the options change (which standard options remain valid, which are replaced or constrained) and links back to the base file.
2. **New setup decisions introduced by this module** — decision blocks in the same format as the base layer: options table, required client info, interactions, default recommendation, risk rating and expertise tags.

When advising a client running Aptean F&B, read the base BC file **and** the module file together; the module file wins where they conflict. Blocks written without access to partner-gated Aptean documentation carry an explicit verification warning.
