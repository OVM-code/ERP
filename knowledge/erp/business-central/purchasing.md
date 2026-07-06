# Purchasing — Business Central (Standard)

> **Scope:** Microsoft Dynamics 365 Business Central (SaaS, current version)
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when the vendor releases functional changes to this area.

Covers procure-to-pay configuration in Business Central: Purchases & Payables Setup, vendor master governance, purchase pricing, how demand becomes purchase orders (manual vs requisition worksheet vs planning worksheet), approval workflows, over-receipt tolerances, prepayments to vendors, and the purchasing side of drop shipments and special orders. In scope for every client; the automation level of replenishment is usually the biggest scoping question in this area.

---

## Purchases & Payables Setup — key toggles

**Where:** **Purchases & Payables Setup** page (search: "Purchases & Payables Setup").
**What it controls:** Company-wide defaults for purchase document behavior: whether vendor invoice numbers are enforced, what posting an invoice does to receipts, cost application on purchase returns, and date/quantity defaults.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Ext. Doc. No. Mandatory = On** (vendor's invoice no. required before posting) | Almost always. It is the duplicate-invoice defense: BC warns on a repeated external document number per vendor, and AP can trace every posted invoice to the vendor's paper. | Only for odd sub-processes (e.g. auto-generated internal charge invoices) — and even then prefer a dummy numbering convention over turning the toggle off. |
| **Exact Cost Reversing Mandatory = On** | Clients that return goods to vendors and care about clean inventory valuation: forces the purchase return to be applied to the original receipt entry (Appl.-to Item Entry) so it leaves inventory at exactly the cost it arrived with. | High-volume returns where staff genuinely can't identify the original receipt; but as on the sales side, fix the process rather than the toggle. |
| **Receipt on Invoice = On** (posting a purchase invoice also posts the receipt) | AP-driven clients without a goods-receipt step: invoice arrives, gets posted, stock updates. | Any client using warehouse receipts or three-way matching (order–receipt–invoice). With warehouse handling the receipt must come from the warehouse document — see [warehouse.md](warehouse.md#inbound-outbound-document-flow). |
| **Default Posting Date = Work Date** vs **No Date** | Work Date for convenience. | No Date where posting-period discipline is weak — forces conscious dating; pair with [allowed posting dates](finance.md#allowed-posting-dates). |
| **Default Qty. to Receive = Remainder** vs **Blank** | Remainder for full-delivery vendors. | Blank where partial deliveries are routine and warehouse should key what physically arrived — prevents accidental full receipts. |
| **Calc. Inv. Discount = On** | Vendors grant total-amount invoice discounts that AP should take automatically. | No such agreements exist — noise. |
| **Over-Receipt behavior** — governed by Over-Receipt Codes (separate page), not a setup toggle | See [Over-receipt codes](#over-receipt-codes--receiving-tolerances) below. | — |

**Required client info:**
- Does AP do three-way matching, or post invoices straight to stock?
- Are vendor invoice numbers captured today, and have duplicate payments happened before? (They almost always have.)
- Do vendors part-deliver routinely?

**Interactions:** Exact Cost Reversing works with the [costing method](inventory.md#costing-method). Receipt on Invoice conflicts with [warehouse receipt documents](warehouse.md#require-receive). Posting date defaults align with [period controls](finance.md#allowed-posting-dates). E-documents/OCR invoice capture relies on external document numbers being disciplined.

**Add-on impact:** Aptean Food & Beverage ERP adds commodity purchasing and vendor trade agreements that assume standard toggles (especially exact cost reversing) are on — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Ext. Doc. No. Mandatory = On, Exact Cost Reversing Mandatory = On, Receipt on Invoice = Off wherever goods receipt is a real step, Default Qty. to Receive = Blank for part-delivering supply chains.

**Risk of getting it wrong:** medium — toggles are reversible, but months of returns posted without exact cost reversing distort valuation, and Ext. Doc. No. off invites duplicate vendor payments (real money, recoverable only by asking the vendor nicely).

**Expertise tags:** `#purchasing` `#setup` `#accounts-payable`

---

## Vendor templates & vendor master data governance

**Where:** **Vendor Templates** page (table "Vendor Templ."); vendor card; approval workflow templates for vendor card changes; Payment Practices / vendor bank account fields.
**What it controls:** Consistent creation of vendors with correct posting groups (vendor, general business, VAT business), payment terms and methods, currency, and — critically — bank account details. Vendor master fraud (changed bank details) is the single most expensive master-data failure in P2P.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Templates per vendor segment (DOMESTIC, EU, IMPORT, EXPENSE/UTILITIES, INTERCOMPANY) | Nearly always; segments mirror posting group and VAT treatment combinations. | Template sprawl for cosmetic variants. |
| Open vendor creation | Micro-teams where the bookkeeper does everything. | Anywhere payments are batch-run: an unvetted vendor with a bank account is a payment waiting to leave. |
| Gated: creation restricted by permission set + **approval workflow on vendor card / bank account changes** | Recommended for any client running payment files. BC ships a vendor approval workflow template; combine with a rule that bank detail changes require a second approver. | Genuinely low-risk cash environments (rare). |

**Required client info:**
- Who creates vendors and who changes bank details today, and is there any call-back verification?
- Vendor segments differing in tax/currency/payment method?
- Is there a group-level vendor master (multi-company: consider IC or master-data sync)?

**Interactions:** Templates require the [posting group architecture](finance.md#posting-groups) to exist first. Payment methods/terms feed [payment journal and payment file setup](finance.md#bank--payment-setup). Purchaser codes on vendors feed [approval routing](#purchase-approval-workflows--amount-limits). Over-Receipt Code can be defaulted per vendor (below).

**Add-on impact:** Aptean F&B adds vendor attributes for commodity trading and quality/compliance (approved supplier status) — extend templates and the gating rules to cover them; see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** 4–6 posting-group-aligned templates, vendor creation permission-restricted, mandatory approval on new vendors and on any bank-account change.

**Risk of getting it wrong:** high — not irreversible in the system, but wrong/unverified bank details lead to unrecoverable outbound payments; wrong posting groups cost audit-time reclassification.

**Expertise tags:** `#purchasing` `#master-data` `#fraud-control`

---

## Purchase pricing & discounts

**Where:** **Purchase Price Lists** (new pricing experience) or legacy Purchase Prices / Purchase Line Discounts pages; vendor card (Invoice Disc. Code, Prices Including VAT); item card (Last Direct Cost as fallback).
**What it controls:** What unit cost and line discount land on a purchase line for a vendor–item–quantity–UoM–date combination. Same best-price engine and same Feature Management switch as sales pricing — enabling the "New sales pricing experience" feature update converts **both** sales and purchase price data, one way.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| No maintained purchase prices — lines default from Last Direct Cost | Small clients, volatile pricing, vendor confirms price per order anyway. | Clients doing invoice matching against agreed prices: without maintained prices, every price variance looks "normal". |
| Purchase price lists per vendor (new experience), with minimum quantities and date ranges | Negotiated vendor agreements, quantity breaks, contract periods. Draft→Active status gives change control; Edit in Excel for mass updates. | — |
| Purchase line discounts (vendor×item(-group)) | Vendors quoting list price minus trade discount; keeps the gross-to-net visible. | Vendors quoting net prices — model as prices, not discounts. |
| Invoice discounts + Calc. Inv. Discount | Genuine total-amount discount agreements. | Absent agreements: off. |

**Required client info:**
- Are vendor prices contractual (matching required) or spot?
- Quantity-break or period pricing? Currency per vendor?
- Who maintains purchase prices — buyer or finance — and how is a price change authorized?

**Interactions:** Shares the one-way pricing feature switch with [sales pricing](sales.md#sales-pricing-model-price-lists-vs-legacy-sales-prices-discounts-hierarchy) — one decision covers both. Purchase price is the planned cost input for margin and for [standard cost review](inventory.md#costing-method). Price variances surface in invoice matching and hit [purchase variance accounts](finance.md#posting-groups) under standard costing.

**Add-on impact:** Major under Aptean F&B: commodity pricing (market-indexed costs, formula pricing) replaces static purchase price lists for commodity items — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** New pricing experience on; maintained purchase price lists for contracted vendors; Last Direct Cost fallback accepted for the tail; line discounts only where the vendor genuinely quotes gross-minus-discount.

**Risk of getting it wrong:** medium (feature switch itself: high-irreversible, shared with sales) — bad purchase prices propagate into planned costs, margins, and PO values that vendors happily don't correct.

**Expertise tags:** `#purchasing` `#pricing`

---

## Requisition flow: manual quotes/orders vs requisition worksheet vs planning worksheet

**Where:** **Purchase Quote/Order** documents; **Requisition Worksheet**; **Planning Worksheet**; **Order Planning** page; item card planning fields (Replenishment System, Reordering Policy, Vendor No., lead time); **Purchasing Codes** for demand-linked buys.
**What it controls:** Who decides what to buy and how automated that decision is — the core P2P scoping question. The worksheet suggests, a human reviews action messages, and Carry Out Action Messages creates the purchase orders.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Manual purchasing** (buyers key POs, optionally from quotes) | Low SKU count, project buying, expense purchasing. Purchase quotes add a compare-and-convert step for tendered buys. | More than a few hundred stocked SKUs — manual replenishment doesn't scale and stockouts/overstock follow. |
| **Requisition Worksheet** (items with Replenishment System = Purchase or Transfer; reordering policies drive suggestions) | The standard answer for distribution: buyers run it daily/weekly per vendor or item filter, review action messages (new/change/cancel), and carry out to create POs. Fits when a purchasing team plans separately from production. | Manufacturing items with BOMs — the requisition worksheet doesn't plan production; use the planning worksheet. |
| **Planning Worksheet** (full MPS/MRP: regenerative or net-change) | Manufacturers: plans all levels — production, purchase, transfer — in one run; purchase suggestions can be handed to the requisition worksheet for a separate purchasing team. | Pure trading companies: MRP machinery and parameter discipline for no benefit — the requisition worksheet is the simpler correct tool. |
| **Order Planning** (manual, order-by-order) | Make-to-order one-offs and occasional demand, decided line by line. | **Do not mix** with req./planning worksheets: automated runs will change or delete supply orders created via Order Planning (documented behavior). Pick one regime. |
| **Demand-linked auto-POs** (drop ship/special order pulled into the req. worksheet via Get Sales Orders / Drop Shipment functions) | Direct-delivery businesses; keeps sales-linked purchases in the same buyer workflow. | — |

**Required client info:**
- Who buys today — dedicated buyers, warehouse, the owner? Per vendor or per category?
- Stocked-to-order ratio; are reorder points/quantities known or must they be derived from history?
- Manufacturing in scope now or later? (Determines requisition vs planning worksheet — and it's cheap to start on requisition and move up.)
- How often should suggestions run, and will someone actually review action messages? (Unreviewed MRP output destroys trust fast.)

**Interactions:** Suggestion quality is entirely a function of item planning parameters — reordering policy, lead times, safety stock — see [inventory.md](inventory.md#planning-parameters--reordering-policies). CTP promises from sales create requisition lines that land in this process — see [sales.md](sales.md#shipping-setup-shipment-methods-agents-order-promising--atp-ctp). Location-level planning needs SKUs ([inventory.md](inventory.md#stockkeeping-units)). Created POs then flow into [approvals](#purchase-approval-workflows--amount-limits).

**Add-on impact:** Aptean F&B adds shelf-life-aware and seasonal planning behavior on top of standard reordering policies — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Requisition worksheet for stocked purchased items with a named owner and a fixed cadence; planning worksheet only when manufacturing is live; manual POs for expenses and one-offs; never Order Planning alongside worksheet planning.

**Risk of getting it wrong:** medium — regimes can be changed, but a launch with bad planning parameters produces weeks of wrong suggestions and permanent user distrust ("we just ignore the worksheet").

**Expertise tags:** `#purchasing` `#planning` `#replenishment`

---

## Purchase approval workflows & amount limits

**Where:** **Approval User Setup** (Purchase Amount Approval Limit, Unlimited Purchase Approval, Request Amount Approval Limit for quotes, Approver ID, Substitute, Approval Administrator); **Workflows** page (Purchase Order / Purchase Invoice approval templates, Approver Limit Type = Approver Chain etc.); Workflow User Groups; optionally Power Automate.
**What it controls:** Whether purchase documents lock in *Pending Approval* until authorized, and how the approver is found: direct approver, approver chain climbing until someone's limit covers the amount (limits are in LCY), specific approver, or workflow user group.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| No approvals | Owner-operated businesses where the buyer is the owner. | Any delegation of purchasing authority; auditors will ask. |
| **PO approval with approver chain + amount limits** | The standard control: requester → line manager → whoever's limit covers it. Set Unlimited Purchase Approval for the top of the chain, substitutes for absence, and one Approval Administrator to unstick orphaned requests. | Chains deeper than 2–3 levels: each level adds latency to every urgent PO. Keep limits generous at level 1. |
| **Purchase invoice approval instead of (or besides) PO approval** | Clients where spend commitment happens outside BC (contracts) and the control point is AP; also catches non-PO invoices. | Approving both PO and its invoice for the same spend doubles friction — pick the control point deliberately. |
| Purchase **quote** approval via Request Amount Approval Limit | Formal requisition-then-tender processes. | Most SMBs — overkill. |
| Power Automate approvals (Teams/Outlook) | M365-centric approvers who won't log into BC. | Adds a second workflow platform to administer; native workflow is simpler to support. |

Watch the documented trap: a user who is both requester and approver in a workflow user group gets auto-approved. Keep requester and approver roles disjoint.

**Required client info:**
- The delegation-of-authority matrix: who may commit how much, in which currency (limits are LCY — agree the conversion stance)?
- Control point: commitment (PO) or payment (invoice)?
- Approver availability — substitutes, vacation coverage, and who is the approval administrator?

**Interactions:** Same Approval User Setup table serves [sales approvals](sales.md#salespeople-commission-tracking--sales-document-approvals) — design once. Over-receipt codes can require approval (below). Job queue/email must be configured for notifications ([finance.md](finance.md#email--job-queue-setup) or admin setup). Approvals delay PO release — factor into [lead times](inventory.md#planning-parameters--reordering-policies).

**Add-on impact:** None known beyond extra document types Aptean F&B may add; verify its documents are covered by workflow events — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** PO approval with a two-level approver chain and realistic limits, substitutes populated, one Approval Administrator, invoice approval only for non-PO spend.

**Risk of getting it wrong:** low–medium — reconfigurable at will; the operational risk is stuck documents when an approver leaves and no substitute/administrator exists.

**Expertise tags:** `#purchasing` `#workflow` `#internal-controls`

---

## Over-receipt codes & receiving tolerances

**Where:** **Over-Receipt Codes** page (Over-Receipt Tolerance %, Approval Required); assigned in the **Over-Receipt Code** field on the Item Card and/or Vendor Card; Over-Receipt Quantity field on purchase lines and warehouse receipt lines.
**What it controls:** Whether the warehouse may receive *more* than the ordered quantity, and by how much. Without a code, receipts are capped at the PO quantity; with one, Qty. to Receive may exceed it within the tolerance %, recorded in Over-Receipt Quantity.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| No over-receipt codes (hard cap at ordered qty) | Strict-compliance receiving; clients who want every excess handled as a vendor return or PO amendment. | Bulk/weight-based goods where +2–5% deliveries are normal — receivers end up faking quantities or receipts queue up unposted. |
| Tolerance code(s), e.g. OR5 = 5%, assigned per item or per vendor | Commodities, packaging, agricultural inputs — anywhere vendors legitimately ship over. Vendor-level assignment covers "this supplier always rounds up to full pallets". | Blanket-assigning a generous tolerance to everything: it quietly authorizes buying more than ordered, with no price agreement for the excess. |
| Tolerance code with **Approval Required** | Middle ground: over-receipt allowed but a workflow approval fires before it can be handled. | High-volume docks where the approval wait blocks put-away. |

Two hard caveats to tell clients: over-receipt does **not** work on orders created from blanket purchase orders, and BC does **not** handle the financial side — the vendor must send a corrected/extra invoice, and the price for the excess is whatever the PO line says. Under-receipt needs no code: receive less and close the line.

**Required client info:**
- Which vendors/commodities routinely over-deliver, and by what %?
- Does the client want to *keep* over-deliveries (discounts for keeping?) or return them?
- Should excess require sign-off before posting (Approval Required)?

**Interactions:** Applies on both purchase lines and [warehouse receipt lines](warehouse.md#require-receive). Invoice matching must expect quantity > ordered — brief AP, and align with [three-way-match expectations](#purchases--payables-setup--key-toggles). Excess stock lands in [planning](inventory.md#planning-parameters--reordering-policies) as extra supply.

**Add-on impact:** Aptean F&B catch-weight receiving changes what "quantity vs ordered" even means for weight-variable items; its tolerance handling may supersede standard over-receipt codes — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** One or two tolerance codes (e.g. 5% and 10%) assigned per vendor/item where over-delivery is a documented pattern; Approval Required only where the excess value is material; everything else stays hard-capped.

**Risk of getting it wrong:** low — codes can be added/removed anytime; the cost of omission is receiving-dock workarounds, the cost of excess is silent over-buying.

**Expertise tags:** `#purchasing` `#receiving` `#tolerances`

---

## Prepayments on purchase

**Where:** **Purchases & Payables Setup** (posted prepayment invoice/credit memo number series, Check Prepmt. when Posting); **General Posting Setup** → Purch. Prepayments Account; Prepayment % on vendor card, Purchase Prepayment Percentages (vendor×item), or per order.
**What it controls:** Formal handling of deposits the client must pay vendors before goods ship: a prepayment invoice is posted from the purchase order, the amount sits on a balance-sheet asset account, and it is automatically deducted when the final vendor invoice is posted against the order.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| No prepayment setup — deposits as manual vendor payments applied later | Rare, small deposits. | Import purchasing with contractual deposits: manual handling loses the link between deposit, order, and final invoice, and misstates assets vs expenses. |
| Full prepayment functionality with Purch. Prepayments Account per posting-group combination and vendor default % | Import/MTO supply chains where 30–50% deposits are standard; Check Prepmt. when Posting blocks receiving/invoicing before the prepayment is settled. | Very high PO volume with trivial deposits — admin overhead per order. |
| 100% prepayment (pay in full before shipment) | Pro-forma-invoice vendors. | Same tax-calculation warnings as the sales side in North America; test the VAT/tax regime first, and mind payment-discount interaction. |

**Required client info:**
- Which vendors demand deposits, at what % — flat per vendor or per deal?
- Must receiving be blocked until the deposit is paid?
- Jurisdictional VAT treatment of prepayments (unrealized VAT setup needed?).

**Interactions:** Needs Purch. Prepayments Account rows in [General Posting Setup](finance.md#posting-groups) and possibly [unrealized VAT](finance.md#vat-posting-setup). Deposit payments flow through [payment journals](finance.md#bank--payment-setup). Mirrors [sales prepayments](sales.md#prepayments-on-sales) — configure both sides in one workshop.

**Add-on impact:** None known.

**Default recommendation:** Set up the accounts during implementation regardless of current volume; default % only on vendors with contractual deposits; Check Prepmt. when Posting = on.

**Risk of getting it wrong:** medium — corrections go through prepayment credit memos; skipping the functionality entirely means vendor deposits sit unmatched in AP and inflate expense timing errors.

**Expertise tags:** `#purchasing` `#prepayments` `#finance`

---

## Drop shipment / special order — purchasing side

**Where:** **Purchasing Codes** page (flags: Drop Shipment, Special Order); Purchasing Code on sales lines (defaultable from the item card); **Requisition Worksheet** → *Drop Shipment — Get Sales Orders* and *Special Order — Get Sales Orders* functions (or create the PO and use Order → Drop Shipment → Get Sales Orders).
**What it controls:** How sales-driven purchases are generated and hard-linked. Drop shipment: vendor ships direct to the customer; posting the **purchase receipt** simultaneously posts the **sales shipment**, and the item never physically touches the client's warehouse. Special order: goods arrive at the client's own location but are rigidly linked/reserved to the originating sales order.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Generate linked POs via the requisition worksheet (Get Sales Orders functions) | Buyers already live in the req. worksheet; drop-ship demand appears in the same daily run and can be batched per vendor. | — (this is the clean pattern) |
| Create the PO manually and pull sales lines onto it | Occasional drop ships handled by AP/sales admin without worksheet routine. | High volume — manual pairing invites missed links. |
| Unlinked workaround: two independent orders keyed by hand | Never recommend; listed only because clients arrive doing this. | Always — no automatic shipment posting, no quantity sync, reconciliation by spreadsheet. |

Consultant caveats: the linked documents are **rigidly coupled** — quantity or date changes must be managed on the linked pair (change the sales line, then update the PO via the link, not independently); the purchase invoice and sales invoice still post separately; drop shipments bypass warehouse activities entirely (nothing to pick); item charges (freight) can still be assigned to the receipt for landed cost. For special orders, the link overrides normal reservation/planning logic — the received stock is not available to other orders even if it sits on the shelf.

**Required client info:**
- Share of revenue that is drop-shipped, and per which vendors?
- Who confirms vendor shipment to trigger posting the purchase receipt (which drives the sales shipment and thus revenue recognition timing)?
- Do drop-shipped items carry item tracking? (Lot/serial on goods the client never sees is an operational problem — see [inventory.md](inventory.md#item-tracking).)
- For special orders: genuine need for hard linking, or is normal reservation enough?

**Interactions:** Sales-side twin decision: [sales.md — Order handling flow](sales.md#order-handling-flow-quote--order--ship--invoice-blanket-orders-drop-shipments-special-orders). Drop-ship receipts post no warehouse documents — exclude these flows from [warehouse KPIs](warehouse.md#inbound-outbound-document-flow). Margin on drop-ship lines depends on purchase cost landing before the sales invoice — coordinate with [item charge / landed cost practice](inventory.md#item-charges--landed-cost). Over-receipt codes and blanket orders don't mix with these flows.

**Add-on impact:** Aptean F&B direct-store-delivery and brokerage scenarios extend drop-shipment handling (commissions, trade deductions on direct deliveries) — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Set up DROPSHIP and SPECORDER purchasing codes at go-live, default DROPSHIP on never-stocked items, and route creation through the requisition worksheet with a named owner.

**Risk of getting it wrong:** medium — the flows work well when linked, but unlinked or half-linked document pairs require manual cleanup, and posting the purchase receipt at the wrong time misstates revenue timing on the sales side.

**Expertise tags:** `#purchasing` `#drop-shipment` `#special-order`
