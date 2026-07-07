# Aftercare system — from reactive support to a product

**Today** aftercare is consultants resolving issues and pushing change requests
through — reactive, time-and-material, and invisible until the invoice. The
proposal: keep that work (it is real), structure it so it compounds, and layer a
productised offering on the assets every project already produces. Workspace:
`clients/<slug>/aftercare/`.

## Layer 1 — structure what already happens (build now)

- **`issues.md`**: every ticket logged with its scenario/manual reference, type and
  resolution. Two effects: the *feeding rule* (a resolved issue must either update
  the manual, propose a lesson learned, or flag a test-script gap — recurring
  user-error issues are documentation debt, not user stupidity), and a defensible
  record of what support actually costs per client.
- **`crs.md`**: the CR pipeline — request with literal quote → agent drafts the
  delta (REQ, coverage, content, FGD if needed) → estimate from effort baselines →
  client approves → delivered with a **BPA version bump**. The deliverables stay
  the single source of truth after go-live instead of drifting from reality; and
  CRs get billed because quoting them costs minutes, not an afternoon.

## Layer 2 — proactive, from existing assets (pilot next)

- **Release-wave impact report** (2×/year, per client): diff the Microsoft release
  plan against the client's in-scope scenario codes + add-on stack; deliver "what
  changes for *you*, what to test, what new standard feature could replace GAP-x".
  Grounded, client-specific, largely generatable — and it lands twice a year as
  proof the partner is paying attention.
- **Doc-grounded Q&A**: the client's own BPA + manual + setup record as the
  knowledge base for a support agent (Copilot Studio deployment kit already
  exists in this repo). First-line questions get cited answers from *their*
  documentation; what the agent cannot answer becomes an ISS with context attached.
  Deflects the cheap tickets, keeps the consultant for the real ones.

## Layer 3 — commercial packaging (after two pilots)

Subscription tiers instead of pure T&M: **Basis** (registers, SLA on issues, CR
fast-quoting) · **Plus** (+ wave impact reports + quarterly value review: open
review-flags, unused in-scope features, KPI's from their own metrics) · **Premium**
(+ Q&A agent + priority CR lane). T&M remains for delivery of approved CRs — the
subscription buys responsiveness and foresight, not unlimited work.

## Validator rules (`tools/check_client.py`)

- CR statuses use the exact tokens; a `delivered` CR must name a BPA version.
- A resolved ISS must reference a scenario/manual topic or state `n.v.t.` — the
  feeding rule is checked, not hoped for.

## Why clients pay for this

They stop buying "hours when something breaks" and start buying **certainty**: a
documented environment that stays current with reality, twice-yearly foresight on
Microsoft's changes, answers grounded in their own processes, and change requests
that are priced the day they are asked. That is a renewal conversation, not a
procurement fight.
