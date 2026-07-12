# Sales — Odoo (Standard)

> **Scope:** Odoo 19 Enterprise (Odoo Online, Odoo.sh or on-premise); Community edition differences flagged inline
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when Odoo releases functional changes to this area (one major release per year, typically October).

Covers the order-to-cash configuration in the Odoo Sales app: customer master data on the shared contacts model, pricelists and discount policy, the quotation-to-order flow with online signature and payment, invoicing policy and down payments, delivery methods and carrier connectors, sales teams and the CRM boundary, the customer portal, returns and credit notes, margins and commissions, and subscriptions. In scope for practically every implementation — even service-only clients quote and invoice something. Odoo's sales flow is opinionated and portal-centric by design; the main consulting work is deciding which of its conveniences to switch on, not building the flow.

---

## Customer master data (contacts model)

**Where:** **Contacts** app; contact form (Company/Individual toggle, child contacts under the "Contacts & Addresses" tab); VAT field on the contact; **Accounting → Settings → Verify VAT Numbers** (VIES check).
**What it controls:** Odoo has **one partner model (`res.partner`) for customers, vendors, contacts and addresses** — there is no separate customer table. A record becomes "a customer" simply by appearing on a sales document. Structure and discipline here determine whether receivables, statements and Peppol e-invoices land on the right legal entity.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Company record + child contacts/addresses** (invoice address, delivery addresses, contact persons as children of the company) | The correct pattern for all B2B. Orders default invoice/delivery addresses from the children; statements and dunning consolidate on the parent. Flat Individual records are for genuine B2C only. | The anti-pattern to prevent: B2B customers keyed as loose Individuals — orders scatter across duplicate person records with no consolidated receivable. |
| Free-form contact creation by any sales user | Tiny teams. Odoo lets anyone with Sales access create partners inline from an order — convenient and dangerous. | More than 2–3 order-entry users: duplicates accumulate within weeks. Name a creation owner and run the built-in duplicate-merge tool as a routine, not a rescue. |
| **VIES VAT validation on** | Any client selling intra-EU: VAT numbers are checked against VIES on entry — also your evidence trail for zero-rating intra-EU B2B sales. | — (leave it on; it validates the number, it does not block sales). |

**Required client info:**
- Who is allowed to create customers today, and is there an existing CRM/MDM that should stay the system of record?
- What share of customers are companies with multiple ship-to addresses or a separate invoicing entity — and how dirty is the legacy customer file (dedupe before migration, not after)?

**Interactions:** The partner's country and VAT number drive automatic [fiscal position mapping for intra-EU VAT](finance.md#taxes-vat-return--fiscal-positions-belgian-vat). Correct legal-entity data is a hard prerequisite for [Peppol e-invoicing](finance.md#e-invoicing--peppol) — Belgian B2B invoices travel via Peppol, and a mis-keyed VAT number means undeliverable invoices. Payment terms default from the partner — see [payment terms](finance.md#payment-terms-follow-ups--payment-methods). Per-salesperson visibility of customers is a record-rule decision — see [users & record rules](general-setup.md#users-access-rights--record-rules).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Company-with-children structure for all B2B, VIES validation on, partner creation open but with a named data owner and a monthly duplicate-merge routine; migrate only deduplicated customers.

**Risk of getting it wrong:** medium — everything is editable, but merging months of duplicate partners with posted invoices is tedious, and wrong VAT/entity data on Peppol invoices fails at the customer's door, not yours.

**Expertise tags:** `#sales` `#master-data` `#governance`

---

## Pricelists & discount policy

**Where:** **Sales → Configuration → Settings → Pricing** (Pricelists, Discounts toggles); **Sales → Products → Pricelists**; pricelist per customer on the contact's Sales & Purchase tab; **Discount & Loyalty** programs under Sales → Products.
**What it controls:** How the unit price on every order line is found: base list price, per-pricelist fixed prices, or computed rules (discount or formula on another price), selectable per customer, currency, quantity break and date range — and whether discounts appear as an explicit % on the line or are silently baked into the unit price.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Pricelists off** — one sales price per product | Single-price businesses, most small service clients. The cleanest answer; don't switch pricelists on "just in case". | Multi-currency selling (a pricelist per currency is the standard mechanism) or any negotiated customer pricing. |
| **Pricelists with fixed prices per product** | A handful of price levels (list / wholesale / key accounts) maintained by hand. | Hundreds of products × several levels — maintenance dies in the UI; use rule-based lists. |
| **Pricelists with computed rules** (discount % or formula on list price/cost/another pricelist, per product category or all products, with quantity breaks and validity dates) | Structured trade pricing: "wholesale = list −20%", promo periods. Rules cascade — a customer list defined relative to the base list follows base-price changes automatically. | Clients who cannot articulate pricing as rules — model those as fixed prices and accept the maintenance. |
| **Discounts shown on the line** (explicit discount % field) vs **discount included in price** | Show the discount when customers negotiate from list price and expect "−15%" on the quote; margin reporting stays honest against list. | Hiding the discount (net price on the line) fits net-price agreements — but then never call it a discount in reporting. |
| **Discount & Loyalty programs** (promotions, coupon codes, loyalty points, gift cards/eWallet) | Retail/e-commerce mechanics: buy-X-get-Y, order-total promos, free-shipping promos. | B2B trade pricing — promotions are the wrong tool for negotiated structural pricing; keep those in pricelists. |

Pitfall to explain to the client: the pricelist engine applies the **first matching rule** for the customer's pricelist, quantity and date — not a "best price wins" search across lists like some ERPs — so test quantity breaks and date overlaps with real cases; and be deliberate about rules computing from **list price vs cost**, because cost-based formulas move with every cost change under AVCO/FIFO. ⚠️ The pricelist settings were reorganised in recent versions (the old "multiple prices" vs "advanced rules" split has been consolidated) — verify exact labels against current Odoo documentation.

**Required client info:**
- How many genuine price levels, per-customer deals and selling currencies exist? Can pricing be expressed as rules off a base list?
- Must the customer see list price and discount separately on documents — and who owns pricelist maintenance after go-live (in what tool today)?

**Interactions:** Pricelist currency must match the customer invoicing currency; prices tax-included vs tax-excluded per pricelist is a classic B2C/B2B trap — see [taxes & fiscal positions](finance.md#taxes-vat-return--fiscal-positions-belgian-vat). Cost-based formula rules depend on the [costing method](inventory.md#product-categories--costing-method-standard--avco--fifo). Quotation templates carry pricelist context — see [quotation flow](#quotation-flow-templates-online-sign--pay); margin display reacts to discounts — see [margins & commissions](#margins--commissions).

**Add-on impact:** None yet — this knowledge base carries no Odoo add-on layers for pricing.

**Default recommendation:** Pricelists off for single-price clients; otherwise one base list plus rule-based level lists (% off base), discounts shown explicitly on the line, and loyalty/promotion programs only where retail mechanics genuinely exist.

**Risk of getting it wrong:** medium — pricelists are restructurable, but every restructure opens a window of wrong prices on live quotes, and discount-hidden-in-price decisions are near-impossible to unpick in historical margin reporting.

**Expertise tags:** `#sales` `#pricing` `#pricelists`

---

## Quotation flow (templates, online sign & pay)

**Where:** **Sales → Configuration → Settings** (Quotation Templates, Online Signature, Online Payment, Default Quotation Validity, Lock Confirmed Sales); **Sales → Configuration → Quotation Templates** (lines, optional products, per-template signature/payment requirements).
**What it controls:** How fast and how consistently quotes go out, and what gate a quotation must pass (nothing / customer e-signature / online payment of a % or all) before it becomes a confirmed sales order. This is Odoo's signature strength — the quote is a portal web page the customer can accept and pay on, not just a PDF.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Quotation templates** with predefined lines, standard terms and validity | Any repetitive quoting (service packages, standard bundles) — most clients need 3–6 templates; free-form quotes remain available for bespoke deals. | Don't multiply templates per customer — customer-specific pricing belongs in [pricelists](#pricelists--discount-policy). |
| **Optional products** on templates/quotes | Structured upsell: the customer ticks options in the portal and the order updates itself. | Catalogues where "options" are really engineering variants — that's a product-configurator problem, not an optional-products one. |
| **Online signature required** to confirm | The standard B2B gate: customer signs in the portal, order confirms itself, audit trail attached. | Customers who confirm by PO over email/EDI only — keep manual confirmation and record the PO in the Customer Reference field. |
| **Online payment required** (full or a down-payment %) to confirm | B2C and prepaid B2B: confirmation and cash arrive together. Requires a payment provider configured. | Credit-term B2B — demanding card payment on order insults customers who pay on 30-day terms. |
| **Lock Confirmed Sales = on** | Confirmed orders become read-only; changes take a documented amendment path. Fits audit-sensitive or high-dispute clients. | Businesses that legitimately edit open orders daily (part-deliveries, substitutions) — locking breeds workaround culture. |

**Required client info:**
- How does a customer accept a quote today — signature, email "OK", PO number? Will their customers actually use a portal link, and should confirmation ever be possible without signature/payment (sales override)?
- What quote validity is standard, and how many distinct standard offerings exist (→ number of templates)?

**Interactions:** Online payment needs a payment provider and journal — see [payment methods](finance.md#payment-terms-follow-ups--payment-methods); a required down-payment % at confirmation creates a down-payment invoice — see [down payments](#invoicing-policy--down-payments). Quote PDFs use the company [document layout](general-setup.md#document-layouts--report-templates); numbering follows the sales [sequence](general-setup.md#document-numbering-sequences). Confirmation triggers the delivery order per the product's route — see [routes](inventory.md#routes--procurement-rules-architecture-mtobuymanufacture).

**Add-on impact:** No add-on overlays recorded for Odoo in this knowledge base yet.

**Default recommendation:** Templates for every repeatable offering, 30-day default validity, online signature on for B2B, online payment only for prepaid segments (as a down-payment % where deposits are contractual), Lock Confirmed Sales off unless audit requirements say otherwise.

**Risk of getting it wrong:** low — all toggles are reversible and quote habits retrain quickly; the real cost of skipping templates is permanent quote inconsistency, not damage.

**Expertise tags:** `#sales` `#order-flow` `#quotations`

---

## Invoicing policy & down payments

**Where:** Per product: **Invoicing Policy = Ordered quantities / Delivered quantities** (product form, sales tab; company default under Sales → Configuration → Settings). Invoice creation via **Create Invoice** on the sales order (Regular invoice / Down payment % / Down payment fixed amount); batch invoicing from the order list; down-payment product and its income account under Sales settings.
**What it controls:** *When* revenue can be invoiced — on order confirmation or only for what was actually delivered — and how deposits are handled. This is set per **product**, not per customer, which surprises consultants coming from other ERPs.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Ordered quantities** | Services billed on commitment, prepaid goods, simple resellers who always ship complete. Invoice available immediately at confirmation. | Part-shipping goods businesses — you will invoice what hasn't shipped, and correcting with credit notes becomes routine. |
| **Delivered quantities** | The safe default for physical goods: the invoiceable quantity follows validated deliveries, so invoice = what left the warehouse. For services, "delivered" means timesheets or milestones — see [service invoicing policies](projects-service.md#service-invoicing-policies-tm-fixed-milestones). | Clients who never track deliveries in Odoo (no Inventory app) — nothing ever becomes invoiceable. |
| **Down payments** (percentage or fixed, from the Create Invoice wizard) | Contractual deposits on made-to-order or project sales: the down payment posts as a real invoice against a dedicated down-payment product/account and is deducted automatically on the final invoice. | High-volume small deposits — each one is a full invoice cycle. Review the down-payment product's income account and tax with the accountant; the default is rarely what a Belgian accountant wants. |
| **Batch invoicing** (select many orders → one run; optionally consolidated per customer) | Weekly/monthly invoicing cadence, many small orders per customer. | Customers who demand one invoice per PO — consolidation merges orders and confuses their AP matching. |

**Required client info:**
- Do they ever ship partially, and what is the invoicing cadence — per order, per delivery, or consolidated per period/customer? Part-shipping makes delivered quantities close to non-negotiable.
- Are deposits contractual, and must they be VAT-bearing invoices (in Belgium: yes — a down-payment invoice is a real invoice with VAT due)? Who raises invoices — sales admin from the SO, or finance in batch?

**Interactions:** Invoicing from delivered quantities requires the delivery flow to be real — see [outbound steps](warehouse.md#inboundoutbound-steps-the-complexity-ladder). Under anglo-saxon accounting COGS posts at invoicing and must align with this policy — see [continental vs anglo-saxon accounting](finance.md#continental-vs-anglo-saxon-accounting--automatic-accounts); Belgian clients normally run continental, where the linkage is softer but still audit-relevant. Customer invoices go out via [Peppol](finance.md#e-invoicing--peppol) — Belgian B2B e-invoicing is mandatory, so the invoice is the legally load-bearing document. Down-payment gates at quote confirmation are set in the [quotation flow](#quotation-flow-templates-online-sign--pay).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Delivered quantities as the company default for goods (and for services where timesheets exist), ordered quantities per product only where commitment billing is explicit, down-payment product/account configured with the accountant on day one even if deposits are "occasional".

**Risk of getting it wrong:** medium — the policy is changeable per product at any time, but months of invoices raised on ordered-but-undelivered quantities means a trail of credit notes, and a mis-accounted down-payment product distorts revenue until someone notices.

**Expertise tags:** `#sales` `#order-flow` `#down-payments` `#prepayments`

---

## Delivery methods & shipping connectors

**Where:** **Inventory/Sales → Configuration → Settings → Delivery Methods** (enable), then **Delivery Methods** records (provider: fixed price / based on rules / third-party connector); connector modules per carrier (bpost, DHL, UPS, FedEx, Sendcloud, …).
**What it controls:** How shipping is charged on the order (flat, rule-computed from weight/volume/order total, or live carrier rates) and whether Odoo talks to the carrier at all (label printing, tracking numbers pushed to the delivery and customer portal).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Fixed price** per method, optionally free above an order-amount threshold | The pragmatic default: "€12 shipping, free above €250" — the threshold lives on the delivery method itself. Beats free-typed "Transport" lines, which have no rules and no reporting. | Freight costs that genuinely vary by weight/destination and matter to margin. |
| **Based on rules** (price from weight/volume/quantity/order total, per destination) | Parcel businesses with a rate card they maintain themselves. | Rate cards that change quarterly per carrier — that's what connectors are for. |
| **Third-party carrier connectors** (bpost, DHL, UPS, FedEx, Sendcloud and others): live rates, label generation, tracking number back onto the delivery and portal | Real parcel volume with a supported carrier; Sendcloud as multi-carrier aggregator is often the fastest route in Benelux. **Community edition:** carrier connectors are Enterprise features — on Community, use fixed/rule pricing or the carrier's own tooling. ⚠️ Connector list and edition availability shift between releases — verify against current Odoo documentation. | Low volume (a handful of parcels a week — setup and carrier-contract wrangling isn't worth it), or carriers not on the supported list. |

**Required client info:**
- Who physically ships — own vehicles, one parcel carrier, or several — and is shipping charged to the customer, by what logic (flat, threshold, weight)?
- Are product weights/volumes actually maintained? Rule-based and connector pricing die without them.

**Interactions:** Delivery methods attach shipping to the **delivery order**, so the outbound flow must exist — see [outbound steps](warehouse.md#inboundoutbound-steps-the-complexity-ladder) and [delivery packaging & shipping integration](warehouse.md#delivery-packaging--shipping-integration). Free shipping can also come from [loyalty programs](#pricelists--discount-policy) — pick one mechanism, not both. Shipping charges are VAT-relevant lines and follow [fiscal positions](finance.md#taxes-vat-return--fiscal-positions-belgian-vat) like any other line.

**Add-on impact:** Nothing recorded — this knowledge base has no Odoo add-on layers yet.

**Default recommendation:** Fixed price with a free-shipping threshold for most SMEs; a connector (bpost or Sendcloud in Belgium) only once parcel volume justifies label automation — and only after product weights are clean.

**Risk of getting it wrong:** low — methods are freely editable; the recurring failure is rule-based pricing on top of empty weight fields, which silently charges the fallback price on every order.

**Expertise tags:** `#sales` `#shipping`

---

## Sales teams & CRM boundary

**Where:** **Sales → Configuration → Sales Teams** (team, leader, members, invoicing target); salesperson field on customer and order; the separate **CRM app** (pipeline of leads/opportunities) if installed.
**What it controls:** Attribution and reporting structure for sales (who sold what, per team), and — the bigger decision — whether pre-order pipeline management (leads, opportunities, activities, stages) is in scope at all. Sales teams exist with the Sales app alone; installing CRM adds the pipeline in front of quotations.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Sales app only, one default team, salesperson attributed per customer/order | Order-entry businesses: dealers, wholesalers, repeat-order B2B. Quotes are created directly; no pipeline ceremony. Add teams (inside/field/export/webshop) only when reporting and targets genuinely follow them. | Clients who genuinely chase deals and need funnel/forecast visibility. |
| **CRM app in scope**: leads/opportunities pipeline feeding quotations | Deal-driven selling with a funnel worth managing; CRM is in both editions and integrates natively (opportunity → new quotation). Scope it properly: stages, lost reasons, activity discipline, a named pipeline owner. | Never half-install CRM "because it's free": an empty pipeline nobody updates poisons trust in every other number in the system. Decide explicitly — either the pipeline is a managed process with an owner, or CRM stays uninstalled. |

**Required client info:**
- Is there a pre-order sales process worth managing (funnel, follow-ups, win/loss), or do orders simply arrive?
- Who would maintain the pipeline daily — and does that person exist?

**Interactions:** Salesperson and team default from the customer record — see [customer master data](#customer-master-data-contacts-model). Whether salespeople see only their own customers/orders is a record-rule decision — see [users, access rights & record rules](general-setup.md#users-access-rights--record-rules). Commission plans build on salesperson/team attribution — see [margins & commissions](#margins--commissions).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** One team and clean salesperson attribution for order-entry businesses; CRM only when the client commits a named pipeline owner — in that case scope it as its own workstream.

**Risk of getting it wrong:** low — teams and CRM can be added later without data damage; the common failure is the half-installed CRM, which costs credibility rather than data.

**Expertise tags:** `#sales` `#crm` `#governance`

---

## Customer portal & self-service

**Where:** **Grant portal access** on the contact; **Settings → Users & Companies → Portal** users; per-app portal behaviour (a portal user sees their own quotations, sales orders, invoices, delivery status — plus projects/timesheets if those apps are used).
**What it controls:** What the customer can do without emailing anyone: view and accept quotes, see order status and deliveries, download and pay invoices. Portal users are free (no user licence) and the portal is the delivery vehicle for the online sign & pay flow above.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Portal for quotes/orders/invoices, optionally with online invoice payment | Nearly all B2B: signature, payment, invoice history and delivery tracking self-served — exactly what removes "where is my order?" phone load. Invite key customer contacts at go-live, not "later". Online payment shortens DSO for card/SEPA-friendly bases; pure bank-transfer cultures rely on [follow-ups](finance.md#payment-terms-follow-ups--payment-methods) instead. | Customer bases that will never click a link (some traditional trades) — PDFs by email remain the channel. |
| **E-commerce (Website app) on top** | Genuine webshop ambitions — but a webshop is a separate project (catalogue, payments, shipping UX, GDPR/terms). | Never scope e-commerce as a portal footnote inside the sales workstream. Flag it, price it separately, sequence it after order-to-cash is stable. |

**Required client info:**
- Will this customer base actually use a portal? Test with three real customers, not the client's optimism. Is online invoice payment wanted, and with which provider?
- Is a webshop on the roadmap (separate project — record it, don't scope it here)?

**Interactions:** Portal acceptance/payment gates are configured in the [quotation flow](#quotation-flow-templates-online-sign--pay); portal invoice payment uses the [payment providers](finance.md#payment-terms-follow-ups--payment-methods); tracking links appear when [carrier connectors](#delivery-methods--shipping-connectors) supply them. Portal document branding follows [document layouts](general-setup.md#document-layouts--report-templates).

**Add-on impact:** No Odoo add-on overlays in this knowledge base to date.

**Default recommendation:** Portal on with the standard quote/order/invoice scope for every B2B client, invitations sent at go-live; e-commerce explicitly out of scope for the sales workstream, captured as its own candidate project.

**Risk of getting it wrong:** low — portal access is per-contact and reversible at any time.

**Expertise tags:** `#sales` `#portal` `#order-flow`

---

## Returns & credit notes

**Where:** **Return** button on a validated delivery order (creates the reverse picking); **Credit Note** button on a posted customer invoice (full or partial refund), or a standalone credit note from Accounting; refund policy is process design, not one setting.
**What it controls:** How goods come back (stock, valuation, lot/serial traceability) and how money goes back (credit note linked to the original invoice vs free-standing). These are separate flows in Odoo — a return picking does not create a credit note by itself, and vice versa.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Return from the original delivery** (reverse picking, linked to the source) | Always, when the original delivery is known: keeps traceability, restocks the right lots/serials, and with delivered-quantity invoicing it corrects the invoiceable-quantity trail. Decide restock-vs-scrap as an explicit disposition step — damaged goods get scrapped on receipt, not parked. | — |
| Ad-hoc inbound receipt for returned goods | Only when the original delivery is genuinely unidentifiable. | Routine use — it orphans the return from the order, breaking both traceability and invoicing reconciliation. |
| **Credit note from the invoice** (partial or full refund wizard) | Always, when crediting invoiced goods/services: the credit stays tied to the original invoice, taxes reverse correctly, and the Peppol credit note references its source. | Standalone credit notes are for goodwill gestures and pricing corrections with no source invoice — crediting delivered goods standalone leaves delivered-vs-invoiced quantities inconsistent on the order. |

**Required client info:**
- Returns volume and reasons (defect vs remorse vs wrong shipment) — does anything justify an RMA-style approval before accepting a return? Do lots/serials need capturing on return (warranty)?
- Are returned goods restocked, refurbished or scrapped, who decides — and is the refund money back, credit on account, or a replacement order?

**Interactions:** Return receipts follow the inbound flow — see [inbound/outbound steps](warehouse.md#inboundoutbound-steps-the-complexity-ladder); restocking valuation follows the [costing method](inventory.md#product-categories--costing-method-standard--avco--fifo). Credit notes transmit via [Peppol](finance.md#e-invoicing--peppol) like invoices and must reference the original. With delivered-quantity [invoicing policy](#invoicing-policy--down-payments), process returns *before* crediting so quantities reconcile.

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Returns always from the source delivery, credits always from the source invoice, an explicit restock-or-scrap step in the return process, standalone credit notes reserved for finance-approved goodwill.

**Risk of getting it wrong:** medium — each mis-handled return is fixable, but a year of ad-hoc receipts and standalone credits leaves order lines, stock valuation and VAT that no longer reconcile without archaeology.

**Expertise tags:** `#sales` `#order-flow` `#returns`

---

## Margins & commissions

**Where:** **Sales → Configuration → Settings → Margins** (shows cost and margin on order lines and in sales reporting); commission plans in the Enterprise commissions feature under Sales (plans, targets, achievements per salesperson/team).
**What it controls:** Whether salespeople see (and are managed on) margin at quote time, and whether commission calculation lives inside Odoo or in a spreadsheet.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Margins on** | Trading businesses managing discount authority by margin. Caveat to explain: the line margin uses the **product cost at the moment the line is created** — a snapshot. Under FIFO/AVCO the actual COGS at delivery can differ, so SO margin is an estimate, not the accounting margin. | Leave margins off for fixed-price service businesses and wherever cost data is unreliable or standards are stale — garbage cost = garbage margin, displayed confidently, and decisions will follow it. |
| Commission via reporting/spreadsheet | Simple plans (% of revenue): sales reporting by salesperson is enough input, payroll pays out. | Plans with tiers/targets that salespeople want to track live. |
| **Commission plans in Odoo** (Enterprise): plans with targets and achievements on revenue/margin per salesperson or team. **Community edition:** not available — reporting + payroll handoff is the answer. ⚠️ The commissions feature is recent and its scope evolves between releases — verify against current Odoo documentation. | Clients wanting commission visibility inside the system, on plan logic Odoo can express. Odoo pays nothing out by itself — payroll still executes. | Exotic plans (splits, clawbacks, multi-year) — validate against the actual written plan before promising anything. |

**Required client info:**
- Is cost data trustworthy per product, and should salespeople see cost/margin at all (some owners explicitly don't want this)?
- The real commission plan, in writing — revenue or margin based, thresholds, when is it "earned" — and who calculates it today, at what effort?

**Interactions:** Margin quality is entirely downstream of [costing method](inventory.md#product-categories--costing-method-standard--avco--fifo) and cost-maintenance discipline; the accounting-grade margin lives in [COGS accounting](finance.md#continental-vs-anglo-saxon-accounting--automatic-accounts), not on the SO. Margin visibility per role is an [access-rights](general-setup.md#users-access-rights--record-rules) question. Commission attribution rides on [sales teams](#sales-teams--crm-boundary).

**Add-on impact:** None yet — no Odoo add-on layers exist in this knowledge base.

**Default recommendation:** Margins on only where costs are maintained (and explain the snapshot caveat in training); commissions via standard sales reporting unless the client is on Enterprise with a plan simple enough to model — then pilot the commission feature for one quarter before relying on it.

**Risk of getting it wrong:** low — both are display/reporting layers, reversible; the danger is decisions made on margin numbers nobody validated, a trust cost rather than a data one.

**Expertise tags:** `#sales` `#pricing` `#margins`

---

## Subscriptions & recurring revenue

**Where:** **Subscriptions** app (Enterprise): recurring plans (monthly/yearly), subscription quotations/orders, automatic recurring invoicing, portal self-service (upsell, close), MRR/churn reporting. **Community edition:** no Subscriptions app — recurring billing is approximated with manually recurring invoices or duplicated orders, without MRR reporting or lifecycle management.
**What it controls:** Whether contracts that renew and bill on a schedule (maintenance contracts, SaaS-like fees, recurring services) are managed as first-class subscriptions or hand-cranked each period.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| No subscriptions — periodic manual/batch invoicing | A handful of recurring contracts; finance invoices them monthly from a list in minutes. | Dozens+ of contracts with different renewal dates, indexation, or upgrade/downgrade traffic — manual tracking starts leaking revenue. |
| **Subscriptions app** (Enterprise) | Recurring revenue is a real business line: automatic renewal invoicing, payment-provider charging, churn/MRR visibility, customer self-service. Recurring invoices flow through [Peppol](finance.md#e-invoicing--peppol) like any other Belgian customer invoice. | Bought "for later" with three contracts — it adds product/plan modelling overhead an SME with trivial recurring volume doesn't need. |

**Required client info:**
- How many recurring contracts, at what billing frequencies, how are renewals/indexations (Belgian index clauses) handled today — and is revenue leakage from missed renewals/upgrades a known problem?

**Interactions:** Recurring invoices follow the same [payment machinery](finance.md#payment-terms-follow-ups--payment-methods); deferred revenue recognition for invoiced-ahead periods is an accounting decision — coordinate with [finance.md](finance.md#continental-vs-anglo-saxon-accounting--automatic-accounts). Service contracts with delivery obligations touch [projects-service.md](projects-service.md#service-invoicing-policies-tm-fixed-milestones).

**Add-on impact:** No Odoo add-on overlays recorded in this knowledge base.

**Default recommendation:** Skip it below ~20 recurring contracts; adopt it when recurring revenue is a managed KPI — and then migrate all recurring contracts, not a half-set split across two mechanisms.

**Risk of getting it wrong:** low — adoptable later; running recurring billing half-in, half-out of the app is the only genuinely painful state.

**Expertise tags:** `#sales` `#subscriptions` `#order-flow`
