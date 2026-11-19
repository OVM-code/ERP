# Prompt for Claude in PowerPoint

How to use:
1. Open your existing Word-features deck in PowerPoint, so Claude reuses its theme, slide master and your Word screenshots.
2. Open Claude in PowerPoint (Home > Claude) and paste everything between the two lines below as one message.
3. Let it propose the outline first (step 1 of the prompt), check it, then say "go".

Source: `output/decision-pack.md`, updated 19 Nov 2026 after both verification passes.

---

```text
ROLE
You build a 15-minute presentation deck in this open PowerPoint file. Use the
existing slide master, theme, fonts and colours. Do not invent a new design.

WORK IN THIS ORDER
1. Look at the slides already in this file. Some contain my screenshots of Word
   layout features. List them (slide number, what the screenshot shows) and map
   each to slides W1, W2 or W3 below. Then show me the outline you will build
   and wait for my "go".
2. After "go": build the slides below in this order. Reuse my existing
   screenshots on the matching slides; never delete one of my slides. Move
   slides you don't use to the end, under a section called "Unused".
3. Where a screenshot is needed and I have none, insert a grey placeholder box
   labelled "SCREENSHOT: <what to show>". Do not search for or generate images.
4. Put the speaker notes I give below into each slide's notes.
5. At the end, list every placeholder and anything you were unsure about.

HARD RULES (content is verified; do not add to it)
- Do not add features, version numbers, dates, licence claims or statistics
  that are not in this prompt. If something seems missing, ask me.
- Word features shown are new in Business Central 2026 release wave 2
  (version 29). Never label any of these as new in version 29:
  Add Data pane (v27), Insert Table / enhanced add-in (v28), layout statuses
  Draft/Approved (v28), Hide If Empty controls (2024 wave 2), a copy starting
  as Draft (already in 28.x). Insert Table (slide W3) is shown with its own
  label "since 2026 wave 1", not as new in 29.
- Do not mention Hide If Empty or Hide If False anywhere in the deck.
- If one of my existing slides shows Hide If Empty or Hide If False, move it to
  "Unused" and tell me.
- English text. Business Central terms exactly as written here.
- Max 6 bullets per slide, max ~8 words per bullet. Tables max 6 rows.
  Plain words: no "improved experience", "seamless", "powerful".
- Small source line at the bottom of each feature slide (text given below).

AUDIENCE
Flemish SME clients on Business Central online: people who edit reports and
decision-makers who pay for them. 15 minutes: Opening 1:00, Word 5:00,
Why Excel 1:30, Excel live demo 5:30, Close 2:00.

SLIDES

1. Title
   Title: What's new in Word and Excel layouts
   Subtitle: Business Central 2026 release wave 2 · [presenter name, date]
   Notes: none.

2. Reports you change yourself  (Opening, 1:00)
   Bullets:
   - Layouts decide how a report looks
   - Word: documents customers see
   - Excel: reports you analyse
   - Both: changed by key users, not developers
   Notes: "Today: what's new for Word in the October 2026 release, and what
   Excel layouts can do since 2025. Most of it you can use without a developer."

3. Word layouts in version 29: three things  (Word, 0:20)
   Three tiles: Design components · One header/footer for all documents ·
   Insert Table
   Callout box: "Off by default: an admin enables 'New Document Report
   Experience' in Feature Management."
   Notes: "Generally available since October, but the header/footer and theme
   features stay off until an admin turns on the switch. Check this first at
   your clients."

4. W1 · Design components in one click  (Word, 1:40)
   Bullets:
   - Ready-made blocks on the Word add-in ribbon
   - Addresses, field groups, amounts, signature lines, notes
   - Build an order confirmation block in one click
   - Less consultant time per document layout
   Visual: my screenshot of the ribbon / before-after, else placeholder
   "SCREENSHOT: BC ribbon in Word with Address Fields, Grouped Fields,
   Calculation Layouts, Signature Lines, Note Lines; empty layout vs after
   three clicks".
   Source line: Microsoft 365 roadmap 573328 · What's new in BC 29.0
   Notes: "Before, you mapped every field one by one. Now you insert a whole
   address block or totals table at once. For decision-makers: layout projects
   get shorter."

5. W2 · One header and footer for all documents  (Word, 1:40)
   Bullets:
   - Header/footer is its own Word file
   - Used by invoice, quote, order, credit memo
   - Default per company, per report or per layout
   - Five sample headers and five footers included
   - Themes work the same way: fonts and colours once
   Visual: my screenshot of the "Report defaults for theme and header-footer"
   page or two documents with the same footer, else placeholder.
   Source line: Microsoft Learn: Set up reusable themes and header and footer
   layouts · roadmap 573326, 573331, 573330
   Notes: "New logo or new address? Today you edit every layout. With this you
   edit one file. For groups with several companies: each company gets its own
   branding without copying layouts. Remember: only after the admin switch."

6. W3 · Insert Table: repeater tables in one dialog  (Word, 1:00)
   Bullets:
   - One dialog builds the whole data table
   - Pick data source, columns, order
   - Header row and captions filled in
   - Repeater and footer bound automatically
   - No manual Add repeater, field by field
   Visual: my screenshot of the Create Data Table dialog / the resulting
   table, else placeholder "SCREENSHOT: Create Data Table dialog with data
   source, columns and Include header row; the inserted line table".
   Source line: Microsoft Learn: Design report layouts with the Business
   Central Word add-in · Release plan 2026 wave 1
   Label on the slide: "Since 2026 wave 1 (preview), now standard in the
   add-in". Do NOT label this slide "new in version 29".
   Notes: "Before, a line table meant: draw a table, select the row, add a
   repeater, then add every field cell by cell. Now one dialog does it,
   including headers and a footer row. It arrived as a preview in the spring
   release; today it is the standard way in the add-in."

7. Where Excel layouts fit  (Why Excel, 1:30)
   Table, 4 columns: (criterion) | Excel layouts | Analysis mode | Power BI
   - Who builds it | Key user in Excel | End user, no build | Power BI skills
   - Extra licence | None stated | Permission set only | Power BI Pro per viewer
   - Data freshness | Snapshot at run time | Live when opened | Last refresh
   - Printing | Download, print from Excel | Not stated | Not stated
   - Scheduling | Job queue to Report Inbox | None found | Scheduled refresh
   - Excel habits | Formulas, pivots, slicers | Pivot-like | Separate tool
   Source line: Microsoft Learn: Excel layouts · Analysis mode · Power BI apps
   Notes: "Excel layouts sit in the middle: more finished and repeatable than
   analysis mode, which is a quick look you build yourself, but lighter and
   cheaper than Power BI, which is a separate dashboard tool with its own
   licences and refresh schedule. Not for invoices or print-perfect output:
   that's Word. Not for live dashboards for many people: that's Power BI."

8. Your standard reports already moved to Excel  (Excel, framing ~0:30)
   Title as above. Table "Area | Examples | Since":
   - Finance | Trial balances, Aged receivables/payables, Fixed assets | 2025 wave 1
   - Sales | Customer/Item Sales and 9 more | 2025 wave 2
   - Deferrals | G/L, Sales, Purchase Deferral Summary | 2025 wave 2
   - Inventory | 8 reports incl. Availability Plan | 2026 wave 1
   - Manufacturing | Quantity Explosion of BOM, Where-Used, Prod. Order List | 2025 wave 2
   Footer line: "2026 wave 1: subtotals added to sales and deferral Excel reports"
   Notes: "About 37 standard reports now come with an Excel layout. You don't
   build them: you open them."

9. Live demo: Customer/Item Sales (report 113)  (Excel, 5:00 live)
   Bullets (what you'll see):
   - Run-time filters on the request page
   - Excel layout with print and analysis sheets
   - Subtotals built in (2026 wave 1)
   - Validate a layout copy (2025 wave 1)
   - Draft vs Approved: only approved reaches users (2026 wave 1)
   Notes (demo script, 5:30 incl. this slide):
   1 Alt+Q Customer/Item Sales, set Posting Date, narrow Item No. (0:40)
   2 Pick the Excel layout, run (0:25)
   3 Print sheet, then analysis sheet, point at subtotals (0:55)
   4 Slicer or filter, collapse a group (0:35)
   5 Flash the data sheet, close (0:15, drop if late)
   6 Report Layouts, filter 113, status column (0:25)
   7 Edit Info > Save Changes to Copy, copy shows status Concept/Draft (0:35)
   8 Validate the copy (0:25)
   9 Request page: copy not listed; Set Approved; now listed (0:40)
   10 Back to this slide: recap (0:35)
   Use case to open with: "A sales controller runs this every month after
   closing, filters top customers, checks discount against profit, and sends it
   on. The subtotals now come built in."

10. Monday morning  (Close, 2:00)
    Bullets:
    - Plan the version 29 update; test in a sandbox
    - Enable New Document Report Experience there
    - List layouts with duplicated headers or empty blocks
    - Move users to the Excel versions of standard reports
    - Set layout statuses: only approved layouts live
    Then: "Questions?"
    Notes: none.

BACKUP (section "Backup", after slide 10)

B1. Not new in version 29 (avoid on stage)
    Table "Feature | Shipped":
    - Add Data pane in the Word add-in | 2025 wave 2
    - Enhanced add-in editing (data picker, search) | 2026 wave 1
    - Layout statuses Draft/Approved/Retired | 2026 wave 1
    - Copy of a layout starts as Draft | already in 28.x

B2. Also new, not in the main story
    - Report themes (version 29): fonts and colours in one .dotx file
    - Company Information data item in Word datasets (version 29)
    - Layout statuses for all layout types (version 29, details not documented)
    - Faster Trial Balance Excel reports (2026 wave 1)
    - Multiple data sheets per Excel layout (2025 wave 1, developer)
    - Mark a layout as obsolete (2025 wave 1)

B3. Sources
    - What's new in Business Central 29.0 (Microsoft Learn)
    - Set up reusable themes and header and footer layouts (Microsoft Learn)
    - Get started with report layouts (Microsoft Learn)
    - Excel report layouts (Microsoft Learn)
    - Release plan 2026 wave 1: easier editing with the enhanced Word add-in
    - Microsoft 365 roadmap 573326, 573328, 573330, 573331
    - Walkthroughs: yzhums.com (Dynamics 365 Business Central posts)
```

---

Notes for you, not for Claude:
- If you use any yzhums.com screenshot to fill a gap, credit it on the slide. Posts 76696 and 76756 show the features; image-79, image-150 and image-380 don't.
- Insert Table is your call against the "version 29 only" Word rule: the 2026 wave 1 release plan already describes the same dialog (preview). No source shows a version 29 change, so the slide says "since 2026 wave 1".
- The demo UI is Dutch ("Concept"). Either say both words or switch the demo user to English.
