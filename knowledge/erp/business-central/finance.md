# Finance — Business Central (Standard)

> **Scope:** Microsoft Dynamics 365 Business Central (SaaS, current version)
> **Last reviewed:** 2026-07
> **Maintainer note:** Update this file when the vendor releases functional changes to this area.

This file covers the core financial setup of a Business Central implementation: General Ledger Setup, chart of accounts and dimensions, the posting group framework (general, customer/vendor, inventory, VAT), currencies, banking and payment processing, receivables collection terms, and Fixed Assets. Finance setup is in scope for **every** BC implementation — even inventory- or production-led projects — because the posting group framework decides where every operational transaction lands in the G/L. Most of these decisions are cheap to change before go-live and expensive (or impossible) to change after the first posting, so they belong in the earliest design workshops.

---

## General Ledger Setup key choices

**Where:** **General Ledger Setup** page (search: "General Ledger Setup"); per-user overrides on the **User Setup** page.
**What it controls:** Company-wide accounting behaviour: which posting dates are accepted, rounding of amounts and invoices in LCY, dimension defaults, the additional reporting currency, and a set of country-specific fields injected by local functionality (e.g. VAT date handling, reverse-charge fields in the UK version).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Allow Posting From/To left open (blank)** | Data migration phase, small teams with a single bookkeeper who manages period close informally | Any live client — sooner or later someone posts into a closed period and the auditor finds it |
| **Allow Posting From/To maintained monthly at company level, with wider ranges for named users in User Setup** | The standard pattern: lock the company to the current period, give the controller a wider window in **User Setup** for accruals and corrections | Rarely — only skip the User Setup override if literally one person posts |
| **Inv. Rounding Precision/Type at legal default** (e.g. 0.01 / Nearest; 0.05 in CH) | Almost always — set it to what local rules/custom require and forget it. Remember rounding must also be **activated** in Sales & Receivables Setup and Purchases & Payables Setup | Don't invent non-standard rounding; it creates penny differences customers dispute |
| **Additional Reporting Currency (ACY) set at go-live** | Subsidiary of a foreign group that must report in group currency (e.g. EUR LCY, USD group) | If there is no hard dual-currency reporting requirement — this switch is effectively irreversible (see [Currencies and exchange rate handling](#currencies-and-exchange-rate-handling)) |
| **Local functionality fields configured** (VAT date, GST, reverse-charge FastTab, etc.) | Always review them with the client's accountant — the localized version adds fields the generic docs don't show | Never leave localization fields at defaults without review in regulated markets (BE/NL/DE/UK/IT...) |

**Required client info:**
- What is your period-close discipline — who is allowed to post into a prior month, and until when?
- Does a parent company require reporting in a second currency? Is that requirement contractual/statutory or "nice to have"?
- What invoice rounding does local law or trade custom require (e.g. CHF 0.05)?
- Which country localization applies, and does the client's accountant know the local statutory fields (VAT date, Intrastat, e-invoicing hooks)?

**Interactions:** Global Dimension 1 & 2 are defined here — see [Chart of Accounts design](#chart-of-accounts-design). ACY is detailed under [Currencies and exchange rate handling](#currencies-and-exchange-rate-handling). The **Bank Recon. with Auto. Match** field (NA versions) switches the reconciliation UI — see [Bank accounts and payment reconciliation](#bank-accounts-and-payment-reconciliation).

**Add-on impact:** Aptean Food & Beverage ERP adds its own setup pages but does not replace General Ledger Setup; review its posting-relevant setup alongside this page — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Company-level posting range locked to the current month, controller exception in User Setup; legal-default invoice rounding activated in both S&R and P&P Setup; no ACY unless the group demands it in writing.

**Risk of getting it wrong:** medium — posting date ranges and rounding are correctable; the ACY field inside this page is **high-irreversible** (cannot be changed or removed once activated without a new company).

**Expertise tags:** `#finance` `#general-ledger-setup` `#period-close`

---

## Chart of Accounts design

**Where:** **Chart of Accounts** page; **G/L Account Categories** page; **Dimensions** page; global/shortcut dimensions on **General Ledger Setup**.
**What it controls:** The structure of all financial reporting: how many G/L accounts exist, how income statement and balance sheet subtotals are built (account types Posting / Heading / Begin-Total / End-Total / Total), and whether analytical detail lives in accounts or in dimensions.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Lean CoA (200–400 posting accounts) + dimensions for analysis** | The BC-native pattern and the right answer for most clients. Departments, cost centers, projects, product lines go into the 2 global + up to 8 shortcut dimensions, not into account numbers | Clients whose statutory CoA is mandated in detail (e.g. FR PCG, BE MAR-influenced charts) — there you keep the statutory skeleton and still push analysis to dimensions |
| **Detailed CoA replicating the legacy system (one account per department/branch/product)** | Almost never as a design goal. Sometimes tolerated transitionally when the client's accountant refuses change mid-project | Multiplies the [General Posting Setup matrix](#general-posting-setup-matrix), makes financial reports brittle, and defeats BC's dimension analytics. Push back hard |
| **Account categories & subcategories mapped on every posting account** | Always — it powers the built-in Balance Sheet/Income Statement, cash flow chart and financial reporting out of the box | No reason to skip; unmapped accounts silently fall out of the standard statements |
| **Global dimensions chosen for the two highest-value analyses** | Pick the two the client filters on everywhere (typically Department + Cost Center or Branch). Global dimensions are usable as filters on every page and report | Choosing rarely-used dimensions as global — swapping global dimensions later is a heavy batch job on a large database, so choose deliberately |

**Required client info:**
- What management reporting cuts do you actually run monthly (department, branch, product group, project)? Those become dimensions, not accounts.
- Is there a statutory chart of accounts format in your country, and does your external accountant file from BC or from an export?
- How many companies will share this CoA? (Group clients should standardize one CoA + dimension set across companies before company no. 2 is created.)
- Who maintains the CoA after go-live, and do we restrict **Direct Posting** on control accounts (receivables, payables, inventory, VAT, bank)?

**Interactions:** Every posting group decision below maps into this CoA — finalize the CoA first. Dimension design feeds Financial Reports and Analysis Views. Control accounts referenced by [Customer and Vendor Posting Groups](#customer-and-vendor-posting-groups), [Inventory Posting Groups and Inventory Posting Setup](#inventory-posting-groups-and-inventory-posting-setup) and VAT accounts should have **Direct Posting = No**.

**Add-on impact:** Aptean F&B posts through the standard posting-group framework into this CoA; it adds industry transactions (catch weight, commodity settlements) but not a separate ledger — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Lean CoA with statutory numbering where required, full account-category mapping, Department + one client-specific dimension as globals, direct posting blocked on all control accounts.

**Risk of getting it wrong:** medium — accounts can be added and blocked, but renumbering a live CoA and swapping global dimensions after months of entries is disruptive and expensive.

**Expertise tags:** `#finance` `#chart-of-accounts` `#dimensions` `#reporting`

---

## General Posting Setup matrix

**Where:** **Gen. Business Posting Groups**, **Gen. Product Posting Groups**, and the **General Posting Setup** page (the combination matrix).
**What it controls:** For every combination of *who* (Gen. Bus. Posting Group on customers/vendors) × *what* (Gen. Prod. Posting Group on items/resources/G-L lines), which income-statement accounts receive sales, purchases, COGS, discounts, and inventory adjustments. This matrix is the routing table for the entire P&L.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Minimal matrix: 2–4 business groups (e.g. DOMESTIC / EU / EXPORT) × 3–6 product groups (e.g. TRADE, RAW, SERVICES, FREIGHT, MISC)** | Most SMB clients. The P&L only needs revenue/COGS split by a handful of lines; finer analysis belongs in dimensions | Only when the client genuinely posts different combinations to different accounts — not to mirror a reporting wish |
| **Business groups mirroring VAT geography** | Common and convenient: DOMESTIC/EU/EXPORT lets you default VAT Bus. Posting Groups from Gen. Bus. groups on the group card | If revenue accounts don't differ by geography, you can still keep one business group and let VAT groups carry the geography — fewer matrix lines |
| **Large matrix (10+ × 10+) mirroring a detailed CoA** | Legacy-driven; occasionally required by group accounting policy | Every new combination is a line someone must maintain; missing combinations block posting mid-order-entry. Use the **Copy** action and the missing-account notifications, but better: shrink the matrix |
| **Blocked flag on retired combinations** | Always, instead of deleting — combinations with posted entries cannot be safely deleted | — |

**Required client info:**
- Which P&L lines must revenue and COGS split into for statutory and group reporting? (That, and only that, sizes the product group list.)
- Do you sell/buy across VAT borders (domestic/EU/export/import)? Sizes the business group list.
- Are there prepayments, discounts posted separately, or inventory adjustment accounts the accountant wants isolated?

**Interactions:** Revenue/COGS accounts must exist in the [CoA](#chart-of-accounts-design) first. Gen. Bus./Prod. groups can carry default [VAT posting groups](#vat-posting-setup) — align the two structures deliberately. Inventory and COGS interplay depends on [Inventory Posting Setup](#inventory-posting-groups-and-inventory-posting-setup) and the costing method (see inventory.md when written). Customer/vendor cards carry the Gen. Bus. group — changing it on a live card changes future postings only.

**Add-on impact:** Aptean F&B introduces additional item and transaction types (catch weight items, brokerage/commodity flows) that need their own Gen. Prod. Posting Groups and matrix lines — plan the matrix with the add-on consultant; see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** 3 business groups × 4–6 product groups, VAT groups defaulted from them, all combinations filled before UAT, retired lines Blocked rather than deleted.

**Risk of getting it wrong:** medium — wrong accounts are correctable by reclassification and matrix updates going forward, but historical entries stay where they landed; missing combinations halt operations until fixed. Once entries exist, groups/combinations effectively cannot be deleted.

**Expertise tags:** `#finance` `#posting-groups` `#general-posting-setup`

---

## Customer and Vendor Posting Groups

**Where:** **Customer Posting Groups** and **Vendor Posting Groups** pages; assigned on the customer/vendor card; **Allow Multiple Posting Groups** toggle in Sales & Receivables / Purchases & Payables Setup and on the posting group pages.
**What it controls:** The balance-sheet control accounts for receivables and payables, plus accounts for payment discounts, payment tolerance, service charges, interest/fees from reminders, invoice rounding, and currency application rounding.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **One customer group / one vendor group** | Clients with a single receivables and single payables control account — perfectly respectable for most SMBs | Only if the balance sheet must split AR/AP (see next row) |
| **Few groups split by balance-sheet requirement (e.g. DOMESTIC/FOREIGN, TRADE/INTERCOMPANY)** | Statutory or group reporting requires separate control accounts (intercompany AR/AP is the classic case) | Don't create groups for analysis you could do with dimensions or customer groups — every group is a control account to reconcile |
| **Allow Multiple Posting Groups = on** | Niche: markets/clients where the same counterparty's entries must hit different control accounts per document (some localizations, factoring scenarios) | Leave off by default — it lets users pick posting groups on documents, which is a reconciliation and audit surface you usually don't want |

**Required client info:**
- Does the balance sheet (statutory or group) require more than one AR/AP control account? Which splits — intercompany, foreign, employees-as-vendors?
- Do you charge interest/fees on late payers (accounts for reminder fees live here)?
- Do you use invoice rounding or payment tolerance? Those accounts must be filled per group.

**Interactions:** Control accounts should be **Direct Posting = No** in the [CoA](#chart-of-accounts-design). Reminder/finance-charge fee accounts connect to [Payment terms, payment methods, reminders and finance charges](#payment-terms-payment-methods-reminders-and-finance-charges). Invoice rounding accounts require a VAT Prod. Posting Group on the rounding G/L account — see [VAT Posting Setup](#vat-posting-setup). Changing the posting group on a customer/vendor card moves only *future* entries; open entries stay on the old control account, so migrate/re-group before go-live, not after.

**Add-on impact:** None known beyond standard use; Aptean F&B counterparties (growers, brokers) use standard customer/vendor posting groups — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** One TRADE group each for customers and vendors, plus INTERCOMPANY groups when the client has group companies; Allow Multiple Posting Groups off.

**Risk of getting it wrong:** medium — regrouping mid-life leaves open entries on the old control account and makes AR/AP-to-G/L reconciliation painful; groups with posted entries cannot be deleted.

**Expertise tags:** `#finance` `#receivables` `#payables` `#posting-groups`

---

## Inventory Posting Groups and Inventory Posting Setup

**Where:** **Inventory Posting Groups** page; **Inventory Posting Setup** page (group × location matrix); interacts with **Inventory Setup** (Automatic Cost Posting, Expected Cost Posting to G/L).
**What it controls:** Which balance-sheet inventory (and WIP) accounts item value entries post to, per combination of inventory posting group (on the item card) and location. This is the balance-sheet counterpart of the COGS/purchase accounts in the [General Posting Setup matrix](#general-posting-setup-matrix).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Groups by inventory type on the balance sheet (RAW, WIP/SEMI, FINISHED, PACKAGING, GOODS)** | Manufacturers and food processors — mirrors how the accountant wants inventory valued and disclosed | Don't proliferate groups for warehouse analysis; location is already a dimension of the matrix, and item categories handle analytics |
| **Single group for all items** | Pure trading companies with one inventory line on the balance sheet | Any client with raw/finished split or production — you can't split the balance sheet later without revaluing history |
| **Per-location account splits in the matrix** | Only when locations are separate legal/reporting units of inventory value (e.g. consignment at customer, goods at external processor) | Same accounts for every location is normal; filling different accounts per location "because we can" multiplies reconciliation work |
| **Expected Cost Posting to G/L = on** | Clients who want received-not-invoiced inventory visible in the G/L (interim accounts) — auditors often like it | Adds interim accounts to reconcile; skip for simple clients who close AP quickly |

**Required client info:**
- How does your balance sheet split inventory (raw / WIP / finished / goods for resale)?
- Do you hold stock at third parties or on consignment, and must it be a separate G/L account?
- Do you need received-not-invoiced visible in the G/L (expected cost), and will you run Adjust Cost / post inventory cost to G/L automatically or as a period task?

**Interactions:** Item card carries both the inventory posting group (balance sheet) and the Gen. Prod. Posting Group (P&L) — design them together. Costing method and cost adjustment cadence (inventory.md, when written) determine when these accounts are correct, not just where amounts land. Production/assembly requires WIP accounts in this matrix. Do not change an item's inventory posting group once it has value entries — regroup via inventory write-down/journal instead.

**Add-on impact:** This is the area Aptean F&B touches most: catch-weight, lot cost adjustments, and commodity flows all post through inventory posting setup, and Aptean prescribes additional groups/accounts — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Groups mirroring the balance-sheet inventory split, identical accounts across locations unless a location is a distinct reporting unit, Expected Cost Posting on for clients with meaningful goods-received-not-invoiced volume.

**Risk of getting it wrong:** high — inventory G/L-to-subledger reconciliation is the classic BC post-go-live firefight; changing groups on items with posted value entries corrupts the reconciliation trail and is effectively irreversible without revaluation exercises.

**Expertise tags:** `#finance` `#inventory` `#posting-groups` `#costing`

---

## VAT Posting Setup

**Where:** **VAT Business Posting Groups**, **VAT Product Posting Groups**, **VAT Posting Setup** (combination matrix); defaults assignable from Gen. Bus./Prod. groups and customer/vendor/item templates.
**What it controls:** VAT calculation and posting for every transaction: VAT %, **VAT Calculation Type** (Normal VAT, Reverse Charge VAT, Full VAT, Sales Tax), the sales/purchase/reverse-charge VAT accounts, VAT Identifier grouping, EU Service flag, and unrealized VAT handling. Feeds the VAT statement and VAT return.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Bus. groups by geography (DOMESTIC / EU / EXPORT / IMPORT), Prod. groups by rate (STANDARD / REDUCED / ZERO / NO-VAT)** | The canonical EU design. Name product groups by rate meaning, not the % itself if rates change often; use **VAT Identifier** per rate | Non-VAT jurisdictions (US: Sales Tax engine instead); don't encode customer industry into VAT groups |
| **Reverse Charge VAT lines for EU B2B purchases (and mirrored for EU sales)** | Mandatory for intra-EU trade: purchase VAT is calculated and simultaneously offset via the Reverse Chrg. VAT account; EU sales post no VAT but report separately. Set the customer's VAT Registration No. and mark **EU Service** for services combos | Using Normal VAT for EU purchases — the VAT return will be wrong, and corrections are posted-document surgery |
| **Full VAT combination for import VAT** | Clients importing goods who receive a VAT-only invoice from customs/forwarder — a dedicated Prod. group with Calculation Type Full VAT posts 100% of the line as VAT | Don't abuse Full VAT for normal corrections; keep it to the import-VAT flow |
| **Unrealized VAT** | Jurisdictions/schemes where VAT is due on payment (cash accounting) — enable in G/L Setup and configure per combination | Leave off otherwise; it complicates application/unapplication of entries |

**Required client info:**
- Which VAT registrations does the company hold, and in which countries? Any OSS/IOSS?
- Which rates apply to the product range (standard/reduced/zero/exempt), and are any items rate-ambiguous (food industry is full of these)?
- Intra-EU purchases and sales? Services vs goods split (EU Service flag, Intrastat/Service Declaration)?
- Cash-accounting VAT scheme? Import flows with postponed accounting or customs-agent VAT invoices?

**Interactions:** The localized country version adds fields and statement formats — always configure with the localization, not the generic W1 picture, and validate against the [General Ledger Setup](#general-ledger-setup-key-choices) VAT/localization fields. VAT groups default from [General Posting Setup](#general-posting-setup-matrix) groups if you wire them. Invoice rounding accounts need a VAT Prod. group ([Customer and Vendor Posting Groups](#customer-and-vendor-posting-groups)). VAT entries also carry ACY amounts once an [additional reporting currency](#currencies-and-exchange-rate-handling) is active.

**Add-on impact:** None fundamental — Aptean F&B transactions use standard VAT posting setup; verify new item types get correct VAT Prod. groups — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Geography × rate matrix with VAT Identifiers per rate, reverse-charge combos for EU trade, a Full VAT import combo, and the whole matrix reviewed line-by-line with the client's tax advisor before the first posting.

**Risk of getting it wrong:** high — wrong VAT calculation type or % produces incorrect VAT returns and legally sensitive corrections; combinations with posted entries can't be deleted, and fixing history means credit/re-invoice or manual VAT-entry corrections.

**Expertise tags:** `#finance` `#vat` `#tax` `#posting-groups` `#localization`

---

## Currencies and exchange rate handling

**Where:** **Currencies** page (with per-currency gain/loss and rounding accounts); **Currency Exchange Rates** + update service; **General Ledger Setup → Additional Reporting Currency**; LCY is implicit (blank currency code) and set by company creation/localization.
**What it controls:** Which foreign currencies can appear on documents and bank accounts, how exchange rates are maintained, where realized/unrealized FX gains and losses post (Adjust Exchange Rates), and whether every ledger entry additionally carries an ACY amount.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **LCY = statutory currency of the legal entity** | Always. LCY is the functional/booking currency; it is fixed at company setup and not changeable later — a wrong LCY means a new company | — |
| **Foreign currencies with automated rate service + periodic Adjust Exchange Rates** | Any client invoicing or paying in foreign currency. Configure realized + unrealized gain/loss accounts per currency and schedule the adjustment monthly | Clients with zero FX exposure — don't set up currencies "just in case"; each one needs accounts and rate maintenance |
| **Additional Reporting Currency (ACY)** | Hard requirement to report every G/L, VAT, value and project entry in a second currency (foreign parent). Activation runs a batch that converts all history at one rate | **Flag clearly to the client: once activated, ACY cannot be turned off or changed** — and historical conversion at a single rate is an approximation auditors must accept. If the need is only periodic group reporting, a consolidation company or BI-layer translation is usually the better, reversible answer |
| **Application between currencies (S&R / P&P Setup: None / EMU / All)** | Clients who receive EUR payments against USD invoices etc. — set to All and fill the currency application rounding accounts on customer/vendor posting groups | Leave at None for simple clients; cross-currency application creates rounding entries someone must understand |

**Required client info:**
- What is the statutory currency of the entity (LCY), signed off by the accountant before company creation?
- Which currencies do you actually invoice, purchase, and bank in?
- Does the parent require full dual-currency ledgers (ACY) or just translated reports (consolidation/BI)?
- Who maintains rates — ECB feed via the exchange-rate service, or group-issued monthly rates?

**Interactions:** ACY lives on [General Ledger Setup](#general-ledger-setup-key-choices) and stamps VAT entries, value entries and project ledgers. Per-currency invoice rounding fields override G/L Setup rounding. Foreign-currency bank accounts lock their currency after first posting — see [Bank accounts and payment reconciliation](#bank-accounts-and-payment-reconciliation). Residual ACY rounding posts to accounts on the Currencies page — they must exist in the [CoA](#chart-of-accounts-design).

**Add-on impact:** None known — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md) if commodity pricing in foreign currency is in scope.

**Default recommendation:** LCY = statutory currency, only genuinely-used currencies configured with an automated rate feed and monthly adjustment, no ACY unless the group mandate is written and understood as permanent.

**Risk of getting it wrong:** high-irreversible — LCY cannot be changed after company creation, and ACY cannot be deactivated or switched once enabled; everything else here is medium.

**Expertise tags:** `#finance` `#currency` `#multicurrency` `#consolidation`

---

## Bank accounts and payment reconciliation

**Where:** **Bank Account Card** (posting group, currency, statement import format, payment export format, IBAN, Credit Transfer Msg. Nos.); **Bank Acc. Reconciliation** page; **Payment Reconciliation Journal** + **Payment Application Rules**; **General Journal Batches** (Allow Payment Export); Data Exchange Framework for formats.
**What it controls:** How company bank accounts map to G/L (Bank Account Posting Groups), how statements come in (CAMT/CSV/AMC Banking/bank feeds), which page reconciles them, and how outgoing payments leave (SEPA Credit Transfer pain.001, SEPA Direct Debit, or local formats).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Bank Acc. Reconciliation page (statement import + auto-match)** | The default reconciliation flow: import CAMT/CSV, auto-match against bank ledger entries, post the reconciliation. Keep one bank G/L account per bank account, Direct Posting = No | NA clients preferring the check-oriented **Bank Rec. Worksheet** (toggle **Bank Recon. with Auto. Match** off in G/L Setup — no file import there) |
| **Payment Reconciliation Journal as the daily cash-application workbench** | Clients who want one step: import statement, auto-apply customer/vendor payments via application rules and text-to-account mapping, post + reconcile together | Heavily manual-cash businesses or messy remittance data — review effort per line can exceed classic cash receipt journals; also don't run it *and* separate reconciliation without agreeing which one closes the bank ledger entries |
| **SEPA Credit Transfer export from Payment Journal** | Eurozone vendors/payroll: set Payment Export Format (pain.001.001.03 or .09) on the bank account, vendor bank accounts with IBAN, Allow Payment Export on the journal batch | Non-SEPA banks/formats — use AMC Banking 365 extension or a Data Exchange Definition instead of hand-building XML |
| **SEPA Direct Debit collections** | Clients collecting from EUR customers with signed mandates: payment method + direct-debit mandates per customer, export pain.008 from Direct Debit Collections | B2C/one-off customers without mandate discipline; failed collections create manual rejection handling |
| **Bank feeds (Envestnet Yodlee / open-banking apps)** | Small clients in supported countries who want statement lines without file handling | Availability is country/bank-dependent; treasury-grade clients should stay on bank-delivered CAMT files |

**Required client info:**
- Which banks and accounts, in which currencies, and what statement format can each bank deliver (CAMT.053? CSV only?)
- Expected daily volume of incoming payments and quality of remittance references (structured references make auto-apply shine)
- How are vendors paid today — file upload to bank portal, and in which format? SEPA-only or international (then AMC/DEF work is in scope)?
- Who reconciles, how often, and do they also do cash application (one role → Payment Reconciliation Journal; split roles → separate flows)?

**Required client info addendum:** collect IBANs/BICs and mandate data early — chasing them at UAT delays payment testing.

**Interactions:** Bank Account Posting Groups map to G/L accounts in the [CoA](#chart-of-accounts-design) (Direct Posting off). Foreign-currency bank accounts depend on [Currencies](#currencies-and-exchange-rate-handling). Payment methods carry the Pmt. Export Line Definition — see [Payment terms, payment methods, reminders and finance charges](#payment-terms-payment-methods-reminders-and-finance-charges). The NA worksheet toggle lives in [General Ledger Setup](#general-ledger-setup-key-choices).

**Add-on impact:** None known specific to banking — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** One bank G/L account per bank account with a dedicated posting group; CAMT import + Payment Reconciliation Journal for cash application where reference quality allows; SEPA CT for outgoing payments in the Eurozone, AMC Banking for the rest.

**Risk of getting it wrong:** medium — reconciliation method and formats are changeable, but a bank account's currency locks after posting, and a sloppy first reconciliation (wrong statement ending balance/date) haunts every later statement.

**Expertise tags:** `#finance` `#banking` `#payments` `#sepa` `#reconciliation`

---

## Payment terms, payment methods, reminders and finance charges

**Where:** **Payment Terms**, **Payment Methods**, **Reminder Terms** (+ levels and customer communication texts), **Finance Charge Terms** pages; assigned on customer/vendor cards.
**What it controls:** Due-date and payment-discount calculation (date formulas on payment terms, calculated from *document date*), how payments are executed (payment method, optional balancing account for cash/COD, Pmt. Export Line Definition for file export, direct-debit flag), and the collections ladder (reminder levels with grace periods, fees, interest; finance charge memos with Average Daily Balance or Balance Due interest).

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **Small shared set of payment terms with date formulas (e.g. 14D, 30D, CM+10D, 8D-2%)** | Always — same list serves sales and purchases; discounts calculate automatically on posting | Per-customer bespoke terms proliferation; also remember due dates run from document date, so back-dated invoices shorten payment windows |
| **Payment methods with blank balancing account (BANK) + export line definition** | Standard for invoice-then-pay flows and SEPA export | — |
| **Payment method with Bal. Account filled (CASH/COD)** | Cash sales, card-settled POS-like flows: the invoice posts as paid in one step | Never on account-customers — it silently closes the invoice against the balancing account and AR ages nothing |
| **Reminder terms with 2–3 levels, grace periods and level-specific texts (multi-language where needed), automated via reminder automation** | Any client that actually chases debtors; automation (create/issue/send) removes the monthly manual grind | Clients with key-account-managed receivables may exempt specific customers — leave the Reminder Terms Code blank for them rather than never issuing |
| **Finance Charge Terms (Average Daily Balance vs Balance Due)** | Clients that contractually charge late interest; pick the method matching contract wording; link interest calculation into reminder levels where wanted | Most SMBs configure it and never issue a memo — don't build elaborate interest setups without a business owner for collections |

**Required client info:**
- Standard terms offered to customers and received from vendors (including discount arrangements worth automating)?
- Do you take cash/immediate payments that should auto-close (COD)?
- Collections policy: how many chasers, at what intervals, with fees/interest? Who signs off before a reminder actually goes to a customer?
- Multi-language customer base (reminder texts per language)?

**Interactions:** Reminder/finance-charge fee and interest accounts come from [Customer Posting Groups](#customer-and-vendor-posting-groups). Payment methods connect to SEPA export and direct-debit mandates — see [Bank accounts and payment reconciliation](#bank-accounts-and-payment-reconciliation). Payment discounts can interact with VAT recalculation settings in [VAT Posting Setup](#vat-posting-setup) (Adjust for Payment Discount).

**Add-on impact:** None known — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Lean shared payment-terms list with date formulas; BANK payment method with export definition as default; 3-level reminder terms with grace periods and automation configured but issuance kept behind a human review at go-live.

**Risk of getting it wrong:** low — all of this is changeable at any time; the real risks are operational (COD method on account customers, reminders auto-sent to strategic accounts).

**Expertise tags:** `#finance` `#receivables` `#collections` `#payment-terms`

---

## Fixed Assets setup

**Where:** **Fixed Assets Setup**, **Depreciation Books** (Integration FastTab), **FA Posting Groups**, FA classes/subclasses/locations; FA G/L Journal vs FA Journal.
**What it controls:** Whether and how FA transactions hit the G/L (per depreciation book G/L integration switches), which accounts acquisition/depreciation/disposal/write-down post to (FA posting groups), and which depreciation methods and books (accounting vs tax) apply.

**Options:**

| Option | When it fits | When to avoid |
|---|---|---|
| **One G/L-integrated depreciation book (COMPANY), straight-line, monthly Calculate Depreciation batch** | The default for the vast majority of clients | — |
| **Second non-integrated TAX book (+ duplication list)** | Jurisdictions with divergent tax depreciation (declining balance, accelerated regimes) — entries duplicate from the accounting book without touching the G/L | Skip when tax = accounting depreciation; every extra book is maintenance |
| **FA posting groups per balance-sheet asset class (BUILDINGS, MACHINERY, VEHICLES, IT, ...)** | Always — mirrors statutory disclosure; fill balancing accounts so **Insert FA Bal. Account** works | Fine-grained groups per asset are pointless; the FA card itself is the analysis level |
| **No G/L integration (memo FA ledger only)** | Rare: asset registers kept outside the ledger, or pre-go-live loading phase | As a permanent state for a client whose balance sheet must show assets — defeats the module |

**Migration note:** load opening balances with **all** Integration toggles off (acquisition + accumulated depreciation via FA Journal), then switch integration on — loading with integration active double-posts to the G/L.

**Required client info:**
- Asset classes on the balance sheet, useful lives, and the depreciation method(s) per class (accounting and tax)?
- Is a separate tax book legally required, and does the accountant want it in BC or in their tax software?
- Volume and source of the opening asset register (fixed asset migration is its own workstream).

**Interactions:** FA posting group accounts live in the [CoA](#chart-of-accounts-design); depreciation rounding should align with [G/L Setup invoice rounding](#general-ledger-setup-key-choices) to avoid disposal rounding errors. Acquisitions via purchase invoices flow through [vendor posting groups](#customer-and-vendor-posting-groups) and VAT setup.

**Add-on impact:** None known — see [Aptean F&B — Overview](../../addons/aptean-food-beverage/overview.md).

**Default recommendation:** Single integrated book, straight-line, FA posting groups per statutory asset class; add a non-integrated tax book only on the accountant's explicit requirement.

**Risk of getting it wrong:** medium — books and groups can be corrected, but opening-balance loads with integration wrongly enabled, or depreciation posted with wrong methods for months, mean tedious FA ledger corrections (cancel/reverse FA entries) rather than simple reclassifications.

**Expertise tags:** `#finance` `#fixed-assets` `#depreciation`
