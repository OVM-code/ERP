# Catch Weight — Aptean Food & Beverage ERP

> **Add-on:** Aptean Food & Beverage ERP (Business Central embedded)
> **Base ERP:** Microsoft Dynamics 365 Business Central
> **Last reviewed:** 2026-07

The Aptean Catch Weight extension (CAW) adds **dual unit of measure** handling through the whole supply chain: items are counted and handled in units (boxes, crates, carcasses, wheels) but priced, costed and invoiced by their *actual* weight, which naturally varies per unit. Core for meat, fish, cheese, whole produce and any protein processor. Rule one of catch weight consulting: **only give an item catch weight if the client can actually weigh it at the points where the system will ask for a weight.** No scales at dispatch = no catch weight at dispatch, however much the demo impressed them.

---

## Changes to standard setup decisions

### Modifies: Item units of measure design ([standard file](../../erp/business-central/inventory.md#units-of-measure-design))

**How it changes:** extends/replaces for affected items. Standard BC UoM assumes fixed conversion factors (1 box = 10 kg, always). CAW breaks that assumption for designated items: the unit count and the weight are captured independently per transaction (and per lot), with the fixed factor kept only as a *nominal* conversion for planning.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Single UoM, sell what you stock | yes | For fixed-weight items — most of the assortment usually stays standard. Do not catch-weight-enable items that don't need it. |
| Multiple UoMs with fixed conversion | changed | Becomes the *nominal* weight for catch weight items; actual weight per transaction overrides it for value. Fixed-conversion sales of variable product ("we just invoice 10 kg per box") is exactly what CAW replaces — but it remains the right choice when weighing infrastructure is absent. |
| Base UoM = KG for weight-priced items | changed | With CAW you normally keep a piece/box handling UoM *and* a weight pricing UoM instead of forcing everything to KG and losing unit counts. |

### Modifies: Costing method & valuation ([standard file](../../erp/business-central/finance.md#inventory-posting-groups-and-inventory-posting-setup))

**How it changes:** constrains. Inventory value for catch weight items follows actual weights, so cost per handling unit varies. Costing method choices made for the rest of the assortment still apply, but expect unit-cost variability and make sure controlling understands that margin per box moves with weight.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| FIFO / Average costing | yes | Both workable; average per weight unit is easiest to explain to finance. |
| Standard costing | yes, with care | Standard cost per weight unit is fine; standard cost per *box* fights the whole concept — variances become noise. |
| Specific (serial) costing | no (practically) | Not relevant for catch weight flows. |

### Modifies: Sales price setup ([standard file](../../erp/business-central/sales.md#sales-pricing-model-price-lists-vs-legacy-sales-prices-discount-hierarchy))

**How it changes:** extends. Prices for catch weight items are maintained per weight UoM; the invoiced amount = actual shipped weight × price, while order lines are entered in handling units. Quotes/order confirmations show nominal weight until actuals are captured.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Price per sales unit (box/each) | yes, for fixed-weight items | For CW items this systematically gives margin away on light boxes or overcharges on heavy ones. |
| Price per KG with fixed conversion | changed | Replaced by price per KG against *actual* weight. |

### Modifies: Warehouse registration flows ([standard file](../../erp/business-central/warehouse.md#warehouse-document-flow-toggles))

**How it changes:** constrains. Every inventory-affecting posting of a CW item needs a weight: receipt, put-away is fine unit-based, but shipment, production consumption/output, reclassification and physical inventory all ask for actual weights. This dictates where scales (or label scanning of pre-printed weight labels) must exist.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Post from order lines (no warehouse docs) | yes, discouraged | Weight entry lands on office staff copying paper — the classic source of weight errors and invoice disputes. |
| Warehouse receipt/shipment + Mobile Warehouse app | yes, recommended | Capture weight at the physical event: scale entry, GS1 label scan (weight in barcode), or connected scales. |

---

## New setup decisions introduced by this module

### Catch weight item scope

**Where:** Item card — catch weight setup (per item)
**What it controls:** which items are dual-UoM. Everything downstream (weight prompts, tolerance checks, weight-based invoicing) follows this flag.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| CW on variable-weight sellable items only (typical) | Meat cuts, whole fish, cheese wheels, whole birds, some produce | — |
| CW also on ingredients purchased by weight-in-box | When purchase invoices are settled on actual received weight | If vendor invoices fixed weights anyway — you add registration without financial effect |
| No CW; fixed nominal weights | No scales at the capture points; product weight variance economically trivial | When customers are invoiced on actual weight — then you *must* have CW or you reconcile manually forever |

**Required client info:**
- Which items are bought and/or sold on actual weight (check real vendor and customer invoices, not what the client says)
- Weight variance per unit (a ±1% item may not be worth it; ±15% carcass absolutely is)
- Where scales exist today: receiving dock, production, dispatch; are they connectable / do labels carry weight barcodes?

**Interactions:** items must typically be lot-tracked for weight-per-lot handling; GS1 barcode parsing (Mobile Warehouse) can populate weight from labels; production input/output weights feed yield calculation in [food-manufacturing.md](food-manufacturing.md).
**Default recommendation:** start with the sellable variable-weight assortment where invoices are already weight-based; extend to purchasing where vendor settlement is actual-weight. Resist blanket enablement.
**Risk of getting it wrong:** high-irreversible in practice — converting an item between CW and standard mid-life with open ledger entries is painful; scope carefully per item before go-live.
**Expertise tags:** `#aptean-fnb` `#catch-weight` `#item-master`

### Weight tolerance policy

**Where:** Catch weight item setup — nominal weight and tolerance ranges per unit
**What it controls:** the accepted band around nominal weight per handling unit; entries outside the band are warned or blocked. Protects against fat-finger weights (155 kg instead of 15.5) and against fraud/shrinkage patterns.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Tight tolerance, hard error | Portion-controlled products, connected scales (no typing) | Natural products with genuine spread — constant overrides train users to ignore controls |
| Wide tolerance, warning only | Carcasses, whole fish, seasonal produce | High-value items where a mistyped weight is a big invoice error |
| Tolerance per item category, reviewed after 3 months of actuals | Everyone — set from data, not guesses | — |

**Required client info:**
- Actual weight distribution per item (get a sample of real weigh data before setting bands)
- Entry method: typed (needs tighter sanity checks) vs. scanned/scale-fed (band can reflect only physical variance)

**Interactions:** tolerance breaches at receipt can trigger a quality check (QC module); weight anomalies per lot are a shrinkage-audit signal.
**Default recommendation:** warnings at ±3× observed standard deviation initially, hardened to errors for typed entry once nominal weights are validated.
**Risk of getting it wrong:** medium — too loose and bad weights hit invoices (credit-memo churn, customer trust); too tight and the floor stalls on overrides.
**Expertise tags:** `#aptean-fnb` `#catch-weight` `#data-quality`

### Weight capture method per process step

**Where:** warehouse/production/mobile setup per location and flow
**What it controls:** how actual weights get into the system at each posting point: manual keying, GS1-128 label scan (weight embedded in barcode), Mobile Warehouse app entry, or connected/integrated scales.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Scan vendor GS1 labels at receipt | Vendors pre-label with weight barcodes (common in protein supply chains) | Vendors without compliant labels — verify label quality with real samples first |
| Connected scales at pack-off/dispatch | Own production lines, higher volume | Low volume where the integration cost outweighs keying |
| Manual entry on Mobile Warehouse app | Transitional, low volume | High volume — typing weights hundreds of times a day is where errors live |
| Manual entry in back office from paper | Never as target state | Acceptable only as a short bridge during rollout |

**Required client info:**
- Sample vendor labels (do they actually carry AI 310x weight?); scale models and whether they output data
- Volume per capture point per day — sizing the ergonomics matters more than the licence cost

**Interactions:** Mobile Warehouse (MWR) parses GS1 application identifiers (GTIN, lot, expiry, weight, SSCC) at receipt — one scan fills lot management, expiration and catch weight simultaneously; scale integration is typically a small partner project, budget it explicitly.
**Default recommendation:** GS1 scanning inbound wherever vendor labels support it; connected scale or weight-label print-and-scan at dispatch; treat any step with manual weight keying as technical debt with a closure date.
**Risk of getting it wrong:** medium — recoverable, but bad capture design silently produces the invoice-dispute pattern the client bought CW to eliminate.
**Expertise tags:** `#aptean-fnb` `#catch-weight` `#mobile-warehouse` `#integration`

### Catch weight in production

**Where:** production order component and output handling for CW items (documented CAW behaviour on production order component lines)
**What it controls:** whether production consumes and outputs CW items by actual weight (weighed at the line) or nominal weight, and therefore how honest your yield numbers are.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Actual weights on consumption and output | Protein processing, anywhere yield is managed (it should be) | No floor scales / no shop-floor registration — nominal-weight "yield" is fiction, better to know that |
| Actual on output only, nominal consumption | Transitional; output scales exist, input weighing doesn't | Long term — input variance lands in yield noise |

**Required client info:**
- Where scales exist along the line; whether Shop Floor Production app is in scope (see [food-manufacturing.md](food-manufacturing.md))
- Which yield KPI the client already reports to management and how it's computed today

**Interactions:** feeds yield % and weight/loss tracking in Process Manufacturing; costing of co-products apportioned by weight needs actual weights to mean anything.
**Default recommendation:** if the client is a processor, plan actual-weight registration at both ends of the critical processes from day one — it is the single biggest value driver of this module for them.
**Risk of getting it wrong:** medium-high — wrong here means the costing and yield story management bought is not delivered, discovered months later.
**Expertise tags:** `#aptean-fnb` `#catch-weight` `#manufacturing` `#yield`

> ⚠️ Verify against current Aptean documentation — grounded in Aptean's public CAW docs (item setup, reclassification, production order component lines) but tolerance mechanics and scale-integration options are partner-gated; validate exact behaviour in the client's version.
