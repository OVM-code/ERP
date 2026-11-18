# Word layouts new in Business Central 2026 release wave 2 (v29.0, 29.1)

Researched 2026-11-18 (subagent A). Scope: Word layout features first shipped in version 29.x only.

## Read this first: evidence limits

- Microsoft Learn pages were opened through the Microsoft Learn fetch tool and are real sources (listed below).
- The 2026 wave 2 release-plan pages could NOT be opened: the guessed URLs `.../release-plan/2026wave2/smb/dynamics365-business-central/planned-features` and `.../design-document-reports-updated-word-add-in` returned "could not be retrieved". Microsoft states that release plans stopped in September 2026 and moved to the Copilot Roadmap (see What's new 29.0).
- The Copilot Roadmap page (https://www.microsoft.com/en-us/microsoft-365/roadmap?id=573328) opened but returned only the generic JavaScript shell ("0 Updates found"). It gave NO feature detail. Not usable as a source.
- BLOCKED (host not reachable from this session, not opened, not cited as sources): mc.merill.net (all RM57332x/RM573328 seed links), yzhums.com, and learn.microsoft.com through WebFetch. The network allow-list for mc.merill.net and yzhums.com must be extended if Olivia wants those secondary sources checked.
- Consequence: feature NAMES, versions, GA status and roadmap IDs come from the opened What's new 29.0 page. Feature BEHAVIOUR comes from the opened product docs (which describe the v29 experience). Anything neither page states is written UNKNOWN. No screenshot of the v29 add-in or of the new BC pages exists at any opened URL (the only images on opened pages are old overview images, see "Screenshots").
- Seed items I could not confirm as separate features: "New design components in the Word add-in", "Header and footer sample controls" and "Shared company information data item". See the section "Seed items not confirmed".

## Sources actually opened (all Microsoft Learn, via fetch tool)

- S1 What's new 29.0: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-29-0
- S2 What's new 29.1: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-29-1 (contains no Word layout item)
- S3 Design report layouts with the Business Central Word add-in: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-design-word-layouts-business-central-add-in
- S4 Set up reusable themes and header and footer layouts: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-set-up-report-themes-header-footer-layouts
- S5 Report and document layouts overview: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-manage-report-layouts
- S6 Get started creating report layouts: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-get-started-layouts
- S7 Declare report layouts in AL: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-report-layout-declaration
- S8 Creating a Word layout report (developer): https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-howto-report-layout
- S9 Release plan 2026 wave 1, enhanced Word add-in (out of scope, used for exclusion): https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/get-easier-editing-document-report-layouts-enhanced-word-add-in
- S10 Enabling new and upcoming features ahead of time (feature management, generic): https://learn.microsoft.com/en-us/dynamics365/business-central/admin-feature-management
- Search-result excerpt only (not opened as page, so NOT used as a source for facts): Excel layouts page https://learn.microsoft.com/en-us/dynamics365/business-central/ui-excel-report-layouts (it shows the same v29 Draft note for Excel; belongs to the Excel researcher).

## Cross-cutting facts that apply to most features

- Wave and version: all features below are listed in S1 under "2026 release wave 2", update 29.0, each as "General availability". Roadmap IDs are from S1.
- Feature switch: S1 lists "Feature: New Document Report Experience" under "New optional features" as "(disabled by default)", linking to S5. S4 and S6 say the composite-layout experience, the Subtype field and the Composite layout actions need the **Document Report Experience** feature enabled on the Feature Management page. So: "General availability" but opt-in; an administrator must switch it on. (Whether the exact Feature Management display name differs from "New Document Report Experience": UNKNOWN. S1 and S4 use two wordings.)
- Licence: UNKNOWN. No opened page names a licence requirement. Do not claim Premium or Essentials.
- Add-in version number: UNKNOWN. Pages say only "Dynamics 365 Business Central Word add-in", installed from Word: Home, Add-ins, More Add-ins (S3). No add-in build number is stated.
- Customers on 28.x see none of this until the 29 update; online admins can schedule 29.0 within the update period that ends February 2027 (S1).
- 29.1: S2 lists no Word-layout feature. So everything here is 29.0. On-premises 29.1 exists (build 29.1.57326, November 2026; from the on-prem updates search excerpt, not opened as page).

---

## Features in scope (first shipped in 29.0)

### F1. Design document reports with the updated Word add-in (roadmap 573328)

- Wave/version: 2026 wave 2, 29.0, GA (S1). VERSION NOTE: S9 shows an "enhanced Word add-in" shipped in 2026 wave 1 (preview Mar 15, 2026, GA Apr 1, 2026). Microsoft calls the v29 item "the updated Word add-in". Which parts of S3 are NEW in v29 versus wave 1 is UNKNOWN from opened sources. Hold the claim narrow: only items with their own v29 entry (F2 to F4, F7) are safely "new in 29".
- Enabled by: S1 does not say. Add-in is installed by the Word user (S3). Document Report Experience switch by admin for composite parts.
- What it does: the add-in lets non-developers add report fields, labels and report metadata to a Word layout through an **Add Data** task pane, instead of the old XML Mapping Pane (S3).
- How it works (S3):
  1. In Business Central, open Report Layouts, pick the Word layout, choose Layout, Update and Export Layout.
  2. Open the downloaded .docx in Word; the Business Central ribbon tab appears once the add-in is installed.
  3. Choose Add Data; expand Data, Labels or Report Information.
  4. Put the cursor in the document, select a field, choose Add field (a bound content control is inserted).
  5. Save, then in Report Layouts choose Replace Layout and Run Report.
  6. In version 29 the replaced layout becomes Draft; Set as Approved to use it (see F8).
- Problem solved: an invoice or order confirmation needs one extra field (for example a reference) and a consultant no longer has to edit XML mappings by hand.
- Report user value: add or move a field on the invoice without technical help.
- Decision-maker value: fewer change requests to developers for document tweaks.
- Prerequisites: Word with the add-in; file must come from Update and Export Layout (S3: without the embedded metadata the add-in cannot list the fields); layout type Word; user-defined layout (extension layouts cannot be replaced, create a copy first, S3).
- Screenshot wanted: Word window, Business Central ribbon tab, Add Data task pane with the Data group expanded on a Sales Invoice layout; highlight the Add field button.
- Gotchas: the XML Mapping Pane still works as fallback (S3). Overlaps with wave 1 (S9), so do not present "Insert table" as new (see Out of scope).
- Screenshot at source URLs: NO (S3 has no screenshots of the add-in in the fetched text).
- Sources: S1, S3, S9.

### F2. Use conditional visibility in the updated Word add-in (roadmap 573329)

- Wave/version: 2026 wave 2, 29.0, GA (S1). No earlier-wave entry found in opened sources.
- Enabled by: UNKNOWN (add-in feature, used by the layout designer).
- What it does: hides content on the rendered document when there is no value, so empty or zero parts do not print (S3, section "Hide content that has no value").
- How it works (S3):
  1. In Word, select the content (field, table, row or header field).
  2. On the Business Central tab choose a control under **Hide if empty**.
  3. Controls: Hide Field if Zero (stand-alone field or field in repeater), Hide Empty Table (select the table, not the repeater), Hide Empty Table Row (select the field controlling the row), Hide Empty Table Column (select the controlling header field).
  4. Combine Hide Field if Zero (row field) with Hide Empty Table Column (header field) to remove a column nobody uses.
  5. Replace the layout and run the report to check.
- Problem solved: a discount column or a zero line prints on every invoice even when nothing is discounted (S3 gives the discount-column example).
- Report user value: cleaner invoices without a developer adding RDLC or AL logic.
- Decision-maker value: customer-facing documents look professional with less per-customer rework.
- Prerequisites: add-in, Word layout. Mapping to the "conditional content" in the seed (hide if empty OR false): S3 documents "hide if empty/zero" only. A "hide if false" control: UNKNOWN, not found.
- Screenshot wanted: Business Central ribbon tab with the Hide if empty dropdown open, and a before/after invoice with the Discount % column present vs removed.
- Gotchas: selection differs per control (table vs field); wrong selection gives the wrong behaviour (S3). Dataset logic that is not empty/zero still needs AL (S8: Word layout cannot calculate; totals come from AL).
- Screenshot at source URLs: NO.
- Sources: S1, S3.

### F3. Design header/footer layouts for document reports with the updated Word add-in (roadmap 573331)

- Wave/version: 2026 wave 2, 29.0, GA (S1).
- Enabled by: admin turns on Document Report Experience; designer authors the file. Authoring controls: UNKNOWN beyond S4.
- What it does: a header/footer becomes its own Word file (.docx, Subtype HeaderFooter) that can be designed with the add-in, instead of living inside each body layout (S4, S7).
- How it works (S4):
  1. Open Manage themes and header-footer layouts; choose New header/footer; name it.
  2. Upload the .docx header/footer file (design it in Word with the add-in).
  3. Part Status, Set Approved (new user parts start as Draft).
  4. Assign it (see F5).
- Problem solved: changing the logo or company address in the page header used to mean editing every invoice, quote and statement layout.
- Report user value: edit the header once.
- Decision-maker value: one controlled place for corporate identity and legal footer text.
- Prerequisites: Document Report Experience on; layout Subtype Body for the reports that consume it; header/footer file is .docx (S4).
- Screenshot wanted: Manage themes and header-footer layouts page with one header/footer row and its status; plus the header file open in Word with company logo content control.
- Gotchas: "Header and footer sample controls" in the seed: no opened page names sample controls. UNKNOWN (see Seed items not confirmed). "Different first page" and "different odd and even" headers are not supported for HTML conversion, so the header does not appear in e-mail body output (S8, general rule, not stated as v29-new).
- Screenshot at source URLs: NO.
- Sources: S1, S4, S7.

### F4. Design document report themes with the updated Word add-in (roadmap 573330)

- Wave/version: 2026 wave 2, 29.0, GA (S1).
- Enabled by: admin (Document Report Experience) plus designer.
- What it does: a theme is a Word template (.dotx, Subtype Theme) holding fonts, colours and styles, designed once and reused (S4, S7).
- How it works (S4):
  1. Manage themes and header-footer layouts, New theme, name it.
  2. Upload the .dotx file.
  3. Part Status, Set Approved.
  4. Assign it as global, company, report or layout default (F5).
- Problem solved: invoice, order confirmation and credit memo each use slightly different fonts and colours.
- Report user value: restyle all documents by swapping one file.
- Decision-maker value: consistent brand across documents, lower maintenance.
- Prerequisites: theme must be .dotx; only Body-subtype Word layouts can use themes (S4, S7).
- Screenshot wanted: Report Layouts page Details FactBox showing Theme and Theme source; a PDF before/after.
- Gotchas: "New document sample controls" in the add-in for themes (Roadmap title wording seen only in a search-result summary of mc.merill.net, unopened): UNKNOWN. Extension-provided themes can be exported but not edited, replaced or deleted (S4).
- Screenshot at source URLs: NO.
- Sources: S1, S4, S7.

### F5. Brand document reports with report themes (roadmap 573327) and Reuse header/footer layouts across document reports (roadmap 573326)

Treated as one story because the docs describe them as one composite-layout mechanism; both are separate entries in S1.

- Wave/version: 2026 wave 2, 29.0, GA (S1 both).
- Enabled by: administrator (assign defaults); Document Report Experience must be enabled (S4).
- What it does: splits a document into Body + Theme + Header/Footer and combines them at run time ("composite layout"). Assign a default globally, per company, per report or per body layout; theme and header/footer resolve independently (S4, S5).
- How it works (S4):
  1. Set global default: search Report defaults for theme and header-footer, Add global default, pick approved Header/Footer Part and Theme Part.
  2. Company default: Company Information, Reporting FastTab, Default Theme and Default Header/Footer.
  3. Report default: Set for one report on the defaults page.
  4. One layout: Report Layouts, select Body layout, Composite layout, Set report theme and header-footer.
  5. Check result in the Details FactBox or Composite layout, Set all report theme and header-footer (Theme source / Header/Footer source columns).
  6. Resolution order, most specific first: layout in company, layout all companies, report in company, report all companies, company, global (S4).
- Problem solved: a group with several companies and brands needs different logos and fonts per company without cloning every document layout.
- Report user value: documents of every report pick up the right brand automatically.
- Decision-maker value: brand compliance across entities with central control; updating a part updates all body layouts that use it (S4).
- Prerequisites: Word layout with Subtype Body (set in Add New Layout dialog; S6); approved parts; Document Report Experience on.
- Screenshot wanted: Report defaults for theme and header-footer page with a global row and a company row, Applies to column highlighted; plus Company Information Reporting FastTab.
- Gotchas (S4): changing a part from Approved to another status does NOT remove existing assignments; Details FactBox and the per-layout page can show None although an extension-declared fallback part is used; deleting a part clears direct assignments.
- Developer side (S7): AL gets `Subtype = Default | Body | HeaderFooter | Theme`, and report properties `DefaultHeaderFooterPart` and `DefaultThemePart` (applies to 2026 wave 2 and later; runtime 18.0).
- Screenshot at source URLs: NO.
- Sources: S1, S4, S5, S6, S7.

### F6. Control the lifecycle of all report layouts (roadmap 573320)

- Wave/version: 2026 wave 2, 29.0, GA (S1). Layout-management page change; applies to all layout types, not only Word.
- Enabled by: admin or whoever manages layouts (Report Layouts page).
- What it does: every layout gets a status: Draft, Pending Approval, Approved, Retired. Only Approved layouts can be chosen on report request pages (S6).
- How it works (S6, S3):
  1. New user-defined layouts start as Draft; replacing a layout file in v29 also resets it to Draft (S3).
  2. Test with Run Report.
  3. Layout, Layout Status, Set Approved (or Pending Approval, Retired, Draft); multiple layouts can be selected.
  4. Changing the status of an extension layout is stored as an override; the extension file is unchanged (S6).
  5. Optional telemetry about layout actions exists since v25 (not new).
- Problem solved: a half-finished invoice layout was selectable by colleagues, or a test layout went to customers.
- Report user value: only finished layouts show in the dropdown.
- Decision-maker value: change control and an approval step on customer-facing documents.
- Prerequisites: permissions to edit layouts (exact permission set: UNKNOWN).
- Screenshot wanted: Report Layouts list with the Layout Status column and the Layout, Layout Status menu open.
- Gotchas: after Replace Layout the layout silently drops to Draft; users who forget Set as Approved wonder why the layout vanished from the request page (S3). Automatic setting of existing layouts on upgrade: UNKNOWN.
- Screenshot at source URLs: NO.
- Sources: S1, S3, S6.

### F7. Reduce complexity of report datasets (roadmap 573321)

- Wave/version: 2026 wave 2, 29.0, GA (S1).
- Everything else: UNKNOWN. The only opened source is the title in S1. The seed claims a "shared company information data item in report datasets" (mc.merill.net RM573321, blocked). S7 mentions a `CompanyMetadata` element in `BCReportInformation` that composite Body layouts use to resolve header/footer and theme, maintained by compiler and add-in; that is a plumbing detail, not proof of the seed claim. Do not present this as a feature until a source is opened.
- Screenshot at source URLs: NO.
- Sources: S1 (title), S7 (CompanyMetadata, related only).

### F8. Developer-side Word items (mention only if the audience is partners)

- Runtime 18.0 (2026 wave 2): compiler always embeds the extended custom XML parts so Word layouts are add-in compatible; feature flag `WordAddInCompatibleLayouts` is deprecated for runtime 18+ (S7).
- Layout paths accept both / and \ (portable on Windows and Linux) (S7).
- Not interesting for report users or decision-makers; one line at most.
- Sources: S7.

---

## Out of scope, older (do NOT show as new)

| Item | First shipped | Evidence |
|---|---|---|
| Enhanced Word add-in editing (data picker with nested data items, search/filter, metadata, dark mode, double-click insert) | 2026 wave 1, preview Mar 15 2026, GA Apr 1 2026 | S9 |
| Insert Table wizard (Create Data Table dialog) | 2026 wave 1, listed there as "currently in preview"; GA date in 29.0 UNKNOWN. Show as wave 1, or label "preview in wave 1" | S9 (S3 documents it without a version) |
| Report and request metadata system data items (ReportMetadata, ReportRequest) in Word layouts | 2025 wave 1 (v26) | S8 |
| Update and Export Layout, create blank layout from report object, Export report schema | 2024 wave 2 (v25) | S8 |
| Layout lifecycle telemetry | 2024 wave 2 (v25) | opened telemetry text only in search excerpt, treat as UNKNOWN-confirm |
| WordMergeDataItem with sections fix | 2024 wave 2 | S8 |

## Seed items not confirmed (do not present as separate features)

- "New design components in the Word add-in" (RM573328): treated as F1; component list not verifiable.
- "Header and footer sample controls" (RM573331): F3 title only; "sample controls" wording unverified.
- "Shared company information data item" (RM573321): F7; unverified.
- "Reuse header and footer layouts across document reports" (RM573326) and "Report themes" (RM573327): confirmed as titles and behaviour (F5).
- yzhums.com walkthroughs: host not reachable; no URL cited.

## Screenshots

No opened URL contains a screenshot of any v29 feature. For the presentation, Olivia must capture her own in a version 29 sandbox. Version 29 sandbox availability: assumed NO in the brief. Her demo environment is 28.5, so none of F1 to F7 can be shown live there; the Document Report Experience feature and Subtype field do not exist in 28.5 (inference from S1 and S6, stated as new in 29).

## Open questions for Olivia

1. Can she get a version 29 sandbox or preview environment for screenshots?
2. Allow mc.merill.net, yzhums.com and WebFetch for learn.microsoft.com in session network settings so secondary sources can be checked?
3. Does she want 573318 "Automate report outputs" (S1, Reporting area; Word relevance UNKNOWN) checked?
