# Verification 2 of recheck-secondary.md

Verifier: independent (did not write the checked file). Date: 2026-11-19. Scope: Word = features first shipped in v29; Excel = v26-v29; presenter env 28.5 (copy of a layout already starts as Draft/"Concept"). Context file verification.md not re-verified.

Method: all cited mc.merill.net (RM573317-573331, plus neighbours) and yzhums.com pages fetched with curl (HTTP 200), stripped with python3 -I, text compared with the claims. The 13 screenshot URLs cited in the file were fetched (all HTTP 200) and 20+ images were opened and looked at. Learn pages read via the Microsoft Learn fetch tool. Extra primary evidence I used that the file did not cite: Learn "Update 29.0" what's-new page, Learn 2024 wave 2 release plan page, Learn Word add-in page, Learn "Get started creating report layouts" and Excel layouts pages.

Verdict key: CONFIRMED, CORRECTED, UNVERIFIED, WRONG. Page-level verdicts refer to the claim in recheck-secondary.md (section in brackets).

## 1. Claims table

Base URL for roadmap rows: https://mc.merill.net/message/RM<ID>. v29 attribution for every RM row below is independently CONFIRMED by https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-29-0 (lists each ID under update 29.0, all "General availability", under Reporting and data analysis, except 573317 under Governance and administration). The file said v29 came from "yzhums titles and the Learn What's new 29.0 page", but never cited the Learn page per ID. Now it can.

| # | Claim (section) | Verdict | Note | URL |
|---|---|---|---|---|
| S1 | RM573315-573335 mirror pages open with HTTP 200 [1] | CONFIRMED | I opened 573317-573331 plus 573312/13/16/32, all 200. 573315 and 573333-573335 not re-opened, but they appear in the Learn 29.0 table. | https://mc.merill.net/message/RM573328 |
| S2 | Every roadmap page: Published Sep 30 2026, Launched, GA, Web, Worldwide Standard Multi-Tenant, GA date "October CY2026"; no BC version number [1] | CONFIRMED | Checked on all 15 pages. grep for "29.0 / version 29 / BC29" in the mirror text finds nothing. | https://mc.merill.net/message/RM573329 |
| S3 | Mirror pages have no screenshots [1] | CONFIRMED | No image tags in page body (checked 573328, 573329). | https://mc.merill.net/message/RM573328 |
| R17 | 573317 Open in Excel telemetry; not a layout feature [2] | CONFIRMED | Service area is Governance and administration (file's "Reporting" shorthand does not fit this one row; irrelevant to layouts). | https://mc.merill.net/message/RM573317 |
| R18 | 573318 Automate report outputs: new report inbox APIs, Power Automate or MCP [2] | CONFIRMED | Summary is exactly one sentence. No Excel, scheduling or layout mention. v29 per Learn 29.0 table. | https://mc.merill.net/message/RM573318 |
| R19 | 573319 Bookmark list views and analysis tabs [2] | CONFIRMED | | https://mc.merill.net/message/RM573319 |
| R20 | 573320 Control lifecycle of all report layouts: status on all layout types incl. shipped, per-tenant extension, AppSource [2] | CONFIRMED | Text matches. Whether it is an extension of the v28 feature is not stated (see answer 6). | https://mc.merill.net/message/RM573320 |
| R21 | 573321 Word layouts get a Company Information dataitem shared across all report datasets [2] | CONFIRMED | Word only as stated. | https://mc.merill.net/message/RM573321 |
| R22 | 573322 System audit fields in analysis mode and profiles [2] | CONFIRMED | | https://mc.merill.net/message/RM573322 |
| R23 | 573323 Report packs, single PDF, run now or schedule to inboxes or email; financial reports [2] | CONFIRMED | yzhums 75984 (2026-09-10, BC29 preview) shows Packages action; the file's table numbers 8371/8372 appear in the post. | https://yzhums.com/75984/ |
| R24 | 573324 Trace G/L account usage [2] | CONFIRMED | | https://mc.merill.net/message/RM573324 |
| R25 | 573325 Financial report changes always logged; yzhums 76076 seen in search only [2] | CONFIRMED | I opened 76076: 2026-09-15, BC29 preview, same text. | https://yzhums.com/76076/ |
| R26 | 573326 composable layouts, header/footer, 4 default levels [2] | CONFIRMED | Roadmap says global, per company, per report, per layout. yzhums 76231 dated 2026-09-24. | https://mc.merill.net/message/RM573326 |
| R27 | 573327 report themes, same 4 levels [2] | CONFIRMED | yzhums 76147 dated 2026-09-17. | https://mc.merill.net/message/RM573327 |
| R28 | 573328 design components: addresses, field groups, amounts, signature lines, notes [2] | CONFIRMED | Roadmap lists these five as examples ("such as"). yzhums 76696 dated 2026-10-15. | https://mc.merill.net/message/RM573328 |
| R29 | 573329 new HideIf logic control, boolean fields in the dataset [2] | CONFIRMED | Only the HideIf control is described as new; the roadmap does NOT mention Hide If Empty (see answer 1). | https://mc.merill.net/message/RM573329 |
| R30 | 573330 document sample controls for themes: invoice, pick list, outstanding orders [2] | CONFIRMED | | https://mc.merill.net/message/RM573330 |
| R31 | 573331 header/footer sample controls; typo "addes" [2] | CONFIRMED | Typo present on roadmap page and in yzhums 76756. | https://mc.merill.net/message/RM573331 |
| N1 | Neighbours 573312/13/14/15/16/32 are not layout features [2] | CONFIRMED | Titles match the Learn 29.0 table. | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-29-0 |
| A1 | 573318 does not mention Excel, scheduling or email; API names unknown [3 1a] | CONFIRMED | Absence confirmed. "Unknown which APIs" stays open (no Learn/yzhums page found; my yzhums searches "report inbox", "Automate report outputs" returned nothing relevant). | https://mc.merill.net/message/RM573318 |
| A2 | Scheduling to distribution group with email plus inbox was a BC28 wave 1 item per 72470 and 71744 [3 1a] | CONFIRMED | Strictly via 71744 (BC28 preview, 2026-04-07: "Schedule reports for a distribution group. Recipients can get the report output in an email and in their report inbox"). 72470 (2026-04-24) is a how-to post, not itself labelled wave 1. | https://yzhums.com/71744/ |
| B1 | 573321 shown in 76367: CompanyMetadata under BCReportInformation, also in custom and standard reports [3 1b] | CONFIRMED | Screenshot Snipaste_2026-09-29 shows XML pane with CompanyMetadata listing CompanyName ... CompanyGiroNo. Post dated 2026-09-29, BC29 preview. | https://yzhums.com/76367/ |
| B2 | Builds on v26 report/request metadata in Word layouts (62169, 2025-03-12) [3 1b] | CONFIRMED | 76367 itself says so. Learn: "APPLIES TO: Business Central 2025 release wave 1 (v26)". | https://yzhums.com/62169/ |
| B3 | 573321 Excel unknown [3 1b] | UNVERIFIED | Nothing says Excel gets it. Treat as Word only. | https://mc.merill.net/message/RM573321 |
| C1 | v27: Add Data task pane (67892, 2025-10-03) [3 1c] | CONFIRMED | Post is BC27 GA; also "not available in Word Online", data visible only after Update and Export Layout. Learn confirms Add Data task pane (Data, Labels, Report Information). | https://yzhums.com/67892/ |
| C2 | v28 enhanced add-in: unknown from these sites [3 1c] | UNVERIFIED | Honest gap, nothing to check. | https://yzhums.com/ |
| C3 | v29 design component catalogue with variants (Sender and Receiver, Receiver Only, Document Information, Column Grid 1-10, Single Stacked 4, Double Stacked 6, 4 amount tables, One/Two signatures, Notes up to 10) [3 1c] | CONFIRMED | Matches 76696 word for word. Signature lines are layout only (no digital signing) also confirmed. The ribbon screenshot shows Address Fields, Grouped Fields, Calculation Layouts, Signature Lines, Note Lines. | https://yzhums.com/76696/ |
| C4 | "Also v29: Hide If False/Hide If Empty (573329)" [3 1c] | CORRECTED | 573329 covers only the HideIf (boolean) control. Hide If Empty (4 controls) shipped in the 2024 wave 2 add-in. | https://learn.microsoft.com/en-us/dynamics365/release-plan/2024wave2/smb/dynamics365-business-central/use-improved-features-report-documents |
| C5 | Add-in store lists 3.0.0.0 and 2.0.4.0, "install the latest" [3 1c] | CONFIRMED | Post text lists both with screenshots. | https://yzhums.com/76655/ |
| C6 | v29 features need add-in 3.0.0.0 [3 1c] | UNVERIFIED | Not stated anywhere. The ribbon screenshots show add-in path bc-report-layout-word-addin-0.1.173, a different numbering, so the store version cannot be mapped to features. | https://yzhums.com/76696/ |
| C7 | Tested on report 1305 Standard Sales Order Conf. [3 1c] | CONFIRMED | 76696 text; 76655 screenshot file name StandardSalesOrderConf. | https://yzhums.com/76696/ |
| C8 | Screenshot Snipaste_2026-10-14_14-50-28.jpg and image-79-1024x573.png as examples for 76696 [3 1c] | CORRECTED | First exists and shows the new ribbon (Address Fields, Grouped Fields, Calculation Layouts, Signature/Note Lines) and the Insert Document Information dialog: good. image-79 is a generic Report Layouts list screenshot reused in 76655, 76696, 76756 and 76763; it shows no feature. | https://yzhums.com/wp-content/uploads/2026/10/image-79-1024x573.png |
| D1 | 72933 (2026-05-15, BC28.1 in title): extension layout status cannot be changed; multi-select; 4 statuses; only Approved selectable; says nothing on initial status [3 1d] | CONFIRMED | All present. Also post says "With this wave (BC28)". | https://yzhums.com/72933/ |
| D2 | Inference: v28 = user-defined only, v29 = all incl. shipped/PTE/AppSource [3 1d] | UNVERIFIED | Inference only, as the file admits. No page says "v29 extends". See answer 6. | https://mc.merill.net/message/RM573320 |
| D3 | Learn: "In version 29, a new or replaced user-defined layout has Draft status" (Excel doc) [3 1d] | CONFIRMED | Exact sentence on the Excel layouts page. The Word add-in page says "In version 29, replacing a layout sets its Layout Status to Draft" (replace only). The Get Started page says untagged "New user-defined layouts start with the Draft status". | https://learn.microsoft.com/en-us/dynamics365/business-central/ui-excel-report-layouts |
| D4 | Olivia's 28.5 copy=Draft conflicts with the "In version 29" tag for new/copied layouts; replace behaviour in 28.5 unknown [3 1d] | CONFIRMED | Reasoning is sound: the version tag in Learn is not reliable for "new"/copy, and nothing documents 28.x replace. Treat copy=Draft as observed 28.5 behaviour, and replace=Draft as documented only for v29. | https://learn.microsoft.com/en-us/dynamics365/business-central/ui-get-started-layouts |
| D5 | 76763 (copy layout via Edit Info, Save Changes to Copy, 2026-10-22, version not stated) does not mention status [3 1d] | CONFIRMED | | https://yzhums.com/76763/ |
| D6 | Status feature: 28.0 vs 28.1 disagreement [3 1d, 6] | CONFIRMED | 72933 title says BC28.1 and PS4 "field was added in version 28.0, but it is not available". New: Learn lists "Control the lifecycle of report layouts" in BOTH the 28.0 and the 28.1 what's-new tables; release plan GA date May 1 2026. | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-28-1 |
| E1 | Header/footer, themes, Subtype: no contradiction, all BC29 (76147, 76205, 76231, 76756) [3 1e] | CONFIRMED | Subtype Default/HeaderFooter/Theme/Body, .dotx for Theme, Body-only, no standard Body layouts, unapproved parts cannot be assigned: all in 76147/76205. Learn 29.0 lists "Feature: New Document Report Experience" as new optional feature, disabled by default (not in file, relevant for demo). | https://yzhums.com/76205/ |
| E2 | "yzhums posts were first drafted in preview (Sep 2026) then re-framed as GA (Oct 2026)" [3 1e] | UNVERIFIED | 76147/76231/76205/76367 are dated Sep and say "public preview"; 76655/76696/76756 are dated Oct and say GA. No page says any post was re-framed. Speculation. | https://yzhums.com/76147/ |
| E3 | Conditional visibility "partial contradiction": 55838 (2024-09-12, BC25 preview) quotes v24.4 and 67892 repeats [3 1e] | CONFIRMED | 55838 contains "In BC v24.4: A new Word add-in lets you control conditional visibility of text, tables, or table rows/columns". 67892 line: "add data controls and control conditional visibility". | https://yzhums.com/55838/ |
| E4 | "Whether the four Hide If Empty controls are new or re-presented in v29: UNKNOWN" [3 1e] | CORRECTED | Not unknown. They shipped in 2024 wave 2 (screenshot and doc text, see answer 1). | https://yzhums.com/55838/ |
| F1 | 73030 (2026-05-25, BC28): subtotals in Excel layouts of five sales reports [4, 4 leads] | CONFIRMED | Five reports named exactly as claimed. "BC28.1" in text refers to missing analysis views. | https://yzhums.com/73030/ |
| F2 | 73030 example screenshot image-150-1024x385.png [4] | CORRECTED | URL 200, but the image is a Tell-me search for "Customer Retention Overview" (Power BI), not the Excel subtotals. | https://yzhums.com/wp-content/uploads/2026/05/image-150-1024x385.png |
| F3 | 73485 (2026-06-01, BC28.1): subtotals in three deferral Excel layouts, repeats the five sales reports, speed-up of five Trial Balance Excel reports, analysis views on G/L Registers and Fixed Assets Ledgers [4] | CONFIRMED | Matches. Trial balance item is speed only. | https://yzhums.com/73485/ |
| F4 | 73485 screenshots image-379.png, image-380-1024x332.png [4] | CORRECTED | image-379.png (hero) shows Deferral Summary Purchasing Excel with subtotal rows: good. image-380 is only a search box for "Deferral Summary - G/L". | https://yzhums.com/wp-content/uploads/2026/05/image-380-1024x332.png |
| F5 | Correction to lead "v27/28.1": v27 introduced Word/Excel for deferral reports (68328, 2025-10-10), subtotals later in wave 1 [4, 4 leads] | CONFIRMED | 68328 title and text match; 73485 says the same. | https://yzhums.com/68328/ |
| F6 | 68328 "yes (23 images)" [4] | UNVERIFIED | Did not count reliably (page also carries related-post thumbnails). Immaterial. | https://yzhums.com/68328/ |
| F7 | 76655 (2026-10-14, BC29 GA): Hide If Empty (4 controls) and Hide If False with boolean dropdown; IIF still not supported in Word layouts [4] | CONFIRMED | Text matches. Note the post also says Microsoft "added a similar feature" (to RDLC IIF) "in this major release", which is the post's framing and not evidence that Hide If Empty is new. Screenshot Snipaste_2026-10-13_16-33-54.jpg shows the Hide If False dialog (What to hide: Table/Row/Column/Field, Boolean field IsTest) and the Visibility ribbon group. | https://yzhums.com/76655/ |
| F8 | 76756 (2026-10-16): samples Invoice, Pick list, Outstanding orders; five header and five footer layouts with names Default, Modern, Modern With Logo, Minimalist, Minimalist Centered [4] | CONFIRMED | Exact. Ribbon screenshot shows Samples (Reports) and Headers & Footers groups. | https://yzhums.com/76756/ |
| F9 | 76147 (2026-09-17): themes saved as .dotx not .thmx, Manage themes and header-footer layouts, Set report theme and header-footer, Body only, no standard Body layouts, 4 levels, unapproved cannot be assigned [4] | CONFIRMED | All present. "36 images" not counted (UNVERIFIED, immaterial). | https://yzhums.com/76147/ |
| F10 | 76231 (2026-09-24): same flow for header/footer, "New header/footer" action [4] | CONFIRMED | image-244 is a roadmap-text snippet, not the flow (see answer 7). | https://yzhums.com/76231/ |
| F11 | 76205 (2026-09-18): Subtype property; Body and Default on Report Layouts, HeaderFooter and Theme on the Manage page [4] | CONFIRMED | Text confirms Subtype values and .dotx rule. The "which page shows which subtype" part is in the lower body, not rechecked word for word. | https://yzhums.com/76205/ |
| F12 | 76319 AL-only path separators; 77038 Custom Report Layouts page removed in BC29, "up to 28.5" [4, 5] | CONFIRMED | Both match. | https://yzhums.com/77038/ |
| F13 | 76763 "works in earlier versions too (Learn-documented), so a demo tip not a v29 feature" [5.8] | CONFIRMED | Post says copying is documented on Learn and BC version not stated. Not a v29 feature claim anywhere. | https://yzhums.com/76763/ |
| F14 | 67838 (2025-09-25, BC27): Excel Aggregated Metadata new fields; 62601/63099/62487 (BC26): ExcelLayoutMultipleDataSheets, ObsoleteState, obsolete marking, Validate layout [4] | CONFIRMED | Titles, dates (62601 2025-03-21 published, 63099 2025-04-04, 62487 2025-03-19) match. "Not yet in Word layouts at that time" for 67838 not rechecked. | https://yzhums.com/67838/ |
| G1 | Excel in v29: no first-shipped Excel layout feature except lifecycle (573320) and AL path change (76319) [4] | CONFIRMED | The Learn 29.0 table has no Excel layout feature either. The "Draft for new/replaced" tag on the Excel page is a lifecycle side effect. | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-29-0 |
| H1 | Corrections table row: "Header/footer, theme sample controls and company info data item 'not confirmed' are now confirmed (RM573330/31/21)" [6] | CONFIRMED | | https://mc.merill.net/message/RM573330 |
| H2 | Corrections table row: "Conditional visibility first shipped v29" is not safe [6] | CONFIRMED | Correct direction, and stronger than the file says: only Hide If False is new. | https://learn.microsoft.com/en-us/dynamics365/release-plan/2024wave2/smb/dynamics365-business-central/use-improved-features-report-documents |
| H3 | Corrections table row: "Hide If False exists" [6] | CONFIRMED | | https://yzhums.com/76655/ |

## 2. Answers to the priority questions

**1. Conditional visibility: new in 29?**
No, not as a whole. Evidence that "Hide If Empty" style controls existed before v29:
- Official Learn release plan 2024 wave 2 (GA Oct 1 2024, so v25; yzhums quotes it as v24.4): "A new Word add-in that lets you control the conditional visibility of text, tables, or table rows and columns." https://learn.microsoft.com/en-us/dynamics365/release-plan/2024wave2/smb/dynamics365-business-central/use-improved-features-report-documents
- yzhums 55838 (published 2024-09-12, BC25 preview), screenshot https://yzhums.com/wp-content/uploads/2024/09/image-224-1024x576.png (I looked at it): add-in "Business Central (Preview)" ribbon with a **Hide If Empty** dropdown holding exactly **Hide Empty Table, Hide Empty Table Row, Hide Empty Table Column, Hide Field If Zero**, next to Insert Layout Comment. The post also shows (image-227) the documentation text for the same four controls (Hide Field if Zero, Hide Empty Table, Hide Empty Table Row, Hide Empty Table Column). https://yzhums.com/55838/
- 67892 (BC27 GA) repeats that the add-in provides conditional visibility. Current Learn add-in page documents the four controls with no version tag.
- What is first shipped in v29: the **Hide If False** control (roadmap calls it "the new HideIf logic control"), driven by a boolean field of the report dataset (including boolean fields added by report extensions), with What-to-hide options Table / Row / Column / Field. Sources: RM573329 and https://yzhums.com/76655/ (screenshot Snipaste_2026-10-13_16-33-54.jpg).
- Decision for the presentation: do NOT say "conditional visibility is new in 29". Safe wording: "Hide If False (boolean fields) is new in 29; Hide If Empty has been in the add-in since 2024 wave 2." The "IIF still unsupported in Word layouts" remark in 76655 is correct per the post.

**2. RM573328 design components: v29 and new?**
Yes. RM573328 (Launched, GA, Oct 2026), listed in Learn 29.0 table; yzhums 76696 (2026-10-15, BC29 GA) shows them: Addresses (Sender and Receiver, Receiver Only, Document Information), Field groups (Column Grid 1-10, Single Stacked, Double Stacked), Amounts (4 variants), Signature lines (One, Two; layout only), Notes (up to 10 printing lines). No earlier mention found: the BC25-era ribbon (image-224) had only Insert Layout Comment and Hide If Empty; the v29 ribbon adds Address Fields, Grouped Fields, Calculation Layouts, Signature Lines, Note Lines, Reports, Header/Footer Layouts. Caveat: the Learn Word add-in page has not been updated for these components (it documents only Add Data, Insert table, layout comment, Hide if empty), so for the demo cite the roadmap and the Learn 29.0 table.

**3. RM573330/573331 theme and header/footer samples: v29?**
Yes. Both in the Learn 29.0 table (GA). yzhums 76756 (2026-10-16, BC29 GA): three sample reports (Invoice with Contoso Coffee data, Pick list, Outstanding orders) opened in a new window to design a theme, plus five header and five footer layouts (Default, Modern, Modern With Logo, Minimalist, Minimalist Centered). They are "new" in the sense that composable layouts, Subtype and the Manage themes and header-footer layouts page are all v29 (RM573326/327).

**4. RM573321 Company Information data item: v29, Word only?**
v29: yes (Learn 29.0 table; yzhums 76367 dated 2026-09-29 in BC29 preview, shows CompanyMetadata under BCReportInformation next to ReportMetadata and ReportRequest). Word only: the roadmap says "Word layouts now include..." and nothing on any page mentions Excel, so Word only is the safe statement; whether Excel gets an equivalent is UNVERIFIED (not stated).

**5. RM573318 Automate report outputs?**
One roadmap sentence: "Use new APIs on the report inbox to extend automation with Power Automate or MCP to reports." Launched, GA, Oct 2026, in the Learn 29.0 table (v29 confirmed). No API names, no Excel/scheduling/email text, no layout relevance, no yzhums or Learn detail found. Present it only as "new report inbox APIs for Power Automate and MCP", not as a layout feature.

**6. RM573320 lifecycle**
- "v29 extends statuses to extension/AppSource layouts" is not stated anywhere. It is an inference from: RM573320 title and text ("all types of layouts incl. shipped, per-tenant extensions, AppSource apps") plus 72933 PS1 (v28: layout status of an extension layout cannot be changed). The title word "all" supports the inference but no page says "v29 adds this" or compares with v28. Additional unversioned Learn text (Get started page): changing the status of an extension-provided layout is saved as an override. So the capability is documented but without a version tag. Present as "per roadmap, v29 lets statuses apply to all layouts including extension layouts", not as a quoted fact about the delta.
- Version of the v28 feature: not settled. Learn lists it in both the 28.0 and 28.1 what's-new tables; release plan GA May 1 2026; yzhums 72933 titles it BC28.1 and says the field was added in 28.0 but not yet visible. Say "28.x (wave 1)".
- Draft default: Learn tags "new or replaced" (Excel page) and "replacing" (Word add-in page) as "In version 29", but the Get Started page states unversioned that new user-defined layouts start as Draft, and the presenter observed copy=Draft in 28.5. Do not present Draft-on-copy as new in 29. Draft-on-replace is documented only for v29 and unverified for 28.5.

**7. yzhums screenshot URLs**
All 13 URLs cited in the file return HTTP 200 (png, jpg, gif) and each appears in the cited post. What they show, judged by looking at them:
- 76655 Snipaste_2026-10-13_16-33-54.jpg: Hide If False dialog + Visibility group. Shows the feature.
- 76696 Snipaste_2026-10-14_14-50-28.jpg: new ribbon text group + Insert Document Information dialog. Shows the feature.
- 76756 Snipaste_2026-10-16_10-32-52.jpg: ribbon with Reports (Samples) and Header/Footer Layouts; header with Report name, Logo, Date. Shows the feature.
- 76367 Snipaste_2026-09-29_10-33-18.png: XML mapping pane with CompanyMetadata fields. Shows the feature. image-271: roadmap-text snippet only.
- 76205 image-221: Subtype documentation excerpt. Matches. 76231 image-244: roadmap text snippet only (not the flow). 76147 .gif: exists in the post (not played).
- 67892 image-42: Learn changelog snippet (data picker / updated report Word layout XML). Matches.
- 72933 image-95: Report Layouts page grid (generic intro image). The status-specific images are image-96 to image-105, not cited.
- Do not use as evidence: 73030 image-150 (Power BI search box), 73485 image-380 (search box), and image-79-1024x573 (generic Report Layouts list, reused in four posts).
- Not checked: image counts in the file ("23 images", "36 images").

## 3. Counts per verdict (rows of the claims table)

60 rows: CONFIRMED 49, CORRECTED 5 (C4, C8, E4, F2, F4), UNVERIFIED 6 (B3, C2, C6, D2, E2, F6), WRONG 0.

## 4. What to change in recheck-secondary.md / downstream use

1. Replace "conditional visibility first shipped v29" with: Hide If False is new in v29; Hide If Empty (4 controls) has existed since 2024 wave 2 (v25 / "24.4 preview").
2. Fix wording in 1c: 573329 is HideIf (boolean) only.
3. Cite the Learn 29.0 page per RM ID as the v29 anchor.
4. Mark "v29 extends statuses to extension layouts" as inference; Draft-on-copy as already behaving in 28.5.
5. Drop or reword the "first drafted in preview then re-framed" remark, and do not use image-150, image-380, image-79 as feature evidence.
