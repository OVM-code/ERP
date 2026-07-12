# Manufacturing — Odoo (Standard)

> **Scope:** Odoo 19 Enterprise (Odoo Online, Odoo.sh or on-premise); Community edition differences flagged inline
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when Odoo releases functional changes to this area (one major release per year, typically October).

Manufacturing covers everything from "we bundle two products into a box" to multi-level make-to-order production with work orders, shop-floor terminals and subcontracting. Odoo's complexity ladder runs: kit BoM (no manufacturing order at all — components deduct at delivery), manufacturing orders without work orders (one-click consume-and-produce), and manufacturing orders with work orders (operations at work centers, Shop Floor app, time registration). The edition split matters more here than anywhere else: BoMs, MOs, by-products, subcontracting, scrap and unbuild are all **Community**; the shop-floor experience (Shop Floor app, work order tablet features, Gantt planning), MPS, Quality, PLM and manufacturing-integrated maintenance are **Enterprise**. As with any ERP: the most expensive mistake is over-scoping — size the footprint to the client's shop-floor discipline, not their ambition.

---

## Manufacturing scope & MO flow

**Where:** Whether the Manufacturing app is installed at all; **BoM Type** on the bill of materials; **Manufacturing app → Configuration → Settings → Operations → Work Orders** checkbox; the *Manufacture* route on the product (Inventory tab).
**What it controls:** Whether making a product generates no document (kit), a manufacturing order posting consumption and output in one step, or an MO broken into work orders processed at work centers.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Pure trade — no Manufacturing app | Buy-and-sell; any "assembly" is cosmetic | Client physically transforms items and needs component-level stock and cost accuracy |
| Kit BoM only (no MOs) | Sales bundles, box-outs picked at shipping time; no labor worth costing; no stock of the combined product | The kit is physically built ahead of sale and stocked — kits are never on-hand as themselves; no production cost, no traceability of the build event |
| MOs without work orders | The workhorse for SMEs: consumption + output in one document, multi-level BoMs, MTO or reordering-rule driven; floor confirms one document per batch | Operation-level costing, per-step registration, or subcontracted *steps* needed — those hang off operations |
| MOs with work orders (Work Orders setting on) | Operation sequences matter; labor/machine time belongs in product cost; work center load visibility; Shop Floor terminals | Floor won't register starts/stops reliably — you get precise-looking durations built on fiction |

**Community edition:** MOs, BoMs and even the Work Orders checkbox exist in Community, but the Shop Floor app, tablet/employee time tracking and the planning Gantt views are Enterprise — a genuinely work-order-driven floor needs Enterprise in practice (see [edition choice](general-setup.md#edition--hosting-enterprise-vs-community-online-vs-odoosh-vs-on-premise)). The *Manufacture* route on the product (plus MTO or a reordering rule) is what makes demand generate MOs — decide it together with the [routes architecture](inventory.md#routes--procurement-rules-architecture-mtobuymanufacture); whether components are picked before production (1/2/3-step manufacturing) is a warehouse decision: [inbound/outbound steps](warehouse.md#inboundoutbound-steps-the-complexity-ladder).

**Required client info:**
- Walk me through what physically happens between components arriving and the finished product shipping — how many distinct steps, and does anyone care how long each takes?
- Is the "assembled" product ever stocked as itself, or only put together at shipping? (kit vs MO)
- Do you need labor/machine cost in the product cost, or is material enough?

**Interactions:** Gates everything below — [work centers](#work-centers-operations--work-orders), [consumption](#component-consumption--backflushing), [planning](#planning-mps-scheduling--capacity), [costing](#manufacturing-costing--overhead). Kit vs manufacture BoM types: [BoM design](#bom-design-kits-multi-level-variants-by-products). Replenishment triggers: [purchasing](purchasing.md#replenishment-triggers-reordering-rules-vs-mto).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Start one rung lower than the client's self-assessment: kits if the build happens at shipping, MOs without work orders as the SME default, work orders only where operation times will actually be registered. Adding work orders later is a settings checkbox plus BoM operations; rescuing an over-scoped shop-floor rollout is a project.

**Risk of getting it wrong:** medium — the ladder can be climbed later, but moving a stocked product from kit to manufacture BoM changes stock, cost and planning behaviour, and over-scoping burns floor goodwill that doesn't come back.

**Expertise tags:** `#manufacturing` `#scoping` `#bom` `#work-orders`

---

## BoM design (kits, multi-level, variants, by-products)

**Where:** **Manufacturing app → Products → Bills of Materials** (**BoM Type** field; Components, Operations, By-products tabs; Miscellaneous tab: **Manufacturing Readiness**, **Flexible Consumption**, **Routing**, **Analytic Distribution**, **Manuf Lead Time**, **Days to prepare Manufacturing Order**). By-products need **Settings → Operations → By-Products** ticked. Optional component columns (**Apply on Variants**, **Consumed in Operation**, **Manual Consumption**) via the settings-adjust icon on the Components tab.
**What it controls:** The master data every MO, planning computation and cost calculation explodes from.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| BoM Type **Manufacture this Product** | Anything that goes through an MO — stocked output, production cost, traceability of the build | Pure shipping-time bundles (use Kit) |
| BoM Type **Kit** | Sales bundles exploded on the delivery order; also the phantom-BoM equivalent — a kit used as a component inside a manufacture BoM explodes into its components on the MO | The combined product must be stocked, costed or tracked as itself |
| Multi-level BoM with stocked semi-finished products | Intermediates made to stock, sold as spares, or batched differently than parents — each level gets its own BoM, route and MO | Every level adds an MO and postings — don't model levels the floor doesn't stop at; use a kit-as-phantom for pure engineering groupings, and stay flat when intermediates are never stocked |
| One BoM with **Apply on Variants** per line/operation | Variant products sharing mostly-common components — one BoM to maintain | Variants differ structurally (different process, few shared lines) — separate BoMs per variant are clearer |
| By-products tab (+ Cost Share %) | Secondary outputs with real value (offcuts, co-products); cost share carves part of the MO cost into the by-product | Worthless residue — post it as [scrap](#scrap--unbuild) instead of polluting BoMs |

**Community edition:** all of the above, including by-products and variants, is Community; the **Version** field on the Miscellaneous tab only appears with the Enterprise PLM app — see [PLM](#plm--engineering-changes). Operations on the BoM (Operations tab) only exist once the Work Orders setting is on, and each operation belongs exclusively to one BoM (use *Copy Existing Operations* to reuse) — there is no shared routing master like BC's. There is also no scrap-% on BoM lines; predictable yield loss is modelled by inflating component quantities or handled as actual scrap postings.

**Required client info:**
- Which intermediates are physically stocked or sold separately? (drives levels)
- Do product variants share one recipe with per-variant deltas, or genuinely different processes?
- Any secondary outputs with value, and should they carry part of the cost?

**Interactions:** BoM type is the [scope decision](#manufacturing-scope--mo-flow) made concrete. Component UoM discipline: [units of measure](inventory.md#units-of-measure-policy). Semi-finished items need their own route and [reordering rules](inventory.md#reordering-rules--replenishment). Flexible Consumption is covered in [consumption](#component-consumption--backflushing); Analytic Distribution in [costing](#manufacturing-costing--overhead).

**Add-on impact:** No add-on overlays for Odoo exist in this knowledge base yet.

**Default recommendation:** As flat as physically honest; kits for shipping-time bundles and as phantoms inside manufacture BoMs; one variant-aware BoM when lines mostly overlap; by-products only where the output has value someone will book.

**Risk of getting it wrong:** medium — BoMs are editable, but a wrong level structure propagates into open MOs, planning and valuation, and restructuring competes with daily business.

**Expertise tags:** `#manufacturing` `#bom` `#variants` `#by-products`

---

## Work centers, operations & work orders

**Where:** **Settings → Operations → Work Orders** (and **Work Order Dependencies**); **Manufacturing app → Configuration → Work Centers** (Working Hours, Time Efficiency, Capacity, OEE Target, Setup/Cleanup Time, **Cost per hour** per workcenter and per employee, Alternative Workcenters, Allowed Employees, Specific Capacities tab); Operations tab on the BoM (Work Center, Duration Computation, Default Duration, Work Sheet tab); the **Shop Floor** app; **Manufacturing app → Planning → Planning by Workcenter**.
**What it controls:** The granularity of the capacity and cost model, and how (and whether) the floor registers work.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| One work center per department/cell, Capacity > 1 for parallel stations | Most SMEs — fewer centers means less registration and stabler BoMs when a machine changes | Genuinely per-machine scheduling, speeds or costs |
| One work center per machine + Alternative Workcenters | Per-machine costing/scheduling; alternatives let planning shift load automatically | Doubles master data and registration burden; avoid where the floor barely copes with per-cell posting |
| Duration Computation = *Compute based on tracked time* | Floor reliably starts/stops work orders — durations self-correct from the last N work orders | Sloppy registration poisons the estimates; use *Set duration manually* until discipline is proven |
| Shop Floor app on floor terminals/tablets | Enterprise; real-time work order processing, employee sign-in and time tracking per operation | Micro floors where a supervisor confirming the MO is faster and cheaper |

**Community edition:** the Work Orders checkbox and work centers exist, but the Shop Floor app, employee time tracking on work orders and the Gantt-style *Planning by Workcenter* view are Enterprise — Community work orders are processed from plain list/form views, workable for a supervisor, not for operators. Rule of thumb: every operation you add to a BoM is a recurring registration obligation, not a drawing of the process — model the steps someone will actually start and stop, merge the rest into one operation.

**Required client info:**
- Do you schedule "the CNC department" or "CNC machine #3"? Who decides which machine runs a job — system or foreman?
- Will operators touch a terminal per operation, or does a supervisor confirm at shift end — honestly?

**Interactions:** Requires Work Orders from [scope](#manufacturing-scope--mo-flow). Cost per hour feeds [MO costing](#manufacturing-costing--overhead). Work center load and Working Hours feed [planning](#planning-mps-scheduling--capacity). Quality checks attach to operations — [quality](#quality-management). Who may process work orders: [access rights](general-setup.md#users-access-rights--record-rules).

**Add-on impact:** None known yet for Odoo in this knowledge base.

**Default recommendation:** Work centers per department/cell with Capacity for parallel stations; manual durations first, switch to tracked-time computation after two or three months of clean registration; Shop Floor terminals only where operators genuinely process per-operation.

**Risk of getting it wrong:** medium — restructuring work centers means touching every BoM operation that references them, and a floor that learned "the tablet is optional" in week one is expensive to re-train.

**Expertise tags:** `#manufacturing` `#routing` `#work-orders` `#capacity`

---

## Component consumption & backflushing

**Where:** BoM Miscellaneous tab → **Flexible Consumption** (`Allowed` / `Allowed with Warning` / `Blocked`); per-component **Manual Consumption** checkbox and **Consumed in Operation** column on the Components tab; **Manufacturing Readiness** (components for 1st operation vs all components); lot/serial registration on the MO's components.
**What it controls:** Odoo's equivalent of BC's flushing methods: components backflush automatically at BoM quantity when the MO (or operation) is completed, unless you force manual confirmation or restrict deviation.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Allowed** (fully flexible) | Trusted operators, variable consumption (yield swings, substitutions) — deviations post silently | Nobody reviews consumption → shrinkage and recipe drift go unnoticed |
| **Allowed with Warning** | The pragmatic default: deviations allowed but flagged, so someone can review exceptions | Warning fatigue if the BoM quantities are chronically wrong — fix the BoM, not the setting |
| **Blocked** (strict) | Regulated or high-value recipes where the BoM is law; forces a formal BoM change instead of ad-hoc deviation | Reality deviates legitimately (natural materials, rework) — operators will game the numbers to close orders |
| **Manual Consumption** per component | High-value or high-variability components: operator must tick/enter Consumed, others still backflush | Ticking everything — you've reinvented full manual issue and the floor will batch-fake it |
| Consumed in Operation (with work orders) | Consumption and readiness tied to the operation that uses the component; components backflush as each operation completes | MO-only footprint — the column is meaningless without work orders |

**Community edition:** all of this is Community — the consumption model does not depend on Enterprise. Consultant judgement (same doctrine as BC flushing): map the setting to shop-floor discipline, not elegance — backflush the boring components at BoM quantity, force manual confirmation on the value drivers, and reconcile with cycle counts. Components tracked by lot/serial always require the specific lot to be registered on the MO — that is your de facto manual step for tracked items ([tracking](inventory.md#tracking-lots-serials--expiry)).

**Required client info:**
- For each component class: does actual usage deviate from the BoM by more than you care about financially?
- Any components under lot/serial tracking? (registration is mandatory regardless of this setting)
- Who would review consumption deviations — would a warning actually reach them?

**Interactions:** Set per BoM — decide it during [BoM design](#bom-design-kits-multi-level-variants-by-products). Wrong backflushing corrupts on-hand accuracy that [reordering rules](inventory.md#reordering-rules--replenishment) and [planning](#planning-mps-scheduling--capacity) rely on, and misstates the component leg of [MO cost](#manufacturing-costing--overhead).

**Add-on impact:** No Odoo add-on overlays in this knowledge base yet.

**Default recommendation:** Allowed with Warning as the house default; Manual Consumption on high-value components; Blocked only for genuinely regulated recipes with a working change process.

**Risk of getting it wrong:** low-to-medium — the field is changeable per BoM at any time, but months of silent mis-consumption mean a physical-count-and-revalue cleanup.

**Expertise tags:** `#manufacturing` `#flushing` `#consumption` `#shop-floor-discipline`

---

## Planning: MPS, scheduling & capacity

**Where:** **Settings → Planning → Master Production Schedule** (Enterprise; plus **Time Range** Monthly/Weekly/Daily and **Number of Columns**); **Manufacturing app → Planning → Master Production Schedule**; reordering rules and MTO per product ([inventory](inventory.md#reordering-rules--replenishment)); MO scheduling from **Manuf Lead Time** and **Days to prepare Manufacturing Order** on the BoM; **Planning → Planning by Workcenter** (Gantt, Enterprise).
**What it controls:** How demand becomes suggested MOs (and component POs), and how MOs and work orders land on dates and work centers.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Reordering rules + MTO only (no MPS) | The SME norm: min/max on stocked items, MTO route on customer-specific items; the scheduler generates MOs automatically | Demand is forecast-driven and lumpy (seasonality, promotions) — rules only see current demand |
| MPS-driven planning (Enterprise) | Forecast-driven make-to-stock; a named planner enters Forecasted Demand per period and clicks Replenish; component needs roll down via Indirect Demand Forecast | Nobody will own the forecast — MPS is a **manual** tool; unowned, it's a stale spreadsheet inside the ERP |
| MPS *and* reordering rules on the same product | Never — Odoo's own documentation warns the two conflict and generate duplicate replenishment | Always split: MPS products vs rule-driven products |
| Work order scheduling with Working Hours + Alternative Workcenters | Work-order footprint; load visible per work center, overloads shifted to alternatives | Expecting finite-capacity optimization — Odoo schedules by lead times and availability; it does not solve the schedule |

**Community edition:** no MPS and no Gantt planning views — planning is reordering rules, MTO and manually scheduled MOs, which is genuinely enough for most job shops. Same doctrine as the BC planning worksheet: don't run forecast-driven planning on day one — go live with reordering rules on proven min/max, let master data (BoMs, lead times) shake out, and introduce MPS in phase 2 only if a planner owns it. Manage the expectation early that capacity is not finitely optimized: the Gantt shows load, a human levels it.

**Required client info:**
- Make-to-stock, make-to-order, or mixed — per product family?
- Is there a usable forecast, at what granularity, and who maintains it monthly?

**Interactions:** Builds entirely on the [routes/procurement architecture](inventory.md#routes--procurement-rules-architecture-mtobuymanufacture) and [reordering rules](inventory.md#reordering-rules--replenishment); component buying triggers: [purchasing](purchasing.md#replenishment-triggers-reordering-rules-vs-mto). Availability accuracy depends on honest [consumption](#component-consumption--backflushing). Work center load comes from [work centers](#work-centers-operations--work-orders).

**Add-on impact:** None known yet — this knowledge base has no Odoo add-on layer.

**Default recommendation:** Reordering rules + MTO at go-live; MPS in phase 2 for forecast-driven families with a named owner; never both on one product.

**Risk of getting it wrong:** medium — reversible, but MPS-plus-rules double replenishment floods the shop with unneeded MOs and destroys planner trust in the suggestions, often permanently.

**Expertise tags:** `#manufacturing` `#planning` `#mps` `#forecast`

---

## Subcontracting

**Where:** **Settings → Operations → Subcontracting** checkbox; BoM Type **Subcontracting** + **Subcontractors** field on the BoM; vendor line (pricelist) on the subcontracted product's Purchase tab; component routes *Resupply Subcontractor on Order* / *Dropship Subcontractor on Order*; the **Resupply** smart button and *Resupply Subcontractor* operation type in Inventory.
**What it controls:** Whether externally produced goods flow as a purchase that consumes a subcontracting BoM — including component provision to the subcontractor and how the finished cost is built.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Basic subcontracting (subcontractor sources own components) | You buy a finished product made to your spec; components tab can stay empty; cost = PO price | You supply materials, or need component-level cost/traceability of the subcontractor's input |
| Resupply subcontracting (*Resupply Subcontractor on Order* route on components) | You ship components to the subcontractor; a resupply order moves them to the subcontractor location and they stay your valued stock until consumed at receipt | Subcontractor is really just a supplier of a finished good — resupply adds transfers nobody needs |
| Dropship components to subcontractor (*Dropship Subcontractor on Order*) | Components bought from a third party and delivered straight to the subcontractor | Components come from your own stock (use resupply) |
| Subcontracted *operation* mid-routing | Odoo has no BC-style subcontract routing operation; model an external step as a semi-finished product with its own subcontracting BoM | — this is a structural workaround; flag it to the client explicitly |

**Community edition:** subcontracting — including resupply and dropship — is Community, a genuine advantage over most mid-market ERPs. Valuation: with resupply, the finished product's value builds from your supplied components plus the subcontractor's PO price; components sitting at the subcontractor remain on your books at their location — make sure the client's accountant understands stock-at-third-party before the first count. Whole-product subcontracting fits Odoo naturally; per-operation subcontracting is where scoping conversations belong.

**Required client info:**
- Does the subcontractor make the whole product or one step in the middle of your process?
- Who supplies the material — you, them, or a third party shipping direct?
- Do you need to see your stock at their site (and count it)?

**Interactions:** Subcontractor locations and resupply flows: [warehouse design](warehouse.md#warehouse--location-design). Component replenishment to feed resupply: [purchasing triggers](purchasing.md#replenishment-triggers-reordering-rules-vs-mto). Finished-good valuation: [costing method](inventory.md#product-categories--costing-method-standard--avco--fifo) and [valuation posting](finance.md#inventory-valuation-posting-manual-vs-automated). Lot traceability through the subcontractor: [tracking](inventory.md#tracking-lots-serials--expiry).

**Add-on impact:** No Odoo add-on overlays exist in this knowledge base yet.

**Default recommendation:** Basic subcontracting when the vendor sources materials; resupply when you provide them; model mid-process external steps as subcontracted semi-finished products and price that honestly in the implementation estimate.

**Risk of getting it wrong:** medium — flows are reworkable, but invisible material at the subcontractor causes phantom shortages, and mis-built subcontract cost distorts margins on every receipt.

**Expertise tags:** `#manufacturing` `#subcontracting` `#purchasing` `#costing`

---

## Manufacturing costing & overhead

**Where:** MO **Overview** smart button (**MO Cost** vs **Real Cost** columns); work center **Cost per hour** (*per workcenter* and *per employee*); employee **Hourly Cost** (Employees app, Settings tab); product **Cost** field + **Compute Price from BoM** button; **Analytic Distribution** on the BoM Miscellaneous tab.
**What it controls:** What a finished product costs when it enters stock: components consumed + work order time × work center rates, and where that cost is visible.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Components-only cost (no work orders) | MO-only footprint: finished cost = component cost; labor stays in P&L as period cost | Management prices from full cost — margins will look fat and be wrong |
| Components + operations at work center rates | Work-order footprint; Real Cost uses actual durations (and actual employee hourly cost where tracked) vs the BoM-estimated MO Cost | Durations are fiction — garbage times produce garbage unit costs order by order |
| Overhead via inflated work center rates | Odoo has no separate overhead/indirect-cost % on BoMs or items (unlike BC): bake machine + allocated overhead into Cost per hour | The client expects a named "overhead absorbed" line — set expectations; it's inside the hourly rate |
| Analytic Distribution on the BoM | Production cost mirrored into analytic accounting per line/plant/project — management view without touching the GL | No one defined the analytic plan yet — do [that architecture](general-setup.md#analytic-accounting-architecture-plans--distributions) first |

**Community edition:** MO costs and analytic distribution are Community; per-employee actual time (and therefore employee-rate Real Cost) needs Enterprise work order time tracking. How cost lands in stock depends on the [costing method](inventory.md#product-categories--costing-method-standard--avco--fifo) of the finished product's category: with AVCO/FIFO the MO's real cost flows into valuation; with Standard the product enters at its set standard cost and the deviation surfaces in the valuation accounts — Odoo has no BC-style variance breakdown (material/capacity variances) out of the box.
> ⚠️ Verify against current Odoo documentation.

**Required client info:**
- Should labor/machine cost be in inventory value, or is material-only acceptable to finance?
- How is overhead absorbed today, and does anyone reconcile absorbed vs actual? Standard costs with a periodic review, or actual costs following the MOs?

**Interactions:** Depends on honest [durations](#work-centers-operations--work-orders) and [consumption](#component-consumption--backflushing). Costing method and category setup: [inventory](inventory.md#product-categories--costing-method-standard--avco--fifo). Whether journal entries post automatically at all: [valuation posting](finance.md#inventory-valuation-posting-manual-vs-automated), and account routing under [Continental vs Anglo-Saxon](finance.md#continental-vs-anglo-saxon-accounting--automatic-accounts). Analytic plans: [general setup](general-setup.md#analytic-accounting-architecture-plans--distributions).

**Add-on impact:** None known yet — no Odoo add-on overlays in this knowledge base.

**Default recommendation:** AVCO finished goods with components + operations at loaded work center rates (overhead inside the rate); analytic distribution on BoMs once the analytic plan exists; standard costing only if a controller owns the review cycle.

**Risk of getting it wrong:** medium here, but it sits on a high-irreversible foundation — the costing method itself is effectively locked once stock moves exist (that decision lives in inventory.md, argue it there).

**Expertise tags:** `#manufacturing` `#costing` `#overhead` `#finance`

---

## Quality management

**Where:** **Settings → Quality** checkbox (Enterprise Quality app; **Quality Worksheet** adds worksheet-type checks); quality control points defined per operation type (Receipts, Manufacturing, Delivery) and per BoM operation (the *Instructions/Steps* list on operations); **Quality Alerts** kanban.
**What it controls:** Whether inspection is a system-enforced step — checks that block receipts, work orders or deliveries until performed — or a paper discipline beside the system.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| No Quality app (Community or by choice) | Discipline-only quality: instructions can still live on the operation's Work Sheet tab (PDF/text), results on paper | Certifications or customers require recorded, enforced checks |
| Control points at goods receipt or before delivery | Supplier quality matters (incl. subcontracted receipts); final inspection gates shipping | Trivial receipts or already-checked output — every check is a click someone must earn |
| Control points on manufacturing operations | In-process checks at defined steps; check types like Instructions, Pass–Fail, Measure (with tolerances), Take a Picture, Worksheet | MO-only footprint with no operations to hang checks on — receipt/delivery points still work |
| Quality Alerts | Nonconformity capture with team/kanban follow-up — cheap to enable, useful from day one | Nobody triages the board — an ignored alert queue is worse than none |

**Community edition:** no Quality app at all — if enforced checks are a hard requirement, that alone decides Enterprise. Rule of thumb: every control point is a mandatory click forever — start with the two or three checks that map to real failure modes (receipt on critical suppliers, final inspection), not a full inspection plan transcribed from the ISO manual.

**Required client info:**
- Which certifications/customer audits require recorded checks, at which points (receipt / in-process / final), and as what — pass–fail, measured values with tolerances, or filled worksheets?
- Who processes failed checks, and what physically happens to the goods (block, rework, scrap)?

**Interactions:** In-process checks require [operations/work orders](#work-centers-operations--work-orders). Receipt checks pair with [inbound steps](warehouse.md#inboundoutbound-steps-the-complexity-ladder) and [subcontracted receipts](#subcontracting). Failed goods flow to [scrap](#scrap--unbuild). Lot-level quality holds relate to [tracking](inventory.md#tracking-lots-serials--expiry).

**Add-on impact:** No Odoo add-on overlays in this knowledge base yet.

**Default recommendation:** Enterprise clients: enable Quality with a minimal set of control points at real failure modes plus Quality Alerts; grow the plan from recorded failures, not from the quality manual.

**Risk of getting it wrong:** low — control points can be added/removed freely; the real risk is check fatigue turning quality into click-through theatre.

**Expertise tags:** `#manufacturing` `#quality`

---

## PLM & engineering changes

**Where:** **Settings → PLM** checkbox (Enterprise, *Product Lifecycle Management*); Engineering Change Orders (ECOs) with types/stages and approvals; the **Version** field on the BoM Miscellaneous tab; revision comparison between BoM versions.
**What it controls:** Whether BoM changes go through a governed change process (draft → approval → apply, producing a new BoM version with history) or are edited in place.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| No PLM — edit BoMs directly | Small teams, one BoM owner, infrequent changes; archive-and-duplicate for the rare big revision | Multiple people change BoMs, or auditability of "what did we build in March" matters |
| PLM with ECOs and approval stages | Recurring engineering/recipe changes, effectivity control, approval trail; versioned BoM history with revision comparison | Team of three where the ECO workflow is ceremony — an unused approval stage is worse than none |

**Community edition:** no PLM; BoM versioning as a feature doesn't exist — the fallback is disciplined archive-and-duplicate with a naming convention and a changelog note on the BoM. When does an SME actually need PLM: when a wrong BoM version reaching the floor costs real money (recalls, certified products), or when change approval is contractual — otherwise plain BoM discipline is enough; revisit after the first painful change incident, which is a cheaper teacher than an unused module.

**Required client info:**
- How often do BoMs change, who requests changes, and who must approve?
- Do you need to know exactly which BoM version an old MO used (audit, recall, warranty)?

**Interactions:** Governs the master data of [BoM design](#bom-design-kits-multi-level-variants-by-products); version-controlled worksheets feed [work orders](#work-centers-operations--work-orders); cost effects of a revision flow through [costing](#manufacturing-costing--overhead) at the next MOs.

**Add-on impact:** None known yet for Odoo in this knowledge base.

**Default recommendation:** Skip PLM at go-live for most SMEs; introduce it when change volume or audit demands appear. If enabled, one ECO type with two stages (draft/approved) — grow stages only when the process is lived.

**Risk of getting it wrong:** low — PLM can be enabled later; existing BoMs become version 1 and the process starts from there.

**Expertise tags:** `#manufacturing` `#plm` `#bom`

---

## Scrap & unbuild

**Where:** **Scrap** action on the MO (components or finished product); **Inventory app → Operations → Scrap** for standalone scrap orders; scrapped stock moves to the virtual location **Virtual Locations/Scrap**. Unbuild: **Manufacturing app → Operations → Unbuild Orders** (Product, BoM, Quantity, optional source MO, source/destination locations).
**What it controls:** How production losses and dismantled products leave (or re-enter) inventory with a trace, instead of vanishing through inventory adjustments.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Scrap from the MO | Loss discovered during production — keeps the link to the order for analysis | Bulk periodic write-offs unrelated to a specific MO (use standalone scrap orders from Inventory) |
| Unbuild orders | Overbuilt products dismantled back to components; reclaiming parts; reversing a mistaken MO (reference the original MO — mandatory for lot/serial-tracked outputs to keep traceability clean) | "Un-selling" or hiding scrap: components return at BoM quantities regardless of what's physically recoverable — scrap the delta honestly |

**Community edition:** both scrap and unbuild are Community. Cost implications: scrapped value leaves stock into the scrap location — with automated valuation this is a real journal entry, so agree with the accountant which account the loss hits; unbuild reverses the build at cost, but does not conjure back operation time already spent, which stays in the cost of the period.

**Required client info:**
- Where is loss discovered — during production, at inspection, in the warehouse — and does anyone review scrap by reason today?
- Which GL account should production losses hit, and who watches it? (feeds [valuation posting](finance.md#inventory-valuation-posting-manual-vs-automated))

**Interactions:** Failed [quality checks](#quality-management) commonly end in scrap. By-products vs scrap boundary: [BoM design](#bom-design-kits-multi-level-variants-by-products). Lot/serial integrity through unbuild: [tracking](inventory.md#tracking-lots-serials--expiry). Scrap location visibility in counts: [warehouse design](warehouse.md#warehouse--location-design).

**Add-on impact:** No Odoo add-on overlays exist in this knowledge base yet.

**Default recommendation:** Scrap from the MO as the standard loss flow (train it in onboarding); unbuild reserved for genuine dismantling and MO reversals with the original MO referenced; never let scrap substitute for inventory adjustments or vice versa.

**Risk of getting it wrong:** low — both are correcting flows; the damage is analytical (losses hidden in adjustments) rather than structural.

**Expertise tags:** `#manufacturing` `#scrap` `#unbuild`
