# BPA content — one file per domain

Each file documents one domain of the Cegeka Process Model for this client:
**only the scenarios that are relevant**, enriched with *how* the requirement is met
(standard Business Central, an add-on, a workaround, or a GAP).

## File format — `NN-<domain-slug>.md`

```markdown
# 2. Verkoop

Korte klantspecifieke inleiding op dit domein (optioneel). Verschijnt boven het
procesdiagram in de viewer.

## BS25.202 Verkooporders maken
- **Invulling:** standaard
- **Requirements:** REQ-001, REQ-004

Documentatie voor de klant: hoe dit scenario bij hen zal verlopen. Vertrek van de
templatetekst (bpa/template/domains/02-verkoop.md), maak ze klantspecifiek en
beschrijf de gekozen variant, relevante instellingen en afspraken uit de workshop.

## BS25.900 Advanced pricing
- **Invulling:** add-on: Aptean

…

## BS25.215 Periodieke verkoopfacturen maken
- **Invulling:** gap: GAP-2

Beschrijf de standaard, waarom die niet volstaat, en verwijs naar het GAP-register.
```

## Rules

- Heading per scenario: `## <BS-code> <titel>` — the code must exist in
  `bpa/template/catalog.json` (the build warns otherwise).
- `Invulling` is one of: `standaard` | `add-on: <naam>` | `workaround` | `gap: GAP-x`.
  It drives the colour coding of the BPMN step and the scope matrix.
- Write for the **client**: what will happen in their process, not feature marketing.
- Ground every claim in `knowledge/` (and check `expertise/` before recommending —
  that is step 4 of the advisory workflow).
