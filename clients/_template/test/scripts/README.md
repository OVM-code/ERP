# Test scripts — one file per domain (`NN-<domain>.md`)

Scripts are **generated from what already exists** — the BPA scenario documentation
says what "working" means, the FGD acceptance criteria say what the customisations
must do. Writing them by hand from scratch is the old way; the assistant drafts,
the consultant trims, the key user executes.

## Format

```markdown
# 2. Verkoop — testscripts

## TS-2.01 Verkooporder met promoprijs
- **Scenario:** BS25.202, BS25.101
- **Dekt:** (FGD AC's indien van toepassing, bv. FGD-GAP-1 AC-1)
- **Rol/tester:** verkoop binnendienst
- **Startdata:** klant DEMO-RETAIL-A, artikel 10001, promo WK41 actief

| Stap | Actie | Verwacht resultaat |
|---|---|---|
| 1 | Maak verkooporder voor DEMO-RETAIL-A, leverdatum in promoweek | Actieprijs WK41 op de regel |
| 2 | Wijzig leverdatum naar ná de promoweek | Basisprijs op de regel |

### Uitvoeringslog
| Ronde | Datum | Tester | Resultaat | Defect |
|---|---|---|---|---|
| R1 | | | pass / fail | DEF-… |
```

## Rules

- Script-id `TS-<domein>.<nr>`; every **in-scope scenario appears in ≥ 1 script**
  and every **approved-FGD acceptance criterion in exactly ≥ 1 script**
  (`tools/check_client.py` enforces both).
- Expected results come from the BPA text and use the client's real master data —
  a script a key user cannot self-check is not finished.
- A failed step creates a `DEF-x` in `../defects.md`; scope discussions become a
  `CR-x` in `../../aftercare/crs.md`, never a silent scope change.
