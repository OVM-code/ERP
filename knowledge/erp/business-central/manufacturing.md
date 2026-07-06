# Manufacturing — Microsoft Dynamics 365 Business Central (Standard)

> **Scope:** Microsoft Dynamics 365 Business Central (SaaS, current version)
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when the vendor releases functional changes to this area.

Manufacturing covers everything from "we occasionally kit two items into a box" to multi-level make-to-order production with routings, capacity planning and subcontracting. It is in scope whenever the client transforms items — assembles, processes, machines, blends or packs them — rather than just buying and selling. Note that production orders, routings and work centers require the **Premium** license; assembly management is available in Essentials. The single most expensive consulting mistake in this area is over-scoping: implementing full manufacturing for a client whose shop floor cannot feed the system with data. Size the footprint to the client's discipline, not their ambition.

---

## Manufacturing footprint (none / assembly / light / full)

**Where:** Licensing decision (Essentials vs Premium) + which modules you configure at all. No single setup page — this is the scoping decision that gates everything below.
**What it controls:** Whether the client uses no make-functionality (pure trade), assembly orders with assembly BOMs, production orders without routings ("light manufacturing"), or full manufacturing with routings, work centers and capacity.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Pure trade (no BOMs) | Buy-and-sell distributor; any "kitting" is cosmetic and can be handled as sales bundles or item charges | Client physically combines items and needs component-level inventory and cost accuracy |
| Assembly BOMs + assembly orders (Essentials) | Kitting, simple pack-out, light configure-to-order at sales entry; little or no resource/machine involvement; assemble-to-order linked to sales lines is a first-class flow | Multi-step processes, operations at machines, subcontracted steps, need for routings/scrap/capacity — assembly has none of these |
| Light manufacturing: production orders + production BOMs, no routings (Premium) | Client needs consumption/output posting, multi-level BOMs, MRP-driven production, but doesn't track operations or machine time | Client wants operation-level costing, subcontracting (needs a routing line), or capacity scheduling — you'll retrofit routings later under pressure |
| Full manufacturing: production BOMs + routings + work/machine centers (Premium) | Operation sequences matter; labor/machine cost belongs in item cost; subcontracted operations; capacity load visibility | Shop floor won't register times/output reliably — you get precise-looking numbers built on garbage input |

**Required client info:**
- Walk me through what physically happens between receiving components and shipping the finished product — how many distinct steps, and are machines/people a bottleneck?
- Do you need the cost of labor/machines in the product cost, or is material cost enough?
- Who would record production data, on what device, how many times a day — realistically?
- Are any steps done by external processors (subcontracting)?
- Do you configure products per customer order at sales-entry time (favors assemble-to-order)?

**Interactions:** Drives the license tier (Essentials vs Premium). Constrains [Flushing methods](#flushing-methods-manual-vs-forward-vs-backward-vs-pick), [Work centers vs machine centers](#work-centers-vs-machine-centers-shop-calendars--capacity) and everything else in this file. Assembly interacts heavily with [warehouse handling levels](warehouse.md#item-journal-vs-warehouse-journal-per-level) (assemble-to-order + inventory picks). Component planning depends on [reordering policies](inventory.md#replenishment--planning-parameters).

**Add-on impact:** Aptean Food & Beverage ERP effectively assumes the full-manufacturing footprint for process production: it adds process-oriented production (batch/recipe thinking, co/by-products, yield) and catch weight handling in production and sales on top of standard BC manufacturing. If the client is food/beverage processing, don't force their process world into bare assembly orders — evaluate the add-on first. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Start one rung lower than the client's self-assessment. If in doubt between assembly and light manufacturing, pick assembly; if in doubt between light and full, pick light and add routings in phase 2 — adding routings later is feasible, removing a failed full-manufacturing rollout is a rescue project.

**Risk of getting it wrong:** medium — footprint can be extended later, but over-scoping burns budget and user trust, and moving items from assembly BOMs to production BOMs mid-life is disruptive (open orders, planning parameters, cost model all change).

**Expertise tags:** `#manufacturing` `#scoping` `#assembly` `#licensing`

---

## Manufacturing Setup — key toggles

**Where:** **Manufacturing Setup** page (General and Planning FastTabs).
**What it controls:** Company-wide defaults for production document numbering, default flushing, planning warnings, low-level code calculation, output presets and whether orders can finish without output.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Doc. No. Is Prod. Order No.** = on | Almost always — item and capacity ledger entries carry the production order no. as document no., making posted entries traceable back to the order | Rarely avoid; only if client has an entrenched external document numbering scheme for production postings |
| **Dynamic Low-Level Code** = on | Small/medium BOM structures; client edits BOMs often and runs planning ad hoc — codes stay current without a batch job | Large BOM structures / high data volume — performance hit (also during cost adjustment). Turn off and schedule the **Calculate Low-Level Code** batch job (daily job queue); it MUST run before Calculate Plan |
| **Planning Warning** = on | Default — planning raises warnings when planned dates can't be met; planners see exceptions | Warnings drown out signal for very high line volumes with an experienced planner who works purely from action messages |
| **Default Flushing Method** (Manual/Forward/Backward…) | Set to the method matching the *dominant* item behaviour so new items default correctly | Don't leave at Manual "for safety" if 90% of components should backward-flush — item creation discipline will drift |
| **Preset Output Quantity** = Expected Quantity | Output journal prefills remaining qty — fast for reliable shop floors | Sloppy floors "post what's prefilled"; use **Zero on All Operations** to force operators to type actual output |
| **Allow Finishing Prod. Order with no Output** = off | Default discipline: forces investigation before finishing orders with no posted output | Turn on only if client deliberately writes off WIP to inventory adjustment on abandoned orders and understands the accounting |
| **Cost Incl. Setup** = on/off | On when setup time is a material cost component (long changeovers, small batches) | Off keeps standard cost simpler when setup time is noise |

**Required client info:**
- How large and deep are the BOM structures, and how many items? (dynamic low-level code performance)
- Who creates item cards, and will they set flushing per item consciously?
- Should operators confirm actual output, or is expected quantity acceptable as a prefill?
- Does setup/changeover time meaningfully affect unit cost?

**Interactions:** Default Flushing Method feeds [Flushing methods](#flushing-methods-manual-vs-forward-vs-backward-vs-pick). Dynamic Low-Level Code interacts with [Planning setup](#planning-setup-mps-vs-mrp-parameters-forecasts) and with automatic cost adjustment ([costing method](inventory.md#costing-method-per-item)). Preset Output Quantity ties to [output/shop-floor registration](#capacityoutput-journals--shop-floor-registration).

**Add-on impact:** Aptean F&B adds its own process-manufacturing setup on top; standard Manufacturing Setup toggles still apply underneath. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Doc. No. Is Prod. Order No. on; Planning Warning on; Dynamic Low-Level Code on for typical SMBs (switch to nightly batch job if BOMs are large); Preset Output = Zero on All Operations unless the floor is proven reliable; Allow Finishing with no Output = off.

**Risk of getting it wrong:** low-to-medium — all toggles are changeable later, but forgetting the low-level code batch job when Dynamic is off silently corrupts planning runs.

**Expertise tags:** `#manufacturing` `#manufacturing-setup` `#planning`

---

## Work centers vs machine centers; shop calendars & capacity

**Where:** **Work Centers**, **Machine Centers**, **Work Center Groups**, **Shop Calendars**, work/machine center calendars (Calculate action); defaults for workday times come from Manufacturing Setup.
**What it controls:** The granularity of your capacity model: what routings point at, where costs and times are captured, and what the load pages show.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Work centers only (capacity ≥ 1 to represent parallel machines/people) | Most SMBs. Capacity planned at department/cell level; simpler master data; routings stay stable when a specific machine changes | Client genuinely schedules and costs per individual machine, or needs per-machine maintenance/downtime granularity |
| Work centers + machine centers underneath (Consolidated Calendar on the work center) | Per-machine scheduling, different speeds/costs per machine within a cell, machine-level output registration | Doubles master-data and registration burden; avoid where the floor barely copes with work-center-level posting |
| Work center groups | Always define — free aggregation layer for load overview and (with the subcontracting app) vendor assignment | — |

Shop calendars: define working days/shifts once per pattern (1-shift, 2-shift), assign to centers, and **calculate** center calendars far enough into the future (planning beyond the calculated horizon sees zero capacity). Efficiency % and Capacity fields tune effective throughput.

**Required client info:**
- Do you schedule "the CNC department" or "CNC machine #3"? Who decides which machine runs a job — the system or the foreman?
- Shift patterns, holidays, planned maintenance windows?
- Are operation costs different per machine within the same department?
- Remember: BC's planning is **infinite capacity** — does the client expect automatic finite scheduling? (Manage that expectation now; finite leveling is manual or via ISV.)

**Required client info addendum:** none.

**Interactions:** Routing design ([Production BOM & routing design](#production-bom--routing-design)) references these centers. Flushing method can be set per work/machine center and overridden on routing lines. Subcontract work centers are the backbone of [Subcontracting](#subcontracting-setup). Unit costs here flow into [standard cost rollup](#standard-cost-vs-actual-costing-for-manufactured-items). Open Shop Floor / To-Production bins on centers interact with [warehouse configuration](warehouse.md#item-journal-vs-warehouse-journal-per-level).

**Add-on impact:** Aptean F&B production lines/process cells map onto work centers; catch-weight and yield reporting hang off output postings at these centers. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Work centers only, one per department/cell, capacity field for parallel machines, one or two shop calendars — introduce machine centers only where a proven per-machine need exists.

**Risk of getting it wrong:** medium — restructuring centers later means rewriting every routing that references them; uncalculated calendars cause mysterious "no capacity" scheduling behaviour.

**Expertise tags:** `#manufacturing` `#capacity` `#work-centers` `#shop-calendar`

---

## Production BOM & routing design

**Where:** **Production BOM** page (with **Versions**), **Routings** page (with versions), routing link codes, scrap % on BOM lines / routing lines / item card; BOMs and routings must be **Certified** and assigned on the item card (Replenishment FastTab).
**What it controls:** Material and operation master data that every production order, planning run and cost rollup explodes from.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Flat single-level BOM | Simple products; subassemblies not stocked or tracked separately | You lose visibility/costing of intermediates that are physically stocked |
| Multi-level BOM with stocked subassemblies | Intermediates are made-to-stock, sold as spares, or produced in different batch sizes than parents | Every level adds a production order, postings and planning noise — don't model levels the floor doesn't actually stop at |
| Phantom BOM (BOM line of type Production BOM, no item) | Logical grouping of components that never exists as a stocked item — keeps engineering structure without extra orders | Client actually stocks the intermediate; phantoms have no inventory, no cost of their own |
| Versions (BOM & routing) with starting dates | Engineering changes, seasonal recipes; keeps history auditable — never edit a certified BOM in place for a real change | Trivial one-off corrections before go-live |
| Scrap % (routing line, BOM line, item card) | Predictable yield loss — planning and cost rollup inflate component demand accordingly | Unpredictable losses: better posted as actual scrap in journals than baked into standards |

Design rule: only certified BOMs/routings are usable; keep an ownership process for who certifies. Routing link codes (operation ↔ component binding) are prerequisites for per-operation flushing — decide them at design time, not after go-live.

**Required client info:**
- Which intermediates are physically stocked or sold separately? (drives levels)
- How often do recipes/designs change, and who approves changes? (drives version discipline)
- Is yield loss predictable per operation/component?
- Which components are consumed at which operation? (routing link codes)

**Interactions:** Routing link codes enable per-operation [flushing](#flushing-methods-manual-vs-forward-vs-backward-vs-pick). BOM depth drives low-level codes ([Manufacturing Setup toggles](#manufacturing-setup--key-toggles)). Scrap % and routing times feed [standard cost rollup](#standard-cost-vs-actual-costing-for-manufactured-items). Subassembly items need their own [reordering policies](inventory.md#replenishment--planning-parameters).

**Add-on impact:** Aptean F&B replaces/extends BOM thinking with recipe management, co-products/by-products and yield-based formulas — standard production BOM design rules still apply to the discrete parts of the flow. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** As flat as physically honest; phantoms for engineering groupings; versions mandatory from day one for any client with recurring engineering/recipe change; scrap % only where loss is statistically stable.

**Risk of getting it wrong:** medium — BOMs/routings are editable via versions, but a wrong level structure propagates into planning, WIP and costing everywhere, and cleanup competes with daily business.

**Expertise tags:** `#manufacturing` `#bom` `#routing` `#versions` `#scrap`

---

## Flushing methods (manual vs forward vs backward vs pick+…)

**Where:** Item card (Replenishment FastTab, **Flushing Method**); default in **Manufacturing Setup**; work/machine center **Flushing Method** for capacity; overridable per production order component / routing line. Routing link codes bind components to operations.
**What it controls:** Whether component consumption (and output at centers) is posted by hand in journals or automatically at order release, operation completion or order finish — the flagship discipline-vs-automation decision in BC manufacturing.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Manual** | Variable consumption (yield swings, substitutions); floor can and will record actuals in consumption/production journals; you want scrap visibility | Data entry burden is high; if the floor won't post, WIP and availability rot |
| **Forward** (at release; with routing link code: at operation start) | Cheap bulk components, kanban-style; consumption "good enough" at expected qty; minimal registration effort | Anything with real variability or theft/shrinkage concerns — actuals never observed; inventory accuracy decays silently |
| **Backward** (at finish; with routing link code: proportional to operation output) | The pragmatic default for disciplined-enough floors: consumption follows reported output, so availability and WIP valuation track progress without extra typing | Long-running orders without routing links — components look available for weeks while physically consumed; month-end WIP is misstated |
| **Pick + Forward / Pick + Backward** | Locations with mandatory bins or directed put-away & pick — consumption comes from the To-Production bin only after a warehouse pick, enforcing material staging | Basic locations without bins (not supported); floors where forcing a pick step just creates queue. Note: Pick + Forward can't have a routing link code to a forward-flushed operation |
| **Pick + Manual** | Warehouse-handled locations where consumption must be manual but picks must still be enforced | — |

Consultant judgement: map flushing to shop-floor discipline, not to elegance. High discipline → Manual (or Backward with routing links for the boring components, Manual for the value drivers). Medium discipline → Backward with routing link codes. Low discipline → Forward/Backward at expected quantity and accept standard-consumption accounting, then tighten via cycle counting. Mixing methods per item is normal and correct.

**Required client info:**
- For each component class: does actual usage deviate from BOM quantity by more than you care about financially?
- Will anyone on the floor touch a terminal/scanner between order release and finish?
- Are production locations bin-mandatory or directed pick? (gates Pick+ variants — see [warehouse](warehouse.md#item-journal-vs-warehouse-journal-per-level))
- How is scrap discovered today, and does anyone want to measure it?

**Interactions:** Requires routing link codes from [BOM & routing design](#production-bom--routing-design) for per-operation behaviour. Default set in [Manufacturing Setup](#manufacturing-setup--key-toggles). Determines whether the [consumption journal](#capacityoutput-journals--shop-floor-registration) is a daily tool or an exception tool. Wrong flushing corrupts availability that [planning](#planning-setup-mps-vs-mrp-parameters-forecasts) and [reordering policies](inventory.md#replenishment--planning-parameters) rely on, and misstates WIP in [finance](finance.md#inventory-posting-groups-and-inventory-posting-setup).

**Add-on impact:** Aptean F&B changes the consumption picture materially: catch-weight components and yield-variable recipes push toward actual-weight registration rather than expected-quantity flushing; the add-on provides shop-floor/scanning flows tuned to this. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Backward with routing link codes for standard components, Manual for high-value or high-variability components, Pick+Backward where bins are mandatory — and revisit six weeks after go-live against actual posting behaviour.

**Risk of getting it wrong:** medium — the field is changeable per item at any time, but months of wrong flushing mean wrong inventory, wrong WIP and a physical-count-and-revalue cleanup.

**Expertise tags:** `#manufacturing` `#flushing` `#consumption` `#shop-floor-discipline`

---

## Planning setup: MPS vs MRP, parameters, forecasts

**Where:** **Planning Worksheet** (Calculate Regenerative/Net Change Plan; MPS/MRP checkboxes), **Manufacturing Setup** Planning FastTab (**Combined MPS/MRP Calculation**, default safety lead time, blank overflow/dampeners), item card Planning FastTab, **Demand Forecast** page, **Requisition Worksheet** for purchase/transfer-only items.
**What it controls:** How demand (sales, forecast, safety stock) becomes suggested production and purchase orders across BOM levels — and who runs which worksheet.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Combined MPS/MRP, one regenerative run (weekly) + net change daily | The SMB norm: one planner owns end-to-end supply; simplest operating model | Separate master schedulers vs material planners exist and want separate MPS-then-MRP runs |
| Separate MPS run (end items from sales/forecast) then MRP (dependent demand) | Larger orgs; forecast-driven end-item scheduling reviewed before component explosion | Overkill when one person does both anyway |
| Planning Worksheet for everything vs Requisition Worksheet for purchased items | Split when a purchasing team replenishes independently of production planning (req. worksheet handles Purchase/Transfer items) | Duplicated/conflicting runs if both worksheets cover the same items without filters |
| Order Planning (order-by-order, no action messages) | Make-to-order shops with low volume wanting manual control per demand | Any volume — it doesn't scale and ignores parameter-based optimization |
| Demand forecasts (item/period/location) | Make-to-stock with seasonality; MPS needs forecast when sales orders arrive short-notice | Pure make-to-order (forecast consumption logic adds confusion for no benefit) |

Planning parameters live on the item (or SKU) card and interplay tightly with reordering policies — Lot-for-Lot with a reorder cycle is the workhorse for manufactured items; Fixed Reorder Qty/Maximum are for purchased commodity components; **Order** policy for pure MTO. Set Reserve = Never on planned manufactured items (reservations fight the planning engine). Dampener period/quantity suppress churn in action messages. Full parameter guidance: [reordering policies](inventory.md#replenishment--planning-parameters) and [planning parameters](inventory.md#replenishment--planning-parameters).

**Required client info:**
- Make-to-stock, make-to-order, or mixed — per product family?
- Is there a usable forecast, and at what granularity (item/month/location)?
- One planner or split purchasing/production planning roles?
- How much rescheduling noise will the planner tolerate? (dampeners, Planning Warning)
- Lead times and lot-size constraints per level of the BOM?

**Interactions:** Depends on correct low-level codes ([Manufacturing Setup](#manufacturing-setup--key-toggles)). Planning is infinite-capacity — check expectations set in [work centers](#work-centers-vs-machine-centers-shop-calendars--capacity). Availability accuracy depends on [flushing](#flushing-methods-manual-vs-forward-vs-backward-vs-pick). Item-level parameters: [inventory.md](inventory.md#replenishment--planning-parameters). Safety stock valuation ties to [costing](inventory.md#costing-method-per-item).

**Add-on impact:** Aptean F&B adds shelf-life/expiry-aware planning considerations and catch-weight quantities into the demand/supply picture; standard MPS/MRP mechanics remain underneath. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Combined MPS/MRP on; weekly regenerative + daily net change run by one planner; Lot-for-Lot on manufactured items, Order policy only for genuine MTO; forecasts only when make-to-stock with real seasonality and someone owns the forecast.

**Risk of getting it wrong:** medium — all reversible, but a badly parameterized first planning run that floods 400 action messages destroys planner trust in the tool, often permanently.

**Expertise tags:** `#manufacturing` `#planning` `#mrp` `#mps` `#forecast`

---

## Subcontracting setup

**Where:** Subcontract **Work Center** (Subcontractor No. on Posting FastTab, optionally Specific Unit Cost), routing lines of type Work Center, **Subcontracting Worksheet** (Calculate Subcontracts → purchase order); newer capability: **Subcontracting Setup** page + Subcontracting FastTab on Manufacturing Setup, **Subcontractor Prices**, vendor **Subcontracting Location Code** (per-vendor location recommended).
**What it controls:** How externally processed operations become purchase orders, how components get to the vendor, and how the vendor's charge lands in production cost.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Classic subcontract work center + subcontracting worksheet | The standard pattern: subcontracted step is a routing operation at a vendor-linked work center; worksheet generates the PO; receipt posts output of that operation | No routing exists (light manufacturing footprint) — subcontracting *requires* a routing line, type Work Center (machine centers don't support subcontractors) |
| Flat cost per vendor (Direct Unit Cost etc. on work center) | One rate per subcontractor regardless of item/operation | Rates differ per process — you'd maintain fictional work centers per rate |
| **Specific Unit Cost** on routing line | Vendor charges per operation/item; price lives on the routing line | Adds routing maintenance; skip if one rate fits |
| Subcontracting app features (Subcontractor Prices, per-vendor subcontracting location, component direct-unit-cost policy, item charges to subcontract receipts) | Heavy subcontracting: price lists per vendor/work-center-group/item, formalized component provision to vendor locations, freight/charges on subcontract receipts | Occasional one-off subcontracting — classic pattern is enough |
| Components at vendor as dedicated location per subcontractor | Material provided to the vendor must stay visible as own stock | Vendor supplies all material themselves (pure service purchase) |

**Required client info:**
- Which operations go outside, always or as overflow? (overflow = alternate routing versions)
- Who supplies the material — you or the subcontractor? Do you need to see your stock at their site?
- How does the vendor price: per unit, per hour, per operation, per item?
- Volume: occasional or an integral step of most routings?

**Interactions:** Requires the full-manufacturing footprint with [routings](#production-bom--routing-design) and [work centers](#work-centers-vs-machine-centers-shop-calendars--capacity). Subcontract PO cost posts into the production order and flows to [cost rollup](#standard-cost-vs-actual-costing-for-manufactured-items). Vendor locations interact with [inventory locations](warehouse.md#location-design) and transfer flows. Purchase approval on subcontract POs: [general-setup — approval workflows](general-setup.md#approval-workflows-native-vs-power-automate).

**Add-on impact:** Common in food (external smoking, packing, irradiation); Aptean F&B combines subcontracting with lot tracking and catch weight so the returned goods keep lot/weight integrity. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Classic subcontract work center per vendor (or per vendor-process pair), Specific Unit Cost when rates vary by operation, dedicated location per subcontractor holding your material; adopt the Subcontracting Setup app features only when volume justifies price-list maintenance.

**Risk of getting it wrong:** medium — reworkable, but subcontract costs landing wrong distort item costs and margins, and invisible material-at-vendor causes phantom shortages in planning.

**Expertise tags:** `#manufacturing` `#subcontracting` `#purchasing`

---

## Standard cost vs actual costing for manufactured items

**Where:** Item card **Costing Method**; **Standard Cost Worksheet** (roll-up + implement, revaluation); **Cost Incl. Setup** in Manufacturing Setup; indirect cost % / overhead rate on work centers and items; **Adjust Cost - Item Entries** / automatic cost adjustment in [Inventory Setup](inventory.md#costing-method-per-item).
**What it controls:** Whether manufactured items carry a frozen expected cost with variance postings (Standard) or a cost derived from actual consumption and time (typically FIFO/Average), and the discipline needed to keep either honest.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Standard** costing | Repetitive manufacturing, stable BOMs/routings; management wants variance analysis (material/capacity/subcontract variances) and stable margins; controller exists who will own annual/periodic roll-ups | No one will maintain standards — stale standards produce large, ignored variance buckets; volatile purchase prices make variance noise structural |
| **FIFO / Average** (actual) for manufactured items | Small shops without a controller; costs should simply follow actuals; recipe/purchase-price volatility high | Management wants variance reporting; actuals inherit every posting sin from the floor (bad flushing → bad unit costs, order by order) |

Cost rollup discipline (Standard): roll up via Standard Cost Worksheet bottom-up (components first — low-level codes matter), review, implement with revaluation at a controlled date (typically fiscal year start); never hand-edit a manufactured item's standard cost without rolling from components; decide whether setup time and overhead rates are in scope before the first rollup, not after.

**Required client info:**
- Is there a controller/finance person who will own standards maintenance and variance follow-up?
- How stable are component prices, BOMs and routing times over a year?
- Does management actually consume variance reports today, or want to?
- Mixed model acceptable? (Common: Standard for manufactured, FIFO for purchased — supported and often right.)

**Interactions:** Costing method is per item and effectively locked once entries exist — see [inventory.md — costing method](inventory.md#costing-method-per-item) for the full decision. Variance and WIP accounts must exist in the [posting setup](finance.md#inventory-posting-groups-and-inventory-posting-setup). Rollup accuracy depends on [BOM/routing quality and scrap %](#production-bom--routing-design) and work center rates ([work centers](#work-centers-vs-machine-centers-shop-calendars--capacity)). Actual costing quality depends directly on [flushing honesty](#flushing-methods-manual-vs-forward-vs-backward-vs-pick).

**Add-on impact:** Aptean F&B complicates costing with catch weight (cost per true weight vs per unit), co/by-product cost allocation and yield variance — verify the add-on's costing model before promising standard-cost variance reporting. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Standard costing for manufactured items *only if* a named person owns the rollup cycle; otherwise FIFO and honest journals. Never default to Standard because "manufacturers use standard costing" — orphaned standards are worse than actuals.

**Risk of getting it wrong:** high-irreversible — costing method cannot be changed once item ledger entries exist (workaround = new item numbers + inventory migration), and years of misallocated variances are unauditable.

**Expertise tags:** `#manufacturing` `#costing` `#standard-cost` `#variances` `#finance`

---

## Capacity/output journals & shop floor registration

**Where:** **Production Journal** (per order line: consumption + output combined), **Output Journal** and **Consumption Journal** (batch, multi-order), **Capacity Journal** (time not tied to a production order); Preset Output Quantity in Manufacturing Setup; scrap codes/stop codes on journal lines.
**What it controls:** How run times, setup times, output quantities and scrap get from the floor into item & capacity ledger entries — the data source for actual costs, WIP and capacity follow-up.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Production Journal per order (office or supervisor posts) | Default for SMBs: one page, consumption + output together, posted end-of-shift or at operation completion | High order volume where per-order journal opening is too slow — use batch output journal |
| Output Journal batch posting (+ Explode Routing) | Central production office posts many orders at once from paper/records | Loses immediacy; availability lags reality by the batch cycle |
| Heavy flushing + exception-only journals | Low-discipline floors: forward/backward flush everything, journal only scrap and deviations | Anyone wanting true actual times/quantities — you've standardized them away |
| Capacity Journal for indirect time | Track maintenance, cleaning, downtime against centers without a production order | Nobody will analyze it — pure ceremony |
| Barcode/terminal shop-floor data capture (ISV or Aptean shop floor) | Real-time registration wanted; volume justifies devices and licenses | Micro floors where a supervisor with the Production Journal is faster and cheaper |

Note: standard BC has no full MES; if the client demos "operators scan start/stop on tablets", that's an ISV/add-on conversation, not base configuration.

**Required client info:**
- Who physically records production data, where, and how long after the event?
- Are actual times wanted for costing/efficiency, or only quantities?
- Is scrap recorded with reasons (scrap codes) and does anyone review it?
- Devices available on the floor? Wi-Fi coverage? Gloves/washdown environment (food)?

**Interactions:** Registration intensity must match the [flushing decision](#flushing-methods-manual-vs-forward-vs-backward-vs-pick) — heavy flushing + heavy journaling double-posts effort; manual flushing + no registration capability is a design contradiction. Output posting to bins interacts with [warehouse flows](warehouse.md#item-journal-vs-warehouse-journal-per-level). Times posted here are the actuals behind [costing](#standard-cost-vs-actual-costing-for-manufactured-items) and capacity load review.

**Add-on impact:** Aptean F&B provides shop-floor-oriented registration (scanning, catch-weight capture at output, lot assignment at reporting) purpose-built for food processes — usually the answer when base journals don't fit the floor. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Production Journal posted by shift supervisors at operation/shift end, backed by backward flushing for routine components; add scanning only after the paper process is proven.

**Risk of getting it wrong:** low-to-medium — journals and habits can be changed, but a floor that learned "the system doesn't need us to post" in week one is expensive to re-train.

**Expertise tags:** `#manufacturing` `#output` `#capacity-journal` `#shop-floor`
