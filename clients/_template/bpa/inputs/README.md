# Meeting inputs

Drop the raw material from requirement meetings here. The assistant works from
whatever is available — a full transcript, rough notes, or both.

## Conventions

- **One file per meeting**, named `YYYY-MM-DD-<topic>-<type>.md` (or `.txt`), e.g.
  `2026-05-12-verkoop-transcript.md`, `2026-05-12-verkoop-notes.md`.
- **Text only.** Recordings must be transcribed first (Teams transcription, Copilot,
  Whisper, …) — audio/video files are git-ignored and cannot be processed here.
- Start each file with a small header block: date, attendees (roles suffice),
  domain(s) discussed, transcript quality (verbatim / auto-generated / summary).
- Keep the originals unedited — corrections and interpretations belong in
  `requirements.md`, not in the source material.

## Traceability

Every requirement extracted into `requirements.md` cites its source as
`<filename> §<section/timestamp>`. Number transcript paragraphs (§1, §2, …) or keep
timestamps so the citation stays checkable.
