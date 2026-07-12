# Purchasing — Odoo (Standard)

> **Scope:** Odoo 19 Enterprise (Odoo Online, Odoo.sh or on-premise); Community edition differences flagged inline
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when Odoo releases functional changes to this area (one major release per year, typically October).

Covers procure-to-pay configuration in Odoo: vendor master data and vendor pricelists, the RFQ→PO document flow and purchase agreements, order approval, how demand becomes purchase orders (reordering rules vs MTO vs manual), bill control and 3-way matching, receiving, vendor bill capture (OCR vs Peppol), landed costs, and dropshipping. In scope for every client. The two biggest scoping questions are usually the replenishment trigger (who decides what gets bought) and the bill-capture channel — in Belgium the second one is largely answered by the Peppol mandate.

---

## Vendor master data & vendor pricelists

**Where:** Vendors are plain contacts (`res.partner`) — Purchase app vendor menu or Contacts app; purchase-relevant fields sit on the contact's Purchase tab (payment terms, fiscal position, receipt reminder). Vendor pricelists live on the **product form → Purchase tab** (one line per vendor) and centrally under **Purchase → Configuration → Vendor Pricelists** (XLSX/CSV import/export supported).
**What it controls:** There is no separate vendor master — a contact becomes a vendor by being used as one. Vendor pricelist lines (vendor, price, minimum quantity, lead time in days, vendor product code/name, validity dates) auto-populate RFQ lines and, critically, tell automated replenishment *which* vendor to buy from and at what price. With multiple vendor lines per product, the first line by sequence wins.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| No maintained vendor lines — buyers key price per RFQ | Spot buying, volatile prices, low SKU count. | Any automated replenishment: a stocked product without a vendor line makes the Buy route fail silently at scheduler time — the single most common "why didn't it order?" ticket. |
| One vendor line per product (price, min qty, lead time, validity dates) | The standard answer for stocked products; lead time feeds scheduled receipt dates and replenishment timing. For annual price rounds, export with External IDs and re-import — importing without them creates duplicates instead of updates. | — |
| Multiple vendor lines, priority by sequence | Dual sourcing with a clear preferred vendor; quantity breaks via several lines per vendor with different minimum quantities. | Expecting Odoo to *choose* the cheapest vendor per order — standard Odoo takes the first matching line by sequence, it does not optimize. |

**Required client info:**
- Who maintains purchase prices — buyer or finance — and how often do vendors reprice? Quantity breaks or validity periods?
- One shared contact database: are customers and vendors already deduplicated, who may create vendors, and what payment terms/VAT treatment per vendor — any reverse-charge / co-contractant vendors needing a [fiscal position](finance.md#taxes-vat-return--fiscal-positions-belgian-vat)?

**Interactions:** Vendor lines fuel [replenishment triggers](#replenishment-triggers-reordering-rules-vs-mto); lead times combine with [reordering rule parameters](inventory.md#reordering-rules--replenishment); confirming a blanket order writes a vendor line automatically ([purchase agreements](#rfqpo-flow--purchase-agreements)). Vendor creation rights are an [access-rights decision](general-setup.md#users-access-rights--record-rules) — Odoo has no native approval flow on vendor bank-detail changes, so gate creation/editing tightly wherever payment files are generated.

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Maintained vendor lines with realistic lead times for every stocked product (make it a data-readiness gate before go-live), sequence-ordered vendors where dual-sourced, vendor creation restricted to a small group.

**Risk of getting it wrong:** medium — data is editable anytime, but missing vendor lines break replenishment quietly, and unverified vendor bank details on an open contact model are a payment-fraud exposure Odoo does not police for you.

**Expertise tags:** `#purchasing` `#master-data`

---

## RFQ→PO flow & purchase agreements

**Where:** Purchase app (an RFQ and a PO are the *same document* — states Draft RFQ → Sent → Purchase Order → Done/Locked). Purchase agreements: **Purchase → Configuration → Settings → Orders → Purchase Agreements**, then **Purchase → Orders → Purchase Agreements** with two agreement types: **Blanket Order** and **Purchase Template**. The same setting enables **alternative RFQs** (the tendering mechanism — the "call for tenders" of older versions) via the Alternatives tab on an RFQ.
**What it controls:** Whether buys go straight to a confirmed PO, pass through a quotation/comparison step, or draw on a pre-negotiated agreement. **Community edition:** purchase agreements and alternative RFQs are available in Community — no edition gap here.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Direct PO (create → Confirm Order), RFQ emailed first only where the vendor genuinely confirms price/date per order | Most SME buying: price known from the vendor line. | Teams that confirm immediately anyway — the Sent state becomes noise; conversely, tendered buys deserve the RFQ paper trail. |
| Alternative RFQs (compare product lines across vendors, keep the best, cancel the rest) | Occasional tendering, public-sector-style comparison, price checks on big buys. | Routine replenishment — too much ceremony. |
| Blanket order (one vendor, agreed prices/quantities over a validity period; RFQs drawn from it; confirms a vendor line for replenishment) | Negotiated annual volumes with call-offs — the agreed price then also serves automated replenishment. Note: prices on agreement lines must be entered manually, they don't pull from existing vendor lines. | No negotiated volumes — maintain plain vendor pricelists instead. |
| Purchase template (reusable order basket, optionally multi-vendor) | Recurring identical baskets (consumables, packaging) reordered frequently. | As a substitute for reordering rules on stocked goods — replenishment, not templates, owns those. |

**Required client info:**
- Are there negotiated volume/price agreements with validity periods, and with how many vendors? (Rule of thumb: most SMEs need agreements for a handful of strategic vendors at most — if the client can't name the contracts, skip the feature and keep vendor pricelists clean.)
- Does anyone actually compare vendor offers per order, or is the vendor fixed per product? Recurring fixed baskets that justify templates?

**Interactions:** Confirmed blanket orders feed [vendor pricelists](#vendor-master-data--vendor-pricelists) and thus [replenishment](#replenishment-triggers-reordering-rules-vs-mto). Confirmed POs flow into [approvals](#purchase-approvals--order-validation) and generate receipts ([receipts](#receipts--overunder-receipt-handling)). PO numbering is a [sequence decision](general-setup.md#document-numbering-sequences).

**Add-on impact:** None yet — this knowledge base has no Odoo add-on layers so far.

**Default recommendation:** Direct POs as the working mode; enable Purchase Agreements only when named, negotiated contracts exist; blanket orders for those vendors so agreed prices drive replenishment.

**Risk of getting it wrong:** low — all reversible; the cost of over-engineering is buyers clicking through states nobody reads.

**Expertise tags:** `#purchasing` `#pricing`

---

## Purchase approvals & order validation

**Where:** **Purchase → Configuration → Settings → Orders**: **Purchase Order Approval** (with **Minimum Amount**) and **Lock Confirmed Orders**. Alternative: the **Approvals** app (purchase-request flows). Approver population = users with the Purchase *Administrator* access level.
**What it controls:** Whether a PO above the threshold stops in a *To Approve* state until a purchase manager confirms it, and whether confirmed orders are locked against silent editing.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| No approval | Owner-operated: the buyer is the spender of record. | Any delegated purchasing authority — there is no other native commitment control. |
| **Purchase Order Approval + Minimum Amount** | The standard SME control. One company-wide threshold, one approval level: orders above the amount wait in To Approve for a Purchase Administrator. | Clients wanting BC-style approver chains, per-user limits, or amount ladders — native Odoo has exactly one threshold and one level. Multi-level needs the Approvals app or customization. |
| **Approvals app** (Enterprise) — purchase *request* approved before an RFQ exists | Pre-commitment control with multiple approvers, categories, and sequenced approvals; catches spend before a PO is even drafted. **Community edition:** not available. | Doubling up: approving the request *and* the PO for the same spend — pick one control point. |
| **Lock Confirmed Orders** | Cheap audit hygiene: confirmed POs go read-only; changes require an explicit Unlock. Recommended wherever 3-way matching or receiving discipline matters. | High-change purchasing environments where every order is renegotiated — constant unlocking breeds resentment; fix the process first. |

**Required client info:**
- The delegation-of-authority matrix — and can it be honestly flattened to one threshold and one approver group?
- Who buys today and what access level do they genuinely need? Is the control point commitment (PO) or payment (vendor bill)?

**Interactions:** See the cross-app approval overview in [general-setup.md](general-setup.md#approval-workflows). The trap to check every time: buyers who hold the Purchase *Administrator* access level approve their own orders — the threshold only bites if day-to-day buyers sit at the *User* level, so design [access rights](general-setup.md#users-access-rights--record-rules) and the threshold together. Locked orders interact with [over-receipt handling](#receipts--overunder-receipt-handling) — quantity corrections on a locked PO need an unlock. Bill-side controls live in [bill control & 3-way matching](#bill-control-policy--3-way-matching).

**Add-on impact:** None known — no Odoo add-on files exist in this knowledge base yet.

**Default recommendation:** Purchase Order Approval on with a threshold high enough to catch material spend only, buyers at Purchase User level, Lock Confirmed Orders on; Approvals app only when a real multi-level policy exists on paper.

**Risk of getting it wrong:** low — toggles are reversible; the real risk is the false comfort of an approval threshold that every buyer can self-approve past.

**Expertise tags:** `#purchasing` `#approvals`

---

## Replenishment triggers (reordering rules vs MTO)

**Where:** Reordering rules per product (Reordering Rules smart button, or all rules at **Inventory → Operations → Replenishment** — also the manual replenishment report); routes on the product's Inventory tab (**Buy**, **Replenish on Order (MTO)** — the MTO route is archived by default and must be unarchived once); the daily scheduler generates the draft RFQs.
**What it controls:** Who — or what — decides that a purchase happens. This is the purchasing side of the choice; the full routes/parameters architecture is treated in [inventory.md](inventory.md#routes--procurement-rules-architecture-mtobuymanufacture) and [reordering rules](inventory.md#reordering-rules--replenishment).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Manual RFQs only | Low SKU count, project buying, expense purchases. | More than a few hundred stocked SKUs — stockouts and firefighting follow. |
| **Reordering rules (min/max, automatic trigger)** | The standard answer for stocked products: forecast dips below min → scheduler creates/updates a draft RFQ up to max, grouped per vendor. Draft RFQs still need human confirmation — that's the buyer's review point, keep it. | Products with lumpy, quote-driven demand; and anywhere nobody will own the parameters — stale min/max quietly buys the wrong things. |
| **Manual-trigger rules / replenishment report** | Buyer-in-the-loop mode: suggestions appear on the Replenishment screen and someone clicks Order Once. Good first step for clients who don't yet trust their own parameters. | High-volume stable SKUs where the review adds no judgment — switch those to automatic. |
| **Replenish on Order (MTO) + Buy** | Back-to-back buying: each sales order spawns its linked RFQ. Fits configured/one-off goods and never-stocked items (compare [dropshipping](#dropshipping) if the vendor ships direct). | Fast movers with shared stock — MTO chains each purchase to one order and bypasses pooling. |

**Required client info:**
- Who buys today, and will a named person own reordering parameters and review draft RFQs on a fixed cadence?
- Stocked-to-order ratio; are min/max levels known or derivable from history? Are vendor lead times reliable enough to automate against?

**Interactions:** Every automated trigger needs a [vendor pricelist line](#vendor-master-data--vendor-pricelists). Parameters and route mechanics: [inventory.md](inventory.md#reordering-rules--replenishment) and [routes architecture](inventory.md#routes--procurement-rules-architecture-mtobuymanufacture). Generated POs pass through [approvals](#purchase-approvals--order-validation). Subcontracted components have their own supply logic — [manufacturing.md](manufacturing.md#subcontracting).

**Add-on impact:** None known yet; no add-on overlays exist for Odoo in this knowledge base.

**Default recommendation:** Rule of thumb: stocked = reordering rules; sold-to-order = MTO or dropship; everything else manual — decided per product category, not per anecdote. Start with manual-trigger rules at go-live, promote stable SKUs to automatic after one or two clean months, with a named owner for parameters from day one.

**Risk of getting it wrong:** medium — regimes are switchable, but a launch with bad min/max produces weeks of wrong draft RFQs and permanent user distrust ("we just ignore the replenishment screen").

**Expertise tags:** `#purchasing` `#replenishment`

---

## Bill control policy & 3-way matching

**Where:** Per product: **Purchase tab → Vendor Bills → Control Policy** (*On ordered quantities* / *On received quantities*); defaults follow the product type — services default to ordered, goods to received. (Older versions had a company-wide Bill Control default in Purchase settings; in v19 the default appears driven by product type only — ⚠️ verify against current Odoo documentation.) 3-way matching: **Purchase → Configuration → Settings → Invoicing → 3-way matching**. **Community edition:** the 3-way matching module is Enterprise-only; bill control policies themselves are Community.
**What it controls:** Which quantities a draft vendor bill is generated from (billing what you ordered vs what actually arrived), and whether bills get a *Should Be Paid* advisory status (Yes / No / Exception) based on receipt state.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **On ordered quantities** | Services, subscriptions, and vendors that bill on confirmation; draft bill available as soon as the PO is confirmed. | Physical goods with partial or unreliable deliveries — you'll book bills for stock that never arrived. |
| **On received quantities** | The default and right answer for goods: bills draw on received quantities, and a bill can't be created before anything is received. | Prepayment-style vendors billing at order — AP fights the error message every time. |
| **3-way matching on top** | AP separated from receiving; flags bills as Exception when billed lines deviate from receipts. Only meaningful with control policy = received quantities. | Understand what it is *not*: Should Be Paid is advisory — Odoo does not block payment of an Exception bill. Clients expecting a hard block (BC-style posting control) need process discipline or customization. |

**Required client info:**
- Does AP match bills to receipts today, and does receiving actually happen in the system before bills arrive?
- Share of service vs goods spend? Does the client expect matching to *block* payment — reset that expectation early?

**Interactions:** Depends on receipts actually being validated on time — [receipts](#receipts--overunder-receipt-handling). Price/quantity deviations land in accounting as the bill is posted; account mapping is a [finance decision](finance.md#continental-vs-anglo-saxon-accounting--automatic-accounts). Bills arriving via [Peppol or OCR](#vendor-bill-digitization-ocr) still match against the PO. Landed-cost lines on bills are handled separately — [landed costs](#landed-costs).

**Add-on impact:** None known — the Odoo add-on layer of this knowledge base is still empty.

**Default recommendation:** Received quantities for all goods, ordered quantities for services (the type defaults already do this — don't fight them); 3-way matching on for any client with separated AP and receiving, sold honestly as a flag, not a gate.

**Risk of getting it wrong:** medium — policies are switchable per product, but months of bills booked on ordered quantities against unreliable deliveries mean accrual cleanup and duplicate-payment exposure.

**Expertise tags:** `#purchasing` `#invoice-matching`

---

## Receipts & over/under-receipt handling

**Where:** Confirming a PO creates a receipt (Inventory app); how many inbound steps that receipt goes through is a warehouse decision — see [warehouse.md](warehouse.md#inboundoutbound-steps-the-complexity-ladder). Partial validation triggers the backorder dialog. **Receipt Reminder** (Purchase settings / per vendor) emails vendors before the expected date.
**What it controls:** How goods arrival is recorded against the PO — and therefore what "received quantities" means for bill control and valuation.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Validate receipts as goods arrive, backorder on partials (Create Backorder) | The standard flow: keeps open PO quantities honest and bill control accurate. | — |
| No Backorder on partial validation | The remainder will genuinely never come (vendor short-closed the line). | Using it to make the list look clean — it silently cancels open supply that replenishment was counting on. |
| Over-receipt: validate more than ordered | Odoo permits receiving above the ordered quantity; billing then follows the received quantity. Acceptable where vendors round up to full packs and the client keeps the excess. | Clients needing enforced receiving tolerances: standard Odoo has no over-receipt tolerance framework (no BC-style tolerance codes) — control is procedural or custom. Whether validation warns or accepts silently varies by setup — ⚠️ verify against current Odoo documentation. |
| Quality control points on receipts (**Quality app — Enterprise**) | Incoming inspection per product/operation before stock is available. **Community edition:** no Quality app. | See [manufacturing.md](manufacturing.md#quality-management) for the quality architecture — don't configure it twice. |

**Required client info:**
- Do vendors part-deliver routinely, and does the dock team understand backorders? Do they legitimately over-ship (pack rounding, bulk goods), and does the client keep or return the excess?
- Any incoming inspection requirement (drives the Quality app, an Enterprise argument)?

**Interactions:** Received quantities drive [bill control](#bill-control-policy--3-way-matching) and stock valuation ([inventory.md](inventory.md#inventory-valuation-manual-vs-automated)). Inbound step count is the [warehouse complexity ladder](warehouse.md#inboundoutbound-steps-the-complexity-ladder). Correcting quantities on a locked PO requires an unlock — [approvals & validation](#purchase-approvals--order-validation).

**Add-on impact:** No Odoo add-ons documented in this knowledge base yet — none known.

**Default recommendation:** Backorders on by habit, No Backorder reserved for consciously short-closed lines, receipt reminders on for long-lead vendors; treat over-receipt as a procedural rule ("flag anything above X% to the buyer") since the system won't enforce it.

**Risk of getting it wrong:** low–medium — everything is correctable, but sloppy receiving corrupts both bill matching and replenishment signals at once, and that shows up as money.

**Expertise tags:** `#purchasing` `#receiving`

---

## Vendor bill digitization (OCR)

**Where:** **Accounting → Configuration → Settings → Digitization → Document Digitization** (process vendor bills automatically or on demand); upload by drag-and-drop onto the purchase journal, or via the journal's email alias (default `vendor-bills@<alias domain>` — each attached PDF becomes a draft bill); optional auto-posting for trusted vendors. **Community edition:** OCR digitization is Enterprise functionality consuming IAP credits (pay-per-document) — Community clients enter bills manually or receive them via Peppol.
**What it controls:** How paper/PDF vendor bills become draft bills in the system, and how much AP typing survives.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| OCR digitization (auto or on-demand per journal) | The PDF tail: foreign vendors, utilities, anyone not on Peppol. On-demand mode is a sensible start — AP triggers digitization per document and builds trust. Manual entry remains viable only below a few dozen bills a month. | As the *primary* channel for a Belgian client in 2026 — see the next row. IAP credits also cost real money per document; budget it. |
| **Peppol inbound as primary channel** | Belgium: the B2B e-invoicing mandate makes structured invoices the norm between Belgian VAT-registered businesses — bills arrive as exact, structured draft vendor bills, no OCR guessing, no credits. Setup and registration live in [finance.md](finance.md#e-invoicing--peppol). | Nothing to avoid — this is the default posture for Belgian clients; OCR mops up the rest. |
| Auto-posting for selected vendors | High-volume, highly reliable recurring billers after months of clean matching. | Early in the implementation — keep a human on every bill until matching quality is proven. |

**Required client info:**
- Monthly vendor bill volume, and what share already arrives via Peppol vs PDF/paper? Who owns the AP inbox — is routing bills to a journal alias realistic?
- Reverse-charge / co-contractant vendors whose bills need the right [fiscal position](finance.md#taxes-vat-return--fiscal-positions-belgian-vat) applied on capture?

**Interactions:** Captured bills still obey [bill control & 3-way matching](#bill-control-policy--3-way-matching) and auto-complete from open POs. Peppol registration, journal setup and the Belgian mandate timeline: [finance.md](finance.md#e-invoicing--peppol). Payment side (SEPA, CODA reconciliation): [finance.md](finance.md#banking-coda-sepa--reconciliation).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** For Belgian clients: Peppol inbound as the primary channel, OCR on-demand for the non-Peppol tail, auto-posting off until matching is demonstrably clean.

**Risk of getting it wrong:** low — channels are adjustable anytime; the failure mode is paying IAP credits to OCR-guess invoices that Peppol would have delivered perfectly structured.

**Expertise tags:** `#purchasing` `#ocr` `#peppol`

---

## Landed costs

**Where:** **Inventory → Configuration → Settings → Valuation → Landed Costs** (plus a Default Journal); a service product flagged **Is a Landed Cost** with a **Default Split Method**; applied from the freight/customs vendor bill (Create Landed Costs) or via **Inventory → Operations → Landed Costs**, targeting a validated receipt.
**What it controls:** Whether freight, customs duties and insurance are absorbed into product valuation (true landed cost, correct margins) or expensed straight to P&L (understated stock value, flattering-then-lumpy margins).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| No landed costs — freight expensed as booked | Domestic buying with immaterial inbound freight. | Importers: at 5–20% of product value, expensing freight misstates both stock and margin per product. |
| Landed costs with split method **By Current Cost** | The usual default — cost allocated proportionally to line value. | Freight actually driven by weight/volume (containers): use By Weight / By Volume, which require weight/volume data on product forms. |
| Split **Equal** or **By Quantity** | Homogeneous shipments where lines are comparable. | Mixed-value shipments — a cheap bulky item and an expensive small one get nonsense allocations. |

Hard prerequisites the client must accept: the products' category must use **FIFO or AVCO** costing with **automated valuation** for the cost to actually land in stock value. Under AVCO, a landed cost applied after part of the receipt is already sold spreads over the remaining units — apply late freight bills promptly. Standard-cost products don't absorb landed costs; deviations go to variance accounts.

**Required client info:**
- Import share and typical freight/duty as % of product value (materiality)? Do freight bills arrive with the goods or weeks later, and from a different vendor?
- Are weights/volumes maintained on products (needed for those split methods)? Costing method and valuation mode per product category — already decided in [inventory.md](inventory.md#product-categories--costing-method-standard--avco--fifo)?

**Interactions:** Requires [automated valuation](inventory.md#inventory-valuation-manual-vs-automated) and [FIFO/AVCO categories](inventory.md#product-categories--costing-method-standard--avco--fifo); journal entries land per the [accounting architecture](finance.md#continental-vs-anglo-saxon-accounting--automatic-accounts). The landed-cost service product rides on [vendor bills](#vendor-bill-digitization-ocr) from freight vendors.

**Add-on impact:** Nothing yet — the add-on layer for Odoo is empty in this knowledge base.

**Default recommendation:** For importers: landed costs on, one service product per charge type (freight, duty, insurance), split By Current Cost unless freight is genuinely weight/volume-driven, applied as part of the AP routine for freight bills — not quarterly cleanup.

**Risk of getting it wrong:** medium — costs can be applied late but valuation history and sold-through units don't retroactively correct; the costing-method prerequisite underneath is the truly hard-to-reverse decision.

**Expertise tags:** `#purchasing` `#landed-costs`

---

## Dropshipping

**Where:** **Purchase → Configuration → Settings → Logistics → Dropshipping**, then the **Dropship** route on the product's Inventory tab (product must be Can be Sold + Can be Purchased, with a vendor line). A sales order then auto-generates a linked RFQ; the confirmed PO carries a *dropship transfer* from vendor location straight to customer location.
**What it controls:** Whether the vendor ships directly to the client's customer, with Odoo pairing the SO and PO and recording a stock move that never touches the client's warehouse.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Dropship route on never-stocked products | Bulky/slow items, wide catalogs where stocking is uneconomic, vendor delivers acceptably in the client's name. | Products where the client adds value in handling (kitting, inspection, consolidation) — dropship skips your warehouse and your quality gate entirely. |
| Dropship + Buy both enabled | Hybrid items: dropship the big orders, serve small ones from stock — the route chosen per SO line. | Teams that won't manage the per-line choice consciously; and remember not dropshipping at all is the right call when control over the customer experience beats the inventory saving. |

Consultant caveats: validating the dropship transfer is the moment Odoo records both the receipt-equivalent and the delivery-equivalent — someone must confirm the vendor actually shipped, because with invoicing policy "delivered quantities" that validation makes the customer invoiceable, and with bill control "received quantities" it releases the vendor bill. Goods never enter stock: no reordering, no receipt quality gate, valuation flows through without resting in inventory, and margin on the SO line is only as good as the vendor price — stale vendor lines produce confidently wrong margins.

**Required client info:**
- Share of revenue to dropship, per which vendors — and are those vendors reliable enough to ship in the client's name?
- Who confirms vendor shipment (vendor portal, tracking mail, customer confirmation?) and validates the transfer? Invoicing policy on dropshipped products — ordered or delivered quantities ([finance.md](finance.md))?

**Interactions:** Route mechanics sit in the [routes architecture](inventory.md#routes--procurement-rules-architecture-mtobuymanufacture); compare [MTO + Buy](#replenishment-triggers-reordering-rules-vs-mto) when goods should pass through the warehouse instead. Requires a [vendor line](#vendor-master-data--vendor-pricelists). Vendor bill timing follows [bill control](#bill-control-policy--3-way-matching); accounting flow per [finance.md](finance.md#continental-vs-anglo-saxon-accounting--automatic-accounts).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Dropship route on genuinely never-stocked products with a written rule for who validates the transfer and on what evidence; hybrid Buy+Dropship only for clients who will actively manage the per-order choice.

**Risk of getting it wrong:** medium — the route itself toggles freely, but transfers validated on guesswork misstate revenue timing, COGS and open payables in one click.

**Expertise tags:** `#purchasing` `#dropship`
