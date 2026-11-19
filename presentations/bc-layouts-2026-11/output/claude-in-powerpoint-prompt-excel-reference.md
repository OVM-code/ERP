# Prompt for Claude in PowerPoint: Excel layouts reference deck

What this is: a documentation deck covering everything verified about Business Central Excel layouts from 2025 wave 1 to 2026 wave 2 (versions 26 to 29). It isn't the 15-minute talk. Use it as a reference, a leave-behind or a source for backup slides.

How to use:
1. Open a new or existing PowerPoint file with your company template (Claude reuses its master).
2. Open Claude in PowerPoint and paste everything between the two lines below as one message.
3. Check the outline it proposes, then say "go".

Source: `output/decision-pack.md` and `research/` (excel-v26-v29, comparison, demo-report, verification, verification-2), 19 Nov 2026. Only claims that survived verification are included, with corrections applied.

---

```text
ROLE
You build a reference deck (documentation, not a keynote) in this open
PowerPoint file about Excel report layouts in Dynamics 365 Business Central,
versions 26 to 29 (2025 release wave 1 to 2026 release wave 2). Use the
existing slide master, theme, fonts and colours.

WORK IN THIS ORDER
1. Show me the outline (slide titles, grouped by section) and wait for "go".
2. Build the slides below in this order, with sections as named.
3. Where a screenshot is useful and none is in this file, insert a grey
   placeholder box "SCREENSHOT: <what to show>". Do not search for or
   generate images.
4. Put the notes I give into each slide's speaker notes.
5. At the end, list all placeholders and anything you were unsure about.

HARD RULES
- Content below is verified. Do not add features, versions, dates, numbers,
  licence claims or report IDs that are not in this prompt. If something
  seems missing, ask me.
- Use the version/wave labels exactly as given. Where I write UNKNOWN or
  "not documented", show it that way; do not fill the gap.
- English. Business Central terms exactly as written.
- Reference style is allowed: tables up to 10 rows, bullets up to 8 per
  slide, short phrases. No marketing words ("seamless", "powerful",
  "improved experience").
- Every content slide gets a small source line at the bottom (given below).
- Version key used in the deck: v26 = 2025 wave 1, v27 = 2025 wave 2,
  v28 = 2026 wave 1, v29 = 2026 wave 2.

=====================================================================
SECTION 1: INTRODUCTION
=====================================================================

1. Title
   Title: Excel layouts in Business Central
   Subtitle: What's new from 2025 wave 1 to 2026 wave 2 (v26-v29) ·
   reference deck · November 2026

2. How to read this deck
   Bullets:
   - Two kinds of news: capabilities and content
   - Capabilities: work with any report's Excel layout
   - Content: Microsoft reports that got an Excel layout
   - Version key: v26 = 2025 wave 1 · v27 = 2025 wave 2 ·
     v28 = 2026 wave 1 · v29 = 2026 wave 2
   - Verified against Microsoft Learn, the Microsoft 365 roadmap
     and yzhums.com walkthroughs
   - UNKNOWN means no source states it
   Source line: Microsoft Learn: What's new 26.0, 27.0, 28.0, 29.0

3. At a glance: count per version
   Table "Version | Capabilities | Reports with new or improved Excel layout":
   - v26 (2025 wave 1) | 4 | 13
   - v27 (2025 wave 2) | 0 | 16
   - v28 (2026 wave 1) | 1 | 21 entries (16 layout changes, 5 performance)
   - v29 (2026 wave 2) | 2 (1 developer-only) | 0 found
   Takeaway line under the table: "Most news is content: standard reports
   moved from RDL to Excel. Few new platform capabilities."
   Source line: research based on release plans 2025w1-2026w1 and What's new 29.0

4. What an Excel layout is (basics)
   Bullets:
   - A workbook (.xlsx) that Business Central fills with report data
   - Data lands in a "Data" sheet (or one sheet per data item)
   - Your own sheets build on it: formulas, pivots, slicers, charts
   - Filters and options from the request page go into hidden metadata sheets
   - Run: opens in Excel online with OneDrive, otherwise downloads
   - No Print or Preview button: download, then print from Excel
   Source line: Microsoft Learn: Excel report layouts · Run and print reports
   · Excel layout developer guide

=====================================================================
SECTION 2: CAPABILITIES (work with any report)
=====================================================================

5. Capabilities overview
   Table "# | Capability | Version | Who, without developer?":
   - C1 | Validate a layout | v26 | Yes, admin
   - C2 | Mark layout as obsolete | v26 | Partly (user layouts yes; extension layouts need AL)
   - C3 | Multiple data sheets set per layout | v26 | Partly (AL property; client toggle)
   - C4 | Layout name, caption, ID inside the workbook | v26.0 | Yes
   - C5 | Layout statuses: Draft, Pending Approval, Approved, Retired | v28 | Yes
   - C6 | Lifecycle for all layout types | v29 | Yes (details not documented)
   - C7 | Portable layout paths in AL (runtime 18) | v29 | No, developer only
   Source line: release plans 2025w1, 2026w1 · What's new 29.0

6. C1 · Validate a layout  (v26, GA 1 April 2025, automatic)
   What: an admin checks an uploaded layout and gets a list of errors.
   How:
   1. Search Report Layouts
   2. Select the user-defined layout
   3. Choose Validate
   4. Read the results, fix the workbook, Replace Layout
   Checks: real .xlsx, not password protected, valid Data sheet.
   Limit: checks structure, not whether the numbers are right.
   Value: fewer broken reports; no developer to diagnose a bad file.
   Visual: placeholder "SCREENSHOT: Validate result dialog on Report Layouts".
   Source line: Release plan 2025 wave 1: validate report layouts ·
   Learn: Get started with layouts (Validate a layout)

7. C2 · Mark a layout as obsolete  (v26, GA 1 April 2025)
   What: flag a layout as deprecated; Obsolete column on Report Layouts.
   How (user-defined layout): Report Layouts > select > Edit Info >
   Mark layout as obsolete > OK.
   Developers: ObsoleteState, ObsoleteReason, ObsoleteTag on the layout in AL.
   Limits: extension layouts can't be marked from the client. The version in
   which the client toggle appeared: UNKNOWN.
   Source line: Release plan 2025 wave 1: use new properties on a report layout

8. C3 · Multiple data sheets, set per layout  (v26, runtime 15)
   What: one data sheet per data item (#DataItemName), for a Power Pivot
   data model. New in v26: set per layout, so a new multi-sheet layout
   doesn't break older single-sheet layouts. (The report-level property
   is older.)
   How: developer sets ExcelLayoutMultipleDataSheets; in the client,
   New layout > Excel > "Create Multiple Data Sheets" toggle > upload.
   Limits: keep generated sheet, table and column names; single-sheet
   layouts need a "Data" sheet and table starting at A1.
   Source line: Release plan 2025 wave 1: new properties · Learn: Excel
   layout developer guide

9. C4 · Which layout produced this file?  (v26.0)
   What: the hidden metadata sheet holds Layout name, caption and ID
   (table ReportRequestValues), so a title or footer can show it.
   Limit: sheet is hidden; needs Excel table formulas.
   Source line: Learn: Excel layout developer guide

10. C5 · Layout statuses  (v28, GA 1 May 2026, automatic)
    What: every layout has a status: Draft, Pending Approval, Approved,
    Retired. Only Approved layouts can be chosen on the request page.
    How: Report Layouts > select one or more > Layout > Layout Status >
    Set Draft / Pending Approval / Approved / Retired.
    Extension layouts: a status change is saved as an override; the
    original stays unchanged.
    Tested in 28.5: a copy of a layout starts as Draft (Dutch UI: "Concept").
    Limits: no approval workflow; status is set by hand.
    Value: nobody runs an untested layout; governance without a developer.
    Visual: placeholder "SCREENSHOT: Report Layouts with status column and
    the Layout Status menu".
    Source line: Release plan 2026 wave 1: control the lifecycle of report
    layouts · Learn: Get started with layouts (Manage layout status)

11. C6 and C7 · Version 29 items
    C6 Control the lifecycle of all report layouts (roadmap 573320, GA):
    - Microsoft lists it as new in 29.0
    - Learn docs say new or replaced layouts start as Draft "in version 29"
    - But copies already start as Draft in 28.5 (tested)
    - What "all layout types" adds beyond v28: not documented
    C7 Portable layout paths (runtime 18): / and \ both work in AL layout
    paths. Developer only.
    Source line: What's new 29.0 · Microsoft 365 roadmap 573320 · Learn:
    Declare report layouts in AL
    Notes: "Don't present C6 as a headline: the visible part already
    works in 28.5."

=====================================================================
SECTION 3: CONTENT (Microsoft reports with Excel layouts)
=====================================================================

12. v26 (2025 wave 1): finance, purchasing, sustainability
    Table "Area | Report (ID) | GA":
    - Finance | Trial Balance (4405), Trial Balance by Period (38), Trial Balance Previous Year (7), Trial Balance/Budget (4406), Consolidated Trial Balance (4410) | 1 Apr 2025
    - Receivables/payables | Aged Accounts Receivable Excel (4402), Aged Accounts Payable Excel (4403) | 2025 wave 1 (sources give 1 Apr and 15 Jun 2025)
    - Fixed assets | Fixed Asset Details Excel (4411), Fixed Asset Projected Value Excel (4413) | 1 Apr 2025
    - Purchasing | Vendor - Top 10 List Excel (4404) | 15 Jun 2025
    - Sustainability | Emission By Category (6210), Emission Per Facility (6211), Total Emissions (6212) | 15 Jun 2025
    Source line: Release plans 2025 wave 1: finance, sales, purchasing,
    sustainability analytics · Learn: Report overview

13. v27 (2025 wave 2): sales, deferrals, manufacturing
    Table "Area | Report (ID) | Change":
    - Sales | Customer List (101), Customer - Order Summary (107), Customer - Order Detail (108), Sales Statistics (112), Customer/Item Sales (113), Customer Balance to Date (121), Customer Trial Balance (129), Sales Reservation Avail. (209), Inventory Order Details (708), Inventory Sales Back Orders (718) | RDL replaced by Word and Excel layouts
    - Deferrals | G/L Deferral Summary (1700), Sales Deferral Summary (1701), Purchasing Deferral Summary (1702) | RDL replaced by Word and Excel layouts
    - Manufacturing | Quantity Explosion of BOM (99000753), Where-Used (Top Level) (99000757) | RDL replaced
    - Manufacturing | Production Order - List (99000763) | New report, Excel, two worksheets
    All GA 1 October 2025.
    Source line: Release plans 2025 wave 2: sales analytics, deferral
    reporting, manufacturing analytics · Learn: Report overview

14. v28 (2026 wave 1): inventory modernised
    Table "Report (ID) | Change":
    - Inventory Top 10 List (711) | RDL replaced by Excel and Word
    - Item Availability (705) | same
    - Inventory Purchase Orders (709) | same
    - Item/Vendor Catalog (720) | same
    - Inventory - Availability Plan Excel (719) | new Excel report; replaces 707
    - Inventory - Transaction Detail (704) | same
    - Item Expiration - Quantity (5809) | same
    - Item Age Composition by Quantity and Value (ID UNKNOWN) | new; old 5807, 5808 deprecated
    GA 1 April 2026.
    Source line: Release plan 2026 wave 1: modernizing analytical reports
    for inventory · Learn: Report overview

15. v28 (2026 wave 1): subtotals and speed
    Table "What | Reports | GA":
    - Subtotals added to Excel layouts | Salesperson Commission (115), Customer/Item Sales (113), Inventory Order Details (708), Inventory Customer Sales (713), Inventory - Sales Back Orders (718) | 1 Apr 2026
    - Subtotals added to Excel layouts | Deferral Summary G/L (1700), Sales (1701), Purchase (1702) | 1 May 2026
    - Faster (performance only) | Trial Balance (4405), Consolidated (4410), Budget (4406), by Period (38), Previous Year (7) | 1 May 2026
    Note line: "Faster trial balance: a Feature Management switch, enabled by
    default from v28."
    Source line: Release plans 2026 wave 1: sales scenarios; deferrals and
    trial balances · Learn: Optional features now mandatory

16. v29 (2026 wave 2): content
    Big text: "No new or improved Microsoft Excel layout found in v29."
    Bullets:
    - Not Excel layouts, but nearby in v29:
    - Automate report outputs (573318): new report inbox APIs for
      Power Automate or MCP; no scheduling, no Excel layout change
    - Monitor usage of Open in Excel with telemetry (573317)
    - Run multiple financial reports, single PDF (573323)
    Source line: What's new 29.0 · Microsoft 365 roadmap 573318

=====================================================================
SECTION 4: POSITIONING
=====================================================================

17. Excel layouts vs analysis mode vs Power BI
    Table, 4 columns: Criterion | Excel layouts | Analysis mode | Power BI
    - Who builds it | Key user in Excel; AL for packaged | End user, no build | Apps: install; custom: Power BI Desktop
    - Who maintains | Layout owner; statuses | Each user, own views | Workspace admin; app updates can overwrite
    - Extra licence | None stated | Permission set DATA ANALYSIS - EXEC | Power BI Pro per viewer, or Premium/Fabric
    - Freshness | Snapshot at run time | Live when opened | Last refresh; 8/day shared, 48 Premium
    - Volume | Up to 10M rows, 12 h (online max) | Large-data mode above 100,000 rows | Refresh under 2 h shared
    - Combining data | Report dataset; several data sheets | Related-table fields since 26.2 | Many APIs; cross-company via Power Query
    - Printing | Download, print from Excel | Not stated | Not stated
    - Scheduling | Job queue to Report Inbox | None found | Scheduled refresh
    - Sharing | Layout per company or all companies | Views private; share a link | Licence per viewer; one app per company
    - Fit with Excel habits | Formulas, pivots, slicers | Pivot-like | Separate tool (opinion)
    Source line: Learn: Excel layouts · Run reports · Analysis mode · Install
    Power BI apps · Power BI data refresh · BC as Power BI data source
    Notes: "Excel layouts sit in the middle: more finished and repeatable
    than analysis mode, but lighter and cheaper than Power BI."

18. Pick Excel layouts when / not when
    Two columns.
    Pick when:
    - Month-end analysis on a standard report, own formatting
    - Several variants per role, no Power BI licences
    - Users live in Excel: formulas, slicers, charts
    Not when:
    - Invoices or print-perfect output: use Word (email layouts must be Word)
    - A one-off question: analysis mode is faster
    - Live dashboard for many viewers, or cross-company: Power BI
    - Scheduled email to many people: not documented for Excel output
    Source line: Learn: Report layouts overview · Run reports (rest is
    consultant judgement)

19. Limits to know
    Bullets:
    - Online: default max 500,000 rows; up to 10,000,000 when raised
    - Default max run time 6 h; up to 12 h
    - Excel's own sheet limits apply on top
    - No Print or Preview: download first
    - Extension layouts: edit a copy, not the original
    - Multi-sheet layouts: keep generated sheet and table names
    Source line: Learn: Operational limits online · Run reports · Excel
    report layouts

=====================================================================
SECTION 5: DEMO
=====================================================================

20. Demo report: Customer/Item Sales (113)
    Bullets:
    - Excel layout since v27; subtotals since v28
    - Tested: runs in 28.5
    - Filters: Posting Date, Item No.
    - Print sheet and analysis sheet
    - Use case: sales controller, monthly after closing
    - Fallbacks: Trial Balance Excel (4405), Aged Accounts Receivable Excel (4402)
    Source line: Learn: report 113 · Release plan 2026 wave 1 sales scenarios

21. Demo path (5:30)
    Table "# | Time | Action | Shows":
    1 | 0:40 | Open Customer/Item Sales, set Posting Date and Item No. | Run-time filters
    2 | 0:25 | Pick the Excel layout, run | Standard report in Excel (v27)
    3 | 0:55 | Print sheet, analysis sheet, subtotals | Subtotals (v28)
    4 | 0:35 | Slicer or filter, collapse a group | Excel habits on BC data
    5 | 0:15 | Data sheet, close | Raw data for own formulas
    6 | 0:25 | Report Layouts, filter 113, status column | One page for all layouts
    7 | 0:35 | Edit Info > Save Changes to Copy; copy is Draft | Copy starts Draft
    8 | 0:25 | Validate the copy | C1 (v26)
    9 | 0:40 | Request page: copy missing; Set Approved; now listed | C5 (v28)
    10 | 0:35 | Recap with the use case | —
    Source line: decision pack, 19 Nov 2026

=====================================================================
SECTION 6: OPEN POINTS AND SOURCES
=====================================================================

22. Open points
    Bullets:
    - v29 "lifecycle for all layout types": what changed is not documented
    - Mark-as-obsolete client toggle: version UNKNOWN
    - Item Age Composition by Quantity and Value: report ID UNKNOWN
    - Item/Vendor Catalog = 720: matched by name only
    - Aged AR/AP Excel GA date: 1 Apr vs 15 Jun 2025 (both v26)
    - Emailing Excel layout output: not documented
    - Report 113 analysis sheet slicers: check in the environment

23. Sources
    - Microsoft Learn: What's new in Business Central 26.0, 27.0, 28.0, 29.0
    - Microsoft Learn: Excel report layouts; Get started with layouts;
      Run and print reports; Excel layout developer guide; Report overview;
      Operational limits online; Analysis mode; Power BI apps
    - Release plans 2025 wave 1: validate layouts; new layout properties;
      finance, sales, purchasing, sustainability analytics
    - Release plans 2025 wave 2: sales analytics; deferral reporting;
      manufacturing analytics
    - Release plans 2026 wave 1: lifecycle of report layouts; inventory
      reports; sales scenarios; deferrals and trial balances
    - Microsoft 365 roadmap 573317, 573318, 573320, 573323
    - yzhums.com walkthroughs (Business Central posts)
```
