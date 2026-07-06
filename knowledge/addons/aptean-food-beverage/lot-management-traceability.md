# Lot Management & Traceability — Aptean Food & Beverage ERP

> **Add-on:** Aptean Food & Beverage ERP (Business Central embedded)
> **Base ERP:** Microsoft Dynamics 365 Business Central
> **Last reviewed:** 2026-07

Extends BC's standard item tracking with food-grade lot control: lot numbering profiles, quality/attribute data registered per lot, vendor lot capture, expiry and minimum-shelf-life logic (Aptean Expiration Management, EXM), FEFO refinements, end-to-end trace (farm-to-fork) and structured recall management (Aptean Lot Management, LMT). Every food client on this product uses this module — it is the reason they bought the vertical. The real consulting work is not turning it on; it is choosing a traceability granularity the shop floor can actually sustain.

---

## Changes to standard setup decisions

### Modifies: Item tracking code design ([standard file](../../erp/business-central/inventory.md#item-tracking-lot--serial--package))

**How it changes:** extends. Standard BC item tracking codes (lot/serial, SN/lot-specific tracking, expiry requirement) remain the underlying mechanism, but Aptean layers lot profiles, lot attribute registration and vendor-lot capture on top. You no longer decide "lot tracking yes/no" per item family in isolation — you decide it together with a lot numbering profile and an expiry regime.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| No tracking | yes, but rare | Only for true non-food items (consumables, packaging where no recall exposure). Any ingredient or sellable food item should be lot-tracked — a recall without lot data is a full-inventory recall. |
| Lot tracking, manual lot numbers | changed | Manual entry stays possible but is superseded by lot number profiles that generate lots by rule; manual-only entry undermines consistency reporting depends on. |
| Serial tracking | yes | Unusual in food; occasionally for equipment/returnable assets. Not extended by this module. |
| Expiration date required (standard BC) | changed | Standard BC has a single expiration date + expiration calculation. EXM adds best-before vs. use-by semantics, minimum shelf life for purchase and for sales per customer, and warning/error behaviour — decide the regime here, not just the flag. |

### Modifies: Picking method / FEFO ([standard file](../../erp/business-central/warehouse.md#put-awaypick-worksheets--warehouse-employees))

**How it changes:** constrains and extends. Standard BC "Pick according to FEFO" remains the base switch, but EXM adds sales-expiration logic (expiry minus the customer's required residual shelf life) and the ability to exclude specific lots from FEFO proposals (e.g. a lot reserved for a tolerant customer or channel).

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| FIFO picking (no FEFO) | no (practically) | With expiry-dated stock, not using FEFO wastes the module. Only acceptable in single-day-stock cross-dock operations. |
| FEFO on expiration date | changed | FEFO should operate against *sales* expiration (expiry minus customer minimum shelf life), not raw expiry — otherwise you pick stock the customer will reject at the dock. |
| Manual lot selection by picker | yes, constrained | Still possible, but Aptean warnings/errors on shelf-life violations should be configured so manual picks can't silently ship short-dated stock. |

### Modifies: Location & bin mandatory decisions ([standard file](../../erp/business-central/warehouse.md#location-design))

**How it changes:** constrains. Trace quality depends on where lot registration happens. If locations run without warehouse documents and without bin content, lot capture happens at posting time by office staff — which is where vendor lot numbers get lost. Directed put-away is not required, but *some* structured receiving flow (warehouse receipt or the Mobile Warehouse app) is strongly recommended so the person physically seeing the pallet records the vendor lot and production date.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Basic location (no WMS documents) | yes, discouraged | Works, but lot/expiry capture becomes a back-office transcription task; error rate is the recall risk. |
| Warehouse receipts/shipments | yes | Recommended minimum for lot-tracked food stock. |
| Directed put-away & pick | yes | Combine with Aptean AWM/License Plating for pallet-level trace (see [logistics-and-planning.md](logistics-and-planning.md)). |

---

## New setup decisions introduced by this module

### Lot numbering strategy (lot number profiles)

**Where:** Aptean Lot Management — Lot No. Profiles (assigned to items/item categories)
**What it controls:** how internal lot numbers are generated (structure, date components, sequence), and how expiration is derived when a lot is created — from the item tracking line if entered, or from the item's expiration calculation when "require expiration date" is off.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Date-based internal lot (e.g. production/receipt date encoded) | Most manufacturers — human-readable, sorts naturally, supports day-level trace | When regulators/customers mandate GS1 or a group-wide scheme that conflicts |
| Sequential internal lot | High-volume, label-driven environments where the number is only ever scanned | Where operators must eyeball lots on the floor — dates in the number prevent mistakes |
| Adopt vendor lot as internal lot | Pure distribution, goods resold unopened | Any manufacturing or repacking — vendor lots collide across vendors and break uniqueness assumptions |

**Required client info:**
- Existing lot number conventions (labels already printed, customer requirements, GS1 membership)
- Whether goods are resold untouched vs. transformed (determines vendor-lot adoption vs. cross-reference)
- Number of production lines/shifts (does the lot number need to distinguish them?)

**Interactions:** recall scope (below) is only as good as lot granularity; barcode/GS1 parsing in Mobile Warehouse populates lot + expiry from the label at receipt; catch weight tolerances are checked per lot.
**Default recommendation:** internal date-based lot profile per item category; always *record* the vendor lot number as a reference on receipt rather than adopting it as the internal lot.
**Risk of getting it wrong:** high-irreversible — lot numbers are stamped into every ledger entry, label and customer document from day one; a scheme change mid-life fragments trace history.
**Expertise tags:** `#aptean-fnb` `#lot-management` `#traceability`

### Traceability granularity vs. registration burden

**Where:** combination of lot profile frequency (per receipt / per production batch / per day), item tracking codes, and warehouse/shop-floor registration flows
**What it controls:** how narrow a recall can be cut, and how much scanning/typing the floor does every hour to earn that.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Lot per receipt line / per production batch (finest) | High-risk categories (RTE, meat, dairy, infant), retailers demanding batch-level trace | Low-risk, high-velocity commodity flows where the floor will not sustain the discipline |
| Lot per production day per line | Bakeries, beverage, most mid-market manufacturers — the pragmatic default | When one bad ingredient sub-lot must not condemn a full day's output (expensive proteins) |
| Lot per delivery/PO (coarse, distribution) | Distributors passing sealed cases through | Anyone opening, blending or repacking product |

**Required client info:**
- Regulatory regime and customer audit requirements (BRC/IFS/SQF, FSMA 204 traceability list items, EU 178/2002)
- Cost of an over-wide recall for their product (value density) vs. labour available for registration
- Realistic floor discipline: are there scanners, or paper and one office admin?

**Interactions:** quality-control checks are dispatched per lot; catch weight registers weight per lot; one-up/one-back tracing in LMT assumes consumption postings actually name the lot consumed — flushing methods that guess (backward flush against FEFO assumption) quietly corrupt trace accuracy.
**Default recommendation:** lot per production day per line for manufactured goods, lot per receipt for ingredients; tighten only the categories where recall economics justify it. Never promise "unit-level trace" in a demo.
**Risk of getting it wrong:** high — too coarse and a recall takes out weeks of production; too fine and the floor invents workarounds (one lot re-used all day) that destroy trace integrity while looking compliant.
**Expertise tags:** `#aptean-fnb` `#traceability` `#recall` `#adoption`

### Expiration regime per item category (Expiration Management, EXM)

**Where:** Aptean Expiration Management setup + item-level expiration fields
**What it controls:** how expiry/best-before is calculated, and the minimum-shelf-life rules: on purchase, a warning/error when (posting date + minimum purchase shelf life) exceeds the received lot's expiry; on sales, a *sales expiration date* per lot = expiry minus the minimum sales shelf life the customer requires.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Expiry auto-calculated from production/receipt date (expiration calculation formula) | Manufactured items with stable shelf life | Items where the vendor's printed date governs (then require entry at receipt) |
| Required manual expiry entry at receipt (from label/GS1 scan) | Purchased/traded goods | High-volume receiving without scanning — typing dates all day breeds errors |
| Minimum shelf-life rules as **warning** | Ramp-up phase; flexible customer base | Retail customers with hard dock rejection rules — a warning gets clicked through |
| Minimum shelf-life rules as **error** (hard block) | Retail supply with chargebacks for short-dated delivery | Businesses that deliberately sell short-dated stock to secondary channels (block would force constant overrides) |

**Required client info:**
- Per customer (or customer group): required residual shelf life at delivery — get this from the sales team in writing, it drives sales expiration
- Per item category: shelf life, best-before vs. use-by, whether vendor date or own calculation governs
- Whether short-dated stock has a legitimate secondary channel (discounters, staff shop, donation)

**Interactions:** drives FEFO (pick by sales expiration, exclude lots below threshold); quality control can release or extend holds near expiry; short-dated stock policy connects to trade & pricing (clearance price rules).
**Default recommendation:** auto-calculate for own production, mandatory scan/entry for purchased goods; start minimum-shelf-life checks as warnings during stabilisation, flip to errors for retail customers once master data (customer shelf-life demands) is verified.
**Risk of getting it wrong:** medium — recoverable in setup, but wrong customer shelf-life data produces either rejected deliveries (too lax) or phantom stock-outs where saleable stock is invisible to FEFO (too strict).
**Expertise tags:** `#aptean-fnb` `#expiration` `#shelf-life` `#fefo`

### Lot attributes / lot information scope

**Where:** Aptean Lot Management — lot information card / lot attributes
**What it controls:** which data is registered against each lot beyond dates: origin (farm/field/vessel, country), grade, brix/fat/protein values, certificates (organic, MSC), vendor lot and production date.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Minimal (vendor lot + dates only) | Distribution, low-spec products | Anyone claiming origin/certification on labels or specs |
| Origin + certification attributes | Fresh produce, organic, fish (catch area), meat (birth/rearing/slaughter chain) | — this is legally driven; if the claim exists, the attribute must |
| Full quality-value attributes per lot | When lot values drive pricing/settlement (protein % on milk, brix on fruit) or customer CoAs | If Quality Control module captures the same values — decide *one* master (usually QC results feed lot attributes, not double entry) |

**Required client info:**
- Label and spec claims that must be substantiated per lot (origin, organic, welfare schemes)
- Which lot values feed pricing or grower settlement
- Who registers each attribute and at which step (receipt, QC, production)

**Interactions:** quality-control results should populate lot data rather than parallel registration; attributes appear on trace and CoA outputs; commodity settlement (trade & pricing) may read lot values.
**Default recommendation:** register what you must prove or pay on — nothing else. Every attribute is a field someone fills 200 times a day.
**Risk of getting it wrong:** low-medium — attributes can be added later; retrofitting historic lots is the pain.
**Expertise tags:** `#aptean-fnb` `#lot-attributes` `#master-data`

### Recall management process design

**Where:** Aptean Lot Management — Manage Recalls (trace + recall documents: purchase return orders, sales credit memos, corrective actions)
**What it controls:** how a recall/withdrawal is executed in-system — tracing affected lots one-up/one-back, identifying customers/vendors touched, generating corrective documents, and evidencing the exercise for auditors.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Full in-system recall (trace + generated return orders/credit memos) | Clients wanting one auditable thread from trace to financial correction | Very early go-live phase before postings are trustworthy |
| Trace in-system, execute commercially outside | Complex recalls involving insurers/lawyers where documents are negotiated | Don't let this become permanent — the trace-to-document link is the module's value |

**Required client info:**
- Regulatory notification deadlines they face (e.g. 24h) — this sets the target time for a mock recall
- Who owns recall execution (QA vs. supply chain vs. finance) — maps to permissions
- Certification requirement for mock recall frequency (BRC/IFS typically annual minimum)

**Interactions:** depends entirely on lot granularity and registration discipline above; QC holds are the *preventive* twin (block before shipping) — see [quality-control.md](quality-control.md).
**Default recommendation:** configure full in-system recall and run a **timed mock recall before go-live sign-off** (ingredient → all customers shipped, and finished lot → all ingredient vendors). If the mock recall takes more than a couple of hours, fix registration, not the report.
**Risk of getting it wrong:** high — you find out during a real incident, with regulators watching.
**Expertise tags:** `#aptean-fnb` `#recall` `#compliance` `#testing`

> ⚠️ Verify against current Aptean documentation — written from Aptean public docs (fnbdocs.apteancloud.com: LMT, EXM, MWR modules) plus general product knowledge; exact page/field names for lot profiles and recall documents are partner-gated.
