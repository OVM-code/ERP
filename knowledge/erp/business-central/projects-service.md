# Projects & Service — Business Central (Standard)

> **Scope:** Microsoft Dynamics 365 Business Central (SaaS, current version)
> **Last reviewed:** 2026-07
> **Maintainer note:** Compact area file — most trade/food clients don't use these
> modules. Expand into full decision blocks the first time a client puts them in scope.

Projects (formerly Jobs) covers project cost tracking, WIP and project invoicing.
Service Management covers service orders, contracts and dispatching for repair/field
service. Both are Premium-experience-independent (Projects is in Essentials; Service
requires Premium licensing for some scenarios — verify current licensing guide).

---

## Are Projects in scope?

**Where:** Projects Setup, Job/Project cards
**What it controls:** Whether time/cost/revenue is tracked and invoiced per project.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| No projects — dimensions only | Client just wants P&L per internal initiative | Real project billing or WIP needed |
| Projects for cost collection, invoice from sales docs | Light needs, invoicing stays in normal flow | True fixed-price/WIP accounting |
| Full Projects incl. WIP methods & project invoicing | Project-driven businesses (installers, engineering) | Trade/production clients — overkill |

**Required client info:**
- Does the client bill time & materials or fixed-price work?
- Are auditors expecting WIP on the balance sheet, and by which method?

**Interactions:** WIP methods post to G/L — coordinate posting groups with [finance](finance.md).
**Add-on impact:** None known for Aptean F&B.
**Default recommendation:** Dimensions-only unless project billing/WIP is explicitly required.
**Risk of getting it wrong:** medium — WIP method changes mid-project are painful.
**Expertise tags:** `#projects` `#wip`

---

## Is Service Management in scope?

**Where:** Service Mgt. Setup
**What it controls:** Service items, service orders, contracts, resource dispatching.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Not used | No after-sales service obligations | — |
| Service orders only | Occasional repairs, warranty handling | Heavy contract/SLA business |
| Full: contracts + SLAs + dispatch | Service is a core revenue stream | Small teams — admin burden exceeds value; consider ISV field-service apps instead |

**Required client info:**
- Volume of service calls/repairs per week; contract/SLA commitments?
- Field technicians needing mobile access? (standard BC is weak here — ISV territory)

**Interactions:** Service items can link to sold items ([sales](sales.md)); loaners and spare parts hit [inventory](inventory.md).
**Add-on impact:** None known for Aptean F&B.
**Default recommendation:** Out of scope unless service is a revenue stream; revisit with an ISV comparison if mobile field service is needed.
**Risk of getting it wrong:** low — can be introduced later without disturbing existing setup.
**Expertise tags:** `#service`
