# Prompt for Claude chat: Word document on Excel layouts

How to use:
1. Open a new chat on claude.ai and paste everything between the two lines below.
2. Optional: attach `output/decision-pack.md` and `research/excel-v26-v29.md` for extra detail. The prompt says which source wins if they disagree.
3. Claude returns a .docx file. Check section 8 ("Not verified") before you share it with clients.

Content verified on 18–19 Nov 2026 in two passes (`research/verification.md`, `research/verification-2.md`).

---

```text
TASK
Create a Word document (.docx) for me: a reference document on Excel report
layouts in Microsoft Dynamics 365 Business Central, covering what is new from
2025 release wave 1 to 2026 release wave 2 (versions 26 to 29), how it works,
how it compares with analysis mode and Power BI, and a demo script.

I am a Business Central consultant. Readers: colleagues and client key users
and decision-makers (Flemish SMEs on Business Central online). Language: English.

HARD RULES
- Use ONLY the facts in this message (and attached files, if any). Do not add
  features, versions, dates, report numbers, licence or price claims from your
  own knowledge. If something seems missing, write "Not verified" instead.
- If an attached file disagrees with this message, this message wins.
  Ignore anything an attached file marks UNVERIFIED, WRONG or UNKNOWN unless it
  is listed in section 8 below.
- Keep version labels exactly as given ("v28", "2026 wave 1", "28.x").
- Plain English, short sentences, tables over prose. Value statements name a
  concrete outcome (time saved, no developer needed, fewer errors), never
  "improved experience", "seamless" or "powerful".
- Paraphrase; do not quote Microsoft text.

DOCUMENT FORMAT
- A4, portrait. Title page, table of contents, page numbers, heading styles
  (Heading 1/2) so the TOC works.
- Tables with a header row, light shading, readable on print.
- Sources as clickable hyperlinks.
- Length: about 10-14 pages.

STRUCTURE AND CONTENT

Title page
  Title: Excel layouts in Business Central: what's new (versions 26-29)
  Subtitle: Reference and demo guide · November 2026
  Line: Based on Microsoft Learn, the Microsoft 365 roadmap and community
  walkthroughs; verified 19 November 2026.

1. Summary (half a page)
- About 37 standard reports moved from RDL to Excel layouts between
  2025 wave 1 and 2026 wave 1. Users open them; nobody builds them.
- New management capabilities without a developer: Validate a layout (v26),
  layout statuses Draft / Pending Approval / Approved / Retired (28.x).
- 2026 wave 1 added subtotals to sales and deferral Excel reports.
- Version 29 adds almost nothing specific to Excel layouts: statuses now cover
  all layout types (details not documented) and a developer-only path change.
- Excel layouts sit between analysis mode and Power BI (section 5).

2. Excel layouts in short: how they work
- A report's data is merged into an Excel workbook at run time. Single-sheet
  layouts use a sheet and table named "Data" starting at A1; multi-sheet
  layouts get one sheet per data item (#DataItemName).
- Request-page options and filters are stored in hidden metadata sheets, so
  formulas can show which filters were used.
- Users choose the Excel layout on the request page and run the report. With
  OneDrive set up it opens in Excel for the web; otherwise it downloads.
- No Print or Preview button for Excel layouts: download, then print from Excel.
- Reports can be scheduled via the job queue; output lands in the Report Inbox.
- Layouts can be made available in one company or all companies.
- Limits online: default max 500,000 rows (can be raised per report),
  absolute max 10,000,000 rows; default max run time 6 hours, max 12 hours.
  Excel's own sheet limits also apply.
- The layout file must be a real .xlsx, not password protected, with a valid
  data sheet.
- Email body layouts must be Word, not Excel.
- Who builds: a key user or consultant in Excel; developers in AL for
  layouts shipped in extensions.

3. What's new, wave by wave

3.1 Capabilities (work in any report)
Table columns: Capability | Version / wave | Who can use it | What it does |
Value for users | Value for decision-makers
- Validate a layout | v26, 2025 wave 1 (GA 1 Apr 2025) | Admin, no developer |
  Checks an uploaded layout and lists errors | Fewer broken reports after an
  upload | Less support time; no developer needed to diagnose a bad file
- Obsolete state for layouts | v26, 2025 wave 1 | Developer (AL property
  ObsoleteState); users can mark their own user-defined layouts via Edit Info >
  "Mark layout as obsolete" (version of that toggle not verified) | Flags a
  layout as deprecated; an Obsolete column shows on Report Layouts | Clear
  "stop using this" signal | Smoother clean-up of old layouts
- Multiple data sheets set per layout | v26, 2025 wave 1 (runtime 15); the
  global report property is older | Developer property; "Create Multiple Data
  Sheets" toggle when adding a layout | One data sheet per data item, for Power
  Pivot / data models | Pivots across several tables | New layouts without
  breaking older custom ones
- Layout name, caption and ID in the workbook metadata | v26.0 | Automatic |
  The hidden metadata sheet records which layout produced the file | Trace a
  file to its layout | Audit trail
- More fields in the hidden Aggregated Metadata sheet (object caption, local
  date, UTC offset) | v27 (community source: yzhums.com/67838) | Automatic |
  Extra context for formulas and titles | Show run date in local time |
  Minor
- Layout lifecycle statuses: Draft, Pending Approval, Approved, Retired |
  28.x, 2026 wave 1 (release plan GA 1 May 2026; Learn lists it under 28.0 and
  28.1) | Admin, no developer | Only Approved layouts can be chosen on the
  request page; set via Layout > Layout Status, several layouts at once; a
  status change on an extension layout is stored as an override | Users only
  see tested layouts | Nobody runs an untested layout; approval step without a
  developer
  Note: a new copy of a layout already starts as Draft in 28.5 (tested,
  shown as "Concept" in the Dutch UI).
- Lifecycle for all layout types | v29, 2026 wave 2 (roadmap 573320) | Admin |
  Roadmap says statuses now apply to all layout types, including shipped,
  per-tenant extension and AppSource layouts. Microsoft does not document what
  changed versus 28.x; in 28.x an extension layout's status could not be
  changed (community source). Learn says in v29 a replaced layout resets to
  Draft. | — | —
- Portable layout paths in AL (runtime 18) | v29 | Developer only | Layout
  file paths accept / and \ on any OS | none | Partner build convenience

3.2 Content: standard reports with new or improved Excel layouts
Table per wave. Columns: Area | Report (ID) | What changed | GA date.

2025 wave 1 (v26)
- Finance | Trial Balance Previous Year (7), Trial Balance (4405), Trial
  Balance by Period (38), Trial Balance/Budget (4406), Consolidated Trial
  Balance (4410) | Excel reports | 1 Apr 2025
- Finance | Aged Accounts Receivable Excel (4402), Aged Accounts Payable
  Excel (4403) | Excel reports | 1 Apr 2025 (finance plan) / 15 Jun 2025
  (sales and purchasing plans); say "2025 wave 1"
- Fixed assets | Fixed Asset Details Excel (4411), Fixed Asset Projected
  Value Excel (4413) | Excel reports | 1 Apr 2025
- Purchasing | Vendor - Top 10 List Excel (4404) | Excel report | 15 Jun 2025
- Sustainability | Emission By Category (6210), Emission Per Facility (6211),
  Total Emissions (6212) | Layouts for print and pivot analysis | 15 Jun 2025

2025 wave 2 (v27)
- Deferrals | G/L Deferral Summary (1700), Sales Deferral Summary (1701),
  Purchasing Deferral Summary (1702) | RDL replaced by Word and Excel layouts
  | 1 Oct 2025
- Sales | Customer List (101), Customer - Order Summary (107), Customer -
  Order Detail (108), Sales Statistics (112), Customer/Item Sales (113),
  Customer Balance to Date (121), Customer Trial Balance (129), Sales
  Reservation Avail. (209), Inventory Order Details (708), Inventory Sales Back
  Orders (718) | Modernised: RDL replaced by Word and Excel layouts | 1 Oct 2025
- Manufacturing | Quantity Explosion of BOM (99000753), Where-Used (Top Level)
  (99000757) | Modernised | 1 Oct 2025
- Manufacturing | Production Order - List (99000763) | New Excel-based report,
  overview and analysis sheets | 1 Oct 2025

2026 wave 1 (v28)
- Inventory | Inventory Top 10 List (711), Item Availability (705), Inventory
  Purchase Orders (709), Item/Vendor Catalog (720), Inventory - Availability
  Plan Excel (719, replaces 707), Inventory - Transaction Detail (704), Item
  Expiration - Quantity (5809) | Modernised: RDL replaced by Excel and Word |
  1 Apr 2026
- Inventory | Item Age Composition by Quantity and Value (new; ID not
  verified) | New report with Excel and Word layouts; old Item Age Composition
  reports (5807, 5808) deprecated | 1 Apr 2026
- Sales | Salesperson Commission (115), Customer/Item Sales (113), Inventory
  Order Details (708), Inventory Customer Sales (713), Inventory - Sales Back
  Orders (718) | Subtotals added to the Excel layouts | 1 Apr 2026
- Deferrals | 1700, 1701, 1702 | Subtotals added to the Excel layouts |
  1 May 2026
- Finance | Trial balance family (7, 38, 4405, 4406, 4410) | Faster
  (performance only). Feature Management item, enabled by default from v28 |
  1 May 2026

2026 wave 2 (v29)
- No standard report with a new or improved Excel layout found.

3.3 Count per wave (put in a small table)
v26: 4 capabilities, 13 reports · v27: 1 minor capability, 16 reports ·
v28: 1 capability, 21 report entries (16 layout changes, 5 performance) ·
v29: 2 capabilities (one developer-only), 0 reports.

4. Not Excel layout features (to avoid confusion)
- "Automate report outputs" (v29, roadmap 573318): new report inbox APIs for
  Power Automate or MCP. No Excel, scheduling or layout content.
- Financial Reporting enhancements (scheduling to groups, PDF): Financial
  Reporting, not Excel layouts.
- "Monitor usage of Open in Excel with telemetry" (v29): list export, not
  layouts.
- Company Information data item in report datasets (v29): Word layouts only.

5. Excel layouts vs analysis mode vs Power BI
5.1 Comparison table (columns: Criterion | Excel layouts | Analysis mode |
Power BI)
- Who builds it | Key user or consultant in Excel; AL for packaged ones | End
  user drags fields; no build | Apps: install; custom: Power BI Desktop skills
- Who maintains | Layout owner; statuses (28.x) | Each user, own views |
  Workspace admin; app updates can overwrite edits
- Extra licence | None stated by Microsoft | Permission set DATA ANALYSIS -
  EXEC | Power BI Pro per viewer, or Premium/Fabric capacity; apps are free
- Freshness | Snapshot at run time | Live when opened | Last refresh: up to 8
  a day on shared capacity, 48 on Premium
- Volume | Up to 10M rows, 12 h (online max) | Large-data mode above 100,000
  rows | Refresh under 2 h on shared capacity; 8-minute call limit
- Combining data | Report dataset; several data sheets possible |
  Related-table fields since 26.2 | Many APIs; cross-company via Power Query
- Printing / fixed layout | Download, print from Excel | Not stated by
  Microsoft | Not stated by Microsoft
- Scheduling | Job queue to Report Inbox | None found | Scheduled data refresh
- Sharing | Layout per company or all companies | Views private; share a
  link | Licence per viewer; one app install per company
- Run-time filters | Request page plus slicers in the workbook | Column
  filters per view | Slicers; environment and company parameters
- Governance | BC permissions plus Excel sheet protection and sensitivity
  labels | Admin can withhold the permission set | Workspace access plus BC
  read permission for the refresh user
- Fit with Excel habits | Highest: formulas, pivots, slicers | Pivot-like,
  not Excel | Separate tool (opinion)

5.2 Pick this when (three bullets per tool)
Excel layouts:
- Finance wants the aged receivables pivot every month-end, in their own
  format, with an extra column.
- Ten variants of one report for different roles, without buying Power BI
  licences.
- The client lives in Excel and wants slicers, charts and formulas on a
  report they run on demand.
Analysis mode:
- A sales manager needs "who owes us more than 10,000 and since when" in two
  minutes.
- An auditor groups ledger entries by month and customer during a call, then
  discards the view.
- A power user tests an idea on a few hundred thousand entries before anyone
  builds a report.
Power BI:
- The board wants a daily dashboard across sales, finance and inventory on any
  device; data a few hours old is fine.
- A group with several companies needs one consolidated view.
- The client wants the shipped Power BI apps running quickly and already pays
  for Power BI Pro or Premium.

5.3 When Excel layouts are the wrong choice
- Customer-facing or print-perfect documents: use Word.
- A one-off question: analysis mode is faster.
- An always-on dashboard for many viewers, or cross-company consolidation:
  Power BI.
- Scheduled email delivery to many people: not documented for Excel output;
  don't promise it.
- Fully locked-down numbers: a downloaded file can be changed; protection
  helps, but a central Power BI model is easier to control (opinion).

5.4 One sentence to say out loud
"Excel layouts sit in the middle: more finished and repeatable than analysis
mode, which is a quick look you build yourself, but lighter and cheaper than
Power BI, which is a separate dashboard tool with its own licences and
refresh schedule."

6. Demo guide: Customer/Item Sales (report 113), 5.5 minutes, version 28.5
Why this report: Excel layout since v27, subtotals since v28, so both are in
28.5; sales per customer and item speaks to finance and operations. Tested:
it works in 28.5.
Use case: a sales controller at a distribution company runs it monthly after
closing, filters top customers, checks discount against profit per item, adds
a comment column and sends it on. The subtotals now come built in.
Admin angle: one approved copy of the layout; nobody runs an untested one.
(Illustrative scenario.)

Table: # | Time | Action | What to say
1 | 0:40 | Search (Alt+Q) "Customer/Item Sales"; set Posting Date to a range
  with data; narrow Item No. | Run-time filters, no developer
2 | 0:25 | Pick the Excel layout and run | Same data, Excel instead of RDL
3 | 0:55 | Print sheet, then analysis sheet; point at subtotals per customer
  | v28: subtotals built in
4 | 0:35 | Use a slicer or filter, collapse a group | What Excel users know
5 | 0:15 | Show the raw data sheet, close (drop if late) | Your own formulas
  and pivots
6 | 0:25 | Report Layouts, filter report 113, point at the status column |
  One page for all layouts
7 | 0:35 | Edit Info > new name > Save Changes to Copy; the copy shows status
  Draft ("Concept" in Dutch) | The Microsoft original stays untouched
8 | 0:25 | Validate the copy | v26: check without a developer
9 | 0:40 | Request page: the Draft copy is not listed; Set Approved; now it is
  | 28.x: only approved layouts reach users
10 | 0:35 | Recap with the use case | Subtotals, Validate, statuses
Total 5:30.
Fallbacks: Trial Balance Excel (4405), then Aged Accounts Receivable Excel
(4402); steps 6-10 stay the same.
Before the demo: check the analysis sheet has a slicer or pivot, check the
Draft copy is absent from the request page, take a backup screenshot of each
step.

7. Limits and gotchas (bullets)
- No Print/Preview for Excel layouts; download first.
- Keep the generated Data sheet/table names; multi-sheet layouts must keep
  their generated sheets and columns.
- Microsoft-shipped (extension) layouts can't be edited: make a copy.
- A copy starts as Draft and is invisible to users until Approved.
- In v29 replacing a layout resets it to Draft: re-approve after every change.
- Row and time limits online (section 2).
- Excel layouts can't be used as email body layouts.

8. Not verified (list honestly in the document)
- What "statuses for all layout types" in v29 adds beyond 28.x.
- Whether the analysis sheet of report 113 has slicers.
- Offline use, print/PDF for analysis mode and Power BI, Power BI
  subscriptions, emailing Excel layout output.
- Version in which the "Mark layout as obsolete" toggle appeared.
- ID of the new Item Age Composition report.
- Deprecation of legacy finance reports in v28 (seen only in a search
  snippet).

9. Sources (hyperlinks)
Microsoft Learn:
- Excel report layouts:
  https://learn.microsoft.com/en-us/dynamics365/business-central/ui-excel-report-layouts
- Get started with report layouts:
  https://learn.microsoft.com/en-us/dynamics365/business-central/ui-get-started-layouts
- Run and print reports:
  https://learn.microsoft.com/en-us/dynamics365/business-central/ui-work-report
- Excel layout developer guide:
  https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-howto-excel-report-layout
- Report overview:
  https://learn.microsoft.com/en-us/dynamics365/business-central/reports-available-reports
- Report 113:
  https://learn.microsoft.com/en-us/dynamics365/business-central/reports/report-113
- What's new 29.0:
  https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-29-0
- Analysis mode:
  https://learn.microsoft.com/en-us/dynamics365/business-central/analysis-mode
- Install Power BI apps:
  https://learn.microsoft.com/en-us/dynamics365/business-central/across-powerbi-install-business-central-apps
- Power BI data refresh:
  https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-data
- Operational limits online:
  https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/operational-limits-online
Release plans:
- Validate layouts (2025 wave 1):
  https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/validate-report-layouts-errors-as-admin
- New layout properties (2025 wave 1):
  https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-new-properties-report-layout
- Finance analytics (2025 wave 1):
  https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365-business-central/use-enhanced-analytics-finance
- Sales analytics (2025 wave 2):
  https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/smb/dynamics365-business-central/use-enhanced-sales-analytics
- Deferral reporting (2025 wave 2):
  https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/smb/dynamics365-business-central/deferral-reporting-enhancements
- Inventory reports (2026 wave 1):
  https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/modernizing-analytical-reports-inventory
- Sales subtotals (2026 wave 1):
  https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/analyze-customer-loyalty-other-sales-scenarios
- Deferral subtotals and faster trial balances (2026 wave 1):
  https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/use-enhanced-faster-reports-analysis-deferrals-trial-balances
- Layout lifecycle (2026 wave 1):
  https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/control-lifecycle-report-layouts
Roadmap: https://mc.merill.net/message/RM573320
Walkthroughs: https://yzhums.com/73030/ (sales subtotals),
https://yzhums.com/73485/ (deferral subtotals), https://yzhums.com/72933/
(layout statuses), https://yzhums.com/67838/ (metadata fields)

When done, give me the .docx and a 3-line summary of anything you could not
place or format.
```
