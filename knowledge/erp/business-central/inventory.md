# Inventory — Business Central (Standard)

> **Scope:** Microsoft Dynamics 365 Business Central (SaaS, current version)
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when the vendor releases functional changes to this area.

Inventory covers everything on the item master and the company-wide costing engine: how items are identified, costed, tracked, replenished and counted. It is in scope for virtually every BC client that holds stock — even service-heavy clients usually carry some parts. The decisions here are among the most irreversible in the whole system: costing method and base unit of measure lock in once the first item ledger entry posts. Get these right in the design workshop, not during UAT. Physical handling (locations, bins, picks) lives in [warehouse.md](warehouse.md); the G/L side of inventory value lives in [finance.md](finance.md#inventory-posting-setup).

---

## Inventory Setup key toggles

**Where:** **Inventory Setup** page (Automatic Cost Posting, Expected Cost Posting to G/L, Automatic Cost Adjustment, Average Cost Calc. Type, Average Cost Period).
**What it controls:** Whether and when inventory cost hits the general ledger, whether cost changes flow forward to already-posted outbound entries automatically, and how average cost is computed for Average-costed items.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Automatic Cost Posting = On** (default) | Almost all SMB clients; G/L inventory value is always current and reconciles without ritual | Very high transaction volumes where per-posting G/L writes hurt performance — then post via the *Post Inventory Cost to G/L* batch job on the job queue |
| **Automatic Cost Posting = Off** + scheduled batch job | High-volume clients; controlled month-end process with a finance team that understands the reconciliation | Small clients with no job-queue discipline — the G/L drifts from the inventory subledger and nobody notices until year-end |
| **Expected Cost Posting to G/L = On** | Clients who receive/ship well before invoicing and want interim accruals visible in the G/L (accrual-strict finance teams, audit requirements) | Clients who invoice same-day; it adds interim accounts to maintain in [Inventory Posting Setup](finance.md#inventory-posting-setup) and confuses weaker finance teams |
| **Automatic Cost Adjustment = Always** (default) | New and low-volume clients: unit costs, COGS and profit stats always correct at posting time | Growing transaction volume — adjustment at posting time slows the system down |
| **Automatic Cost Adjustment = Month/Quarter (time-window)** | Mid-size clients: late item charges within the window still auto-adjust; older ones wait for the batch job | Clients who never schedule *Adjust Cost – Item Entries* — anything outside the window silently stays unadjusted |
| **Automatic Cost Adjustment = Never** + scheduled *Adjust Cost – Item Entries* | High-volume clients with a nightly job queue | Anyone without the job queue set up — margins will be wrong all month |
| **Average Cost Calc. Type = Item** vs **Item, Variant & Location**; **Average Cost Period = Day/Week/Month/Accounting Period** | Item + Day is the common default; per-location/variant when the same item genuinely has different cost pools per site | Note: only one period and calc type per fiscal year — you cannot flip this mid-year |

**Required client info:**
- How many item ledger entries per day do you expect at go-live and in 3 years? (drives Automatic vs batch)
- Do you ship or receive before invoicing, and does finance need those accruals in the G/L monthly?
- Is there anyone who will own a job queue, or must everything be automatic?
- For Average items: should the same item cost differently per warehouse?

**Interactions:** Expected Cost Posting requires interim accounts in [Inventory Posting Setup and General Posting Setup](finance.md#inventory-posting-setup). Cost adjustment timing directly determines when [item charges](#item-charges-landed-costs) land in COGS. Average settings only matter for items using the Average [costing method](#costing-method-per-item).

**Add-on impact:** Aptean Food & Beverage adds heavy item-cost machinery (catch weight, commodity pricing) that assumes disciplined cost adjustment — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Automatic Cost Posting = On, Expected Cost Posting = Off, Automatic Cost Adjustment = Always for SMB; move both cost jobs to the job queue once volume grows. Average Cost = Item / Day.

**Risk of getting it wrong:** medium — all toggles are changeable later, but a period of Never/off leaves wrong margins and a G/L reconciliation clean-up; average cost calc type/period can only change at fiscal-year boundary.

**Expertise tags:** `#inventory` `#costing` `#finance-integration`

---

## Costing method per item

**Where:** **Costing Method** field on the **Item Card** (default from **Inventory Setup → Default Costing Method**, or item templates).
**What it controls:** How inventory decreases are valued and therefore COGS, gross margin and balance-sheet inventory value — per item, forever. This is the flagship inventory decision.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **FIFO** | Stable product costs; shelf-life goods (oldest sold first); the safe default for distribution | Highly volatile purchase prices where average smoothing is wanted |
| **Average** | Volatile costs; bulk/commingled goods (chemicals, liquids, grain) that can't be differentiated | Clients who want entry-level cost traceability per receipt; note the average-cost-period settings then matter |
| **Standard** | Repetitive manufacturing wanting variance analysis; cost-control culture with staff to maintain standards | Clients without the discipline to maintain and roll up standard costs — stale standards produce garbage variances. See [manufacturing.md](manufacturing.md#standard-cost-and-variances) |
| **Specific** | High-value serialized items (machines, vehicles); regulated goods where the exact unit's cost must follow it | Anything not serial-tracked — requires SN-specific item tracking on inbound *and* outbound |
| **LIFO** | Rarely; only where the jurisdiction allows it and inventory levels are stable/growing | Disallowed under IFRS and in many countries — check the client's accounting framework first |

**Required client info:**
- What does the client's accountant/auditor require or forbid (IFRS ⇒ no LIFO)?
- Are costs stable or volatile? Are goods commingled or unit-identifiable?
- Is there manufacturing with a desire for variance reporting?
- Are any items serialized and high-value?
- What does the legacy system use, and does the opening balance strategy match?

**Interactions:** Standard cost ties into [manufacturing BOM roll-up](manufacturing.md#standard-cost-and-variances); Specific requires [SN-specific item tracking](#item-tracking-lot--serial--package); Average behaviour is tuned by the [Inventory Setup toggles](#inventory-setup-key-toggles); posted cost reaches the G/L via [inventory posting groups](finance.md#inventory-posting-groups). Lot-tracked items do **not** need Specific costing — item tracking and costing method are independent.

**Add-on impact:** Aptean F&B clients (catch weight, commodities) almost always land on FIFO or Average; verify Aptean module assumptions in [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** FIFO for trading/distribution; Standard only where manufacturing explicitly wants variance management; Average for bulk/commingled goods. One method per item is fine — but keep the set small and rule-based (e.g. "all manufactured = Standard, all traded = FIFO").

**Risk of getting it wrong:** **high-irreversible** — the costing method cannot be changed once item ledger entries exist for the item. The official workaround is to create a *new* item and move stock across with assembly orders, which is disruptive and pollutes history. Decide per item class before the first posting, including opening balances.

**Expertise tags:** `#inventory` `#costing` `#high-stakes`

---

## Item categories & attributes vs. item variants

**Where:** **Item Categories** page, **Item Attributes** page, **Item Variants** (Item Card → Related → Variants), plus **Item Templates**.
**What it controls:** How the item catalogue is structured: hierarchy for defaulting and reporting (categories), searchable/filterable properties (attributes), and whether one item number carries multiple sellable versions (variants, e.g. colour/size).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Categories + attributes, one item per SKU** | Most clients; clean master data, category-level defaulting of posting groups; attributes drive search and web catalogues | Apparel/footwear-style matrices — thousands of near-identical items explode the item list |
| **Item variants** (one item, many variants) | Colour/size/style matrices; variants share costing method and most master data but can have own SKUs, prices and stock | When the "variants" differ in cost structure, BOM, or posting behaviour — those are separate items. Also note many ISV apps and integrations handle variants poorly — verify before committing |
| **Catalog (nonstock) items** | Large vendor catalogues sold occasionally; convert to real items on first sale | Fast-movers — convert them properly up front |

**Required client info:**
- How many items, and is there a colour/size/style matrix?
- Do e-commerce/EDI/ISV integrations in scope support variants?
- What does the client want to report margin by — category, attribute, brand?
- Who owns master data creation, and can templates enforce their standards?

**Interactions:** Categories default posting groups — align with [finance posting group design](finance.md#inventory-posting-groups). Variants interact with [Average Cost Calc. Type](#inventory-setup-key-toggles) and can carry their own [SKUs](#stockkeeping-units-skus). Attributes matter for [sales-side catalogue and pricing](sales.md#pricing-and-discounts) but do not drive posting.

**Add-on impact:** Aptean F&B extends the item model substantially (catch weight units, quality attributes) — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Categories (2–3 levels max) + attributes; use variants only for genuine matrix products after confirming every integration in scope supports them.

**Risk of getting it wrong:** medium — categories and attributes are re-mappable, but retro-fitting variants onto items with history (or dissolving variants into items) means new records and data migration.

**Expertise tags:** `#inventory` `#master-data` `#catalogue`

---

## Units of measure design

**Where:** **Base Unit of Measure** on the Item Card; **Item Units of Measure** table (with qty-per); **Sales Unit of Measure** / **Purch. Unit of Measure** fields on the Item Card.
**What it controls:** The unit in which all inventory quantities, availability and unit costs are stored (base UoM), plus the default transactional units for sales and purchasing with conversion factors.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Base = smallest handling unit (PCS/EA)**, sell/buy in larger UoMs (BOX, PALLET) | The standard pattern; picking and counting happen in eaches; conversions are whole numbers | Items never handled below the case — storing in eaches just adds noise |
| **Base = the selling unit even if larger (e.g. KG, L, M)** | Bulk and continuous goods; quantities are naturally decimal | Discrete goods — decimal eaches are a data-quality smell |
| **Separate Sales/Purch. UoM defaults** | Buy by pallet, sell by carton — defaults save keying errors | Conversions that aren't exact (e.g. variable case weights) — that's catch weight territory, standard BC cannot do it |

**Required client info:**
- What is the smallest unit the client ever picks, counts or sells?
- Are purchase and sales units different, and are conversion factors truly fixed?
- Any variable-weight products (meat, cheese, produce)? — standard UoM cannot represent price-per-kg against count-based stock; that needs an add-on
- Rounding expectations: will fractional base quantities ever be legitimate?

**Interactions:** Base UoM is the unit of [cost](#costing-method-per-item) and of every availability figure the [planning engine](#replenishment--planning-parameters) sees. Warehouse UoM/break-bulk behaviour in directed put-away and pick depends on item UoM setup — see [warehouse.md](warehouse.md#bin-setup-zones-bin-codes-rankings). Sales UoM defaults flow into [sales documents and price lists](sales.md#pricing-and-discounts).

**Add-on impact:** Catch weight (dual UoM: pieces + actual kg) is a flagship Aptean F&B extension — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md). Do not fake it with decimal conversions in standard BC.

**Default recommendation:** Base = smallest handled unit; define larger UoMs with exact conversions; set Sales/Purch. UoM defaults where they differ. Never plan to "fix the base later."

**Risk of getting it wrong:** **high-irreversible** — the base unit of measure effectively locks once item ledger entries exist; changing it means a new item (or zeroing stock and rebuilding), and every historical quantity and cost is expressed in the old base. Rounding-precision errors from sloppy conversions are also painful to unwind.

**Expertise tags:** `#inventory` `#master-data` `#uom`

---

## Item tracking: lot / serial / package

**Where:** **Item Tracking Codes** page; assigned via **Item Tracking Code**, **Lot Nos.**, **Serial Nos.** fields on the Item Card. Expiration settings on the tracking code (**Use Expiration Dates**, **Require Expiration Date Entry**, **Strict Expiration Posting**).
**What it controls:** Whether every unit/lot/package must be identified on inbound and/or outbound postings, whether the identity must follow the unit through inventory (specific tracking), whether warehouse activities also track it (SN/Lot/Package *Warehouse* Tracking), and expiry-date enforcement.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **No tracking** | Commodity hardware, low-risk goods; keeps every transaction lighter | Regulated goods, recall exposure, warranty claims |
| **Lot tracking (specific)** | Food, pharma, chemicals — recall traceability both directions; the lot entering must be the lot leaving | High-velocity trading where nobody will actually key lots — tracking half-heartedly is worse than not at all |
| **Serial tracking (specific)** | Machines, electronics, warranty-managed goods; prerequisite for Specific costing | High-volume small items — the keying burden is brutal without scanning |
| **Package tracking** | Container/SSCC-level logistics on top of (or instead of) lots | Clients confusing it with license plating — it's an identifier, not full LP functionality |
| **Inbound-only (non-specific) tracking** | Record lots/SNs at receipt for warranty reference without enforcing at issue | Anywhere the auditor expects full traceability — non-specific tracking does not guarantee the chain |
| **Expiration dates + Strict Expiration Posting** | Perishables; blocks posting expired stock outward; enables FEFO picking | Clients whose supplier data has no reliable expiry dates yet |

**Required client info:**
- Recall/regulatory exposure? (Food, pharma, medical, aerospace ⇒ specific lot/serial)
- Where will numbers be captured — at receipt only, or every warehouse move? (drives SN/Lot Warehouse Tracking toggles and [scanning hardware](warehouse.md#barcode--handheld-readiness))
- Do items expire, and is FEFO picking expected?
- Realistic keystroke budget per transaction — is there scanning?

**Interactions:** SN-specific tracking is required for [Specific costing](#costing-method-per-item). FEFO picking requires warehouse-tracking toggles plus location settings — see [warehouse.md](warehouse.md#warehouse-document-flow-toggles). Changing a tracking code on an item with stock on hand is restricted; plan it at go-live. Tracking multiplies counting effort — see [inventory counting](#inventory-counting).

**Add-on impact:** This is Aptean F&B's home turf — extended lot attributes, quality holds, shelf-life stages, and vendor lot capture go far beyond standard — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md). If the client is food/beverage, design tracking with the add-on, not standard-first.

**Default recommendation:** Only track what regulation or warranty genuinely demands; when in doubt for food/pharma choose lot-specific with expiration dates and warehouse tracking on, and budget for scanners.

**Risk of getting it wrong:** high — turning specific tracking on/off for items with open documents and stock is a painful remediation (reclass journals, re-receipts), and missing traceability is discovered exactly when a recall happens.

**Expertise tags:** `#inventory` `#item-tracking` `#compliance`

---

## Stockkeeping Units (SKUs)

**Where:** **Stockkeeping Unit Card** (create via *Create Stockkeeping Unit* batch from the Item Card); **Average Cost Calc. Type** on Inventory Setup interacts.
**What it controls:** Per-location (and per-variant) overrides of item data: replenishment system, reordering policy and parameters, lead times, standard cost, transfer routing (Replenishment System = Transfer with a from-location). Without SKUs, one set of planning parameters applies everywhere.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **No SKUs** (item-level planning only) | Single stocking location, or multi-location where all sites behave identically | Any site-specific replenishment (buy centrally, transfer to branches) — impossible without SKUs |
| **SKUs for selected item/location pairs** | Hub-and-spoke distribution: central warehouse buys, branches replenish by transfer; different safety stocks per site | — |
| **SKUs everywhere, auto-created** | Mature multi-site clients with an owner for the extra master data | Small clients — every SKU is another card to maintain; unmaintained SKUs silently override the item card and cause "why did planning do that?" tickets |

**Required client info:**
- How many stocking locations, and do they replenish differently?
- Are branch warehouses replenished by transfer from a hub? (⇒ SKU with Replenishment System = Transfer)
- Who maintains planning parameters — one planner or per site?
- Standard-cost items with site-specific cost? (SKU standard cost, relevant with manufacturing)

**Interactions:** SKUs are where [reordering policies](#replenishment--planning-parameters) get location-specific; they pair with [transfer orders](warehouse.md#transfer-orders-vs-direct-transfers) for hub-and-spoke; per-SKU average costing requires the corresponding [Average Cost Calc. Type](#inventory-setup-key-toggles). Location design itself is in [warehouse.md](warehouse.md#location-design).

**Add-on impact:** None known beyond Aptean planning refinements — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Skip SKUs for single-site; introduce them the moment two locations need different replenishment behaviour, and only for the item/location pairs that are actually stocked.

**Risk of getting it wrong:** low–medium — SKUs can be added/deleted later; the real cost is planner confusion from stale SKU data overriding item cards.

**Expertise tags:** `#inventory` `#planning` `#multi-site`

---

## Replenishment & planning parameters

**Where:** Item Card / SKU Card **Planning** FastTab (Reordering Policy, Reorder Point, Reorder/Maximum Quantity, Safety Stock, Safety Lead Time, Time Bucket, Rescheduling/Lot Accumulation/Dampener periods, order modifiers); **Requisition Worksheet** and **Planning Worksheet**; MPS/MRP toggles in [Manufacturing Setup](manufacturing.md#manufacturing-setup).
**What it controls:** Whether and how the planning engine proposes purchases, transfers and production: blank policy = not planned; the four policies each imply a different philosophy of when and how much to reorder.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Blank (no policy)** + Order Planning / manual | Go-live phase; sporadic items; clients not ready to trust MRP | Steady-state fast movers — manual reordering doesn't scale |
| **Fixed Reorder Qty.** (+ reorder point) | Cheap, low-risk, steadily consumed items ("order 500 when below 200") | Items with forecasts or reservations — the docs explicitly warn against both; phase-out items (supply keeps coming) |
| **Maximum Qty.** (+ reorder point) | Shelf/bin top-up logic ("fill back to 1,000") | Same caveats as Fixed Reorder Qty.; avoid combining with time buckets that get overruled |
| **Lot-for-Lot** | Demand-driven items; works with forecasts; accumulates demand in a period into one supply | Items needing hard 1:1 order pegging |
| **Order** | Make/buy-to-order, configured or high-value goods; supply stays linked to the demand | Stocked commodities — every sales line spawns its own purchase |

Safety Stock covers demand variability; Safety Lead Time covers supply timing variability (set at least 1 day default on Inventory Setup per Microsoft's guidance); order modifiers (min/max/multiple) shape the proposed quantity.

**Required client info:**
- Which items are stock-driven vs order-driven? (usually an ABC split)
- Reliable demand history/forecast, or reorder-point gut feel?
- Supplier lead times and their variability; MOQs and order multiples per vendor
- Will manufacturing use MPS with a demand forecast, MRP, or both? (see [manufacturing.md](manufacturing.md#mps-mrp-scope))
- Who runs the worksheet, how often, and will they actually review action messages?

**Interactions:** Location-specific parameters require [SKUs](#stockkeeping-units-skus); reorder-point policies clash with reservations (set Reserve = Never on those items) and with forecasts (use Lot-for-Lot instead); planning respects [location and transfer structures](warehouse.md#location-design) and [UoM order multiples](#units-of-measure-design). Components planned for production tie to [manufacturing policy Make-to-Stock/Make-to-Order](manufacturing.md#manufacturing-setup).

**Add-on impact:** Aptean F&B adds shelf-life-aware planning behaviours — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Start narrow: Lot-for-Lot for A-items with real demand signals, Fixed Reorder Qty. or Maximum Qty. for C-items, Order for true make-to-order, blank for the long tail — and switch on planning per item group in waves after go-live, not big-bang.

**Risk of getting it wrong:** medium — parameters are freely changeable, but a badly tuned first run floods the requisition worksheet, the planner loses trust, and the client reverts to Excel for years.

**Expertise tags:** `#inventory` `#planning` `#mrp`

---

## Item charges (landed costs)

**Where:** **Item Charges** page; **Item Charge Assignment** from purchase/sales invoice and credit-memo lines (assignable to receipts, transfer receipts, return shipments).
**What it controls:** How freight, duty, insurance and handling costs are added to the inventory value of specific received quantities instead of being expensed — i.e. landed cost.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Expense freight to P&L** (no item charges) | Domestic buyers with immaterial inbound freight; simplest month-end | Importers — margins by item are systematically wrong |
| **Item charges assigned on the freight vendor's invoice** | Importers/wholesalers wanting true landed cost per item; charges can arrive after the goods and still flow to COGS via cost adjustment | Clients who won't do the assignment clicks — half-assigned charges are worse than a clean policy of expensing |
| **Standard cost absorbing estimated landed cost** | Standard-cost environments; variances catch the difference | FIFO/Average clients (not applicable) |

**Required client info:**
- Share of product cost that is freight/duty — is it material?
- Do freight invoices arrive before or after the goods (weeks later ⇒ check [Automatic Cost Adjustment window](#inventory-setup-key-toggles))?
- Allocation basis: amount, weight, volume, or equally?
- Who processes the freight vendor's invoice, and will they know which receipts to assign to?

**Interactions:** Late charges reach COGS only through [cost adjustment](#inventory-setup-key-toggles) — a Never/short-window setting plus no batch job means landed cost never lands. Charge postings follow [general posting setup](finance.md#general-posting-setup). Direct transfers restrict charge assignment to transfer receipts — see [warehouse.md](warehouse.md#transfer-orders-vs-direct-transfers).

**Add-on impact:** None known specific to Aptean F&B beyond standard usage — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md). Dedicated landed-cost ISV apps exist for complex duty/container scenarios.

**Default recommendation:** Use item charges for importers (allocate by amount unless weight/volume is clearly fairer); expense freight for domestic-only clients with immaterial inbound costs. Write the rule down — consistency beats precision.

**Risk of getting it wrong:** low–medium — reversible policy, but historical margins can't be restated retroactively and inconsistent usage muddies item profitability analysis.

**Expertise tags:** `#inventory` `#costing` `#landed-cost`

---

## Inventory counting

**Where:** **Physical Inventory Orders** + **Physical Inventory Recordings** (document-based); **Physical Inventory Journal** / **Warehouse Physical Inventory Journal** (journal-based); **Physical Inventory Counting Periods** assigned per item/SKU for cycle counting.
**What it controls:** How stock counts are organised, captured, approved and posted — annual wall-to-wall vs cycle counting, and documents vs journals.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Physical Inventory Orders + Recordings** | Structured counts split across several counters; blind-count print-outs; audit-friendly posted documents; double-count protection | Locations using **zones** in directed put-away and pick — not supported; use the warehouse journal instead |
| **Physical Inventory Journal** | Small teams, simple locations, quick ad-hoc corrections | Larger counts needing control/segregation — a journal is one editable page |
| **Warehouse Physical Inventory Journal** | Mandatory for bin-level counting at directed put-away and pick locations; counts warehouse entries, then sync to item ledger | Non-bin locations (irrelevant) |
| **Cycle counting via counting periods** | Mature clients; A-items monthly, B quarterly, C annually; spreads workload and may replace the year-end count (agree with auditor) | Clients without daily warehouse discipline — cycle counts on top of messy processes just document the chaos |

**Required client info:**
- Auditor requirements: full annual count, or is a documented cycle-count regime acceptable?
- How many counters at once, and do they need blind counts on paper/handheld?
- Any directed put-away and pick locations (forces the warehouse journal at bin level)?
- Item tracking density — counting lot/serial stock takes far longer; plan recording layout accordingly

**Interactions:** Which journal you count in depends entirely on the [warehouse complexity level](warehouse.md#the-warehouse-complexity-ladder) — at directed locations you count bins in the warehouse journal and synchronize to item ledger entries. Count adjustments post through the accounts wired in [inventory posting setup](finance.md#inventory-posting-setup). Counting item-tracked stock interacts with [item tracking](#item-tracking-lot--serial--package).

**Add-on impact:** Aptean F&B and most handheld/WMS ISVs replace paper recordings with scanner-driven counting — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md) and [barcode readiness](warehouse.md#barcode--handheld-readiness).

**Default recommendation:** Physical Inventory Orders for the annual count (non-zone locations), plus counting periods for cycle counting A/B items once the client is stable — typically from year two.

**Risk of getting it wrong:** low — process choice is reversible; the lasting damage is posting a badly controlled count (wrong quantities are a valuation event, and with item tracking, a traceability event).

**Expertise tags:** `#inventory` `#counting` `#stocktake`
