# BC Word & Excel layouts: plan and agent instructions

Nov 18, 2026 · @Olivia

## Goal and scope

The agent run produces one decision pack: every feature found, its client value, a score, and a proposed 15-minute run of show. You pick the features; the agents do not.

| Item | Decision |
| --- | --- |
| Word layouts | Only features new in 2026 release wave 2 (version 29). Anything from wave 1 or earlier is excluded. |
| Excel layouts | Everything new from 2025 release wave 1 through 2026 release wave 2 (versions 26, 27, 28, 29). |
| Audience | Mixed: users who edit reports and decision-makers who pay for them. Each feature gets one value line for each group. |
| Word format | Screenshots, no live demo. |
| Excel format | Live demo in one report, plus a comparison with analysis mode and Power BI. |
| Where it runs | Claude Code. Opus orchestrates and synthesises; Sonnet subagents research. |
| Language of the output | English (assumed; say so in the kickoff if you want Dutch). |

For Excel, the agents separate two kinds of news: new capabilities of Excel layouts as a technology, and new Microsoft-shipped reports that come with an Excel layout. Both count, but only the first kind is a "feature" you can demo in any report.

One input is still missing: the exact version of your demo environment. Fill it in under the orchestrator prompt before you start.

## Settle this first: you have no version 29 environment

Every Word feature in scope exists only in version 29, so you cannot take your own screenshots in an older environment. Decide before the agents run, because it changes the Word shot list.

| Option | Effort | Result |
| --- | --- | --- |
| A. Get a version 29 sandbox (recommended) | Check in the Business Central admin center whether you can create a new sandbox or trial on version 29 | Your own screenshots on Cronus data, and the Excel demo can show version 29 features too |
| B. Use published screenshots | None | Screenshots from Microsoft Learn and community blogs, shown with credit; less convincing and you cannot answer "show me" questions |

The same gap affects Excel: any Excel feature newer than your environment cannot be in the live demo. The demo-report agent therefore marks each feature as "demoable in your version" or "slide only".

Second point of pushback: 15 minutes holds about five or six features in total, not a full tour. The scoring exists to cut, so expect to drop more than you keep.

## Plan

Three research tasks run in parallel, followed by one dependent task, one independent check and one synthesis. You do the setup before and the selection after.

| Step | Who | Task | Runs | Output file |
| --- | --- | --- | --- | --- |
| 0 | You | Create an empty folder, export this doc as Markdown to `PLAN.md`, fill in your environment version, start Claude Code on Opus | First | `PLAN.md` |
| 1 | Sonnet A | Word layout features new in version 29 | Parallel with 2 and 3 | `research/word-v29.md` |
| 2 | Sonnet B | Excel layout features, versions 26 to 29 | Parallel with 1 and 3 | `research/excel-v26-v29.md` |
| 3 | Sonnet C | Excel layouts versus analysis mode versus Power BI | Parallel with 1 and 2 | `research/comparison.md` |
| 4 | Sonnet D | Best report to demo the Excel features in | After 2 | `research/demo-report.md` |
| 5 | Sonnet E | Fresh-eyes check of every claim against its source | After 1 to 4 | `research/verification.md` |
| 6 | Opus | Score, cut to 15 minutes, write the decision pack | After 5 | `output/decision-pack.md` |
| 7 | You | Pick features, capture screenshots, rehearse with a timer | Last | The presentation |

Research goes to Sonnet because it is wide, repetitive lookup work. Scoring and cutting go to Opus because they need judgment across all four research files. The verifier is a separate agent so the research does not grade itself; wrong release-wave attribution is the most likely error and it would break your Word scope.

Kickoff line to type in Claude Code: `Read PLAN.md and execute the Opus orchestrator prompt. Use the Sonnet briefs verbatim.`

## Scoring and time budget

Each feature gets four scores from 1 to 5, weighted into a total out of 100.

| Criterion | Weight | 5 means | 1 means |
| --- | --- | --- | --- |
| Client value | 40% | Removes a developer dependency or saves hours every month | Cosmetic or rarely needed |
| Breadth | 20% | Almost every client uses the affected reports | One niche role or industry |
| Demo impact | 25% | Understood from one screenshot or under 60 seconds live | Needs long setup or explanation |
| Readiness | 15% | Generally available, on by default, no extension needed | Preview, or needs developer work first |

Total = (value x 8) + (breadth x 4) + (demo impact x 5) + (readiness x 3). Every score comes with a one-sentence reason, so you can overrule it.

Default time budget the run of show must fit:

| Block | Minutes | Content |
| --- | --- | --- |
| Opening | 1 | Why layouts matter: reports users can change themselves |
| Word layouts | 5 | Top 3 features, one or two screenshots each |
| Why Excel layouts | 1.5 | The comparison with analysis mode and Power BI on one slide |
| Excel demo | 5.5 | One report, 2 to 3 features live |
| Close | 2 | What to do Monday, questions |

Cut rule: features are added in score order until a block is full. Anything below 60 goes to a backup slide.

## Opus orchestrator prompt

Opus coordinates, never researches features itself, and writes the final decision pack. Fill in the two bracketed values before running.

```text
ROLE
You are the orchestrator for a presentation-prep project. You run on Opus.
You delegate research to Sonnet subagents and you write the final synthesis yourself.

CONTEXT
Olivia is a Business Central consultant. She gives a 15-minute presentation on
what is new in Word layouts and Excel layouts in Dynamics 365 Business Central.
Audience: mixed (report users and decision-makers at client companies).
Her demo environment version: 28.5
Version 29 sandbox available: NO (assumed; to confirm with Olivia)
Today is after general availability of 2026 release wave 2 (version 29, October 2026).

SCOPE (hard rules)
- Word layouts: ONLY features introduced in 2026 release wave 2 (version 29.x).
  A feature first shipped in 2026 wave 1 or earlier is out, even if improved later;
  in that case list only the version 29 improvement.
- Excel layouts: features introduced in 2025 wave 1, 2025 wave 2, 2026 wave 1,
  2026 wave 2 (versions 26, 27, 28, 29).
- No feature without a source URL that was actually opened.

STEPS
1. Create folders research/ and output/.
2. Start subagents A, B and C in parallel, model sonnet, each with its brief from
   PLAN.md verbatim plus the CONTEXT and SCOPE blocks above.
3. When B is done, start subagent D (model sonnet) with its brief and the path to
   research/excel-v26-v29.md.
4. When A to D are done, start subagent E (model sonnet) as verifier. Give it only
   its brief and the four file paths, not your own impressions.
5. Read research/verification.md. Drop every claim marked UNVERIFIED or WRONG, or
   send the owning subagent back once to fix it. Do not repair claims from memory.
6. Write output/decision-pack.md (structure below).
7. Report back in under 10 lines: number of features found per area, top 3 per
   area, and the open questions for Olivia.

SCORING (apply to every verified feature)
Four scores 1-5: client value, breadth, demo impact, readiness.
Total = value*8 + breadth*4 + demo*5 + readiness*3 (max 100).
One sentence of reasoning per feature. Score for a mixed audience of Flemish
SMEs on Business Central online. Be harsh: a 5 is rare.

DECISION PACK STRUCTURE
1. Word layouts: table sorted by total score. Columns: feature, what it does
   (one line), value for users, value for decision-makers, four scores, total,
   include/backup/cut, source links.
2. Word screenshot shot list for the included features: which screen, what to
   highlight, before/after if useful, and whether she can capture it herself or
   which published screenshot to use (URL).
3. Excel layouts: same table, plus columns "introduced in version" and
   "demoable in her version (yes/no)".
4. Why Excel layouts: the comparison table from subagent C, plus one sentence
   she can say out loud, plus the cases where Excel layouts are the wrong choice.
5. Demo report: the recommended report, why, and a click-by-click path that fits
   5.5 minutes and shows the included Excel features.
6. Run of show: fit the time budget (opening 1, Word 5, why Excel 1.5, Excel
   demo 5.5, close 2). Add features in score order until each block is full.
7. How-it-works sources: per included feature, the Microsoft Learn page and at
   most one walkthrough blog.
8. Open questions and anything you could not verify.

STYLE
Plain English, short sentences, tables over prose. Value statements name a
concrete outcome (time saved, no developer needed, fewer errors), never
"improved experience". Do not copy source text; paraphrase and link.
```

## Sonnet subagent briefs

Five briefs, each self-contained. All five share the same source rules, listed once here and repeated by Opus to each agent.

```text
SOURCE RULES (all subagents)
- Primary: learn.microsoft.com release plans for Business Central (2025wave1,
  2025wave2, 2026wave1, 2026wave2), the "What's new" pages per version, and the
  product docs on report layouts.
- Secondary: Microsoft 365 roadmap entries, the Business Central launch-event
  videos, and walkthrough blogs with screenshots (for example yzhums.com).
- Open every page you cite. A search snippet is not a source.
- For each feature record: name, wave and version it first shipped in, status
  (generally available / preview), enabled by whom (automatic / admin / developer),
  what it does in your own words, how it works in 3-6 steps, source URLs,
  and whether a usable screenshot exists at one of those URLs.
- If two sources disagree on the version, say so and keep both URLs.
- Never fill a gap from memory. Write UNKNOWN instead.
- No copied paragraphs. Paraphrase.
```

### Sonnet A: Word layouts, version 29 only

```text
TASK
List every Word layout feature that is new in Business Central 2026 release
wave 2 (version 29.0 and its minor updates so far). Write research/word-v29.md.

INCLUDE
Word report layouts, the Business Central Word add-in, document report design,
headers/footers, themes, conditional content, dataset changes that affect Word
layouts, layout management pages when they change how Word layouts are handled.

EXCLUDE AND LIST SEPARATELY
Anything that first shipped before version 29 (for example the enhanced Word
add-in editing from 2026 wave 1). Put these in a short "Out of scope, older"
list with the version, so the presenter does not show them by mistake.

PER FEATURE, ADD
- The problem it solves for someone editing an invoice or order confirmation.
- Value for a report user (one line) and for a decision-maker (one line).
- Prerequisites: add-in version, licence, feature switch, layout type.
- What a good screenshot would show (screen and the element to highlight).
- Limits or gotchas you found.

START FROM, BUT VERIFY
The seed list in PLAN.md under "Starting sources". It is unverified.
```

### Sonnet B: Excel layouts, versions 26 to 29

```text
TASK
List everything new for Excel layouts in Business Central from 2025 release
wave 1 through 2026 release wave 2. Write research/excel-v26-v29.md.

SPLIT INTO TWO TABLES
1. Capabilities: new things Excel layouts can do or new ways to create, edit,
   manage, schedule or distribute them (platform and user-facing).
2. Content: Microsoft-shipped reports that received a new or improved Excel
   layout, grouped by area (finance, sales, purchasing, inventory, and so on),
   with the report name and number where available.

PER CAPABILITY, ADD
- Version and wave, status, who can use it without a developer.
- Value for a report user (one line) and for a decision-maker (one line).
- How it works in 3-6 steps, with the Microsoft Learn how-to URL.
- Limits: row counts, performance, what still needs a developer.

ALSO
Go wave by wave so nothing is skipped: 2025wave1, 2025wave2, 2026wave1,
2026wave2. End with a count per wave.
```

### Sonnet C: why Excel layouts instead of analysis mode or Power BI

```text
TASK
Compare three ways to analyse Business Central data: Excel report layouts,
analysis mode (data analysis on list pages and queries), and Power BI
(including the shipped Power BI apps). Write research/comparison.md.

COMPARE ON
Who builds it and what skills they need; who maintains it; licence and extra
cost; data freshness; data volume limits; combining several tables or sources;
formatting, printing and fixed layouts; scheduling and emailing; sharing and
reuse across users and companies; parameters and filters at run time;
governance and security; offline use; fit with existing Excel habits.

OUTPUT
1. One table: rows are the criteria above, columns are the three tools.
   Keep each cell under 12 words.
2. "Pick this when": three bullets per tool with concrete client situations.
3. Honest section: situations where Excel layouts are the wrong choice.
4. One sentence a presenter can say to explain where Excel layouts sit
   between the other two.
Every row of the table needs a Microsoft Learn URL behind it. Mark opinion
as opinion.
```

### Sonnet D: which report to demo

```text
TASK
Recommend the single best standard report for a 5.5-minute live demo of the
Excel layout features. Input: research/excel-v26-v29.md. Write
research/demo-report.md.

CRITERIA
- Exists with a Microsoft-shipped Excel layout in the presenter's version
  (given in CONTEXT). Say from which version the report and layout exist.
- Produces meaningful output on Cronus demo data without setup.
- Recognisable to both finance and operations people.
- Lets the presenter show the largest number of capabilities from table 1.
- Runs fast and has run-time filters worth showing.

OUTPUT
- Three candidates in a table scored on the five criteria, one recommended.
- For the recommended report: which capabilities it can show, marked
  "demoable in her version" or "slide only", and a click-by-click path with
  a time per step that adds up to 5.5 minutes.
- One realistic client use case to frame the demo (who needs this report,
  how often, what they do with it in Excel afterwards).
- A fallback report if the first one returns empty data.
```

### Sonnet E: verifier

```text
TASK
You did not write the research files. Check them. Write
research/verification.md.

FOR EVERY FEATURE AND EVERY COMPARISON ROW
- Open the cited URL. Does the page say what the file claims?
- Is the version and wave correct? This is the most likely error. A Word
  feature that shipped before version 29 must be flagged WRONG SCOPE.
- Is the status correct (generally available versus preview)?
- Mark each claim CONFIRMED, CORRECTED (with the correction and URL),
  UNVERIFIED, or WRONG.

ALSO
- Search once more per wave for Word and Excel layout features the files
  missed. List them under "Possibly missing" with a URL.
- Check the demo report exists in the stated version.
Be strict. Do not soften a finding because the file looks thorough.
```

## Starting sources

These came from a quick search on 18 November 2026; the pages were not opened, so the agents treat every line as a lead to verify, not a fact.

Word layouts, likely version 29:

| Lead | Where |
| --- | --- |
| New design components in the Word add-in | [Roadmap 573328](https://mc.merill.net/message/RM573328) |
| Conditional visibility (hide if empty or false) | [Roadmap 573329](https://mc.merill.net/message/RM573329) |
| Header and footer sample controls | [Roadmap 573331](https://mc.merill.net/message/RM573331) |
| Reuse header and footer layouts across document reports | [Roadmap 573326](https://mc.merill.net/message/RM573326) |
| Report themes for consistent branding | [Roadmap 573327](https://mc.merill.net/message/RM573327) |
| Shared company information data item in report datasets | [Roadmap 573321](https://mc.merill.net/message/RM573321) |
| Per-feature walkthroughs with screenshots | [yzhums.com, Business Central posts](https://yzhums.com/tag/dynamics-365-bc/) |

Out of scope for Word, to avoid by mistake: the easier editing in the enhanced Word add-in shipped in 2026 wave 1 ([release plan](https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/get-easier-editing-document-report-layouts-enhanced-word-add-in)).

Excel layouts, leads so far:

| Lead | Version | Where |
| --- | --- | --- |
| Subtotals added to Excel layouts of built-in sales reports | 28 | [yzhums.com](https://yzhums.com/73030/) |
| Inventory reports modernised with Excel and Word layouts | 28 | [Release plan](https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/modernizing-analytical-reports-inventory) |
| Deferral and trial balance reports with Excel layouts | 27 and 28.1 | [yzhums.com](https://yzhums.com/73485/) |
| Control over the lifecycle of report layouts | 28 | [Release plan](https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/smb/dynamics365-business-central/control-lifecycle-report-layouts) |

The Excel list is thin for versions 26 and 29; Sonnet B's wave-by-wave pass is there to close that gap.
