# General Setup & Cross-Cutting Foundations — Odoo (Standard)

> **Scope:** Odoo 19 Enterprise (Odoo Online, Odoo.sh or on-premise); Community edition differences flagged inline
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when Odoo releases functional changes to this area (one major release per year, typically October).

This file covers the decisions that sit under every functional area of an Odoo implementation: edition and hosting, company structure, app scope, customization policy, numbering, analytic architecture, users and access, approvals, document output, data migration, integration posture and audit/retention. Odoo's marketing says "install the app and go" — the consultant's job is the opposite: several of these choices (edition/hosting, the fiscal localization chosen at database creation, multi-company structure, analytic plans) quietly constrain everything else for the lifetime of the database. Treat edition/hosting and the analytic plan design as the flagship conversations with management, not as checkbox setup.

---

## Edition & hosting (Enterprise vs Community; Online vs Odoo.sh vs on-premise)

**Where:** Commercial/contract decision before any configuration; database creation on odoo.com (Online), project creation on odoo.sh, or own infrastructure. Not reversible from a settings page.
**What it controls:** Which apps exist at all, whether custom Python code is possible, who runs upgrades, and the per-user subscription cost. Capability line to memorize: **Community has Invoicing but not full Accounting** — no localized financial reports, no bank sync, no Belgian VAT return; for a Belgian SME that alone usually decides Enterprise.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Enterprise on Odoo Online (SaaS) | The default for SMEs with standard-ish processes; Odoo hosts, backs up and upgrades on its own schedule (with a test window); Studio available for light tailoring | Any need for custom Python or OCA modules — Online runs **no custom code**; Studio, imports and API only |
| Enterprise on Odoo.sh (PaaS) | Custom or OCA modules needed but no infrastructure team; git-based deployment with staging branches; you plan your own upgrades (only the last three versions are supported) | Pure-standard clients — platform cost and upgrade responsibility for flexibility you don't use |
| Enterprise on-premise | Hard data-residency demands, existing infra team, heavy integration landscape | SMEs without ops capability — self-managed upgrades and backups become the partner's unpaid job |
| Community on-premise (free, LGPL) | Budget-driven micro clients with dev capability; core sales/purchase/inventory/invoicing works | Anyone needing full Accounting, Studio, Barcode, Quality, PLM, MPS, Helpdesk, Approvals, Sign, Payroll — all Enterprise-only |

Licensing is per internal user; on Odoo Online, Studio, multi-company and the external API require the higher plan tier. > ⚠️ Verify current plan names and inclusions against Odoo pricing.

**Community edition:** the whole left column of this decision — and Odoo Online is not an option, it runs Enterprise exclusively.

**Required client info:**
- Budget reality: per-user Enterprise subscription acceptable? Headcount now and in 3 years?
- Any process standard Odoo demonstrably doesn't cover (drives custom code → Odoo.sh/on-premise)?
- Data-residency/IT-policy constraints on SaaS — and who owns upgrades and backups if not Odoo?

**Interactions:** Constrains [customization policy](#customization-policy-studio-vs-custom-modules-vs-standard), [company structure](#company-structure-one-company-vs-multi-company) and [integration posture](#integration-posture-apis-webhooks-e-invoicing) (plan-gated on Online). The fiscal localization is chosen at database creation — [finance — Belgian localization](finance.md#fiscal-localization-package-belgian-l10n_be).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base. On-premise/Odoo.sh clients often run OCA community modules; treat any found at intake as an add-on to document.

**Default recommendation:** Enterprise on Odoo Online for a standard Belgian SME; Odoo.sh only when a concrete, named requirement forces custom code — never "for flexibility."

**Risk of getting it wrong:** high-irreversible in practice — changing edition/hosting later is a migration project; discovering mid-project that a needed app is Enterprise-only reopens the whole architecture.

**Expertise tags:** `#general-setup` `#odoo-hosting` `#licensing` `#flagship-decision`

---

## Company structure: one company vs multi-company

**Where:** **Settings → Users & Companies → Companies**; inter-company transaction options in Settings; per-company fiscal localization.
**What it controls:** Odoo is multi-company in **one database**: each company has its own chart of accounts, journals, sequences and localization, while contacts and products can be shared or restricted per company. Rule of thumb: **legal entity = company in one shared database; everything softer = analytic plans.**

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| One company, [analytic plans](#analytic-accounting-architecture-plans--distributions) for branches/BUs | One legal entity; reporting needs are analytical, not statutory | Multiple legal entities with separate statutory filings |
| Multi-company in one database | A Belgian group (holding + opcos): shared contacts/products where wanted, inter-company rules auto-generating the counterpart document, per-company CoA and VAT — different countries coexist in one database | Entities that must never see each other's data — record-rule discipline gets heavy; an unnecessary company multiplies every setup object |
| Separate databases per entity | Hard isolation; sale of an entity anticipated | Groups trading internally daily — you lose inter-company automation and shared master data |

**Community edition:** multi-company works; inter-company automation and consolidated-reporting comfort are weaker — verify the specific flows needed.

**Required client info:**
- How many legal entities, which countries, acquisitions planned? Consolidation requirement and tool ([finance](finance.md))?
- Do entities trade with each other, and how often? Shared customers/suppliers/products, or strictly separate?
- On Odoo Online: does the plan tier include multi-company?

**Interactions:** Per-company CoA and VAT: [finance — localization](finance.md#fiscal-localization-package-belgian-l10n_be), [chart of accounts](finance.md#chart-of-accounts-design-belgian-mar). Sequences are per company ([document numbering](#document-numbering-sequences)); user access per company: [users & record rules](#users-access-rights--record-rules); warehouses are per company ([warehouse design](warehouse.md#warehouse--location-design)).

**Add-on impact:** None known yet — OCA has inter-company modules for Odoo.sh/on-premise; document at intake if found.

**Default recommendation:** One database; one Odoo company per legal entity; branches and divisions as analytic plans, not companies.

**Risk of getting it wrong:** high-irreversible — merging or splitting databases later is a migration project.

**Expertise tags:** `#general-setup` `#company-structure` `#multi-company` `#intercompany`

---

## Apps & module scope discipline

**Where:** **Apps** menu; each app's Settings section once installed.
**What it controls:** Which functional modules run. Installing an app is one click but a real implementation decision: it adds menus, fields, automatic postings and dependencies, and changes behaviour of existing flows. On the entry-level one-app Online plan, a second app also moves the client to paid per-user pricing.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Minimal app set matching the signed scope | Always — install only what the project implements; add later deliberately | — |
| "Install everything, we'll see" | Never — on Online the marginal app feels "free," which invites scope creep by enthusiastic users with admin rights | **Uninstalling an app deletes its data** — experiments in production are destructive |
| Staging database for app trials | Always have one (trial DB, Odoo.sh staging branch, or a copy) | — |

**Required client info:**
- Which processes are in scope for phase 1 (signed statement of work)?
- Who has admin rights and installs apps after go-live? Is there a staging database, and who refreshes it?

**Interactions:** App choices activate the functional areas in [finance](finance.md), [inventory](inventory.md), [manufacturing](manufacturing.md), [sales](sales.md), [purchasing](purchasing.md), [projects-service](projects-service.md); installation rights belong in [access rights](#users-access-rights--record-rules); Enterprise-only apps: [edition & hosting](#edition--hosting-enterprise-vs-community-online-vs-odoosh-vs-on-premise).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Install exactly the scoped apps in production; every trial happens in staging; installation rights restricted to one named admin.

**Risk of getting it wrong:** medium — uninstalling deletes data and can break linked flows; treat installs as one-way doors in production.

**Expertise tags:** `#general-setup` `#module-scope` `#governance`

---

## Customization policy (Studio vs custom modules vs standard)

**Where:** **Studio** (Enterprise); custom addons via Odoo.sh git repository or on-premise addons path; OCA modules from github.com/OCA (Odoo.sh/on-premise only).
**What it controls:** How gaps between standard Odoo and client wishes get closed — and who pays for it at every yearly upgrade, forever. Rule of thumb: every customization must name the business case that beats "adapt to standard," and the client must hear "you will pay to re-test or migrate this at every yearly upgrade" before signing.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Standard first: change the process, not the software | The doctrine — Odoo's standard flows are opinionated and coherent; most "requirements" are habits from the legacy system | Genuine legal or competitive-differentiator gaps |
| Studio (fields, views, simple automations, reports) | Light no-code tailoring on any hosting incl. Online | Complex logic — Studio automations become an unauditable tangle, and every change adds upgrade-test surface |
| Custom Python modules | Real functional gaps, clean dev practices, Odoo.sh/on-premise only | Odoo Online (impossible); clients without a maintenance budget — every module is migrated at each yearly upgrade |
| OCA community modules | On Odoo.sh/on-premise, mature peer-reviewed modules often cover the gap (logistics, accounting, EDI) | Treating OCA as free-forever — someone ports/verifies each module per version, and coverage lags new releases |

**Community edition:** no Studio; custom and OCA modules are the only tailoring path.

**Required client info:**
- Which requirements are legal/contractual vs "the old system did it this way"?
- Who maintains customizations after go-live (partner contract, internal dev, nobody)? Recurring upgrade budget accepted?

**Interactions:** Bounded by [edition & hosting](#edition--hosting-enterprise-vs-community-online-vs-odoosh-vs-on-premise); Studio surfaces in [approval workflows](#approval-workflows) and [document layouts](#document-layouts--report-templates); custom fields complicate [data migration](#data-migration-approach-imports--opening-balances) and upgrades.

**Add-on impact:** None known yet. OCA modules found at intake should each be documented as an add-on overlay.

**Default recommendation:** Standard first; Studio for light gaps with a documented inventory of every change; custom modules only for named, signed business cases with a maintenance agreement.

**Risk of getting it wrong:** medium — customizations are removable, but a database of undocumented Studio tweaks and orphaned modules turns every upgrade into archaeology.

**Expertise tags:** `#general-setup` `#studio` `#customization` `#upgrades`

---

## Document numbering (sequences)

**Where:** Journal entry/invoice numbers: derived per journal from the sequence pattern of the last posted entry (editable on the entry; Odoo detects prefix/year/reset from it). Other documents (SO, PO, transfers…): **Settings → Technical → Sequences** (developer mode).
**What it controls:** The number every document carries and the per-journal fiscal sequences for invoices. Belgian reality: sales invoice numbers must be sequential and gapless per series; Odoo assigns the number at posting, so the discipline is procedural — post in date order, never delete posted invoices (credit-note them), lock closed periods ([finance — lock dates](finance.md#period-close--lock-dates)). Drafts carry no fiscal number, which is exactly right.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Per-journal invoice sequences, year prefix, yearly reset (e.g. `INV/2026/00001`) | The Odoo norm and the right answer for Belgian sales invoices — one uninterrupted, chronological sequence per journal per year | — |
| Editing the first entry's number to set the pattern | Standard mechanism to set the format or continue legacy numbering at cutover | Casual renumbering later — mid-year pattern changes break continuity |
| Multiple sales journals (shops, channels), each its own sequence | Legitimate — Belgian rules allow several series if each is internally gapless and identifiable | Multiplying journals for cosmetics; every journal is VAT-return surface ([finance — journals](finance.md#journal-design--sequences)) |

**Required client info:**
- Legacy numbering to continue at cutover, or a clean break at fiscal-year start?
- How many invoice series does the business genuinely need (channels, sites)? Do users expect to read year/site/type in operational numbers?

**Interactions:** Sequences live per journal — design together ([finance — journal design](finance.md#journal-design--sequences)); per company ([company structure](#company-structure-one-company-vs-multi-company)); cutover numbering is a [data migration](#data-migration-approach-imports--opening-balances) task; posted-entry protection: [audit trail](#audit-trail-logging--data-retention).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** One sales journal per real series with `PREFIX/YYYY/` pattern and yearly reset, set via the first posted entry at cutover; operational sequences left standard unless users articulate a need.

**Risk of getting it wrong:** medium — patterns are adjustable, but a gap or duplicate in a posted Belgian invoice sequence is an auditor finding you cannot repair retroactively.

**Expertise tags:** `#general-setup` `#number-series` `#compliance`

---

## Analytic accounting architecture (plans & distributions)

**Where:** **Accounting → Configuration → Analytic Plans** and **Analytic Accounts** (analytic accounting enabled in Accounting settings); applicability rules per plan; **Analytic Distribution Models** for automatic coding.
**What it controls:** Odoo's answer to Business Central dimensions and the entire management-reporting model: analytic plans are the axes (department, project, branch…), analytic accounts the values, and the analytic distribution on document lines splits amounts across them in percentages (multiple parallel plans since v16). Unlike BC's two global dimensions stamped on every ledger entry, analytics live on the line's distribution, mainly on P&L-relevant flows — design what must be covered (typically all P&L) and enforce exactly that. Flagship analytics decision of the implementation.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| 1–3 plans mirroring actual management reports (e.g. BRANCH + PROJECT) | Always — every plan must have a named report consumer | A plan nobody can tie to a decision; delete it from the design |
| Applicability = **mandatory** per plan per document domain (invoices, bills, expenses…) | The disciplined model where the axis matters — enforced at posting, clean data | Enforcing on flows where users legitimately can't know the value |
| Applicability = optional everywhere | Feels flexible; produces Swiss-cheese data nobody can report on | Almost always wrong for the core plans |
| Analytic distribution models (auto-fill by partner, product, account…), incl. percentage splits | Always — defaults do the coding so users don't; the analytic equivalent of BC default dimensions | Splitting everything 60/40 "to be fair" — reporting becomes unreadable |
| Projects app auto-creating analytic accounts | Project-driven businesses — profitability per project out of the box ([projects-service](projects-service.md)) | — |

**Community edition:** analytic accounting exists but plan/applicability depth is tied to the full Accounting app. > ⚠️ Verify against current Odoo documentation.

**Required client info:**
- Show me the management reports you run the business on — which breakdowns recur? (those are your plans)
- Which axes must be enforced vs nice-to-have, and on which documents? Monthly P&L per branch required?
- Who maintains analytic accounts (new projects, new departments)?

**Interactions:** Substitutes for [multi-company splits](#company-structure-one-company-vs-multi-company) for non-legal segmentation; keeps the [chart of accounts](finance.md#chart-of-accounts-design-belgian-mar) lean; project profitability feeds [projects-service](projects-service.md); analytic accounts must exist before [data migration](#data-migration-approach-imports--opening-balances) imports reference them.

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** 1–3 plans taken from actual management reports, mandatory applicability on P&L document flows for the core plan, distribution models on every recurring vendor/product so correct coding is the path of least resistance.

**Risk of getting it wrong:** high-irreversible in effect — plans are editable, but historical entries missing an axis can't be re-told; you get one clean shot at the analytical story.

**Expertise tags:** `#general-setup` `#analytics` `#dimensions` `#reporting` `#flagship-decision`

---

## Users, access rights & record rules

**Where:** **Settings → Users & Companies → Users**; per-app role groups on the user form (e.g. Sales: User / Administrator); groups and record rules (developer mode); multi-company allowed/active companies per user; portal access via "Grant portal access" on contacts.
**What it controls:** Who sees and does what: groups per app role (menu/action access) plus record rules (row-level filters — own documents only, company isolation). Internal users consume licenses; portal users (customers/vendors seeing their own documents) are free. Settle early who may enter developer mode in production — it exposes technical menus that can break the database.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Standard per-app role groups | The 90% case — lowest role that does the job; app "Administrator" is a functional admin, not IT | Handing app-admin or Settings access broadly "to avoid friction" |
| Settings (general admin) for one named admin + partner | Always | Everyone-is-admin databases — the classic Odoo SME disease; combined with one-click installs it dissolves scope control |
| Portal users for customers/vendors | Document self-service at zero license cost | — |
| Custom groups/record rules | Real row-level needs (salesperson sees own customers) | Early-phase custom security matrices — they rot as apps get added; record rules are near-development work |
| Multi-company access per user | Group staff working across entities; the active-company switch controls where documents land | Granting all companies to everyone — mis-company'd documents are a recurring mess |

**Required client info:**
- Role inventory including holiday cover — who does what? Segregation-of-duties demands from the accountant/auditor?
- Who is the one named admin after go-live? Which external parties can be portal instead of licensed users?

**Interactions:** App-install rights enforce [module scope discipline](#apps--module-scope-discipline); approval rights complement [approval workflows](#approval-workflows); company access depends on [company structure](#company-structure-one-company-vs-multi-company); accounting roles tie to [finance controls](finance.md#period-close--lock-dates).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Lowest sufficient per-app role per user, one named Settings admin plus the partner, portal users for every external party — and licenses counted before promising a budget.

**Risk of getting it wrong:** medium — rights are adjustable, but an everyone-is-admin go-live produces installed-app surprises and data messes that are expensive to unwind.

**Expertise tags:** `#general-setup` `#users` `#permissions` `#governance` `#licensing`

---

## Approval workflows

**Where:** Purchase: **Purchase → Configuration → Settings → Purchase Order Approval** (minimum amount, manager validation); **Approvals** app (Enterprise) for generic request types; Studio approval rules on buttons/status changes (Enterprise).
**What it controls:** Which documents need a second pair of eyes, at what thresholds, and whether the approval lives inside the document flow or in a separate layer — the same native-vs-extra-engine framing as BC's native-vs-Power-Automate question.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Purchase order approval above a minimum amount | The core financial control for most SMEs — one threshold, one level in standard | Multi-level amount ladders (€1k team lead, €10k CFO) — needs Studio approval rules or custom |
| Approvals app (Enterprise) | Non-document requests: purchase *requests* before a PO exists, HR-ish approvals; configurable types/approvers | Shadowing real documents — a parallel approval object detached from the PO invites drift |
| Studio approval rules | Multi-level or conditional approval on any model's action (Enterprise) | Deep conditional routing — unauditable; consider whether the org, not the tool, is the problem |
| No workflows, access rights only | Micro teams where the owner confirms everything anyway | Any real SoD requirement — "we trust each other" ends at the first fraud audit |

**Community edition:** purchase minimum-amount validation exists; the Approvals app and Studio rules do not — multi-level approval means custom/OCA modules.

**Required client info:**
- Which documents genuinely need approval, thresholds, and delegation rules (vacations!)? One level enough, or is a multi-level ladder non-negotiable?
- Volume: approvals per week? (Ten POs/week doesn't justify an approval architecture)

**Interactions:** Detailed purchase-side setup: [purchasing — approvals & order validation](purchasing.md#purchase-approvals--order-validation). Approval limits complement, not replace, [access rights](#users-access-rights--record-rules); Studio rules fall under the [customization policy](#customization-policy-studio-vs-custom-modules-vs-standard).

**Add-on impact:** None known yet — OCA has multi-level purchase approval modules for Odoo.sh/on-premise; document as an add-on if found at intake.

**Default recommendation:** Standard PO minimum-amount validation as the day-one control; Approvals app only for genuinely document-less requests; Studio rules only when a multi-level ladder is a hard requirement.

**Risk of getting it wrong:** low — all changeable; the classic failure is operational (documents stuck at an absent approver), not structural.

**Expertise tags:** `#general-setup` `#workflows` `#approvals`

---

## Document layouts & report templates

**Where:** **Settings → General Settings → Companies → Configure Document Layout** (logo, layout template, colors, fonts, footer); QWeb report templates (developer work, or Studio's report editor — the only report-editing path on Odoo Online); per-contact language on the partner form.
**What it controls:** What every outbound PDF (quote, order confirmation, invoice, delivery slip) looks like and in which language it renders per customer. Belgian footer to hard-check: legal name and form, registered office, enterprise number/VAT (BE 0xxx.xxx.xxx), RPR/RPM with competent court, IBAN/BIC — most flows from the company record, so complete the company form before judging the layout.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Document layout wizard only (logo + template + colors + footer) | Budget-conscious go-lives — documents are presentable and legally fine out of the box | Brand-sensitive clients — expect a change request within a month; budget layout work up front instead |
| Studio report editor (Enterprise) | Moderate layout changes by a power user; the only option on Online | Heavy restructuring — Studio-edited reports add upgrade-test surface |
| QWeb template development | Full control on Odoo.sh/on-premise | Standard-hosting clients; every custom template is code per the [customization policy](#customization-policy-studio-vs-custom-modules-vs-standard) |
| Per-language documents via partner language | Belgian default — NL/FR (often EN); Odoo renders in the partner's language once translations are loaded | Skipping the translation check until the first French customer complains |

**Community edition:** no Studio — layout wizard or QWeb development only.

**Required client info:**
- Which documents leave the building, and who signs off their appearance (get the name early)? Customer languages — NL/FR/EN split?
- Company legal details complete and verified (enterprise number, RPR/RPM court, IBAN)?

**Interactions:** Quote templates and online sign/pay shape what the customer sees before the PDF ([sales — quotation flow](sales.md#quotation-flow-templates-online-sign--pay)); Peppol makes the XML, not the PDF, the legal artifact for B2B invoices ([finance — e-invoicing](finance.md#e-invoicing--peppol)).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Layout wizard + complete company legal data at go-live, translations loaded for NL/FR, a budgeted layout-polish pass in week 2–4, QWeb only for named branding requirements.

**Risk of getting it wrong:** low — everything is changeable; the risk is reputational, except that a wrong VAT number or missing RPR on invoices is also a compliance defect — check once, properly.

**Expertise tags:** `#general-setup` `#document-layouts` `#output` `#multi-language`

---

## Data migration approach (imports & opening balances)

**Where:** Import button on any list view (CSV/XLSX, downloadable templates, field mapping, **external IDs** for idempotent re-imports and record relations); opening balance journal entry in Accounting; open AR/AP as individual invoices/bills; opening stock via inventory adjustment (with lots/serials where tracked).
**What it controls:** How master data and opening balances enter Odoo, how much history comes along, and whether go-live reconciles to the legacy trial balance. Sequencing discipline: localization + settings first, master data second, open documents third, balances last — against a cutover checklist with signed reconciliation (trial balance, AR/AP aging, stock value).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| CSV/XLSX imports with external IDs for all master data | The standard: contacts, products, pricelists, BoMs from templates; external IDs make re-runs update instead of duplicate — non-negotiable practice | Hand-keying anything above ~50 records |
| Opening balance journal entry per G/L account; open AR/AP as individual invoices/bills (legacy number, dates) | The standard, auditable pattern — aging, reminders and payment matching work from day one; ledger against the Belgian MAR chart ([finance — CoA](finance.md#chart-of-accounts-design-belgian-mar)) | Lump-sum AR/AP balances — collections is blind; only for genuinely tiny ledgers |
| Open orders re-created as documents; no transactional history in Odoo | The doctrine — open SOs/POs must be workable documents; legacy stays read-only (or a BI copy) for history | Migrating posted history — almost never justified; cost and posting-logic distortion are huge |
| Opening stock via inventory adjustment with costs and lots | Standard; opening cost quality is forever — it feeds AVCO/FIFO layers from entry one ([inventory — costing](inventory.md#product-categories--costing-method-standard--avco--fifo)); tracked items need lot detail ([inventory — tracking](inventory.md#tracking-lots-serials--expiry)) | Importing stock before product categories/costing are final |

**Required client info:**
- Source system(s) and extract quality — who owns data cleansing (client, always — in writing)?
- Cutover window: big-bang weekend or parallel run? Open orders/invoices at go-live (order of magnitude)?
- Comparative-history expectations — can BI absorb them instead? Lot/serial-tracked stock to migrate?

**Interactions:** Opening entries respect [lock dates](finance.md#period-close--lock-dates) and [journal design](finance.md#journal-design--sequences); cutover numbering: [document numbering](#document-numbering-sequences); analytic accounts and [Studio fields](#customization-policy-studio-vs-custom-modules-vs-standard) must exist before mapped imports.

**Add-on impact:** None known yet — install any OCA/add-on modules *before* master-data migration, or you migrate twice.

**Default recommendation:** Template-based imports with external IDs, per-invoice AR/AP, opening stock with real costs and lots, open orders as documents, no history in Odoo, signed reconciliation as the go-live gate.

**Risk of getting it wrong:** high-irreversible in effect — almost anything is technically correctable, but unreconciled balances or wrong opening costs contaminate the ledgers from entry one, and the cleanup happens live, under fire.

**Expertise tags:** `#general-setup` `#data-migration` `#cutover` `#imports`

---

## Integration posture (APIs, webhooks, e-invoicing)

**Where:** External API via XML-RPC/JSON-RPC with API keys (user preferences → account security); automation rules incl. webhook triggers (**Settings → Technical → Automation Rules**); native connectors per app (shipping, payment, e-commerce, bank synchronization); Peppol e-invoicing in Accounting settings.
**What it controls:** How Odoo talks to the outside world and which platform bets the client makes. Brief here; each concrete integration is its own project.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| External API (XML-RPC/JSON-RPC) | Any bespoke or middleware/iPaaS integration — full model access, stable across versions | On Odoo Online, API access is plan-gated — confirm the plan before architecting. > ⚠️ Verify against current Odoo pricing/documentation. |
| Automation rules + webhooks | Lightweight event-driven notifications and outbound calls without custom modules | High-volume transactional sync — automation rules are not middleware |
| Native connectors (shipping, payment, e-commerce, bank sync/CODA) | Prefer over custom builds wherever they exist; Belgian bank flows: [finance — CODA/SEPA](finance.md#banking-coda-sepa--reconciliation) | Feature gaps forcing workarounds worse than a clean custom integration |
| Peppol e-invoicing (built-in access point) | Belgian B2B e-invoicing via Peppol is **mandatory since 2026-01** — day-one setup for every Belgian client, not phase 2; details in [finance — e-invoicing](finance.md#e-invoicing--peppol) | — |

**Community edition:** external API and automation rules exist; several polished connectors (bank sync among them) are Enterprise services — inventory the needed connectors explicitly.

**Required client info:**
- System inventory that must talk to Odoo (webshop, WMS, payroll, banks, EDI partners) with direction and volume per flow
- Who owns integrations after go-live (internal dev, partner, nobody — "nobody" pushes toward native connectors)?
- Peppol registration status, and the accountant's role in it?

**Interactions:** Gated by [edition & hosting](#edition--hosting-enterprise-vs-community-online-vs-odoosh-vs-on-premise); Peppol interlocks with [VAT setup](finance.md#taxes-vat-return--fiscal-positions-belgian-vat) and [document layouts](#document-layouts--report-templates); barcode/WMS hardware: [warehouse — barcode operations](warehouse.md#barcode-operations).

**Add-on impact:** None known yet — OCA's EDI/connector ecosystem is a common reason clients sit on Odoo.sh/on-premise; document at intake.

**Default recommendation:** Native connectors first, external API for anything transactional and bespoke, automation-rule webhooks only for light eventing — and Peppol activated at go-live for every Belgian client, no exceptions.

**Risk of getting it wrong:** medium — integrations are replaceable, but a plan-gated API discovered after architecture, or a missed Peppol mandate, hurts immediately.

**Expertise tags:** `#general-setup` `#integration` `#api` `#peppol` `#e-invoicing`

---

## Audit trail, logging & data retention

**Where:** Chatter on every record (messages, field-change tracking on tracked fields); **Audit Trail** option in Accounting settings for journal-entry change logging (> ⚠️ Verify exact feature name and scope against current Odoo documentation.); server logs on Odoo.sh/on-premise; GDPR contact deletion/anonymization; database storage quota on Odoo Online.
**What it controls:** Who-changed-what traceability, protection of posted accounting data, and how database size and personal data are managed. Retention is a legal question before a technical one; on Odoo.sh/on-premise, logging and backup retention are the partner's explicit responsibility — write it into the support contract.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Chatter + tracked fields as the baseline | Free and always on for key fields; add tracking to sensitive master data (bank accounts, prices, credit limits) via Studio/dev | Assuming chatter equals a fiscal audit trail — it's a communication log first |
| Accounting audit trail enabled | Belgian clients: enable — modification history on posted entries is what the auditor asks for | — |
| Attachment/document housekeeping | Odoo Online storage quotas cost real money once exceeded — scans and EDI attachments accumulate | Deleting anything under Belgian retention duties (books and supporting docs: 7–10 years) |
| GDPR deletion/anonymization of contacts | Data-subject requests on prospects/portal users | Contacts on posted invoices — fiscal retention beats erasure; anonymize the marketing layer, keep the books |

**Community edition:** chatter/tracking identical; treat the accounting audit-trail feature as Enterprise until confirmed.

**Required client info:**
- Statutory retention duties (Belgian books/invoices) mapped against any cleanup wishes? Which master-data changes must be traceable, and for how long?
- Current/projected storage vs the Online quota, and who watches it? Any GDPR request process today?

**Interactions:** Posted-entry protection interlocks with [lock dates](finance.md#period-close--lock-dates) and [document numbering](#document-numbering-sequences); who can change tracked setup ties to [access rights](#users-access-rights--record-rules).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Accounting audit trail on, field tracking added to sensitive master data, a yearly storage review on Online, and GDPR erasure implemented as anonymization that never touches posted fiscal documents.

**Risk of getting it wrong:** low — mostly adjustable; the exceptions are deleting data under legal retention (compliance incident) and discovering after a dispute that a sensitive field was never tracked.

**Expertise tags:** `#general-setup` `#retention` `#audit` `#gdpr` `#compliance`
