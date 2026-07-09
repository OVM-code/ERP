# REV-001 — Template challenge: EDI framework classified as standard BC

- **Component:** `bpa/template/domains/12-interfaces.md` (scenario `BS95.002` + sub-scenarios `BC95.002.01–03`)
- **Raised by:** catalog refresh 2026-07 (`/catalog-refresh`, see `bpa/catalog/refresh-log.md`)
- **Status:** OPEN — awaiting human review (`/review-system bpa/template`)
- **Reviewer:** —
- **Verdict:** —

## Finding

The template documents `BS95.002 EDI framework` (inbound/outbound EDI messages,
"vergaande functionaliteiten") under domain 12 without an add-on flag, implying
it is achievable in standard Business Central. The 2026-07 catalog verification
could not confirm this against official sources:

- Standard BC covers **e-documents/Peppol** (send/receive electronic invoices
  and credit memos — [Use e-documents in the purchase process](https://learn.microsoft.com/dynamics365/business-central/finance-how-use-edocuments-purchase))
  and **REST APIs** for integration.
- A **generic EDI framework** (arbitrary message types, trading-partner
  mappings, EDIFACT/X12 handling) is **not** standard BC functionality — it is
  typically delivered by an ISV connector or, in the Cegeka practice, the
  Cegeka 365 layer / custom interfaces.

The demo client uses BS95.002 for webshop/EDI order intake, which in that BPA is
correctly documented as an interface implementation — supporting the reading
that BS95.002 is *delivery work*, not standard product capability.

## Proposed template edit (draft — do NOT apply without reviewer approval)

In `bpa/template/domains/12-interfaces.md`, under the `BS95.002` heading, add a
classification note:

> **Invulling-richtlijn:** het EDI-framework is geen standaard
> Business Central-functionaliteit. Standaard BC dekt e-documents (Peppol,
> e-facturatie) en API's. Klassieke EDI-berichtstromen (orders, pakbonnen,
> facturen per retailer-mapping) worden ingevuld als `add-on: Cegeka 365` of
> als interface-maatwerk (GAP) — nooit als `standaard`.

And in `bpa/template/catalog.json` (via the split-tool source), consider setting
`addon: "cegeka-365"` for `BS95.002` and its sub-scenarios so the viewer colours
them correctly by default.

## Decision needed from reviewer

1. Is the Cegeka EDI framework part of the Cegeka 365 product (→ add-on flag) or
   project maatwerk (→ GAP guidance)?
2. Should the template text change, or only the catalog metadata?
