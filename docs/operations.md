# Operations — running this system inside a live ERP project

Failure modes observed/anticipated in real implementations, and how this repo
handles them. Read before the first client engagement.

## Concurrency & change control

- **One branch per client engagement** (`client/<slug>`), merged to main at
  milestones. Two consultants editing the same client on main invites lost work.
- Deliverables are **versioned**: bump `version` in the client config per delivery;
  the build stamps version + date into the HTML. Keep delivered builds committed in
  `output/` so "what did the client see in June" has an answer.
- The scenario **catalog is append-mostly**: when a new template version renames or
  renumbers scenarios, rebuild every active client with `--strict` — dangling codes
  surface as warnings (see `docs/bpa.md` → Updating the template).

## Source material & privacy

- Transcripts contain personal data. Before committing inputs: replace employee
  names with roles (`[Key-user verkoop]`), drop small talk, never commit recordings
  (`.gitignore` blocks common audio/video formats). The repo must stay private.
- Auto-transcripts mishear numbers and product names. Requirements keep the literal
  quote **plus** the interpretation, so a wrong number is traceable to its source.
  Anything decision-critical (volumes, deadlines, amounts) → confirm with the
  consultant, don't trust the transcript.
- One meeting file per meeting, immutable after extraction. New insights → new
  meeting file or an edit to `requirements.md`, never a rewrite of the source.

## Scope & change management

- The BPA states it: **what is not in the document is not in scope.** The coverage
  matrix is the contractual scope record — keep out-of-scope rows with reasons.
- Post-BPA changes are **change requests**: new REQ (source: "CR-mail 2026-08-12"),
  coverage row, content block, possibly FGD — then rebuild and re-version. Never
  silently edit delivered scope.
- SDRs stay the *why* record. BPA/plan/designs say *what*; when a decision is
  revisited the SDR chain shows the history.

## Deliverable logistics

- The HTML is fully self-contained and offline — but mail filters commonly block
  `.html` attachments. Deliver via SharePoint/Teams or zip it.
- It renders in any modern browser (Edge/Chrome/Firefox/Safari); no server, no
  tracking, nothing leaves the file.
- Regenerating needs only Python ≥ 3.8 stdlib — no packages, no network.

## Pipeline integrity (enforced by `tools/check_client.py`)

- Every in-scope scenario documented; every documented scenario in the catalog.
- REQ/GAP references resolve in both directions; no duplicate ids.
- TGD only exists for an FGD whose status is `approved` (human gate).
- Setup plan covers every in-scope scenario (or defers it explicitly).
- Session prep only references scenarios that are in the client's BPA scope.
- Manual sections without a grounded source carry the review flag.
- English deliverables contain no leftover Dutch glossary terms.

Run it in CI or by hand before every delivery; `--strict` builds fail on warnings.
Run with `--log` to persist results to `clients/<slug>/checks.log.jsonl` —
`tools/metrics.py` turns that plus git history into the stage-cycle-time and
validator-failure KPIs.

## Human review coverage

Every methodology component passes through a human review session
(`/review-system <component>`); coverage and verdicts are tracked in
`system/reviews/register.md`. The rule for applied changes: the diff the reviewer
approved is the diff that lands — no bundled extras.

## When reality disagrees with the system

Software behaves differently than knowledge/content claims → trust reality, fix the
knowledge file, stamp `Last reviewed`, log in `system/update-check-log.md`, and
sweep active clients whose deliverables repeat the stale claim (grep the scenario
code across `clients/*/`).
