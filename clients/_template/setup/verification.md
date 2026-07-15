# Environment verification — trust, then verify

> Configuration drift is found here, not in a training session. Before every
> training block and before cutover, the environment is verified against the setup
> plan: each `done` step gets a concrete, checkable probe. The assistant generates
> the probes from the plan; execution is a read-only API/page pass (never writes).

| | |
|---|---|
| Environment verified | <TEST/PROD> |
| Against setup plan version | |
| Trigger | vóór trainingsblok <x> / vóór cutover |

## Probes

> One row per setup-plan step with status `done`. Method: BC API endpoint (read-only)
> waar mogelijk, anders pagina-controle. Resultaat: `ok` / `afwijking` (+ actie).

| Planstap | Probe | Methode | Verwacht | Resultaat | Actie bij afwijking |
|---|---|---|---|---|---|
| 2.2 | Traceringscode op alle traceerplichtige artikelen | API `items` + filter categorie | 0 traceerplichtige artikelen met code GEEN | | |
| 3.1 | Verzendadvies per klantgroep | API `customers` | retail = volledig; overige = deellevering | | |

## Drift log

| Datum | Omgeving | Afwijkingen | Oorzaak | Opgelost |
|---|---|---|---|---|

> Automation path (H2): a read-only verifier agent runs these probes via the BC API
> (`/api/v2.0/companies(...)/...`) on schedule and writes the drift log — the probe
> table above is written to be machine-executable from day one.
