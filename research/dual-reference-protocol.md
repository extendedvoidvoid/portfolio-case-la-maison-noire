# Dual reference protocol

## Gap (fixed as process)

Regens must **not** use only MADAME_X.  
2016 Parfums Beauté DA needs a **second visual plate** for light / makeup / bottle refraction.

## Two plates

| # | Plate | Role | Never |
|---|--------|------|--------|
| 1 | `00-character-reference.jpg` (MADAME_X) | Face, body, chignon, pearls, curves | — |
| 2 | L’Eau 2016 **aesthetic** plate | Luminosity, makeup finish, rim light, photo-shoot appetite, crystal light | **Face of Lily-Rose or any celebrity** |

## 2016 L’Eau people (web)

| Role | Person |
|------|--------|
| House Parfums Beauté image | **Thomas du Pré de Saint Maur** |
| Campaign **stills** | **Karim Sadli** (Aug 2016) |
| Campaign **film** | **Johan Renck** |
| Campaign face | Lily-Rose Depp — **codes only, no likeness** |

## image_edit rule

```
images = [character_MADAME_X, aesthetic_leau_2016]
prompt = Face and body ONLY from image 1.
         Light, skin luminosity, makeup finish, bottle refraction from image 2.
         Do not copy face, hair, or age from image 2.
```

## Status

**Aesthetic plate APPROVED** (user pick 2026-07-17 — Image #1):

- `assets/refs/aesthetic_leau_2016_APPROVED.jpg`  
  ← color L’Eau campaign still: luminous makeup, bottle hero, lace, soft grey ground  
  Codes only for dual-ref light/makeup/bottle — **not** MADAME_X face

Character plate unchanged: `assets/shots/001/00-character-reference.jpg`

Shot frames not modified until dual-ref regen + your install approval.
