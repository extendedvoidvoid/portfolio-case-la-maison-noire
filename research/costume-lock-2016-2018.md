# Costume + makeup lock — 2016–2018 house codes

**Blocks** wardrobe and makeup for MADAME_X continuity.  
**Images not regenerated yet** — this locks **future** edits and prompt language.

Full DA / people: [da-2016-chanel-parfums-beaute.md](da-2016-chanel-parfums-beaute.md)

---

## Makeup (Parfums Beauté 2016 DA)

| Zone | Lock |
|------|------|
| Skin | Luminous, fresh, dewy porcelain — “L’Eau” radiance under hard fashion light |
| Eyes | Soft definition; clean; optional soft smoke only if still luminous |
| Lips | Full, defined cupid’s bow; natural deep / dark fashion (bible already) |
| Brows | Strong, natural arch |
| Continuity | **Same makeup recipe** on every shot where face is visible (01, 02, 04, 05, 07, 08 edge) |

**Ban:** matte full glam, teen soft-focus beauty, Lily-Rose face/hair copy.

---

## Clothes (2016–18 Chanel house codes)

Late-Karl era still owns the house codes in 2016–18:

| Piece | Lock |
|-------|------|
| Jacket / skirt | B&W houndstooth or classic tweed tailleur, structured shoulders |
| Trim | White piping acceptable |
| Jewelry | Triple-strand pearls when neck visible |
| Shoes | Black pumps |
| Gloves | Fingerless black lace (ritual shots) |
| Sunglasses | Black, armor — remove only in shot 05 |

**Wardrobe states** (from bible) stay A–F but all are **variations of this one 2016–18 set**, not other decades.

**Ban:** logo streetwear, sneakers as default, pure 80s fetish brace/saddle as costume.

---

## Prompt injection (append to face shots)

```
Makeup: luminous fresh porcelain skin, soft eye definition, strong natural brows,
defined lips — 2016 Parfums Beauté light radiance, not matte Instagram glam.
Wardrobe: structured black-and-white tweed tailleur, triple pearls, black pumps —
2016–2018 house codes, same woman same makeup throughout.
```

---

## Consistency pipeline

1. `00-character-reference.jpg` = face + body + **full A outfit + makeup lock**  
2. All regen = `image_edit` from that plate  
3. Never invent new lipstick color or haircut mid-sequence  
