# Excel layouts vs analysis mode vs Power BI

Research for Olivia's 15-minute talk. Written 2026-11-18. Sources are Microsoft Learn pages that were opened in full (list at the bottom). Anything not stated on an opened page is marked UNKNOWN. Items marked (inference) or (opinion) are my reading, not Microsoft's statement.

Short names: **XL** = Excel report layouts. **AM** = analysis mode on list pages and queries. **PBI** = Power BI, including the shipped Power BI apps.

## 1. Comparison table

Source keys are in square brackets and map to the URL list in section 6.

| Criterion | XL | AM | PBI | Sources |
|---|---|---|---|---|
| Who builds it, skills | Consultant or power user with Excel; AL for packaged ones | End user drags fields; no build step | Shipped apps: install and configure; custom: Power BI Desktop skills | [XL1][XL3] [AM1] [PBI1][PBI3] |
| Who maintains it | Layout owner; version 29 adds Draft/Approved status | Each user, for their own views | Workspace admins; app updates can overwrite edits | [XL1] [AM1] [PBI1] |
| Licence and extra cost | No extra licence stated on the pages | Needs DATA ANALYSIS - EXEC permission, no fee stated | Paid Power BI licence per user; apps themselves free | [XL1] [AM1] [PBI1][PBI2] |
| Data freshness | Live snapshot taken when the report runs | Live list data when opened | As fresh as last refresh; up to 8 a day shared | [XL3][XL4] [AM1] [PBI1][PBI4] |
| Data volume limits | Online: 10,000,000 rows, 12 h render | Over 100,000 rows: large-data mode, trade-offs | Refresh under 2 h shared; load filters; 8 min call limit | [XL2] [AM1] [PBI1][PBI4][PBI5] |
| Combining tables or sources | Report dataset only; several data sheets possible | Related-table fields since 26.2; one page at a time | Many APIs; cross-company via Power Query | [XL3] [AM1] [PBI5] |
| Formatting, printing, fixed layout | Excel formatting; print by download then Excel | Grid only; no print layout | Rich visuals; app reports not print-fixed (UNKNOWN) | [XL2][XL3] [AM1] [PBI3] |
| Scheduling and emailing | Job queue schedule, Report Inbox, OneDrive share | None found; only a share link | Scheduled data refresh; subscriptions UNKNOWN | [XL2][XL6] [AM1] [PBI1][PBI4] |
| Sharing, reuse, companies | Layout per company or all companies | Link or exported JSON; views private by default | Share needs licences; one app install per company | [XL1] [AM1] [PBI2][PBI5] |
| Parameters and filters at run time | Request page options and filters; slicers in workbook | Column and analysis filters; list filters first | Slicers; semantic model parameters environment, company | [XL2][XL3] [AM1] [PBI2] |
| Governance and security | BC permissions; Excel sheet protection, sensitivity labels | Permission set; respects table permissions | Workspace access plus BC Read permission for refresh user | [XL1] [AM1] [PBI2] |
| Offline use | Downloaded .xlsx works in Excel (inference) | Needs the live client (inference) | UNKNOWN on opened pages | [XL2] [AM1] |
| Fit with Excel habits | Highest: formulas, PivotTables, slicers | Pivot-like, but not Excel; export option | Low; separate tool and skills (opinion) | [XL1] [AM1] [PBI5] |

### Notes behind the cells

- **Who builds / skills (XL).** Learn describes creating layouts from an exported dataset in Excel, with VS Code and AL described as the most advanced route for programmers [XL1].
- **Maintains (XL).** In version 29 a new or replaced user-defined layout starts as Draft until someone sets it as Approved [XL1]. This is a version 29 point and is also relevant to the Word/Excel layout talk.
- **Licence (XL).** The Excel layout pages do not mention extra cost. I read that as "none stated", not as a Microsoft guarantee.
- **Licence (PBI).** Template apps need a Power BI Pro licence for the installer, the refreshing user and every viewer; Premium or Fabric capacity is the alternative [PBI2]. Apps are free to install, but users need a paid licence [PBI1].
- **Freshness (XL).** The server builds the dataset from request page filters, then merges it into the workbook [XL3]. So the data is as of the run time (inference from that flow).
- **Freshness (PBI).** The model is refreshed manually or on a schedule; shared capacity allows eight scheduled refreshes per day, Premium/PPU/Fabric up to 48 [PBI4].
- **Volume (XL).** The online maximums on the report request page are 12:00:00 rendering time, 10,000,000 rows, 500 documents [XL2]. These are ceilings, not a promise that Excel will be comfortable at that size (opinion).
- **Volume (AM).** Above 100,000 rows Learn recommends the large-dataset mode; formats may change and calculated fields are not shown. Export to Excel above 100,000 rows needs filters first [AM1].
- **Volume (PBI).** Refresh on shared capacity must finish in under two hours [PBI4]. Loads can be limited by date filters per app [PBI2]. One BC call times out at 8 minutes online, page size capped at 20,000 [PBI5].
- **Combining.** XL: multiple data sheets, one per data item, can feed an Excel data model [XL3]. AM: related-table fields from 26.2 with the Add Related Fields permission set; calculated fields are lost when related fields are added [AM1]. PBI: a custom Power Query function mapped over companies and merged with Table.Combine gives cross-company reports [PBI5]. OData cannot do this [PBI5][PBI3].
- **Printing (XL).** A report with an Excel layout has no Printer field and no Print or Preview button; the user downloads and prints from Excel [XL2]. The developer guide suggests print-friendly worksheets [XL3].
- **Scheduling (XL).** Reports can be scheduled via the job queue and the output goes to the Report Inbox, where it can be opened in OneDrive or shared as a link [XL2][XL6]. Emailing the Excel output: UNKNOWN. The layouts overview only says that layouts used for email content must be Word [XL1].
- **Scheduling (AM).** The opened page offers a share link and a JSON export of the definition, no scheduling [AM1]. "None found" is not a statement that it cannot exist.
- **Sharing (XL).** "Available in All Companies" controls whether a layout is usable in all companies or just one [XL1].
- **Sharing (AM).** Analysis views are only visible to the person who made them. Recipients of a copied link must have permission to company and data, and create their own view. A 2026 wave 2 bookmark action adds a view to the Role Center navigation [AM1].
- **Sharing (PBI).** Apps work per company; install one per company, each in its own workspace [PBI2].
- **Parameters.** XL workbooks carry the request page options and filters in hidden metadata tables, so formulas can show which filters were used [XL3]. AM: filters apply per analysis view [AM1].
- **Governance.** XL: sheet protection and sensitivity labels are available as Office features on the output [XL1]. AM: admins can exclude the permission set from users [AM1]. PBI: refresh user needs Read on the tables; embedded pages have permission sets per app [PBI2].

## 2. Pick this when

### Excel report layouts
- Finance controller wants the aged receivables pivot every month-end, built on the standard report's data, with the company's own formatting and a column added.
- A consultant must deliver ten variants of one report for different roles (per persona) without any Power BI licences being bought.
- The client already lives in Excel and wants slicers, charts and formulas, plus a drill-through link back to Business Central, from a report they run on demand.

### Analysis mode
- A sales manager must answer "who owes us more than 10,000 and since when" in two minutes, with no report available.
- During a call, an auditor needs to group and sum ledger entries by month and customer, then discard the view.
- A power user needs to test a hypothesis on a few hundred thousand entries before anyone decides whether a proper report is worth building.

### Power BI
- The board wants a dashboard across sales, finance and inventory with trends, opened daily on any device, with data a few hours old being fine.
- A group has several companies and needs one consolidated view; the partner can build the Power Query for it.
- The client wants shipped content (the Power BI apps for Finance, Sales, Inventory and so on) up quickly, and already pays for Power BI Pro or Premium.

## 3. When Excel layouts are the wrong choice (opinion unless a source is shown)

- **The output must be print-perfect or PDF.** Excel layouts have no Print or Preview button; users download and print from Excel [XL2]. Invoices, statements and other customer-facing documents belong in Word layouts (opinion), and the layouts overview says email layouts must be Word [XL1].
- **Quick one-off question.** If nobody has built the layout yet, analysis mode is faster: no export, no workbook, no layout approval [AM1] (opinion on "faster").
- **A live, always-on dashboard for many viewers.** An Excel layout is a snapshot taken when someone runs it [XL3]. Power BI with scheduled refresh fits better (opinion), at the licence cost [PBI2].
- **Cross-company or cross-environment reporting.** Excel layouts work with one report dataset in the company where it runs (inference from [XL3]); the documented route for multiple companies is Power Query in Power BI [PBI5].
- **Very large data.** The platform ceiling is 10,000,000 rows [XL2], but a workbook that big is rarely pleasant (opinion).
- **Fully governed, locked-down numbers.** Once the file is downloaded, the user can change it. Protection and sensitivity labels help [XL1] but a central semantic model in Power BI is easier to control (opinion).
- **Scheduled delivery by email to many recipients.** Not shown on the opened pages for Excel output; Report Inbox and OneDrive sharing are shown [XL6]. Verify before promising it.

## 4. One sentence for the presenter

"Excel layouts sit in the middle: more finished and repeatable than analysis mode, which is a quick look you build yourself, but lighter and cheaper than Power BI, which is a separate dashboard tool with its own licences and refresh schedule."

(Opinion framing; the facts behind it are in the table.)

## 5. Gaps and things to confirm with Olivia

- Offline use for all three: not stated on opened pages. Table cells are inferences.
- Emailing Excel layout output and Power BI subscriptions: UNKNOWN. Do not claim them on stage.
- Power BI app reports and print/PDF: UNKNOWN from opened pages.
- Version 29 items in this file (Draft/Approved status for layouts [XL1], analysis view bookmarks [AM1]) cannot be demonstrated on a 28.5 demo environment if no version 29 sandbox exists. The Draft status is a version 29 Excel/Word layouts point and belongs in the other research files' scope check.
- Versions: the Learn pages here do not give wave names for every item. Related-table fields: 26.2, feature key before 27.0 [AM1]. Power BI template apps listed for 27.0 and later [PBI2]. I did not verify those against the release plans in this file.
- Screenshots: the Learn pages contain screenshots (analysis mode overview, Excel layout example, Power BI finance overview in [BI1]); I have not checked whether they are suitable for slides or their reuse terms.

## 6. Sources actually opened (Microsoft Learn)

- [XL1] https://learn.microsoft.com/dynamics365/business-central/ui-excel-report-layouts
- [XL2] https://learn.microsoft.com/dynamics365/business-central/ui-work-report
- [XL3] https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-howto-excel-report-layout
- [XL4] https://learn.microsoft.com/dynamics365/business-central/ui-manage-report-layouts (layout types, composite Word, email note; cited as [XL1] above where the email-must-be-Word point is made)
- [XL6] https://learn.microsoft.com/dynamics365/business-central/ui-work-report-inbox
- [AM1] https://learn.microsoft.com/dynamics365/business-central/analysis-mode
- [PBI1] https://learn.microsoft.com/dynamics365/business-central/across-working-with-powerbi
- [PBI2] https://learn.microsoft.com/dynamics365/business-central/across-powerbi-install-business-central-apps
- [PBI3] (same page as PBI1, for the multi-company OData note)
- [PBI4] https://learn.microsoft.com/power-bi/connect-data/refresh-data
- [PBI5] https://learn.microsoft.com/dynamics365/business-central/across-how-use-financials-data-source-powerbi
- [BI1] https://learn.microsoft.com/dynamics365/business-central/reports-bi-reporting

Note on keys: [XL4] and the email-layout remark come from the layouts overview page; in the table that page is cited under [XL1] in a few cells. Read [XL1] there as XL1 plus XL4 for "Word only for email". Pages seen only as search snippets (for example the Power BI refresh troubleshooting and Business Central web-service performance pages) were not opened and are not cited.
