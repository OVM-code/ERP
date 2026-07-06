# General Setup & Cross-Cutting Foundations — Microsoft Dynamics 365 Business Central (Standard)

> **Scope:** Microsoft Dynamics 365 Business Central (SaaS, current version)
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when the vendor releases functional changes to this area.

This file covers the decisions that sit under every functional area: company structure, numbering, dimensions, users and permissions, approvals, document output, data migration, integration posture and data retention. Most of these are decided once in week one of an implementation and then quietly constrain everything else for a decade. Two of them — the multi-company split and the two global dimensions — are effectively irreversible in practice; treat those as the flagship conversations with the client's management, not as checkbox setup.

---

## Company structure: one company vs many

**Where:** **Companies** page (environment level); **Company Information** page per company; environment/tenant strategy in the Business Central admin center; intercompany setup if splitting.
**What it controls:** The hardest boundary in BC: a company is a separate set of ledgers, master data, number series, setup and posted history. Nothing posts across companies without intercompany functionality or integration.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| One company, [dimensions](#dimensions-architecture-global-vs-shortcut) for business units/branches | One legal entity; management reporting needs are analytical (by department, branch, product line) not statutory | Multiple legal entities with separate statutory filings — dimensions cannot produce a legal entity's books |
| One company, multiple [locations](warehouse.md#location-design) | Multiple warehouses/sites within one legal entity | Sites are separate legal entities |
| Multiple companies in one environment | Multiple legal entities, same country/localization; shared admin, per-company books; intercompany postings for cross-charges | Entities in different countries needing different localizations — those need separate environments (localization apps are per environment) |
| Multiple environments | Different country localizations, hard data-isolation or performance/update-cadence needs | Adds admin and integration overhead; don't split environments for org-chart vanity |

Rule of thumb: **legal entity = company; everything softer = dimensions or locations.** Splitting one operating business into several BC companies "for clarity" creates permanent pain: duplicated master data, intercompany friction on every internal transaction, consolidated reporting projects.

**Required client info:**
- How many legal entities exist today, and are acquisitions/spin-offs planned in 3 years?
- Which countries/localizations must be supported?
- Do entities trade with each other? How often? (intercompany volume)
- Is consolidated reporting required, and in which tool ([finance — consolidation](finance.md))?
- Shared master data expectations: same items/customers across entities?

**Interactions:** Constrains [dimensions architecture](#dimensions-architecture-global-vs-shortcut) (dimensions handle what companies shouldn't), [number series](#number-series-design) (per company), master data sync and every integration ([integration posture](#integration-posture-apis-power-platform-e-invoicing)). Consolidation and intercompany: [finance.md](finance.md).

**Add-on impact:** Aptean Food & Beverage ERP is licensed and installed at environment level and configured per company — a multi-company food group repeats add-on setup per company. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** One company per legal entity, not one more; branches, sites and divisions as dimensions and locations inside it.

**Risk of getting it wrong:** high-irreversible — merging companies later means a re-implementation with data migration; an unnecessary split taxes every transaction and report for the system's lifetime.

**Expertise tags:** `#general-setup` `#company-structure` `#multi-company` `#intercompany`

---

## Number series design

**Where:** **No. Series** page (+ No. Series Lines with starting dates); assigned in each area's setup page (Sales & Receivables Setup, Purchases & Payables Setup, Inventory Setup, [Manufacturing Setup](manufacturing.md#manufacturing-setup--key-toggles), etc.) and on master-data setup; per-series toggles: **Default Nos.**, **Manual Nos.**, **Date Order**, **Allow Gaps in Nos.**
**What it controls:** Numbering of every master record and document; audit continuity of posted document numbers; performance (gaps toggle) and users' ability to type their own numbers.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| One series per document type, meaningful prefixes (SO-, PI-, FA-) | Always — the baseline; keeps posted vs unposted distinguishable and audits simple | — |
| **Allow Gaps in Nos.** = on | Non-posted/internal records where sequence continuity is legally irrelevant (quotes, master data) — faster, no locking | Posted sales invoices/credit memos in jurisdictions requiring gapless fiscal numbering — check the localization before enabling |
| **Manual Nos.** = on | Master data where users bring external codes (item numbers from a legacy catalogue) | Documents — hand-typed document numbers destroy consistency; leave off |
| **Default Nos.** = on with automatic assignment | Standard everywhere | — |
| Yearly series lines (new starting no. per Jan 1 via Starting Date) | Clients who read the year in the number (INV-2026-…); restarts happen automatically | Meaningless ritual if nobody uses the year; more setup rows to maintain |
| Separate posted-document series vs same-as-unposted | Separate series for posted invoices/shipments is the BC norm and keeps the fiscal sequence clean | Reusing one series across unposted and posted blurs the audit trail |

**Required client info:**
- Statutory numbering rules in the client's country (gapless invoice numbers? prefixes per branch?)
- Do users expect to recognize year/type/branch from the number?
- Legacy numbers to preserve on master data (items, customers)?
- Expected yearly volumes (size the number ranges — running out mid-year is an embarrassing incident)

**Interactions:** Every functional area's setup page references series. Branch-specific series interact with [dimensions](#dimensions-architecture-global-vs-shortcut) and responsibility centers. E-invoicing mandates can constrain formats ([integration posture](#integration-posture-apis-power-platform-e-invoicing)). Posted-series design matters for [audit and financial reporting](finance.md#general-ledger-setup-key-choices).

**Add-on impact:** Aptean F&B adds its own document types (e.g., trade agreements, quality documents) each needing series — include them in the numbering concept from the start. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Per-document-type series with clear prefixes, separate posted series, Manual Nos. only on master data, Allow Gaps only on non-fiscal records, ranges sized for 10+ years.

**Risk of getting it wrong:** medium — series can be extended and relationships added, but renumbering posted documents is impossible, and a gapless-numbering compliance failure is an auditor finding.

**Expertise tags:** `#general-setup` `#number-series` `#compliance`

---

## Dimensions architecture (global vs shortcut)

**Where:** **Dimensions** page (+ Dimension Values); **General Ledger Setup → Dimensions FastTab** (Global Dimension 1–2, Shortcut Dimensions 3–8); **Default Dimensions** on master records (with **Value Posting**: Code Mandatory / Same Code / No Code); Dimension Combinations for blocking; **Change Global Dimensions** action (last resort).
**What it controls:** The company's entire analytical reporting model: which two dimensions are filterable everywhere (global), which six more appear as line columns (shortcuts), and how hard the system enforces coding at posting time. Flagship decision of the whole implementation.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Global 1–2 = the two dimensions used in *every* management conversation (classically DEPARTMENT + PROJECT, or BRANCH + PRODUCTLINE) | Always — globals are stored on every ledger entry and usable as filters on all reports, batch jobs, entries | Choosing a fashionable-but-marginal dimension as global; changing later requires the heavy **Change Global Dimensions** batch (table-locking, sequential or parallel mode, sign-out) — plan never to run it |
| Shortcut dimensions 3–8 for the rest (up to 8 total shortcuts incl. the two globals) | Everything analysts want on journal/document lines without opening the Dimensions page | Exceeding what users will actually code — every dimension is a data-entry tax on every line, forever |
| Few dimensions, mandatory (Value Posting = **Code Mandatory** on relevant accounts/records) | The disciplined model: 3–5 dimensions, enforced where they matter — clean data | — |
| Many dimensions, optional | Feels flexible; produces Swiss-cheese data nobody can report on. Almost always wrong | Almost always |
| **Same Code** value posting on master records | Records that belong to exactly one dimension value (a machine to one department) — locks it | Records legitimately posted across values |
| Default dimensions on customers/vendors/items/G/L accounts (+ Default Dimensions-Multiple for bulk) | Always — defaults do the coding so users don't | — |

Discipline rule: every dimension must have a named report consumer. If no one can say which decision the dimension feeds, delete it from the design. Combined dimension values are stored as dimension sets, so cardinality is cheap technically — the cost is human.

**Required client info:**
- Show me the management reports you run the business on — which columns/breakdowns appear repeatedly? (those are your globals)
- Which breakdowns must be enforced (cost accounting) vs nice-to-have?
- Who will maintain dimension values (new projects, new departments)?
- Is a P&L per branch/BU required monthly? (pushes that dimension to global + Code Mandatory)
- Any plans that would change the org model (would invalidate a global) within 5 years?

**Interactions:** Substitutes for [multi-company splits](#company-structure-one-company-vs-many) for non-legal segmentation. Chart-of-accounts design should shrink when dimensions do the analytics ([finance — chart of accounts](finance.md#chart-of-accounts-design)). Default dimensions on items/locations feed inventory and production postings ([inventory](inventory.md#costing-method-per-item), [manufacturing](manufacturing.md#capacityoutput-journals--shop-floor-registration)). Analysis views and financial reports consume dimensions ([finance — reporting](finance.md#chart-of-accounts-design)).

**Add-on impact:** None structural — Aptean F&B transactions carry dimensions like standard ones; ensure defaults are set on add-on master data too. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Two globals chosen from actual management reports; total dimension count 3–5; Code Mandatory on P&L accounts for the core dimensions; defaults on all master data so correct coding is the path of least resistance.

**Risk of getting it wrong:** high-irreversible — globals are technically changeable via a painful locking batch job, but historical entries' analytical story is rewritten or lost; in practice you get one shot at this.

**Expertise tags:** `#general-setup` `#dimensions` `#reporting` `#flagship-decision`

---

## User setup, permission sets & security-light governance

**Where:** **Users** page (licenses/Entra ID assignment usually IT-led via M365 admin), **Permission Sets** (+ composable/copied sets), **User Groups**/security groups, **User Setup** page (posting date ranges, register time, salesperson/purchaser codes), profiles (role centers) per user.
**What it controls:** Who can do what, which role center users land in, and lightweight functional guardrails like allowed posting date ranges per user.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Standard permission sets assigned per functional role (via security groups) | The 90% case — combine Microsoft's out-of-box sets per role (AP clerk, warehouse, controller) | Regulated clients demanding least-privilege proofs — expect a proper permissions project |
| Custom/composed permission sets | Standard sets are too broad for audit findings; build by inclusion/extension, not by recording from scratch | Early project phase — premature custom sets rot as features get added |
| SUPER for everyone "temporarily" | Never as an end state; acceptable during data migration week only, with a dated removal task | Any production go-live — it *will* persist if not scheduled away |
| **User Setup** posting-date ranges per user | Always: restrict Allow Posting From/To for non-finance users tighter than G/L Setup's company-wide range | — |
| Role centers/profiles per role | Always — landing page defines what users think BC "is"; assign consciously | — |

Consultant reality: licensing and Entra ID are usually IT-led; the consultant's accountable slice is *functional* — mapping people to roles, roles to permission sets and profiles, and setting User Setup guardrails. Don't silently absorb the whole security domain into the functional budget, but don't ship SUPER-for-all either.

**Required client info:**
- Role inventory: who does what, including holiday cover (drives set composition)?
- Segregation-of-duties requirements from auditors (payment runs vs vendor master edits)?
- Who administers users after go-live — internal IT or the partner?
- License types per user (Essentials/Premium/Team Member — Team Member is heavily restricted; verify each "light user" fits before promising cheap licenses)

**Interactions:** Approval thresholds complement permissions ([approval workflows](#approval-workflows-native-vs-power-automate)). Allowed posting dates interact with period close ([finance — period close](finance.md#general-ledger-setup-key-choices)). Warehouse role separation ties to [warehouse setup](warehouse.md#item-journal-vs-warehouse-journal-per-level).

**Add-on impact:** Aptean F&B ships its own permission sets — add them to role compositions or add-on pages error out for non-admins. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Security groups per functional role composed of standard permission sets, User Setup date guardrails for everyone, SUPER only for the sysadmin and the partner, role centers assigned deliberately.

**Risk of getting it wrong:** medium — permissions are always adjustable, but discovering a Team Member license can't do the user's job after go-live, or an auditor finding SUPER-for-all, are avoidable embarrassments.

**Expertise tags:** `#general-setup` `#users` `#permissions` `#governance` `#licensing`

---

## Approval workflows (native vs Power Automate)

**Where:** **Workflows** page (+ workflow templates), **Approval User Setup** (approvers, amount limits, substitutes), workflow notifications (email/notes); alternatively Power Automate flows surfaced through BC's built-in Power Automate integration.
**What it controls:** Which documents (purchase orders, sales documents, journals, master-data changes) require approval, by whom, at what thresholds, and where approvers experience the approval.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Native BC workflows + Approval User Setup | Classic in-BC approvals: amount-limit chains on purchase docs, journal approvals, customer/item change approval; approvers work inside BC; no extra platform dependency | Multi-stage conditional logic, approvals in Teams/Outlook, non-BC participants — native engine gets awkward fast |
| Power Automate approval flows | Approvers live in Teams/Outlook/mobile; conditions beyond templates; org already invested in Power Platform governance | No Power Platform governance/ownership at the client — flows become orphaned shadow IT owned by an ex-employee's account; licensing and connection ownership must be settled |
| No workflows, permissions only | Micro teams where the owner posts everything anyway | Any real SoD requirement — "we trust each other" ends at the first fraud audit |
| Hybrid: native for core financial docs, Power Automate for exotic/multi-app processes | Pragmatic mainstream choice for mid-size clients | Keep an inventory — two engines mean two places to debug "why is this stuck" |

**Required client info:**
- Which documents genuinely need approval, and what are the amount thresholds and delegation rules (vacations!)?
- Where do approvers live all day — BC, Outlook, Teams, phone?
- Does the client have Power Platform governance (environments, DLP, service accounts)?
- Volume: approvals per week? (Ten POs/week doesn't justify a flow architecture)

**Interactions:** Overlaps [permission sets](#user-setup-permission-sets--security-light-governance) — approval limits are not a substitute for posting restrictions. Purchase approval interacts with purchasing setup and [subcontract POs](manufacturing.md#subcontracting-setup). Power Automate choice belongs to the broader [integration posture](#integration-posture-apis-power-platform-e-invoicing). Journal approvals touch [finance controls](finance.md#general-ledger-setup-key-choices).

**Add-on impact:** Aptean F&B documents (e.g., quality dispositions, trade agreements) may have their own release/approval concepts — align so users don't face two competing approval metaphors on one document. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Native workflows with Approval User Setup amount limits for purchase documents and general journals; escalate to Power Automate only for Teams-based approvers or genuinely conditional routing — and only with named flow ownership.

**Risk of getting it wrong:** low — workflows are fully changeable; the classic failure is operational (documents stuck at an unset substitute during vacation), not structural.

**Expertise tags:** `#general-setup` `#workflows` `#approvals` `#power-automate`

---

## Report selections & document layouts

**Where:** **Report Selections** per document type (Report Selection – Sales, – Purchase, – Warehouse, etc.), **Custom Report Layouts** / Word and Excel layouts, **Document Layouts** per customer/vendor (per-document-type layout + email settings), email scenarios in **Email Accounts** setup.
**What it controls:** Which report object prints/emails for each document event (order confirmation, invoice, reminder), what it looks like, and per-counterparty overrides including email addresses per document type.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Standard layouts, logo and footer via Company Information | Budget-conscious go-lives; documents are legally fine out of the box | Brand-sensitive clients — expect a change request within a month; budget layout work up front instead |
| Word layouts customized per document | Marketing-grade invoices/confirmations maintainable by a power user | Complex conditional content — Word layouts get fragile; consider an RDLC/AL layout by a developer |
| Per-customer/vendor **Document Layouts** (incl. per-doc email addresses) | Key accounts demanding specific formats/languages; invoices to accounting@, order confirmations to purchasing@ | Maintaining dozens of per-customer variants without an owner |
| ISV output-management add-ons | High document volume, batch distribution, archiving requirements | Cost/complexity overkill for a standard SMB |

Quiet trap: report selections are per company and often forgotten after copying a company or adding a custom layout — the old object keeps printing. Also settle the *language* question (report captions per customer language code) during layout work, not after the first foreign invoice.

**Required client info:**
- Which documents leave the building, and who signs off their appearance (get the sign-off name early)?
- Multi-language documents needed? Which languages?
- Per-customer document email routing rules?
- Legal footer requirements (registration numbers, bank details — varies by country)

**Interactions:** Emailing depends on email account setup and [integration posture](#integration-posture-apis-power-platform-e-invoicing); e-invoicing (Peppol) replaces the *printed* invoice as the legal artifact for some customers — coordinate. Reminder/finance charge layouts tie to [receivables management](finance.md#payment-terms-payment-methods-reminders-and-finance-charges). Warehouse document selections tie to [warehouse flows](warehouse.md#item-journal-vs-warehouse-journal-per-level).

**Add-on impact:** Aptean F&B extends outbound documents with food-specific content (lot numbers, catch weights, certifications on delivery notes/invoices) via its own layouts — start from the add-on's layout set, not from vanilla BC layouts. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Standard layouts + logo for go-live with a budgeted layout-polish sprint in week 2–4; per-customer Document Layouts only for accounts that demand them; one named owner for layout changes post go-live.

**Risk of getting it wrong:** low — everything here is changeable at any time; the risk is reputational (ugly or wrong documents at customers) rather than structural.

**Expertise tags:** `#general-setup` `#report-selections` `#document-layouts` `#output`

---

## Data migration approach (config packages / opening balances)

**Where:** **Configuration Packages** (RapidStart) with per-table field selection and validation, **Configuration Worksheet**, Edit-in-Excel for corrections, opening balance journals (item journal, general journal, customer/vendor opening entries), data migration assisted setup (QuickBooks etc. where relevant).
**What it controls:** How master data and opening balances get into BC, how much history comes along, and how reconcilable go-live is.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Config packages for master data + journals for opening balances | The standard, auditable pattern: items/customers/vendors/BOMs via packages; open AR/AP as per-invoice opening entries; inventory via item journal (qty + cost per location/lot); G/L via opening balance journal per account | — |
| Open documents migrated as documents (open SOs/POs re-keyed or imported) | Operationally necessary — open orders must exist as workable documents, not balances | Trying to import them as posted history |
| Historical transactions migrated into BC | Almost never justified — cost and posting-logic distortion are huge | Default: keep legacy read-only (or a BI copy) for history; migrate balances + open items only |
| Per-invoice AR/AP opening entries vs one lump balance | Per-invoice is strongly preferred: application, aging and reminders work day one | Lump-sum only for genuinely tiny ledgers — collections is blind otherwise |
| Aged-history compromise: monthly G/L balances for 1–2 comparative years | Client insists on comparative reporting in BC financial reports | Full detail demanded — push back or route to BI |

Sequencing discipline: setup + posting groups first, master data second, open documents third, balances last, all against a cutover checklist with signed reconciliation (trial balance, AR/AP aging, inventory value) between legacy and BC on day one. Inventory opening cost must respect the chosen [costing method](inventory.md#costing-method-per-item) — garbage opening costs are forever in the cost history.

**Required client info:**
- Source system(s) and extract quality — who can produce clean CSVs, and who owns cleansing (client, always — get this agreed in writing)?
- Cutover window: big-bang weekend or parallel run?
- How many open orders/invoices at go-live (order of magnitude)?
- Comparative-history expectations, and can BI absorb them instead?
- Lot/serial-tracked inventory to migrate? (needs lot detail in the item journal — see [inventory tracking](inventory.md#item-tracking-lot--serial--package))

**Interactions:** Opening inventory cost interlocks with [costing method](inventory.md#costing-method-per-item) and [posting groups](finance.md#customer-and-vendor-posting-groups); production master data (BOMs/routings) migration ties to [manufacturing BOM design](manufacturing.md#production-bom--routing-design); dimension values must exist before defaults import ([dimensions](#dimensions-architecture-global-vs-shortcut)).

**Add-on impact:** Aptean F&B adds migration objects — lots with expiry/status, catch-weight quantities, recipes, vendor certifications — install and configure the add-on *before* master data migration, or you migrate twice. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Config packages for master data, per-invoice AR/AP opening entries, item journal with correct costs per location/lot, open orders as documents, no transactional history in BC, signed reconciliation as the go-live gate.

**Risk of getting it wrong:** high-irreversible in effect — you can technically correct almost anything, but a go-live on unreconciled balances or wrong opening costs contaminates the ledgers from entry one and the cleanup happens live, in production, under fire.

**Expertise tags:** `#general-setup` `#data-migration` `#rapidstart` `#cutover`

---

## Integration posture (APIs, Power Platform, e-invoicing)

**Where:** Built-in REST APIs (standard v2.0 + custom API pages), OData/web services, **E-Documents** framework + Peppol/service-provider connectors, Power Platform (Power Automate, Power Apps, Dataverse virtual tables), Shopify connector, entra app registrations for service-to-service auth.
**What it controls:** How BC exchanges data with the outside world — webshop, WMS/MES, banking, e-invoicing networks — and which platform bets the client is making. Brief here; each concrete integration is its own project.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Standard API v2.0 / custom API pages | Any bespoke or middleware integration; stable, versioned, supported | Screen-scraping-style ODATA on UI pages — brittle across updates |
| Power Automate for light integrations | Notifications, small syncs, human-in-the-loop steps; low volume | High-volume transactional sync — flows are not middleware; throughput, error handling and ALM suffer |
| Native connectors (Shopify, banking apps) | Where they exist, prefer them over custom builds | Feature gaps force workarounds worse than a clean custom integration |
| E-Documents + Peppol access point | Increasingly mandatory (EU e-invoicing mandates rolling in) — assess readiness at every new implementation *now*, even if the mandate is next year | Treating it as "phase 2, someday" for clients in mandate countries |
| ISV middleware/iPaaS | Multiple endpoints, mapping/monitoring needs, no internal dev | Single simple integration — overkill |

**Required client info:**
- Inventory of systems that must talk to BC (webshop, WMS, MES, payroll, banks, EDI partners) with direction and volume per flow
- Country e-invoicing mandates applicable to the client, and timeline
- Who owns integrations after go-live (internal dev, partner, nobody — "nobody" changes the architecture toward native connectors)
- Existing Power Platform footprint and governance

**Interactions:** EDI/e-invoicing shapes [number series](#number-series-design) and [document layouts](#report-selections--document-layouts); shop-floor/WMS integrations tie to [manufacturing registration](manufacturing.md#capacityoutput-journals--shop-floor-registration) and [warehouse handling](warehouse.md#item-journal-vs-warehouse-journal-per-level); Power Automate governance overlaps [approval workflows](#approval-workflows-native-vs-power-automate).

**Add-on impact:** Aptean F&B occupies extension points and has its own EDI/integration accelerators for food retail customers (GS1, retailer EDI) — check the add-on's integration catalogue before building custom. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Standard APIs for anything transactional, native connectors where they exist, Power Automate only for light automation, and a Peppol/e-invoicing readiness check in every discovery from 2026 onward.

**Risk of getting it wrong:** medium — integrations are replaceable, but a business built on a brittle flow-based sync discovers it at the worst possible volume moment.

**Expertise tags:** `#general-setup` `#integration` `#api` `#peppol` `#power-platform`

---

## Retention policies & data cleanup

**Where:** **Retention Policies** page (+ retention periods, per-table filters), applied to log-like tables (change log, job queue log entries, posted document archives, workflow step instances, etc.); **Change Log Setup** (what gets logged at all); date compression functions for ledger entries (use with extreme care).
**What it controls:** Automatic deletion of aging log/archive data to keep the database inside capacity limits and performance healthy; brief but worth configuring at go-live rather than at the first storage-overage invoice.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| Retention policies on log tables (change log 90–365 days, job queue logs 30–90 days, document archives 1–5 years) | Every SaaS tenant — set at go-live; storage overage costs real money | Tables under legal retention duties (posted ledgers) — policies are for logs/archives, not books |
| Change Log scoped to sensitive fields only | Log master-data fields that matter (bank accounts, credit limits, prices) | "Log everything" — bloats the DB and buries the signal |
| Date compression of old ledger entries | Very old, very large databases hitting limits | Anything the auditor may want at line level; compression is destructive summarization — last resort, with client sign-off |
| Do nothing | Never — every unmanaged tenant eventually hits capacity warnings | Always avoid |

**Required client info:**
- Statutory retention duties in the client's jurisdiction (books typically 7–10 years — those tables are out of scope for deletion)
- Which master-data changes must be traceable, and for how long?
- Current/projected database size vs licensed capacity

**Interactions:** Change Log scope supports [governance](#user-setup-permission-sets--security-light-governance) and audit; archive retention interacts with [document layouts/archiving habits](#report-selections--document-layouts); ledger retention duties are a [finance/compliance](finance.md#general-ledger-setup-key-choices) question before a technical one.

**Add-on impact:** Aptean F&B generates additional high-volume data (quality records, lot traceability, scanning logs) — include its log tables in the retention concept; traceability records may carry *food-law* retention minimums that override cleanup instincts. See [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** At go-live: change log scoped to sensitive fields with a 1-year retention policy, job queue/telemetry-ish logs at 90 days, document archives per client policy; ledger compression never, absent a crisis and written sign-off.

**Risk of getting it wrong:** low — policies are adjustable; the exceptions are deleting something under legal retention (compliance incident) or date-compressing entries you later needed (irreversible).

**Expertise tags:** `#general-setup` `#retention` `#data-cleanup` `#compliance`
