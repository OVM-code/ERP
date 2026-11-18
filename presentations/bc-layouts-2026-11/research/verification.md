# Verification of research files (verifier E)

Checked 2026-11-18. Demo environment version: 28.5. Word scope: first shipped in v29 only. Excel scope: v26 to v29.
Method: every URL below was opened with the Microsoft Learn fetch tool unless marked otherwise. Verdicts: CONFIRMED, CORRECTED, UNVERIFIED, WRONG (WRONG also covers WRONG SCOPE).

## Headline findings (read first)

1. **Word F1 is WRONG SCOPE in substance.** The Add Data task pane (data, labels, report metadata, Add field, Add repeater) first shipped in 2025 wave 2, v27, GA 1 Oct 2025 (U6). Insert Table is wave 1 2026 (v28, preview). The v29 item named "Design document reports with the updated Word add-in" (573328) exists only as a title; what is new in v29 inside it is UNKNOWN. Do not show the Add Data pane as new in 29.
2. **Word F6 is WRONG SCOPE for the lifecycle statuses.** Draft, Pending Approval, Approved, Retired shipped in 2026 wave 1, v28, GA 1 May 2026 (U2, U7). Only "replaced or new user-defined layout starts as Draft" is documented as version 29 (U8, U9).
3. **Trial Balance Excel speed-up is a Feature Management item that is ON by default from v28.** The What's new 28.0 page puts it under "New optional features" (U2), but the mandatory-features page lists it under "New features added and enabled by default in version 28" (U10). Three research files treat it as "not automatic" or "admin-switched". That is CORRECTED below.
4. **Excel file misses report IDs it called UNKNOWN**: Quantity Explosion of BOM = 99000753, Where-Used (Top Level) = 99000757 (U11). Inventory Availability Plan: the new Excel report is 719, introduced 2026 wave 1; 707 is the obsolete one (U12).
5. Comparison table cell "version 29 adds Draft/Approved status" is wrong. Statuses are v28; only the Draft default is v29.

## URL keys

- U1 What's new 29.0: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-29-0
- U2 What's new 28.0: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-28-0
- U3 What's new 27.0: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-27-0
- U4 What's new 26.0: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-26-0
- U5 What's new 29.1: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-29-1
- U6 RP 2025w2 Add data fields (Word add-in): https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/smb/dynamics365-business-central/add-data-fields-report-layouts-using-word-add-in
- U7 RP 2026w1 Control lifecycle of report layouts: https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/control-lifecycle-report-layouts
- U8 Word add-in doc: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-design-word-layouts-business-central-add-in
- U9 Get started with layouts: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-get-started-layouts
- U10 Optional features now mandatory: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/feature-management-mandatory-features
- U11 Report overview: https://learn.microsoft.com/en-us/dynamics365/business-central/reports-available-reports
- U12 Report 719 page: https://learn.microsoft.com/dynamics365/business-central/reports/report-719 (seen in Learn search result, content only; not fetched as full page)
- U13 Layouts overview: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-manage-report-layouts
- U14 Themes and header/footer: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-set-up-report-themes-header-footer-layouts
- U15 Declare layouts in AL: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-report-layout-declaration
- U16 Word layout dev doc: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-howto-report-layout
- U17 RP 2026w1 enhanced Word add-in: https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/get-easier-editing-document-report-layouts-enhanced-word-add-in
- U18 Excel layouts doc: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-excel-report-layouts
- U19 Excel layout dev doc: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-howto-excel-report-layout
- U20 RP 2025w1 new properties: https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-new-properties-report-layout
- U21 RP 2025w1 validate layouts: https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/validate-report-layouts-errors-as-admin
- U22 RP 2025w1 finance analytics: https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-enhanced-analytics-finance
- U23 RP 2025w1 sales analytics: https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-enhanced-analytics-sales
- U24 RP 2025w1 purchasing analytics: https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-enhanced-analytics-purchasing
- U25 RP 2025w1 sustainability Excel: https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-enhanced-excel-reports-sustainability
- U26 RP 2025w2 deferral reporting: https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/smb/dynamics365-business-central/deferral-reporting-enhancements
- U27 RP 2025w2 sales analytics: https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/smb/dynamics365-business-central/use-enhanced-sales-analytics
- U28 RP 2025w2 manufacturing: https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/smb/dynamics365-business-central/use-enhanced-power-bi-manufacturing-app-modernized-reports-manufacturing-analytics
- U29 RP 2026w1 inventory reports: https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/modernizing-analytical-reports-inventory
- U30 RP 2026w1 customer loyalty / sales subtotals: https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/analyze-customer-loyalty-other-sales-scenarios
- U31 RP 2026w1 deferral subtotals and faster trial balances: https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/use-enhanced-faster-reports-analysis-deferrals-trial-balances
- U32 Run and print reports: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-work-report
- U33 Report 113 page: https://learn.microsoft.com/en-us/dynamics365/business-central/reports/report-113
- U34 Report 4402 page: https://learn.microsoft.com/en-us/dynamics365/business-central/reports/report-4402
- U35 Report 4405 page: https://learn.microsoft.com/en-us/dynamics365/business-central/reports/report-4405
- U36 Analysis mode: https://learn.microsoft.com/en-us/dynamics365/business-central/analysis-mode
- U37 Install Power BI apps: https://learn.microsoft.com/en-us/dynamics365/business-central/across-powerbi-install-business-central-apps
- U38 Work with Power BI: https://learn.microsoft.com/en-us/dynamics365/business-central/across-working-with-powerbi
- U39 BC as Power BI data source: https://learn.microsoft.com/en-us/dynamics365/business-central/across-how-use-financials-data-source-powerbi
- U40 Power BI data refresh: https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-data
- U41 Operational limits online (report limits seen in Learn search result, content only): https://learn.microsoft.com/dynamics365/business-central/dev-itpro/administration/operational-limits-online
- U42 Report inbox items API: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reporting/report-inbox-items-api
- U43 Report inbox (Learn search result, content only): https://learn.microsoft.com/dynamics365/business-central/ui-work-report-inbox
- U44 RP 2026w1 sales document ESG layouts: https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/use-new-sales-document-reports-layout-that-show-carbon-footprint
- U45 Deprecated features (Learn search result, content only): https://learn.microsoft.com/dynamics365/business-central/dev-itpro/upgrade/deprecated-features-w1

---

## 1. word-v29.md

| Claim | Verdict | Note / correction | URL |
|---|---|---|---|
| W-a. 29.0 lists 573328, 573329, 573330, 573331, 573326, 573327, 573320, 573321 as GA under 2026 wave 2 | CONFIRMED | All eight titles and IDs match the 29.0 table, all "General availability". | U1 |
| W-b. Release plans stopped Sept 2026, moved to Copilot Roadmap | CONFIRMED | Stated on 29.0 and 29.1 pages. | U1, U5 |
| W-c. 2026 wave 2 release-plan URLs and roadmap not usable | CONFIRMED | I also could not open the roadmap entry (WebFetch returned a page without the item) or mc.merill.net (host not resolvable from this session). | U1 |
| W-d. "New Document Report Experience" is a new optional feature, disabled by default; composite layouts and Subtype need "Document Report Experience" enabled | CONFIRMED | 29.0 "New optional features: Feature: New Document Report Experience (disabled by default)"; mandatory page repeats "disabled by default in version 29". Display-name question stays UNKNOWN (docs use both wordings). | U1, U10, U9, U14 |
| W-e. 29.1 has no Word layout item | CONFIRMED | 29.1 feature table: country/region, e-documents, expense agent, finance, sandbox, payables agent, sustainability. No layout item. | U5 |
| W-f. On-prem 29.1 build 29.1.57326, Nov 2026 | UNVERIFIED | Only seen in a Learn search snippet of the on-prem updates page; not fetched. Irrelevant to the talk. | https://learn.microsoft.com/dynamics365/business-central/dev-itpro/deployment/update-versions-29 |
| W-g. Online update period ends Feb 2027 | CONFIRMED | "five-month update period, which ends in February 2027". | U1 |
| W-h. F1 Design document reports with updated Word add-in (573328): wave 2 2026, v29, GA | CORRECTED | The title is in 29.0 GA. But the behaviour described (Add Data pane, Data/Labels/Report Information groups, Add field, content controls) first shipped in 2025 wave 2 (v27), GA 1 Oct 2025. Insert Table is 2026 wave 1. So F1 as written is WRONG SCOPE for a "new in 29" slide. What v29 adds under this ID is UNKNOWN. | U6, U17, U1 |
| W-i. F1 how-to steps (Update and Export Layout, Add Data, Add field, Replace Layout, Draft after replace) | CONFIRMED | Matches the Word add-in doc. The Draft-after-replace note is explicitly "In version 29". | U8 |
| W-j. F1 prerequisite: file must come from Update and Export Layout; extension layouts cannot be replaced | CONFIRMED | Stated in the doc. | U8 |
| W-k. F1 "XML Mapping Pane still works as fallback" | CONFIRMED | Stated in the doc. | U8 |
| W-l. F2 Conditional visibility (573329): Hide Field if Zero, Hide Empty Table, Hide Empty Table Row, Hide Empty Table Column; combine field + column | CONFIRMED | Four controls and the discount-column example match. Version: no earlier release-plan entry found; title is in 29.0 GA. Treat as v29. | U8, U1 |
| W-m. F2 "hide if false" control not documented | CONFIRMED | None on the page. | U8 |
| W-n. F3 Header/footer layouts (573331): separate .docx, Subtype HeaderFooter, New header/footer, Set Approved | CONFIRMED | Matches. | U14, U15 |
| W-o. F3 "sample controls" wording unverified | CONFIRMED | No page names sample controls. Keep as UNKNOWN. | U8, U14 |
| W-p. F3 Different first page / odd-even headers unsupported for HTML conversion | CONFIRMED | Stated in the dev doc, not as v29-new (file says so). | U16 |
| W-q. F4 Themes (573330): .dotx, Subtype Theme, only Body layouts use them | CONFIRMED | | U14, U15, U13 |
| W-r. F4 extension parts can be exported but not edited/replaced/deleted | CONFIRMED | | U14 |
| W-s. F5 Reuse header/footer (573326) and Brand with themes (573327): global, company, report, layout defaults; Company Information Reporting FastTab; Composite layout actions | CONFIRMED | Menu names and pages match. | U14 |
| W-t. F5 resolution order (six levels) | CONFIRMED | Matches the table exactly. Note one extra rule the file omits: a part stored with the selected layout by an extension wins first. | U14 |
| W-u. F5 gotchas (status change does not remove assignment; FactBox shows None; delete clears assignments) | CONFIRMED | | U14 |
| W-v. F5 AL: Subtype Default/Body/HeaderFooter/Theme; DefaultHeaderFooterPart and DefaultThemePart; 2026 wave 2 and later | CONFIRMED | "APPLIES TO: 2026 release wave 2 and later". File says runtime 18.0 for Subtype; the page states runtime 18.0 only for the compiler items. Minor. | U15 |
| W-w. F6 Lifecycle (573320) "first shipped in 29.0" | WRONG | The status model (Draft, Pending Approval, Approved, Retired) was GA 1 May 2026 in 2026 wave 1 and is in the 28.0 table as "Control the lifecycle of report layouts". Only the Draft-on-new/replace behaviour is documented as version 29. Label as "extended in 29", not "new in 29". | U7, U2, U9 |
| W-x. F6 statuses and "only Approved selectable"; extension status change stored as override | CONFIRMED | | U9 |
| W-y. F6 "Draft after Replace Layout" is v29 | CONFIRMED | | U8 |
| W-z. F6 telemetry since v25 | UNVERIFIED | Telemetry section exists on the layouts overview page, no version stated; the telemetry trace page was not opened. | U13 |
| W-aa. F6 permissions UNKNOWN; upgrade behaviour UNKNOWN | CONFIRMED | Not documented on opened pages. | U9 |
| W-ab. F7 Reduce complexity of report datasets (573321): only title known; CompanyMetadata is plumbing | CONFIRMED | Title only on Learn. CompanyMetadata text confirmed in U15. See open points. | U1, U15 |
| W-ac. F8 runtime 18.0: extended XML always embedded, flag deprecated; both slash types | CONFIRMED | | U15 |
| W-ad. Out of scope: enhanced add-in editing, wave 1, preview 15 Mar 2026, GA 1 Apr 2026 | CONFIRMED | | U17 |
| W-ae. Out of scope: Insert Table in preview in wave 1 | CONFIRMED | Page says "Currently in preview". GA date of Insert Table: UNKNOWN. | U17 |
| W-af. Out of scope: ReportMetadata/ReportRequest system data items v26 | CONFIRMED | "APPLIES TO 2025 release wave 1 (v26) and later". | U16 |
| W-ag. Out of scope: Update and Export Layout, create blank layout, Export report schema v25 | CONFIRMED | "2024 release wave 2 and later". | U16 |
| W-ah. Out of scope: WordMergeDataItem sections fix 2024 wave 2 | CONFIRMED | | U16 |
| W-ai. Out of scope table is complete | CORRECTED | Missing the most important older item: Add Data task pane, v27, GA 1 Oct 2025. Add it. | U6 |
| W-aj. 28.5 cannot show F1 to F7 | CONFIRMED (partly) | F2 to F5, F7 are v29-new; F1's Add Data pane and F6's statuses DO exist in 28.5 per U6 and U7. | U6, U7 |
| W-ak. Licence, add-in build number UNKNOWN | CONFIRMED | Not on opened pages. | U8 |

## 2. excel-v26-v29.md

| Claim | Verdict | Note / correction | URL |
|---|---|---|---|
| E-a. Version mapping 26.0=2025w1, 27.0=2025w2, 28.0=2026w1, 29.0=2026w2 | CONFIRMED | | U4, U3, U2, U1 |
| E-b. Release-plan pages carry "archived as of October 2026" banner; GA dates as shown | CONFIRMED | | U7, U20 |
| E-c. C1 Validate Layout, v26, GA 1 Apr 2025, no developer, screenshot on plan page | CONFIRMED | Plan names the action "Validate Layout"; docs call it "Validate". Listed in 26.0 table. | U21, U4, U9 |
| E-d. C1 server-side Excel checks (real .xlsx, not password protected, Data sheet) | CONFIRMED | | U19 |
| E-e. C2 ObsoleteState, v26, GA 1 Apr 2025; Obsolete column on Report Layouts | CONFIRMED | | U20 |
| E-f. C2 "applies to v26 and later" from the multiple-layouts page | UNVERIFIED | File itself says not fetched; I did not open it either. Release plan supports v26. | U20 |
| E-g. C2 client toggle "Mark layout as obsolete" exists; version UNKNOWN | CONFIRMED | Toggle documented under Edit Info; no version stated. | U9 |
| E-h. C3 ExcelLayoutMultipleDataSheets per layout, 2025 wave 1, runtime 15 | CONFIRMED | | U20, U19 |
| E-i. C3 "Create Multiple Data Sheets" toggle in New layout dialog | CONFIRMED | Version of toggle UNKNOWN. Background correction: the global report property dates from v23 (2023 wave 2); only the per-layout override is v26. The file's "What it does" implies the whole feature is v26. | U18, U19 |
| E-j. C4 layout name/caption/id in ReportRequestValues "Introduced in version 26.0" | CONFIRMED | | U19 |
| E-k. v27: 0 platform capabilities for Excel layouts | CONFIRMED | None in the 27.0 table. | U3 |
| E-l. C5 Lifecycle statuses, v28, GA 1 May 2026, in 28.0 table | CONFIRMED | | U7, U2 |
| E-m. C5 "Draft and Pending hidden, Retired phased out" | CONFIRMED | Docs: not available for selection. | U9 |
| E-n. C5 "no approval workflow engine is described" | CONFIRMED | Absence on page. | U7 |
| E-o. C8 v29 title "Control the lifecycle of all report layouts" 573320 GA | CONFIRMED | | U1 |
| E-p. C8 note "In version 29, a new or replaced user-defined layout has Draft status" | CONFIRMED | Exact doc note. | U18 |
| E-q. C8 "scope widened to all layouts incl. extension layouts" | UNVERIFIED | File labels it a reading. Extension overrides are documented on U9 without version tag; v28 plan does not say extension layouts excluded. Do not claim. | U9, U7 |
| E-r. C9 portable paths, runtime 18, developer only | CONFIRMED | "2026 release wave 2 and later". | U15 |
| E-s. Title-only: Automate report outputs 573318, Reduce complexity 573321 | CONFIRMED | Titles and GA match. See open points for what they might contain. | U1 |
| E-t. Other v29 items "Monitor usage of Open in Excel with telemetry", "Run multiple financial reports...", "Trace G/L account usage", "system audit fields in analysis mode" | CONFIRMED | Present in 29.0 table; contents not opened. | U1 |
| E-u. Excel layouts have no Print/Preview, user downloads | CONFIRMED | | U32 |
| E-v. Limits: default max rows 500,000, absolute 10,000,000; default 6 h, max 12 h; Excel sheet limits apply | CONFIRMED | | U41, U32 |
| E-w. OneDrive opens Excel online | CONFIRMED | | U18 |
| E-x. Scheduling via job queue, output to Report Inbox | CONFIRMED | | U32, U43 |
| E-y. Named formulas v25 (2024 wave 2); company display name 25.3 | CONFIRMED | | U19 |
| E-z. v26 content: finance plan lists Trial Balance Previous Year, Trial Balance, by Period, Budget, Consolidated, Aged AR, Aged AP, Fixed Asset Details, Fixed Asset Projected as Excel reports, GA 1 Apr 2025 | CONFIRMED | | U22 |
| E-aa. v26 IDs: 7, 4405, 38, 4406, 4410, 4402, 4403, 4411, 4413 | CONFIRMED | All match the report overview. | U11 |
| E-ab. v26 sales plan: Aged AR Excel "now GA", 15 Jun 2025 | CONFIRMED | | U23 |
| E-ac. v26 purchasing plan: Vendor Top List, Aged AP Excel "now GA", 15 Jun 2025; Vendor Top List = 4404 | CONFIRMED | 4404 "Vendor - Top 10 List Excel" on overview. | U24, U11 |
| E-ad. v26 sustainability: Emission By Category, Per Facility, Total Emissions (6210, 6211, 6212), 15 Jun 2025 | CONFIRMED | | U25, U11 |
| E-ae. Aged AR/AP date conflict 1 Apr vs 15 Jun 2025 unresolved | CONFIRMED | Both pages say what the file says. Wave is v26 either way. See open points. | U22, U23, U24 |
| E-af. "Customer Top 10 List Excel (4409) and Fixed Asset Analysis Excel (4412) not named in any release plan opened" | CONFIRMED (limited) | IDs exist on overview (4409 "Customer - Top list Excel"). I did not search every plan either. | U11 |
| E-ag. v27 deferral: three summaries (1700, 1701, 1702), RDL replaced by Word and Excel, GA 1 Oct 2025 | CONFIRMED | | U26, U11 |
| E-ah. v27 sales: ten modernized reports, IDs 101,107,108,112,113,121,129,209,708,718 | CONFIRMED | All IDs match overview. Note overview describes 209 as "a legacy report for sales analysis"; odd but the plan names it. | U27, U11 |
| E-ai. v27 manufacturing: Quantity Explosion of BoM, Where-Used (Top Level) IDs UNKNOWN | CORRECTED | IDs are 99000753 and 99000757 on the overview. | U28, U11 |
| E-aj. v27 new report "Prod. Order - List" = 99000763, Excel-based with two worksheets | CONFIRMED | Overview calls it "Production Order - List", Excel-based, two worksheets. | U28, U11 |
| E-ak. Audit Trail report 330 not counted, GA 1 Nov 2025 | UNVERIFIED | Page not opened by me. Low impact. | https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/smb/dynamics365-business-central/print-audit-trail-report |
| E-al. v27 count 16 | CONFIRMED | 3 + 10 + 2 + 1. | U26, U27, U28 |
| E-am. v28 inventory: seven modernized + new Item Age Composition by Quantity and Value; three deprecated; GA 1 Apr 2026 | CONFIRMED | | U29 |
| E-an. v28 inventory IDs 711, 705, 709, 720, 704, 5809 | CONFIRMED | | U11 |
| E-ao. "Item/Vendor Catalog (720; US, CA, MX use 10164 per overview)" | CORRECTED | The 10164 note on the overview is attached to report 320 "Vendor Item catalog", not 720. Whether 720 is the release-plan "Item/Vendor Catalog" is a name match only. | U11 |
| E-ap. "Inventory Availability Plan 707 or 719, UNKNOWN" | CORRECTED | New Excel report is 719 "Inventory - Availability Plan Excel", INTRODUCED IN 2026 wave 1; 707 is the obsolete predecessor. | U12, U11 |
| E-aq. v28 sales subtotals: Salesperson Commission (115), Customer/Item Sales (113), Inventory Order Details (708), Inventory Customer Sales (713), Inventory Sales Back Orders (718), GA 1 Apr 2026 | CONFIRMED | Names match; IDs match overview. | U30, U11 |
| E-ar. v28 deferral subtotals, GA 1 May 2026 | CONFIRMED | | U31 |
| E-as. v28 trial balance five reports "faster", performance not layout | CONFIRMED | | U31 |
| E-at. Trial Balance speed-up: "listed as NEW OPTIONAL feature; treat as admin-switched in 28.0" | CORRECTED | In 28.0 it is a Feature Management item "Feature Update: Improved performance in Trial Balance-related Excel reports", and the mandatory-features page says it was "added and enabled by default in version 28". Release plan says "Users, automatically". Not in the v29 mandatory list. So: switch exists, default is ON. Confirm the switch state in the 28.5 environment. | U2, U10, U31 |
| E-au. "28.1" label for subtotals/trial balance unverifiable | CONFIRMED | No page names a minor version. 28.5 is later anyway. | U2 |
| E-av. v28 counts 21 (16 layout, 5 perf) | CONFIRMED | 8 + 5 + 3 + 5 = 21; arithmetic ok. | U29, U30, U31 |
| E-aw. v29 content: none verified | CONFIRMED | Absence in opened sources; Learn 29.0 lists none. See "Possibly missing". | U1 |
| E-ax. Counts table (4, 0, 1, 2 capabilities; 13, 16, 21, 0 content) | CONFIRMED | Matches the sections. C9 is developer-only, so the audience-relevant v29 count is 1. | n/a |
| E-ay. "Safe to show in 28.5: Validate, lifecycle statuses, subtotals, inventory Excel reports" | CONFIRMED | All v26/v28 GA before 28.5. | U21, U7, U30, U29 |
| E-az. Capability list complete for v26 | CORRECTED | Missing from "Possibly missing" check: none strictly Excel-layout capabilities in 26.0 beyond C1 to C4, but PDF post-processing (26.0 table) is not Excel. No correction needed to counts. See "Possibly missing" for v28 legacy-report removal. | U4 |

## 3. comparison.md

| Claim | Verdict | Note / correction | URL |
|---|---|---|---|
| X-a. XL "Who builds": consultant/power user with Excel; AL for packaged | CONFIRMED | | U18, U19 |
| X-b. XL "Who maintains: version 29 adds Draft/Approved status" | CORRECTED | Statuses are v28 (GA 1 May 2026). V29 only makes new/replaced layouts start as Draft. | U7, U18 |
| X-c. XL licence: no extra licence stated | CONFIRMED | None on opened pages. | U18 |
| X-d. XL freshness: snapshot at run time (inference) | CONFIRMED | Flow in dev doc supports it. | U19 |
| X-e. XL volume: 10,000,000 rows, 12 h | CONFIRMED | | U32, U41 |
| X-f. XL combining: report dataset only, several data sheets | CONFIRMED | | U19 |
| X-g. XL printing: download then print from Excel; no Printer field or buttons | CONFIRMED | | U32 |
| X-h. XL scheduling: job queue, Report Inbox, OneDrive share | CONFIRMED | | U32, U43 |
| X-i. XL emailing Excel output UNKNOWN; email layouts must be Word | CONFIRMED | Layouts overview says email layouts must be Word. | U13 |
| X-j. XL sharing: Available in All Companies | CONFIRMED | | U9 |
| X-k. XL parameters in hidden metadata tables | CONFIRMED | ReportRequestPageValues, ReportFilterValues. | U19 |
| X-l. XL sheet protection and sensitivity labels | CONFIRMED | | U18 |
| X-m. XL slicers in workbook | CONFIRMED | | U18 |
| X-n. AM "no build step; end user drags fields" | CONFIRMED | | U36 |
| X-o. AM needs DATA ANALYSIS - EXEC permission (v23+) | CONFIRMED | | U36 |
| X-p. AM over 100,000 rows: large-data mode with trade-offs; export needs filters above 100,000 | CONFIRMED | | U36 |
| X-q. AM related-table fields since 26.2, Add Related Fields permission set, calculated fields lost | CONFIRMED | | U36 |
| X-r. AM views private; link share; recipients create own view; JSON export | CONFIRMED | | U36 |
| X-s. AM 2026 wave 2 bookmark action | CONFIRMED | "Starting in Business Central 2026 release wave 2". Matches 573319. | U36, U1 |
| X-t. AM "Grid only; no print layout" | UNVERIFIED | The analysis-mode page does not state this. Inference. | U36 |
| X-u. AM governance "respects table permissions" | UNVERIFIED | Page says you need permission to a table or field to add related fields; no general statement. | U36 |
| X-v. AM scheduling "none found" | CONFIRMED | None on page. | U36 |
| X-w. PBI: paid Power BI licence per user; apps free | CONFIRMED | | U38, U37 |
| X-x. PBI: Pro for installer, refreshing user and every viewer; Premium/Fabric alternative | CONFIRMED | | U37 |
| X-y. PBI refresh: up to 8 on shared, 48 on Premium/PPU/Fabric; under 2 h on shared | CONFIRMED | | U40 |
| X-z. PBI: one app install per company, own workspace | CONFIRMED | | U37 |
| X-aa. PBI: 8 min call limit, page size cap 20,000, date filters per app | CONFIRMED | | U39, U37 |
| X-ab. PBI cross-company via custom Power Query function and Table.Combine; OData cannot | CONFIRMED | | U39, U38 |
| X-ac. PBI governance: Read permission for refresh user; permission sets per app; app updates can overwrite edits | CONFIRMED | | U37 |
| X-ad. PBI template apps 27.0 and later | CONFIRMED | Table shows 27.0 and later for all nine. | U37 |
| X-ae. Offline use cells (inference) | UNVERIFIED | File marks them as inference; no page states it. | U18, U36 |
| X-af. Fit with Excel habits "Low" for PBI (opinion) | UNVERIFIED | Opinion, labelled as such. | n/a |
| X-ag. "[BI1] reports-bi-reporting" screenshot mention | UNVERIFIED | Page not opened by me. Low impact. | https://learn.microsoft.com/dynamics365/business-central/reports-bi-reporting |
| X-ah. Citation keys: [XL4] vs [XL1] mix | CORRECTED | Presentation risk only: email-must-be-Word point is on the layouts overview (U13) and the get-started page (U9), not the Excel page. Fix the key before the notes are reused. | U13, U9 |
| X-ai. Draft status "cannot be demonstrated on 28.5; belongs to other research files" | CORRECTED | Lifecycle statuses CAN be shown in 28.5 (v28). Only the Draft default is v29. | U7, U18 |
| X-aj. "Pick this when" / "wrong choice" sections | UNVERIFIED | Opinion and scenarios, mostly labelled. Scheduled-email caveat is consistent with the sources. | n/a |

## 4. demo-report.md

| Claim | Verdict | Note / correction | URL |
|---|---|---|---|
| D-a. Report 113 Customer/Item Sales exists with Excel layout introduced 2025 wave 2 (v27); Excel layout with print and analysis worksheets; Word layout for print | CONFIRMED | "INTRODUCED IN: Business Central 2025 release wave 2". Exists in 28.5. | U33 |
| D-b. Subtotals added to Excel layout of 113 in 2026 wave 1 (v28), GA 1 Apr 2026 | CONFIRMED | Customer/Item Sales is named explicitly. Not listed in the 28.0 What's new table; wave-level only. 28.5 is later than 28.0 so it should be present. Verify in the dry run (checklist item 1). | U30, U2 |
| D-c. Filters Posting Date and Item No. on 113 | CONFIRMED | | U33 |
| D-d. 4402 exists; request-page "Aged as of" and "Period length"; summarised by global dimensions; four worksheets with slicers | CONFIRMED | By period (LCY), By Period (FCY), Due by Currencies, CustomerAgingData. | U34 |
| D-e. 4405 exists; Date Filter, Hide Accounts with No Activity; four sheets incl. printable list; slicers | CONFIRMED | Sheets: Trial Balance List (Print), LCY, ACY, TrialBalanceData. | U35 |
| D-f. "Speed-up in v28 is a Feature Management item, so not automatic" (candidate C row) | CORRECTED | Switch exists but is enabled by default in v28. Not a barrier; also "not visible in a demo" is fair. | U10, U2 |
| D-g. Recommended path steps 6 to 9 (Report Layouts, Edit Info + Save Changes to Copy, Validate, Layout Status, extension layout asks to edit a copy) | CONFIRMED | | U9 |
| D-h. Step 7 "Mark layout as obsolete" toggle on the copy | CONFIRMED | Documented under Edit Info; availability in 28.5 not verifiable (file says dry run). | U9 |
| D-i. Step 9 Draft/Pending not available for selection; Approved available | CONFIRMED | | U9, U7 |
| D-j. Step 5 "report pages mention Copilot in Excel or what-if tools" | CORRECTED | True for 4402 and 4405 (raw data sheet text). The 113 page contains no such text. Say it from the Excel product, not from the 113 page. | U34, U35, U33 |
| D-k. Step 2 Excel opens in Excel online if OneDrive set up, else downloads | CONFIRMED | | U18, U32 |
| D-l. Step 10 slide: v29 new/replaced layouts start Draft | CONFIRMED | | U18, U8 |
| D-m. Row "Draft default: in 28.5 a new copy may start as Approved; do not claim either way" | CONFIRMED | Correct caution. The get-started page says new user-defined layouts start as Draft, with no version tag; the Excel and Word pages tie it to version 29. Behaviour in 28.5 UNVERIFIED. | U9, U18 |
| D-n. Row "Extend lifecycle to all layouts (C8): slide only, v28/v29 difference UNKNOWN" | CONFIRMED | Unresolved in all sources. | U1, U7 |
| D-o. Row "Multiple data sheets (C3) slide only" | CONFIRMED | | U18, U19 |
| D-p. Row "Layout name in metadata (C4), v26.0" | CONFIRMED | | U19 |
| D-q. Row "Portable paths: skip" | CONFIRMED | | U15 |
| D-r. Row "Automate report outputs v29 title-only, do not present as Excel" | CONFIRMED | Reasonable. See open points. | U1 |
| D-s. Validate = v26 | CONFIRMED | | U21 |
| D-t. Obsolete = v26 (release plan) | CONFIRMED | | U20 |
| D-u. Layout statuses = v28 | CONFIRMED | | U7 |
| D-v. Scoring "Cronus returns data" for 113, 4402, 4405 | UNVERIFIED | Demo data content not documented on opened pages. File says so. A newer release plan says 2026 wave 1 added more sales orders and sales backorders to demo data (U30), which helps 113 but is not proof. | U30 |
| D-w. Step 4 slicers on 113 analysis sheet unknown | CONFIRMED | 113 page says only "worksheets designed for print and for analysis". | U33 |
| D-x. Fallback 1 and 2 (4405, 4402) | CONFIRMED | | U35, U34 |
| D-y. Timing sum 330 s | CONFIRMED | 40+25+55+35+15+25+35+25+40+35 = 330. | n/a |
| D-z. Client use case "illustrative" | CONFIRMED | Labelled as such. | n/a |
| D-aa. Demo environment is 28.5 and the feature set used is v26/v27/v28 | CONFIRMED | Every demoed feature is in 26.0, 27.0 or 28.0. | U4, U3, U2 |

---

## Possibly missing

Word (v29-first only):
- None found with a separate v29 Word-layout entry beyond the eight in the 29.0 table. The 29.0 table has no further Word entry (checked "Reporting and data analysis" and "Development" blocks). U1.
- Add Data task pane is NOT v29 (v27). See W-h. U6.
- Word add-in **Insert layout comment** (maintenance notes and version-history table, not rendered): documented on the Word add-in page, no version stated. Could be v29 or older; do not list as v29 without a source. U8.
- Developer: `DefaultHeaderFooterPart`, `DefaultThemePart` properties and Subtype in AL: already covered in F5. U15.
- 2026 wave 1 (v28) Word-adjacent, out of scope for Word but worth knowing: "Use new sales document report layouts that show your carbon footprint" (Word ESG invoice/quote layouts, GA 1 Apr 2026, v28). U44. "Set default language for documents on the company level" (v28, in 28.0 table). U2.

Excel (v26 to v29):
- v26: nothing new beyond C1 to C4. The 26.0 table also lists "Use enhanced analytics for inventory" (queries and list-page fields, Inventory by Location Analysis query, not Excel layouts, GA 1 Apr 2025) and "Enhance reports with PDF post-processing". U4.
- v27: 27.0 lists "Use enhanced Financial Reporting" (default values feature update, not Excel). U3.
- v28: **Inventory - Availability Plan Excel (719), INTRODUCED IN 2026 wave 1** (see E-ap). U12. Deprecation: legacy finance reports (Aged AR/AP legacy, Trial Balance legacy, Trial Balance/Budget legacy, Fixed Asset legacy) and Excel reports on Business Manager/Accountant role centers removed in 2026 wave 1; these are replaced by the Excel-layout reports, so it is a useful "why move to Excel layouts" point. U45 (search-result content only).
- v28: Financial Reporting enhancements (scheduling to distribution group with email, logo on PDF) are Financial Reporting, not Excel layouts. Do not mix. https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/financial-reporting-enhancements
- v29: report inbox APIs (items, content, file, companies) "APPLIES TO 2026 release wave 2 and later", output types PDF, Word, Excel, Zip. Probably relevant to Excel output automation; see open point 1. U42.
- v29: "Run multiple financial reports and get a single PDF output" (573323), "Trace G/L account usage in finance reports" (573324), "Monitor usage of Open in Excel with telemetry" (573317): contents not opened; likely not Excel layouts. U1.
- Secondary sources (yzhums.com, mc.merill.net, Copilot Roadmap page) could not be reached from this session (DNS or no item content), so no walkthrough screenshots were checked.

## Open points resolved/unresolved

1. **"Automate report outputs" (573318): PARTLY RESOLVED, unverified link.** Learn has four new report inbox API pages (items GET/PATCH to mark read, content, file, companies), all "APPLIES TO 2026 release wave 2 and later", with output types PDF, Word, Excel, Zip. A web-search snippet of roadmap item RM573318 (mc.merill.net, not opened, host blocked) says "use new APIs on the report inbox to extend automation with Power Automate or MCP". Evidence is consistent but no Microsoft page states that 573318 equals these APIs. Verdict: PROBABLE, mark UNVERIFIED on slides. It is read-only access plus a mark-as-read PATCH: it is NOT a scheduling feature. U42, https://learn.microsoft.com/dynamics365/business-central/dev-itpro/api-reporting/report-inbox-content-api
2. **"Reduce complexity of report datasets" (573321): UNRESOLVED.** Only the title is on Learn. The Word dev docs show `ReportRequest` system data item with company columns (CompanyName, CompanyDisplayName, CompanyId; "APPLIES TO v26 and later") and `CompanyMetadata` in v29, but neither is tied to 573321 by any source. The "shared company information data item" seed claim remains unsupported. U1, U15, U16.
3. **Layout lifecycle v29 versus v28: PARTLY RESOLVED.** v28 (GA 1 May 2026): the four statuses, only Approved selectable, extension-status override (U7, U9; U7 text does not mention overrides, U9 does without version). v29: title changed to "all report layouts" (U1); two docs state "In version 29" a new or replaced user-defined layout is Draft (U8, U18). What "all" adds beyond v28 is NOT documented. Do not state it.
4. **Aged AR/AP date conflict: UNRESOLVED, but harmless.** Finance plan: GA 1 Apr 2025 (U22); sales and purchasing plans: "now generally available" at 15 Jun 2025 (U23, U24). Both in 2025 wave 1 (v26). No Microsoft page explains the gap. Safe wording: "2025 wave 1, v26".
5. **Trial Balance Excel speed-up: RESOLVED.** Feature Management entry exists and is enabled by default from v28 (U10), while 28.0 What's new files it under "New optional features" (U2) and the plan says "Users, automatically" (U31). Not in the v29 mandatory list (U1, U10). Check the toggle in the 28.5 environment before saying "automatic".

## Counts per verdict

Counted from the four tables above (rows, including CONFIRMED (limited/partly) as CONFIRMED).

| File | CONFIRMED | CORRECTED | UNVERIFIED | WRONG | Rows |
|---|---|---|---|---|---|
| word-v29.md | 32 | 2 | 2 | 1 | 37 |
| excel-v26-v29.md | 44 | 5 | 3 | 0 | 52 |
| comparison.md | 27 | 3 | 6 | 0 | 36 |
| demo-report.md | 24 | 2 | 1 | 0 | 27 |
| Total | 127 | 12 | 12 | 1 | 152 |

Note: the Word F1 row (W-h) is graded CORRECTED, but its substance is wrong scope (Add Data pane is v27). Treat it as the second WRONG-SCOPE finding. Rows combine several related claims, so counts are by row, not by atomic fact.
