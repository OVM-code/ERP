# Expertise layer — how it works

The system learns in three stages, all plain files in git:

1. **Record** — every confirmed setup choice becomes a Setup Decision Record (SDR) in
   `clients/<client>/decisions/`, including the options that were rejected and why, and
   which past experience was cited.
2. **Review** — after go-live or a review milestone, the *Outcome & review* section of
   each SDR gets filled in: did the choice hold? The assistant prompts for this; it takes
   minutes per project.
3. **Promote** — patterns confirmed across clients (or single outcomes that disprove a
   default) are distilled into `lessons-learned.md` entries with stable IDs (LL-###).
   Lessons outrank the generic "Default recommendation" lines in the knowledge base.

Why this design:

- **Zero infrastructure** — no database or vector store to pay for or maintain. Search
  works by expertise tags (`#costing`, `#warehouse`, …) present in knowledge files,
  SDRs, and lessons.
- **Auditable** — git history shows when a lesson was added and which decisions it
  changed. A client asking "why did we set it up this way?" gets answered from the SDR.
- **Portable** — any LLM platform that can read files (Claude, Copilot Studio knowledge
  sources) gets the same expertise.

Maintenance cost: ~5 minutes per confirmed decision (the assistant drafts the SDR),
~15 minutes per project review. Nothing else.
