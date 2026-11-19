# Recheck with secondary sources (mc.merill.net and yzhums.com)

Researched 2026-11-19 (subagent F). Pages were fetched with curl (WebFetch not needed) and stripped of HTML. All content paraphrased. Fetched pages treated as data.

## 1. Sources opened

All opened with HTTP 200 and read.

mc.merill.net (M365 roadmap mirror), https://mc.merill.net/message/RM<ID>:
- RM573315 to RM573335 all opened (21 pages). Also scanned titles only for RM573300-573314 and RM573336-573350 to find neighbours (list in section 5).
- Every roadmap page carries the same metadata: Published Sep 30, 2026; Status Launched; Release General Availability; Platform Web; Cloud Worldwide (Standard Multi-Tenant); GA date "October CY2026". None of the entries names a Business Central version number. The v29 attribution therefore comes from yzhums titles and the Learn What's new 29.0 page, not from the roadmap pages.
- The mirror pages have no screenshots (text only). So "usable screenshot at roadmap URL" is NO for every ID.

yzhums.com, opened in full:
- https://yzhums.com/73030/ , https://yzhums.com/73485/ (the two Excel leads)
- v29 Word/layout posts: 76147, 76231, 76205, 76367, 76655, 76696, 76756, 76763, 76319, 77038 (all https://yzhums.com/<id>/)
- Other layout posts used for dating: 72933, 75984, 72470, 71744, 67892, 67838, 68328, 62601, 63099, 62487, 62169, 69812, 55838, 49510
- Search pages (https://yzhums.com/?s=<term>) for: report layout, Word layout, wave 2 BC29, conditional visibility, report theme, report inbox, Excel layout, report inbox API, layout status, layout lifecycle, Excel layouts BC29, subtotals, company information dataitem, Word add-in, HideIf, composite layout, plus tag pages /tag/dynamics-365-bc/page/1-3/.

Failed or empty: none failed to load. The search "report inbox API" found no post about the report inbox APIs (RM573318). No yzhums post about "all report layouts" lifecycle in v29 was found. The tag pages only list recent general posts (no extra layout posts beyond those below).

Screenshot caveat: yzhums posts embed many screenshots as PNG/JPG/GIF under https://yzhums.com/wp-content/uploads/<year>/<month>/. I give the first body image URLs as examples. I did not download or view the images, so I cannot say what each shows beyond what the surrounding text says.

## 2. Roadmap table (one row per ID)

"Reporting" means the roadmap service area "Reporting and data analysis". All IDs below: Published Sep 30 2026, Launched, GA, GA date October CY2026, URL https://mc.merill.net/message/RM<ID>. Screenshot: none on any of them.

| ID | Title | What it says (own words) | Layout relevance | v29 corroboration |
|---|---|---|---|---|
| 573317 | Monitor usage of Open in Excel with telemetry | Open in Excel actions are logged to telemetry so data export is auditable. | Not a layout feature (Edit/Open in Excel on pages). | none |
| 573318 | Automate report outputs | New APIs on the report inbox let Power Automate or MCP act on report outputs. | Indirect: outputs of any layout type. | no yzhums post found |
| 573319 | Bookmark list views and analysis tabs | Bookmark analysis tabs and list views to the role center and/or profiles. | Not a layout feature. | none |
| 573320 | Control the lifecycle of all report layouts | Status can be set on all layout types, including layouts shipped with BC, per-tenant extension layouts and AppSource app layouts, to control which layouts end users can pick. | Word, Excel, RDLC (all types). | no v29 yzhums post; v28 post 72933 |
| 573321 | Reduce complexity of report datasets | Word layouts get a Company Information data item that is shared across all report datasets. Less work for report developers, consistent use of company information. | Word only as stated. | yzhums https://yzhums.com/76367/ (2026-09-29) |
| 573322 | Use system audit fields in analysis mode and in profiles | System audit fields in analysis tabs and in profile page customisation. | Not a layout feature. | none |
| 573323 | Run multiple financial reports and get a single PDF output | Report packs combine several financial reports, run now or schedule delivery to report inboxes or by email. | Financial reports (not Word/Excel layouts). | yzhums https://yzhums.com/75984/ (2026-09-10) |
| 573324 | Trace G/L account usage in finance reports | Financial report authors find uncategorised accounts, trace usage and calculations, preview definitions before publishing. | Not a layout feature. | none |
| 573325 | Financial report changes are now always logged | Changes to financial row, column and report definitions go to the change log. | Not a layout feature. | https://yzhums.com/76076/ (title seen in search only, not opened) |
| 573326 | Reuse header/footer layouts across document reports | With composable layouts, apply a header/footer to layouts for consistent PDF output. Defaults can be set globally, per company, per report or per layout. | Word. | yzhums https://yzhums.com/76231/ (2026-09-24) |
| 573327 | Brand document reports with report themes | With composable layouts, apply a report theme to layouts for consistent PDF output. Same four default levels as above. | Word. | yzhums https://yzhums.com/76147/ (2026-09-17) |
| 573328 | Design document reports with the updated Word add-in | New design components in the add-in: controls for addresses, field groups, amounts, signature lines, notes. | Word. | yzhums https://yzhums.com/76696/ (2026-10-15) |
| 573329 | Use conditional visibility in the updated Word add-in | New HideIf logic control: content inside is shown or hidden based on boolean fields in the dataset. | Word. | yzhums https://yzhums.com/76655/ (2026-10-14) |
| 573330 | Design document report themes with the updated Word add-in | New document sample controls to design themes. Samples look like common documents: invoice, pick list, outstanding orders. | Word. | yzhums https://yzhums.com/76756/ (2026-10-16) |
| 573331 | Design header/footer layouts for document reports with the updated Word add-in | New header and/or footer sample controls in the add-in; samples usable for internal or external reports. (Source text has typo "addes".) | Word. | yzhums https://yzhums.com/76756/ |

Neighbours that are not layout features (noted so nobody re-checks): 573313 (actions on reports and pages inherit tooltips, AL development), 573312 (run data queries with MCP server), 573315/573316/573314 (indexes), 573332 (table extension data model).

## 3. Answers to the key questions

**1a. "Automate report outputs" (573318).** The roadmap text is one sentence: new APIs on the report inbox, to extend automation with Power Automate or MCP to reports. So yes, it is the report inbox APIs. It does NOT mention Excel output, scheduling or emailing. It says nothing about layouts. Scheduling and emailing appear in other entries: RM573323 (report packs, scheduled delivery to report inboxes or by email, financial reports) and, from yzhums https://yzhums.com/72470/ and https://yzhums.com/71744/, scheduling a financial report to a distribution group with email plus report inbox was a 2026 wave 1 (BC28) item. Which APIs exist (names, endpoints, whether they return Excel files): UNKNOWN. No yzhums post found.

**1b. "Reduce complexity of report datasets" (573321).** Contents: a Company Information data item shared across all report datasets, for Word layouts. It reduces developer work and standardises company information. Yes, it is a shared company information data item. Affects Word layouts (stated). Excel: UNKNOWN, the roadmap says Word layouts only. yzhums https://yzhums.com/76367/ shows it in practice: even a custom report with no such data item defined shows a CompanyMetadata data item under BCReportInformation, and an empty layout of a standard report shows it too; the post tests it with a quick example. This builds on the v26 report/request metadata in Word layouts (https://yzhums.com/62169/, 2025-03-12). The post has screenshots (first body images: https://yzhums.com/wp-content/uploads/2026/09/Snipaste_2026-09-29_10-33-18.png, https://yzhums.com/wp-content/uploads/2026/09/image-271-1024x181.png).

**1c. What is new in v29 in "Design document reports with the updated Word add-in" (573328) versus v27 and v28?**
- v27 (2025 wave 2): the Add Data task pane (data picker with tree of data, labels, report metadata; tooltips). Source https://yzhums.com/67892/ (2025-10-03).
- v28 enhanced add-in (2026 wave 1): not re-opened here; see earlier file S9 in word-v29.md. UNKNOWN from these two sites.
- v29 per RM573328 and https://yzhums.com/76696/: ready-made design components inserted with one click. Addresses: Sender and Receiver (side by side), Receiver Only (billing and ship-to), Document Information (both addresses plus six document fields). Field groups: Column Grid (1 to 10 fields), Single Stacked (4 fields), Double Stacked (6 fields). Amounts: Full Calculation Table, Full Calculation Table (No Totals), Totals Row, Totals Row (With Details, e.g. VAT breakdown). Signature lines: One signature, Two signatures (layout only, no digital signing). Notes: up to 10 printing text lines (unlike internal BC notes).
- Also v29 and closely tied: Hide If False/Hide If Empty (573329), theme samples (573330), header/footer samples (573331). The yzhums add-in install screenshot lists two add-in versions in the Add-ins store: 3.0.0.0 and 2.0.4.0, "install the latest". That the v29 features need add-in 3.0.0.0: UNKNOWN (post only says install the latest).
- The author tested on report 1305 "Standard Sales - Order Conf." in the BC29 environment. The post has screenshots (https://yzhums.com/wp-content/uploads/2026/10/Snipaste_2026-10-14_14-50-28.jpg, https://yzhums.com/wp-content/uploads/2026/10/image-79-1024x573.png).

**1d. "Control the lifecycle of all report layouts" (573320) beyond v28.**
Evidence points to scope extension, not (only) the Draft default:
- RM573320 describes status for all layout types including layouts shipped with BC, per-tenant extensions and AppSource apps.
- yzhums v28 post https://yzhums.com/72933/ (2026-05-15, titled BC28.1) says: like Edit Info, the status of a layout provided by an extension cannot be changed; multiple selected layouts can be changed at once; statuses Draft, Pending approval, Approved, Retired; only Approved layouts selectable on request pages. It does not say what a new or copied layout starts as.
- Therefore: v28 = statuses for user-defined layouts only (extension layouts blocked); v29 = statuses for all layouts incl. shipped, PTE and AppSource layouts. This is a strong inference from two opened pages, but no page states "v29 adds this" in one sentence. Earlier file excel-v26-v29.md line ~111 says Learn docs describe extension status changes as stored overrides: consistent with this.
- Whether "replace resets to Draft" is v29-specific: the Learn doc notes quoted in earlier files tie it to v29, yzhums neither confirms nor contradicts. Olivia's 28.5 observation (a COPY starts as Draft/Concept) conflicts with the Excel doc wording "In version 29, a new or replaced user-defined layout has the Draft status" for new/copied layouts. So the doc version tag looks too late for "new/copy"; whether "replace" resets in 28.5: UNKNOWN. The https://yzhums.com/76763/ post (copy via Edit Info with Save Changes to Copy, 2026-10-22, BC version not stated) does not mention status in its text.
- Version disagreement for the status model itself: yzhums title says BC28.1 and PS 4 says the field was added in 28.0 but was not available there; earlier files say v28.0 table, GA 1 May 2026. Keep both: https://yzhums.com/72933/ and https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/control-lifecycle-report-layouts . For the talk: "v28 wave 1 (arrives in a 28.x minor)".

**1e. Contradictions to v29 attribution of conditional visibility, header/footer, themes?**
- Header/footer and themes (composable layouts, Subtype Body/HeaderFooter/Theme, Manage themes and header-footer layouts page): no contradiction. RM573326/573327/573330/573331 and yzhums 76147, 76205, 76231, 76756 all show v29 (BC29). The yzhums posts were first drafted in the preview window (Sep 2026) and then re-framed as GA (Oct 2026), which fits GA October.
- Conditional visibility: PARTIAL CONTRADICTION. yzhums https://yzhums.com/55838/ (2024-09-12, BC25 preview) quotes that from BC v24.4 a new Word add-in "lets you control conditional visibility of text, tables, or table rows/columns", and https://yzhums.com/67892/ (2025-10-03, BC27) repeats that the add-in provides control of conditional visibility. So hide-if-empty style visibility predates v29. What RM573329 and https://yzhums.com/76655/ present as new in v29 is the HideIf logic control driven by boolean dataset fields ("Hide If False", boolean fields of the report incl. report-extension fields). Whether the four Hide If Empty controls (Field if Zero, Table, Table Row, Table Column) are new or only re-presented in v29: UNKNOWN. The earlier claim "first shipped in v29" for all of conditional visibility is not safe; "boolean Hide If False is new in v29" is safe.

## 4. yzhums findings table

| Post | Date | BC version shown | What it shows | Screenshots (example image URLs) |
|---|---|---|---|---|
| https://yzhums.com/73030/ | 2026-05-25 | Title BC28 (wave 1); text also says "BC28.1" for analysis views not found | Customer loyalty Power BI reports; subtotals added to Excel layouts of five sales reports: Salesperson Commission, Customer/Item Sales, Inventory Order Details, Inventory Customer Sales, Inventory - Sales Back Orders | yes, https://yzhums.com/wp-content/uploads/2026/05/image-150-1024x385.png |
| https://yzhums.com/73485/ | 2026-06-01 | Title BC28.1 (wave 1) | Subtotals in Excel layouts of three deferral reports (Deferral Summary G/L, Purchasing, Sales); repeats the five sales reports with subtotals; speed-up of five finance Excel reports: Trial Balance, Consolidated Trial Balance, Trial Balance/Budget, Trial Balance by Period, Trial Balance Previous Year; analysis views on G/L Registers and Fixed Assets Ledgers (not layouts) | yes, https://yzhums.com/wp-content/uploads/2026/05/image-379.png, .../image-380-1024x332.png |
| https://yzhums.com/68328/ | 2025-10-10 | BC27 (GA) | Deferral reports modernised: RDL replaced by Word and Excel layouts, plus three list pages | yes (23 images) |
| https://yzhums.com/76696/ | 2026-10-15 | BC29 GA | Word add-in design components (see 1c) | yes, https://yzhums.com/wp-content/uploads/2026/10/Snipaste_2026-10-14_14-50-28.jpg |
| https://yzhums.com/76655/ | 2026-10-14 | BC29 GA | Hide If Empty (Field if Zero, Table, Table Row, Table Column) and Hide If False with boolean field dropdown; IIF still not supported in Word layouts | yes, https://yzhums.com/wp-content/uploads/2026/10/Snipaste_2026-10-13_16-33-54.jpg |
| https://yzhums.com/76756/ | 2026-10-16 | BC29 GA | Theme sample reports (Invoice, Pick list, Outstanding orders, opened as sample documents), five header layouts (Default, Modern, Modern With Logo, Minimalist, Minimalist Centered) and five footer layouts with the same names | yes, https://yzhums.com/wp-content/uploads/2026/10/Snipaste_2026-10-16_10-32-52.jpg |
| https://yzhums.com/76147/ | 2026-09-17 | BC29 preview text, wave 2 | Themes: build a theme in Word, save as .dotx (not .thmx), add on Manage themes and header-footer layouts, approve it, assign via Set report theme and header-footer; works only on Word layouts with Subtype Body; no standard Body layouts exist yet (export and re-import a standard layout); defaults at global, company, report, layout level; unapproved parts cannot be assigned | yes (36 images, one GIF), https://yzhums.com/wp-content/uploads/2026/09/36a4d569-8a56-49e0-8630-68a787c0a997.gif |
| https://yzhums.com/76231/ | 2026-09-24 | BC29 preview text | Same flow for header/footer parts; "New header/footer" action; same restrictions | yes, https://yzhums.com/wp-content/uploads/2026/09/image-244-1024x183.png |
| https://yzhums.com/76205/ | 2026-09-18 | BC29 preview text | New Subtype property on Word layouts: Default, HeaderFooter, Theme, Body (Theme must be .dotx); Body and Default shown on Report Layouts; HeaderFooter and Theme on the new Manage themes and header-footer layouts page | yes, https://yzhums.com/wp-content/uploads/2026/09/image-221-1024x635.png |
| https://yzhums.com/76367/ | 2026-09-29 | BC29 preview text | Company Information dataitem (CompanyMetadata under BCReportInformation) | yes (see 1b) |
| https://yzhums.com/76763/ | 2026-10-22 | not stated (likely a BC29 environment, UNKNOWN) | How to copy a layout: Report Layouts, Edit Info, switch on Save Changes to Copy, give a new name | yes, https://yzhums.com/wp-content/uploads/2026/10/image-79-1024x573.png |
| https://yzhums.com/76319/ | 2026-09-25 | BC29 preview text | AL only: layout path properties accept both / and \ separators; AL0363 no longer reported | yes (4 images) |
| https://yzhums.com/77038/ | 2026-10-30 | BC29 (and "up to 28.5") | Custom Report Layouts page removed in BC29; migrate to Report Layouts before upgrading | yes (8 images) |
| https://yzhums.com/72933/ | 2026-05-15 | Title BC28.1; says field added in 28.0 but not available | Layout Status (see 1d) | yes, https://yzhums.com/wp-content/uploads/2026/05/image-95-1024x513.png |
| https://yzhums.com/75984/ | 2026-09-10 | BC29 | Financial report packages (Packages action, tables 8371/8372), single PDF, schedulable. Financial reports, not layout types | yes (24 images) |
| https://yzhums.com/72470/ , https://yzhums.com/71744/ | 2026-04-24 / 2026-04-07 | BC28 wave 1 | Scheduling financial reports to a distribution group (email plus report inbox); not layout types | yes |
| https://yzhums.com/67892/ | 2025-10-03 | BC27 | Add Data task pane; note: not available in Word Online; data visible only after Update and Export Layout | yes, https://yzhums.com/wp-content/uploads/2025/10/image-42-1024x231.png |
| https://yzhums.com/67838/ | 2025-09-25 | BC27 | Excel layout: new fields in the hidden Aggregated Metadata sheet (object caption, local date, UTC offset); not yet in Word layouts at that time | yes (3 images) |
| https://yzhums.com/62601/ , https://yzhums.com/63099/ , https://yzhums.com/62487/ | 2025-03-21, 2025-04-04, 2025-03-19 | BC26 | ExcelLayoutMultipleDataSheets and ObsoleteState properties; mark user layout obsolete; Validate layout and Show layout info (cannot check RDLC) | yes |

Excel leads confirmed or corrected:
- Subtotals in sales Excel reports: CONFIRMED, wave 1 / BC28 (title) on https://yzhums.com/73030/ . Five reports named above. The post text mentions "BC28.1" only for something else (missing analysis views).
- Deferral subtotals: wave 1, titled BC28.1 on https://yzhums.com/73485/ . CORRECTION to the lead "v27 / 28.1": the v27 item is the introduction of Word and Excel layouts for the deferral reports (https://yzhums.com/68328/); the subtotals in those Excel layouts are the later wave 1 item.
- Trial balance: the wave 1 (BC28.1 title) item is speed (five finance Excel reports run faster), not new layout features. The v27 deferral and v28 trial-balance Excel layouts are not the same thing.
- Excel in v29: none of the opened yzhums or roadmap pages shows a first-shipped-in-v29 Excel layout feature, other than the lifecycle extension (573320) which applies to all layout types and the AL path change (76319).

## 5. Possibly missing (not in earlier files, or only unconfirmed there)

Word, v29:
1. Design component catalogue (addresses, field groups, amounts, signature lines, notes) with the exact variant names: see 1c. Earlier files named only the feature title.
2. Header layouts (five) and footer layouts (five) in the add-in, names above; theme sample documents (Invoice, Pick list, Outstanding orders). Earlier file listed these as "unconfirmed seed items"; RM573330/573331 and https://yzhums.com/76756/ now confirm them.
3. Shared company information data item: confirmed (RM573321, https://yzhums.com/76367/).
4. Hide If False with boolean fields: confirmed (earlier said UNKNOWN).
5. Subtype property (Default, HeaderFooter, Theme, Body) and the Manage themes and header-footer layouts page, approval of parts, 4-level defaults: partly in earlier files; yzhums adds the practical limits (only Body layouts; no standard Body layout shipped; .dotx not .thmx; unapproved parts cannot be assigned).
6. Add-in store versions 3.0.0.0 and 2.0.4.0 (https://yzhums.com/76655/). Not tied to features anywhere.
7. Custom Report Layouts page removed in BC29 (https://yzhums.com/77038/): relevant as upgrade warning, not a "new layout feature".
8. "Copy a layout" via Edit Info with Save Changes to Copy (https://yzhums.com/76763/): works in earlier versions too (Learn-documented), so a demo tip, not a v29 feature.
9. AL path separators (https://yzhums.com/76319/): developer only.

Excel (v26-v29): nothing new beyond earlier files; adds yzhums confirmation for v26 properties, v27 Aggregated Metadata fields and deferral modernisation, v28 subtotals in 5 sales and 3 deferral Excel layouts, and wave 1 speed-up of 5 finance Excel reports (check earlier file lists them: the trial balance speed item is a performance note, not a layout capability).

Not layout features but adjacent and v29 (mention only if asked): report packs (573323), report inbox APIs (573318), financial report change log (573325), G/L account tracing (573324).

## 6. Corrections to earlier files

| Claim | Earlier statement | New evidence | URL |
|---|---|---|---|
| Hide If False exists | word-v29.md F2: "hide if false" control UNKNOWN, not found; verification W-m confirmed it as not documented | Documented as a v29 HideIf control driven by boolean fields | https://mc.merill.net/message/RM573329 ; https://yzhums.com/76655/ |
| Conditional visibility first shipped v29 | word-v29.md F2: "No earlier-wave entry found" | Add-in already offered conditional visibility of text, tables, rows, columns from v24.4 preview and BC25/BC27 per yzhums; v29 new part is boolean Hide If False (and possibly the packaging of Hide If Empty controls) | https://yzhums.com/55838/ ; https://yzhums.com/67892/ |
| Header/footer, theme sample controls and company info data item "not confirmed" | word-v29.md "Seed items not confirmed" | Confirmed as separate roadmap entries RM573330, RM573331, RM573321 | https://mc.merill.net/message/RM573330 ; https://mc.merill.net/message/RM573331 ; https://mc.merill.net/message/RM573321 |
| Lifecycle v29 vs v28 difference UNKNOWN | excel-v26-v29.md C8, verification X-ai/D-n | Roadmap says statuses on all layouts incl. shipped, PTE, AppSource; v28 post says extension layouts cannot have status changed | https://mc.merill.net/message/RM573320 ; https://yzhums.com/72933/ |
| Draft default is v29 | verification E-p, D-m (28.5 behaviour unverified) | Olivia reports copy is Draft in 28.5, so the Learn "In version 29" tag is not reliable for new/copied layouts. Replace behaviour in 28.5: UNKNOWN. No yzhums post states initial status. | https://yzhums.com/72933/ ; https://yzhums.com/76763/ |
| Lifecycle version | v28.0 (earlier files) | yzhums titles it BC28.1 and says the field was not present in 28.0; keep both | https://yzhums.com/72933/ |
| Deferral subtotals and trial balance (lead "v27 / 28.1") | Lead in task | v27 = Word and Excel layouts introduced for deferral; subtotals in deferral Excel layouts = wave 1 (BC28.1 title); trial balance = speed-up only | https://yzhums.com/68328/ ; https://yzhums.com/73485/ |
| Sales subtotals | Lead: v28 | Confirmed, wave 1 (BC28 title), 5 named reports | https://yzhums.com/73030/ |
| Report inbox API content (573318) | UNKNOWN / seed | Sentence only: new report inbox APIs for Power Automate or MCP. No Excel, scheduling, email text. | https://mc.merill.net/message/RM573318 |
| Roadmap detail unavailable | word-v29.md "Roadmap page returned no detail" | The mirror gives short summaries; no version numbers and no screenshots | https://mc.merill.net/message/RM573328 |
