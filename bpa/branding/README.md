# Cegeka branding assets

Visual identity for every client-facing deliverable (BPA, user manual, PDF
export). Extracted from the official **Cegeka PowerPoint template** (PDF export
of the example slides, received June 2026) — nothing here is guessed.

| File | What it is | Used by |
|---|---|---|
| `tokens.css` | Design tokens (colours) as CSS custom properties, sampled from the template's vector artwork | inlined before `bpa/viewer/viewer.css` at build time |
| `cegeka-logo-dark.png` | Full-colour logo + dark wordmark, white background — for white surfaces (viewer header, PDF cover) | injected as data-URI (`--cg-logo-dark`) |
| `cegeka-logo-white.png` | White wordmark, transparent background — for cyan/dark surfaces (print footer band) | injected as data-URI (`--cg-logo-white`) |

## Palette (sampled values)

| Token | Hex | Template role |
|---|---|---|
| Cegeka cyan | `#00C7F9` | primary brand colour: full-bleed slides, highlights, numbered accents |
| Light cyan | `#80E3FC` | secondary fills (outlined number chips) |
| Ink | `#001D24` | all text |
| Purple | `#632064` | accent (logo swoosh, date pill) |
| Coral | `#F04B4C` | accent (logo swoosh, action arrow) |
| Gray / light gray | `#B1B1B1` / `#D9D9D9` | muted text, dividers |

Derived (not in the template, computed for accessibility): `--cg-cyan-deep`
`#0079A1` for links/text on white where `#00C7F9` has too little contrast, and
the `*-tint` backgrounds.

## How it flows into deliverables

`tools/build_bpa.py` (and `tools/build_manual.py`, which reuses it) concatenate
`tokens.css` + a generated `:root { --cg-logo-… }` block + `bpa/viewer/viewer.css`
into the single self-contained HTML file. No build step ever references these
files at view time — deliverables stay fully offline.

To rebrand (new corporate style, another consultancy): replace the two PNGs and
the token values here, rebuild — nothing else in the system references colours
directly.
