# Nutritional Supplementation Page — UX Review & Hero Fix

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Audit `nutritional-supplementation.html` for UX/design issues vs `design.md`, fix all problems, then review the hero image style against `ayurveda.html` (the design.md canonical reference).

**Architecture:** Two parallel tracks — (A) UX/CSS fixes applied locally to `nutritional-supplementation.css` and `nutritional-supplementation.html`, and (B) hero image style review. Visual verification gates each track via browser preview screenshots.

**Tech Stack:** HTML, CSS, preview MCP (visual verification). No JS changes expected.

---

## File Map

| File | Role |
|---|---|
| `nutritional-supplementation.html` | Main page markup — hero image refs, inline style block, HTML structure |
| `nutritional-supplementation.css` | Page-specific styles (prefix: `.ns-`) — all visual fixes go here |
| `design.md` | Source of truth for all design decisions |
| `ayurveda.html` | Reference for hero image style (transparent PNG on dark bg) |
| `ayurveda.css` | Reference for mask-position hover reveal pattern |

---

## Task 1: UX/Design Audit

**Files:**
- Read: `nutritional-supplementation.html`
- Read: `nutritional-supplementation.css`
- Read: `design.md`
- Read: `ayurveda.css` (reference)

- [ ] **Step 1.1: Identify all UX/design issues**

Audit against these specific design.md rules:

1. **Hero image hover — opacity reveal** — `nutritional-supplementation.css` lines 130–136 uses `opacity: 0 → 1` on `.ns-hero-img-color` hover. `design.md` section 5.10 mandates the **mask-position slide reveal**, not opacity. This is a **critical violation**.

2. **Hero image wrapper max-width** — `.ns-hero-image-wrapper` has `max-width: 960px` (line 109). `design.md` section 5.10 rule 3: "No max-width constraint on the wrapper." Must be removed.

3. **`border-radius` on both image tags** — `nutritional-supplementation.css` line 120 sets `border-radius: 20px` on `.ns-hero-img-bw` and line 128 sets `border-radius: 20px` on `.ns-hero-img-color`. The colour overlay must NOT have `border-radius`; wrapper `overflow: hidden` handles clipping.

4. **Hero colour overlay missing `height` and `object-fit`** — `.ns-hero-img-color` at lines 123–136 is `position: absolute` but has no `height: 100%` or `object-fit: cover`. Without these the overlay image may not fill the wrapper correctly at all viewport widths.

5. **Hardcoded hex `#c4ff49` in inline `<style>` block** — `nutritional-supplementation.html` line 14 contains `.hero-slogan{color:#c4ff49!important;}`. `design.md` rule: "Do not hardcode color hex values. Use `var(--lime-green)`." This cannot be updated to `var(--lime-green)` directly inside `!important` inline overrides, but the override itself can be moved into `nutritional-supplementation.css` as a scoped rule using the CSS variable.

6. **CTA heading colour is `var(--white)` not `var(--lime-green)`** — `.ns-cta-heading` (line 729 of CSS) uses `color: var(--white)`. Per the ayurveda pattern and brand consistency (also fixed in `functional-health.css` per prior plan), the CTA heading should be `var(--lime-green)`.

7. **No stats/authority strip after hero** — The page jumps from hero to a compound badges strip (Section 2: "What We Work With"), which is a compound index, not a trust/authority signal. Ayurveda has a `ay-stats-strip` with 4 key trust metrics after the hero. A stats strip with nutritional protocol-relevant metrics should be added between the hero (Section 1) and the badges strip (Section 2).

8. **Section dividers missing** — Sections run together visually. Ayurveda uses `.ay-divider` gradient lines between key sections for visual rhythm. The nutritional supplementation page has no equivalent separators between its 9 sections.

- [ ] **Step 1.2: Prioritise issues**

| Priority | Issue | Action |
|---|---|---|
| 🔴 Critical | Hero opacity reveal → must be mask-position | Fix CSS |
| 🔴 Critical | `max-width: 960px` on hero wrapper | Remove from CSS |
| 🔴 Critical | `border-radius` on both image tags | Remove from colour overlay in CSS |
| 🔴 Critical | Colour overlay missing `height: 100%` + `object-fit: cover` | Add to CSS |
| 🟡 Important | Hardcoded hex in inline `<style>` block | Move override to CSS using `var(--lime-green)` |
| 🟡 Important | CTA heading colour to lime-green | Update CSS |
| 🟡 Important | Add stats strip after hero | Add HTML + CSS |
| 🟢 Enhancement | Add section dividers | Add to HTML |

---

## Task 2: Implement CSS Fixes — Hero Image Reveal

**Files:**
- Modify: `nutritional-supplementation.css` (hero section, lines 107–136)

- [ ] **Step 2.1: Replace hero image CSS with canonical mask-position pattern**

In `nutritional-supplementation.css`, replace the entire `/* Hero dual-layer image */` block (lines 107–136) with:

```css
/* Hero dual-layer image — mask-position slide reveal (matches design.md section 5.10) */
.ns-hero-image-wrapper {
  position: relative;
  /* NO max-width — .ns-hero-inner (1300px) acts as natural constraint per design.md */
  margin: 0 auto;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 40px 80px rgba(0, 0, 0, 0.45),
              0 0 0 1px rgba(196, 255, 73, 0.15);
}

.ns-hero-image-wrapper .ns-hero-img-bw {
  width: 100%;
  display: block;
  filter: grayscale(100%);
  /* NO border-radius — wrapper overflow:hidden handles clipping */
}

.ns-hero-image-wrapper .ns-hero-img-color {
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

.ns-hero-image-wrapper:hover .ns-hero-img-color {
  -webkit-mask-position: 0 0;
  mask-position: 0 0;
}
```

- [ ] **Step 2.2: Commit CSS hero fix**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.css
git commit -m "fix: replace opacity reveal with canonical mask-position slide reveal on ns hero"
```

---

## Task 3: Fix Hardcoded Hex in Inline Style Block

**Files:**
- Modify: `nutritional-supplementation.html` (line 14, inline `<style>` block)
- Modify: `nutritional-supplementation.css` (hero slogan rule)

- [ ] **Step 3.1: Move `.hero-slogan` color override into CSS**

The inline `<style>` block in `nutritional-supplementation.html` (line 14) currently hardcodes:
```css
.hero-slogan{color:#c4ff49!important; ...}
```

Since inline `<style>` blocks cannot use CSS custom properties injected via external stylesheets in all contexts, and the `!important` override is a workaround, the cleanest fix is:

1. Remove the `color:#c4ff49!important` from the inline style block. Keep the other non-color rules (font-size, font-weight, line-height, letter-spacing, margin, text-align, white-space, max-width).
2. Add a scoped rule at the top of `nutritional-supplementation.css`:

```css
/* Hero slogan — scoped override using design token (not hardcoded hex) */
.ns-hero .hero-slogan {
  color: var(--lime-green) !important;
}
```

This eliminates the hardcoded hex violation while maintaining the override specificity.

- [ ] **Step 3.2: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html nutritional-supplementation.css
git commit -m "fix: replace hardcoded hex #c4ff49 with var(--lime-green) for hero slogan"
```

---

## Task 4: Implement CSS Fixes — CTA Heading

**Files:**
- Modify: `nutritional-supplementation.css` (CTA section, line ~729)

- [ ] **Step 4.1: Update CTA heading to lime-green**

In `nutritional-supplementation.css`, change `.ns-cta-heading` color:

```css
.ns-cta-heading {
  ...
  color: var(--lime-green);  /* was var(--white) */
  ...
}
```

- [ ] **Step 4.2: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.css
git commit -m "fix: update ns-cta-heading to lime-green for brand consistency"
```

---

## Task 5: Add Stats Strip (Authority Signal) After Hero

**Files:**
- Modify: `nutritional-supplementation.html` (insert after hero section, before badges strip)
- Modify: `nutritional-supplementation.css` (add stats strip styles)

- [ ] **Step 5.1: Add stats strip HTML**

In `nutritional-supplementation.html`, after the closing `</section>` of `.ns-hero` (line 85), insert before the `<!-- SECTION 2 — COMPOUND BADGES STRIP -->` comment:

```html
<!-- ══════════════════════════════════════════════════════
     STATS STRIP — Authority signal
     ══════════════════════════════════════════════════════ -->
<div class="ns-stats-strip">
  <div class="ns-stats-inner">
    <div class="ns-stat">
      <span class="ns-stat__value">600+</span>
      <span class="ns-stat__label">Enzymatic Reactions Requiring Magnesium</span>
    </div>
    <div class="ns-stat">
      <span class="ns-stat__value">14–48%</span>
      <span class="ns-stat__label">T2D Patients with Hypomagnesemia</span>
    </div>
    <div class="ns-stat">
      <span class="ns-stat__value">37 RCTs</span>
      <span class="ns-stat__label">Meta-Analysed for Berberine Glycemic Control</span>
    </div>
    <div class="ns-stat">
      <span class="ns-stat__value">Lab-First</span>
      <span class="ns-stat__label">Protocol Built on Your Biomarkers — Not Guesswork</span>
    </div>
  </div>
</div>
```

- [ ] **Step 5.2: Add stats strip CSS**

In `nutritional-supplementation.css`, after the hero section block and before the `/* SECTION 2 — COMPOUND BADGES STRIP */` comment, add:

```css
/* ════════════════════════════════════════════════════════
   STATS STRIP — Authority signal
   ════════════════════════════════════════════════════════ */
.ns-stats-strip {
  background: rgba(196, 255, 73, 0.06);
  border-top: 1px solid rgba(196, 255, 73, 0.18);
  border-bottom: 1px solid rgba(196, 255, 73, 0.18);
  padding: 52px 20px;
}

.ns-stats-inner {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
}

.ns-stat {
  text-align: center;
  padding: 0 32px;
  position: relative;
}

.ns-stat + .ns-stat::before {
  content: '';
  position: absolute;
  left: 0; top: 15%; height: 70%; width: 1px;
  background: rgba(196, 255, 73, 0.15);
}

.ns-stat__value {
  display: block;
  font-family: 'Poppins', sans-serif;
  font-size: clamp(1.8rem, 3.5vw, 2.8rem);
  font-weight: 700;
  color: var(--lime-green);
  line-height: 1.1;
  margin-bottom: 8px;
}

.ns-stat__label {
  display: block;
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--white-800);
  line-height: 1.4;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

@media (max-width: 900px) {
  .ns-stats-inner { grid-template-columns: repeat(2, 1fr); gap: 40px 0; }
  .ns-stat + .ns-stat::before { display: none; }
  .ns-stat:nth-child(odd) { border-right: 1px solid rgba(196,255,73,0.12); }
  .ns-stat:nth-child(n+3) { border-top: 1px solid rgba(196,255,73,0.12); padding-top: 40px; }
}

@media (max-width: 480px) {
  .ns-stats-strip { padding: 36px 16px; }
  .ns-stat { padding: 0 16px; }
  .ns-stat__value { font-size: clamp(1.4rem, 6vw, 2rem); }
}
```

- [ ] **Step 5.3: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html nutritional-supplementation.css
git commit -m "feat: add stats strip authority signal below hero on nutritional supplementation page"
```

---

## Task 6: Add Section Dividers

**Files:**
- Modify: `nutritional-supplementation.html` (insert dividers between key sections)
- Modify: `nutritional-supplementation.css` (add divider style)

- [ ] **Step 6.1: Add divider CSS**

In `nutritional-supplementation.css`, after the stats strip styles, add:

```css
/* ════════════════════════════════════════════════════════
   SECTION DIVIDER
   ════════════════════════════════════════════════════════ */
.ns-divider {
  height: 1px;
  background: linear-gradient(to right, transparent 0%, rgba(196, 255, 73, 0.18) 20%, rgba(196, 255, 73, 0.25) 50%, rgba(196, 255, 73, 0.18) 80%, transparent 100%);
  margin: 0;
  border: none;
}
```

- [ ] **Step 6.2: Insert dividers between sections in HTML**

Add `<hr class="ns-divider">` between the following sections in `nutritional-supplementation.html`:
- Between the stats strip and the badges section (Section 2) — though these already share borders; skip if the badges strip's `border-top` is sufficient
- After Section 3 (Supplement Categories) and before Section 4 (Botanical Spotlights)
- After Section 5 (Section Image) and before Section 6 (3-Phase Protocol)
- After Section 6 (3-Phase Protocol) and before Section 7 (Quality Standards)
- After Section 8 (Citations) and before Section 9 (CTA)

Specific placement — add `<hr class="ns-divider">` at these 3 locations only:
- After Section 3 closing `</section>` and before Section 4 opening `<section class="ns-botanicals-section"` — these two sections are visually adjacent with no separator
- After Section 6 closing `</section>` and before Section 7 opening `<section class="ns-quality-section"` — protocol phases and quality standards run together
- After Section 8 closing `</section>` and before Section 9 opening `<section class="ns-cta-section"` — citations run directly into CTA

Skip: Sections 4, 7 already have `border-top: 1px solid rgba(196,255,73,0.08)` built in — they do not need a divider. The stats strip and badges strip share borders already.

- [ ] **Step 6.3: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html nutritional-supplementation.css
git commit -m "feat: add gradient section dividers for visual rhythm on nutritional supplementation page"
```

---

## Task 7: Increment CSS Version Query String

**Files:**
- Modify: `nutritional-supplementation.html` (line 12 — CSS link tag)

- [ ] **Step 7.1: Increment CSS version**

In `nutritional-supplementation.html` line 12, change:
```html
<link rel="stylesheet" href="nutritional-supplementation.css?v=1">
```
To:
```html
<link rel="stylesheet" href="nutritional-supplementation.css?v=2">
```

- [ ] **Step 7.2: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html
git commit -m "chore: increment ns CSS version to v=2 after UX fixes"
```

---

## Task 8: Visual Verification — UX/Design Fixes

**No file changes — verification only.**

- [ ] **Step 8.1: Start preview server**

Use `preview_start` MCP tool to serve the `odin lab landers` directory.

- [ ] **Step 8.2: Screenshot the page**

Use `preview_screenshot` to capture full-page view of `nutritional-supplementation.html`.

- [ ] **Step 8.3: Verify checklist**

Check screenshot against these criteria:
- [ ] Hero image shows grayscale photo by default (no colour bleed)
- [ ] Stats strip visible below hero with 4 lime-green stat values
- [ ] CTA section heading is lime-green (not white)
- [ ] Hero slogan text is lime-green (via CSS variable, not hardcoded)
- [ ] No obvious layout breaks on desktop view

- [ ] **Step 8.4: Hover test on hero**

Use `preview_eval` to trigger a hover event on `.ns-hero-image-wrapper`:
```js
document.querySelector('.ns-hero-image-wrapper').dispatchEvent(new MouseEvent('mouseenter', { bubbles: true }));
```
Then `preview_screenshot` to confirm colour reveal appears as a mask slide, not an opacity pop.

If any issues found: read the relevant CSS block, diagnose, fix, re-screenshot. Do not proceed to Task 9 until all checks pass.

---

## Task 9: Review Hero Image Style vs Ayurveda

**Files:**
- Read: `ayurveda.html` (hero image src reference)
- Read: `nutritional-supplementation.html` (current hero image src)

- [ ] **Step 9.1: Compare hero image styles**

Ayurveda hero image:
- Style: **Transparent PNG** of an illustrated/infographic element (three doshas diagram) on dark green background — image blends seamlessly into page bg; no photographic content; no card frame needed
- Hover: mask-position slide reveal of the colour version of the same PNG

Nutritional Supplementation hero image:
- URL: `https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/nutritional-hero-color.jpg?v=2`
- Style: **JPEG photograph** of medicinal herbs and supplements — opaque background, requires the card wrapper with `border-radius` + `box-shadow` to frame it

**Decision criteria:** If the ns page should match the ayurveda illustrated-transparent-PNG style, the hero image needs to be regenerated as a transparent PNG illustration. If the photographic style is intentional (herbs and supplements lend themselves to photography and may be more trustworthy in a clinical context), only the reveal mechanism needs fixing (already done in Task 2).

> **Recommended approach:** Keep the photographic style for the nutritional supplementation page. Unlike ayurveda (which is conceptual/diagrammatic), supplements and herbs are tangible physical objects. A photographic hero adds credibility and specificity to a clinical supplementation protocol. The card wrapper with `border-radius: 20px` and `box-shadow` is appropriate for this photographic style.

- [ ] **Step 9.2: Confirm decision and document**

If keeping photographic style: no image changes needed. Ensure the hero wrapper styling from Task 2 (border-radius + box-shadow retained) is confirmed in the screenshot.

If switching to transparent PNG: generate new hero image via `nanobanana` with this prompt:
```
A clean, minimalist medical/scientific infographic illustration of botanical herbs, nutritional compounds, and molecular structures arranged as an elegant diagram. Transparent background. Soft whites, greens, and translucent overlapping elements. Precision scientific style suitable for a functional health clinic. Wide landscape format 16:9.
```
Then follow the same Task 6 steps from the Functional Health UX Review plan for swapping the image.

---

## Task 10: Final Full-Page Screenshot

**No file changes — documentation only.**

- [ ] **Step 10.1: Take final full-page screenshot**

Use `preview_screenshot` for a full-page view of `nutritional-supplementation.html`. This is the record screenshot.

- [ ] **Step 10.2: Verify final checklist**

- [ ] Hero image shows grayscale by default
- [ ] Hover reveals colour image via mask slide (not opacity)
- [ ] Stats strip below hero with 4 authority metrics
- [ ] CTA heading is lime-green
- [ ] No hardcoded hex values in CSS (verify in DevTools)
- [ ] Section dividers visible between main content blocks
- [ ] CSS version string is `?v=2`
- [ ] No regressions — badges strip, category cards, botanical cards, protocol phases, quality standards, citations, CTA all intact

---

## Summary of Changes

| File | Changes |
|---|---|
| `nutritional-supplementation.html` | Hero img: remove hardcoded hex from inline style; stats strip HTML added; section dividers added; CSS version incremented to v=2 |
| `nutritional-supplementation.css` | Hero reveal → mask-position (critical fix); hero wrapper max-width removed; border-radius removed from overlay; height + object-fit added to overlay; hero slogan color moved to CSS var token; stats strip styles added; divider style added; CTA heading → lime-green |

## Verification Gate

Before claiming completion, ensure:
1. Hero has grayscale base + mask-position colour reveal (not opacity)
2. Hero wrapper has no `max-width` constraint
3. Colour overlay has no `border-radius`, has `height: 100%` and `object-fit: cover`
4. Stats strip shows below hero
5. CTA heading is lime-green
6. No hardcoded hex `#c4ff49` anywhere in the page
7. CSS version string is `?v=2`
8. All other sections intact (no regressions)
