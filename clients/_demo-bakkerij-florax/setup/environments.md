# Environments — Bakkerij Florax (demo)

| Environment | Type | Purpose | Company/companies | Owner | Notes |
|---|---|---|---|---|---|
| FLORAX-PROD | production | live vanaf go-live 2027-01 | FLORAX | klant-IT | |
| FLORAX-TEST | sandbox | setup, key-user testen, trainingen | FLORAX | consultant | refresh: vóór elk trainingsblok |
| FLORAX-DEV | sandbox | maatwerk GAP-1/GAP-2 | FLORAX | dev-partner | |

## Conventions

- Setup eerst in FLORAX-TEST, na verificatie herhaald in FLORAX-PROD via
  configuratiepakketten waar mogelijk.
- Trainingen draaien in FLORAX-TEST met de dataset per sessieprep.
- Geen credentials in dit bestand — teampasswordmanager.
