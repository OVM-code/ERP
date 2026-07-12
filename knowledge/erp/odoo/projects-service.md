# Projects & Service — Odoo (Standard)

> **Scope:** Odoo 19 Enterprise (Odoo Online, Odoo.sh or on-premise); Community edition differences flagged inline. Compact by design: scope decisions only — deepen per real client need.
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when Odoo releases functional changes to this area (one major release per year, typically October).

Covers the Project app (tasks, stages, milestones), service selling and invoicing via Sales, Timesheets, and the Enterprise service apps (Helpdesk, Field Service, Planning). In scope for clients that sell time, projects or after-sales service; for pure trade/production clients most of this file is consciously out of scope.

---
## Project & task structure
**Where:** Project app — project settings, task stages; service tracking on the product card.
**What it controls:** Whether work is tracked in projects at all, and how projects map to the client's commercial reality (one per customer vs one per engagement).

| Option | When it fits | When to avoid |
|---|---|---|
| No Project app — analytic accounts only | Client only wants P&L per activity, no task/work tracking | Anyone billing time or managing deliverables |
| One long-running project per client | Recurring support/retainer work, small engagements | Fixed-scope engagements needing per-deal profitability |
| One project per engagement (auto-created from the sales order via the service product) | Project businesses: implementations, construction, agencies | High volume of tiny orders — project sprawl |

**Required client info:**
- Do they need to track work (tasks, deadlines, who does what) or only money per activity?
- Is the billing/profitability unit the customer relationship or the individual engagement?
**Interactions:** Service products can auto-create a project and/or task per sales order line — decide jointly with [Service invoicing policies](#service-invoicing-policies-tm-fixed-milestones). Task stages are per project (shareable); keep the stage set minimal.
**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.
**Default recommendation:** Project per engagement, auto-created from the sales order, for project-driven clients; one project per client for retainer-style service.
**Risk of getting it wrong:** low — projects can be restructured, but historical profitability comparisons get muddy.
**Expertise tags:** `#projects` `#service`

---
## Service invoicing policies (T&M, fixed, milestones)
**Where:** Product card (service type) — invoicing policy and service tracking fields; milestones on the project.
**What it controls:** When and how service revenue is invoiced, and how tasks link back to the sales order item that funds them.

| Option | When it fits | When to avoid |
|---|---|---|
| Prepaid / fixed price (invoice ordered qty) | Fixed-fee packages, prepaid hour bundles | Scope varies — margin invisible until too late |
| Based on timesheets (invoice delivered hours) | Classic T&M billing; hours flow from task timesheets to the invoice | Client refuses variable invoices; weak timesheet discipline |
| Based on milestones | Long fixed-price projects invoiced per phase | Short engagements — administrative overkill |

**Required client info:**
- Contract types actually sold: T&M, fixed-fee, milestone-based, retainers — in what mix?
- Must every billable hour trace to a sales order line, or is billing looser?
**Interactions:** Each task's sales order item determines what its timesheets are invoiced against — see [sales](sales.md#invoicing-policy--down-payments) for the general invoicing-policy and down-payment logic. Timesheet-based invoicing presupposes the next block.
**Add-on impact:** No add-on overlays recorded for Odoo in this knowledge base yet.
**Default recommendation:** Match the product to the contract: timesheet-based for T&M, milestones for phased fixed-price work — don't force one policy on all services.
**Risk of getting it wrong:** medium — changing the policy on already-sold order lines is painful; credit notes and manual fixes follow.
**Expertise tags:** `#service` `#projects`

---
## Timesheets & profitability
**Where:** Timesheets app; project profitability/dashboard view; analytic account on the project; hourly cost on the employee record.
**What it controls:** How hours are captured, which are billable, and whether per-project margin (invoiced revenue vs cost of hours and purchases) is visible.

| Option | When it fits | When to avoid |
|---|---|---|
| No timesheets | Nobody bills or costs time | Any T&M billing or labour-cost interest |
| Timesheets for costing only (non-billable) | Client wants project margin but bills fixed-fee | — |
| Timesheets driving invoicing (billable vs non-billable per line) | T&M businesses | Teams that won't book hours reliably — invoices become wrong, not just margins |

**Required client info:**
- Will staff actually book hours daily/weekly, and who validates them?
- Is an hourly cost per employee available (needed for real profitability)?
**Interactions:** Every project carries an analytic account; timesheets post analytic cost lines against it — analytic plan design lives in [general setup](general-setup.md#analytic-accounting-architecture-plans--distributions). **Community edition:** only basic timesheet lines on tasks; the full Timesheets app (grid entry, validation, timers) is Enterprise. > ⚠️ Verify against current Odoo documentation.
**Add-on impact:** None known — this knowledge base holds no Odoo add-on layer so far.
**Default recommendation:** Timesheets on for any service client, with employee costs filled in — profitability without hour costs is fiction.
**Risk of getting it wrong:** medium — missing or costless historical hours can't be reconstructed; margin history is lost, not just delayed.
**Expertise tags:** `#timesheets` `#profitability`

---
## Helpdesk, field service & planning scope
**Where:** Helpdesk, Field Service and Planning apps (each installed and configured separately).
**What it controls:** Whether after-sales support (tickets, SLA policies), onsite interventions (worksheets, onsite invoicing) and shift scheduling run in Odoo. **Community edition:** all three apps are Enterprise-only — without them, tickets end up misused as project tasks. > ⚠️ Verify against current Odoo documentation.

| Option | When it fits | When to avoid |
|---|---|---|
| None — email and projects suffice | No structured support or field obligations | SLA commitments exist — you'll fail them invisibly |
| Helpdesk (teams, SLA policies, tickets billable via timesheets) | Support is a real workload or revenue stream | A handful of mails per week — overhead exceeds value |
| Field Service and/or Planning (onsite tasks + worksheets; shifts, roles, published schedules) | Technicians on the road; rostered or dispatch-style teams | No onsite work and stable 9-to-5 teams |

**Required client info:**
- Ticket/intervention volume per week; contractual SLAs or response-time promises?
- Do field technicians need mobile worksheets and onsite payment/signature?
**Interactions:** Helpdesk and Field Service both bill through sales orders and timesheets — the [invoicing policy](#service-invoicing-policies-tm-fixed-milestones) decisions apply to them too; field service material consumption touches inventory.
**Add-on impact:** Nothing yet — the Odoo add-on layer of this knowledge base is still empty.
**Default recommendation:** Out of scope unless the client names support or field work as a revenue stream or contractual duty; each app is its own mini-implementation — scope them one at a time, never as a bundle.
**Risk of getting it wrong:** low — all three can be added later without disturbing the existing setup.
**Expertise tags:** `#service` `#projects`
