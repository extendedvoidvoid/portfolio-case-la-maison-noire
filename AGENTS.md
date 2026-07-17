# AGENTS.md — La Maison Noire / fragrance film candidature

Read this **before** any edit, regen, or push.  
Human owns install to production and any public publish.

---

## What this project is

Private **spec fragrance film** + research pack for a **concepteur-rédacteur** candidature (Parfums Beauté / films & images).  
**Not** an official brand campaign. **Not** for public/commercial use of third-party likeness without rights.

Related apply folder (CV/lettre): `~/projects/chanel-apply/` (do not mix tech CV into creative docs).

---

## Canonical files (read order)

| Priority | Path | Role |
|----------|------|------|
| 1 | `research/SCRIPT_AD_VALIDATED.md` | **Locked script direction** (text) |
| 1b | `research/REF_madonna_massive_attack_i_want_you.md` | Cine/narration grammar (waiting → refusal) |
| 2 | `research/NEW_CONCEPTS_lilyrose_newton.md` | Concept menu A–E |
| 3 | `data/concepts-all-five.json` | Machine prompts for A–E |
| 4 | `research/newton-ideology-critical.md` | Newton = ideology, not prop zoo |
| 5 | `research/helleu-simplicity.md` | Ending: scent before name, black |
| 6 | `research/da-2016-chanel-parfums-beaute.md` | Who owns fragrance image DA |
| 7 | `research/dual-reference-protocol.md` | Face vs aesthetic refs |
| 8 | `data/narrative-progression.json` | Older MADAME_X spine (superseded for new film by script) |

**Storyboard HTML / production stills:** `index.html`, `assets/shots/001/` — do not overwrite without human **install** command.  
**Current production board (installed):** *Tu me connais* / I Want You mise — see `assets/shots/001/INDEX.md` + `_staging_i_want_you_mise/`.

---

## Hard rules (non-negotiable)

### Film content
1. **No house brand name** in script, supers, dialogue, storyboard labels, or on-bottle type in frames meant for portfolio.  
   **Hard visual ban on every bottle prompt:** no logo, no monogram, no readable label text, no brand geometry on glass.
2. **No VO** explaining the woman; almost silence + sparse piano + one spray.
3. **Bottle = discreet:** personal/travel scale (~hand-held), max **2 short beats**, first appear **not before beat 4**, unlabeled blank glass, never giant hero packshot.
4. **No on-the-nose pastiche:** no Dobermans, no clinic syringe as hero, no checkerboard “Amazon entrance,” no gilt-mirror monstrance.
5. **Newton = ideology:** complicit gaze, documented not performing, ambivalence — **not** a prop checklist.
6. **Paradox** (known / unknown) is structural only — **no slogan text on screen**.

### Identity / legal
7. **Face lock (current direction):** `assets/refs/aesthetic_leau_2016_APPROVED.jpg` when user wants that character.  
   **Legacy plate:** `assets/shots/001/00-character-reference.jpg` (MADAME_X) — archive unless human says otherwise.
8. Celebrity likeness = **private interview research / staging only** unless human clears rights for public Pages.
9. Always frame as **spec / concept personnel / étude**.

### Git / deploy
10. **No push** to GitHub / Pages unless human explicitly asks.
11. **Staging only** for new renders until human says `install …`.

---

## Staging layout

| Path | Purpose |
|------|---------|
| `_staging_concepts_all/` | Concepts A–E boards + key renders + `INDEX_CONTACT.html` |
| `_staging/` | Earlier dual-ref MADAME_X pipeline (legacy) |
| `assets/shots/001/_staging_pending_approval/` | Older shot candidates |
| `assets/refs/` | Approved aesthetic / research stills |
| `assets/shots/001/` | **Production** stills — human install only |
| `assets/shots/001/_backup_pre_regen_*` | Backups — never delete without ask |

**Install pattern (only when human says so):**  
copy from staging → `assets/shots/001/shot-XX.jpg` (backup first).

---

## Script spine (v1 — see SCRIPT_AD_VALIDATED.md)

Working title: **Tu me connais** · ~70s · 16:9 · B&W  

| Beat | Content | Bottle |
|------|---------|--------|
| 01 | Almost known — looks past lens | no |
| 02 | Double reflection | no |
| 03 | Frame watches — partial frame | no |
| 04 | Private spray — small flacon | **yes, discreet** |
| 05 | Eyes to lens — long hold | no |
| 06 | Lace / breath macro | no |
| 07 | Night window | no |
| 08 | Small crystal + light only | **yes, discreet** |
| 09 | Empty afterimage | no |
| 10 | Pure black — no card | no |

---

## Image generation rules

1. Prefer `image_edit` from face lock; do not free-`image_gen` a new face mid-sequence.
2. Dual-ref if needed: **[face plate, light plate]** — face only from image 1.
3. Max ~3 parallel gens; write to **staging**, not production.
4. Shot 10 black = code/solid black, not a model call.
5. After gen: open staging folder; wait for human red-tag or `install` / `reject` / `retry`.

---

## Interview talking points (agent may remind; human speaks)

1. **Gaze / power** without costume cliché (Newton ideology).  
2. **Simplicity:** film ends before the name (Helleu).  
3. **Parfums image system:** house creative resources for fragrance & beauty vs film director execution (research notes) — speak carefully; no false claims of employment.  
4. **360:** 9:16 crop of gaze + gesture; print without bottle or bottle tiny; CRM line without house name.

---

## Do not

- Mix software-engineer CV into this creative case.  
- Auto-submit France Travail / any candidature.  
- “Improve” the script by adding brand, dogs, giant bottle, or VO.  
- Force-push or rewrite history without ask.  
- Treat staging as production.

---

## Default next steps (if human is vague)

1. Confirm script text still OK.  
2. Storyboard frames **from SCRIPT_AD_VALIDATED.md** + *I Want You* mise grammar → `_staging_i_want_you_mise/` (current).  
3. Human approves → install selected frames only.  
4. Optional: rebuild animatic after install.

---

## One-line agent summary

**Spec film script locked: no brand name, discreet bottle, Newton gaze + known/unknown paradox, staging-only renders, human install gate.**
