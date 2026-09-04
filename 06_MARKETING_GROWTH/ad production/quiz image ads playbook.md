# QUIZ IMAGE ADS — Ad Production Playbook

How the 5-ad Owen funnel image batch was built end-to-end: concept process, photo generation, brand compositing, and the mistakes we hit so the next batch doesn't repeat them. Companion to `quiz voice over ads playbook.md` (video). Use both as templates for the next Odin Lab ad batch.

---

## 1. Tech stack

- **nanobanana MCP** (`generate_image`) — photorealistic base photos from text prompts
- **Python + Pillow** in a scratch venv — ALL typography composited programmatically, never AI-rendered
- **cairosvg** — renders the brand SVG logo to PNG at any size (white + lime variants)
- Output: 1080×1080 PNG, named `quiz - [concept] - image ad.png`, saved to
  `Calgary-Local/marketing/Odin Labs Calgary Meta Ads/` (moved here in the 2026-09-04 vault reorg)

**Why split photo/text this way:** AI-rendered text is the #1 giveaway of AI-generated ads (warped glyphs, fake kerning). Photoreal base from the model + crisp vector text from Pillow = passes as a designed ad. Never prompt the image model to render headlines.

---

## 2. Concepts before pixels (do this first, every time)

Concepts come from the Copy OS diagnosis, not from brainstorming visuals:

1. **State check:** Owen funnel audience = Schwartz State 4 (problem-aware) at high market sophistication. Ads must lead with the problem in the prospect's own words, or a new mechanism — never bigger claims.
2. **Message-match to the quiz:** the strongest concepts are literal quiz answer options turned into images. "3pm crash" = quiz Q3 option 1. "Normal range, no answers" = quiz Q9 option 3. The prospect sees the ad, clicks, then *selects the same sentence in the quiz* 60 seconds later.
3. **Andromeda diversity:** every concept in a batch must differ on BOTH axes — emotion (recognition / validation / nostalgia / curiosity / frustration) and visual format (portrait / macro object / cinematic scene / typographic / environmental). Near-identical creatives get clustered and delivery-suppressed.
4. **Get concept approval before designing.** Present concept + text/visual split, wait for sign-off.

The 5-concept batch shipped July 2026:

| Concept | Image | Text on image | Emotion |
|---|---|---|---|
| 3pm wall | Fit professional at desk, pinching nose | "You used to own 3pm." | Recognition |
| Normal range | Bloodwork close-up, circled value | ""Normal." Still exhausted." | Validation |
| You remember | Man on bed edge, dawn | SHARP. STRONG. RECOVERED. | Nostalgia |
| The pattern | Shadowed torso, dark | 01 Stress / 02 Hormones / 03 Metabolism | Curiosity |
| Doctor's note | Man in waiting room | "Everything looks normal." | Frustration |

**Rejected angles and why:** before/after body imagery (Meta health policy risk), testimonials (no real assets — never fabricate), discount ads (wrong State, poisons cash-pay positioning), generic "low energy?" (Stage-1 claim in a Stage-5 market).

---

## 3. Photo generation prompts — the anti-AI-look recipe

Every prompt includes, explicitly:

- **A camera + lens:** "shot on Canon 5D Mark IV 50mm f/1.8", "35mm f/2", "100mm macro f/2.8"
- **"Candid documentary photograph"** or "cinematic photograph" — never "photo of"
- **Imperfections by name:** real skin texture with pores, natural film grain, slight lens vignette, wrinkled fabric, crumpled paper
- **Mood sentence:** what the person feels ("a high performer whose body is failing him, not a defeated man")
- **Grade instruction:** "muted desaturated color grade with deep green shadow tones" — pre-biases toward the brand tint
- **Layout reservation:** "Square 1:1 composition with empty negative space in the upper third for text"
- **Negations:** "No text, no watermark, no signage"

### Subject casting — the mistake we made twice

First-pass subjects for "3pm wall" (balding, defeated office worker) and "doctor's note" (rough, blue-collar man in dirty work jacket) were rejected as **not relatable**. The avatar is a *fit, successful professional 35–52 hitting a wall* — the ad must show who he believes he is, not who he fears becoming.

Casting spec that works: **"fit, well-groomed professional man in his early 40s — full head of hair, strong jawline, athletic build, quality fitted shirt, expensive watch."** Environment matters equally: modern office with standing desk + MacBook, clean modern clinic — not beige cubicles and plastic chairs.

### Known generation defects to check for

- **Blank bands:** model sometimes leaves a flat white strip at a frame edge (happened on the 3pm reshoot). Fix by cropping the content region, rescaling, and center-cropping back to square — bias the crop window to keep the subject.
- **Film borders:** "shot on 35mm"-style prompts can produce black film-frame borders. Trim ~3.5% per side before compositing.
- **Gibberish text inside the photo** (lab reports, screens): mostly fine when out of focus, but verify the ONE readable element is correct (our bloodwork ad's circled "TESTOSTERONE, TOTAL — 345 ng/dL (250–1100)" reads correctly; surrounding blur-text is gibberish). Don't use such images in tap-to-zoom placements without checking.

---

## 4. Brand system (extracted from odinhealthlab.ca — see video playbook §2)

| Token | Value |
|---|---|
| Background green | `#1a3a1a` |
| Accent lime | `#c4ff49` |
| Near-black panel | `#0e2410` |
| Headline font | Helvetica Neue Bold (index 1 in `/System/Library/Fonts/HelveticaNeue.ttc`) — closest installed match to the site's weight-900 system sans |
| Punch stacks / numbers | Helvetica Neue Condensed Black (index 9) |
| Labels | Helvetica Neue Medium (index 10) |

**Logo:** ALWAYS the real SVG (`06_MARKETING_GROWTH/odinlablogo.svg+xml`, viewBox 0 0 640 175), rendered via cairosvg to white and lime PNGs. Never a text wordmark. User rule, non-negotiable.

### Photo brand tint (adapted from video b-roll recipe)

Gentler than the video version — photos are the hero here, not a background:

```python
base = ImageEnhance.Color(img).enhance(0.68)        # desaturate
base = ImageEnhance.Brightness(base).enhance(0.88)  # darken
base = ImageEnhance.Contrast(base).enhance(1.05)
mult = ImageChops.multiply(base, Image.new("RGB", size, (120,160,120)))  # green multiply
out  = Image.blend(base, mult, wash)                # wash 0.22–0.32 per image
```

Then gradient scrims (deep green `(10,26,12)`, band = 42% of height, alpha falloff `(1-y/band)^1.5`) top and/or bottom wherever text sits. Photos already graded dark need less wash (0.22); bright office shots need more (0.32).

### Layout system

- `PAD = 72` px — one constant for every margin
- **Headline top-left** (or top-right stack), white, 72–80 px, with soft dark drop shadow (offset +2/+3, blur 6, then sharp text on top)
- **Footer band owns the bottom** (mirrors the video ad's Footer component):
  lime divider bar (130×5 px) → CTA line with vector arrow at left → white logo (190 px wide) bottom-right
- **≤ 3 text elements per ad** (headline, optional sub-line, CTA). Text-to-image ratio target ~10%, except deliberate typographic concepts (the pattern ≈ 20%, acceptable because text IS the visual)

### The arrow bug (will bite again)

Helvetica Neue has **no `→` glyph** — it renders as a tofu box. Draw arrows as vectors: shaft line + chevron head, stroke `size*0.11`, same drop-shadow treatment as text. The compositor's `cta_with_arrow()` handles "text → text" and trailing-arrow cases.

Also: PIL has no letter-tracking — draw labels char-by-char if letterspacing is needed.

---

## 5. Verification workflow

1. Render base photos → **Read every image** before compositing. Check: subject relatable? negative space where planned? generation defects (§3)?
2. Composite → **Read every final ad at full size.** Check: tofu glyphs, text collisions, scrim contrast, logo legibility, CTA arrow.
3. Fix in the script, re-run, re-read. Never ship on code review alone — every bug caught in this batch (tofu arrows, white band, film border) was caught by looking at rendered output.

---

## 6. Meta copy pairing (GOATED adapted for image+text)

Image = **G**rab. Primary text carries Outcome → mechanism tease → CTA:

- First line must survive ~125-char "See more" truncation AND continue the image's thought — never repeat the image headline verbatim
- Headline field < 40 chars; CTA button: Learn More (standardize — mixed CTAs shipped once by accident)
- No fabricated stats/testimonials; credibility via specificity until real proof assets exist
- `utm_content` per concept slug (`3pm-wall`, `normal-range`, …) so Mixpanel sessions map to concepts

---

## 7. Reusable checklist for the next batch

- [ ] Concepts from State/sophistication diagnosis + quiz message-match, approved before design
- [ ] Every concept distinct on emotion AND visual format (Andromeda)
- [ ] Prompts: camera/lens, documentary style, named imperfections, mood sentence, green-grade bias, negative-space reservation, no-text negation
- [ ] Subjects cast as the avatar's self-image: fit professional, quality wardrobe, modern environment
- [ ] Base photos reviewed before compositing (blank bands, film borders, gibberish text, relatability)
- [ ] All text composited in Pillow — zero AI-rendered typography
- [ ] Real SVG logo (white/lime), never a wordmark
- [ ] Brand tint recipe + scrims on every photo; wash tuned per image brightness
- [ ] Arrows drawn as vectors (no `→` glyph in Helvetica Neue)
- [ ] ≤ 3 text elements; footer band = divider + CTA + logo
- [ ] Every final ad visually reviewed at full size before saving
- [ ] Filenames: `quiz - [concept] - image ad.png` into `Odin Labs Calgary Meta Ads/`
- [ ] Ads Manager: standardized CTA button, concept-slug UTMs, hooks under 125 chars
