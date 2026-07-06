# Trade & Pricing — Aptean Food & Beverage ERP

> **Add-on:** Aptean Food & Beverage ERP (Business Central embedded)
> **Base ERP:** Microsoft Dynamics 365 Business Central
> **Last reviewed:** 2026-07

The trade layer covers the commercial mechanics food margins actually live in: **Trade Management (TMT)** with *trade plans* (price rules and/or accruals auto-applied to sales/purchase documents for selected customers/vendors/items) and *trade statements* (settling accrued amounts — customer refunds/rebates, commissions to external commissioners); **commission/commission group setup** (GRR, which also carries grower-settlement functionality from the fresh heritage); **promotions/condition rules** (SPC, Drink-IT heritage — e.g. free-goods promotions like "1 free crate per 40"); and **commodity functionality** (COM) with Commodity Harvest Planning (CHP) and Contract Management for market-priced raw materials and grower contracts. In food distribution and manufacturing, 2–10% of revenue typically flows through rebates and promotions — if this module is configured casually, the client's margin reporting is fiction and year-end brings six-figure accrual surprises.

---

## Changes to standard setup decisions

### Modifies: Sales pricing architecture ([standard file](../../erp/business-central/sales.md#sales-pricing-model-price-lists-vs-legacy-sales-prices-discount-hierarchy))

**How it changes:** extends/layers. Standard BC price lists remain the base price. Trade plans sit on top as automatically applied price rules and accruals; promotions add condition-based benefits (free goods, order-size discounts). You must now design a **precedence story**: base list price → customer/contract price rule → promotion → off-invoice vs. accrued benefit.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| BC price lists (customer/group/all) | yes | Still the foundation for list/base prices. |
| BC sales line discounts | yes, constrained | Keep for simple, permanent discounts; anything with a validity window, a fund, or a settlement should be a trade plan, not a discount line — otherwise it's invisible to rebate accounting. |
| Manual price overrides by sales staff | yes, discouraged | Overrides bypass trade-plan logic and pollute the accrual base; restrict via permissions and monitor. |

### Modifies: Purchase pricing ([standard file](../../erp/business-central/purchasing.md#purchase-pricing--discounts))

**How it changes:** extends. Trade plans apply on the purchase side too (vendor rebates/allowances you *receive*); commodity items can price from market quotations and purchase contracts (COM/Contract Management, incl. contracts created from harvest planning).

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Fixed vendor price lists | yes | For non-commodity purchased goods. |
| Manually re-keyed market prices | changed | Commodity pricing should come from maintained quotations/contracts, not weekly manual price-list edits. |

### Modifies: Accruals & GL mapping ([standard file](../../erp/business-central/finance.md#customer-and-vendor-posting-groups))

**How it changes:** extends. Trade-plan accruals post rebate/commission liabilities as sales occur; trade statements settle them (credit memo, payment, invoice from commissioner). Finance must provide GL accounts/posting setup for accrual and settlement and own the reconciliation.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Year-end manual rebate accrual journal | no (as primary method) | Replaced by transaction-level accrual; the manual journal survives only as a true-up. |
| Rebates netted against revenue vs. cost lines | yes (policy choice) | Module posts where you map it — get the client's auditor's view on gross-to-net presentation early. |

---

## New setup decisions introduced by this module

### Trade plan structure & scope

**Where:** TMT — trade plans (price rule and/or accrual; assignment to customers/vendors/items)
**What it controls:** how commercial agreements are encoded: as price rules (net price on document), as accruals (invoice at list, accrue the benefit for later settlement), or both; and the customer/vendor/item scoping model.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Price rules (off-invoice net pricing) | Everyday net-net agreements; simple channel pricing | Retrospective volume rebates — by definition not knowable at invoice time |
| Accruals (on-invoice list price, benefit settled later) | Volume rebates, growth bonuses, listing fees, marketing funds | Trivial permanent discounts — accruing those is pointless admin |
| Combined (net price + accrued bonus) | Retail agreements that stack mechanisms | If the client can't articulate the agreement precisely — model follows contract, and a vague contract can't be configured |
| Scope by customer group / item category | Manageable agreement portfolios | Hundreds of per-customer-per-SKU micro-plans nobody maintains |

**Required client info:**
- The actual signed trade agreements (read them — the sales director's summary is always simplified)
- Volume tiers: retrospective-to-unit-one vs. incremental; period definitions; payout basis (invoiced vs. paid sales)
- Who maintains plans when agreements renew annually (commercial back office needs an owner)

**Interactions:** accruals hit finance mappings (above); catch weight items accrue on actual weight-based amounts; promotions (below) may stack with plans — define precedence explicitly; margin reports must show margin *net of accruals* or sales will steer on wrong numbers.
**Default recommendation:** price rules for unconditional net pricing, accruals for anything conditional/retrospective; scope at group/category level; a named owner and an annual renewal calendar for plan maintenance.
**Risk of getting it wrong:** high — under-accrued rebates surface as a P&L hit at settlement; the pattern ("great margins all year, terrible Q4") destroys trust in the system.
**Expertise tags:** `#aptean-fnb` `#trade-management` `#rebates` `#margin`

### Rebate settlement via trade statements

**Where:** TMT — trade statements (connect accrued amounts to trading partners: customer refunds, commissioner payments)
**What it controls:** the settlement cycle: statement frequency, settlement document type (sales credit memo, payment, purchase invoice from broker), approval, and matching against claims/deductions.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Periodic statements (monthly/quarterly) with credit memo settlement | Standard retail/wholesale rebate practice | — |
| Settlement against customer deductions (customer short-pays, you match) | US retail reality — deduction matching is the actual job | Ignoring this and assuming clean credit-memo flow — cash application will drown |
| Annual settlement only | Small agreement portfolios | Large accrual balances sitting 12 months invite disputes and audit questions |

**Required client info:**
- How customers actually take their rebates today: wait for credit memo, or deduct from remittance?
- Approval policy for settlements (who signs off paying out accrued funds)
- Dispute history — which agreements generate arguments (those need line-level accrual evidence)

**Interactions:** ties into AR/cash application processes (finance); accrual balance per plan should be reconciled to GL monthly; unsettled accruals at year-end need auditor-ready detail.
**Default recommendation:** monthly or quarterly statements aligned to each agreement's contractual cycle; reconcile accrual subledger to GL monthly from month one.
**Risk of getting it wrong:** medium-high — settlement mess is recoverable but expensive: overpaid rebates are rarely clawed back.
**Expertise tags:** `#aptean-fnb` `#trade-management` `#settlement` `#finance`

### Commission & broker/royalty handling

**Where:** GRR — commission and commission group setup (compensation to agents/trading companies, % of revenue on sale); trade statements pay external commissioners
**What it controls:** which sales carry commission, to whom (internal reps vs. external brokers), the basis (revenue %, per-weight, margin-based) and settlement.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Commission groups on customers/items, % of revenue | Broker-driven sales (common in US food distribution), agent models | Internal-only sales-comp better handled in payroll/CRM — don't drag payroll into ERP without need |
| Royalty accrual per unit/weight sold | Licensed brands, private-label royalty deals | — |
| No commission in ERP | No third-party commissioners | If brokers exist, spreadsheet commission tracking is a recurring dispute generator — bring it in |

**Required client info:**
- Broker contracts: basis, rates, exclusions (does commission apply net of rebates? on catch weight actuals?)
- Whether commissioners invoice the client or receive self-billed statements

**Interactions:** commission basis interacting with trade-plan accruals (commission on gross vs. net-of-rebate revenue) is the detail everyone gets wrong — pin it down in writing; settlement runs through trade statements.
**Default recommendation:** model external brokers/royalties in ERP with self-billed statements; keep internal sales-rep compensation out of ERP.
**Risk of getting it wrong:** medium — recalculable, but broker relationships sour fast over commission disputes.
**Expertise tags:** `#aptean-fnb` `#commissions` `#trade-management`

### Promotion mechanics

**Where:** SPC — promotion/condition rules (documented walkthroughs include free-goods promotions, e.g. one free crate per 40; order-size-based benefits); multi-level promotion offers incl. order-size rebates per the bcFood/Drink-IT heritage
**What it controls:** temporary, condition-based benefits on sales documents: free goods, quantity-break discounts, bundled offers, validity windows.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Free-goods promotions (buy X get Y) | Beverage and impulse categories; wholesaler push promos | Categories where free goods wreck price perception — use temporary price rules instead |
| Order-size discounts/rebates | Encouraging drop-size economics (full pallets, full trucks) | If logistics constraints (below, [logistics-and-planning.md](logistics-and-planning.md)) aren't aligned — promoting order sizes your routes can't carry |
| Temporary price-rule promotions via trade plans | Simple period discounts | When the mechanic is genuinely conditional (free goods) — a price rule can't express it |

**Required client info:**
- Current promo calendar and mechanics actually used (collect last year's promo sheet)
- Who funds the promo (own margin vs. vendor-funded — vendor-funded needs a purchase-side accrual to claim it back)
- Stacking policy: promo on top of net price? on top of rebate-bearing volume?

**Interactions:** free goods affect inventory planning and lot allocation; vendor-funded promos need mirrored purchase-side claims; promo effectiveness reporting needs the promo identifiable on posted documents.
**Default recommendation:** implement only the mechanics in last year's actual promo calendar; define stacking precedence in a one-page rule sheet signed by the commercial director.
**Risk of getting it wrong:** medium — misconfigured promos leak margin invisibly during the promo window; recoverable but never recovered.
**Expertise tags:** `#aptean-fnb` `#promotions` `#pricing`

> ⚠️ Verify against current Aptean documentation — SPC promotion mechanics are documented for the beverage (Drink-IT) heritage; confirm availability/behaviour in the client's edition. Written partly from general product knowledge.

### Commodity & contract pricing

**Where:** COM (commodity), CHP (Commodity Harvest Planning — harvest orders/planning), Contract Management (purchase contracts, incl. created from harvest orders/planning pages)
**What it controls:** raw-material pricing from market quotations and contracts rather than static price lists: commodity price feeds/updates, purchase contracts with volumes and price terms, grower/harvest planning for fresh intake.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Contract-based purchasing with contract call-offs | Anyone buying crop/protein on forward contracts | Spot-only buyers — contract admin without contracts |
| Market/commodity price-driven pricing (quotation-based) | Dairy, grains, oils, cocoa — index-linked buying (and index-linked selling) | Stable-price supply chains |
| Harvest planning + grower settlement (CHP/GRR fresh heritage) | Fresh produce packers working with growers, consignment intake | Non-fresh businesses — this is specialised LINKFRESH-heritage territory; scope with an Aptean fresh specialist |

**Required client info:**
- Which inputs are commodity-priced and against which index/quotation source; update frequency
- Contract structures: fixed volume/fixed price, min-max, pooling/settlement with growers (settle on grade/quality outcome?)
- Whether sales prices are formula-linked to input indices (cost-plus/index-linked selling needs the same quotation data on the sales side)

**Interactions:** quality/grade results (QC module) can drive grower settlement values; harvest intake hits lot attributes (origin/field); contract positions vs. forecast consumption is a planning report finance will want.
**Default recommendation:** contracts + quotations for the top commodity inputs by spend; leave grower settlement to a dedicated phase with fresh-produce specialists — it is its own sub-project.
**Risk of getting it wrong:** medium-high — mispriced commodity intake flows straight into COGS; grower settlement errors are relationship-ending for a packer.
**Expertise tags:** `#aptean-fnb` `#commodity` `#contracts` `#grower-settlement`

> ⚠️ Verify against current Aptean documentation — trade plans, trade statements, commissions, commodity/harvest/contract integration are grounded in Aptean's public TMT/GRR/COM/CHP docs; field-level settlement mechanics and grower accounting depth are partner-gated.
