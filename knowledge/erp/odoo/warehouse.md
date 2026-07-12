# Warehouse — Odoo (Standard)

> **Scope:** Odoo 19 Enterprise (Odoo Online, Odoo.sh or on-premise); Community edition differences flagged inline
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when Odoo releases functional changes to this area (one major release per year, typically October).

Warehouse covers the physical handling layer in the Inventory app: warehouses, locations, the multi-step receipt and delivery flows, putaway and removal logic, picking methods, and barcode execution. It is in scope for every client that stores goods — the question is how many of Odoo's optional layers to switch on. Odoo's equivalent of a warehouse complexity ladder is the combination of receipt/delivery steps (1/2/3), storage locations, batch/wave/cluster picking, and the Barcode app: each rung adds process control and each rung adds daily clicks. Item master, routes and costing live in [inventory.md](inventory.md); who may touch which operation is access-rights territory ([general-setup.md](general-setup.md#users-access-rights--record-rules)).

---

## Warehouse & location design

**Where:** Inventory app → Configuration → Warehouses; Inventory → Configuration → Settings → Warehouse → **Storage Locations** (unlocks Configuration → Locations).
**What it controls:** The physical/logical structure of stockholding: how many warehouses exist (each gets its own operation types, routes and short-code prefix, e.g. `WH`), whether stock is tracked per location inside a warehouse, and the location hierarchy (parent/child, e.g. `WH/Stock/Shelf 1`). Location types: Internal (real stock), View (grouping node, cannot hold stock), and the virtual counterpart types Odoo posts against — Vendor, Customer, Inventory Loss (adjustments), Production (consumption/output) and Transit.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **One warehouse, Storage Locations off** | Single small site where nobody asks *where inside the building* stock sits; fewest clicks per transfer | Any ambition toward multi-step flows, putaway, removal by location or barcode — all of it presumes locations |
| **One warehouse, Storage Locations on** | The standard SMB setup: one site, locations for zones/racks/shelves; enables the whole ladder later | Micro-operations that will genuinely never care about position — every move now carries a source/destination location |
| **Multiple warehouses (one per physical site)** | Any client with more than one stocking point — branch, shop, 3PL, consignment site; each site gets its own steps setting and resupply routes | Modelling *areas within one building* as warehouses — that is what locations are for; extra warehouses multiply operation types and routes |
| **Deep location hierarchy (4+ levels)** | Barcode-scanned warehouses where the shelf code is the walk path | Paper-based sites — deep trees look tidy in a workshop and die in daily use; two or three levels (`WH/Stock/Zone/Rack`) is plenty |

Rule of thumb: one warehouse per physical address, locations for everything inside the building, View-type locations only as grouping nodes for reporting.

**Required client info:**
- How many physical stocking points, including 3PLs, consignment stock and vans?
- Does anyone need to know *where inside the building* an item sits, or just how many are on site?
- Will stock move between sites (⇒ [resupply routes](#internal-transfers--inter-warehouse-resupply))?
- Any site expected to run barcode scanning later? (Design location codes now, scan later)

**Interactions:** Steps per warehouse are set on the warehouse form ([complexity ladder](#inboundoutbound-steps-the-complexity-ladder)); putaway and storage categories presume locations ([putaway](#putaway-rules--storage-categories)); a Removal Strategy and a cycle-count frequency can be set per location ([removal](#removal-strategies-fifofefolifo), [inventory.md — cycle counting](inventory.md#inventory-adjustments--cycle-counting)); warehouses per company in multi-company setups: [general-setup.md](general-setup.md#company-structure-one-company-vs-multi-company).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** One warehouse per site, Storage Locations on from day one (the cost is small, retrofitting is not), a shallow location tree named after the physical walk sequence.

**Risk of getting it wrong:** medium — warehouses and locations can be added later, but re-carving a single-location history into real locations means mass internal transfers and re-tuned putaway/removal, and renaming warehouse short codes ripples through every document reference.

**Expertise tags:** `#warehouse` `#locations` `#structure`

---

## Inbound/outbound steps (the complexity ladder)

**Where:** Warehouse form → Warehouse Configuration tab → **Incoming Shipments** / **Outgoing Shipments**; prerequisite: Inventory → Configuration → Settings → Warehouse → **Multi-Step Routes** (auto-enables Storage Locations).
**What it controls:** THE key Odoo warehouse decision, set per warehouse: how many chained transfers stand between a purchase order and stock, and between stock and the customer. Each extra step is a separate operation type with its own document queue and staging location.

**Options:**

| Level | Setting (exact option label) | Flow | Client profile it fits |
|---|---|---|---|
| **Receipt, 1 step** | Receive goods directly (1 step) | Vendor → WH/Stock | Default. Goods go straight to shelf; office or warehouse validates one receipt |
| **Receipt, 2 steps** | Receive goods in input and then stock (2 steps) | Vendor → WH/Input → internal transfer → stock | Real unloading/checking zone, dedicated receivers, goods must not be reservable until put away |
| **Receipt, 3 steps** | Receive goods in input, then quality and then stock (3 steps) | Input → WH/Quality Control → stock | Formal inbound QC hold. Note: quality *checks* don't require this — the Quality app (Enterprise) attaches checks to any step |
| **Delivery, 1 step** | Deliver goods directly (1 step) | WH/Stock → Customer | Default. One delivery order, picked and shipped by the same person |
| **Delivery, 2 steps** | Send goods in output and then deliver (2 steps) | Pick → WH/Output → ship | Separate pickers and shippers; staging/consolidation at the dock; entry ticket for [batch picking](#picking-methods-batch-wave-cluster) |
| **Delivery, 3 steps** | Pack goods, send goods in output and then deliver (3 steps) | Pick → WH/Packing Zone → pack → ship | Distinct pick, pack and ship teams; packing station with [put-in-pack and carrier labels](#delivery-packaging--shipping-integration) |

Start-simple doctrine: 1-step both ways unless the client physically operates a staging zone *today*. If the same person picks, packs and ships, three steps means one human validating three documents per order — the classic way to make Odoo feel bureaucratic. Changing steps later is a dropdown, not a migration: Odoo creates/archives the staging locations and operation types — but every open transfer keeps its old routing and the whole team re-learns its daily queue, so change between waves, not mid-season.

**Required client info:**
- Walk the actual flow: where do goods physically pause between truck and shelf, and shelf and truck?
- Are receiving/picking/packing/shipping different people or the same person wearing hats?
- Inbound quality hold required (⇒ 3-step receipts, and is the Enterprise Quality app in scope)?
- Order lines per day per warehouse — enough volume to feed consolidation steps?

**Community edition:** the 1/2/3-step options themselves are standard `stock` and available in Community; the Quality app that makes 3-step receipts worthwhile is Enterprise-only.

**Interactions:** Steps are implemented as [routes and rules](inventory.md#routes--procurement-rules-architecture-mtobuymanufacture) — do not hand-edit the generated rules. 2/3-step deliveries create the Pick operation that [batch/wave/cluster](#picking-methods-batch-wave-cluster) optimize. Receipt handling of over/under quantities: [purchasing.md](purchasing.md#receipts--overunder-receipt-handling). Manufacturing has its own 1/2/3-step equivalent: [manufacturing.md](manufacturing.md#manufacturing-scope--mo-flow).

**Add-on impact:** No add-on overlays recorded for Odoo in this knowledge base yet.

**Default recommendation:** 1-step receipts and deliveries for most SMB go-lives; move to 2-step deliveries when a real picker/shipper split plus batch picking arrives; 3 steps only where the staging zones physically exist and are staffed.

**Risk of getting it wrong:** medium — reversible configuration, but the classic failure is going too high: users start force-validating chained transfers they don't understand, staging locations accumulate phantom stock, and trust in the system erodes. Going up a step re-trains everyone and re-papers every work instruction.

**Expertise tags:** `#warehouse` `#warehouse-complexity` `#high-stakes`

---

## Putaway rules & storage categories

**Where:** Inventory → Configuration → **Putaway Rules**; Inventory → Configuration → **Storage Categories** (field appears on location forms); prerequisites: Storage Locations + Multi-Step Routes settings.
**What it controls:** Whether Odoo suggests *where* incoming goods go. A putaway rule says: when this product / product category / package type arrives in location X, store it in sublocation Y. Storage categories add capacity logic to locations (Max Weight, capacity by product or by package type) and an **Allow New Product** policy (If location is empty / If products are the same / Allow mixed products), letting rules pick the closest suitable sublocation instead of a fixed one.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **No putaway rules** | Small crews who know their warehouse; receipt destination stays `WH/Stock` and people shelve by habit | Temporary staff, multi-zone warehouses, anything scanned — "wherever" is not scannable |
| **Putaway by product category to zones** | The 80% case: fruit to the cold zone, paint to the hazmat cage; a handful of rules, low upkeep | Per-SKU fixed bins at small scale — hundreds of product-level rules for a two-aisle warehouse is master-data theatre |
| **Putaway + storage categories (capacity, closest location)** | Bin-level warehouses with real capacity limits (pallet racking, weight-limited mezzanine) and barcode discipline | Anyone unwilling to maintain capacities and keep bin contents honest — wrong capacity data quietly misroutes every receipt |

Rule of thumb: zones pay off from day one; bins (shelf-level sublocations with capacity) only pay once scanning exists and someone owns the master data — a bin system maintained by nobody is worse than a fat zone.

**Required client info:**
- Are there segregation constraints (temperature, hazmat, quarantine) that *force* zone rules?
- Do items have fixed homes or float? Who decides today where a pallet goes?
- Real capacity limits worth encoding (rack weight, pallet positions per bay)?
- Who will own putaway/storage-category master data after go-live — a name, not a role?

**Interactions:** Putaway triggers on the receipt or the input→stock transfer depending on [receipt steps](#inboundoutbound-steps-the-complexity-ladder); package-type putaway needs the Packages feature ([inventory.md](inventory.md#packages-packaging--consignment)); suggested destinations become scan targets in [Barcode](#barcode-operations).

**Add-on impact:** None known yet — this knowledge base has no Odoo add-on layers.

**Default recommendation:** Category-to-zone putaway rules at go-live where segregation or a real zoning habit exists; defer storage categories and capacity to a phase 2 that arrives together with barcode scanning.

**Risk of getting it wrong:** low — rules are added, changed and deleted freely; the cost of a bad rule is misplaced pallets and annoyed pickers, not corrupted data.

**Expertise tags:** `#warehouse` `#locations` `#bins` `#putaway`

---

## Removal strategies (FIFO/FEFO/LIFO)

**Where:** Product category form → **Force Removal Strategy**; per location: location form → Logistics → **Removal Strategy** (needs Storage Locations + Multi-Step Routes). Category setting wins over location.
**What it controls:** *Which* units Odoo reserves when several lots/locations could satisfy a move — pure reservation logic, distinct from costing (FIFO costing lives in [inventory.md](inventory.md#routes--procurement-rules-architecture-mtobuymanufacture) territory; do not let the client conflate the two).

**Options:**

| Strategy | When it fits | When to avoid / prerequisites |
|---|---|---|
| **First In First Out (FIFO)** | Default rotation for most goods; oldest receipt reserved first | — |
| **First Expiry First Out (FEFO)** | Anything with a shelf life: food, pharma, cosmetics, adhesives | Requires Lots & Serial Numbers + **Expiration Dates** — see [inventory.md — lots & expiry](inventory.md#tracking-lots-serials--expiry); pointless without disciplined lot capture at receipt |
| **Last In First Out (LIFO)** | Rare physically-driven cases (stacked bulk where the top *is* the newest) | Anywhere rotation matters; never choose it for accounting reasons |
| **Closest Location** | Bin-level warehouses optimizing picker travel; alphanumeric location codes define "closest" | Sites without meaningful location codes — it degrades to arbitrary |
| **Least Packages** | Minimize opened boxes/pallets per order | Requires the Packages feature; verify fit against real packing behaviour before promising |

**Required client info:**
- Expiry-dated products anywhere in the assortment? (⇒ FEFO for those categories, and the lot-capture discipline that feeds it)
- Are location codes walk-ordered (⇒ Closest Location viable) or historical accidents?
- Does the client currently break multiple pallets for one order and hate it (⇒ Least Packages)?

**Interactions:** FEFO depends entirely on lot + expiry setup in [inventory.md](inventory.md#tracking-lots-serials--expiry); strategy per location interacts with [location design](#warehouse--location-design); what the picker actually takes is enforced only if [Barcode](#barcode-operations) makes them scan the suggested lot/location.

**Add-on impact:** No Odoo add-on overlays exist in this knowledge base yet.

**Default recommendation:** FIFO globally; FEFO forced on every expiry-tracked product category; consider Closest Location only after bin codes and scanning are real.

**Risk of getting it wrong:** low–medium — the setting itself changes freely and applies to future reservations, but months of FIFO-instead-of-FEFO on perishables is written-off stock the client will remember.

**Expertise tags:** `#warehouse` `#removal-strategy` `#fefo`

---

## Picking methods: batch, wave, cluster

**Where:** Inventory → Configuration → Settings → Operations → **Batch, Wave & Cluster Transfers** (requires Storage Locations + Multi-Step Routes); per operation type: **Automatic Batches** with Batch Grouping criteria; processing under Inventory → Operations → Batch Transfers.
**What it controls:** Whether pickers work order-by-order or on consolidated work: a *batch* groups whole transfers for one picker; a *wave* groups selected *lines* from different transfers (split first, then batch); *cluster* picking is a batch picked directly into one package per order (needs the Packages feature) so no post-pick sorting is needed.

**Options:**

| Method | Volume where it starts paying | When to avoid |
|---|---|---|
| **Order-by-order (no batching)** | Up to roughly 20–30 order lines/day — below that, batching is ceremony | — |
| **Batch picking** | Dozens of small orders/day, few SKUs ordered often; one warehouse walk, sort at the output area | Orders too bulky to share a cart; no output area to sort in |
| **Wave picking** | High volume with grouping logic (zone, carrier cut-off, shipping date); waves released by a coordinator | No coordinator role — waves need someone to build them |
| **Cluster picking** | Many small multi-line orders; pick straight into per-order boxes, skip sorting | Urgent single orders (can't jump a cluster); requires Packages discipline |
| **Automatic Batches (per operation type)** | Stable grouping criteria: Contact, Carrier, Destination Country, Source/Destination Location | Grouping logic that changes daily — auto-rules fight ad-hoc dispatching |

**Community edition:** batch, wave and cluster transfers are standard modules available in Community — contrary to a common assumption. What Community lacks is the [Barcode app](#barcode-operations) that makes them shine on the floor; paper batch pick lists still work.

**Required client info:**
- Order lines per day and lines per order — the arithmetic decides the method, not preference
- Is there a team lead who releases work (⇒ waves), or do pickers self-serve (⇒ auto-batches)?
- Carrier cut-off times that naturally define waves?
- Cart/tote equipment for cluster picking, and is Packages already in the design?

**Interactions:** Batching optimizes the Pick step, so 2/3-step [deliveries](#inboundoutbound-steps-the-complexity-ladder) are the natural habitat (1-step works but batches whole delivery orders); cluster picking presumes [packages](inventory.md#packages-packaging--consignment); execution on scanners: [Barcode operations](#barcode-operations).

**Add-on impact:** Nothing recorded — no Odoo add-on files exist in this knowledge base yet.

**Default recommendation:** None at go-live. Introduce batch picking when pickers visibly retrace their steps; add Automatic Batches once the grouping criterion is stable; reserve wave/cluster for genuine volume with a coordinator and scanning in place.

**Risk of getting it wrong:** low — settings toggle on and off freely; the waste is operational (over-engineered picking nobody follows), not structural.

**Expertise tags:** `#warehouse` `#batch-picking` `#picking`

---

## Barcode operations

**Where:** The **Barcode** app (separate app, **Enterprise-only**); Inventory → Configuration → Settings → Barcode section → **Barcode Scanner**, nomenclature selection, **Stock Barcode Database** (pre-fills product data from scanned GTINs); print location/command barcodes from Settings and Locations.
**What it controls:** Whether receipts, internal transfers, picks, deliveries and inventory counts are executed by scanning instead of keyboard: scan the operation, scan products/lots/locations/packages, validate on the device. Supports the default nomenclature (plain EAN/UPC) and **GS1 nomenclature** (one GS1-128 scan carries GTIN + lot + expiry + quantity — the difference between misery and flow for lot-tracked goods).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Paper first, scanner-ready design** | Go-live under time pressure, low volume; locations/lots designed so scanning is a phase 2, not a redesign | Lot/serial-heavy operations at volume — hand-keying lot numbers is the top warehouse go-live complaint |
| **Barcode app from day one** | Enterprise clients with volume, lot capture, or temp staff; accuracy enforced by scan-to-confirm | Micro-warehouses where device cost and process overhead exceed the error cost |
| **GS1 nomenclature** | Suppliers ship GS1-128/GTIN-14 labelled goods (food, pharma, logistics) | Product barcodes are internal-only EANs — default nomenclature is simpler |

Hardware: USB scanners (fixed station), Bluetooth scanners paired to a phone/tablet, or mobile computer scanners running the Odoo app (recent Android + Chrome works; verify specific devices). Wi-Fi coverage is a project prerequisite, not a detail.

**Community edition:** no Barcode app. The fallback is paper documents and manual entry in the Inventory app — workable at low volume, but if scanning is a hard requirement, that alone justifies Enterprise licensing (see [general-setup.md — edition & hosting](general-setup.md#edition--hosting-enterprise-vs-community-online-vs-odoosh-vs-on-premise)).

**Required client info:**
- Are supplier barcodes present and reliable — GTIN on units *and* cases? GS1 labels with lot/expiry?
- Lot/serial captures per day (the volume that makes scanning non-optional)
- Wi-Fi coverage in the warehouse; device budget; who maintains devices?
- Enterprise licensing confirmed? This feature alone often decides the edition question

**Interactions:** Scanners execute whatever the [step design](#inboundoutbound-steps-the-complexity-ladder) and [picking methods](#picking-methods-batch-wave-cluster) define — change those later and device workflows change too; location barcodes come from [location design](#warehouse--location-design); lot/expiry capture rules from [inventory.md](inventory.md#tracking-lots-serials--expiry); counts via the app feed [cycle counting](inventory.md#inventory-adjustments--cycle-counting).

**Add-on impact:** None known yet in this knowledge base's Odoo layer.

**Default recommendation:** Decide scanning during design, not after go-live. Enterprise + lot tracking + real volume ⇒ Barcode app from day one with GS1 where suppliers support it; otherwise paper-but-scanner-ready.

**Risk of getting it wrong:** medium — nothing irreversible in configuration, but a go-live that assumed manual lot keying at volume fails loudly in week one, and retrofitting scanning re-opens the step and location design.

**Expertise tags:** `#warehouse` `#barcode` `#hardware`

---

## Internal transfers & inter-warehouse resupply

**Where:** Inventory → Operations → **Internal Transfers** (an operation type per warehouse); warehouse form → **Resupply From** checkboxes (visible with multiple warehouses; generates a "Supply Product from …" route per pair); Transit-type locations for goods between warehouses/companies.
**What it controls:** How stock moves inside and between warehouses: ad-hoc internal transfers within one warehouse, and structured inter-warehouse replenishment where a route chains an outbound move at the supplying warehouse and an inbound at the receiving one, met in transit.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Internal transfers (same warehouse)** | Location-to-location moves: replenish pick faces, quarantine, re-zoning | Using them *between* warehouses ad hoc when a resupply route should exist — invisible to planning |
| **Resupply From routes + reordering rules** | Branch/shop warehouses topped up from a central warehouse on min/max | One-off moves — a route per pair is structure, not a favour |
| **Resupply From routes + MTO** | Each customer order at the branch pulls specifically from central | Stocked fast-movers — MTO chains every order to a transfer and multiplies documents |
| **Inter-company transit (multi-company)** | Each company owns its warehouse; stock crosses a company boundary through transit with an intercompany sale/purchase | Same-company sites — keep one company and use plain resupply. See [general-setup.md — company structure](general-setup.md#company-structure-one-company-vs-multi-company). ⚠ Verify the intercompany flow details against current Odoo documentation |

**Required client info:**
- Which site replenishes which, and on what trigger — min/max stock (⇒ reordering rules) or per order (⇒ MTO)?
- Transport time between sites — does finance need goods-in-transit visibility (transit location stock is still owned)?
- Are the sites one legal entity or several (changes the design entirely)?
- Who validates the receiving end — a person at the branch, or should it auto-validate? (process question before config question)

**Interactions:** Resupply routes are ordinary [route/rule machinery](inventory.md#routes--procurement-rules-architecture-mtobuymanufacture) — same debugging skills apply; each leg respects the warehouse's [step settings](#inboundoutbound-steps-the-complexity-ladder); reordering rules live with [inventory planning](inventory.md#routes--procurement-rules-architecture-mtobuymanufacture); multi-company boundaries: [general-setup.md](general-setup.md#company-structure-one-company-vs-multi-company).

**Add-on impact:** None yet — the Odoo knowledge layer has no add-on overlays.

**Default recommendation:** Internal transfers freely within a warehouse; Resupply From + reordering rules as the standard branch-replenishment pattern; MTO between warehouses only for genuine order-driven flows; involve the accountant before designing anything inter-company.

**Risk of getting it wrong:** medium — routes can be reconfigured, but a mis-designed multi-company flow leaves intercompany stock and invoices to untangle, and undisciplined ad-hoc transfers between warehouses starve the receiving site's planning.

**Expertise tags:** `#warehouse` `#transfers` `#multi-site`

---

## Delivery packaging & shipping integration

**Where:** Inventory → Configuration → Settings → Operations → **Packages** (enables **Put in Pack** on transfers); Package Types (dimensions/weight per box type); Inventory → Configuration → **Delivery Methods**; per operation type: Print on "Put in Pack", **Connect Scale** (IoT); carrier connectors configured per Shipping Method (Provider field).
**What it controls:** The last metres: grouping picked items into packages, telling the carrier what ships, and getting a label back. Connectors (Odoo 19 documents DHL Express, FedEx, UPS, USPS, Sendcloud, **bpost**, Shiprocket, Starshipit, Easypost, Envia) fetch real-time rates, push shipments and print labels on delivery validation.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **No packages, manual shipping** | Few parcels/day; labels typed in the carrier portal | Any real parcel volume — double entry breeds address errors |
| **Packages + package types, delivery methods with fixed/rule-based prices** | Charge shipping on orders without carrier integration; package weights feed the pricing rules | Clients expecting live carrier rates — static rules drift from reality |
| **Carrier connector (label printing, tracking)** | Daily parcel flows; Belgian clients: bpost and Sendcloud (ships from Belgium) are the usual candidates | Carriers without a connector — check the current connector list before promising anything |
| **Scale integration (Connect Scale, IoT)** | Weight-billed carriers, high parcel volume | Small flows — an IoT box for five parcels a day is gadgetry |

**Community edition:** the base Delivery Methods feature (fixed and rule-based pricing) is available; the carrier connectors (bpost, Sendcloud, DHL, UPS, FedEx, …) are Enterprise-only modules. Community fallback: manual labels in the carrier's own portal.

**Required client info:**
- Parcels per day and which carriers under contract — negotiated rates or a broker like Sendcloud?
- Should the customer pay real carrier cost, a flat fee, or free-above-threshold ([sales.md — delivery methods](sales.md#delivery-methods--shipping-connectors) owns the pricing side)?
- Standard box sizes worth defining as package types? Actual weighing at the pack bench?
- Where do labels print — pack station printer, and is 3-step delivery the trigger point?

**Interactions:** Put-in-pack presumes the Packages feature ([inventory.md](inventory.md#packages-packaging--consignment)); the pack step of [3-step deliveries](#inboundoutbound-steps-the-complexity-ladder) is the natural label-printing moment; [cluster picking](#picking-methods-batch-wave-cluster) packs during the pick; delivery method pricing and sales-side setup: [sales.md](sales.md#delivery-methods--shipping-connectors).

**Add-on impact:** No add-on overlays known — none recorded for Odoo in this knowledge base.

**Default recommendation:** Packages + package types plus one carrier connector (bpost or Sendcloud for most Belgian SMBs) as soon as parcel volume is daily; rule-based delivery pricing until then; test label formats with real printers during UAT, not after.

**Risk of getting it wrong:** low — all reversible configuration; the traps are commercial (connector rates vs. negotiated contract rates — verify per carrier) and operational (labels that print in the wrong format on go-live morning).

**Expertise tags:** `#warehouse` `#shipping` `#packages` `#carriers`
