# Decision pack: what is new in Word and Excel layouts (BC, 15 minutes)

18 November 2026 · prepared for Olivia · demo environment 28.5 · version 29 sandbox: assumed NO

How to read this: every feature below survived the verifier (`research/verification.md`). Claims it marked UNVERIFIED or WRONG are dropped from the tables and listed in section 8. Scores are my proposal, harsh by design; overrule any of them. **You pick the features.**

Scoring: Total = value×8 + breadth×4 + demo×5 + readiness×3 (max 100). Include = fits its time block in score order. Backup = 60 or more but no room, or below 60 but worth one line on a backup slide. Cut = not presented.

---

## 1. Word layouts (version 29 only)

All in-scope items are listed as generally available in What's new 29.0. Important for the whole block: the composite features (themes, header/footer) only work after an admin turns on **New Document Report Experience** in Feature Management. It is **off by default** in version 29.

| # | Feature | What it does | Value for users | Value for decision-makers | Value | Breadth | Demo | Ready | Total | Decision | Sources |
|---|---|---|---|---|---|---|---|---|---|---|---|
| W1 | Conditional visibility in the Word add-in (573329) | "Hide if empty" controls hide a zero field, an empty table, row or column at print time | Remove an always-empty discount column yourself, no developer | Cleaner customer documents without paid layout work per customer | 4 | 4 | 5 | 4 | **85** | Include | [What's new 29.0](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-29-0), [Word add-in](https://learn.microsoft.com/en-us/dynamics365/business-central/ui-design-word-layouts-business-central-add-in) |
| W2 | Reusable header/footer layouts (573331 design + 573326 reuse) | Header/footer becomes one separate Word file used by all document reports; defaults per company, report or layout | Change logo or address once instead of in every layout | One controlled place for brand and legal footer; per-company branding without cloning layouts | 4 | 4 | 4 | 2 | **74** | Include | [Themes and header/footer](https://learn.microsoft.com/en-us/dynamics365/business-central/ui-set-up-report-themes-header-footer-layouts), What's new 29.0 |
| W3 | Report themes (573330 design + 573327 branding) | A .dotx theme holds fonts, colours and styles for all document layouts | Restyle all documents by swapping one file | Consistent brand across invoice, quote, credit memo; lower maintenance | 3 | 3 | 4 | 2 | **62** | Include | Same as W2 |
| W4 | New or replaced layouts start as Draft (v29 increment of 573320) | After upload or replace, a layout is Draft until someone approves it | No half-finished layout appears in the list | Test-then-approve habit on every customer-facing document | 3 | 4 | 3 | 5 | **70** | Include, **but in the Excel block** (demo step 10); applies to all layout types | [Excel layouts](https://learn.microsoft.com/en-us/dynamics365/business-central/ui-excel-report-layouts), Word add-in |
| W5 | AL items: Subtype, DefaultThemePart, DefaultHeaderFooterPart, runtime 18 compiler | Developer plumbing for composite layouts | None directly | Partner effort only | 1 | 1 | 1 | 2 | 23 | Cut | [Layout declaration in AL](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-report-layout-declaration) |

Score reasons (one sentence each):
- W1: removes a typical developer request (hide empty columns) and reads instantly from one before/after picture; readiness 4 because it needs the add-in.
- W2: a rebrand or address change today means editing every layout, and this fixes that; readiness 2 because the feature switch is off by default and only "Body" layouts can use parts.
- W3: mostly cosmetic unless the client runs several brands, same switch caveat as W2.
- W4: low effort, high governance value, but it needs a sentence of explanation and overlaps with the version 28 statuses, so it belongs in the Excel lifecycle story.
- W5: not for this audience.

**Do NOT show as new in 29** (verifier: wrong scope):
| Item | Actually shipped |
|---|---|
| Add Data task pane in the Word add-in (fields, labels, report info, Add field) | 2025 wave 2, v27 ([release plan](https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/smb/dynamics365-business-central/add-data-fields-report-layouts-using-word-add-in)) |
| Enhanced add-in editing, Insert Table | 2026 wave 1, v28 ([release plan](https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/get-easier-editing-document-report-layouts-enhanced-word-add-in)) |
| Layout statuses Draft / Pending Approval / Approved / Retired | 2026 wave 1, v28 ([release plan](https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/control-lifecycle-report-layouts)) |
| ReportMetadata / ReportRequest data items | 2025 wave 1, v26 |
| Sales document layouts showing carbon footprint (ESG) | 2026 wave 1, v28 |

Two v29 titles are not presentable: "Design document reports with the updated Word add-in" (573328) and "Reduce complexity of report datasets" (573321). Only the titles are on Learn, so what they add is UNKNOWN (section 8).

## 2. Word screenshot shot list

Problem first: **you cannot capture any of these in 28.5**, and **no opened source has a screenshot of any v29 Word feature**. The community sources (yzhums.com, mc.merill.net) were blocked from this session, so they are unchecked. So option B from the plan (published screenshots) currently has nothing to offer. Without a v29 sandbox the Word block is text-only. See open question 1.

| Feature | Screen | Highlight | Before/after | Capture |
|---|---|---|---|---|
| W1 | Word, Business Central ribbon tab, **Hide if empty** dropdown open on a sales invoice layout | The four controls (Hide Field if Zero, Hide Empty Table / Row / Column) | Yes: invoice PDF with an all-empty Discount % column vs the same invoice without it | Own, v29 sandbox only |
| W2 | BC page **Report defaults for theme and header-footer** with a global row and one company row | "Applies to" column and the Header/Footer part | Optional: two documents (invoice, quote) with the same new footer | Own, v29 sandbox, after enabling New Document Report Experience |
| W2 (alt) | **Company Information**, Reporting FastTab | Default Header/Footer and Default Theme fields | n/a | Own, v29 sandbox |
| W3 | Report Layouts, Details FactBox on a Body layout | Theme and Theme source fields | Yes: same invoice PDF with the old vs new theme (font and colour) | Own, v29 sandbox |
| Feature switch | **Feature Management**, "New Document Report Experience" row | "Enabled for" = None by default | n/a | Own, v29 sandbox |

## 3. Excel layouts (versions 26 to 29)

"Demoable" = shown live in your 28.5 environment. Capabilities (C) work in any report. Content (K) = Microsoft-shipped reports with new or improved Excel layouts.

| # | Feature | Type | Introduced | Demoable in 28.5 | What it does | Value for users | Value for decision-makers | Value | Breadth | Demo | Ready | Total | Decision | Sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X1 | Layout lifecycle statuses (Draft, Pending Approval, Approved, Retired) | C | v28 (GA 1 May 2026) | Yes | Only Approved layouts can be picked on the request page | Only see layouts that were tested | Nobody runs an untested layout; approval step without a developer | 4 | 4 | 4 | 5 | **83** | Include (live) | [Release plan](https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/control-lifecycle-report-layouts), [Get started with layouts](https://learn.microsoft.com/en-us/dynamics365/business-central/ui-get-started-layouts) |
| X2 | Standard reports moved from RDL to Excel layouts | K | v26 to v28 | Yes (report 113) | About 37 standard reports now ship with an Excel layout: finance (trial balances, aged AR/AP, fixed assets), sales (10), deferrals (3), inventory (8 incl. 719), manufacturing (3), sustainability (3) | Analysis-ready workbook from a standard report, no export-and-rebuild | Less custom report work; customisations move from developer to key user | 4 | 4 | 4 | 5 | **83** | Include (live, as framing) | Release plans [2025w1 finance](https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-enhanced-analytics-finance), [2025w2 sales](https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/smb/dynamics365-business-central/use-enhanced-sales-analytics), [2026w1 inventory](https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/modernizing-analytical-reports-inventory) |
| X3 | Subtotals in Excel layouts of sales and deferral reports | K | v28 (GA 1 Apr / 1 May 2026) | Yes (to confirm in dry run) | Reports 113, 115, 708, 713, 718 and deferral 1700-1702 now have subtotals built in | No more adding subtotals by hand every month | Faster month-end reconciliation | 3 | 4 | 5 | 5 | **80** | Include (live) | [Release plan sales](https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/analyze-customer-loyalty-other-sales-scenarios), [deferrals](https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/use-enhanced-faster-reports-analysis-deferrals-trial-balances) |
| X4 | Validate a layout | C | v26 (GA 1 Apr 2025) | Yes | Admin checks an uploaded layout and gets an error list | Fewer broken reports after an upload | Less support time; no developer to diagnose a bad file | 3 | 3 | 4 | 5 | **71** | Include (live) | [Release plan](https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/validate-report-layouts-errors-as-admin), Get started with layouts |
| X5 | New or replaced layouts start as Draft (= W4) | C | v29 | No, slide only | See W4 | See W4 | See W4 | 3 | 4 | 3 | 5 | **70** | Include (slide, demo step 10) | [Excel layouts](https://learn.microsoft.com/en-us/dynamics365/business-central/ui-excel-report-layouts) |
| X6 | Faster Trial Balance Excel reports | K | v28 (feature switch, on by default) | Not visible | Performance only | Shorter waits | None visible | 3 | 4 | 1 | 4 | 57 | Backup (one line) | Release plan deferrals/trial balance, [mandatory features](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/feature-management-mandatory-features) |
| X7 | Multiple data sheets set per layout | C | v26 (per-layout override; global property is older) | Not with 113 | One data sheet per data item, for Power Pivot models | Pivot across several tables | Richer reports without breaking old layouts | 3 | 2 | 2 | 2 | 48 | Backup | [Excel layout dev guide](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-howto-excel-report-layout) |
| X8 | Mark layout as obsolete | C | v26 (AL property; client toggle version unknown) | Check in dry run | Flags a layout as deprecated | Clear "stop using this" signal | Smoother clean-up | 2 | 2 | 3 | 3 | 48 | Backup | [Release plan](https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-new-properties-report-layout) |
| X9 | Layout name/caption/ID in workbook metadata | C | v26.0 | Hidden sheet | Workbook knows which layout produced it | Trace a file to its layout | Audit trail | 1 | 2 | 1 | 4 | 33 | Cut | Excel layout dev guide |
| X10 | Portable layout paths in AL (runtime 18) | C | v29 | No | Developer build convenience | None | None | 1 | 1 | 1 | 2 | 23 | Cut | Layout declaration in AL |

Score reasons:
- X1: real governance gain with no developer, two clicks live; it's v28, so it's in scope for Excel but not for Word.
- X2: the biggest Excel story by volume, but it's content, so frame it as "your standard reports already got this" rather than as a feature.
- X3: instantly visible in the workbook, but saves minutes rather than hours.
- X4: valuable only to clients who customise layouts, and quick to show.
- X5: see W4.
- X6: a real gain, but nothing to see on screen.
- X7: needs developer work first.
- X8: low value, and it's unclear whether the toggle exists in 28.5.
- X9, X10: not for this audience.

Count per wave (verified): v26: 4 capabilities, 13 reports · v27: 0 capabilities, 16 reports · v28: 1 capability, 21 report entries · v29: 2 capabilities (1 developer-only), 0 reports.

## 4. Why Excel layouts (one slide, 1.5 minutes)

Corrected comparison. The "offline use" row is dropped (inference only), and cells the verifier could not confirm are reworded or marked.

| Criterion | Excel layouts | Analysis mode | Power BI |
|---|---|---|---|
| Who builds it | Key user or consultant in Excel; AL for packaged ones | End user drags fields; no build | Apps: install; custom: Power BI Desktop skills |
| Who maintains | Layout owner; statuses (v28), Draft on upload (v29) | Each user, own views | Workspace admin; app updates can overwrite edits |
| Extra licence | None stated | Permission set DATA ANALYSIS - EXEC | Power BI Pro per viewer, or Premium/Fabric |
| Freshness | Snapshot at run time | Live when opened | Last refresh; 8/day shared, 48 Premium |
| Volume | Up to 10M rows, 12 h (online max) | Large-data mode above 100,000 rows | Refresh under 2 h shared; 8 min call limit |
| Combining data | Report dataset; several data sheets possible | Related-table fields since 26.2 | Many APIs; cross-company via Power Query |
| Printing / fixed layout | Download, then print from Excel | Not stated on Learn | Not stated on Learn |
| Scheduling | Job queue to Report Inbox | None found | Scheduled data refresh |
| Sharing | Layout per company or all companies | Views private; share a link | Licence per viewer; one app per company |
| Run-time filters | Request page plus slicers in workbook | Column filters per view | Slicers; environment and company parameters |
| Governance | BC permissions plus Excel protection and labels | Admin can withhold the permission set | Workspace access plus BC read permission |
| Fit with Excel habits | Highest: formulas, pivots, slicers | Pivot-like, not Excel | Separate tool (opinion) |

Sources: [Excel layouts](https://learn.microsoft.com/en-us/dynamics365/business-central/ui-excel-report-layouts), [Run reports](https://learn.microsoft.com/en-us/dynamics365/business-central/ui-work-report), [Analysis mode](https://learn.microsoft.com/en-us/dynamics365/business-central/analysis-mode), [Install Power BI apps](https://learn.microsoft.com/en-us/dynamics365/business-central/across-powerbi-install-business-central-apps), [Power BI refresh](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-data), [BC as Power BI source](https://learn.microsoft.com/en-us/dynamics365/business-central/across-how-use-financials-data-source-powerbi). Full detail in `research/comparison.md`.

**Say this:** "Excel layouts sit in the middle: more finished and repeatable than analysis mode, which is a quick look you build yourself, but lighter and cheaper than Power BI, which is a separate dashboard tool with its own licences and refresh schedule."

**When Excel layouts are the wrong choice:**
- Customer-facing or print-perfect documents: use Word (Excel has no Print or Preview button, and email layouts must be Word).
- A one-off question: analysis mode is faster.
- An always-on dashboard for many viewers, or cross-company consolidation: Power BI.
- Scheduled email delivery to many people: not documented for Excel output, so don't promise it.

## 5. Demo report: Customer/Item Sales (113)

**Why:** its Excel layout exists since v27 and its subtotals since v28, so both are in 28.5. Sales per customer and item speaks to finance and operations alike. It is also the only candidate that shows a v28 change live. Fallbacks: Trial Balance Excel (4405), then Aged Accounts Receivable Excel (4402). Steps 6 to 10 stay identical.

**Use case to open with:** a sales controller at a distribution company runs this monthly after closing. In Excel they filter the top customers, check discount against profit per item, add a comment column and send it on. The subtotals now come built in. Admin angle: one approved copy of the layout, nobody runs an untested one. (Illustrative, not a real client.)

| # | Time | Action | Say |
|---|---|---|---|
| 1 | 0:40 | Alt+Q "Customer/Item Sales"; set Posting Date to a range you checked; narrow Item No. | Run-time filters, no developer |
| 2 | 0:25 | Pick the Excel layout, run (opens in Excel online if OneDrive is set up) | Same data, Excel instead of the old RDL (X2) |
| 3 | 0:55 | Show the print sheet, then the analysis sheet; point at subtotals per customer | v28: subtotals built in (X3) |
| 4 | 0:35 | Use a slicer or filter, collapse a group | What Excel users already know, on BC data |
| 5 | 0:15 | Flash the raw data sheet, close | The data is there for your own formulas and pivots |
| 6 | 0:25 | Search Report Layouts, filter report 113, point at the status column | One page for all layouts |
| 7 | 0:35 | Select the Excel layout, Edit Info, new name, Save Changes to Copy | A user-defined copy; the Microsoft original stays untouched |
| 8 | 0:25 | Select the copy, Validate, show result | v26: check a layout without a developer (X4) |
| 9 | 0:40 | Layout > Layout Status > Set Pending Approval, show it is gone from the request page, then Set Approved | v28: only approved layouts reach users (X1) |
| 10 | 0:35 | Slide | v29: every new or replaced layout starts as Draft (X5/W4) |
| | **5:30** | | |

If time runs short, drop step 5. Changed from the research file: step 5 no longer claims the report page mentions Copilot (verifier correction), and the obsolete toggle is dropped (backup, score 48).

**Dry run in 28.5 before the day (15 minutes):** (1) report 113 returns rows and shows subtotals; (2) the analysis sheet has a slicer or pivot; (3) which status a fresh copy starts with; (4) Pending Approval really hides the copy from the request page; (5) take a backup screenshot of every step.

## 6. Run of show (15:00)

| Block | Time | Content | Features |
|---|---|---|---|
| Opening | 1:00 | Layouts = reports users change themselves. Two news blocks: Word (v29) and Excel (v26 to v29) | — |
| Word | 5:00 | 0:20 framing · 1:40 hide-if-empty, before/after invoice (W1) · 1:40 one header/footer for all documents, defaults page (W2) · 0:50 themes, before/after PDF (W3) · 0:30 "off by default: an admin enables New Document Report Experience" | W1 85, W2 74, W3 62 |
| Why Excel | 1:30 | Comparison slide plus the one-liner; one line on when not to use it | Section 4 |
| Excel demo | 5:30 | Report 113 path, section 5 | X2 83, X1 83, X3 80, X4 71, X5 70 (slide) |
| Close | 2:00 | Monday: (1) plan the v29 update and enable the document feature in a sandbox; (2) list invoice layouts with empty columns or duplicated headers; (3) switch users to the Excel versions of standard reports and set layout statuses. Questions | — |

Backup slide: X6 faster trial balances, X7 multiple data sheets, X8 obsolete flag, the "Do NOT show as new" table.

Word timing holds only with screenshots. Without a v29 sandbox, cut the Word block to 3:00 and give 2:00 to the Excel demo or to questions.

## 7. How-it-works sources per included feature

Blogs: none listed. yzhums.com could not be reached from this session, so no walkthrough was opened.

| Feature | Microsoft Learn |
|---|---|
| W1 Conditional visibility | [Design layouts with the Word add-in](https://learn.microsoft.com/en-us/dynamics365/business-central/ui-design-word-layouts-business-central-add-in) (section on hiding content without a value) |
| W2 Header/footer reuse | [Set up themes and header/footer layouts](https://learn.microsoft.com/en-us/dynamics365/business-central/ui-set-up-report-themes-header-footer-layouts) |
| W3 Themes | Same page as W2 |
| X1 Lifecycle statuses | [Get started with layouts](https://learn.microsoft.com/en-us/dynamics365/business-central/ui-get-started-layouts) (Manage layout status) |
| X2 Standard Excel reports | [Report overview](https://learn.microsoft.com/en-us/dynamics365/business-central/reports-available-reports); [report 113](https://learn.microsoft.com/en-us/dynamics365/business-central/reports/report-113) |
| X3 Subtotals | [Release plan, sales scenarios](https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/analyze-customer-loyalty-other-sales-scenarios) |
| X4 Validate | [Get started with layouts](https://learn.microsoft.com/en-us/dynamics365/business-central/ui-get-started-layouts) (Validate a layout) |
| X5 / W4 Draft on upload | [Excel layouts](https://learn.microsoft.com/en-us/dynamics365/business-central/ui-excel-report-layouts) |

## 8. Open questions and what could not be verified

**Questions for you:**
1. **Can you get a version 29 sandbox?** Without one the Word block has no images: you can't capture them, and no published v29 screenshot was found.
2. **Allow yzhums.com and mc.merill.net for this session?** That would let an agent look for walkthrough screenshots and the roadmap text behind 573318, 573321 and 573328.
3. **Output language:** English, as assumed in the plan. Say so if you want Dutch.

**Dropped or unverified (not in the tables):**
- "Automate report outputs" (573318, v29): probably the new report inbox APIs (read output, mark as read, for Power Automate or MCP). That link is unconfirmed, and it is not scheduling. Left out.
- "Reduce complexity of report datasets" (573321, v29): title only; the seed claim of a "shared company information data item" is unsupported.
- "Updated Word add-in" (573328, v29): what is new versus v27/v28 is unknown.
- What "all report layouts" in the v29 lifecycle title adds beyond v28: undocumented. Only Draft-on-upload is stated.
- Comparison: offline use (inference), print/PDF for analysis mode and Power BI, Power BI subscriptions, emailing Excel output: all unknown.
- Whether the analysis sheet of report 113 has slicers, and whether Cronus returns data for it: check in the dry run.
- The deprecation of legacy finance reports in v28 (a good "why move" point) was seen only in a search snippet.
- The Aged AR/AP Excel release dates conflict (1 April vs 15 June 2025). Both fall in v26, so say "2025 wave 1".

**Verification totals:** 152 claim rows: 127 confirmed, 12 corrected, 12 unverified, 1 wrong; one more is graded corrected but is wrong scope in substance (two wrong-scope Word items in total, both moved to "Do NOT show as new").
