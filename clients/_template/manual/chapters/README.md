# Manual chapters — one file per chapter

Same interactive format as the BPA (clickable BPMN flows), but the content is
**how-to for end users** after the training sessions. Chapter numbers that match a
BPA domain number automatically reuse that domain's process flow, so users click the
same diagram they saw in training.

## File format — `NN-<slug>.md`

```markdown
# 2. Verkoop

Korte inleiding voor de eindgebruiker (optioneel).

## BS25.202 Een verkooporder ingeven
- **Bron:** bpa
- **Rol:** verkoop binnendienst

1. Kies **Verkooporders** > **Nieuw**.
2. …stap voor stap, in de taal en volgorde van de gebruiker…

## BS25.328 Leverdatum controleren
- **Bron:** docs: https://learn.microsoft.com/… (BC24)
- **Rol:** verkoop binnendienst

…

## MAN-001 Aanmelden en navigeren
- **Bron:** review
- **Rol:** iedereen

…concepttekst die een consultant nog moet nakijken…
```

## Rules

- **Topic code**: a BS/BC scenario code when the topic explains a BPA process step
  (that makes it clickable in the flow), or `MAN-xxx` for general topics.
- **Bron (source) is mandatory** and drives the colour + review register:
  - `bpa` — grounded in the client's BPA content (blue);
  - `docs: <url> (<BC version>)` — grounded in official documentation; the link and
    version are required and shown to the user (purple);
  - `review` — could not be grounded in either: **auto-flagged for consultant
    review** (red, listed in the "Te reviewen" tab). Better an honest flag than a
    confident invention.
- Write steps against the client's **actual configuration** (names of their
  locations, number series, roles) — the BPA and setup plan tell you what those are.
- Version-check the `docs:` links against the client's stack before delivery.
