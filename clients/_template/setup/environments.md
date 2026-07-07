# Environments — <Client name>

> Register of the client's BC environments. Never write tenant credentials here —
> only names, URLs and ownership. Credentials live in the team's password manager.

| Environment | Type | Purpose | Company/companies | Owner | Notes |
|---|---|---|---|---|---|
| <PROD> | production | live | | | |
| <TEST> | sandbox | key-user testing, training sessions | | | refresh cadence: <…> |
| <DEV> | sandbox | development (gaps), config trials | | | |

## Conventions

- Setup is executed in <TEST> first, verified, then repeated/promoted to <PROD>
  (configuration packages / manual, per step in the setup plan).
- Training sessions run in <TEST> with the dataset described per session in
  `../training/sessions/`.
- After every sandbox refresh from PROD: re-check the "Afhankelijk van" state of
  in-progress setup-plan steps.
