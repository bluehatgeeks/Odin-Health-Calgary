# Functional Health Coaching Page — UX Review & Design Fixes

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Audit `functional-coaching.html` for UX/design issues vs `design.md`, then fix all problems found.

**Architecture:** Single track — UX/CSS fixes applied locally to `functional-coaching.css` and `functional-coaching.html`. Visual verification gates each phase via browser preview screenshots.

**Tech Stack:** HTML, CSS, preview MCP (visual verification). No JS changes expected.

---

## File Map

| File | Role |
|---|---|
| `functional-coaching.html` | Main page markup |
| `functional-coaching.css` | Page-specific styles — all visual fixes go here |
| `design.md` | Source of truth for all design decisions |
| `ayurveda.html` | Reference page for stats strip + divider patterns |
| `functional-health.css` | Reference for already-fixed mask-position hero pattern |

---

## Task 1: UX/Design Audit

**Files:**
- Read: `functional-coaching.html`
- Read: `functional-coaching.css`
- Read: `design.md`

- [ ] **Step 1.1: Identify all UX/design issues**

Audit against `design.md` rules. Issues found:

1. **Hero image reveal — opacity toggle instead of mask-position** (`functional-coaching.css` lines 144–157)
   `.fc-hero-img-color` uses `opacity: 0 → 1` on hover. `design.md` section 5.10 mandates the **mask-position slide reveal**. Critical violation — same error that was fixed on `functional-health.html`.

2. **Hero image wrapper has `max-width: 960px`** (`functional-coaching.css` line 131)
   `design.md` section 5.10 rule 3: "No `max-width` constraint on the wrapper." Must be removed.

3. **Hero image color layer missing `height: 100%` and `object-fit: cover`** (`functional-coaching.css` lines 144–157)
   The `.fc-hero-img-color` rule has no `height: 100%` or `object-fit: cover`. Without these, the absolutely-positioned color overlay won't fill the wrapper correctly when the mask transition runs. Must be added.

4. **`border-radius: 20px` on both img tags** (`functional-coaching.css` lines 141, 149)
   `design.md` section 5.10 rule 2: "No `border-radius` on the colour overlay image." The wrapper's `overflow: hidden` handles corner clipping. Both images currently have `border-radius: 20px` — the color overlay image must have it removed.

5. **No stats strip after hero** — The page has no authority/trust signal below the hero. `ayurveda.html` and (now) `functional-health.html` both have a stats strip after the hero. Functional Coaching has none. A 4-stat strip with coaching-specific evidence stats should be added.

6. **CTA heading colour is `var(--white)` instead of `var(--lime-green)`** (`functional-coaching.css` line 814)
   `design.md` patterns and other lander pages use `var(--lime-green)` for CTA section headings. This is `var(--white)` — off-brand for the CTA block.

7. **No section dividers** — Sections run directly into each other with no visual rhythm separator. `ayurveda.html` uses `.ay-divider` gradient rules between sections. Adding thin lime-tinted horizontal rules between key sections would improve visual pacing.

8. **`.fc-hero-img-bw` missing `filter: grayscale(100%)`** (`functional-coaching.css` line 138–142)
   The base image has no grayscale filter applied. Without it, the dual-image hover pattern is meaningless — both images appear identical. Must add `filter: grayscale(100%)`.

- [ ] **Step 1.2: Prioritise issues**

| Priority | Issue | Action |
|---|---|---|
| 🔴 Critical | Hero opacity reveal → must be mask-position | Fix CSS |
| 🔴 Critical | `max-width: 960px` on hero wrapper | Remove |
| 🔴 Critical | `.fc-hero-img-bw` missing `filter: grayscale(100%)` | Add to CSS |
| 🔴 Critical | `.fc-hero-img-color` missing `height: 100%` + `object-fit: cover` | Add to CSS |
| 🔴 Critical | `border-radius` on color overlay image | Remove |
| 🟡 Important | CTA heading colour to `var(--lime-green)` | Update CSS |
| 🟡 Important | Add stats strip after hero | Add HTML + CSS |
| 🟢 Enhancement | Add section dividers | Add to HTML |

---

## Task 2: Implement CSS Fixes — Hero Image Reveal

**Files:**
- Modify: `functional-coaching.css` (hero section, lines 128–157)

- [ ] **Step 2.1: Replace hero image CSS with canonical mask-position pattern**

In `functional-coaching.css`, replace the entire hero dual-image block (lines 128–157) with:

```css
/* Hero dual-image — mask-position slide reveal (matches design.md section 5.10) */
.fc-hero-image-wrapper {
  position: relative;
  /* NO max-width — .fc-hero-container (1300px) acts as natural constraint per design.md */
  margin: 0 auto;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 24px 80px rgba(0, 0, 0, 0.5);
}

.fc-hero-image-wrapper .fc-hero-img-bw {
  width: 100%;
  display: block;
  filter: grayscale(100%);
}

.fc-hero-image-wrapper .fc-hero-img-color {
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

.fc-hero-image-wrapper:hover .fc-hero-img-color {
  -webkit-mask-position: 0 0;
  mask-position: 0 0;
}
```

- [ ] **Step 2.2: Commit CSS hero fix**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add functional-coaching.css
git commit -m "fix: replace opacity reveal with canonical mask-position slide reveal on functional-coaching hero"
```

---

## Task 3: Implement CSS Fixes — CTA Heading Colour

**Files:**
- Modify: `functional-coaching.css` (CTA section, around line 810–820)

- [ ] **Step 3.1: Update CTA heading to lime-green**

In `functional-coaching.css`, change `.fc-cta-heading` color from `var(--white)` to `var(--lime-green)`:

```css
.fc-cta-heading {
  ...
  color: var(--lime-green);  /* was var(--white) */
  ...
}
```

- [ ] **Step 3.2: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add functional-coaching.css
git commit -m "fix: update fc-cta-heading to lime-green for brand consistency"
```

---

## Task 4: Add Stats Strip (Authority Signal) After Hero

**Files:**
- Modify: `functional-coaching.html` (insert after hero section closing `</section>`)
- Modify: `functional-coaching.css` (add stats strip styles)

- [ ] **Step 4.1: Add stats strip HTML**

In `functional-coaching.html`, after the closing `</section>` of `.fc-hero` (after line 91), insert:

```html
<!-- ══════════════════════════════════════════════════════
     STATS STRIP — Authority signal
     ══════════════════════════════════════════════════════ -->
<div class="fc-stats-strip">
  <div class="fc-stats-inner">
    <div class="fc-stat">
      <span class="fc-stat__value">104</span>
      <span class="fc-stat__label">Randomized Trials — 2023 Meta-Analysis</span>
    </div>
    <div class="fc-stat">
      <span class="fc-stat__value">168K+</span>
      <span class="fc-stat__label">Study Participants Covered</span>
    </div>
    <div class="fc-stat">
      <span class="fc-stat__value">6</span>
      <span class="fc-stat__label">Coaching Protocol Pillars</span>
    </div>
    <div class="fc-stat">
      <span class="fc-stat__value">Root</span>
      <span class="fc-stat__label">Cause — Not Symptom — Focused</span>
    </div>
  </div>
</div>
```

- [ ] **Step 4.2: Add stats strip CSS**

In `functional-coaching.css`, after the hero section block and before the definition section block, add:

```css
/* ════════════════════════════════════════════════════════
   STATS STRIP
   ════════════════════════════════════════════════════════ */
.fc-stats-strip {
  background: rgba(196, 255, 73, 0.06);
  border-top: 1px solid rgba(196, 255, 73, 0.18);
  border-bottom: 1px solid rgba(196, 255, 73, 0.18);
  padding: 52px 20px;
}

.fc-stats-inner {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
}

.fc-stat {
  text-align: center;
  padding: 0 32px;
  position: relative;
}

.fc-stat + .fc-stat::before {
  content: '';
  position: absolute;
  left: 0; top: 15%; height: 70%; width: 1px;
  background: rgba(196, 255, 73, 0.15);
}

.fc-stat__value {
  display: block;
  font-family: 'Poppins', sans-serif;
  font-size: clamp(1.8rem, 3.5vw, 2.8rem);
  font-weight: 700;
  color: var(--lime-green);
  line-height: 1.1;
  margin-bottom: 8px;
}

.fc-stat__label {
  display: block;
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--white-800);
  line-height: 1.4;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

@media (max-width: 900px) {
  .fc-stats-inner { grid-template-columns: repeat(2, 1fr); gap: 40px 0; }
  .fc-stat + .fc-stat::before { display: none; }
  .fc-stat:nth-child(odd) { border-right: 1px solid rgba(196,255,73,0.12); }
  .fc-stat:nth-child(n+3) { border-top: 1px solid rgba(196,255,73,0.12); padding-top: 40px; }
}

@media (max-width: 480px) {
  .fc-stats-strip { padding: 36px 16px; }
  .fc-stat { padding: 0 16px; }
  .fc-stat__value { font-size: clamp(1.4rem, 6vw, 2rem); }
}
```

- [ ] **Step 4.3: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add functional-coaching.html functional-coaching.css
git commit -m "feat: add stats strip authority signal below hero on functional-coaching page"
```

---

## Task 5: Add Section Dividers

**Files:**
- Modify: `functional-coaching.html` (between major sections)
- Modify: `functional-coaching.css` (divider styles)

- [ ] **Step 5.1: Add divider HTML**

In `functional-coaching.html`, insert a `<hr class="fc-divider">` element between these section pairs:
- After the stats strip `</div>`, before `<!-- SECTION 2 — DEFINITION -->`
- After section 3 pillars `</section>`, before `<!-- SECTION 4 — CLIENT PROFILES -->`
- After section 4 profiles `</section>`, before `<!-- SECTION 5 — SECTION IMAGE -->`
- After section 6 journey `</section>`, before `<!-- SECTION 7 — OUTCOME STATEMENTS -->`
- After section 8 citations `</section>`, before `<!-- SECTION 9 — BOOKING CTA -->`

- [ ] **Step 5.2: Add divider CSS**

In `functional-coaching.css`, add before the global responsive helpers block:

```css
/* ════════════════════════════════════════════════════════
   SECTION DIVIDER
   ════════════════════════════════════════════════════════ */
.fc-divider {
  border: none;
  height: 1px;
  background: linear-gradient(
    to right,
    transparent 0%,
    rgba(196, 255, 73, 0.18) 20%,
    rgba(196, 255, 73, 0.18) 80%,
    transparent 100%
  );
  margin: 0;
}
```

- [ ] **Step 5.3: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add functional-coaching.html functional-coaching.css
git commit -m "feat: add section dividers between major sections on functional-coaching page"
```

---

## Task 6: Visual Verification

**No file changes — verification only.**

- [ ] **Step 6.1: Start preview server**

Use `preview_start` MCP tool to serve the `odin lab landers` directory.

- [ ] **Step 6.2: Screenshot the page**

Use `preview_screenshot` to capture full-page view of `functional-coaching.html`.

- [ ] **Step 6.3: Verify checklist**

Check screenshot against these criteria:
- [ ] Hero image shows grayscale photo by default (not color)
- [ ] Stats strip visible below hero with 4 lime-green stat values
- [ ] CTA section heading is lime-green (not white)
- [ ] Section dividers visible between major sections
- [ ] No obvious layout breaks on desktop view

- [ ] **Step 6.4: Hover test on hero**

Use `preview_eval` to trigger a hover event on `.fc-hero-image-wrapper` and then `preview_screenshot` to confirm color reveal appears as a mask slide (not opacity pop):

```js
document.querySelector('.fc-hero-image-wrapper').dispatchEvent(new MouseEvent('mouseenter', { bubbles: true }));
```

- [ ] **Step 6.5: Mobile responsive check**

Use `preview_resize` to set viewport to 375px width. Take `preview_screenshot`. Verify:
- [ ] Stats strip collapses to 2×2 grid
- [ ] Pillars grid collapses to single column
- [ ] Profile cards stack vertically
- [ ] No horizontal overflow

If any issues found: read the relevant CSS block, diagnose, fix, re-screenshot. Do not claim completion until all checks pass.

---

## Summary of Changes

| File | Changes |
|---|---|
| `functional-coaching.html` | Stats strip HTML added, divider `<hr>` elements added between sections |
| `functional-coaching.css` | Hero reveal → mask-position (critical fix), grayscale filter added to BW image, color overlay height/object-fit corrected, hero wrapper max-width removed, border-radius removed from color overlay, stats strip styles added, CTA heading → lime-green, divider styles added |

## Verification Gate

Before claiming completion, ensure:
1. Hero image base is grayscale by default
2. Hero hover triggers mask-position slide reveal (not opacity)
3. Stats strip shows below hero with 4 lime stats
4. CTA heading is lime-green
5. Section dividers present between major content blocks
6. Mobile layout correct at 375px
7. No regressions — all other sections intact
