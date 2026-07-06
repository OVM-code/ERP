# Running this system in Microsoft Copilot Studio

The repo is the single source of truth; Copilot Studio is a *deployment target*. You
maintain everything here (or in any Claude session on this repo), and sync content to
the Copilot Studio agent. Expect ~30 minutes for first setup, minutes for updates.

## One-time setup

1. **Get the content somewhere Copilot Studio can read.** Two options:
   - **Recommended — SharePoint:** create a SharePoint document library (e.g.
     `ERP-Assistant`) and copy the repo folders `knowledge/`, `clients/`, `expertise/`
     into it. Keep the folder structure. If you sync the library with OneDrive on your
     PC, updating the agent's knowledge becomes "copy files, done".
   - **Alternative — file upload:** upload the same files directly as *Files* knowledge
     in the agent. Simpler, but every update means re-uploading changed files by hand.
   - Note: if `.md` files are rejected by your tenant's upload/indexing settings, batch-rename
     them to `.txt` before uploading — the content works identically for retrieval.
2. **Create the agent** at [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com):
   *Create → New agent* (skip the conversational builder, use *Configure* directly).
   - Name: e.g. `ERP Setup Advisor`.
   - Instructions: paste the block from [`agent-instructions.md`](agent-instructions.md).
   - Ensure **generative orchestration / generative answers** is enabled so the agent
     actually searches the knowledge sources.
3. **Add knowledge sources:** *Knowledge → Add* → your SharePoint library (or uploaded
   files). Add ALL of: `knowledge/`, `clients/`, `expertise/`. Without the clients and
   expertise folders the agent loses its memory layer.
4. **Test in the built-in test pane** with a real question, e.g. *"Client X, food
   distributor with Aptean lot management — what are my options for warehouse
   complexity level and what do you recommend?"* Check that it cites knowledge files
   and lessons.
5. **Publish** to the channels you want (Teams is the usual one: *Channels →
   Microsoft Teams → Publish*).

## Keeping it in sync (the maintenance loop)

| What changed | What to do |
|---|---|
| Knowledge file edited (new software release, correction) | Copy the changed file(s) to SharePoint / re-upload. Indexing takes a few minutes. |
| New SDR or intake created during a Copilot Studio chat | The agent outputs it as a copy-paste block → save it in the repo (`clients/<client>/decisions/`) → commit → copy to SharePoint. |
| New lesson learned | Same: save in `expertise/lessons-learned.md`, commit, copy to SharePoint. |
| `system/instructions.md` changed | Regenerate `copilot-studio/agent-instructions.md` (condensed, ≤8,000 chars) and re-paste into the agent's Instructions field. |

Git remains the audit trail: commit every change here first, then sync outward.

## Known limitations vs. running on Claude

- Copilot Studio **cannot write files** — decision records come back as copy-paste
  blocks you save yourself. On Claude (Code/desktop with this repo), the assistant
  writes SDRs, intakes and lessons directly.
- Retrieval is chunk-based: the agent sees relevant fragments, not whole files. The
  knowledge files are written with self-contained decision blocks so this works, but
  very long cross-file reasoning is stronger on Claude.
- Instructions are capped (8,000 chars) — hence the condensed copy.

## Cost note

Copilot Studio licensing (per-message packs or Microsoft 365 Copilot seats) is the only
running cost; the knowledge layer itself is free files. If cost matters, keep heavy
authoring/maintenance work in Claude or any editor, and use Copilot Studio only for
quick advisory lookups in Teams.
