# Cloning this system to another GitHub account

The whole methodology is **plain files under git** — markdown, stdlib-Python tools,
self-contained HTML, and the `.claude/skills/` that travel with the repo. There is
no database, no server, no build artifact to reproduce, and nothing account-specific
baked in. Cloning it is therefore an ordinary git transfer plus a one-command health
check. A clone needs only **Python 3.8+** to be fully usable.

> ⚠️ These steps run under **your** GitHub credentials on your own machine — the
> assistant cannot push to an account it isn't authorised for. Copy/paste and run
> them yourself.

## Before you clone: privacy check

```bash
python3 tools/doctor.py
```

The last line of the report flags any **real client folder** (anything under
`clients/` that is not `_template` or `_demo-…`). Client intakes and workshop
transcripts are confidential — remove or review them before copying the repo to a
less-controlled account. Recordings are already blocked by `.gitignore`. Today the
repo contains only the fictional demo, so it is safe to clone as-is.

## Path A — copy with full history (recommended)

Keeps every commit. Best when the new account continues the same work.

1. On the target account, create a new **empty** repository (no README/licence), e.g.
   `you/erp-methodology`. Copy its URL.
2. Mirror-push from a bare clone of the source:

```bash
git clone --bare https://github.com/ovm-code/erp.git erp-bare
cd erp-bare
git push --mirror https://github.com/<NEW-ACCOUNT>/<NEW-REPO>.git
cd .. && rm -rf erp-bare
```

3. Clone the new repo normally and verify:

```bash
git clone https://github.com/<NEW-ACCOUNT>/<NEW-REPO>.git
cd <NEW-REPO>
python3 tools/doctor.py      # expect: kloon is gezond
```

**Branches / default.** All current work lives on the branch
`claude/bpa-documentation-system-qzkhgg`. On the new repo, make that the trunk:

```bash
git checkout claude/bpa-documentation-system-qzkhgg
git branch -m main                       # rename to main
git push -u origin main
# then in GitHub → Settings → Branches, set 'main' as the default branch
```

## Path B — fresh start, no history

A clean first commit (drops the development history). Best for a public or handover
copy where the commit trail isn't wanted. Uses only git — no extra tools.

```bash
# clone the branch that holds the current system, then drop its history
git clone --branch claude/bpa-documentation-system-qzkhgg \
  https://github.com/ovm-code/erp.git erp-new
cd erp-new
rm -rf .git
git init -b main && git add -A
git commit -m "ERP setup-assistant methodology — initial import"
git remote add origin https://github.com/<NEW-ACCOUNT>/<NEW-REPO>.git
git push -u origin main
python3 tools/doctor.py
```

## Path C — reusable template (many independent copies)

Do Path A or B once, then in the new repo: **GitHub → Settings → General → check
“Template repository.”** Anyone can then click **“Use this template”** to spin up
their own independent instance — no fork link, clean history. Give each new instance
a `doctor.py` run as its first step (add it to the repo's onboarding note).

## After cloning — make it yours

The system is generic; a new owner personalises a few files. None block usage:

| What | Where | Note |
|---|---|---|
| Model-identity / branch rules | injected by your Claude Code harness, **not** in the repo | nothing to edit here |
| Copilot Studio deployment | `copilot-studio/` | re-deploy per `copilot-studio/DEPLOYMENT.md` under the new tenant |
| Organisation name / branding | `bpa/template/` cover block, viewer accent (`bpa-config.json`) | cosmetic |
| Effort baselines | `pricing/effort-baselines.json` | seeds — recalibrate from your own actuals |
| Industry packs | `bpa/packs/` | keep or clear; add your own verticals |
| Dated report artifacts | `docs/methodology-review-*.html`, `docs/build-out-report-*.html` | history of this instance; keep or delete |

To start an instance **without** the worked demo (bare template only), delete
`clients/_demo-bakkerij-florax/` and the demo-derived pack, then re-run `doctor.py`
(it skips the demo smoke-test and still passes). Keeping the demo is recommended —
it is how a new user learns the pipeline.

## What travels, and what a clone needs

- **Travels in the repo:** all knowledge, templates, tools, the interactive viewer,
  the four skills (`.claude/skills/`), docs, the terminology glossary, the demo.
- **A clone needs:** Python 3.8+ (that's it — the build tools are stdlib-only).
- **Optional, maintainers only:** Node + Playwright to browser-verify the viewer;
  a Claude Code or Copilot Studio environment to run the assistant. Using the built
  deliverables (the HTML files) needs only a browser.

`python3 tools/doctor.py` is the single source of truth for “did the clone come
across intact.” If it ends with **kloon is gezond**, you're ready.
