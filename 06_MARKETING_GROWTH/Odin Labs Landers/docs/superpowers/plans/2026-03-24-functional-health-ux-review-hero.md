# Functional Health Page — UX Review, Design Fixes & Hero Image Refresh

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Audit `functional-health.html` for UX/design issues vs `design.md`, fix all problems, then align the hero image style to match `ayurveda.html`.

**Architecture:** Two parallel tracks — (A) UX/CSS fixes applied locally to `functional-health.css` and `functional-health.html`, and (B) hero image regeneration via `nanobanana` to match the transparent/illustrated style of the Ayurveda page hero. Visual verification gates each track via browser preview screenshots.

**Tech Stack:** HTML, CSS, nanobanana MCP (image generation), preview MCP (visual verification). No JS changes expected.

---

## File Map

| File | Role |
|---|---|
| `functional-health.html` | Main page markup — hero image refs, HTML structure |
| `functional-health.css` | Page-specific styles — all visual fixes go here |
| `design.md` | Source of truth for all design decisions |
| `ayurveda.html` | Reference for hero image style (transparent PNG on dark bg) |
| `ayurveda.css` | Reference for mask-position hover reveal pattern |

---

## Task 1: UX/Design Audit

**Files:**
- Read: `functional-health.html`
- Read: `functional-health.css`
- Read: `design.md`
- Read: `ayurveda.css` (reference)

- [ ] **Step 1.1: Identify all UX/design issues**

Audit against these specific design.md rules:
1. **Hero image hover** — `functional-health.css` uses `opacity: 0 → 1` for the colour overlay (lines 67–77). `design.md` section 5.10 mandates the **mask-position slide reveal**, not opacity. This is a critical violation.
2. **Hero image wrapper max-width** — `.fh-hero-image-wrapper` has `max-width: 1000px`. `design.md` says "No max-width constraint on the wrapper" (section 5.10, rule 3). Must be removed.
3. **Hero image border-radius on colour image** — `.fh-hero-image-wrapper .fh-hero-img` has `border-radius: 20px`. The colour overlay image must NOT have border-radius; wrapper `overflow: hidden` handles clipping.
4. **Hero image — both img tags point to the same file** — Currently both use `functional-health-hero-color.jpg`. That is correct — no change needed, but verify.
5. **Section tag used in CTA section** — The `fh-cta-section` uses a bare `<span class="fh-section-tag">` directly (not inside `.fh-header-block`). Minor structural inconsistency; acceptable — no change needed.
6. **CTA heading colour** — `.fh-cta-heading` is `var(--white)`. Ayurveda's `.ay-cta-heading` uses `var(--lime-green)`. The design.md doesn't prescribe this specifically for CTA, but lime-green for CTA heading is more on-brand. Update to `var(--lime-green)`.
7. **Stats/authority strip missing** — Ayurveda page has a `ay-stats-strip` after the hero. Functional Health has no equivalent authority/trust signal after the hero. Add a 4-stat strip (matching ayurveda's pattern) with relevant functional medicine stats.
8. **Divider lines missing** — Ayurveda uses `.ay-divider` gradient lines between sections for visual rhythm. Functional Health has no dividers — sections run together. Add between key sections.
9. **Hero image class naming** — The HTML uses `fh-hero-img` for the BW base and `fh-hero-img fh-hero-img-color` for the colour overlay. CSS targets `.fh-hero-image-wrapper .fh-hero-img-color` for the override, but the base image also gets the `fh-hero-img` class styling (including `border-radius: 20px`). This must be split properly:
   - Base: class `fh-hero-img-bw` (grayscale, no absolute positioning)
   - Overlay: class `fh-hero-img-color` (absolute, mask animation)

- [ ] **Step 1.2: Prioritise issues**

| Priority | Issue | Action |
|---|---|---|
| 🔴 Critical | Hero opacity reveal → must be mask-position | Fix in CSS |
| 🔴 Critical | `max-width: 1000px` on hero wrapper | Remove |
| 🔴 Critical | `border-radius` on both images | Remove from overlay image |
| 🟡 Important | CTA heading colour to lime-green | Update CSS |
| 🟡 Important | Add stats strip after hero | Add HTML + CSS |
| 🟢 Enhancement | Add section dividers | Add to HTML |

---

## Task 2: Implement CSS Fixes — Hero Image Reveal

**Files:**
- Modify: `functional-health.css` (hero section, lines 51–77)
- Modify: `functional-health.html` (hero img class names, lines 72–82)

- [ ] **Step 2.1: Update hero image HTML — split BW/colour classes**

In `functional-health.html`, change lines 72–82 from:
```html
<img
  src="https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/functional-health-hero-color.jpg?v=2"
  alt="Functional medicine practitioner reviewing advanced lab results with a patient at Odin Lab Calgary"
  class="fh-hero-img"
/>
<img
  src="https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/functional-health-hero-color.jpg?v=2"
  alt=""
  aria-hidden="true"
  class="fh-hero-img fh-hero-img-color"
/>
```
To:
```html
<img
  src="https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/functional-health-hero-color.jpg?v=2"
  alt="Functional medicine practitioner reviewing advanced lab results with a patient at Odin Lab Calgary"
  class="fh-hero-img-bw"
/>
<img
  src="https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/functional-health-hero-color.jpg?v=2"
  alt=""
  aria-hidden="true"
  class="fh-hero-img-color"
/>
```

- [ ] **Step 2.2: Replace hero image CSS with canonical mask-position pattern**

NOTE: `border-radius: 20px` is added here provisionally. If Task 6 proceeds with a transparent PNG hero (recommended), Task 6 Step 6.6 will remove it and the `box-shadow`. An executor must apply Task 6 Step 6.6 as an explicit CSS update.

In `functional-health.css`, replace the entire hero dual-image block (lines 51–77) with:

```css
/* Hero dual-image — mask-position slide reveal (matches design.md section 5.10) */
/* NOTE: border-radius + box-shadow are provisional; removed in Task 6 if transparent PNG is used */
.fh-hero-image-wrapper {
  position: relative;
  /* NO max-width — .fh-container (1300px) acts as natural constraint per design.md */
  margin: 0 auto;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 32px 80px rgba(0, 0, 0, 0.5);
}

.fh-hero-image-wrapper .fh-hero-img-bw {
  width: 100%;
  display: block;
  filter: grayscale(100%);
}

.fh-hero-image-wrapper .fh-hero-img-color {
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

.fh-hero-image-wrapper:hover .fh-hero-img-color {
  -webkit-mask-position: 0 0;
  mask-position: 0 0;
}
```

Also remove the now-redundant old `.fh-hero-image-wrapper .fh-hero-img` rule.

- [ ] **Step 2.3: Commit CSS+HTML hero fix**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add functional-health.css functional-health.html
git commit -m "fix: replace opacity reveal with canonical mask-position slide reveal on functional-health hero"
```

---

## Task 3: Implement CSS Fixes — CTA Heading & Other Design Issues

**Files:**
- Modify: `functional-health.css` (CTA section, lines ~777)

- [ ] **Step 3.1: Update CTA heading to lime-green**

In `functional-health.css`, change `.fh-cta-heading` color:
```css
.fh-cta-heading {
  ...
  color: var(--lime-green);  /* was var(--white) */
  ...
}
```

- [ ] **Step 3.2: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add functional-health.css
git commit -m "fix: update fh-cta-heading to lime-green for brand consistency"
```

---

## Task 4: Add Stats Strip (Authority Signal) After Hero

**Files:**
- Modify: `functional-health.html` (insert after hero section, before section 2)
- Modify: `functional-health.css` (add stats strip styles)

- [ ] **Step 4.1: Add stats strip HTML**

In `functional-health.html`, after the closing `</section>` of `.fh-hero` (line 85), insert:

```html
<!-- ══════════════════════════════════════════════════════
     STATS STRIP — Authority signal
     ══════════════════════════════════════════════════════ -->
<div class="fh-stats-strip">
  <div class="fh-stats-inner">
    <div class="fh-stat">
      <span class="fh-stat__value">7,252</span>
      <span class="fh-stat__label">Patients — Cleveland Clinic FM Study</span>
    </div>
    <div class="fh-stat">
      <span class="fh-stat__value">31%</span>
      <span class="fh-stat__label">Clinically Meaningful Health Improvement</span>
    </div>
    <div class="fh-stat">
      <span class="fh-stat__value">6</span>
      <span class="fh-stat__label">Advanced Diagnostic Panels</span>
    </div>
    <div class="fh-stat">
      <span class="fh-stat__value">Root</span>
      <span class="fh-stat__label">Cause — Not Symptom — Focused</span>
    </div>
  </div>
</div>
```

- [ ] **Step 4.2: Add stats strip CSS**

In `functional-health.css`, after the hero section block, add:

```css
/* ════════════════════════════════════════════════════════
   STATS STRIP
   ════════════════════════════════════════════════════════ */
.fh-stats-strip {
  background: rgba(196, 255, 73, 0.06);
  border-top: 1px solid rgba(196, 255, 73, 0.18);
  border-bottom: 1px solid rgba(196, 255, 73, 0.18);
  padding: 52px 20px;
}

.fh-stats-inner {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
}

.fh-stat {
  text-align: center;
  padding: 0 32px;
  position: relative;
}

.fh-stat + .fh-stat::before {
  content: '';
  position: absolute;
  left: 0; top: 15%; height: 70%; width: 1px;
  background: rgba(196, 255, 73, 0.15);
}

.fh-stat__value {
  display: block;
  font-family: 'Poppins', sans-serif;
  font-size: clamp(1.8rem, 3.5vw, 2.8rem);
  font-weight: 700;
  color: var(--lime-green);
  line-height: 1.1;
  margin-bottom: 8px;
}

.fh-stat__label {
  display: block;
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--white-800);
  line-height: 1.4;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

@media (max-width: 900px) {
  .fh-stats-inner { grid-template-columns: repeat(2, 1fr); gap: 40px 0; }
  .fh-stat + .fh-stat::before { display: none; }
  .fh-stat:nth-child(odd) { border-right: 1px solid rgba(196,255,73,0.12); }
  .fh-stat:nth-child(n+3) { border-top: 1px solid rgba(196,255,73,0.12); padding-top: 40px; }
}

@media (max-width: 480px) {
  .fh-stats-strip { padding: 36px 16px; }
  .fh-stat { padding: 0 16px; }
  .fh-stat__value { font-size: clamp(1.4rem, 6vw, 2rem); }
}
```

- [ ] **Step 4.3: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add functional-health.html functional-health.css
git commit -m "feat: add stats strip authority signal below hero on functional-health page"
```

---

## Task 5: Visual Verification — UX/Design Fixes

**No file changes — verification only.**

- [ ] **Step 5.1: Start preview server**

Use `preview_start` MCP tool to serve the `odin lab landers` directory.

- [ ] **Step 5.2: Screenshot the page**

Use `preview_screenshot` to capture full-page view of `functional-health.html`.

- [ ] **Step 5.3: Verify checklist**

Check screenshot against these criteria:
- [ ] Hero image shows grayscale photo by default
- [ ] Stats strip visible below hero with 4 lime-green stat values
- [ ] CTA section heading is lime-green (not white)
- [ ] No obvious layout breaks on desktop view

- [ ] **Step 5.4: Hover test on hero**

Use `preview_eval` to trigger a hover event on `.fh-hero-image-wrapper` and then `preview_screenshot` to confirm colour reveal appears (mask slide, not opacity pop).

If any issues found: read the relevant CSS block, diagnose, fix, re-screenshot. Do not proceed to Task 6 until all checks pass.

---

## Task 6: Review Hero Image Style vs Ayurveda

**Files:**
- Read: `ayurveda.html` (hero image src reference)
- Read: `functional-health.html` (current hero image src)

- [ ] **Step 6.1: Compare hero image styles**

Ayurveda hero image:
- URL: `https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/ay-transparent_darkgreen.png?v=1`
- Style: **Transparent PNG** of an illustrated/infographic element (three doshas diagram) on the dark green background — no photographic content; the image blends seamlessly into the page bg
- Hover: mask-position slide reveal of the colour version of the same PNG

Functional Health hero image:
- URL: `https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/functional-health-hero-color.jpg?v=2`
- Style: **JPEG photograph** of a practitioner and patient — opaque background, requires the rounded card wrapper to frame it

These are meaningfully different. The ayurveda style is: a transparent PNG illustration/diagram placed directly on the dark green background, no card frame needed. The functional health page uses a photographic style in a card.

**Decision criteria:** If the functional-health page should match the ayurveda illustrated-transparent-PNG style, the hero image needs to be regenerated as a transparent PNG illustration. If the photographic style is intentional, only the reveal mechanism needs fixing (already done in Task 2).

- [ ] **Step 6.2: Generate new hero image in Ayurveda style**

Generate a new hero image using `nanobanana` `generate_image` MCP tool.

Prompt for generation:
```
A clean, minimalist medical/scientific infographic illustration showing interconnected biological systems — gut microbiome, hormone pathways, metabolic network, and cellular health — represented as a beautiful diagram with flowing lines and nodes on a transparent background. The illustration uses a limited palette of soft whites, subtle greens, and translucent overlapping circles. The style is precise and scientific yet elegant, suitable for a functional health clinic landing page. Transparent background. PNG format. No text. 16:9 aspect ratio, wide landscape format.
```

Save output to: `nanobanana-output/functional-health-hero-transparent.png`

- [ ] **Step 6.3: Evaluate generated image**

View generated image. Confirm it:
- Has transparent background (or very close to the dark green page bg)
- Matches the illustrated/diagrammatic style (not photographic)
- Is wide landscape format suitable as a hero image

If the image is photographic or doesn't match style: re-prompt with stronger transparency/illustration emphasis. Up to 3 attempts.

- [ ] **Step 6.4: Upload image to CDN repo**

The image will need to be committed to the `bluehatgeeks/Odin-Health-Calgary` GitHub repo (the CDN source). For local testing, we will reference it via a local relative path first.

Copy the approved PNG from `nanobanana-output/` to the working directory:
```bash
cp "nanobanana-output/functional-health-hero-transparent.png" "/Users/alexandertretjakov/Downloads/odin lab landers/functional-health-hero-transparent.png"
```

- [ ] **Step 6.5: Update hero image src in functional-health.html to local path**

Change both `<img>` src attributes in the hero from:
```
https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/functional-health-hero-color.jpg?v=2
```
To:
```
functional-health-hero-transparent.png
```

Also update the `alt` text to match the new image content.

- [ ] **Step 6.6: Remove card-style wrapper constraints if switching to transparent PNG**

If switching to transparent PNG style (like ayurveda), the wrapper should NOT have:
- `box-shadow: 0 32px 80px rgba(0, 0, 0, 0.5)` — remove (transparent PNG doesn't need card shadow)
- `border-radius: 20px` on the wrapper — remove (no card frame needed)

In `functional-health.css`, update `.fh-hero-image-wrapper`:
```css
.fh-hero-image-wrapper {
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
git add functional-health.html functional-health.css functional-health-hero-transparent.png
git commit -m "feat: replace photographic hero with transparent PNG illustration matching ayurveda page style"
```

---

## Task 7: Visual Verification — Hero Image

**No file changes — verification only.**

- [ ] **Step 7.1: Screenshot hero section**

Use `preview_screenshot` focused on the hero section of `functional-health.html`.

- [ ] **Step 7.2: Verify checklist**

Check screenshot against these criteria:
- [ ] Hero image is an illustration/diagram (not a photograph)
- [ ] Image blends into the dark green background (transparent PNG look)
- [ ] No card border/shadow around the image (seamless integration)
- [ ] Image is wide, full-width within container
- [ ] Page otherwise intact — nav, headings, stats strip all visible

- [ ] **Step 7.3: Test hover colour reveal**

Use `preview_eval` to simulate hover on `.fh-hero-image-wrapper`:
```js
document.querySelector('.fh-hero-image-wrapper').dispatchEvent(new MouseEvent('mouseenter', { bubbles: true }));
```
Then `preview_screenshot` to confirm mask-position reveal works on the new image.

- [ ] **Step 7.4: Final full-page screenshot**

Take a full-page screenshot for the record. If any issues found, diagnose, fix CSS/HTML, re-screenshot. Task complete when all checks pass.

---

## Summary of Changes

| File | Changes |
|---|---|
| `functional-health.html` | Hero img class split (bw/color), stats strip HTML added, hero img src updated to new transparent PNG |
| `functional-health.css` | Hero reveal → mask-position (critical fix), stats strip styles added, CTA heading → lime-green, hero wrapper simplified for transparent PNG |
| `functional-health-hero-transparent.png` | New hero image in ayurveda illustrated style |

## Verification Gate

Before claiming completion, ensure:
1. Hero has grayscale base + mask-position colour reveal (not opacity)
2. Hero image is illustration-style transparent PNG (not photograph)
3. Stats strip shows below hero
4. CTA heading is lime-green
5. No regressions — all other sections intact
