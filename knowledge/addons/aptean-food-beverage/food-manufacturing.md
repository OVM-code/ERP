# Food Manufacturing — Aptean Food & Beverage ERP

> **Add-on:** Aptean Food & Beverage ERP (Business Central embedded)
> **Base ERP:** Microsoft Dynamics 365 Business Central
> **Last reviewed:** 2026-07

The Aptean Process Manufacturing extension (PRM) reshapes BC's discrete manufacturing into process/batch manufacturing: production BOMs with **batch size** and scalable recipes, **yield percentage** and process weight change per component, **co-products** (one input, multiple outputs) with consumption allocation and cost apportionment, and **unplanned output and consumption** registration. Around it sit the Shop Floor Production app (SFP/SFPBC) for operator registration, Process Manufacturing OEE (APMOEE), and Product Specifications (PRS) for allergen and spec data. This module requires **BC Premium** licensing (production orders). It's for actual manufacturers — meat/fish disassembly, dairy, bakery, blending/batching, beverages; distributors with light repack can often stay on assembly orders.

---

## Changes to standard setup decisions

### Modifies: BOM & routing structure ([standard file](../../erp/business-central/manufacturing.md#production-bom--routing-design))

**How it changes:** extends significantly. Standard BC BOM quantities are per parent unit. PRM lets you define the BOM against a **batch size** (recipe for a 500 kg batch) with product yield % and per-component process weight change % (loss/gain in cooking, drying, marinating), scaling orders to any batch quantity.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Quantity-per-parent BOM | yes | Fine for packing/assembly stages; keep it there. |
| Phantom BOMs | yes | Still useful for label/pack variants. |
| Batch-size recipe BOM | new default for process stages | Model the recipe as the kitchen writes it; let the system scale. |
| Routing with fixed setup/run times | yes, extended | Line-based thinking (batching, then packaging) usually maps to fewer, bigger work centers than a discrete client would use. |

### Modifies: Production order execution & output posting ([standard file](../../erp/business-central/manufacturing.md#capacityoutput-journals--shop-floor-registration))

**How it changes:** extends. Unplanned output and consumption become first-class: registering an extra output item or extra consumption on a running order without pre-engineering the BOM change. Output for co-product structures posts multiple items from one order, with consumption allocated across them.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Output = the one parent item, quantity as planned | changed | Real food orders produce the main product, co-products, and sometimes downgrade product — the module models this instead of forcing fake orders. |
| Backward flushing of components | yes, dangerous | Backflush guesses lots; in a lot-traceability environment prefer forward/pick-based consumption or shop-floor registration for anything trace-critical (see [lot-management-traceability.md](lot-management-traceability.md)). |
| Journal-based output posting by office staff | yes, discouraged | Shop Floor Production app moves registration to the operator at the line, with lot and weight capture. |

### Modifies: Item setup for manufactured items ([standard file](../../erp/business-central/inventory.md#costing-method-per-item))

**How it changes:** extends. Manufactured food items carry recipe/spec data: allergen declarations and product specifications (PRS) with analysis of allergen presence rolled up from ingredients.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Free-text item description of composition | no | Allergen and spec data must be structured — labels and customer specs are generated/validated from it. |
| Item attributes (standard BC) | yes, supplemented | PRS provides purpose-built specification/allergen structures with analysis; use those for food safety data, standard attributes for commercial data. |

### Modifies: Costing of production ([standard file](../../erp/business-central/finance.md#inventory-posting-groups-and-inventory-posting-setup))

**How it changes:** extends/constrains. With co-products, order cost must be apportioned across outputs (Aptean Production Cost Apportionment integrates here, including with warehouse flows). Single-output cost logic underneath is unchanged, but controllers need to sign off the apportionment basis.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| All order cost → the single parent | changed | Replaced by apportionment across primary product and co-products for disassembly/multi-output processes. |
| Standard cost for manufactured items | yes, with care | Meaningful only if yields are stable; with volatile yields prefer actual costing and manage yield as a KPI. |

---

## New setup decisions introduced by this module

### Process model: batch-size recipes vs. discrete BOMs per stage

**Where:** PRM — production BOM with batch size, product yield %, process weight change % per component
**What it controls:** how each production stage is modelled: scalable recipe (process stages: mixing, cooking, fermenting) vs. per-unit BOM (packing stages), and how many BOM levels separate raw → bulk/WIP → packed SKU.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Two-level model: bulk recipe (batch-size) + packing BOM per SKU | Most food manufacturers — bakery, dairy, sauces, beverage | Trivially simple one-step producers where one level does the job |
| Single-level, batch-size recipe straight to SKU | One recipe, one pack format | Multi-format packing off shared bulk — you'll duplicate the recipe per SKU and it will drift |
| Deep multi-level (pre-mixes as stocked items) | Pre-mixes genuinely stocked/shared across products | Modelling every kettle transfer as a stocked item — order admin explodes |

**Required client info:**
- Actual recipes with batch sizes and where yields are measured today (get the spec sheets, not a verbal description)
- Whether bulk/WIP is physically stored between stages (stocked WIP) or flows continuously (keep in one order)
- Number of pack formats per recipe

**Interactions:** batch size interacts with equipment capacity (kettle size) and scheduling; lot genealogy follows the BOM levels — a stocked bulk item creates a trace hop that must be lot-tracked; yield % here is what OEE/yield reporting measures against.
**Default recommendation:** two-level (bulk recipe + packing BOM) for anyone with shared bulk and multiple pack formats; keep WIP items only where WIP physically waits in stock.
**Risk of getting it wrong:** high — the BOM architecture is the skeleton of costing, planning and traceability; restructuring after go-live touches every order and history comparison.
**Expertise tags:** `#aptean-fnb` `#process-manufacturing` `#bom-design`

### Yield & loss registration policy

**Where:** PRM — product yield %, process weight change % per component; weight and yield percentage calculations from input/output weights
**What it controls:** planned vs. actual yield: what loss is engineered into the BOM (expected cook loss) vs. what is registered as deviation at execution, and at which stages weights are actually captured.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Engineered yield in BOM + actual weights registered → variance reporting | Processors managing margin on yield (meat, fish, dairy) — the target model | No weighing capability at stage boundaries (fix that first, see [catch-weight.md](catch-weight.md)) |
| Engineered yield only, actuals assumed | Stable, low-value processes; phase 1 | Anywhere yield is a top-3 cost driver — you're flying blind exactly where money leaks |
| 100% yield in BOM, all loss as scrap postings | Never as design | Hides expected loss inside "scrap", making real anomalies invisible |

**Required client info:**
- Which stages lose/gain weight and the expected range (cook loss, drip loss, water uptake)
- Where scales exist between stages; whether catch weight items flow through
- The yield KPI management already uses — the system must reproduce it or explain the difference

**Interactions:** actual weights come from Shop Floor Production/catch weight registration; yield variance is where shrinkage, giveaway and theft appear — controlling will build reports on this; QC in-process checks often capture the same weighings (avoid double registration).
**Default recommendation:** engineer known process losses into the BOM, register actual weights at every stage boundary the client can weigh, and review yield variance weekly in the first quarter after go-live.
**Risk of getting it wrong:** medium-high — recoverable in config, but a first year of meaningless yield numbers costs the project its credibility with operations management.
**Expertise tags:** `#aptean-fnb` `#yield` `#process-manufacturing` `#costing`

### Co-product / by-product architecture

**Where:** PRM — co-products (one input, multiple outputs; register input once, multiple outputs during production; consumption allocation between primary items and co-products), Production Cost Apportionment
**What it controls:** which secondary outputs are modelled as co-products on the order (trim, offal, whey, B-grade, dough re-work) vs. negative-value waste, and how cost is apportioned across outputs.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Full co-product model with cost apportionment | Disassembly processes (meat/fish cutting), dairy separation — anywhere secondary outputs have real value | Outputs with negligible value — model as scrap/waste, don't burden orders |
| Co-products at zero/fixed value, all cost to primary | Simple cases; conservative accounting preference | When co-product margin is actually managed (then it needs real cost) |
| By-product as re-usable input (rework loop: dough, trimmings back into recipes) | Bakery/meat rework flows | Unmanaged rework loops without lot discipline — allergen carryover risk lives here |

**Required client info:**
- Full output list per process with realistic values (walk the floor, the BOM on paper always misses outputs)
- How the client prices/sells co-products (drives apportionment basis: market value vs. weight vs. fixed)
- Rework flows and their allergen implications

**Interactions:** apportionment integrates with AWM/warehouse flows; co-product lots inherit genealogy from the input lot (recall implications: one contaminated carcass touches every output); rework loops must carry allergen status (below).
**Default recommendation:** co-products for every output the client sells or re-uses; market-value-based apportionment where co-product prices are volatile (meat), weight-based where outputs are homogeneous.
**Risk of getting it wrong:** high — wrong apportionment misstates margin per product line and silently misprices the primary product.
**Expertise tags:** `#aptean-fnb` `#co-products` `#costing` `#process-manufacturing`

### Unplanned output & consumption policy

**Where:** PRM — unplanned output and consumption registration on production orders
**What it controls:** whether operators may register outputs/consumption not on the order's BOM (extra ingredient added, unexpected downgrade output), and under what control.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Allowed, with reason codes and review | Real food production — recipes get adjusted at the kettle; capturing truth beats forcing lies | — |
| Allowed freely, no review | Never | Uncontrolled unplanned consumption is the end of recipe cost integrity |
| Forbidden (BOM change required first) | Regulated recipe environments (infant formula) | Normal operations — operators will post fake "planned" entries instead |

**Required client info:**
- How often recipes are adjusted in-flight today and by whom
- Whether allergen-relevant substitutions ever happen ad hoc (they must be blocked or flagged, not merely recorded)

**Interactions:** unplanned consumption of a different lot/ingredient changes trace and allergen status of the batch — connect to PRS analysis; frequent unplanned entries on the same recipe are a signal to fix the BOM.
**Default recommendation:** allow with mandatory reason codes; weekly review by both controlling (cost) and QA (allergen/trace); hard-block substitutions that change the allergen profile.
**Risk of getting it wrong:** medium — the control is adjustable, but an early culture of casual unplanned postings is hard to walk back.
**Expertise tags:** `#aptean-fnb` `#process-manufacturing` `#shop-floor` `#governance`

### Shop-floor registration model

**Where:** Shop Floor Production app (SFP) + its BC setup (SFPBC); optionally APMOEE for OEE capture
**What it controls:** whether operators register consumption, output, lots, weights and downtime at the line via the app, or production is posted from journals/back office.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| SFP app at every line (operator self-registration) | Target state for manufacturers; enables QC triggers, real-time lot/weight capture | Tiny operations (one mixer, three staff) where a shared terminal suffices |
| Shared terminal per area | Mid-size, budget-constrained | High-frequency registration points — queueing kills compliance |
| Back-office posting from paper | Bridge only | As target state it forfeits trace timeliness, yield truth and QC integration |
| Add APMOEE for downtime/OEE | Clients with line-efficiency programs | Before basic registration is stable — OEE on bad data is decoration |

**Required client info:**
- Lines, shifts, device/Wi-Fi situation on the floor; operator IT literacy and languages
- Whether QC production checks are in scope (they surface through this app — see [quality-control.md](quality-control.md))

**Interactions:** shares device estate with Mobile Warehouse and QC apps — run one hardware project; registration quality here determines lot genealogy, yield and co-product data quality everywhere else.
**Default recommendation:** SFP app on every line that produces lot-tracked output; phase OEE in a later wave.
**Risk of getting it wrong:** medium — deployment is adjustable; under-investing in devices/training is the most common cause of "the module doesn't work" escalations.
**Expertise tags:** `#aptean-fnb` `#shop-floor` `#mobile` `#adoption`

### Allergen & product specification management

**Where:** PRS — product specifications, allergen records, product specification analysis (allergen presence values rolled up/analysed across the BOM)
**What it controls:** structured allergen data per item (contains / may contain / free-from), specification documents, and analysis that derives finished-product allergen status from ingredient data.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Full PRS: ingredient allergen data + roll-up analysis to finished specs | Manufacturers making label/spec claims — the defensible model | — |
| Allergen data maintained only on finished items (manual) | Pure distribution of finished goods | Any manufacturing — manual finished-item data goes stale the first time a supplier reformulates |
| External spec system (e.g. dedicated PLM) as master, ERP mirrors | Clients already invested in a spec/PLM platform | Duplicated maintenance without a defined master — two diverging truths is worse than one imperfect one |

**Required client info:**
- Jurisdictions sold into (allergen lists differ: EU 14, US 9, etc.)
- Supplier spec collection process — the data is only as good as vendor declarations, plan the intake process
- Cross-contact policy (shared lines) — "may contain" is a process decision, scheduling and cleaning validation included, not just a data field

**Interactions:** rework/co-product loops and unplanned consumption can change batch allergen status — those controls must consult this data; production scheduling on shared lines should sequence allergen-light → allergen-heavy with cleaning breaks; label generation and customer spec sheets read from here.
**Default recommendation:** PRS as the single allergen master, populated ingredient-up; block allergen-profile-changing substitutions at the shop floor; review supplier declarations on a fixed cycle.
**Risk of getting it wrong:** high-irreversible in consequence — undeclared allergens are the #1 cause of food recalls; this is a safety control, not a data nicety.
**Expertise tags:** `#aptean-fnb` `#allergens` `#product-specifications` `#compliance`

> ⚠️ Verify against current Aptean documentation — batch-size BOM, yield %, process weight change %, co-products and unplanned output/consumption are grounded in Aptean's public PRM docs; cost apportionment mechanics and PRS field-level behaviour are partner-gated, validate in the client's version.
