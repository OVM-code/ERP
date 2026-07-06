# Logistics & Planning — Aptean Food & Beverage ERP

> **Add-on:** Aptean Food & Beverage ERP (Business Central embedded)
> **Base ERP:** Microsoft Dynamics 365 Business Central
> **Last reviewed:** 2026-07

This area covers getting food out the door and onto trucks with trace intact: **Logistics (LOG)** with the Route Planning worksheet (route planning numbers/drives, logistics data on sales orders, warehouse documents inheriting route data), **Transport (TRA)** with transport orders, route assignments per customer/vendor/location and trip numbering, optional **Aptean TMS** for routing/sequencing/scheduling, **License Plating (LPL)** to trace logistic transactions to a licence plate (pallet/case/mixed lot), **SSCC (SSC)** for GS1 serial shipping container codes, and the **Mobile Warehouse app (MWR)** with GS1 barcode parsing and SSCC handling incl. for lot-tracked and licence-plate-tracked items. Forecasting extensions round out planning. Prime territory for food distributors and any manufacturer running own fleet or retail DC compliance (SSCC-labelled pallets, ASN/DESADV).

---

## Changes to standard setup decisions

### Modifies: Shipping agent & delivery setup ([standard file](../../erp/business-central/sales.md#shipping-setup-shipment-methods-shipping-agents-order-promising--atpctp))

**How it changes:** extends/replaces for route-delivered customers. Standard BC shipping agents/services remain for parcel/3PL flows, but customers on fixed delivery routes get route assignments (customer × weekday → route), and sales orders carry logistics data that flows into route planning and delivery documents.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Shipping agent + service per order | yes | Keep for carrier/parcel shipments outside own-fleet routes. |
| Promised delivery date managed manually per order | changed | For routed customers, deliverable dates follow from the route calendar (Tuesday/Friday route = Tuesday/Friday delivery); order entry should validate against it. |
| No structured delivery scheduling | no (for route businesses) | The point of the module is replacing the whiteboard. |

### Modifies: Warehouse shipment process ([standard file](../../erp/business-central/warehouse.md#warehouse-document-flow-toggles))

**How it changes:** extends. Warehouse shipments/receipts inherit fields from route planning numbers, so picking and staging organise by route/trip and stop sequence rather than per order; SSCC numbers are generated/managed on warehouse shipments.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Ship per sales order | yes, for non-routed flows | Routed flows pick/stage per route with drop-sequence awareness. |
| Combined shipments ad hoc | changed | Route planning formalises consolidation; ad-hoc combining works against trip building. |

### Modifies: Bin/put-away and inventory registration granularity ([standard file](../../erp/business-central/warehouse.md#location-design))

**How it changes:** extends. License plating introduces the pallet/handling unit as a first-class object: moves, picks and shipments can act on a licence plate (everything on it) instead of item+lot+bin lines. This changes how you decide bin granularity and mobile flows.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Bin content by item/lot only | yes | Fine without LPL; with LPL the plate carries the content and one scan moves the pallet. |
| Directed put-away & pick | yes | Combines well with LPL; but LPL also adds value in simpler location configurations. |

### Modifies: Demand forecasting & planning parameters ([standard file](../../erp/business-central/manufacturing.md#planning-setup-mps-vs-mrp-parameters-forecasts))

**How it changes:** extends. Standard BC demand forecasts and reordering policies still drive MPS/MRP, but food adds short shelf life (you cannot pre-build stock beyond expiry), day-of-week demand patterns and promotion uplifts. Aptean provides forecasting support in this direction; treat specifics as version-dependent.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Reorder-point policies on finished goods | yes, constrained | Only where shelf life comfortably exceeds replenishment cycle; useless for day-fresh goods. |
| Single monthly demand forecast | changed | Fresh operations need day-of-week-level patterns and promo-aware uplifts; monthly buckets hide everything that matters. |

> ⚠️ Verify against current Aptean documentation — forecasting extension scope varies by edition; written from general product knowledge.

---

## New setup decisions introduced by this module

### Route model: fixed routes vs. dynamic trip planning

**Where:** LOG — Route Planning worksheet (route planning numbers, drives); TRA — transport route assignments (customers/vendors/locations), transport setup incl. Trip No. feature toggle
**What it controls:** whether deliveries follow a fixed route calendar (route per weekday with assigned customers, orders auto-flow to their route) or are planned dynamically per day into trips; and whether trip numbering is used to group transport orders into vehicle departures.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Fixed routes + route assignments per customer/weekday | Food distribution with stable delivery days (foodservice, retail drops) — the classic model | Highly variable ship-to patterns (project/spot business) |
| Dynamic trip building in the Route Planning worksheet per day | Mixed/fluctuating volumes; seasonal businesses | If planners lack time/skill for daily planning — fixed routes are self-running |
| Full TMS (Aptean TMS or third-party) for routing/sequencing/scheduling | Larger fleets, time-window pressure, fuel/route optimisation goals | Small fleets (< ~5 trucks) — worksheet planning is enough; TMS is its own project |

**Required client info:**
- Fleet size, own vs. contracted; delivery-day agreements with customers (the real ones, incl. exceptions)
- Order cut-off times vs. departure times — this drives the whole order-to-dispatch timeline design
- Time windows/dock bookings at key customers (retail DCs)

**Interactions:** route calendar constrains order-entry date promising (above); picking waves organise per route; catch weight dispatch weighing and SSCC labelling must fit inside the cut-off-to-departure window — time-budget the dock, not just the software.
**Default recommendation:** fixed routes with weekday assignments for distribution clients, worksheet-level daily adjustment; evaluate TMS only after six months of stable base operation.
**Risk of getting it wrong:** medium — route models are changeable, but a cut-off/departure design that doesn't fit physical dock throughput shows up as missed trucks in week one.
**Expertise tags:** `#aptean-fnb` `#logistics` `#routes` `#transport`

### Transport order & trip administration

**Where:** TRA — transport orders (shipping info: address, delivery date, load type), trip numbers grouping departures
**What it controls:** whether a transport document layer separate from warehouse shipments is used: transport orders carry the delivery/load information, trips bundle them per vehicle departure, and driver documents (load list, delivery notes per stop in drop order) generate from it.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Transport orders + trips for own-fleet deliveries | Own trucks, multi-drop, returnables/empties handling | Pure carrier shipping — the carrier's system does this |
| Warehouse shipment only, no transport layer | Simple single-drop, carrier-collected flows | Multi-drop own fleet — you'll rebuild trip lists in Excel |

**Required client info:**
- Driver document requirements (drop-sequenced delivery notes, load list, temperature docs, empties/returnables per stop)
- Cash-on-delivery or driver-collected returns? (drives what the driver must record)

**Interactions:** trips consume route planning output; load type interacts with load planning (below); returnable packaging (crates, kegs, pallets) per stop is a Drink-IT-heritage strength — scope it explicitly if relevant.
**Default recommendation:** transport orders + trip numbers for any own-fleet multi-drop operation; keep carrier flows on standard shipping agents.
**Risk of getting it wrong:** low-medium — additive layer, adjustable; skipping it where needed just leaves manual work in place.
**Expertise tags:** `#aptean-fnb` `#transport` `#logistics`

### Load planning & vehicle capacity

**Where:** route/trip level — load building against vehicle constraints (weight, pallet places/volume, temperature compartments); Route Load List processing per route planning number
**What it controls:** whether trips are validated against vehicle capacity and compartment constraints (frozen/chilled/ambient on one truck) when orders are assigned.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Capacity-checked load planning (weight/pallet places) | Full trucks, mixed-temperature fleets | Trivially under-utilised vehicles — checks without a binding constraint are noise |
| Planner judgement, no system check | Small operations, experienced dispatchers | Growth situations — the tribal-knowledge dispatcher is a single point of failure |

**Required client info:**
- Vehicle list with real capacities per compartment/temperature zone
- Pallet-place accounting conventions (do half pallets count? stacking rules?)

**Interactions:** order-size promotions ([trade-and-pricing.md](trade-and-pricing.md)) change drop sizes — trade and logistics must agree; catch weight gives actual load weights only after picking, so plan against nominal and verify at close.
**Default recommendation:** weight + pallet-place checks per trip for full-truck operations; temperature-compartment modelling only if the fleet is genuinely multi-temp.
**Risk of getting it wrong:** low — planning-quality issue, recoverable.
**Expertise tags:** `#aptean-fnb` `#load-planning` `#transport`

> ⚠️ Verify against current Aptean documentation — Route Load List handling is documented in the AOW/warehouse docs; compartment/capacity mechanics vary by edition, written partly from general product knowledge.

### License plating scope (LPL)

**Where:** Aptean License Plating extension — licence plates for pallets, cases or mixed lots; generate own plates and/or record supplier-applied plates by scanning
**What it controls:** where the handling unit (pallet) becomes the tracked object: which locations/flows use plates, whether inbound supplier plates are adopted, and which items are plate-tracked vs. lot-only.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Full LPL in the DC (receipt → put-away → pick → ship on plates) | Pallet-in/pallet-out distribution, high-volume DCs — one scan per pallet instead of per line | Piece-picking-dominated operations with broken-case work (plates help less at the pick face) |
| LPL on finished-goods pallets only (production pack-off → dispatch) | Manufacturers palletising own output | — a good phase 1 |
| No LPL, lot-level only | Small warehouses, low pallet volumes | Retail-DC customers demanding SSCC pallet labels — plates and SSCC go together naturally |

**Required client info:**
- Share of full-pallet vs. broken-case movements; whether suppliers ship SSCC/plate-labelled pallets worth adopting inbound
- Label printing infrastructure at receipt and pack-off (plates need printers where plates are born)

**Interactions:** plate ↔ SSCC (a shipped plate typically carries the SSCC); Mobile Warehouse supports SSCC operations for both lot-tracked and licence-plate-tracked items; recall speed improves materially when trace resolves to plates on specific trips.
**Default recommendation:** LPL for finished-goods pallets and full-pallet flows first; extend to inbound adoption where supplier labels are reliable.
**Risk of getting it wrong:** medium — retrofitting plating into a live warehouse is disruptive; but over-scoping into broken-case areas creates scan burden without payback.
**Expertise tags:** `#aptean-fnb` `#license-plating` `#warehouse`

### SSCC & GS1 labelling strategy

**Where:** SSC extension — SSCC generation/management incl. on warehouse shipments; MWR — GS1-128 barcode parsing (GTIN, lot, expiry, weight, SSCC) and SSCC operations
**What it controls:** whether the client issues GS1 SSCC codes on outbound logistic units (own GS1 company prefix), captures supplier SSCCs inbound, and which GS1 application identifiers its labels carry.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Outbound SSCC on every shipped pallet + GS1-128 labels | Retail DC supply (usually mandated, with DESADV/ASN), export | No customer requires it and no internal trace benefit sought — cost without driver |
| Inbound SSCC/GS1 capture (scan supplier labels) | Suppliers label compliantly — one scan populates item, lot, expiry, weight | Suppliers without labels — don't build receiving around scans that won't exist |
| Both directions | Mid-size and up food distribution/manufacturing — the end state | — |

**Required client info:**
- GS1 membership/company prefix (apply early — lead time); customer label specs and ASN requirements (get the retailer spec documents)
- Supplier label quality survey — physically scan a sample week of receipts before designing the inbound flow

**Interactions:** SSCC pairs with licence plates; DESADV/ASN EDI messages reference SSCCs (coordinate with the EDI workstream); FSMA 204/retailer trace programs increasingly assume case/pallet-level GS1 identification.
**Default recommendation:** outbound SSCC wherever a retail customer mandates it (non-negotiable anyway); inbound GS1 parsing for the top suppliers by receipt volume with compliant labels.
**Risk of getting it wrong:** medium — label non-compliance triggers retailer fines/refusals; inbound is merely opportunity cost.
**Expertise tags:** `#aptean-fnb` `#sscc` `#gs1` `#edi`

### Mobile warehouse deployment scope (MWR)

**Where:** Aptean Mobile Warehouse app + BC setup per location/flow
**What it controls:** which warehouse processes run on scanners: receipt (with GS1 parse), put-away, movement, pick, shipment/SSCC, production supply, physical inventory.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| All flows mobile from go-live | Greenfield warehouses, strong site leadership | Big-bang on a struggling site — sequence instead |
| Inbound + outbound first, internal moves later | Most implementations — captures lot/expiry/weight/SSCC where it matters most | — |
| Paper long-term | Never for lot-tracked food stock | Transcription is where trace dies; see [lot-management-traceability.md](lot-management-traceability.md) |

**Required client info:**
- Device fleet, Wi-Fi coverage (freezers!), glove/cold-store usability needs
- Volume per flow to size number of devices and printer placement

**Interactions:** the same device estate typically serves QC app and Shop Floor Production — one hardware/MDM project; every lot/expiry/weight/SSCC decision in the other modules lands on these scanners, so MWR scope is effectively the delivery vehicle for the whole vertical's data quality.
**Default recommendation:** inbound and outbound flows mobile at go-live, internal moves and physical inventory in wave 2.
**Risk of getting it wrong:** medium — recoverable, but under-provisioned devices produce queueing, and queueing produces workaround culture.
**Expertise tags:** `#aptean-fnb` `#mobile-warehouse` `#adoption`

### Forecasting model for short shelf-life demand

**Where:** demand forecast setup (standard BC forecast + Aptean forecasting extensions where licensed)
**What it controls:** forecast granularity (item/variant/location, daily vs. weekly buckets), whether day-of-week patterns and promotion uplifts are modelled, and how forecast drives production planning for fresh goods.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Daily-bucket forecast with day-of-week profiles | Fresh/short-shelf-life production (bakery, chilled) | Long-shelf-life ambient goods — weekly is fine and cheaper to maintain |
| Weekly forecast + reorder policies | Ambient distribution assortment | Day-fresh goods — weekly buckets guarantee simultaneous waste and stock-outs |
| Promo-adjusted forecasting (uplift per promotion) | Promotion-heavy retail suppliers | Before base-line forecast discipline exists |

**Required client info:**
- Shelf life vs. production/replenishment lead time per category (the ratio dictates required forecast granularity)
- Where forecasting lives today (often the production planner's spreadsheet — understand it before replacing it)
- Waste numbers by category — the business case and the baseline

**Interactions:** promotion calendar ([trade-and-pricing.md](trade-and-pricing.md)) must feed forecast uplifts; expiry logic makes over-forecasting immediately visible as waste; route/delivery-day patterns shape demand timing.
**Default recommendation:** daily day-of-week-profiled forecasting for fresh categories, weekly for ambient; measure forecast accuracy and waste from day one so tuning is evidence-based.
**Risk of getting it wrong:** medium — tunable, but for fresh producers forecast quality *is* the margin; treat it as an ongoing process with an owner, not a setup task.
**Expertise tags:** `#aptean-fnb` `#forecasting` `#planning` `#fresh`

> ⚠️ Verify against current Aptean documentation — LOG/TRA/LPL/SSC/MWR capabilities are grounded in Aptean's public docs; TMS scope, load-planning depth and forecasting extensions vary by edition and are partly written from general product knowledge.
