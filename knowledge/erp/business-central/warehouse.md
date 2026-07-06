# Warehouse — Business Central (Standard)

> **Scope:** Microsoft Dynamics 365 Business Central (SaaS, current version)
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when the vendor releases functional changes to this area.

Warehouse covers the physical handling layer: locations, bins, and the document flows (receipts, put-aways, picks, shipments, movements) between posting an order and touching a box. It is in scope whenever a client stores goods — the real question is *how much* of it to switch on. The single most consequential decision is the complexity level per location: it determines which documents users live in every day, and changing it on a location with open activity and stock is genuinely disruptive. Item master and costing decisions live in [inventory.md](inventory.md); G/L wiring in [finance.md](finance.md#inventory-posting-groups-and-inventory-posting-setup).

---

## Location design

**Where:** **Locations** page / **Location Card**; **Inventory Setup → Location Mandatory**; in-transit locations (Location Card **Use As In-Transit** toggle); **Responsibility Centers** page.
**What it controls:** The physical/logical structure of stockholding: how many locations exist, whether every posting must carry a location code, which locations serve as virtual in-transit stock for transfers, and (via responsibility centres) how sales/purchase documents default to an office or site.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Single location, Location Mandatory = On** | One physical warehouse; keeps the door open for growth and warehouse features later | Almost never avoid — blank-location postings are the thing to avoid |
| **Multiple locations (one per physical site)** | Any client with more than one stocking point, including 3PL sites, consignment stock, vans/service vehicles, and quarantine as a separate location at basic levels | Modelling *areas within one building* as locations — that's what bins are for; location sprawl multiplies SKUs, transfer admin and posting-setup rows |
| **In-transit locations** | Required for standard (non-direct) transfer orders; also useful to make goods-on-the-water visible for import lead times | — (create at least one if transfers exist) |
| **Responsibility centres** | Multi-office clients wanting per-site document defaults and user filtering without separate companies | Simple clients — an extra admin concept users must understand; keep the mention brief and skip unless asked for |

**Required client info:**
- How many physical stocking points, including 3PLs, vans, consignment and returns/quarantine areas?
- Will stock move between sites (⇒ transfers, in-transit locations, possibly [SKUs](inventory.md#stockkeeping-units-skus))?
- Do different sites need different address/document defaults (responsibility centres) or just different stock (locations)?
- Any site expected to need bins or WMS-grade handling later? (Design its location code now, complexity later)

**Interactions:** Every location × posting-group combination needs a row in [Inventory Posting Setup](finance.md#inventory-posting-groups-and-inventory-posting-setup). Per-location planning needs [SKUs](inventory.md#stockkeeping-units-skus). Each location independently picks a rung on the [complexity ladder](#the-warehouse-complexity-ladder). Transfers between locations: [transfer orders vs direct transfers](#transfer-orders-vs-direct-transfers).

**Add-on impact:** None known beyond standard — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Location Mandatory = On from day one, one location per physical site (plus one in-transit), bins — not locations — for areas inside a building. Skip responsibility centres unless the client explicitly needs per-office document defaults.

**Risk of getting it wrong:** medium — locations can be added later, but re-carving stock from one location into several means transfer/reclass migrations, new posting-setup rows and planning re-tuning; retrofitting Location Mandatory after blank-location history is messy.

**Expertise tags:** `#warehouse` `#locations` `#structure`

---

## The warehouse complexity ladder

**Where:** **Location Card → Warehouse FastTab**: Require Put-away, Require Pick, Require Receive, Require Shipment, Directed Put-away and Pick (plus Bin Mandatory on the Bins FastTab).
**What it controls:** THE key warehouse decision, set per location: which documents the warehouse works with, how many process steps stand between an order and a posting, and whether the system directs *where* goods go. Microsoft frames these as complexity levels from "no dedicated warehouse activity" to full directed put-away and pick.

**Options:**

| Level | Settings | Client profile it fits | When to avoid |
|---|---|---|---|
| **(a) No warehouse handling** | All toggles off; post from orders/journals; bins optional | Micro-warehouses; office staff post shipments; few orders/day; trust in paperwork over process control | Any real separation between office and warehouse staff — nothing tells the warehouse what to do |
| **(b) Basic: inventory put-away / pick** | Require Put-away and/or Require Pick (order-by-order inventory documents; movements for internal flows) | Small warehouse, 1–5 warehouse staff, wants pick/put-away paper (or scanner) per order without changing office workflows; optional bins for shelf reference | High order volume needing consolidated waves — inventory documents are strictly order-by-order. Note: users can *still* post straight from the source document at this level, so discipline is procedural |
| **(c) Warehouse shipment / receipt (+ warehouse picks/put-aways)** | Require Receive + Require Ship (optionally + Require Put-away/Pick for warehouse put-away & pick documents, pick worksheets) | Mid-size warehouse; one truck arrives covering many POs, one shipment covers many orders; dedicated warehouse team; wave/consolidated picking via pick worksheet | Tiny operations — every receipt/ship now takes two documents; users who found (a) hard will drown |
| **(d) Full WMS: Directed Put-away and Pick** | Directed Put-away and Pick = On (forces all four requires + Bin Mandatory); zones, bin types, bin rankings, put-away templates, capacity, break-bulk, FEFO by bin | Larger/high-accuracy warehouses; system decides destination bins by ranking/template; temporary staff can operate from instructions; usually paired with scanners | Anyone unwilling to maintain bin master data; clients without scanning at meaningful volume; note item-journal-level restrictions (adjustments and counting go via warehouse journals) |

**Required client info:**
- Orders and order lines per day, per location; lines per pick run?
- Is there a dedicated warehouse team separate from office staff?
- Does one truck serve many orders (⇒ consolidated receipt/shipment, level c+)?
- Should the *system* decide where stock lives (⇒ level d), or do people know their warehouse?
- Inventory accuracy today and appetite for master-data upkeep (bin rankings, capacities)?
- Scanning hardware planned? ([barcode readiness](#barcode--handheld-readiness))

**Interactions:** Level determines everything downstream: [bin setup](#bin-setup-zones-bin-codes-rankings), [which journals adjust stock](#item-journal-vs-warehouse-journal-per-level), [counting method](inventory.md#inventory-counting), production/assembly/project handling fields (Prod. Consumption/Output Whse. Handling — coordinate with [manufacturing.md](manufacturing.md#flushing-methods-manual-vs-forward-vs-backward-vs-pick)), and FEFO picking which also needs [warehouse item tracking](inventory.md#item-tracking-lot--serial--package).

**Add-on impact:** Aptean F&B and handheld ISVs typically assume level (b) or (c) with bins and add scanning on top; full directed (d) plus ISV verticals needs compatibility checking — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Map each location honestly to the lowest level that supports its flows: (a) for micro-sites and vans, (b) for most SMB warehouses, (c) once consolidated receiving/shipping is real, (d) only with genuine scale, accuracy needs and a master-data owner. Do not give every location the flagship site's level.

**Risk of getting it wrong:** **high — disruptive to change on a live location.** Directed Put-away and Pick (and bin-structure changes generally) cannot simply be toggled on a location with open item ledger entries / warehouse documents; moving a live location up or down the ladder is a mini-project: stop activity, close or delete open warehouse documents, often zero out and re-post stock into the new bin structure, retrain everyone. Going *too high* is the classic failure: the client abandons warehouse documents and posts around them, corrupting the process.

**Expertise tags:** `#warehouse` `#wms` `#complexity-level` `#high-stakes`

---

## Bin setup (zones, bin codes, rankings)

**Where:** Location Card **Bins/Bin Policies FastTabs** (Bin Mandatory, default/receipt/shipment/production bins, Pick According to FEFO); **Bins** and **Zones** pages; **Bin Types**, **Bin Rankings** on bins, **Put-away Templates**, **Warehouse Classes** (directed only); Bin Creation Worksheet.
**What it controls:** Whether every posting at the location must state a bin, how the warehouse is addressed (bin coding), and — at directed locations — how the system chooses bins (types, rankings, templates, capacity, classes).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **No bins** | Small rooms where everyone knows where things are | Any location aspiring to level (c)/(d) later — retrofitting bins onto a stocked location is a stock-out/reload exercise |
| **Bin Mandatory, simple bins (+ fixed/default bin per item)** | Levels (a)–(c) wanting shelf-level accuracy and pick paper that says where to go | Clients who won't keep bin contents honest — wrong bin data is worse than none |
| **Zones + bin types + rankings + put-away templates** | Level (d) only: rankings drive pick sequence and put-away priority; templates encode placement rules; classes handle frozen/hazard segregation | Everywhere else — most of this machinery only executes under Directed Put-away and Pick |

Bin coding: mirror the physical walk sequence (aisle-rack-level, e.g. `A-01-3`) so bin-code sorting equals travel path — rankings then refine it (high ranking = preferred pick bins at directed locations).

**Required client info:**
- Physical layout: aisles/racking today, and any re-racking planned before go-live? (code bins after the *final* layout)
- Do items have fixed homes or float?
- Segregation needs: temperature zones, hazmat, quarantine?
- Who will own bin master data and bin-content accuracy?

**Interactions:** Bin Mandatory is forced by [Directed Put-away and Pick](#the-warehouse-complexity-ladder) and cannot be enabled while the location has open item ledger entries — sequence it at cutover. FEFO by bin requires warehouse [item tracking](inventory.md#item-tracking-lot--serial--package). Bin-level stock lives in warehouse entries — see [item vs warehouse journal](#item-journal-vs-warehouse-journal-per-level). Production input/output bins coordinate with [manufacturing.md](manufacturing.md#flushing-methods-manual-vs-forward-vs-backward-vs-pick).

**Add-on impact:** Aptean F&B leans on bins/zones for quality-status and temperature segregation — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Bin Mandatory with walk-sequence bin codes and fixed bins for fast movers at any location level (b)+; zones/rankings/templates only at directed locations, designed with the warehouse manager on the floor, not in a workshop room.

**Risk of getting it wrong:** medium–high — bin *codes* can be renamed/moved with effort (reclass/movement journals), but enabling or restructuring bins on a live stocked location requires emptying it logically; do it at go-live or during a stock freeze.

**Expertise tags:** `#warehouse` `#bins` `#directed-putaway-pick`

---

## Warehouse document flow toggles

**Where:** Location Card → Warehouse FastTab: **Require Receive / Require Shipment / Require Put-away / Require Pick** (and the derived combinations), plus the newer per-flow handling fields (e.g. Prod. Consump. Whse. Handling, Prod. Output Whse. Handling, Asm./Project handling).
**What it controls:** Which documents each inbound/outbound flow is forced through — this is the mechanical expression of the [complexity ladder](#the-warehouse-complexity-ladder), and the combinations matter.

**Options:**

| Combination | Forced flow | Notes |
|---|---|---|
| All off | Post receipt/shipment directly on the order | Level (a) |
| **Require Put-away** only | Purchase order → Inventory Put-away | Order-by-order; direct posting from the source document still possible — control is procedural |
| **Require Pick** only | Sales order → Inventory Pick | Same caveat; also feeds production/assembly component picking at basic level via inventory picks/movements |
| **Require Receive** / **Require Shipment** | Purchase orders → Warehouse Receipt; Sales orders → Warehouse Shipment | Consolidated, many orders per document; level (c) |
| **Require Receive + Put-away** | Warehouse Receipt → Warehouse Put-away | Two-step inbound with put-away instructions |
| **Require Shipment + Pick** | Warehouse Shipment → (Pick Worksheet →) Warehouse Pick | Two-step outbound, wave picking possible |
| **Directed Put-away and Pick** | All of the above, bin-directed; dependent toggles set automatically and greyed | Level (d); Bin Mandatory enforced |

**Required client info:**
- Per flow (purchase, sales, transfers, returns, production, assembly, projects): who physically handles it and should the system force a handling document?
- Are partial receipts/shipments and cross-order consolidation needed?
- Which flows must block direct posting by office users? (At basic levels the block is training + permissions, not the toggle itself)

**Interactions:** Combinations must be consistent with the location's [ladder level](#the-warehouse-complexity-ladder); production/assembly handling fields must match the [manufacturing design](manufacturing.md#flushing-methods-manual-vs-forward-vs-backward-vs-pick); shipments integrate with [sales order processing and shipping agents](sales.md#order-handling-flow-quote--order--ship--invoice-blanket-orders-drop-shipments-special-orders). Transfers respect these toggles too — see [transfer orders](#transfer-orders-vs-direct-transfers).

**Add-on impact:** Handheld ISVs and Aptean F&B drive their scanner transactions off these documents — the toggle design is effectively the scanner-workflow design; see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Set toggles per location from an agreed flow diagram per document type; resist enabling Receive/Ship "because it looks more professional" — every toggle adds a mandatory step for every order at that location.

**Risk of getting it wrong:** medium — toggles on a location can be changed with far less drama than the directed flag, but only when no open warehouse documents/orders reference the location, and every change re-trains the whole team and invalidates work instructions.

**Expertise tags:** `#warehouse` `#document-flow` `#location-card`

---

## Put-away/pick worksheets & warehouse employees

**Where:** **Put-away Worksheet** (enable via Location Card **Use Put-away Worksheet**), **Pick Worksheet**, **Movement Worksheet**; **Warehouse Employees** page (user ↔ location, one default location per user); worksheet templates.
**What it controls:** Whether put-away/pick instructions generate automatically per source document or are collected in a worksheet where a coordinator builds consolidated/prioritised work; and which users can operate warehouse documents at which locations (warehouse employee assignment is a hard gate, not a convenience).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Auto-create activity per document** | Smaller level (b)/(c) sites; receipt or shipment directly spawns its put-away/pick | Sites wanting waves, split-by-zone, or workload balancing |
| **Worksheets + coordinator** | Level (c)/(d) with a team lead who releases work in batches (by route, carrier cut-off, zone) | One-person warehouses — pure overhead |
| **Warehouse employees: minimal (each user, own site)** | Standard; set the default location correctly per user | Forgetting it entirely — "I can't see the pick" is the classic day-one go-live ticket |

**Required client info:**
- Is there a dispatcher/team-lead role to run worksheets, or do workers self-serve?
- Carrier cut-off times / route departures that define pick waves?
- Which users work at which locations, including floaters covering multiple sites?

**Interactions:** Worksheets only exist within the [ladder levels](#the-warehouse-complexity-ladder) that use warehouse picks/put-aways; pick worksheet lines come from released [warehouse shipments](#warehouse-document-flow-toggles); at directed locations, [bin rankings](#bin-setup-zones-bin-codes-rankings) drive suggested take bins and sorting.

**Add-on impact:** Scanner ISVs typically replace worksheet paper with device task queues; Aptean adds F&B-specific pick logic — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Auto-create per document at level (b); introduce the pick worksheet at level (c) once a coordinator role exists. Set up warehouse employees (with default locations) as a go-live checklist item.

**Risk of getting it wrong:** low — all reversible configuration; the pain is operational (unbalanced workloads, missed cut-offs) rather than structural.

**Expertise tags:** `#warehouse` `#picking` `#users`

---

## Item journal vs warehouse journal per level

**Where:** **Item Journal / Item Reclassification Journal** (item-ledger level) vs **Warehouse Item Journal / Warehouse Reclassification Journal / Warehouse Physical Inventory Journal** (bin/warehouse-entry level, directed locations).
**What it controls:** Which tool corrects stock at each complexity level. At non-directed locations, item journals adjust quantity (with bin codes on the line where bins exist). At directed put-away and pick locations, bin stock lives in warehouse entries: adjustments and counts are made in warehouse journals first, then synchronized to item ledger entries via the adjustment bin (*Calculate Warehouse Adjustment* in the item journal).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Item journal directly** | Levels (a)–(c); simple corrections, opening balances | Directed locations — posting item journals against bin-managed stock desynchronizes bins and ledger |
| **Warehouse journal → sync to item journal** | Mandatory at directed locations (two-step: register warehouse entry, then calculate/post warehouse adjustment) | Anywhere else (the pages exist only for bin-managed flows) |
| **Item reclassification vs warehouse reclassification** | Item reclass moves location/lot/dimension at ledger level; warehouse reclass moves bin-to-bin at directed locations | Using item reclass for bin moves at directed sites |

**Required client info:**
- Which locations will be directed (this decision is derivative of the ladder)?
- Who is allowed to make stock corrections, and do they understand the two-step at directed sites?
- How are opening balances loaded per location type (item journal vs warehouse journal with full tracking fields)?

**Interactions:** Entirely driven by the [complexity ladder](#the-warehouse-complexity-ladder); counting equivalents in [inventory.md — Inventory counting](inventory.md#inventory-counting); adjustment postings hit the accounts from [inventory posting setup](finance.md#inventory-posting-groups-and-inventory-posting-setup); item-tracked adjustments follow [item tracking rules](inventory.md#item-tracking-lot--serial--package).

**Add-on impact:** None known beyond scanner ISVs surfacing these journals on devices — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Train a named, small group on corrections; at directed sites make the warehouse-journal-then-sync sequence a written SOP and restrict item-journal permissions for that location's stock.

**Risk of getting it wrong:** medium — mis-posted adjustments at directed locations create bin/ledger mismatches that take specialist time to untangle (adjustment-bin archaeology), though no configuration is irreversible.

**Expertise tags:** `#warehouse` `#journals` `#stock-corrections`

---

## Transfer orders vs direct transfers

**Where:** **Transfer Orders** page; **Direct Transfer** toggle on the transfer order; **Inventory Setup → Direct Transfer Posting** (Direct Transfer vs Receipt and Shipment); in-transit locations.
**What it controls:** How stock moves between locations: a full two-step shipment/receipt through an in-transit location, or a one-step direct transfer — with real functional differences, not just fewer clicks.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Standard transfer order (in-transit)** | Real transport time between sites; partial shipments/receipts; full warehouse handling on both ends; item charges (freight) assignable to the transfer receipt | Same-building or same-day moves — the in-transit step is pure ceremony |
| **Direct transfer (posting = Direct Transfer)** | Instant moves between nearby sites; 2 item ledger entries, one posted document | No partial posting, no undo receipt, **no/limited warehouse handling** (notably unsupported into warehouse-receipt or directed locations), no item charges |
| **Direct transfer (posting = Receipt and Shipment)** | Wants one-step UX but partial posting and item-charge assignment; posts 4 entries with blank in-transit | Directed locations on the receiving end — check the supported-handling matrix before promising |
| **Item reclassification journal** | Back-office corrections of location codes, not an operational flow | Anything the warehouse should physically execute or that needs documents |

**Required client info:**
- Transport time between sites — hours or days? Is goods-in-transit visibility needed (finance may want it — in-transit stock is still owned)?
- Do receiving sites run warehouse receipts or directed put-away (constrains direct transfers hard)?
- Freight costs on inter-site moves to capitalise via [item charges](inventory.md#item-charges-landed-costs)?
- Should branch replenishment be planned (⇒ [SKUs](inventory.md#stockkeeping-units-skus) with Replenishment System = Transfer)?

**Interactions:** Requires [in-transit locations](#location-design) for the standard flow; respects each location's [document-flow toggles](#warehouse-document-flow-toggles); planned transfers come from [replenishment planning](inventory.md#replenishment--planning-parameters) via SKUs; item-tracked stock keeps its lot/serial identity across transfers ([item tracking](inventory.md#item-tracking-lot--serial--package)).

**Add-on impact:** None known beyond standard — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Standard transfer orders with one in-transit location as the norm; enable direct transfers (posting = Receipt and Shipment) only for genuinely instantaneous moves between low-complexity locations.

**Risk of getting it wrong:** low — per-order and per-setup choices are changeable; the trap is promising direct transfers into a directed or receipt-managed location and discovering the unsupported matrix during UAT.

**Expertise tags:** `#warehouse` `#transfers` `#multi-site`

---

## Barcode & handheld readiness

**Where:** Mostly *not* standard BC configuration: ISV apps (handheld/scanning solutions on AppSource, e.g. warehouse-scanning add-ons; Aptean's own devices layer) driving standard warehouse documents; standard BC contributes GTIN and Item Reference (item cross-reference/barcode) fields, item tracking warehouse toggles, and the document structure scanners execute against.
**What it controls:** Whether warehouse work is executed on paper or scanners. Flag to the client early: real-time scanning in BC is almost always an add-on/ISV purchase and a hardware project, not a checkbox — but the *standard* setup decisions above determine whether scanning can work at all.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Paper first, scanner-ready design** | Go-live under time pressure; low volumes; design bins/documents/tracking so scanners can be added in phase 2 | High-volume or serial/lot-heavy operations — keying tracking numbers by hand fails in practice |
| **Scanning ISV from day one** | Item-tracked goods at volume, directed locations, accuracy demands; budget for licences + devices + Wi-Fi survey | Micro-warehouses where the ISV cost exceeds the error cost |

**Required client info:**
- Are product barcodes present and reliable (GTIN on items, case vs each codes as item references)? Supplier labels usable, or will the client print own labels?
- Volume of lot/serial captures per day ([item tracking](inventory.md#item-tracking-lot--serial--package) without scanners is the top go-live complaint)
- Warehouse Wi-Fi coverage; device budget; IT capability for MDM
- If Aptean F&B is in scope, its handheld offering usually pre-empts a third-party scanning ISV — decide once, together

**Interactions:** Scanner workflows execute the documents chosen in the [complexity ladder](#the-warehouse-complexity-ladder) and [flow toggles](#warehouse-document-flow-toggles) — change those later and the scanner config changes too; SN/Lot *Warehouse* Tracking toggles ([inventory.md](inventory.md#item-tracking-lot--serial--package)) determine what scanners must capture; bin codes ([bin setup](#bin-setup-zones-bin-codes-rankings)) become scannable shelf labels.

**Add-on impact:** This whole area is add-on territory; for food & beverage clients evaluate the Aptean-native option first — see [Aptean F&B overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Decide the scanning question during design, not after go-live: paper-but-scanner-ready for simple sites, ISV scanning from day one wherever lot/serial capture is dense or the location is directed.

**Risk of getting it wrong:** medium — nothing irreversible in BC itself, but retrofitting scanning re-opens the document-flow design, and a go-live that assumed manual lot keying at volume tends to fail loudly in week one.

**Expertise tags:** `#warehouse` `#barcode` `#isv` `#hardware`
