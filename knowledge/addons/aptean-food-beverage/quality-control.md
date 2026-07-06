# Quality Control — Aptean Food & Beverage ERP

> **Add-on:** Aptean Food & Beverage ERP (Business Central embedded)
> **Base ERP:** Microsoft Dynamics 365 Business Central
> **Last reviewed:** 2026-07

The Aptean Quality Control extension (QCL) plus its companion **Quality Control app** (QCA) bring structured QC into BC: quality plans with check points (inbound, production, outbound, recurring), automatically **triggered quality checks** assigned to quality teams by check point and warehouse, result registration on mobile/tablet, disposition actions (release, block, reject, rework) and Certificate of Analysis output (REP reporting). For food clients this is the difference between "QA keeps a spreadsheet" and inventory that physically cannot ship until released. The design tension: every check you configure is labour on receiving docks and lines — configure the checks the food safety plan requires, not everything the QA manager can imagine.

---

## Changes to standard setup decisions

### Modifies: Item/lot blocking approach ([standard file](../../erp/business-central/inventory.md#item-tracking-lot--serial--package))

**How it changes:** replaces ad-hoc practice. Standard BC offers blunt instruments (item blocked, lot blocked flag, moving stock to a "QA location"). QC introduces status-driven holds tied to check results — a lot under inspection is unavailable to picking/shipping until released, with an audit trail of who released it and on what result.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Manual lot blocked flag | yes, demoted | Keep for exceptional/manual holds; routine inspection holds should come from QC checks, not memory. |
| Separate quarantine location/bin | yes, optional | Physical segregation can still make sense (allergen, temperature), but it's no longer the *system* mechanism for hold — don't build the process on stock moves alone. |
| No formal hold process | no | With this module installed, an unmanaged hold process is an implementation failure, not an option. |

### Modifies: Warehouse receiving flow ([standard file](../../erp/business-central/warehouse.md#warehouse-document-flow-toggles))

**How it changes:** extends. Inbound check points generate quality checks on receipt (by item/vendor/check plan); put-away may proceed to a hold state but stock stays unavailable until the check passes. Receiving throughput planning must include inspection time.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Post receipt directly to available stock | changed | Only for item/vendor combinations without an inbound check plan. |
| Receipt → inspection → release | yes (now systemised) | The module automates check creation and the release gate. |

### Modifies: Production order execution ([standard file](../../erp/business-central/manufacturing.md#capacityoutput-journals--shop-floor-registration))

**How it changes:** extends. QC integrates with Shop Floor Production: quality checks can be triggered from work centers, production orders, and on a recurring basis (e.g. hourly line checks); outstanding checks are visible to operators and executed in the QC app. Output can be held pending release before it becomes shippable.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Output posting straight to available inventory | changed | For QC-relevant items, output lands under hold until in-process/final checks pass. |
| Paper HACCP/line-check records | yes, discouraged | Legally acceptable, but you lose the trigger-and-escalate machinery and CoA data capture. |

### Modifies: Vendor management / purchasing controls ([standard file](../../erp/business-central/purchasing.md#vendor-templates--vendor-master-data-governance))

**How it changes:** extends. Check plans can differentiate by vendor (approved vendors get skip-lot or reduced inspection; new/problem vendors get 100%). Vendor performance conversations get data: rejection rates per vendor from check results.

| Standard option | Still valid with this module? | Notes |
|---|---|---|
| Uniform receiving controls for all vendors | yes, but wasteful | Risk-based inspection intensity is the point of configurable plans. |

---

## New setup decisions introduced by this module

### Check point & trigger architecture

**Where:** Quality Control Setup and Monitoring — quality plans, check points, Quality Control Triggers (incl. work-center-based and recurring triggers via Shop Floor Production integration)
**What it controls:** *when* the system creates a quality check: inbound receipt, production (per order, per work center, recurring interval), outbound before shipping, or ad hoc/recurring on stock (e.g. retained samples, ageing checks).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Inbound checks only (phase 1) | Distributors; manufacturers starting adoption | Processors whose real risk is in-process (then this is theatre) |
| Inbound + production checks (per order / per work center / recurring) | Manufacturers with HACCP CCP monitoring to digitise | Lines with no operator device — checks will be batch-faked at shift end, which is worse than paper |
| Full farm-to-fork: inbound, in-process, pre-ship, recurring stock checks | Audited environments (BRC/IFS/SQF), RTE and high-risk products | Rolling all out in one go — sequence it |

**Required client info:**
- The client's HACCP plan and CCP list — the check architecture should mirror it, not reinvent it
- Audit scheme requirements (frequency, records, sign-off)
- Devices available at each check location (the QCA app needs something to run on)

**Interactions:** production triggers require the Shop Floor Production extension; inbound checks interact with put-away flow and dock capacity; check results can populate lot attributes (single source — see [lot-management-traceability.md](lot-management-traceability.md)).
**Default recommendation:** mirror the HACCP plan: inbound checks for high-risk ingredients, CCP checks as production/recurring triggers, pre-ship checks only where customers contractually require positive release. Go live in two waves (inbound first, production second).
**Risk of getting it wrong:** medium — plans are adjustable, but over-instrumenting at go-live is the classic adoption killer for this module.
**Expertise tags:** `#aptean-fnb` `#quality-control` `#haccp` `#adoption`

### Quality plan content: tests, sampling, teams

**Where:** Quality Control Setup — quality teams, equipment, units of measure; quality plans per item (category)/check point; team assignment derives from check point type + location
**What it controls:** what each check measures (attributes with target/limits, pass/fail, text observations), sample size logic, and which quality team the check auto-assigns to based on check point and warehouse.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Short plans: the 3–8 values QA actually acts on | Everyone at go-live | — |
| Full lab-sheet replication (20+ values) | Only where a CoA to customers requires every value | As default — every field is registration time, and unused data rots |
| Team per check-point type (inbound team, line QA, lab) | Sites with dedicated QA staffing | Micro-sites where one person does everything — keep one team, avoid routing complexity |

**Required client info:**
- Current inspection sheets/lab forms (take real ones, strike out what nobody acts on)
- Which measured values appear on customer CoAs (those must be captured structured)
- QA staffing per site/shift — checks assigned to a team nobody staffs on nights will pile up and get bulk-passed

**Interactions:** measured values feed Certificate of Analysis (REP); limits can drive automatic disposition proposals; equipment records support calibration traceability.
**Default recommendation:** start from the CoA backwards — anything printed to customers is structured; the rest earns its place per field. One team per check-point type per site, no finer.
**Risk of getting it wrong:** low-medium — content is editable; the irreversible part is floor trust, lost by bloated plans.
**Expertise tags:** `#aptean-fnb` `#quality-control` `#coa` `#master-data`

### Hold & disposition policy (blocking behaviour)

**Where:** quality check result handling / quality control actions — disposition on pass/fail
**What it controls:** what a check outcome does to the stock: hold until explicit release (positive release), released-unless-failed (negative release), and the failure paths — block, reject to vendor (purchase return), rework order, downgrade/re-grade, destroy.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Positive release (hold everything until passed) | High-risk/RTE product, micro testing with lab lead times, contractual positive release | Short-shelf-life fresh flows where 24h hold kills saleability — unless the customer mandates it, then the process must be built around lab turnaround |
| Negative release (available unless failed) | Low-risk items, trusted vendors, in-spec history | Where a failed test after shipment means recall — you've built a recall generator |
| Mixed, by item risk class | Most real clients | Only if the risk classification is actually maintained |

**Required client info:**
- Lab turnaround times vs. product shelf life (this decides positive vs. negative release more than policy preference does)
- Who may release, who may release *with deviation* (concession) — map to permission sets, keep the concession list short
- Failure-path economics: is rework real? is vendor rejection commercially feasible?

**Interactions:** holds must be respected by warehouse picking, Mobile Warehouse and route/load planning (a held pallet on a planned trip is a dispatch incident); expiry near-date stock may need re-check rules (EXM); failed inbound checks generate vendor performance data for purchasing.
**Default recommendation:** positive release only where risk or contract demands it; negative release with sharp failure handling elsewhere. Document the concession/deviation path explicitly — the informal "QA manager says ship it" override is where audits fail.
**Risk of getting it wrong:** high — too loose ships unsafe product; too strict and operations pressure QA into rubber-stamp releases, which is the same failure with extra steps.
**Expertise tags:** `#aptean-fnb` `#quality-control` `#holds` `#compliance`

### Execution surface: BC client vs. Quality Control app

**Where:** deployment choice — checks processed in Business Central pages (QCL) vs. the dedicated Quality Control app (QCA) on mobile/tablet
**What it controls:** where inspectors record results; affects device provisioning, licensing and check ergonomics.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| QCA app at the point of inspection | Docks, lines, anywhere gloves and distance from a PC are realities | — this is the default for floor checks |
| BC pages only | Lab-centric QA (results typed from lab systems), office QA teams | Floor checks — walking to a PC guarantees batch entry from memory |
| Mixed: app on floor, BC pages in lab | Most manufacturers | — |

**Required client info:**
- Device inventory and Wi-Fi coverage in inspection areas (cold stores are the usual dead zone)
- Whether an external LIMS exists that should feed results instead (integration, not re-typing)

**Interactions:** app rollout usually rides on the same devices as Mobile Warehouse (MWR) — coordinate the hardware project; production checks surface to operators in the Shop Floor Production app with execution in QCA.
**Default recommendation:** app for all physical-inspection check points; BC pages for lab/desk work.
**Risk of getting it wrong:** low — switchable; just budget devices before go-live, not after.
**Expertise tags:** `#aptean-fnb` `#quality-control` `#mobile` `#infrastructure`

### Certificate of Analysis output

**Where:** REP (reporting) — Certificate of Analysis based on registered quality results
**What it controls:** which customers/items get a CoA with shipments, and which measured values it exposes.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Auto CoA per shipment for flagged customers/items | B2B ingredient supply, private label | Consumer-goods distribution where no one asks |
| On-demand CoA | Occasional requests | High CoA volume — manual generation won't keep up |

**Required client info:**
- Which customers contractually require CoAs and the exact values/layout they expect (collect real examples)
- Language/branding requirements per market

**Interactions:** only structured check results can print — this back-propagates into quality plan content (above); lot attributes may supplement.
**Default recommendation:** automatic for contractual customers, on-demand otherwise; validate the layout with the two most demanding customers before go-live.
**Risk of getting it wrong:** low — report iteration; reputational only if a CoA states values you don't actually measure.
**Expertise tags:** `#aptean-fnb` `#quality-control` `#coa` `#reporting`

> ⚠️ Verify against current Aptean documentation — check-point/trigger and team-assignment behaviour is grounded in Aptean's public QCL/QCA docs; disposition/hold configuration detail is partner-gated and version-dependent, so validate the exact blocking mechanics in the client's environment.
