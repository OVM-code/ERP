# Excel layouts in Business Central: what is new in versions 26 to 29

Research subagent B. Written 2026-11-18. Scope: 2025 wave 1 (v26), 2025 wave 2 (v27), 2026 wave 1 (v28), 2026 wave 2 (v29).
Version mapping confirmed on the "What's new" pages: update 26.0 = 2025 wave 1, 27.0 = 2025 wave 2, 28.0 = 2026 wave 1, 29.0 = 2026 wave 2.

## 0. Read this first

- **yzhums.com could not be opened** (host not allowed in this session: DNS failure). The two yzhums leads (https://yzhums.com/73030/ and https://yzhums.com/73485/) are NOT cited. The same facts are covered by Microsoft Learn release-plan pages that were opened. Screenshots from yzhums are therefore not available.
- **mc.merill.net** (a mirror of the Microsoft 365 roadmap) could not be opened either. **microsoft.com/roadmap** opened but rendered empty (JavaScript). So no roadmap entry text was read. Roadmap IDs below come only from the Learn "What's new in 29.0" page.
- **Release plan 2026 wave 2 on Learn: not available.** `.../release-plan/2026wave2/...` returned "could not be retrieved" for the overview and for three guessed feature URLs. The What's new 29.0 page says Microsoft stopped publishing release plans from September 2026 and moved to the Microsoft Copilot Roadmap. So v29 facts come from the What's new 29.0 page and the product docs only. For two v29 features I only have a title (see section 3).
- All release-plan pages carry the banner "As of October 2026, this content is archived and no longer maintained". Dates below are the "General availability" dates shown on those pages.
- Not verified: no version 29 sandbox was available, so nothing here was tried in a live environment.

## 1. Capabilities (new platform and user-facing things Excel layouts can do or ways to manage them)

Column "Without developer" = can a consultant or key user do it without AL code.

### 2025 wave 1 (v26)

#### C1. Validate Layout action on the Report Layouts page
- Wave / version: 2025 wave 1, v26. GA Apr 1, 2025.
- Status: generally available. Enabled by: automatically; used by admins.
- Without developer: yes.
- What it does: an admin can check an uploaded layout and get a list of errors. Before, a broken layout often needed a developer or a support request. It applies to all layout types, Excel included.
- Value for report user: fewer broken reports after a layout upload.
- Value for decision-maker: lower support cost and less dependence on a developer.
- How it works:
  1. Search for **Report Layouts**.
  2. Select the user-defined layout.
  3. Choose **Validate**.
  4. A dialog shows the validation results; fix the workbook and replace the layout.
- Sources (opened): https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/validate-report-layouts-errors-as-admin (how-to: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-get-started-layouts, section "Validate a layout"). Also listed on https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-26-0
- Screenshot: yes, a validation dialog image on the release plan page (media/layout-validation-780x440.png). Not downloaded.
- Limits: validation covers the layout structure, not whether the numbers are right. Server-side Excel check: file must be a real .xlsx, not password protected, with a valid Data sheet (devenv-howto-excel-report-layout page, opened).

#### C2. Layout obsolete state (ObsoleteState property, plus Mark as obsolete in the client)
- Wave / version: 2025 wave 1, v26. GA Apr 1, 2025 (release plan "Use new properties on a report layout"). The Learn page "Defining multiple report layouts" says "applies to v26 and later".
- Status: generally available. Enabled by: developer sets the property in AL (extension layouts). The client toggle **Mark layout as obsolete** exists for user-defined layouts; the version in which that toggle appeared is UNKNOWN (the page does not say).
- Without developer: partly. Users mark their own user-defined layouts obsolete; extension layouts need a developer.
- What it does: flags a layout as deprecated so people move to another one. An **Obsolete** column shows on the Report Layouts page.
- Value for report user: a clear signal which layout to stop using.
- Value for decision-maker: smoother retirement of old layouts across releases.
- How it works (user-defined layout):
  1. Open **Report Layouts**.
  2. Select the layout, choose **Edit Info**.
  3. Turn on **Mark layout as obsolete**, select OK.
  4. The Obsolete column shows the flag.
  Developers: set ObsoleteState, ObsoleteReason, ObsoleteTag on the layout in AL.
- Sources (opened): https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-new-properties-report-layout ; https://learn.microsoft.com/en-us/dynamics365/business-central/ui-get-started-layouts ("Mark a layout as obsolete"); https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-multiple-report-layouts (only seen as a search result excerpt, NOT fetched; do not rely on it for the v26 statement beyond the release plan page).
- Screenshot: none on the release plan page.
- Limits: extension layouts cannot be marked obsolete from the client.

#### C3. ExcelLayoutMultipleDataSheets can be set per layout
- Wave / version: 2025 wave 1, v26 (runtime 15). GA Apr 1, 2025.
- Status: generally available. Enabled by: developer (AL property on the layout). The client dialog for a new layout has a **Create Multiple Data Sheets** toggle; the version in which that toggle was added is UNKNOWN.
- Without developer: partly. A consultant can import a multi-sheet workbook and set the toggle; a new built-in structure needs a developer.
- What it does: a report can give one data sheet per data item, so an Excel layout can use a PowerPivot data model. Setting it per layout means a new multi-sheet layout can be added without breaking existing single-sheet layouts that users uploaded earlier.
- Value for report user: richer Excel reports (pivots across several data tables) without losing older layouts.
- Value for decision-maker: new layouts can be rolled out without breaking custom layouts already in use.
- How it works:
  1. Developer sets ExcelLayoutMultipleDataSheets on the layout in the report's rendering section.
  2. Each data item becomes a sheet named #DataItemName.
  3. In the client: **Report Layouts**, **New**, Format Options = Excel, set **Create Multiple Data Sheets** to match the workbook.
  4. Upload the workbook (drag and drop or browse) and run the report.
- Sources (opened): https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-new-properties-report-layout ; https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-howto-excel-report-layout (tip: "Starting in 2025 release wave 1 (runtime 15)"); https://learn.microsoft.com/en-us/dynamics365/business-central/ui-excel-report-layouts (step 6 of "Task 2").
- Screenshot: none for this feature. The Excel layout overview page has an example image (media/excel-layout-2.png).
- Limits: for a multi-sheet layout you must keep the generated sheets, tables and column names; do not merge them into one Data table. Single-sheet layouts must keep a sheet and table named Data starting at A1.

#### C4. Layout name, caption and ID available inside the workbook
- Wave / version: v26.0 (2025 wave 1). Documented only in the developer article; no release plan entry found.
- Status: generally available (docs state "introduced in version 26.0"). Enabled by: automatic; used by whoever designs the layout.
- Without developer: yes (an Excel designer can reference the table).
- What it does: the hidden metadata sheet now tells the workbook which layout produced it, so a title or footer can show the layout name.
- Value for report user: can see which layout version a file came from.
- Value for decision-maker: easier audit trail for shared reports.
- How it works: open the Aggregated Metadata sheet (hidden), table ReportRequestValues, read Layout name / Layout caption / Layout id; reference it with an Excel table formula.
- Source (opened): https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-howto-excel-report-layout
- Screenshot: none.
- Limits: designer must know Excel table formulas; sheets are hidden by default.

### 2025 wave 2 (v27)

No new Excel-layout platform capability found. The v27 reporting items on https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-27-0 are content (section 2) or about Word, Power BI and Financial Reporting. Count: 0. (If Olivia knows of one, it is not in the sources opened.)

### 2026 wave 1 (v28)

#### C5. Control the lifecycle of report layouts (Draft, Pending approval, Approved, Retired)
- Wave / version: 2026 wave 1, v28. Release plan GA date May 1, 2026; the What's new 28.0 page lists it under 28.0. (See conflict note below.)
- Status: generally available. Enabled by: automatically; report layout administrators set the status.
- Without developer: yes.
- What it does: each layout gets a status. Only Approved layouts can be chosen on a report request page. Draft and Pending approval layouts are hidden from users, Retired layouts are phased out. Applies to all layout types, Excel included.
- Value for report user: sees only checked, approved layouts, so fewer wrong numbers.
- Value for decision-maker: governance and compliance: nobody runs an untested layout.
- How it works:
  1. Search for **Report Layouts**.
  2. Select one or more layouts.
  3. Choose **Layout**, then **Layout Status**.
  4. Pick Set Draft, Set Pending Approval, Set Approved or Set Retired.
  5. Changing the status of an extension-provided layout saves an override; the original stays unchanged.
- Sources (opened): https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/control-lifecycle-report-layouts ; how-to: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-get-started-layouts ("Manage layout status"); https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-28-0
- Screenshot: yes, on the release plan page (media/report-layout-lifecycle-780x440.png, relative link; not downloaded).
- Limits: no approval workflow engine is described; the status is set by hand. Whether v28 already covers extension layouts is UNKNOWN (see C8).
- **Version note:** release plan GA date "May 1, 2026" versus What's new 28.0 (which starts in April 2026). Minor version (28.0 or 28.1) is UNKNOWN from opened sources.

### 2026 wave 2 (v29)

#### C8. Lifecycle status for ALL report layouts, new layouts start as Draft
- Wave / version: 2026 wave 2, v29. Title on the What's new 29.0 page: "Control the lifecycle of all report layouts" (General availability, roadmap ID 573320).
- Status: generally available. Enabled by: automatically; admins approve layouts.
- Without developer: yes.
- What it does (from the product docs): in v29 a new or replaced user-defined layout starts in **Draft**. After testing it, an admin sets it to Approved so it shows on request pages. The docs say status changes on extension layouts are stored as overrides.
- Value for report user: only approved layouts appear, so no half-finished Excel files in the list.
- Value for decision-maker: a test-then-approve habit for every custom layout.
- How it works:
  1. Upload or replace an Excel layout (**Report Layouts**, **New** or **Replace Layout**).
  2. The layout shows status Draft; run it with **Run Report** to test.
  3. Select **Layout**, **Layout Status**, **Set as Approved**.
  4. The layout becomes selectable on report request pages.
- Sources (opened): https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-29-0 ; https://learn.microsoft.com/en-us/dynamics365/business-central/ui-excel-report-layouts (note: "In version 29, a new or replaced user-defined layout has the Draft status") ; https://learn.microsoft.com/en-us/dynamics365/business-central/ui-get-started-layouts
- Screenshot: none opened for v29.
- Limits: **Open question for Olivia:** the v28 and v29 features have almost the same name. The opened sources do not say what exactly v29 added on top of v28 (my reading: scope widened to all layouts including extension layouts, and the Draft-by-default behaviour). Marked UNKNOWN; treat as one feature family "lifecycle", with the Draft default dated v29 by the docs note. Do not present Draft-by-default as v28.

#### C9. Portable layout file paths in AL (runtime 18)
- Wave / version: 2026 wave 2 (runtime 18.0, the v29 runtime).
- Status: generally available per the docs ("applies to 2026 release wave 2 and later"). Enabled by: developer.
- Without developer: no.
- What it does: the properties that point at layout files (including ExcelLayout and LayoutFile) accept both / and \ on every operating system, so the same AL source builds on Windows and Linux.
- Value for report user: none directly.
- Value for decision-maker: indirect: easier build pipelines for partners. Probably NOT a presentation topic for this audience.
- How it works: developer writes layout paths with either slash; the compiler no longer reports AL0363.
- Source (opened): https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-report-layout-declaration
- Screenshot: none.
- Limits: developer-only.

#### Title-only candidates in v29 (NOT counted, details UNKNOWN)
Both appear in the What's new 29.0 table (opened) under "Reporting and data analysis", General availability. I could not open any detail page, so I cannot say whether they touch Excel layouts.
- "Automate report outputs" (roadmap ID 573318). UNKNOWN what it does. A web search snippet (not an opened source) suggested report inbox APIs for Power Automate or MCP; this is unverified. Worth confirming with Olivia, because scheduling and distribution of Excel output is a good story.
- "Reduce complexity of report datasets" (roadmap ID 573321). UNKNOWN whether it affects Excel layouts.
- Also on the v29 list but not Excel layout features: "Monitor usage of Open in Excel with telemetry" (list export, not layouts), "Run multiple financial reports and get a single PDF output" (Financial Reporting, PDF), "Trace G/L account usage in finance reports" (UNKNOWN), "Use system audit fields in analysis mode and in profiles".

### Related general limits for Excel layouts (opened)
- Excel layouts do not print from the request page: the user gets **Download**, then prints from Excel. Source: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-work-report
- Report row limits in Business Central online: default max rows 500,000 (user or developer can raise per report), absolute max 10,000,000; default max execution time 6 hours, max 12 hours. Excel's own sheet limits also apply (the page says Excel layouts cannot exceed them; the Excel limits themselves are on a Microsoft support page that was not opened). Source: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/operational-limits-online
- With OneDrive set up, a run of an Excel layout opens in Excel online. Source: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-excel-report-layouts
- Scheduling: any report can be scheduled through the job queue and the output goes to the Report Inbox. Source: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-work-report . Version in which scheduling appeared is outside scope.
- Out of scope but nearby: named formulas in new Excel workbooks come from 2024 wave 2 (v25); Company display name from 25.3. Not counted.

## 2. Content: Microsoft-shipped reports with a new or improved Excel layout

Report IDs come from the "Report overview" page (https://learn.microsoft.com/en-us/dynamics365/business-central/reports-available-reports, opened) matched by name. The release-plan pages give names only, so an ID marked "match by name" is my matching, not Microsoft's statement. Layout types (Word, Excel) are as stated on the release plan page.

### 2025 wave 1 (v26)

| Area | Report (ID) | What changed | Source (opened) | GA date shown |
|---|---|---|---|---|
| Finance | Trial Balance Previous Year (7), Trial Balance (4405), Trial Balance by Period (38), Trial Balance/Budget (4406), Consolidated Trial Balance (4410) | Listed as Excel reports under "better reporting and analytics for finance". Whether each was new in v26 or only improved: UNKNOWN. | https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-enhanced-analytics-finance | Apr 1, 2025 |
| Finance / receivables, payables | Aged Accounts Receivable Excel (4402), Aged Accounts Payable Excel (4403) | Listed as Excel reports. The sales and purchasing plans below also say "now generally available". | same as above | Apr 1, 2025 |
| Finance / fixed assets | Fixed Asset Details Excel (4411), Fixed Asset Projected Value Excel (4413) | Listed as Excel reports. | same as above | Apr 1, 2025 |
| Sales | Aged Accounts Receivables Excel | "now generally available" | https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-enhanced-analytics-sales | Jun 15, 2025 |
| Purchasing | Vendor Top List (Vendor - Top 10 List Excel, 4404; match by name), Aged Accounts Payables | "now generally available" | https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-enhanced-analytics-purchasing | Jun 15, 2025 |
| Sustainability | Emission By Category (6210), Emission Per Facility (6211), Total Emissions (6212) | New layouts that work for print and for pivot analysis in Excel. | https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-enhanced-excel-reports-sustainability | Jun 15, 2025 |

**Version conflict (same reports):** Aged Accounts Receivable and Payable are dated Apr 1, 2025 on the finance page and Jun 15, 2025 on the sales and purchasing pages. Both URLs kept above. Likely a first release in 26.0 and GA wording later, but the sources do not say; marked UNKNOWN.
Customer - Top 10 List Excel (4409) and Fixed Asset Analysis Excel (4412) exist as Excel reports in the overview but are not named in any release plan page I opened for these waves, so they are not counted.

Count v26 content: 13 reports (5 trial balance family, 2 aged, 2 fixed asset, Vendor Top List, 3 sustainability). Aged AR/AP are named on two pages but counted once.

### 2025 wave 2 (v27)

| Area | Report (ID) | What changed | Source (opened) | GA date shown |
|---|---|---|---|---|
| Finance (deferrals) | G/L Deferral Summary (1700), Sales Deferral Summary (1701), Purchasing Deferral Summary (1702) | RDL layouts replaced by Word and Excel layouts, in-client help and docs added. Also three new list pages for unposted deferral lines (analysis mode; not layouts). | https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/smb/dynamics365-business-central/deferral-reporting-enhancements | Oct 1, 2025 |
| Sales | Customer List (101), Customer - Order Summary (107), Customer - Order Detail (108), Sales Statistics (112), Customer/Item Sales (113), Customer Balance to Date (121), Customer Trial Balance (129), Sales Reservation Availability (209; match by name "Sales Reservation Avail."), Inventory Order Details (708), Inventory Sales Back Orders (718) | "Modernized": RDL replaced by Word and Excel layouts, docs supplement in-client help. Which of Word or Excel each report received: UNKNOWN. | https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/smb/dynamics365-business-central/use-enhanced-sales-analytics | Oct 1, 2025 |
| Manufacturing | Quantity Explosion of BoM, Where-Used (Top Level) | Modernized: RDL replaced by Word and Excel layouts. IDs not found by name, UNKNOWN. | https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/smb/dynamics365-business-central/use-enhanced-power-bi-manufacturing-app-modernized-reports-manufacturing-analytics | Oct 1, 2025 |
| Manufacturing | Production Order - List (99000763) (new, called "Prod. Order - List" on the release plan) | New report. The Report overview page describes it as Excel-based with two worksheets (overview and analysis). | release plan page above; overview page https://learn.microsoft.com/en-us/dynamics365/business-central/reports-available-reports | Oct 1, 2025 |

Not counted: Audit Trail report (330), GA Nov 1, 2025 (https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/smb/dynamics365-business-central/print-audit-trail-report): the page does not name a layout type.
Purchasing: the 2025 wave 2 purchasing page (opened) only describes a Power BI app, no report layouts. So v27 purchasing content: none found.

Count v27 content: 16 (3 deferral, 10 sales, 2 manufacturing modernised, 1 new manufacturing).

### 2026 wave 1 (v28)

| Area | Report (ID) | What changed | Source (opened) | GA date shown |
|---|---|---|---|---|
| Inventory | Inventory Top 10 List (711), Item Availability (705; match by name "Inventory Availability"), Inventory Purchase Orders (709), Item/Vendor Catalog (720; US, CA and MX use report 10164 per the overview page), Inventory Availability Plan (707 or 719: the overview page has two similar names, UNKNOWN which), Inventory - Transaction Detail (704), Item Expiration - Quantity (5809) | Modernized: RDL replaced by Excel and Word layouts; docs updated. | https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/modernizing-analytical-reports-inventory | Apr 1, 2026 |
| Inventory | Item Age Composition by Quantity and Value (NEW; ID UNKNOWN) | New report with Excel and Word layouts. The old Item Age Composition - Value (5808) and - Quantity (5807) and Items with Negative Inventory reports are deprecated. | same page | Apr 1, 2026 |
| Sales | Salesperson Commission (115), Customer/Item Sales (113), Inventory Order Details (708), Inventory Customer Sales (713), Inventory - Sales Back Orders (718) | Subtotals added to the Excel layouts. | https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/analyze-customer-loyalty-other-sales-scenarios | Apr 1, 2026 |
| Finance (deferrals) | Deferral Summary - GL (1700), - Purchase (1702), - Sales (1701) | Subtotals added to the Excel layouts, for reconciliation and audit. | https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/use-enhanced-faster-reports-analysis-deferrals-trial-balances | May 1, 2026 |
| Finance (trial balance) | Trial Balance (4405), Consolidated Trial Balance (4410), Trial Balance/Budget (4406), Trial Balance by Period (38), Trial Balance Previous Year (7) | Faster. Performance, not layout design. Note the What's new 28.0 page lists "Improved performance in Trial Balance-related Excel reports" as a NEW OPTIONAL feature in Feature Management, while the release plan says "Users, automatically". Treat as admin-switched in 28.0 until checked in an environment. Whether it is mandatory in v29: not in the opened v29 list ("Optional features now mandatory" does not name it). | release plan page above; https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-28-0 | May 1, 2026 |

Lead check: "Subtotals added to Excel layouts of built-in sales reports, v28" is confirmed by the Learn release plan page (not by yzhums, which could not be opened). "Deferral and trial balance Excel reports, v27 and 28.1" is confirmed in substance: v27 = deferral modernisation (Oct 2025); the subtotals and trial balance speed-up carry GA May 1, 2026. The label "28.1" is not stated in any opened source: UNKNOWN.
Screenshot: the deferral/trial balance release plan page has an image of an enhanced deferral Excel report (media/deferral-excel-780x440.png); the customer-loyalty page has only a Power BI screenshot; the inventory page has none.
The release plan page "Showcase analytics with enhanced demo data" (GA Apr 1, 2026) was found in the list but not opened; not used.

Count v28 content: 21 report entries (8 inventory modernised incl. 1 new, 5 sales subtotals, 3 deferral subtotals, 5 trial balance speed-up). Of these, 16 are layout changes and 5 are performance only.

### 2026 wave 2 (v29)

No Microsoft-shipped report with a new or improved Excel layout was found in the opened sources. The What's new 29.0 page does not name any, and the 2026 wave 2 release plan could not be opened. UNKNOWN. Count: 0 verified.

## 3. Counts per wave

| Wave | Version | Capabilities (verified) | Content (reports) | Notes |
|---|---|---|---|---|
| 2025 wave 1 | v26 | 4 (C1 to C4) | 13 | C2 and C3 partly developer; C4 from dev doc only |
| 2025 wave 2 | v27 | 0 | 16 | content only |
| 2026 wave 1 | v28 | 1 (C5) | 21 (16 layout, 5 performance) | |
| 2026 wave 2 | v29 | 2 (C8 lifecycle/Draft, C9 portable paths; C9 developer-only) | 0 verified | 2 title-only candidates, details UNKNOWN |
| Total | | 7 | 50 report entries (a few reports repeat across waves) | |

## 4. Open points for Olivia

1. Confirm what "Automate report outputs" (v29) does; it could be the best new story for decision-makers if it covers Excel output scheduling or distribution. Needs the Microsoft Copilot Roadmap (ID 573318) or a v29 environment.
2. Confirm what "Reduce complexity of report datasets" (v29) changes.
3. Confirm the exact v28 vs v29 difference for report layout lifecycle (C5 vs C8). Demo environment 28.5 should already have the v28 statuses; Draft-by-default is documented as v29.
4. Allow yzhums.com and mc.merill.net in the session network settings if walkthrough screenshots are wanted.
5. For a demo in 28.5, safe to show: Validate, lifecycle statuses, subtotals in the sales and deferral Excel layouts, inventory modernised Excel reports. Not showable in 28.5: anything marked v29.
