# Gap designs — FGD → human review → TGD

Every `GAP-x` in a client's BPA gap register flows through two design stages with a
hard human gate between them. Workspace: `clients/<slug>/gaps/` (templates in
`clients/_template/gaps/`). File names: `FGD-GAP-1.md`, `TGD-GAP-1.md`.

## Pipeline

1. **FGD draft (assistant).** Source: the GAP block in `bpa/gaps.md`, its linked
   REQ blocks (with quotes) and BPA scenario docs, plus `knowledge/` to substantiate
   chapter 2 ("why standard doesn't suffice" — re-verify this against the current
   software version before drafting; the cheapest customisation is one that became
   standard in the last release). Status: `draft`.
2. **Human review (consultant).** Status `draft → in review → approved / rejected`,
   recorded in the review log with date + name. A rejected FGD goes back to step 1
   or kills the GAP (update the BPA gap register either way).
3. **TGD draft (assistant), only from an `approved` FGD.** Self-containment rule:
   an AL developer with no project background must be able to build it — project
   context chapter, glossary, exact events/objects, test plan mapping every FGD
   acceptance criterion. `tools/check_client.py` refuses a TGD whose FGD is not
   approved and warns when acceptance criteria are unmapped.
4. **Developer/architect review** of the TGD, then build. The built app lands in
   setup-plan fase 4.
5. **AL scaffold (optional but default)**: from an `approved` TGD the assistant
   generates `gaps/al/GAP-x/` — app.json, object skeletons with bilingual captions,
   event-subscriber signatures with `// VERIFY:` markers, and a test codeunit per
   TGD test row with `// TODO(TGD §n)` bodies. The architect reviews the scaffold
   diff before development starts (rules: `clients/_template/gaps/al/README.md`);
   the validator refuses a scaffold whose TGD is not approved.

## Statuses (machine-checked, keep these exact tokens)

`draft` → `in review` → `approved` | `rejected` — in the `Status` row of the header
table. The validator parses them; prose variants break the gate.

## Quality bar

- FGD chapter 2 must name the standard alternatives it rejects **and cite** the BPA
  scenario/SDR where they were argued.
- Every FGD acceptance criterion is individually testable; every TGD test maps to
  one.
- TGDs are SaaS-safe by default: extension objects + event subscribers, never base
  app changes; deviations need an explicit argument in chapter 8.
- Amounts, field names and examples use real client data from the requirements —
  invented examples hide misunderstandings.
