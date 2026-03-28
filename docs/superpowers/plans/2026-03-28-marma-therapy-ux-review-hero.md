# Marma Therapy Page — UX Review, Design Fixes & Hero Image Refresh

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Audit `marma-therapy.html` for UX/design issues vs `design.md`, fix all problems, then evaluate the hero image style against `ayurveda.html`.

**Architecture:** Two parallel tracks — (A) UX/CSS fixes applied locally to `marma-therapy.css` and `marma-therapy.html`, and (B) hero image regeneration via `nanobanana` to match the transparent/illustrated style of the Ayurveda page hero. Visual verification gates each track via browser preview screenshots.

**Tech Stack:** HTML, CSS, nanobanana MCP (image generation), preview MCP (visual verification). No JS changes expected.

---

## File Map

| File | Role |
|---|---|
| `marma-therapy.html` | Main page markup — hero image refs, HTML structure |
| `marma-therapy.css` | Page-specific styles — all visual fixes go here |
| `design.md` | Source of truth for all design decisions |
| `ayurveda.html` | Reference for hero image style (transparent PNG on dark bg) |
| `ayurveda.css` | Reference for mask-position hover reveal pattern |

---

## Task 1: UX/Design Audit

**Files:**
- Read: `marma-therapy.html`
- Read: `marma-therapy.css`
- Read: `design.md`
- Read: `ayurveda.css` (reference)

- [ ] **Step 1.1: Identify all UX/design issues**

Audit against these specific design.md rules:

1. **Hero reveal: opacity toggle instead of mask-position** — `marma-therapy.css` lines 132–145 use `opacity: 0 → 1` on `.mt-hero-image-color` for the colour reveal. `design.md §5.10` mandates the **mask-position slide reveal** (left-to-right wipe), not opacity. This is a critical pattern violation.
2. **Hero wrapper max-width** — `.mt-hero-image-wrapper` has `max-width: 960px` (line 119). `design.md §5.10 rule 3` says "No max-width constraint on the wrapper" — the `.mt-container` (1300px) acts as the natural constraint.
3. **border-radius on both img tags** — Both `.mt-hero-image-bw` (line 129) and `.mt-hero-image-color` (line 137) carry `border-radius: 20px`. Per `design.md §5.10`, only the wrapper clips; the overlay img must NOT have its own border-radius.
4. **Missing `filter: grayscale(100%)` on BW base** — `.mt-hero-image-bw` (lines 126–130) has no grayscale filter — the "base" already shows full colour. Per `design.md §5.10`, the BW layer must use `filter: grayscale(100%)`. Without it the hover reveal does nothing.
5. **No stats strip after hero** — Ayurveda and functional-health both have a post-hero authority strip. Marma has rich quantitative material (107 points, 1000–600 BCE, 74% medication reduction, 40 Hz research) that can power a 4-stat strip. None currently exists.
6. **CTA heading colour** — `.mt-cta-heading` uses `color: var(--white)` (line 871). On-brand consistency with ayurveda and functional-health requires `var(--lime-green)`.

- [ ] **Step 1.2: Prioritise issues**

| Priority | Issue | Action |
|---|---|---|
| 🔴 Critical | Hero opacity reveal → must be mask-position | Fix in CSS |
| 🔴 Critical | `max-width: 960px` on hero wrapper | Remove |
| 🔴 Critical | `border-radius` on both img tags | Remove from both |
| 🔴 Critical | Missing `filter: grayscale(100%)` on BW layer | Add to CSS |
| 🟡 Important | Add stats strip after hero | Add HTML + CSS |
| 🟡 Important | CTA heading colour to lime-green | Update CSS |
| 🟢 Enhancement | Hero image style: transparent PNG (optional) | Evaluate in Task 6 |

---

## Task 2: Implement CSS Fixes — Hero Image Reveal

**Files:**
- Modify: `marma-therapy.css` (hero section, lines 117–145)

- [ ] **Step 2.1: Replace hero image CSS with canonical mask-position pattern**

NOTE: `border-radius: 20px` and `box-shadow` are added provisionally for the photographic JPEG. If Task 6 proceeds with a transparent PNG hero, Task 6 Step 6.6 removes them.

In `marma-therapy.css`, replace the entire hero dual-image block (lines 117–145) with:

```css
/* Hero dual-image — mask-position slide reveal (matches design.md §5.10) */
/* NOTE: border-radius + box-shadow are provisional; removed in Task 6 if transparent PNG is used */
.mt-hero-image-wrapper {
  position: relative;
  /* NO max-width — .mt-container (1300px) acts as natural constraint per design.md */
  margin: 0 auto;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 32px 80px rgba(0, 0, 0, 0.5);
}

.mt-hero-image-wrapper .mt-hero-image-bw {
  width: 100%;
  display: block;
  filter: grayscale(100%);
  /* NO border-radius — wrapper overflow:hidden handles clipping */
}

.mt-hero-image-wrapper .mt-hero-image-color {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  object-fit: cover;
  /* NO border-radius — wrapper overflow:hidden handles clipping */
  -webkit-mask-image: linear-gradient(to right, black 0%, black 50%, rgba(0,0,0,0.6) 65%, rgba(0,0,0,0.2) 82%, transparent 100%);
  mask-image: linear-gradient(to right, black 0%, black 50%, rgba(0,0,0,0.6) 65%, rgba(0,0,0,0.2) 82%, transparent 100%);
  -webkit-mask-size: 200% 100%;
  mask-size: 200% 100%;
  -webkit-mask-position: -100% 0;
  mask-position: -100% 0;
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
  transition: mask-position 0.9s cubic-bezier(0.4, 0, 0.2, 1),
              -webkit-mask-position 0.9s cubic-bezier(0.4, 0, 0.2, 1);
}

.mt-hero-image-wrapper:hover .mt-hero-image-color {
  -webkit-mask-position: 0 0;
  mask-position: 0 0;
}
```

- [ ] **Step 2.2: Commit CSS hero fix**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add marma-therapy.css
git commit -m "fix: replace opacity reveal with canonical mask-position slide reveal on marma-therapy hero"
```

---

## Task 3: Implement CSS Fixes — CTA Heading Colour

**Files:**
- Modify: `marma-therapy.css` (CTA section, ~line 871)

- [ ] **Step 3.1: Update CTA heading to lime-green**

In `marma-therapy.css`, change `.mt-cta-heading` color:
```css
.mt-cta-heading {
  ...
  color: var(--lime-green);  /* was var(--white) */
  ...
}
```

- [ ] **Step 3.2: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add marma-therapy.css
git commit -m "fix: update mt-cta-heading to lime-green for brand consistency"
```

---

## Task 4: Add Stats Strip (Authority Signal) After Hero

**Files:**
- Modify: `marma-therapy.html` (insert after hero div, before first divider)
- Modify: `marma-therapy.css` (add stats strip styles)

- [ ] **Step 4.1: Add stats strip HTML**

In `marma-therapy.html`, after the closing `</div>` of `.mt-hero.mt-container` (line 89), and before the first `.mt-divider` (line 91), insert:

```html
<!-- ══════════════════════════════════════════════════════
     STATS STRIP — Authority signal
     ══════════════════════════════════════════════════════ -->
<div class="mt-stats-strip">
  <div class="mt-stats-inner">
    <div class="mt-stat">
      <span class="mt-stat__value">107</span>
      <span class="mt-stat__label">Vital Marma Points — Sushruta Samhita</span>
    </div>
    <div class="mt-stat">
      <span class="mt-stat__value">40 Hz</span>
      <span class="mt-stat__label">Clinically Studied Therapeutic Frequency</span>
    </div>
    <div class="mt-stat">
      <span class="mt-stat__value">74%</span>
      <span class="mt-stat__label">Pain Medication Reduction — Fibromyalgia Study</span>
    </div>
    <div class="mt-stat">
      <span class="mt-stat__value">1000 BCE</span>
      <span class="mt-stat__label">Original Codification — Sushruta Samhita</span>
    </div>
  </div>
</div>
```

- [ ] **Step 4.2: Add stats strip CSS**

In `marma-therapy.css`, after the hero section block (after line 145), add:

```css
/* ════════════════════════════════════════════════════════
   STATS STRIP
   ════════════════════════════════════════════════════════ */
.mt-stats-strip {
  background: rgba(196, 255, 73, 0.06);
  border-top: 1px solid rgba(196, 255, 73, 0.18);
  border-bottom: 1px solid rgba(196, 255, 73, 0.18);
  padding: 52px 20px;
}

.mt-stats-inner {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
}

.mt-stat {
  text-align: center;
  padding: 0 32px;
  position: relative;
}

.mt-stat + .mt-stat::before {
  content: '';
  position: absolute;
  left: 0; top: 15%; height: 70%; width: 1px;
  background: rgba(196, 255, 73, 0.15);
}

.mt-stat__value {
  display: block;
  font-family: 'Poppins', sans-serif;
  font-size: clamp(1.8rem, 3.5vw, 2.8rem);
  font-weight: 700;
  color: var(--lime-green);
  line-height: 1.1;
  margin-bottom: 8px;
}

.mt-stat__label {
  display: block;
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--white-800);
  line-height: 1.4;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

@media (max-width: 900px) {
  .mt-stats-inner { grid-template-columns: repeat(2, 1fr); gap: 40px 0; }
  .mt-stat + .mt-stat::before { display: none; }
  .mt-stat:nth-child(odd) { border-right: 1px solid rgba(196,255,73,0.12); }
  .mt-stat:nth-child(n+3) { border-top: 1px solid rgba(196,255,73,0.12); padding-top: 40px; }
}

@media (max-width: 480px) {
  .mt-stats-strip { padding: 36px 16px; }
  .mt-stat { padding: 0 16px; }
  .mt-stat__value { font-size: clamp(1.4rem, 6vw, 2rem); }
}
```

- [ ] **Step 4.3: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add marma-therapy.html marma-therapy.css
git commit -m "feat: add stats strip authority signal below hero on marma-therapy page"
```

---

## Task 5: Visual Verification — UX/Design Fixes

**No file changes — verification only.**

- [ ] **Step 5.1: Start preview server**

Use `preview_start` MCP tool to serve the `odin lab landers` directory.

- [ ] **Step 5.2: Screenshot the page**

Use `preview_screenshot` to capture full-page view of `marma-therapy.html`.

- [ ] **Step 5.3: Verify checklist**

Check screenshot against these criteria:
- [ ] Hero image shows grayscale photo by default (not full colour)
- [ ] Stats strip visible below hero with 4 lime-green stat values
- [ ] CTA section heading is lime-green (not white)
- [ ] No obvious layout breaks on desktop view

- [ ] **Step 5.4: Hover test on hero**

Use `preview_eval` to trigger a hover event on `.mt-hero-image-wrapper` and then `preview_screenshot` to confirm colour reveal appears (mask slide, not opacity pop):
```js
document.querySelector('.mt-hero-image-wrapper').dispatchEvent(new MouseEvent('mouseenter', { bubbles: true }));
```

If any issues found: read the relevant CSS block, diagnose, fix, re-screenshot. Do not proceed to Task 6 until all checks pass.

---

## Task 6: Review Hero Image Style vs Ayurveda

**Files:**
- Read: `ayurveda.html` (hero image src reference)
- Read: `marma-therapy.html` (current hero image src)

- [ ] **Step 6.1: Compare hero image styles**

Ayurveda hero image:
- URL: `https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/ay-transparent_darkgreen.png?v=1`
- Style: **Transparent PNG** of an illustrated/infographic element (three doshas diagram) on the dark green background — no photographic content; the image blends seamlessly into the page bg
- Hover: mask-position slide reveal of the colour version of the same PNG

Marma Therapy hero image:
- URL: `https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/marma-hero-color.jpg?v=2`
- Style: **JPEG photograph** of a marma therapy session — opaque background, requires the rounded card wrapper to frame it

These are meaningfully different. The ayurveda style is: a transparent PNG illustration/diagram placed directly on the dark green background, no card frame needed. The marma page uses a photographic style in a card.

**Decision criteria:** If the marma page should match the ayurveda illustrated-transparent-PNG style, the hero image needs to be regenerated as a transparent PNG illustration. If the photographic style is intentional, only the reveal mechanism fix (already done in Task 2) is needed.

- [ ] **Step 6.2: Generate new hero image in Ayurveda style**

Generate a new hero image using `nanobanana` `generate_image` MCP tool.

Prompt for generation:
```
A clean, minimalist anatomical/energetic illustration showing the human body's marma point network — 107 vital junctions mapped as glowing nodes connected by flowing energy channels across the body silhouette, with tuning fork frequency waves radiating from key points. The illustration uses a limited palette of soft whites, subtle greens, and translucent overlapping circles and wave patterns. The style is precise and scientific yet elegant, suitable for a therapeutic wellness clinic landing page. Transparent background. PNG format. No text. 16:9 aspect ratio, wide landscape format.
```

Save output to: `nanobanana-output/marma-hero-transparent.png`

- [ ] **Step 6.3: Evaluate generated image**

View generated image. Confirm it:
- Has transparent background (or very close to the dark green page bg)
- Matches the illustrated/diagrammatic style (not photographic)
- Is wide landscape format suitable as a hero image

If the image is photographic or doesn't match style: re-prompt with stronger transparency/illustration emphasis. Up to 3 attempts.

- [ ] **Step 6.4: Copy image for local testing**

```bash
cp "nanobanana-output/marma-hero-transparent.png" "/Users/alexandertretjakov/Downloads/odin lab landers/marma-hero-transparent.png"
```

- [ ] **Step 6.5: Update hero image src in marma-therapy.html to local path**

Change both `<img>` src attributes in the hero from:
```
https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/marma-hero-color.jpg?v=2
```
To:
```
marma-hero-transparent.png
```

Also update the `alt` text to match the new image content.

- [ ] **Step 6.6: Remove card-style wrapper constraints for transparent PNG**

If switching to transparent PNG style, the wrapper should NOT have card styling:

In `marma-therapy.css`, update `.mt-hero-image-wrapper`:
```css
.mt-hero-image-wrapper {
  position: relative;
  overflow: hidden;
  margin: 0 auto;
  background: var(--dark-green);
  /* No border-radius, no box-shadow — transparent PNG blends into bg */
}
```

- [ ] **Step 6.7: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add marma-therapy.html marma-therapy.css marma-hero-transparent.png
git commit -m "feat: replace photographic hero with transparent PNG illustration matching ayurveda page style"
```

---

## Task 7: Visual Verification — Hero Image

**No file changes — verification only.**

- [ ] **Step 7.1: Screenshot hero section**

Use `preview_screenshot` focused on the hero section of `marma-therapy.html`.

- [ ] **Step 7.2: Verify checklist**

Check screenshot against these criteria:
- [ ] Hero image is an illustration/diagram (not a photograph)
- [ ] Image blends into the dark green background (transparent PNG look)
- [ ] No card border/shadow around the image (seamless integration)
- [ ] Image is wide, full-width within container
- [ ] Page otherwise intact — nav, headings, stats strip all visible

- [ ] **Step 7.3: Test hover colour reveal**

Use `preview_eval` to simulate hover on `.mt-hero-image-wrapper`:
```js
document.querySelector('.mt-hero-image-wrapper').dispatchEvent(new MouseEvent('mouseenter', { bubbles: true }));
```
Then `preview_screenshot` to confirm mask-position reveal works on the new image.

- [ ] **Step 7.4: Final full-page screenshot**

Take a full-page screenshot for the record. If any issues found, diagnose, fix CSS/HTML, re-screenshot. Task complete when all checks pass.

---

## Summary of Changes

| File | Changes |
|---|---|
| `marma-therapy.html` | Stats strip HTML added, hero img src updated to new transparent PNG |
| `marma-therapy.css` | Hero reveal → mask-position + grayscale fix (critical), max-width removed, border-radius removed from img tags, stats strip styles added, CTA heading → lime-green, hero wrapper simplified for transparent PNG |
| `marma-hero-transparent.png` | New hero image in ayurveda illustrated style |

## Verification Gate

Before claiming completion, ensure:
1. Hero base image shows grayscale (filter applied)
2. Hero hover uses mask-position slide (not opacity fade)
3. Hero wrapper has no max-width constraint
4. Stats strip shows below hero with 4 lime-green values
5. CTA heading is lime-green
6. No regressions — all other sections intact
