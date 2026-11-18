# Demo report recommendation: Excel layouts (5.5 minutes, live, version 28.5)

Research subagent D. Written 2026-11-18. Input: research/excel-v26-v29.md (capability IDs C1 to C9 refer to its section 1).

## 0. Honest limits

- Nothing here was run in a live environment. "Returns data on Cronus" is NOT verified for any candidate. I could not check Cronus demo data content from documentation. Do a 2-minute dry run in the 28.5 demo environment before the talk (checklist in section 6).
- Version 29 sandbox assumed not available: all v29 items are "slide only".
- Pages opened for this note (Microsoft Learn): report overview https://learn.microsoft.com/en-us/dynamics365/business-central/reports-available-reports ; report pages .../business-central/reports/report-113, report-4402, report-4405 ; https://learn.microsoft.com/en-us/dynamics365/business-central/ui-excel-report-layouts ; https://learn.microsoft.com/en-us/dynamics365/business-central/ui-get-started-layouts ; release plan https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/analyze-customer-loyalty-other-sales-scenarios
- Whether the ID 113 Excel layout uses a multi-sheet data model: UNKNOWN.

## 1. Candidates scored

Scale: 3 = strong, 2 = acceptable, 1 = weak, ? = cannot be verified from sources. Scores are my judgement from the opened pages.

| Criterion | A. Customer/Item Sales (113) | B. Aged Accounts Receivable Excel (4402) | C. Trial Balance Excel (4405) |
|---|---|---|---|
| Exists with a Microsoft Excel layout in 28.5; since when | 3. Excel layout introduced 2025 wave 2 (v27), per the report page "Available layouts". Subtotals added in 2026 wave 1 (v28), per the release plan page. Both in 28.5. | 3. Excel report listed in the 2025 wave 1 release plan (v26); version of first release has a source conflict: Apr 1, 2025 on the finance plan, Jun 15, 2025 on the sales plan (see input file C-table). Exists in 28.5. | 3. Listed in the 2025 wave 1 finance plan (v26); whether new or improved in v26: UNKNOWN. Speed-up in v28 is a Feature Management item, so not automatic (input file section 2). Exists in 28.5. |
| Meaningful output on Cronus without setup | ? Needs posted sales within the Posting Date filter. Cronus dates are relative to the workdate: UNKNOWN. Risk: empty or thin. | ? Needs open customer ledger entries; "Aged as of" date drives buckets. Likely populated but UNVERIFIED. | ? G/L entries exist in any Cronus company, so likely populated, but UNVERIFIED. |
| Recognisable to finance and operations | 3. Sales per customer and item: operations know the items, finance knows amounts and profit. | 2. Strong for finance; operations less so. | 2. Finance only. Operations people rarely open it. |
| Number of capabilities from table 1 it can show | 3. Subtotals in the Excel layout (v28 content) plus all Report Layouts page capabilities (C1 Validate, C2 Obsolete, C5 lifecycle) via a copy of its layout. | 2. Same Report Layouts page capabilities, no v28 subtotals feature. Four sheets with slicers show Excel strengths well. | 2. Same platform capabilities. v28 speed-up is not visible in a demo. Four sheets incl. printable list. |
| Fast and with run-time filters worth showing | 2. Filters Posting Date and Item No. (report page). Speed UNKNOWN; summarises value entries, so can be slower on big data, fine on Cronus. | 3. Request page parameters "Aged as of" and "Period length"; summarised by the two global dimensions. | 3. Date Filter and "Hide Accounts with No Activity" are good, simple filters; v28 made it faster. |
| Total (out of 15, "?" counted as 2) | 13 | 12 | 12 |

**Recommended: A, Customer/Item Sales (report ID 113).**
Reason in one line: it is the only candidate that shows a v28 content change (subtotals) live, and sales per customer and item speaks to both audiences.
Note that the platform capabilities (Validate, Obsolete, lifecycle) are report-independent, so any candidate would show those equally. The decisive differences are the subtotals and the audience fit.

## 2. What the recommended report can show

| Capability (input file ID) | Wave, version | Status in the demo | Source opened |
|---|---|---|---|
| Subtotals in the Excel layout of built-in sales reports (content item, Customer/Item Sales named explicitly) | 2026 wave 1, v28 | Demoable in her version (28.5), provided the 28.5 build contains the change: it should, GA Apr 1, 2026 on the release plan; confirm in dry run | release plan page above |
| Excel layout with separate print and analysis worksheets (content item) | Report page: introduced 2025 wave 2, v27 | Demoable in her version | .../reports/report-113 |
| Validate a layout (C1) | 2025 wave 1, v26 | Demoable in her version, on a user-defined copy | .../ui-get-started-layouts ("Validate a layout") |
| Mark layout as obsolete (C2) | 2025 wave 1, v26 (release plan); client toggle version UNKNOWN | Demoable only if the Edit Info dialog in 28.5 shows the toggle; check in dry run, otherwise slide only | .../ui-get-started-layouts |
| Layout lifecycle statuses Draft, Pending Approval, Approved, Retired (C5) | 2026 wave 1, v28 | Demoable in her version (Layout > Layout Status) | .../ui-get-started-layouts ("Manage layout status"); release plan control-lifecycle-report-layouts (cited in input file) |
| Draft status by default for new or replaced user-defined layouts (C8) | 2026 wave 2, v29 (note on Excel layouts page) | Slide only. In 28.5 a new copy may start as Approved; do not claim either way | .../ui-excel-report-layouts |
| Extend lifecycle to all layouts (C8 title) | v29 | Slide only; exact v28/v29 difference UNKNOWN (input open point 3) | What's new 29.0 (cited in input file) |
| Multiple data sheets per layout (C3) | 2025 wave 1, v26 | Slide only for this report: use of multiple data sheets by 113 is UNKNOWN; the toggle exists in the New layout dialog but its version is UNKNOWN | .../ui-excel-report-layouts (Task 2 step 6) |
| Layout name in the workbook metadata (C4) | v26.0 | Slide only (hidden sheet, too technical for this audience) | developer article (cited in input file) |
| Portable layout paths (C9) | v29, runtime 18 | Skip (developer only) | developer article (cited in input file) |
| Faster trial balance Excel reports | v28 | Not on this report; slide only | input file section 2 |

Possible extra for the slide: "Automate report outputs" (v29) is title-only and UNKNOWN. Do not present it as an Excel feature.

## 3. Click-by-click path (total 5:30 = 330 seconds)

Pre-set before going live: browser logged in to the demo company in 28.5, Excel for the web or desktop Excel ready, a copy of layout NOT yet made.

| # | Time | Action | What to say or show |
|---|---|---|---|
| 1 | 0:40 | Search (Alt+Q) "Customer/Item Sales", open. On the request page set Posting Date to a range you verified has data, and filter Item No. to a small range. | Run-time filters: the user decides the slice, no developer needed. |
| 2 | 0:25 | Choose the Excel layout in the layout field of the request page, then run it (opens in Excel online if OneDrive is set up, otherwise downloads). | Same data, a different look: Excel instead of the old RDL. |
| 3 | 0:55 | In the workbook show the print sheet, then the analysis sheet. Point at the subtotals per customer. | v28 improvement: subtotals added, so users no longer add them by hand. Report page says the layout has sheets for print and for analysis. |
| 4 | 0:35 | On the analysis sheet use a slicer or filter, then expand or collapse a group. | What Excel users already know, working on live BC data. (Only if the analysis sheet has slicers or a pivot: UNKNOWN; otherwise use a plain column filter.) |
| 5 | 0:15 | Show the raw data sheet briefly (sheet tab), then close the workbook. | The data is there for your own formulas, Copilot in Excel or what-if tools (the report pages mention these). |
| 6 | 0:25 | Back in BC: Search "Report Layouts", filter on report ID 113. Point at the Excel layout row and the Obsolete and status columns. | Where all layouts of all reports are managed. |
| 7 | 0:35 | Select the Excel layout, Edit Info, give a new name, turn on "Save Changes to Copy", OK. | A user-defined copy (the original extension layout cannot be edited). Optional: toggle "Mark layout as obsolete" on the copy if present (see section 2). |
| 8 | 0:25 | Select the copy, choose Validate, show the results dialog. | v26: admin checks a layout without a developer. |
| 9 | 0:40 | Select the copy, Layout > Layout Status > Set Pending Approval, then Set Approved. Return to the report request page and show the layout list. | v28: only Approved layouts can be chosen by users. Governance in two clicks. |
| 10 | 0:35 | Switch to a slide. | v29 (October 2026): new or replaced user-defined layouts start as Draft; scope of lifecycle widened (details UNKNOWN). Close with the use case. |
| Total | 5:30 | | |

Check: 40+25+55+35+15+25+35+25+40+35 = 330 seconds.
Step 9 caveat: whether the Draft/Pending statuses visibly hide the layout on the request page in 28.5 follows from the docs, but I could not try it.
If time runs short, drop step 5 (15 s) and step 7's obsolete toggle.

## 4. Client use case to frame the demo

Who: a sales controller at a trading or distribution company that sells hundreds of items to a few hundred customers (a typical small or mid-sized BC client).
How often: monthly, after the sales and cost adjustment close; ad hoc before customer review meetings.
What they do afterwards in Excel: filter the top customers, check discount against sales amount and profit per item, add their own comment column, and send the workbook to the sales manager. The report page itself names this analysis: discounts, amounts and volumes per item sold. With the subtotals now built in, the controller no longer rebuilds them by hand each month.
Decision-maker angle: the admin keeps one approved copy of the layout (with the company's added columns); nobody runs an untested version. That is the Validate plus lifecycle story.
This is an illustrative scenario assembled from the report's documented use cases, not a statement from a real client.

## 5. Fallback if the recommended report returns empty

Fallback 1: Trial Balance Excel (4405). G/L entries exist in any company with postings. Use Date Filter and Hide Accounts with No Activity as the filters; show the printable list sheet, then the LCY analysis sheet with its slicers (documented on the report page). The v28 capabilities (steps 6 to 10) work unchanged because they are report-independent. You lose the live subtotals point: say the subtotals on a slide, with the release plan as source.
Fallback 2: Aged Accounts Receivable Excel (4402), set "Aged as of" to the workdate; use the By period (LCY) sheet.
Either way, steps 6 to 10 of the path stay identical, so switching costs only steps 1 to 5.

## 6. Dry-run checklist (15 minutes, in the 28.5 environment)

1. Run report 113 for the last 12 months and the Excel layout: does it return rows, and does it show subtotals?
2. Does the analysis sheet have a slicer or pivot?
3. Edit Info on the Excel layout: is the "Mark layout as obsolete" toggle shown?
4. After copying the layout, which status does the copy start with (Draft or Approved)? This tells whether you can say "in my version it starts as..." (only if the answer is clear).
5. After Set Pending Approval, is the copy missing from the request page layout list?
6. Screenshot each step as a backup in case of connectivity problems (no usable screenshots were downloaded from the sources; the 4402 and 4405 report pages have sheet screenshots, the 113 page has none).
