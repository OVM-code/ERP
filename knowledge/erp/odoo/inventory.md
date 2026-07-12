# Inventory — Odoo (Standard)

> **Scope:** Odoo 19 Enterprise (Odoo Online, Odoo.sh or on-premise); Community edition differences flagged inline
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when Odoo releases functional changes to this area (one major release per year, typically October).

Inventory covers the product master, the costing engine and the replenishment logic: how products are modelled, costed, tracked, reordered and counted. It is in scope for every Odoo client that holds stock. Two structural facts shape everything here: costing is configured **per product category, not per product** (the opposite granularity of Business Central), and material flow is driven by a **routes-and-rules engine** that is elegant when kept standard and a maintenance trap when customised early. Get category design and route architecture right in the design workshop — both are cheap to draw and expensive to redraw once stock moves exist. Physical handling (warehouses, locations, picking steps) lives in [warehouse.md](warehouse.md#warehouse--location-design); the G/L side of stock value lives in [finance.md](finance.md#inventory-valuation-posting-manual-vs-automated).

---

## Product type & catalogue design

**Where:** Product form (Inventory/Sales → Products), *Product Type* field plus the inventory-tracking option on goods; attributes and variants on the product template; Inventory Settings → *Variants* toggle.
**What it controls:** Whether a product carries stock at all, whether Odoo counts its quantities, and whether one product record represents many sellable versions (variants) or each version is its own product.

Since Odoo 18 the old *Storable / Consumable / Service* trio is gone: a product is **Goods** or **Service** (plus a sales-bundle *Combo* type), and goods have a *Track Inventory* option — tracked goods behave like the old storable products; untracked goods behave like the old consumables (always available, never counted, expensed on receipt). Odoo 19 keeps this model.
> ⚠️ Verify exact type/toggle labels against current Odoo documentation.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Goods, inventory tracked** | Anything bought/made to be stocked, valued and counted — the default for physical products | Low-value supplies nobody will ever count (packaging tape, office stock) — tracking them creates permanent phantom differences |
| **Goods, not tracked** ("consumable" pattern) | Cheap consumables expensed on receipt; items where availability checks would only block flow | Anything with real value on the balance sheet or recall exposure — untracked goods have no valuation and no traceability |
| **Service** | Labour, subscriptions, fees; no stock moves ever | — |
| **One template + variants** (attribute matrix: size/colour/etc.) | Genuine matrix products; variants share category (hence costing method), routes and most master data; eCommerce and POS handle variants natively | "Variants" that differ in cost structure, BoM logic or supplier — those are separate products. Matrices multiply: 3 attributes × handfuls of values = hundreds of variants, each with its own stock, forecast and reordering rule |
| **Separate products per version** | Few versions, or versions with different costing/routes/compliance | Large true matrices — the product list explodes and web-shop UX suffers |

Rule of thumb: variants are a **sales-side** convenience; the moment a variant needs its own costing method, category or procurement behaviour, it has outgrown being a variant.

**Required client info:**
- How many products, and is there a real attribute matrix (apparel-style) or just a handful of versions?
- Which "products" are actually consumables nobody will count?
- Do e-commerce/POS/EDI channels in scope rely on variant structure, and who will maintain attribute discipline?

**Interactions:** The product's category drives [costing method](#product-categories--costing-method-standard--avco--fifo) and [valuation](#inventory-valuation-manual-vs-automated) for all its variants alike. Tracked goods feed [reordering rules](#reordering-rules--replenishment) and [routes](#routes--procurement-rules-architecture-mtobuymanufacture). Per-variant BoM behaviour is a [manufacturing decision](manufacturing.md#bom-design-kits-multi-level-variants-by-products). Bulk product creation belongs to the [data migration approach](general-setup.md#data-migration-approach-imports--opening-balances).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Goods + tracked inventory for everything stocked and valued; untracked goods only for genuinely expendable supplies; variants only for true matrix products after confirming every channel in scope supports them.

**Risk of getting it wrong:** medium — types and tracking can be changed on a product with care, but dissolving a variant matrix into separate products (or the reverse) after go-live means new records, remapped integrations and migrated stock.

**Expertise tags:** `#inventory` `#item-design` `#variants`

---

## Product categories & costing method (standard / AVCO / FIFO)

**Where:** Inventory → Configuration → Product Categories — *Costing Method* field on the category (with the valuation and account settings alongside it).
**What it controls:** How outbound stock is valued — therefore COGS, margins and balance-sheet stock value — for **every product in the category at once**. This is the flagship inventory decision in Odoo, and the granularity is the trap: where BC sets costing method per item, Odoo sets it per category, so the category tree must be designed *around* costing boundaries, not around reporting taste.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Standard Price** | Manufacturers wanting stable costs and variance-style analysis; clients with the discipline to maintain the cost field | Anyone who won't maintain standards — a stale cost silently misstates every margin; purchase-price swings vanish into price-difference postings |
| **Average Cost (AVCO)** | Volatile purchase prices; bulk/commingled goods; clients wanting smooth margins without per-receipt cost layers | Clients needing receipt-level cost traceability; note AVCO recomputes on every receipt — opening-balance and return handling need care |
| **First In First Out (FIFO)** | Trading/distribution; the safe default where costs move and auditors want a defensible flow assumption | Highly volatile prices where the client explicitly wants smoothing (then AVCO) |

No LIFO (irrelevant for IFRS/Belgian GAAP anyway) and no specific/serial-cost method — high-value serialized goods get FIFO plus [serial tracking](#tracking-lots-serials--expiry), which approximates but does not equal unit-specific costing. If per-unit costing is a hard requirement, flag it as a gap early.

Rule of thumb: design the category tree **costing-first** — one category per (costing method × account set × removal strategy) combination, usually 5–15 categories total. A category tree mirroring the web-shop menu is a design smell; that's what eCommerce categories and tags are for.

**Required client info:**
- What does the accountant/auditor require or forbid, and what does the legacy system use?
- Are costs stable or volatile? Goods commingled or unit-identifiable? Manufacturing that wants standard-cost variance thinking?
- Can product groups be partitioned cleanly so no group needs two costing methods?

**Interactions:** The category also carries the [valuation mode and accounts](#inventory-valuation-manual-vs-automated), the default [removal strategy](warehouse.md#removal-strategies-fifofefolifo), and can carry [routes](#routes--procurement-rules-architecture-mtobuymanufacture) — four reasons the tree is load-bearing. Standard price interacts with [BoM roll-up](manufacturing.md#manufacturing-scope--mo-flow); landed costs layer onto FIFO/AVCO via [purchasing.md](purchasing.md#landed-costs).

**Add-on impact:** No add-on overlays recorded for Odoo in this knowledge base yet.

**Default recommendation:** FIFO for trading/distribution categories, AVCO for bulk/commingled goods, Standard only where manufacturing explicitly wants it — and a deliberately small category tree drawn before any product import.

**Risk of getting it wrong:** high — unlike BC it is *technically* changeable: switching a category's costing method revalues on-hand stock and posts the accounting delta. But doing so mid-flight disrupts margins, audit trail and open documents, and moving products between categories with stock on hand is equally disruptive. Treat as irreversible-in-practice; change only at a controlled period cut-over with finance in the room.

**Expertise tags:** `#inventory` `#costing` `#high-stakes`

---

## Inventory valuation: manual vs automated

**Where:** *Inventory Valuation* setting per product category (Manual/periodic vs Automated/perpetual); the stock input/output/valuation accounts configured with the category when automated.
> ⚠️ Recent versions have moved parts of this configuration between the category and accounting settings — verify placement against current Odoo documentation.
**What it controls:** Whether stock moves post journal entries in real time (perpetual) or the accountant books stock value periodically from inventory reports (periodic). This block owns the *operational* choice; the account wiring and the continental vs anglo-saxon question live in [finance.md](finance.md#continental-vs-anglo-saxon-accounting--automatic-accounts) and [finance.md — valuation posting](finance.md#inventory-valuation-posting-manual-vs-automated).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Manual (periodic)** | Small clients whose fiduciary books stock value at year-end (the Belgian SME norm); simplest go-live; no risk of a misconfigured automated posting stream | Clients wanting monthly margins and a stock figure in the G/L that means something between closes |
| **Automated (perpetual)** | Clients with monthly reporting discipline; wholesale/manufacturing where stock is the balance sheet; anyone reconciling stock to G/L more than annually | Clients without a controller — automated valuation generates entries nobody reviews, and cleanup is far worse than never having switched it on |
| **Mixed per category** | Valuing the material categories automatically, leaving consumable-ish categories manual | Doing it accidentally — a half-automated valuation confuses every reconciliation |

Rule of thumb: automated valuation is a *finance-maturity* decision, not a feature checkbox. If nobody will reconcile the stock interim accounts monthly, choose Manual and revisit in year two.

**Required client info:**
- Who closes the books, how often, and do they want stock in the G/L monthly or annually?
- Continental or anglo-saxon COGS presentation (Belgium: continental default)? — decided in [finance.md](finance.md#continental-vs-anglo-saxon-accounting--automatic-accounts)
- Is there a controller who will own the stock-to-G/L reconciliation?

**Interactions:** Meaningless without the [costing method](#product-categories--costing-method-standard--avco--fifo) decision; adjustment postings from [counts](#inventory-adjustments--cycle-counting) only hit the G/L when automated; valuation entries respect [lock dates](finance.md#period-close--lock-dates); opening stock posting belongs to [data migration](general-setup.md#data-migration-approach-imports--opening-balances).

**Add-on impact:** None known yet — this knowledge base holds no Odoo add-on layers.

**Default recommendation:** Manual for small clients with an external fiduciary; Automated (with continental accounting) once the client wants monthly margins and has someone to reconcile — decided per category but kept uniform unless there's a stated reason.

**Risk of getting it wrong:** medium — switchable per category later, but flipping mid-year creates a reconciliation project and a discontinuity in the G/L stock figure; agree the switch date with the accountant.

**Expertise tags:** `#inventory` `#costing` `#finance-integration`

---

## Units of measure policy

**Where:** Inventory Settings → *Units of Measure* toggle; unit list under Inventory → Configuration; per product: the stock/sales unit and a separate purchase unit.
**What it controls:** The unit in which stock, availability and cost are expressed, and the conversion factors applied when buying or selling in other units. Odoo gives each product **one** stock unit (also the sales default) plus an optional purchase unit — leaner than BC's three-way split, and less forgiving of sloppy conversions.

**Odoo 19 note:** v19 reworked the UoM model — packagings and units were consolidated into a single unit concept with relative ratios, relaxing the older strict UoM-category constraint (where conversions only worked inside one category such as Weight or *Unit*). The policy advice below is version-stable; the mechanics are not.
> ⚠️ Verify the current v19 UoM/packaging model against Odoo documentation before the design workshop.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **One unit per product, everywhere** | Most clients; zero conversion risk; counting, costing and pricing all speak the same unit | Genuinely different buy/sell units (buy pallets, sell pieces) — forcing one unit pushes conversion errors into people's heads |
| **Stock in smallest handled unit + separate purchase unit** | Buy by box/pallet, pick and sell by piece; exact integer conversions | Conversions that aren't fixed (variable case weights) — that is catch-weight territory, which standard Odoo does not do |
| **Stock in bulk unit (kg, L, m)** | Continuous goods; decimal quantities are natural | Discrete goods — decimal pieces are a data-quality smell |

Traps: rounding precision on units (a 0.01 rounding on a unit converted 1:1000 manufactures phantom quantities); changing a product's unit after stock moves exist is blocked/destructive — plan it like a costing change; users "fixing" conversions per order line instead of on the master data.

**Required client info:**
- Smallest unit ever picked, counted or sold, per product family?
- Are purchase and sales units different, with truly fixed conversion factors?
- Any variable-weight products (food, metals)? — standard UoM cannot price per kg against piece-counted stock

**Interactions:** The stock unit is the unit of [cost](#product-categories--costing-method-standard--avco--fifo) and of every quantity [reordering rules](#reordering-rules--replenishment) see. Purchase units pair with [vendor pricelists](purchasing.md#vendor-master-data--vendor-pricelists). Box/pallet multiples may be better modelled as [packaging](#packages-packaging--consignment). Scanned units must match [barcode operations](warehouse.md#barcode-operations).

**Add-on impact:** None known — no Odoo add-ons documented in this knowledge base yet.

**Default recommendation:** One unit per product wherever possible; otherwise stock in the smallest handled unit with exact integer purchase conversions. Never plan to "fix the unit later."

**Risk of getting it wrong:** **high-irreversible** — a product's stock unit is effectively locked once moves exist, and every historical quantity and cost is expressed in it. Conversion and rounding errors compound silently until a count exposes them.

**Expertise tags:** `#inventory` `#uom`

---

## Tracking: lots, serials & expiry

**Where:** Inventory Settings → Traceability → *Lots & Serial Numbers* and *Expiration Dates* toggles; per product, the inventory-tracking option (by quantity / by lots / by unique serial number); expiry-day defaults on the product; dates carried on the lot/serial record.
**What it controls:** Whether each unit or batch must be identified on receipts and deliveries, whether expiry dates are captured and enforced, and what the traceability report can reconstruct when a recall call comes.

Lots, serials and expiration dates are all standard and available in **Community** — expiry does not require Enterprise. What *is* Enterprise is the Barcode app that makes capturing them bearable at volume.
> ⚠️ Verify current edition boundaries against Odoo documentation.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **No tracking (by quantity)** | Commodity goods, low-risk items; every transaction stays light | Regulated goods, recall exposure, warranty-managed items |
| **By lots** | Food, pharma, chemicals, batch-made goods; recall traceability upstream (which supplier lot?) and downstream (which customers got it?) via the traceability report | High-velocity flows where nobody will really key lots — half-hearted tracking is worse than none |
| **By unique serial number** | Machines, electronics, warranty units; one number per unit, enforced on out as well as in | High-volume small items without scanners — the keying burden is brutal |
| **Lots + expiration dates** | Perishables; expiry/best-before/removal/alert dates default from the product onto each lot; expired stock can be blocked and FEFO picking enabled | Clients whose inbound data has no reliable dates yet — garbage dates make FEFO actively harmful |

Rule of thumb: track exactly what regulation, recall exposure or warranty demands — nothing more. Every tracked product multiplies keystrokes on receipt, delivery *and* [counting](#inventory-adjustments--cycle-counting).

**Required client info:**
- Recall/regulatory exposure (food, pharma, medical ⇒ lots at minimum)?
- Do items expire, and is FEFO picking expected (⇒ [removal strategies](warehouse.md#removal-strategies-fifofefolifo))?
- Where are numbers captured — receipt only or every move — and is there scanning hardware ([barcode readiness](warehouse.md#barcode-operations))?
- Can suppliers actually provide lot/expiry data on their labels/ASNs?

**Interactions:** FEFO/FIFO removal by lot date is configured with [removal strategies](warehouse.md#removal-strategies-fifofefolifo); tracking density shapes [count effort](#inventory-adjustments--cycle-counting); serial tracking does **not** give serial-specific costing (see [costing block](#product-categories--costing-method-standard--avco--fifo)); manufacturing consumption of tracked components ties to [MO flow](manufacturing.md#manufacturing-scope--mo-flow).

**Add-on impact:** No Odoo add-on layers exist in this knowledge base yet — quality/compliance add-ons would land here.

**Default recommendation:** Lots with expiration dates for anything perishable or regulated, serials only for high-value warranty units, nothing for the rest — and budget Enterprise Barcode if more than a handful of products are tracked.

**Risk of getting it wrong:** high — enabling tracking on a product with untracked stock on hand (or vice versa) forces adjustment gymnastics, and missing traceability is discovered exactly when a recall happens.

**Expertise tags:** `#inventory` `#item-tracking` `#compliance`

---

## Routes & procurement rules architecture (MTO/buy/manufacture)

**Where:** Inventory Settings → Warehouse → *Multi-Step Routes*; Inventory → Configuration → Routes (and the push/pull rules inside them); route checkboxes on products, product categories, warehouses and sales order lines.
**What it controls:** How demand becomes supply: whether a product is bought, manufactured, replenished on order (MTO), dropshipped, or moved between locations — and along which chain of steps. This is Odoo's flagship supply-chain abstraction and the second flagship decision of this file.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Buy** route (with Purchase app) | Anything procured; pairs with a vendor on the product | — |
| **Manufacture** route (with Manufacturing app) | Anything made in-house; pairs with a BoM | — |
| **Replenish on Order (MTO)** + Buy/Manufacture | Order-driven goods: each sales order spawns its linked PO/MO; note the MTO route ships **archived** — unarchive it deliberately, not accidentally | Stocked fast-movers — MTO on those creates a PO per order line and destroys purchasing consolidation |
| **Dropship** route (Purchase setting) | Vendor ships direct to customer; Odoo books the flow without stock touching the warehouse | Clients wanting quality inspection of every unit — dropship bypasses the dock |
| **Custom routes** (own push/pull rules) | Genuine multi-step or inter-warehouse flows the standard warehouse-generated routes don't cover | Almost everywhere else. Custom rule chains are the classic Odoo consulting scar: hard to debug, harder to hand over |

Route resolution when a need arises: the route forced on the sales order line wins, then routes on the product, then its category, then the warehouse's own routes.
> ⚠️ Verify the exact precedence order against current Odoo documentation.

Rule of thumb: standard routes + the warehouse's auto-generated reception/delivery routes cover ~95% of SMEs. Every custom route must be drawn as a diagram, named for its business meaning, and owned by someone.

**Required client info:**
- Per product family: bought, made, or both? Order-driven or stock-driven? Any dropship flows?
- Multi-warehouse resupply (hub feeds branches)?
- How many receiving/shipping steps ([complexity ladder](warehouse.md#inboundoutbound-steps-the-complexity-ladder))?

**Interactions:** MTO vs reordering rules is the central replenishment fork — see [reordering block](#reordering-rules--replenishment) and [purchasing.md](purchasing.md#replenishment-triggers-reordering-rules-vs-mto). Routes generated per warehouse depend on [warehouse design](warehouse.md#warehouse--location-design) and step configuration. Manufacture route presumes [manufacturing scope](manufacturing.md#manufacturing-scope--mo-flow). Categories can carry routes — one more reason the [category tree](#product-categories--costing-method-standard--avco--fifo) is load-bearing.

**Add-on impact:** Nothing recorded — this knowledge base has no Odoo add-on overlays yet.

**Default recommendation:** Standard routes only at go-live: Buy or Manufacture per product, MTO unarchived only for genuinely order-driven items, dropship where the business already works that way. First custom route no earlier than phase two, diagrammed and reviewed.

**Risk of getting it wrong:** medium-high — routes are editable, but wrong route assignments generate wrong documents daily (surprise POs, missing MOs), and a custom-rule architecture calcifies fast: open documents pin old rules, and nobody dares touch the chains.

**Expertise tags:** `#inventory` `#routes` `#high-stakes`

---

## Reordering rules & replenishment

**Where:** Reordering rules per product (and per location): min/max quantities, multiple-of, trigger auto/manual, preferred route, visibility days; the Replenishment dashboard under Inventory → Operations; lead times on vendor pricelists, product and company settings.
**What it controls:** Whether Odoo proposes (or silently creates) purchase orders, manufacturing orders and transfers to keep stock between minimum and maximum — based on **forecasted** quantity (on hand + incoming − outgoing), not on-hand.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **No rule** (manual/MTO) | Order-driven items ([MTO route](#routes--procurement-rules-architecture-mtobuymanufacture)); the long tail; go-live phase | Steady fast-movers — manual reordering doesn't scale past a few dozen SKUs |
| **Min/max rule, trigger = Manual** | The trust-building default: shortages appear on the Replenishment dashboard, a human clicks *Order* | Clients who will never open the dashboard — a suggestion nobody reads is no rule at all |
| **Min/max rule, trigger = Auto** | Mature data: draft POs/MOs appear untouched by humans; use *visibility days* to pull forward demand inside the lead-time horizon | Dirty demand data or untrusted lead times — auto rules amplify garbage into real purchase orders |
| **0/0 rule** | "Replenish exactly what's consumed, when consumed" — MTO-like behaviour while keeping demand consolidated | When true order-to-order pegging is required (that's MTO) |

Rule of thumb: min = demand over replenishment lead time + safety; max = min + economic order cycle. Wrong lead times break the forecast quietly — maintain vendor lead time per [vendor pricelist](purchasing.md#vendor-master-data--vendor-pricelists) before tuning any rule.

**Required client info:**
- Which items are stock-driven vs order-driven (ABC split)?
- Are supplier lead times and MOQs known and maintained anywhere today?
- Who reviews replenishment, how often — and can they be trusted with Auto?
- Manufacturing planning ambitions? Statistical/forecast-based planning is the Master Production Schedule's job — **MPS is Enterprise-only**, boundary and fit in [manufacturing.md](manufacturing.md#planning-mps-scheduling--capacity). Reordering rules themselves are available in Community.

**Interactions:** Rules act per location, so [warehouse/location design](warehouse.md#warehouse--location-design) comes first; each rule fires its preferred [route](#routes--procurement-rules-architecture-mtobuymanufacture); the MTO-vs-rule fork is argued in [purchasing.md](purchasing.md#replenishment-triggers-reordering-rules-vs-mto); quantities are in the product's [unit](#units-of-measure-policy).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Manual-trigger min/max rules on A/B movers at go-live, nothing on the tail, MTO only where genuinely order-driven; graduate proven rules to Auto in waves once lead times and demand data have earned trust.

**Risk of getting it wrong:** medium — parameters are freely changeable, but a badly tuned first month floods purchasing with junk proposals, the planner stops trusting the system, and the client reverts to Excel for years.

**Expertise tags:** `#inventory` `#replenishment` `#planning`

---

## Inventory adjustments & cycle counting

**Where:** Inventory → Operations → Physical Inventory (count lines per product/location/lot with counted qty, scheduled date and assigned counter); company-level annual inventory date in Inventory settings; per-location recurring count frequency for cycle counting.
> ⚠️ Verify current menu naming and the per-location count-frequency field against Odoo documentation.
**What it controls:** How counted reality replaces system quantity — wall-to-wall annual counts vs rolling cycle counts — and who may apply differences. Every applied line is an adjustment move; under [automated valuation](#inventory-valuation-manual-vs-automated) it is also a journal entry.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Annual full count** | The audit baseline; small stock, once-a-year discipline | As the *only* control in a busy warehouse — 11 months of drift between truths |
| **Cycle counting** (recurring counts per location, A-locations more often) | Mature clients; spreads workload; may replace the year-end count if the auditor agrees in writing | Sites without daily process discipline — cycle counts on a messy process just document the chaos on a schedule |
| **Ad-hoc adjustments** | Correcting a found error, today, with a reason | As a culture. Odoo makes adjusting a quantity dangerously easy; unreviewed ad-hoc adjustments are how shrinkage, bad UoM conversions and process failures stay invisible |

Rule of thumb: restrict who can *apply* counts, require a reason on every ad-hoc adjustment, and review the adjustment history monthly — the pattern of adjustments is a free process-quality report.

**Required client info:**
- Auditor requirement: full annual count, or is a documented cycle-count regime acceptable?
- Counting workload: locations, SKUs, and lot/serial density (tracked stock counts far slower)?
- Who is allowed to apply differences — and is stock trusted enough at [migration](general-setup.md#data-migration-approach-imports--opening-balances) to import as-is, or is a full count part of go-live?

**Interactions:** Adjustment postings hit the G/L only under [automated valuation](#inventory-valuation-manual-vs-automated) — and land in a closed period if [lock dates](finance.md#period-close--lock-dates) aren't respected. Counting tracked stock interacts with [lots & serials](#tracking-lots-serials--expiry); count layout follows [location design](warehouse.md#warehouse--location-design); scanner-driven counting needs [barcode operations](warehouse.md#barcode-operations) (Enterprise).

**Add-on impact:** No add-on overlays recorded for Odoo in this knowledge base yet.

**Default recommendation:** Full count at migration and year one's close; introduce cycle counting on A-items from year two; lock adjustment rights to named users from day one.

**Risk of getting it wrong:** low–medium — process choice is reversible, but a badly controlled count is a valuation event (and with tracking, a traceability event), and an easy-adjustment culture permanently corrupts stock accuracy.

**Expertise tags:** `#inventory` `#counting`

---

## Packages, packaging & consignment

**Where:** Inventory Settings toggles: *Packages* (physical boxes/pallets with package types), product packaging (quantity multiples such as "box of 12" — in Odoo 19 folded into the reworked [unit model](#units-of-measure-policy)), and *Consignment* (owner field on receipts).
> ⚠️ Verify the v19 packaging/UoM consolidation and setting names against current Odoo documentation.
**What it controls:** Three separate things clients constantly conflate: **packaging** = a sales/purchase quantity multiple (ordering in boxes of 12 while stocking pieces); **packages** = identifiable physical containers (this pallet, SSCC label, moved as one unit); **consignment** = stock physically present but owned by someone else, excluded from your valuation.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **None of the three** | Most simple SMEs — pieces in, pieces out | — |
| **Packaging (quantity multiples)** | Buying/selling in fixed multiples without changing the stock unit; keeps POs/SOs in the language of boxes | Non-fixed multiples; or when the multiple is really a separate purchase unit decision — decide against the [UoM policy](#units-of-measure-policy), not alongside it |
| **Packages** | Pallet/carton-level logistics, SSCC labelling, moving a whole pallet in one scan | Clients without scanning or real container handling — package records nobody maintains become fiction |
| **Consignment (owner on receipt)** | Vendor-owned stock on your floor (or customer-owned goods for processing); keeps foreign stock out of your valuation | Faking it with a separate location and no owner — the stock then wrongly enters your valuation and your counts |

**Required client info:**
- Are buy/sell multiples fixed, and should documents speak in boxes or pieces?
- Is there pallet/SSCC-level handling, and is scanning hardware in scope?
- Any stock on site not owned by the client (or client stock at third parties)?

**Interactions:** Packaging vs purchase unit is one decision, taken in [units of measure policy](#units-of-measure-policy). Packages pair with [barcode operations](warehouse.md#barcode-operations) and [putaway rules](warehouse.md#putaway-rules--storage-categories). Consigned stock must stay out of [valuation](#inventory-valuation-manual-vs-automated) — verify with finance how the auditor wants it evidenced at [count time](#inventory-adjustments--cycle-counting).

**Add-on impact:** None known yet — this knowledge base holds no Odoo add-on layers.

**Default recommendation:** Skip all three at go-live unless there's a concrete flow demanding them; packaging first where fixed multiples exist, packages only with scanners, consignment only for genuinely foreign-owned stock.

**Risk of getting it wrong:** low — all three toggle on later with modest rework; the exception is consignment modelled wrongly from the start, which silently misstates stock value until an auditor finds it.

**Expertise tags:** `#inventory` `#item-design` `#uom`
