# Maintenance — designed to cost minutes, not days

Everything is markdown in git. No servers, no database, no subscriptions for the system
itself. The only recurring costs are your LLM usage (Claude and/or Copilot Studio
messages) and your minutes. This page is the entire operations manual.

## The three routines

### 1. Per decision (~5 min, mostly automatic)
When you confirm a setup choice in a session, the assistant writes the SDR (or gives
you the copy-paste block in Copilot Studio). You review, save, commit.

### 2. Per project milestone (~15 min)
At go-live / +3 months, open the client's SDRs and fill the *Outcome & review*
sections — the assistant walks you through them as a checklist. Approve any
lessons-learned entries it proposes from the outcomes.

### 3. Per software release (~30–60 min, 2–3× per year)
Business Central has two release waves per year (April & October); Aptean releases on
its own cadence. After release notes are out, ask the assistant:
*"Here are the release notes / what's new links — check them against the knowledge
files and propose edits."* Review the diff, commit. The `Last reviewed:` stamp in every
file header tells you what's overdue: grep for stamps older than ~8 months.

### 4. Per BC knowledge update you want to share (~1 min)
If you distribute the Business Central edition (`share/README.md`), run
`share/export-bc-edition.sh --push` after committing BC knowledge changes. The
export is allowlisted and guarded — it refuses to ship Odoo content or client
data. Recipients pull the update from the distribution repo.

## Git hygiene

- Commit messages: `knowledge: <what changed>`, `client(<slug>): <what>`,
  `expertise: LL-00X <topic>`. Small commits keep the audit trail useful — "why did we
  configure it this way" is answered by `git log` + the SDR.
- The repo may contain client-identifiable information. Keep it **private**, and mind
  your NDA/GDPR obligations if you ever add collaborators or sync to SharePoint —
  intakes should carry only what setup decisions need, not personal data.

## Cost optimization

- Authoring and heavy analysis: do in Claude sessions on this repo (full file access,
  writes SDRs itself).
- Quick lookups in the field: Copilot Studio in Teams (see `copilot-studio/DEPLOYMENT.md`).
- Never pay for both doing the same job — the repo keeps them interchangeable, so you
  can drop either platform at any time without losing the system.
