# Finance — Odoo (Standard)

> **Scope:** Odoo 19 Enterprise (Odoo Online, Odoo.sh or on-premise); Community edition differences flagged inline. Belgian localization (l10n_be) specifics woven in — this knowledge base serves Belgian SME implementations.
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when Odoo releases functional changes to this area (one major release per year, typically October).

This file covers the financial core of an Odoo implementation for a Belgian SME: the fiscal localization package, the Belgian MAR chart of accounts, journals and sequences, VAT and its Belgian declarations, the Peppol e-invoicing mandate, the continental-vs-anglo-saxon posting logic and the automatic accounts on product categories (Odoo's equivalent of BC's posting groups), banking with CODA and SEPA, receivables terms and follow-ups, currencies, fixed assets, budgets/consolidation, and period close. Finance setup is in scope for **every** Odoo project — even a sales- or inventory-led one — because product categories and the localization package silently decide where every operational transaction posts. Note the recurring Enterprise/Community fault line running through this file: the full **Accounting** app is Enterprise-only; Community ships **Invoicing** only (customer invoices, vendor bills, payments — no statutory reports, no bank reconciliation, no assets, no budgets), with OCA modules filling gaps on on-premise installs only.

---
## Fiscal localization package (Belgian l10n_be)

**Where:** Chosen at database/company creation (the company's country sets it); visible under **Accounting → Configuration → Settings → Fiscal Localization**. Package `l10n_be` plus companion modules (CODA import, Intrastat, Belgian reports — exact module split varies by version).
**What it controls:** Everything country-specific in one shot: the Belgian MAR chart of accounts, all Belgian VAT taxes wired to the official return grids, fiscal positions (intra-EU, export, co-contractant), the Belgian tax report, annual client listing, EC sales list, Intrastat, CODA import, structured communication and the NBB annual-accounts export. Every block below builds on it. **Community edition:** the package (chart + taxes) installs, but the Belgian *reports* (VAT return export, client listing, Intrastat, NBB export) live in the Enterprise Accounting app — a Community client files from the accountant's tools or OCA reporting modules (on-premise only).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **l10n_be installed at company creation (company country = Belgium)** | Every Belgian legal entity, no exceptions — not a discussion point, but a checklist item to *verify* before any posting. Never substitute a foreign package for a Belgian entity to please a foreign parent: group reporting is solved with account mapping, not by sacrificing the statutory localization | — |
| **Generic/wrong package, "fix the chart later"** | Never | Retrofitting taxes, grids and the MAR onto a company with posted entries means remapping every tax, account and open document — effectively a re-implementation into a fresh company |
| **Optional Belgian modules reviewed one by one (Intrastat, disallowed expenses, 281.50 fee forms, SODA payroll-entry import)** | Review with the client's accountant at kickoff — cheap to install early, annoying to discover missing at the first filing | Don't install speculative modules "just in case"; each adds configuration surface |

**Required client info:**
- Is the entity Belgian VAT-registered, and under which regime (monthly vs quarterly returns)? Who files the VAT return and annual accounts — internal, or an external accountant who may prefer their own tooling?
- Any Intrastat obligation, 281.50 fee forms, disallowed-expenses reporting, or payroll entries arriving as SODA files? Multi-company database (each company gets its own localization — see [company structure](general-setup.md#company-structure-one-company-vs-multi-company))?

**Interactions:** Feeds every block in this file, especially the [MAR chart](#chart-of-accounts-design-belgian-mar), [Belgian VAT](#taxes-vat-return--fiscal-positions-belgian-vat) and [Peppol](#e-invoicing--peppol). Edition/hosting choice constrains what is available — see [edition & hosting](general-setup.md#edition--hosting-enterprise-vs-community-online-vs-odoosh-vs-on-premise).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base. For on-premise Community installs, the OCA `l10n-belgium` repository is the recognized fallback for missing Belgian reports.

**Default recommendation:** Company created with country Belgium so l10n_be installs automatically; verify chart, taxes and tax report are present *before* the first posting; review optional Belgian modules with the accountant at kickoff.

**Risk of getting it wrong:** high-irreversible — changing the fiscal localization after entries are posted is effectively a re-implementation in a new company.

**Expertise tags:** `#finance` `#l10n-be` `#compliance` `#vat`

---
## Chart of accounts design (Belgian MAR)

**Where:** **Accounting → Configuration → Chart of Accounts**; account groups define the hierarchy; analytic plans under **Accounting → Configuration → Analytic Plans**.
**What it controls:** The structure of all financial reporting. l10n_be installs the Belgian **MAR/PCMN** (minimum normalized chart of accounts, classes 1–7) — in Belgium this numbering is the legal norm, not a template to redesign. The real design decision is what *not* to add: analytical detail belongs in analytic plans, not in account proliferation.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Standard MAR kept lean, a handful of client-specific sub-accounts within the legal classes** | Every Belgian client. The external accountant recognizes it, the NBB export maps from it, the VAT grids are wired to it. Renumbering outside MAR logic is never on the table | — |
| **Legacy chart replicated (one account per department/branch/product line)** | Almost never — tolerated transitionally only when the accountant refuses change mid-project | Multiplies maintenance, breaks the fit with Belgian reports, and defeats Odoo's analytics. Push back hard: departments and projects are analytic plans, not 61x sub-accounts |
| **Analytic plans + distribution models for management analysis** | The Odoo-native pattern: dimensions (department, project, branch) as analytic plans with mandatory/optional policies per plan, auto-applied via distribution models | Don't create a plan nobody will filter on monthly — every mandatory analytic plan is a data-entry burden on operational users |

**Required client info:**
- Which management cuts does the client actually review monthly (department, project, site, product line)? Those become analytic plans — see [analytic architecture](general-setup.md#analytic-accounting-architecture-plans--distributions).
- Does the external accountant work *in* Odoo or from exports (their habits decide your freedom with sub-accounts)? Were legacy accounts genuine ledger splits or misused analytics?

**Interactions:** Automatic accounts on product categories must point into this chart — see [continental vs anglo-saxon](#continental-vs-anglo-saxon-accounting--automatic-accounts). Receivable/payable control accounts (400000/440000) come from partner account properties; keep manual entries off them. Opening balances land here at cutover — see [data migration](general-setup.md#data-migration-approach-imports--opening-balances).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Standard MAR untouched in structure, lean additions inside legal classes, all management analysis in analytic plans with distribution models.

**Risk of getting it wrong:** medium — accounts can be added, merged or deactivated later, but unpicking an account-proliferation chart after months of postings (and retraining the accountant) is disruptive and expensive.

**Expertise tags:** `#finance` `#chart-of-accounts` `#l10n-be` `#reporting`

---
## Journal design & sequences

**Where:** **Accounting → Configuration → Journals**; the sequence is derived from the journal's short code and the last posted entry's number; per-journal defaults on each journal form.
**What it controls:** Which document streams exist (sales, purchase, bank, cash, miscellaneous), the short code prefixing every entry number, and — critical in Belgium — the numbering of fiscal documents. Belgian law expects invoices numbered sequentially and gapless per series; Odoo numbers per journal, per period pattern (e.g. `INV/2026/00001`), and posted entries cannot be deleted, only cancelled/reversed, which preserves the sequence.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Standard set: one sales, one purchase, one bank journal per IBAN, one cash (if any), miscellaneous — plus a dedicated OPENING journal for migration and one per recurring import (SODA payroll)** | Most SMEs — start here and add only on a demonstrated need; purpose-split misc journals keep the audit trail readable | Don't over-engineer tiny clients — one misc journal is fine |
| **Dedicated credit-note sequence on sales/purchase journals** | Belgian practice: credit notes in their own series (`RINV/…`); enable it on both document journals | Sharing one sequence between invoices and credit notes muddies the accountant's audit trail — avoid. > ⚠️ Verify against current Odoo documentation. |
| **Multiple sales journals (per branch, activity or invoice series)** | Genuinely separate invoice series: branches with own numbering, distinct activities the accountant books separately, POS vs field sales | Don't split journals for analysis you could do with analytic plans — every journal is a sequence, a dashboard tile and a set of defaults to maintain |

**Required client info:**
- How many invoice series does the client legally/operationally run today (branches, activities, cash registers)?
- Continue legacy numbering at cutover or start fresh series at go-live? (Odoo derives the sequence from the first entry's name — set it deliberately.)
- How many bank accounts and cash drawers (one journal each), and how do payroll entries arrive?

**Interactions:** Numbering conventions belong with [document numbering](general-setup.md#document-numbering-sequences). Bank journals are configured in [banking](#banking-coda-sepa--reconciliation). The Peppol inbound flow targets one purchase journal — see [E-invoicing & Peppol](#e-invoicing--peppol). Lock dates apply per company across all journals — see [period close](#period-close--lock-dates).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Standard journal set, dedicated credit-note sequences on sales and purchase journals, one bank journal per IBAN, a dedicated OPENING journal; extra sales journals only for legally distinct series.

**Risk of getting it wrong:** medium — journals can be added and renamed, but a botched first sequence (wrong format or starting number) lives in the legal document trail forever, and merging two journals' history is not a thing.

**Expertise tags:** `#finance` `#compliance` `#l10n-be`

---
## Taxes, VAT return & fiscal positions (Belgian VAT)

**Where:** **Accounting → Configuration → Taxes** (installed by l10n_be, each tax wired to Belgian return grids); **Fiscal Positions** under Configuration; the return at **Accounting → Reporting → Tax Report**; annual client listing via **Accounting → Reporting → Belgium: Create 325 form**; EC sales list and Intrastat under the same Reporting menu when installed.
**What it controls:** VAT on every document line, and whether the periodic Belgian VAT return, the annual client listing and the EC sales list come out of Odoo correct. l10n_be taxes carry the grid mapping (boxes 00–03, 44–49, 54–59, 81–87…), so using the *installed* taxes — never hand-built lookalikes — is what makes the return right. Fiscal positions remap taxes (and optionally accounts) per counterparty: intra-EU B2B, export, and the Belgian **co-contractant** reverse charge for works in immovable state.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Standard l10n_be taxes + standard fiscal positions, auto-applied by country/VAT number** | Every Belgian client. Auto-detect the fiscal position and validate EU customers' VAT numbers (VIES) so the intra-EU exemption holds | Hand-crafting taxes that look identical but miss grid mappings — the return silently goes wrong |
| **Co-contractant fiscal position on the customer record / auto-apply rules** | Mandatory for construction-sector reverse-charge flows: 0% with the right grids on both sides | Applying it from memory per invoice — it will be forgotten. Cash-basis VAT regimes are rare — accrual is the default; confirm with the accountant before touching that switch |
| **VAT return filed from Odoo (Intervat XML export; Odoo 19 adds direct submission to Intervat/MyMinFin)** | Client files internally: close the tax period from the Tax Report, export/submit, set the tax lock date | External accountant files from fiduciary software → agree who owns the tax lock date; Odoo's return becomes a control, not the filing |
| **Intrastat module configured (commodity codes, regions, transaction codes)** | Clients above the arrivals/dispatches thresholds | Below threshold: skip — the per-line data-entry burden is real |

**Required client info:**
- Monthly or quarterly VAT regime, and who files from which tool?
- Intra-EU sales/purchases, exports, imports (postponed accounting via ET 14000 license?), co-contractant flows? Above Intrastat thresholds in either direction, and who maintains commodity codes on products?
- Any mixed/partial VAT deduction or car/disallowed-expense limits the accountant expects the system to respect?

**Interactions:** Taxes and grids come from the [localization package](#fiscal-localization-package-belgian-l10n_be) — never rebuild them. The tax lock date after each filed period is part of [period close](#period-close--lock-dates). Fiscal-position account mapping interacts with [automatic accounts](#continental-vs-anglo-saxon-accounting--automatic-accounts). Default taxes on products feed sales and purchase flows — see [invoicing policy](sales.md#invoicing-policy--down-payments) and [bill control](purchasing.md#bill-control-policy--3-way-matching).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Installed l10n_be taxes only, fiscal positions auto-applied with VIES validation, co-contractant position where relevant, the VAT return generated in Odoo every period even when the accountant files externally (the cheapest reconciliation you will ever get), tax lock date set immediately after each filing.

**Risk of getting it wrong:** high — a wrong tax or missing grid produces incorrect legal filings; corrections mean credit-and-reinvoice surgery plus amended returns, and the accountant loses trust in the system precisely when you need them onside.

**Expertise tags:** `#finance` `#vat` `#l10n-be` `#compliance`

---
## E-invoicing & Peppol

**Where:** **Accounting → Configuration → Settings → PEPPOL Electronic Invoicing** (registration, receiving journal); per-customer e-invoicing format on the partner; sending via the invoice **Send** flow.
**What it controls:** Compliance with the Belgian B2B e-invoicing mandate: since **1 January 2026**, Belgian VAT-registered businesses must send and receive structured B2B invoices over the Peppol network (UBL / Peppol BIS Billing 3.0). Odoo is itself a certified **Peppol access point** — registration happens inside Accounting settings (Belgian EAS `0208` + enterprise number as endpoint), with no third-party access-point contract or per-document fee in Enterprise. Inbound Peppol documents land as **draft vendor bills** in a purchase journal you designate.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Register Odoo as the client's Peppol access point (send + receive)** | The default for every Belgian go-live since 2026 — one system, invoices sent and received as structured documents, drafts created automatically. A receive-only phase during cutover is fine; staying there isn't — the mandate covers sending too | Client already registered via another access point (bank, Billit, accountant's platform): a Peppol ID receives at *one* access point only — plan the registration migration deliberately, not on go-live day |
| **Peppol as primary B2B channel, PDF/email secondary** | Standard: B2B invoices go Peppol; PDF remains for B2C, foreign non-Peppol customers, and human readability | Treating PDF-by-email as the primary channel for Belgian B2B — non-compliant since 2026 |
| **Vendor-bill digitization (OCR) for the residual paper/PDF inflow** | Suppliers outside the mandate's scope still send PDFs; Enterprise OCR (IAP credits) extracts them into draft bills | Don't sell OCR as the main inbound channel for a Belgian client — Peppol is, and it beats any OCR on accuracy |
| **Community edition: external access point or partner/OCA connector (on-premise)** | Only when the client is locked into Community — Odoo's built-in access point and the OCR service are Enterprise/Odoo-hosted features. > ⚠️ Verify against current Odoo documentation. | Don't leave a Community client without *any* Peppol answer — the mandate doesn't care about edition |

**Required client info:**
- Is the client already on Peppol via another access point (check the Peppol directory), and who owns moving the registration?
- Share of customers/suppliers that are Belgian B2B vs B2C vs foreign — sizes the residual PDF/OCR flow.
- Who validates inbound draft vendor bills, and into which purchase journal should they arrive?

**Interactions:** Inbound journal choice belongs to [journal design](#journal-design--sequences). Vendor-bill validation discipline connects to [bill control](purchasing.md#bill-control-policy--3-way-matching). Structured payment communication rides on outbound invoices — see [banking](#banking-coda-sepa--reconciliation). Overall API posture — see [integration posture](general-setup.md#integration-posture-apis-webhooks-e-invoicing).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Register Odoo as the access point at go-live (after confirming no competing registration), Peppol as primary B2B channel with PDF secondary, inbound drafts into a designated purchase-journal review queue, OCR only for the residual non-Peppol inflow.

**Risk of getting it wrong:** medium — registration and formats are fixable, but a botched access-point migration means weeks of invoices landing at the old provider, and mandate non-compliance exposes the client to sanctions and VAT-deduction disputes.

**Expertise tags:** `#finance` `#peppol` `#compliance` `#l10n-be`

---
## Continental vs Anglo-Saxon accounting & automatic accounts

**Where:** Anglo-saxon toggle: company-level accounting setting (visible with developer mode; the localization sets the default — l10n_be = continental/off). Automatic accounts: **product category** form (income/expense account properties; stock input/output/valuation accounts when valuation is automated), overridable per product.
**What it controls:** The single most consequential posting decision in Odoo — *when* purchases hit expenses and *where* every product transaction lands. **Continental (Belgian GAAP): the vendor bill posts to a class-60 expense account immediately, and inventory movement is stock-variation logic (609/71x).** Anglo-saxon: purchases park on an interim/stock account and COGS posts at delivery/invoice. The product category's accounts are Odoo's equivalent of BC's posting-group matrix: get them wrong and every sale, receipt and delivery posts wrong — silently.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Continental (anglo-saxon off) — the l10n_be default** | Every standalone Belgian entity: matches Belgian GAAP, the MAR, and what the accountant expects to see | — |
| **Anglo-saxon on** | Only when a foreign parent mandates COGS-at-delivery group reporting *and* the local accountant signs off on deriving Belgian statutory figures from it | Switching a live Belgian company — existing balances don't convert; treat the toggle as fixed at go-live. > ⚠️ Verify against current Odoo documentation. |
| **Automatic accounts set per product category, few categories, per-product overrides banned by convention** | The design pattern: categories sized by *posting behaviour* (trade goods, raw materials, services, freight), each mapped to MAR income/expense/stock accounts and reviewed with the accountant line by line | One category per product family "for analysis" — that's what attributes and analytic plans are for; and habitual per-product account overrides make the category design meaningless and audits painful |

**Required client info:**
- Standalone Belgian entity, or subsidiary with group-mandated COGS logic? Get the accountant's position in writing before go-live.
- Which MAR accounts should each product family's revenue, expense and stock hit? (Walk the category → account mapping with the accountant.)
- Are services and goods invoiced by the same entity (separate categories with separate 70x revenue accounts)?

**Interactions:** Product category also carries costing method and valuation mode — design all three together with [product categories & costing](inventory.md#product-categories--costing-method-standard--avco--fifo) and [inventory valuation posting](#inventory-valuation-posting-manual-vs-automated). Fiscal positions can remap accounts per counterparty ([Belgian VAT](#taxes-vat-return--fiscal-positions-belgian-vat)). Landed costs post through these accounts too — see [landed costs](purchasing.md#landed-costs).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Continental posting (leave the l10n_be default alone), a handful of product categories sized by posting behaviour, category-to-MAR mapping signed off by the accountant before UAT.

**Risk of getting it wrong:** high-irreversible — flipping the anglo-saxon toggle or re-pointing category accounts after months of postings leaves a ledger half in each logic; practically you reclassify history manually or restart valuation. This is the block to spend workshop time on.

**Expertise tags:** `#finance` `#anglo-saxon` `#posting-groups` `#chart-of-accounts` `#costing`

---
## Inventory valuation posting (manual vs automated)

**Where:** **Product category → Inventory Valuation: Manual (periodic) / Automated (perpetual)**; stock journal and stock input/output/valuation accounts on the category when automated.
**What it controls:** Whether stock moves generate accounting entries in real time. **Manual/periodic:** stock moves post nothing; the accountant books stock variation at close from the inventory valuation report (the classic Belgian SME pattern — 609/71x entries quarterly or yearly). **Automated/perpetual:** every receipt and delivery posts to stock valuation and counterpart accounts through a stock journal — a continuously correct balance sheet, at the price of many entries and a real monthly stock-to-GL reconciliation discipline.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Manual (periodic) valuation** | Trading/service clients whose accountant books stock variation at close; small teams without a stock-to-GL reconciliation habit | Clients who want monthly management accounts with true margins and stock — the ledger stock line is stale between closes |
| **Automated (perpetual) valuation — for all material stock categories, or mixed per category (automate trade goods, keep consumables manual)** | Manufacturers and stock-intensive clients with monthly reporting; pairs naturally with AVCO/FIFO. A deliberate, documented mix per category is legitimate | Clients with sloppy warehouse discipline — every unrecorded move becomes an accounting error; and undocumented accidental mixes, where the accountant finds half a balance sheet |

**Required client info:**
- Does the accountant book stock variation periodically today, and do they *want* real-time stock accounting? (Ask literally — many Belgian fiduciaries prefer periodic.)
- Are monthly management accounts with margins a stated requirement, is warehouse discipline honestly same-day, and who will own the monthly stock-to-GL reconciliation if automated?

**Interactions:** This is the accounting face of the inventory decision — the operational face is in [inventory valuation](inventory.md#inventory-valuation-manual-vs-automated) and [product categories & costing](inventory.md#product-categories--costing-method-standard--avco--fifo); decide them in the same workshop. Accounts and posting logic come from [automatic accounts](#continental-vs-anglo-saxon-accounting--automatic-accounts). Switching a category's valuation mode mid-life triggers revaluation entries — plan it at a close, not casually.

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Manual valuation for trading SMEs whose accountant closes stock periodically; automated only when monthly margin reporting is a stated requirement *and* someone owns the reconciliation — then AVCO/FIFO per the inventory file.

**Risk of getting it wrong:** medium — the mode can be switched per category, but the switch creates opening-valuation entries and history stays in the old logic; a year of unreconciled automated valuation is a forensic cleanup job.

**Expertise tags:** `#finance` `#costing` `#posting-groups` `#reporting`

---
## Banking: CODA, SEPA & reconciliation

**Where:** Bank journals (one per IBAN) under **Accounting → Configuration → Journals**; statement import on the journal/dashboard (CODA upload); **Settings → Bank Synchronization** (online providers); **Reconciliation Models** under Configuration; SEPA payment methods on the bank journal; direct-debit mandates on customers; Belgian structured communication (OGM/VCS, `+++xxx/xxxx/xxxxx+++`) as the payment-reference standard on sales journals/settings.
**What it controls:** How money movements enter Odoo and how they clear open invoices and bills. Belgium has a gift here: **CODA**, the standardized statement format every Belgian bank exports, imports natively via l10n_be — richer and more reliable than CSV/CAMT guesswork. Outbound, Odoo generates **SEPA credit transfer** files (ISO 20022 pain.001) from batch payments and **SEPA direct debit** collections (pain.008) from signed mandates.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **CODA import per bank journal + structured communication (OGM/VCS) on all outgoing invoices** | The Belgian default — deterministic, complete, every accountant knows it, and CODA + structured reference makes customer-payment matching near-automatic | — |
| **Bank synchronization (Enterprise, via connected providers) on top** | Convenience for small clients: transactions flow in automatically between CODA files | Treasury-critical clients should anchor on bank-delivered CODA; sync coverage/quality is provider- and bank-dependent. **Community edition:** no bank sync and no native statement import (the Accounting app is Enterprise) — OCA import modules on-premise, or manual entry |
| **Reconciliation models (auto-match rules, fee write-offs, recurring counterparts)** | Build a short, clearly named list at go-live: bank charges, rounding write-offs, payroll and VAT payments | Dozens of overlapping rules nobody remembers |
| **SEPA credit transfer batches; SEPA direct debit where signed mandates exist** | Standard vendor-payment flow: select bills → batch payment → pain.001 to the bank portal; direct debit (pain.008) for recurring receivables with mandate discipline | Non-SEPA international payments remain manual/bank-side; skip direct debit for one-off customers without mandates — failed collections (R-transactions) need a defined follow-up |

**Required client info:**
- Which banks and IBANs, and does each subscription include CODA delivery (all Belgian banks can — confirm it's activated)?
- How are vendors paid today (bank-portal upload, which format?), and are there direct-debit collections with signed SEPA mandates?
- Who reconciles, how often, and do they also do cash application (same person → lean hard on reconciliation models)?

**Interactions:** One bank journal per IBAN — [journal design](#journal-design--sequences). Payment terms and follow-ups decide what the matching engine sees — [next block](#payment-terms-follow-ups--payment-methods). Foreign-currency bank journals need [currencies](#currencies--exchange-rates) configured and their currency treated as fixed once posted on. Peppol invoices carry the structured reference too — [E-invoicing & Peppol](#e-invoicing--peppol).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base. On-premise Community clients typically use OCA banking modules (CODA statement import, payment order for SEPA files) — flag it in scoping. > ⚠️ Verify against current Odoo documentation.

**Default recommendation:** CODA import as the backbone (sync as convenience on top), structured communication on every outgoing invoice, a short list of reconciliation models, SEPA CT batches for vendor payments, direct debit only where mandates genuinely exist.

**Risk of getting it wrong:** medium — formats and rules are changeable, but a sloppy first statement import (wrong opening balance) haunts every later reconciliation.

**Expertise tags:** `#finance` `#banking` `#coda` `#sepa` `#payments` `#l10n-be`

---
## Payment terms, follow-ups & payment methods

**Where:** **Accounting → Configuration → Payment Terms**; follow-up levels and the follow-up report under **Accounting → Customers** (Enterprise); payment providers under **Configuration → Payment Providers**; early-payment discount settings on the payment term.
**What it controls:** Due-date calculation on invoices and bills, cash-discount handling (Belgian VAT rules on early-payment discounts — the discount reduces the VAT base — are handled by the localization when configured on the term), the automated dunning ladder (follow-up levels with per-level actions: email, letter, escalation), and whether customers can pay online via a provider link. **Community edition:** basic payment terms exist, but the automated follow-up engine is Enterprise — Community clients chase from aged-balance exports or OCA modules on-premise.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Small shared list of payment terms (30 days end of month, 30 net, immediate, 8 days −2%)** | Always — one list serves sales and purchases; early-payment discount configured on the term so the VAT treatment is automatic | Per-customer bespoke-terms proliferation; and keep promised terms inside the Belgian B2B payment-term cap (60 days unless validly agreed otherwise) |
| **Follow-up levels: 2–3 steps with grace days and level texts, human-approved at go-live; late-payment interest/fee wording included only if the client actually enforces it** | Any client that chases debtors — the queue-and-review screen removes the monthly grind while keeping a human in the loop; exempt key accounts deliberately rather than never chasing | Fully automatic sending from day one, and elaborate interest invoicing nobody will ever issue |
| **Payment provider on customer invoices (online payment link)** | B2C-ish or low-trust segments where a pay-now link measurably accelerates cash | Pure B2B with bank-transfer culture — provider fees buy nothing; CODA + structured reference already matches transfers |

**Required client info:**
- Standard terms given and received today, and any cash-discount arrangements worth automating?
- Collections reality: who chases, at what intervals, who must approve before a reminder reaches a strategic customer, and are follow-up texts needed in FR/NL/EN?

**Interactions:** Follow-up quality depends entirely on reconciliation keeping open invoices honest — [banking](#banking-coda-sepa--reconciliation). Terms shown on quotes come from the sales flow — see [invoicing policy](sales.md#invoicing-policy--down-payments) and [pricelists & discount policy](sales.md#pricelists--discount-policy). Direct-debit customers pair a payment method with mandates ([banking](#banking-coda-sepa--reconciliation)).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Lean shared terms list with the client's two or three real terms plus an early-payment-discount variant if used; 3-level follow-ups configured but human-approved at go-live; no payment provider unless the customer base is B2C-shaped.

**Risk of getting it wrong:** low — all of this is changeable anytime; the real risks are operational (auto-reminders to strategic accounts, discount terms mis-stating VAT).

**Expertise tags:** `#finance` `#payments` `#vat`

---
## Currencies & exchange rates

**Where:** **Accounting → Configuration → Settings → Currencies**: activate currencies, automatic rate service (ECB among others) with update frequency; exchange-difference journal and gain/loss accounts in settings; unrealized-gains revaluation via the Enterprise adjustment report/wizard.
**What it controls:** Which currencies can appear on documents, prices and bank accounts; where realized exchange differences post automatically at payment (654/754 in the MAR); and whether open foreign-currency balances are revalued at close — Belgian GAAP treats unrealized gains and losses asymmetrically, so the *booking* of the revaluation is the accountant's call, not a system default.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **EUR only, nothing activated** | The honest default for most Belgian SMEs — don't configure currencies "just in case" | — |
| **Foreign currencies + automatic ECB rates (daily)** | Any client genuinely invoicing, purchasing or banking in USD/GBP/CHF…; realized differences then post automatically | Manually keyed rates as a routine — someone forgets, and every margin is noise. Group-issued monthly rates are the exception: turn auto-update off and name an owner |
| **Currency revaluation at close (unrealized)** | Clients with material open FX positions; entries validated by the accountant given the Belgian GAAP asymmetry | Immaterial exposure — skip the ceremony. **Community edition:** the revaluation wizard/report is Enterprise; Community books it as a manual journal entry. > ⚠️ Verify against current Odoo documentation. |

**Required client info:**
- Which currencies actually flow through sales, purchases and bank accounts, and how material are open positions at close?
- Whose rates govern (ECB daily vs group monthly), and how does the accountant book unrealized differences under Belgian GAAP (provision for unrealized losses, deferral of gains)?

**Interactions:** Gain/loss accounts must exist in the [MAR chart](#chart-of-accounts-design-belgian-mar). Foreign-currency bank journals — [banking](#banking-coda-sepa--reconciliation). Group reporting in another presentation currency is a [consolidation](#budgets--consolidation) topic, not a reason to multiply document currencies. The company currency itself is fixed at creation — see [company structure](general-setup.md#company-structure-one-company-vs-multi-company).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Activate only currencies with real flows, ECB automatic rates daily, exchange-difference accounts verified against the MAR, revaluation at close only for material positions with the accountant's sign-off.

**Risk of getting it wrong:** medium — currencies and rates are correctable, but the company currency is high-irreversible (a wrong one means a new company), and a year of manual-rate drift quietly corrupts every FX margin.

**Expertise tags:** `#finance` `#currencies` `#reporting`

---
## Fixed assets

**Where:** **Accounting → Accounting → Assets** (Enterprise); **Asset Models** under Configuration; automation hook on the asset account (create draft/validated asset when a vendor bill hits it).
**What it controls:** The asset register and automated depreciation. Asset models define method (straight-line, declining, declining-then-straight-line), duration, prorata start and the accounts (21x–24x asset, 63x depreciation, accumulated-depreciation counterpart); linking a model to an account makes a vendor-bill line on that account spawn a draft asset automatically — the single best trick for keeping the register complete. Belgian pro-rata rules and the corporate-tax treatment of degressive depreciation have changed in recent years: the *method per asset class is the accountant's decision*; Odoo just executes it.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Asset models per MAR asset class (buildings, plant, vehicles, IT, furniture), auto-draft from vendor bills** | The default: register stays complete, monthly depreciation posts itself. Fully manual asset creation is defensible only at a few assets per year | Manual registers at any real volume — they drift from the ledger within a year |
| **Accounting vs tax depreciation divergence kept out of Odoo** | Where the accountant runs a separate tax computation: keep Odoo on the *accounting* books; the tax adjustment lives in the return | Forcing two depreciation regimes into one Odoo book — there is no native second (tax) book; that divergence belongs to the accountant's tax software. > ⚠️ Verify against current Odoo documentation. |
| **Community edition: no Assets module** | OCA `account_asset_management` on-premise is the recognized alternative; otherwise assets live in the accountant's tooling | Don't promise Community clients Enterprise asset automation |

**Required client info:**
- Asset classes, useful lives and methods per class, confirmed by the accountant (including their position on degressive for tax)?
- Volume and quality of the current asset register (its migration is its own workstream), and the capitalization threshold below which purchases are expensed?
- Who validates auto-drafted assets from vendor bills?

**Interactions:** Asset and depreciation accounts live in the [MAR chart](#chart-of-accounts-design-belgian-mar); acquisitions arrive through vendor bills and [Belgian VAT](#taxes-vat-return--fiscal-positions-belgian-vat) (cars: deduction limits). Depreciation entries respect [lock dates](#period-close--lock-dates). Load the opening register as assets *in running mode* (acquisition value + already-depreciated amount + remaining schedule) against migrated balances — never let opening assets re-post acquisitions; see [data migration](general-setup.md#data-migration-approach-imports--opening-balances).

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base (OCA asset module noted above for Community on-premise).

**Default recommendation:** Asset models per MAR class with auto-draft from the mapped accounts, straight-line unless the accountant specifies otherwise, opening register loaded in running mode, monthly automated depreciation.

**Risk of getting it wrong:** medium — assets can be modified/re-evaluated, but a wrong opening load double-posts acquisitions, and months of wrong-method depreciation mean asset-by-asset corrections rather than one reclassification.

**Expertise tags:** `#finance` `#fixed-assets` `#l10n-be`

---
## Budgets & consolidation

**Where:** Budgets: **Accounting → Budgets** (Enterprise) — budget lines against analytic plans and/or accounts with achieved-vs-planned tracking. Consolidation: since Odoo 18 the separate Consolidation app was replaced by ledger-based consolidation inside Enterprise Accounting (consolidation ledgers, account mapping/merge across companies, horizontal groups on reports). > ⚠️ Verify against current Odoo documentation.
**What it controls:** Whether plan-vs-actual lives in Odoo, and how a multi-entity group sees combined figures. Two different animals hide under "consolidation": *aggregated multi-company reporting* (same database, standardized/mapped charts, reports across companies — cheap and usually enough for management) and *true consolidation* (eliminations, adjustment journals, currency translation with a manual CTA line in equity — an accountant's exercise Odoo only partially automates). **Community edition:** no budget feature and no consolidation tooling — OCA alternatives on-premise, or spreadsheets.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **No budgets in Odoo** | The honest default for SMEs that budget in a spreadsheet once a year and never track against it | — |
| **Budgets on analytic plans (departments/projects) reviewed monthly** | Clients with a real monthly plan-vs-actual routine and clean analytic distributions | Budgeting without the analytic discipline to match — achieved figures will be garbage |
| **Multi-company reporting with a standardized chart; ledger-based consolidation only when group statements are genuinely required** | Groups on one database wanting combined figures — standardize the CoA across companies *before* company no. 2 exists; step up to consolidation ledgers when statutory-style group statements with adjustments are needed | Most Belgian SME groups fall under the consolidation-exemption thresholds and the external accountant produces whatever is filed — don't implement machinery for a report nobody must produce |

**Required client info:**
- Does anyone review plan-vs-actual monthly today, and at what granularity? (No routine → no budgets module.)
- How many legal entities now and in 18 months, same database, and is consolidated filing legally required (thresholds) or is this management aggregation? Are intercompany partners flagged consistently for eliminations?

**Interactions:** Budgets stand on the [analytic architecture](general-setup.md#analytic-accounting-architecture-plans--distributions). Consolidation quality is decided by CoA standardization ([MAR chart](#chart-of-accounts-design-belgian-mar)), the [company structure](general-setup.md#company-structure-one-company-vs-multi-company) and [currency](#currencies--exchange-rates) handling for non-EUR entities.

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base.

**Default recommendation:** Skip budgets unless a monthly review routine demonstrably exists; multi-company reporting with a standardized chart for group visibility; true consolidation only when filing is legally required or the group genuinely runs on consolidated statements — and then with the accountant in the room.

**Risk of getting it wrong:** low — budgets and consolidation setups are additive and reversible; the one expensive mistake is *not* standardizing the chart before the second company exists.

**Expertise tags:** `#finance` `#consolidation` `#reporting`

---
## Period close & lock dates

**Where:** **Accounting → Accounting → Lock Dates**: separate dates to Lock Sales, Lock Purchases, Lock Tax Return, Lock Everything, plus the irreversible **Hard Lock**; year-end via the tax-return flow and a manual allocation entry; Belgian annual accounts via the NBB/BNB export (XBRL) under the Belgian reports; optional inalterability hashing on journals for a tamper-evident trail.
**What it controls:** Who can still post into which period. The tax lock protects filed VAT periods (entries dated before it get their tax values pushed into the next open period); sales/purchase locks stop operational users back-dating documents; Lock Everything closes the period for all entries; the Hard Lock is permanent — Odoo's answer to inalterability requirements. Year-end: Odoo has no closing transaction per se — the P&L rolls into undistributed profits automatically; the accountant books the allocation (MAR 69x/14x) as a misc entry, and the annual accounts go to the National Bank via the XBRL export. Belgian retention applies: books and supporting documents must stay retrievable for **7+ years** (longer for real-estate VAT records) — on Odoo Online, that makes the backup/exit strategy part of close design; see [edition & hosting](general-setup.md#edition--hosting-enterprise-vs-community-online-vs-odoosh-vs-on-premise).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Monthly rhythm: sales/purchase locks rolled forward each month, tax lock set immediately after each VAT filing, Lock Everything at approved year-end** | The standard pattern for every live client — cheap insurance against the auditor finding entries in filed periods | No locks at all — someone *will* back-date into a filed VAT period, and the correction lands in a later return with an explanation owed |
| **Hard Lock on closed fiscal years (and inalterability hashing where the auditor wants it)** | After NBB filing and shareholder approval, when provable inalterability is wanted | Setting it casually — it is genuinely irreversible; agree the policy with the accountant and apply it only to fully settled years. > ⚠️ Verify against current Odoo documentation. |
| **NBB annual accounts from Odoo (XBRL export)** | Clients filing internally: generate from the Belgian reports | Most SMEs: the external accountant files from their fiduciary suite — Odoo's export is then a cross-check, not the filing |

**Required client info:**
- Close calendar and discipline: who may post into a prior month, until when, and who moves the lock dates?
- Who files the VAT return and the NBB annual accounts, and from which system? Where do accruals, deferrals and the profit-allocation entry get booked — internal or accountant?
- Does the client (or their auditor) want hard locks/hashing, and on what cadence?

**Interactions:** The tax lock date is the closing act of every [VAT filing](#taxes-vat-return--fiscal-positions-belgian-vat). Depreciation ([fixed assets](#fixed-assets)), currency revaluation ([currencies](#currencies--exchange-rates)) and stock variation ([inventory valuation posting](#inventory-valuation-posting-manual-vs-automated)) are the recurring close tasks to calendar. Lock dates apply across all [journals](#journal-design--sequences) per company.

**Add-on impact:** None known yet — no Odoo add-on overlays exist in this knowledge base. Community on-premise clients without the Enterprise Belgian reports handle the NBB filing in the accountant's tooling or via OCA `l10n-belgium` modules.

**Default recommendation:** Monthly sales/purchase locks, tax lock set the day the VAT return is filed, Lock Everything at approved year-end, Hard Lock only on settled years by explicit policy, and the close-task calendar (depreciation, revaluation, stock variation, accruals) agreed with the accountant before go-live.

**Risk of getting it wrong:** medium — lock dates themselves are adjustable (except the Hard Lock, which is high-irreversible by design); the real cost of lax locking is amended VAT returns and an audit trail the accountant stops trusting.

**Expertise tags:** `#finance` `#period-close` `#compliance` `#l10n-be`
