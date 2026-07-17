# Folder Guide — for humans browsing in Finder

**Your workflow in three colors:**

| Phase | Where | What you do |
|-------|-------|-------------|
| **RED — Read & think** | Project root (`red` tag) | Read docs, understand intention, plan before touching images |
| **GREEN — Go** | `green/` | Interviews, references, character, prompts — light is green, start creating |
| **OUTPUT** | `video exports/` | Finished images, then videos |

---

## RED — Read before you do

Stay at the root. Don't open exports until green is ready.

| File | Purpose |
|------|---------|
| [README.md](README.md) | Rules — read first every session |
| [ROADMAP.md](ROADMAP.md) | Future/near-future milestones (not today's work) |
| [TEMPLATE.md](TEMPLATE.md) | Reuse for other candidatures |
| [storyboard.html](storyboard.html) | Visual shot list — double-click |
| [conversation.md](conversation.md) | Chat history — internal, do not publish |

**Rule:** If you're still thinking, stay in RED. Open `green/` only when you're ready to act.

---

## GREEN — References & creation data

Everything you need to **do** the images lives here. Interviews distilled, references cited, character locked, prompts written.

| File / folder | Purpose |
|---------------|---------|
| [research-intention-summary.json](green/research-intention-summary.json) | **WHY** — interview meaning, version logic |
| [character-bible.json](green/character-bible.json) | **WHO** — MADAME_X, costume per shot |
| [references/shot-references.json](green/references/shot-references.json) | Literal URLs justifying each frame |
| [shots/](green/shots/) | Per-shot prompts → maps to images |
| [INDEX.md](green/INDEX.md) | Quick legend for all JSON files |

**Agent-only** (ignore unless debugging): `agent-tasks.json`, `token-budget.json`, `grok-adaptation-guide.json`, `roadmap.json`

**Rule:** Green = go. When references and intention are clear, generate into `video exports/`.

---

## OUTPUT — Images, then videos

### `video exports/001/` — one complete ad

| File | Human meaning |
|------|---------------|
| [INDEX.md](video%20exports/001/INDEX.md) | Shot list with titles — **open this first** |
| [contact-sheet.html](video%20exports/001/contact-sheet.html) | All thumbnails in one grid |
| `00-character-reference.jpg` | MADAME_X — identity lock |
| `shot-01.jpg` … `shot-10.jpg` | Frames in story order (filenames are numbers only — see INDEX for titles) |
| `video/` | Future mp4 clips and animatic |
| `manifest.json` | Machine status log |

### Empty versions

- `002/` — The Clinic (not started) — see INDEX inside
- `003/` — The Absence (not started) — see INDEX inside

---

## Quick decision tree

```
Am I still reading / thinking?
  → YES: stay at root (RED) — README, storyboard, FOLDER_GUIDE
  → NO: open green/ — check intention + references + character
        → Ready to render? → video exports/001/
        → Ready for motion? → video exports/001/video/ (grok-build)
```

---

## Finder tip

The folder has a **red tag** in Finder — that's your "stop and think" signal at the root. `green/` has no special tag: it's the workspace once you're ready to create.