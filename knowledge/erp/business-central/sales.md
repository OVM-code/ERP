# Sales — Business Central (Standard)

> **Scope:** Microsoft Dynamics 365 Business Central (SaaS, current version)
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when the vendor releases functional changes to this area.

Covers the order-to-cash configuration in Business Central: Sales & Receivables Setup, customer master data governance, pricing and discounts, the document flow from quote to posted invoice, shipping and order promising, salespeople and approvals, prepayments, and intercompany sales. In scope for practically every implementation — even "finance-only" clients invoice something. The depth of each decision below depends on whether the client ships physical goods, sells services, or both.

---

## Sales & Receivables Setup — key toggles

**Where:** **Sales & Receivables Setup** page (search: "Sales & Receivables Setup").
**What it controls:** Company-wide defaults for how sales documents behave: credit checking, stockout warnings, what gets posted with an invoice, discount calculation, and cost application on returns. Most fields here are silent defaults that users never revisit — get them right in week one.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Credit Warnings = Both Warnings** (credit limit + overdue balance checked on document entry) | Clients with real credit-control discipline; B2B with meaningful credit exposure. Warning is advisory — posting is still allowed. | Cash-sale / prepaid businesses where the popups just train users to click through warnings. |
| **Credit Warnings = No Warning** | POS-like or prepaid flows; when credit control lives in an external tool. | Any client that has ever written off a receivable because "the system let us ship." |
| **Stockout Warning = On** | Trading companies where order entry should see availability problems immediately. | Large BOM/kit sales lines — this check is a documented performance drag on sales line entry. Turn it off company-wide and re-enable per item on the Item Card for the SKUs that matter. |
| **Shipment on Invoice = On** (posting a sales invoice also creates a posted shipment) | Service companies and simple traders who invoice without a separate ship step. | Clients using warehouse documents — shipping must happen through the warehouse flow, not as a side effect of invoicing. See [warehouse.md](warehouse.md#inbound-outbound-document-flow). |
| **Return Receipt on Credit Memo = On** | Mirror of the above for returns; fits the same simple profile. | Warehouse-managed returns. |
| **Default Posting Date = Work Date** vs **No Date** | *Work Date* is the standard convenience default. | *No Date* forces users to consciously pick a posting date — useful where period discipline is weak and month-end cutoff errors are recurring; pair with [Allowed Posting Period](finance.md#allowed-posting-dates). |
| **Default Quantity to Ship = Remainder** vs **Blank** | *Remainder* suits full-shipment businesses (less typing). | *Blank* is safer for clients who habitually part-ship: it forces explicit Qty. to Ship entry and prevents accidental full shipments. |
| **Calc. Inv. Discount = On** | Client actually grants invoice (total-amount) discounts; on orders the discount recalculates as lines are added. | Clients with no invoice-discount scheme — leaving it on just adds calculation noise and confuses margin analysis. |
| **Exact Cost Reversing Mandatory = On** | Almost always. Forces sales returns to be cost-applied to the original shipment entry so the return re-enters inventory at the original cost, not current average/FIFO cost. | High-volume returns where staff cannot identify the original shipment (they must fill Appl.-from Item Entry); but the better fix is training, not turning it off. |
| **Ext. Doc. No. Mandatory = On** | Clients whose customers require a PO reference on every invoice (most B2B, all EDI). | Genuine walk-in retail. |

**Required client info:**
- Do you enforce credit limits, and what happens today when a customer is over limit — block, warn, or escalate?
- Do you ever ship partially? Who decides the shipped quantity — sales admin or warehouse?
- Do your customers' POs have to appear on your invoices?
- What is your returns volume, and can staff trace a return to the original shipment?

**Interactions:** Exact cost reversing interacts directly with the [costing method](inventory.md#costing-method) — with Average or FIFO costing it is the only way returns don't distort margins. Shipment on Invoice conflicts with [warehouse shipment documents](warehouse.md#require-shipment). Default Posting Date pairs with [posting period controls](finance.md#allowed-posting-dates).

**Add-on impact:** Aptean Food & Beverage ERP layers trade management (rebates, promotions, bill-backs) on top of the standard discount toggles; if the client is on Aptean F&B, decide the discount architecture there first — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Credit Warnings = Both, Stockout Warning = On (Off for BOM-heavy catalogs), Shipment on Invoice = Off when warehouse docs are used, Exact Cost Reversing Mandatory = On, Ext. Doc. No. Mandatory = On for B2B, Calc. Inv. Discount only if a scheme exists.

**Risk of getting it wrong:** medium — all toggles are reversible, but Exact Cost Reversing left off with months of returns posted produces cost distortions that are painful (item ledger re-application) to repair, and Shipment on Invoice = On in a warehouse site creates ghost shipments outside the warehouse flow.

**Expertise tags:** `#sales` `#setup` `#costing`

---

## Customer templates & customer master data governance

**Where:** **Customer Templates** page (table "Customer Templ."); customer card; **Data Templates** / configuration templates for migration; VAT Reg. No. validation service in VAT setup.
**What it controls:** How new customers are created consistently: posting groups (customer, general business, VAT business), payment terms, currency, price/discount group assignments, dimensions. Templates are the main defense against the classic BC failure mode — a customer created with the wrong posting group silently posting receivables to the wrong G/L account.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| One template per customer segment (e.g. DOMESTIC, EU, EXPORT, INTERCOMPANY, CASH) | Nearly always. Segments should map 1:1 to posting group combinations and default payment terms. | Don't multiply templates for cosmetic differences (salesperson, territory) — those belong in manual entry or defaulting logic. |
| Open creation — any user creates customers free-form | Tiny teams (1–2 people) where the bookkeeper is the only creator anyway. | Any client with >1 order entry user; guaranteed posting-group drift within months. |
| Gated creation — templates + approval workflow on customer card changes (standard workflow template exists) | Clients with credit-control or compliance requirements (who can raise a credit limit?). | Adds friction; skip where the risk is low. |

**Required client info:**
- Who is allowed to create customers and change credit limits / payment terms today?
- What customer segments exist that differ in tax treatment, currency, or payment terms?
- Is there an external MDM/CRM that should own customer master (Dataverse/D365 Sales sync in play)?

**Interactions:** Templates carry the customer posting group and Gen. Bus. Posting Group — those must exist first; see [posting group architecture](finance.md#posting-groups). If Dynamics 365 Sales integration is on, decide the system of record before go-live. Customer price group / discount group fields feed the [pricing model](#sales-pricing-model-price-lists-vs-legacy).

**Add-on impact:** Aptean F&B adds food-trade attributes (delivery schedules, route codes, trade agreement links) to the customer card; extend the templates accordingly — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** 4–6 templates mapped to posting-group segments, customer creation restricted by permission set, approval workflow only on credit-limit changes.

**Risk of getting it wrong:** medium — wrong posting groups are correctable but every posted document until discovery hits the wrong receivables/revenue accounts, and reclassification at audit time is expensive.

**Expertise tags:** `#sales` `#master-data` `#governance`

---

## Sales pricing model (Price Lists vs legacy sales prices; discount hierarchy)

**Where:** **Feature Management** → "Feature Update: New sales pricing experience"; then **Sales Price Lists** page (new) or **Sales Prices / Sales Line Discounts** pages (legacy). Defaults on Sales & Receivables Setup (Default Price List, Allow Editing Active Price).
**What it controls:** How unit prices and line discounts are found when a line is entered. BC always runs a "best price" calculation across all applicable prices/discounts for the customer–item–quantity–date–UoM–currency combination. The new experience organizes everything into price lists with Draft/Active status; legacy stores loose price records per customer/price group/all customers.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **New Price Lists experience** (enable in Feature Management) | All new implementations. Draft→Active status gives change control, Suggest Lines/Copy Lines + Edit in Excel handle mass maintenance, Applies-to targeting is clearer. Microsoft's stated direction; legacy pages get no new investment and the feature update is on the mandatory-features track. | An existing tenant with heavy ISV customization against the old price tables (Sales Price table 7002) — verify ISV compatibility before enabling, because **enabling the feature update runs a one-way data conversion and cannot be switched back off**. |
| Legacy sales prices | Only as a transitional state on an existing tenant you're not ready to convert. | Any greenfield project. |
| Pricing structure: all-customer default list + customer price group lists + per-customer exceptions | The maintainable hierarchy for most clients. | Per-customer price lists for thousands of customers — usually a sign the client should be using price groups plus a discount scheme instead. |
| Line discounts via **item discount groups × customer discount groups** | Matrix-style trade discounting (wholesale). | Clients whose "discounts" are really net-price agreements — model those as prices, not discounts, so margin reporting stays honest. |

Discount hierarchy to explain to the client: **unit price** (best price wins among applicable) → **line discount %** (best discount wins) → **invoice discount** (document total threshold, per customer's Invoice Disc. Code, auto-calculated only if Calc. Inv. Discount is on). Line and invoice discounts stack; two line discounts do not.

**Required client info:**
- How many price levels exist (list, wholesale, key accounts, promo), and how many genuine per-customer deals?
- Who maintains prices, how often, and in what tool today (Excel almost always — Edit in Excel is the selling point)?
- Are discounts margin-tracked separately from price (trade-discount reporting requirement)?
- Any ISV apps touching pricing?

**Interactions:** Price group / discount group fields default from [customer templates](#customer-templates--customer-master-data-governance). Prices incl./excl. VAT per list must align with [VAT posting setup](finance.md#vat-posting-setup). Campaign pricing ties into marketing/contact setup.

**Add-on impact:** Significant. Aptean F&B replaces/extends standard pricing with trade management: commodity-based pricing, price change management, rebates and accruals, promotions. On an Aptean F&B project, standard price lists typically only carry base prices — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Enable the new Price Lists experience on every new tenant, structure as one default list + price-group lists + exception lists, and keep Allow Editing Active Price off so changes go through Draft.

**Risk of getting it wrong:** high-irreversible for the feature switch itself (one-way conversion of existing price data); medium for the structure — restructurable, but every restructure risks a window of wrong prices on live orders.

**Expertise tags:** `#sales` `#pricing` `#feature-management`

---

## Order handling flow (quote → order → ship → invoice; blanket orders; drop shipments; special orders)

**Where:** Document types on the Sales menu; **Sales & Receivables Setup** (Archive Quotes/Orders, Default Quantity to Ship); **Purchasing Codes** page for drop ship/special order; user-level **Invoice Posting Policy** (Prohibited / Allowed / Mandatory ship-and-invoice).
**What it controls:** Which document path each sales scenario takes, and therefore what users see, what gets archived, and where inventory and revenue postings happen.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Full flow: Quote → Order → post Shipment → post Invoice (separately) | Physical goods, part-shipments, warehouse involvement, invoice batching (combine shipments onto one invoice per period). | Pure service billing — the extra ship step is ceremony. |
| Order → post Ship+Invoice in one action | Small traders, counter sales, full shipments only. Enforce per user via Invoice Posting Policy if some roles may ship but not invoice. | Clients that combine multiple shipments per invoice, or where warehouse posts shipments. |
| Sales Invoice document directly (no order) | Services, recurring fees, miscellaneous charges. | Anything needing partial delivery tracking or warehouse handling. |
| **Blanket order** → releases as linked sales orders | Framework agreements: agreed quantity/price over a period, called off in parts. Gives commitment visibility and price lock. | Don't use blanket orders as a pricing tool — that's what price lists with ending dates are for. Note over-receipt logic and some promising features don't apply to blanket-linked orders. |
| **Drop shipment** (Purchasing Code with Drop Shipment; vendor ships direct to customer) | Goods the client never wants to touch physically. Sales line links 1:1 to a purchase order; posting the purchase receipt posts the sales shipment; item never enters inventory quantity-wise on the client's floor but still flows through item ledger. | Items needing inspection/QA before customer receipt; lot-controlled goods where the client must record lot data they never see (painful — see [inventory.md](inventory.md#item-tracking)). |
| **Special order** (Purchasing Code with Special Order; goods come into own warehouse but are reserved hard to the sales order) | Customer-specific procurement that must not be consumed by other orders, but ships from own dock (consolidation with stock lines). | Standard stocked items — hard linking removes planning flexibility. |

**Required client info:**
- Do quotes need formal versioning/archiving for audit or CRM reasons? (Turn on Archive Quotes/Orders.)
- Are invoices per shipment or consolidated per period/customer? (Drives Combine Shipments batch usage and the separate-invoice flow.)
- What share of sales is drop-shipped, and do those vendors confirm shipment dates reliably?
- Should order entry staff be able to invoice? (Invoice Posting Policy per user.)

**Interactions:** Drop shipments and special orders require the purchasing side configured identically — see [purchasing.md — Drop shipment / special order](purchasing.md#drop-shipment--special-order-purchasing-side). Ship-then-invoice separation depends on [warehouse document choice](warehouse.md#require-shipment). Combine Shipments affects customer statement/invoicing cadence in [finance.md](finance.md#receivables-management).

**Add-on impact:** Aptean F&B adds catch-weight and delivery-trip handling into the order flow; order line UoM/weight behavior changes materially — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Full quote→order→ship→invoice for goods with archiving on; direct invoices for services; blanket orders only where genuine call-off agreements exist; purchasing codes set up on day one even if drop shipping is "rare" — it never is.

**Risk of getting it wrong:** low–medium — document flow habits are re-trainable, but retrofitting drop-shipment links onto manually-keyed pairs of orders is manual reconciliation misery.

**Expertise tags:** `#sales` `#order-to-cash` `#drop-shipment`

---

## Shipping setup (shipment methods, shipping agents, order promising / ATP–CTP)

**Where:** **Shipment Methods** (incoterms), **Shipping Agents** + **Shipping Agent Services** (carrier + service level with shipping time D-formula), **Order Promising Setup** (offset, worksheet template), plus Outbound Whse. Handling Time on Location / Inventory Setup and Shipping Time on customer/SKU.
**What it controls:** Delivery-date arithmetic on every order line (Shipment Date + Outbound Handling = Planned Shipment; + Shipping Time = Planned Delivery), incoterm printing on documents, package tracking links, and whether BC can *promise* dates it can't meet from stock.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Minimal: shipment methods only, no agents, no handling times | Service clients; goods clients where delivery dates are managed by phone and gut feel (be honest about this in scoping). | Anyone who later wants reliable Planned Delivery Dates — retro-fitting handling/shipping times invalidates open-order dates. |
| Full date setup: agents + services with shipping time, outbound handling time per location | Distribution clients quoting delivery dates to customers; prerequisite for meaningful ATP. | Overkill if all shipping is "next truck, same day". |
| **ATP (Available-to-Promise)** on demand from the order line | Checks unreserved inventory + scheduled receipts to validate/compute the earliest ship date. Good default for stocked goods. | Items with heavy reservations (ATP sees only unreserved qty) or made-to-order items with no scheduled supply — dates come back blank. |
| **CTP (Capable-to-Promise)** | Make/buy-to-order: simulates the earliest date if the item were produced/purchased/transferred now; accepting the date creates requisition lines and a reservation. | Clients without planning discipline: CTP silently creates requisition worksheet lines and reservations that someone must own; if no one runs the [requisition process](purchasing.md#requisition-flow-quotesorders-vs-requisition-worksheet-vs-planning-worksheet), CTP promises rot. Also calculation-heavy. |

**Required client info:**
- Do you promise delivery dates at order entry, and how do you calculate them today?
- Which carriers/service levels exist and are their transit times stable enough to encode?
- How long from pick release to truck (outbound handling time), per location?
- For out-of-stock items: quote a lead-time date (CTP) or just say "backordered"?

**Interactions:** Handling times sit on Locations — coordinate with [warehouse.md](warehouse.md#location-setup). CTP writes into the requisition worksheet — coordinate ownership with [purchasing.md](purchasing.md#requisition-flow-quotesorders-vs-requisition-worksheet-vs-planning-worksheet). Reservation policy on items ([inventory.md](inventory.md#reservations)) directly changes ATP results. The Sales Order Agent (Copilot) uses this same Order Promising Setup if the client adopts it.

**Add-on impact:** Aptean F&B route/delivery-trip planning typically supersedes plain shipping-agent dates for DSD-style distribution — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Always set up shipment methods (documents look amateur without incoterms) and shipping agents with realistic shipping times; enable ATP usage for stocked goods; introduce CTP only once requisition-worksheet ownership is established.

**Risk of getting it wrong:** low — all reconfigurable; the real risk is credibility (systematically wrong promised dates) rather than data damage.

**Expertise tags:** `#sales` `#shipping` `#order-promising`

---

## Salespeople, commission tracking & sales document approvals

**Where:** **Salespeople/Purchasers** page (Commission % field); Salesperson Code on customer/document; **Approval User Setup** (Sales Amount Approval Limit, Unlimited Sales Approval, Salespers./Purch. Code); **Workflows** page (sales document approval templates).
**What it controls:** Attribution of sales to people (for reporting and commission), and whether sales documents (quotes, orders, invoices, credit memos) require approval before release.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Salesperson codes for attribution only; commission computed outside BC | Almost everyone. Be blunt with clients: BC stores a Commission % and reports commission on posted entries, but has **no native commission settlement/payout engine**. Reporting + payroll handoff, or an ISV, does the payout. | Complex plans (tiers, splits, clawbacks) — scope an ISV or Power BI + manual payroll from the start, don't promise standard BC will do it. |
| No sales approvals | Small trusted teams; speed-critical order entry. | Clients with discount-authority or credit-exposure rules that today live in a manager's inbox. |
| Sales document approval workflow, approver-chain by **Sales Amount Approval Limit** | Enforces "orders above X need manager sign-off" natively; document locks in Pending Approval status until released. | High-volume order entry where every order would exceed limits — approvals become rubber-stamping and delay shipping; use credit-limit warnings or targeted workflows (credit memo only) instead. |
| Targeted approvals only: **sales credit memos** and/or customer card changes | The 80/20 answer: fraud/margin risk concentrates in credit memos and credit-limit edits, not in ordinary orders. | — |
| Power Automate flows instead of native workflow | Client already lives in Teams/M365 approvals; modern UX. | Offline/latency concerns; another admin surface to govern. |

**Required client info:**
- Are commissions actually paid on posted sales, and what's the plan structure? (Determines ISV-vs-reporting answer.)
- What needs a second pair of eyes: all orders, orders over a threshold, discounts over a %, or only credit memos?
- Who are approvers and substitutes, and do they work in BC or only in email/Teams?

**Interactions:** Approval limits are LCY — multi-currency clients see limits applied to converted amounts ([finance.md](finance.md#currencies)). Credit memo approvals complement [Exact Cost Reversing](#sales--receivables-setup--key-toggles) as return controls. Purchase-side approvals share the same Approval User Setup — configure both at once, see [purchasing.md](purchasing.md#purchase-approval-workflows--amount-limits).

**Add-on impact:** Aptean F&B trade-management deductions and rebates change what "commissionable revenue" means; align commission reporting with the trade ledger — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Salesperson codes mandatory on customers (attribution), commission via reporting, approvals only on credit memos and above-threshold orders with one substitute per approver and the approval administrator named.

**Risk of getting it wrong:** low — workflows toggle on/off freely; the common failure is over-engineering approvals then disabling them all after go-live week.

**Expertise tags:** `#sales` `#workflow` `#commission`

---

## Prepayments on sales

**Where:** **Sales & Receivables Setup** (Posted Prepmt. Inv./Cr. Memo number series, Check Prepmt. when Posting); **General Posting Setup** → Sales Prepayments Account per posting-group combination; Prepayment % on customer card, Sales Prepayment Percentages page (customer×item), and per order.
**What it controls:** Whether the client can demand deposits against sales orders as formal posted prepayment invoices, with the deposit held on a balance-sheet liability account and automatically deducted on the final invoice.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| No prepayment setup; deposits handled as manual customer payments applied later | Rare deposits, simple VAT regime; avoids setting up prepayment accounts per posting group. | Clients where deposits are contractual and need a proper invoice with VAT — manual handling breaks VAT timing and statement clarity. |
| Full prepayment functionality (accounts in General Posting Setup, default % on customer or customer×item, Check Prepmt. when Posting = on) | Made-to-order, project-like sales, high-value equipment: invoice 30–50% before work starts; system blocks shipping until prepayment is paid when the check toggle is on. | Very high document volume with small deposits — the extra invoice/credit-memo cycle per order is real admin load. |
| 100% prepayment | Pro-forma-style full payment before shipment. | **North America:** Microsoft explicitly warns against 100% due to sales-tax calculation issues; also breaks payment-discount deduction. Use 100% only where tested for the tax regime, and set the Invoice Rounding Account on customer posting groups (required for rounding offsets). |

**Required client info:**
- Are deposits contractual, and must they be VAT-bearing invoices in this jurisdiction?
- Should the system *block* shipment/invoice until the prepayment is settled (Check Prepmt. when Posting)?
- One deposit per order or staged prepayments?

**Interactions:** Requires prepayment G/L accounts and possibly separate VAT product posting groups for 100% cases — coordinate with [posting groups](finance.md#posting-groups) and [VAT setup](finance.md#vat-posting-setup); unrealized VAT regimes add setup. Prepayment invoices post through the normal number series — reserve dedicated series. Purchase-side twin: [purchasing.md — Prepayments](purchasing.md#prepayments-on-purchase).

**Add-on impact:** None known.

**Default recommendation:** Configure the accounts even if usage is "occasional" (retrofitting General Posting Setup lines later is annoying), default % only on the few customers with contractual deposits, Check Prepmt. when Posting = on.

**Risk of getting it wrong:** medium — posted prepayment invoices are corrected via prepayment credit memos only; NA clients on 100% prepayment can hit genuine tax-calculation errors.

**Expertise tags:** `#sales` `#prepayments` `#finance`

---

## Intercompany sales (brief)

**Where:** **Intercompany Setup**, **Intercompany Partners**, IC Chart of Accounts / IC Dimensions mapping, IC Inbox/Outbox; customer card flagged with IC Partner Code.
**What it controls:** Whether a sales order to a sister company automatically generates the corresponding purchase document in the partner company (and vice versa), eliminating double keying and mismatched intercompany balances.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| No IC functionality — sister companies keyed as normal customers | One-off intra-group sales; partner not on BC. | Recurring intra-group trade: guaranteed reconciliation pain at consolidation. |
| Standard IC (partners, mapped IC COA/dimensions, auto-send through IC outbox) | Both entities in BC (same or different environments); moderate document volume. Works with sales orders/invoices and returns; combine with IC G/L journals for cost recharges. | Heavily customized document flows or third-party ERP counterparties — IC is BC-to-BC. |
| IC + drop shipment patterns for central-purchasing groups | Group where one entity buys and others sell. | Complexity multiplies; prototype before promising. |

**Required client info:**
- Which group entities trade with each other, on which system, and at what volume?
- Transfer-pricing rules (who sets IC prices — a dedicated IC price list?).
- Consolidation approach and IC elimination requirements (see [finance.md](finance.md#consolidation--intercompany)).

**Interactions:** IC COA/dimension mapping depends on [chart of accounts and dimension design](finance.md#dimensions) being stable in both companies first. IC customers still need posting groups from [templates](#customer-templates--customer-master-data-governance) — use a dedicated IC segment.

**Add-on impact:** None known specific to IC; verify Aptean F&B document extensions survive the IC document transfer if both entities run it — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** If both entities run BC and trade monthly or more often, implement IC from the start; otherwise defer but name IC customers/vendors consistently so a later switch-on is clean.

**Risk of getting it wrong:** low–medium — can be adopted later; the cost of skipping it is ongoing reconciliation labor, not data damage.

**Expertise tags:** `#sales` `#intercompany` `#multi-company`
