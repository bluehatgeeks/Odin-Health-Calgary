# Odin Lab — Design Requirements Document

> **Reference this document before creating any new design element.** It defines the canonical visual language, component patterns, and conventions used across all Odin Lab lander pages.

---

## 1. Brand Identity

**Practice tagline:** "We Do Not Practice Medicine. We Practice Health."
**Tone:** Clinical authority + approachable partnership. No hype. No quick-fix language.
**Voice:** Direct, systems-thinking, data-informed.

---

## 2. Color Palette

All colors are defined as CSS variables in `odin-shared.css` and must be referenced via `var(--*)`.

| Token | Hex | Usage |
|---|---|---|
| `--dark-green` | `#1a3a1a` | Page background, nav, cards, footer |
| `--lime-green` | `#c4ff49` | Primary accent: CTAs, highlights, hover states, icons |
| `--lime` | `#c4ff49` | Alias for `--lime-green` |
| `--white` | `#ffffff` | Body text, headings on dark backgrounds |
| `--white-800` | `rgba(255,255,255,0.8)` | Secondary text |
| `--white-500` | `rgba(255,255,255,0.5)` | Tertiary / muted text |

**Additional derived values used inline:**
- `rgba(196, 255, 73, 0.08–0.15)` — subtle lime tint backgrounds
- `rgba(196, 255, 73, 0.25–0.4)` — lime-tinted borders
- `rgba(255,255,255,0.04–0.06)` — card surface backgrounds
- `rgba(255,255,255,0.07–0.1)` — card/item border strokes
- `rgba(0,0,0,0.5)` — modal overlay

**Do not introduce new brand colors.** Extend only with opacity variants of the palette above.

---

## 3. Typography

### Font Families
- **Primary:** `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif` (system stack, defined in `--font-family`)
- **Display (therapies pages):** `Poppins` — weights 200–700, used for headings
- **Body (therapies pages):** `Plus Jakarta Sans` — weights 200–800, used for body copy

### Type Scale

| Class / Element | Size | Weight | Notes |
|---|---|---|---|
| `.hero-slogan` | `clamp(1.25rem, 3vw, 2.2rem)` | 900 | `line-height: 1.1`, `letter-spacing: 0.02em`, centered |
| `.large-heading` / `h1` | ~2.5–3rem | 700 | Full-width within `max-width: 800px` container |
| `.medium-heading` / `h2` | ~1.8–2.2rem | 700 | Section titles |
| `.h4-heading` / `h4` | `1.4rem` (inline) | 700 | Card titles, step headings |
| `.sub-text` | `1.1–1.4rem` | 400–600 | Body paragraphs under headings |
| `.lead` | ~1.2rem | 600 | Section intro lines |
| `p.faq-answer` | ~1rem | 400 | FAQ body copy |
| `.mega-col-heading` | `0.68rem` | 700 | `letter-spacing: 0.14em`, `text-transform: uppercase` |
| `.mega-item-title` | `0.95rem` | 600 | Nav mega menu items |
| `.mega-item-sub` | `0.78rem` | 400 | Nav mega menu subtitles |

**Color rules:** Headings use `var(--white)`. Accent headings (step labels, card titles) use `var(--lime-green)`. Muted copy uses `var(--white-800)` or `var(--white-500)`.

---

## 4. Spacing & Layout

### Container Widths
| Context | Max-width |
|---|---|
| Default `.container` / `.content-wrapper` | `1300px` |
| `.metabolism-section`, `.client-journey-section`, `.about-us-section` | `900px` |
| `.symptoms-section` | `950px` |
| `.faq-section` | `800px` |
| Hero text blocks | `800px` |
| Sub-text paragraphs | `600–700px` |

All containers: `margin: 0 auto`, `padding: 0 20px`.

### Section Spacing
- Standard section: `padding-top: 60px; padding-bottom: 60px`
- Hero section: `padding-top: 90px; padding-bottom: 60px`
- Main with nav offset: `padding-top: 80px` on `<main>`
- Hero inner top: `padding-top: 30px` on first `.section`

### Common Internal Spacing
- Between hero slogan and hero image: `margin-bottom: 20px`
- Between section heading and body: `margin-top: 20–30px`
- Between CTA buttons: `margin-top: 15px`, `margin-left: 10px`
- Card gap: `20–25px`

---

## 5. Component Library

### 5.1 Buttons

#### `.btn-primary`
```
background: linear-gradient(135deg, var(--lime-green) 0%, #a8e64a 100%)
color: var(--dark-green)
padding: 15px 30px
border-radius: 15px
font-weight: bold
font-size: 1.2rem
transition: transform 0.2s ease
hover: translateY(-2px)
```

#### `.btn` / `.btn-outline`
Bordered secondary button. Used alongside `.btn-primary` for secondary actions (e.g., "Take the Assessment").

#### `.btn-first-time` / `.btn-follow-up`
Used exclusively inside the booking modal. Link to external LeadConnector booking URLs.

**Rule:** All booking CTAs must carry the class `.booking-trigger` to hook into the shared booking modal JS.

---

### 5.2 Navigation (Shared Component)

Loaded dynamically via `odinnav.html` from `raw.githubusercontent.com` with `cache: 'no-store'`.

- Fixed header with `--dark-green` background
- Logo left, nav links center/right, CTA button far right
- Hover: nav links turn `--lime-green`
- Mobile breakpoint: `≤900px` — slide-out panel (`min(320px, 85vw)`)
- Hamburger toggle: 3-line → X animation on `aria-expanded="true"`
- **Mega menu** (`.mega-menu`): drops below header, `--dark-green` bg, lime border-top `2px rgba(196,255,73,0.25)`, animated opacity + translateY
  - `.mega-item`: `border-radius: 12px`, hover lifts `translateY(-2px)`, lime tint on hover
  - `.mega-item-icon`: 42×42px, lime tinted background, `border-radius: 10px`
- **About Us (`#about-us-section`):** `odinnav.html` includes a small script that, when the current document contains `#about-us-section` (main lander only), rewrites those nav `href`s to `location.origin + pathname + search + #about-us-section` so the in-page reveal/scroll handler matches the host (localhost, www vs apex, embedded funnel paths). Pages without that section keep the canonical `https://odinhealthlab.ca/#about-us-section` link for a full navigation home.

**Do not recreate nav inline.** Always use the shared component loader pattern.

---

### 5.3 Footer (Shared Component)

Loaded dynamically via `odinfooter.html` from `raw.githubusercontent.com` with `cache: 'no-store'`.

Append `?v=N` to the footer URL and **increment N whenever `odinfooter.html` changes** (GitHub Raw and edge caches may otherwise serve an older file for several minutes even with `no-store`).

**Do not recreate footer inline.** Always use the shared component loader pattern.

---

### 5.4 Cards

#### Therapy / Feature Card (`.therapy-card`)
- Dark semi-transparent surface: `rgba(255,255,255,0.04–0.06)`
- Border: `1px solid rgba(255,255,255,0.07)`
- Border-radius: `12–16px`
- Padding: `20–32px`
- Card headings: `var(--lime-green)`, `1.4rem`, `font-weight: 700`
- Card body: `var(--white)`, `1.1rem`

#### Profile Cards (`.profile-card__image` + `.profile-card__content`)
Used in "You Feel Functional — But Not Optimal" section. Grid of 3 columns. Image on top, content below.

#### Founder Card (`.about-us-founder-card`)
```
background: linear-gradient(135deg, rgba(196,255,73,0.08) 0%, rgba(0,0,0,0.2) 100%)
border: 1px solid rgba(196,255,73,0.25)
border-radius: 16px
padding: 32px
```
Portrait image: absolute-positioned left (240px wide), grayscale filter, with dark gradient overlay from 40% bottom. Content offset: `margin-left: 268px`.

---

### 5.5 Tag / Pill Lists

#### Metabolism / Symptom Tags (`.metabolism-tags`, `.symptoms-tags`)
- `list-style: none`
- Each `<li>` rendered as a pill/badge
- Used for feature lists within cards

#### Modality Badges (`.about-us-modalities span`)
```
background: rgba(196, 255, 73, 0.15)
border: 1px solid rgba(196, 255, 73, 0.4)
color: var(--white)
padding: 8px 14px
border-radius: 20px
font-size: 0.95rem
font-weight: 500
```

#### Authority Bar (`.authority-bar`)
Horizontal row of icon + text pairs. Uses inline SVG icons (24×24), stroke-based, `currentColor`. Items spaced with flexbox/grid.

---

### 5.6 Grid Layouts

| Pattern | CSS |
|---|---|
| 2-column framework steps | `grid-template-columns: repeat(2, 1fr); gap: 20px` |
| 3-column profile / testimonials | `grid-template-columns: repeat(3, 1fr); gap: 25px` |
| Client journey checklist | `.client-journey-grid` — checklist with `✓` check icons |
| Core feature grid | `.core-feature-grid` — multi-column card layout |
| Metabolism cards | `.metabolism-cards` — 2 columns (stable vs unstable) |

**Breakpoint:** All multi-column grids collapse to single column at `≤768px`.

---

### 5.7 Booking Modal

**ID:** `#booking-modal-overlay`

```
position: fixed, inset: 0
background: rgba(0,0,0,0.5)
display: none → .is-visible adds display:flex
z-index: above nav
```

Modal inner (`.booking-modal`):
- Dark green background, `border-radius: 16px`, centered
- Close button `#booking-modal-close`: `&times;`, top-right
- Heading `#booking-modal-title`
- Two CTA links: `.btn-first-time` (first-time intake) + `.btn-follow-up` (follow-up)
- External booking URLs: `https://api.leadconnectorhq.com/widget/bookings/odin-labs-*`

**Trigger:** Any element with class `.booking-trigger` opens the modal via shared JS delegation.

**Keyboard:** `Escape` closes. Body overflow locked while open.

---

### 5.8 Metabolic Survey Panel

**ID:** `#metabolic-survey-panel` / class `.metabolic-survey-panel`

Progressive 6-question assessment. Branching on biological sex (male/female question sets). Shows outcome card with result key and CTA.

Key sub-elements:
- `.metabolic-survey-progress-bar` — visual step indicator
- `.metabolic-survey-question[data-id]` — individual question screens
- `.metabolic-survey-option` — choice buttons, `.selected` state
- `.metabolic-survey-outcome` — result screen (hidden until complete)
- `.metabolic-survey-outcome-badge`, `.metabolic-survey-outcome-title`, `.metabolic-survey-outcome-blocks`
- `.metabolic-survey-nav` — Back / Next buttons

Outcome keys: `hpa`, `insulin`, `low-testosterone`, `estrogen-dominance`, `low-androgens`, `mitochondrial`, `healthy`.

---

### 5.9 FAQ Accordion

Class `.faq-item` uses native `<details>/<summary>`. Hover triggers open; mouseleave triggers close. Only one item open at a time (JS collapses others on `mouseenter`).

```
.faq-question — summary label
.faq-answer — body paragraph
.faq-section .container — max-width: 800px
```

---

### 5.10 Hero Image

Class pattern: `.hero-image-wrapper` containing two `<img>` tags:
1. `.hero-image.hero-image-bw` — grayscale base image (`filter: grayscale(100%)`)
2. `.hero-image.hero-image-color` — color overlay, `aria-hidden="true"`

The dual-image pattern enables a **B&W → colour gradual slide reveal** on hover using a CSS mask-position animation — **not a simple opacity toggle**.

> **CRITICAL — Three rules that must all be followed:**
> 1. **Same source file for both layers.** Both `<img>` tags point to the same colour image. The BW layer uses `filter: grayscale(100%)` in CSS — never a separately generated grayscale file. Different files cause pixel mismatch at the mask boundary.
> 2. **No `border-radius` on the colour overlay image.** The wrapper's `overflow: hidden` handles corner clipping. Adding `border-radius` to the absolutely-positioned colour image creates independent clipping that interferes with the mask gradient edge.
> 3. **No `max-width` constraint on the wrapper.** The image must stretch to the full container width (matching `odinlabcalgary.html`'s ~1256px). Constraining the wrapper (e.g. `max-width: 1000px`) makes the mask gradient stops appear proportionally earlier in the wipe — the colour bleeds in too fast and the transition character differs from the main lander. Always let the wrapper fill the container naturally.

**Canonical implementation (must match `odinlabcalgary.html`):**
```css
.hero-image-color {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  object-fit: cover;
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

.hero-image-wrapper:hover .hero-image-color {
  -webkit-mask-position: 0 0;
  mask-position: 0 0;
}
```

Do not use a single image in the hero. Do not implement the reveal as `opacity: 0 → 1`.

---

### 5.11 Marma-Therapy Page Components (.mt- prefix)

These components are used on the marma-therapy lander and follow the standard design system conventions.

#### Zone Card (.mt-zone-card)
Five-column flex grid on desktop, collapses to single column at ≤768px. Semi-transparent white surface (`rgba(255,255,255,0.04)`), lime-green top border accent, hover lift effect. Used to present body zones with Sanskrit point names, functions, and therapeutic applications.

#### Frequency Block (.mt-freq-block)
Three-column grid on desktop, single column at ≤900px. Centered content with large lime-green frequency value, title, and description. Used to present clinically studied vibroacoustic frequencies.

#### Metaphor Block (.mt-metaphor-block)
Two-column grid. Icon container (60×60px, lime-tinted background), tag label, title, and description. Used to present the "Map + Signal" combination rationale.

#### Citation Card (.mt-citation-card)
Three-column grid, collapses to single column at ≤900px. Lime-green left border accent (3px), semi-transparent surface, hover lift. Text hierarchy: author → journal → finding. Used for peer-reviewed research citations.

#### Fit Card (.mt-fit-card)
Three-column grid, collapses to single column at ≤900px. Differentiated by top border color: lime-green (well-suited), white-40 (info), orange-60 (caution). Used in "Is This Right For You?" section.

#### Credibility Strip (.mt-credibility-strip)
Full-width strip with lime-green tinted background and border. Used to surface research credibility signal early in the page flow.

#### Mid-Page CTA (.mt-mid-cta)
Full-width centered block with subtle lime-green border top/bottom. Contains italic teaser text + booking-trigger button. Placed after high-engagement sections to capture mid-funnel conversions.

---

## 6. Sections — Page Anatomy

### odinlabcalgary.html (Main Calgary Lander)
1. Hero + slogan + hero image + CTAs + authority bar
2. Metabolism explainer (stable vs unstable cards)
3. Symptoms section (2-column tag lists)
4. Profile types (3-column grid: shift workers, executives, new mothers)
5. Odin Labs Systems Optimisation Framework™ (2×2 step grid)
6. Client journey checklist
7. Results / outcomes (3-column testimonial quotes)
8. FAQ accordion
9. About Us section (hidden by default, toggled by link)
10. Final CTA section

### odintherapiestemplate.html (Therapy-Specific Lander)
1. Hero + slogan
2. Therapy benefits heading
3. Core feature cards grid (colored variants: lime, purple, white-smoke)
4. How It Works section
5. Testimonial slider (Webflow slider component)
6. Science / peer-reviewed research citations
7. Booking CTA

---

## 7. Animation & Interaction Conventions

| Pattern | Spec |
|---|---|
| Button hover lift | `transform: translateY(-2px)`, `transition: 0.2s ease` |
| Card hover lift | Same as button hover |
| Mega menu open | `opacity 0→1`, `translateY(-10px → 0)`, `0.25s ease` |
| Nav slide-out (mobile) | `translateX(100% → 0)`, `0.3s ease` |
| Survey question transition | Slide in/out, `350ms` delay on direction classes `.leaving` / `.leaving-back` |
| Modal overlay | Fade in via `.is-visible` class |
| FAQ accordion | Native `<details>` open/close; hover-driven via JS |

---

## 8. Accessibility Requirements

- All interactive elements must have visible focus states
- Modals must use `aria-hidden`, `aria-labelledby`, `role="dialog"`
- Booking modal locks `body overflow: hidden` when open; restores on close
- Survey panel: `role="radiogroup"`, `aria-checked` on option buttons, `aria-expanded` on trigger
- Nav toggle: `aria-expanded` on hamburger button; `aria-hidden` on overlay
- `Escape` key closes all overlays (modal, survey panel)
- Images: meaningful `alt` text; decorative duplicates use `aria-hidden="true"`

---

## 9. External Services & CDN

| Resource | URL Pattern |
|---|---|
| Shared CSS | `https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/odin-shared.css?v=N` |
| Page CSS | `https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/{page}.css?v=N` |
| Nav component | `https://raw.githubusercontent.com/bluehatgeeks/Odin-Health-Calgary/master/odinnav.html` |
| Footer component | `https://raw.githubusercontent.com/bluehatgeeks/Odin-Health-Calgary/master/odinfooter.html?v=N` (increment `N` on footer edits) |
| Media / Images | `https://assets.cdn.filesafe.space/Q6uTvwNHOg3F0JyLXiUV/media/` |
| Booking system | `https://api.leadconnectorhq.com/widget/bookings/odin-labs-*` |

Nav and footer fetches use `cache: 'no-store'`. Still increment **`odinfooter.html?v=N`** on every footer edit so clients bypass stale cached responses.

Version query strings (`?v=N`) must be incremented when CSS files are updated.

---

## 10. File Structure

```
odin lab landers/
├── odin-shared.css            # Global variables, nav, footer, shared components
├── odinlabcalgary.css         # Calgary main page styles
├── odinlabcalgary.html        # Calgary main lander
├── odintherapiestemplate.css  # Therapy page styles
├── odintherapiestemplate.html # Therapy page template
├── odinnav.html               # Shared nav component (loaded via fetch)
├── odinfooter.html            # Shared footer component (loaded via fetch)
├── design.md                  # ← This document
└── CLAUDE.md                  # AI assistant instructions
```

---

## 11. Rules for New Design Elements

1. **Check this document first.** Do not introduce colors, fonts, or spacing values not listed here.
2. **Use CSS variables.** Never hardcode color hex values — always use `var(--lime-green)` etc.
3. **New page-level CSS** goes in a page-specific `.css` file loaded from the CDN repo. Do not write page styles into `odin-shared.css`.
4. **Shared components** (nav, footer) are never duplicated inline. Always use the component loader pattern.
5. **Buttons** that trigger booking must always use class `.booking-trigger`.
6. **Cards** follow the semi-transparent dark surface + lime-accented border pattern.
7. **New sections** follow the `padding: 60px 0` + `.container` + max-width constraint pattern.
8. **Responsive:** All multi-column layouts must collapse gracefully at `≤768px`.
9. **Typography:** Add no new font families. Use system stack or Poppins/Plus Jakarta Sans as appropriate to the page.
10. **Icons:** Use inline SVG, stroke-based, `currentColor`, 24×24 viewport.

---

## 12. GoHighLevel (GHL) Deployment — CSS & Custom Code

**The live site is hosted on GoHighLevel (HighLevel).** GHL does not serve static files — it cannot resolve relative CSS paths like `functional-health.css?v=1`. All stylesheets and scripts must use **full absolute jsDelivr CDN URLs**.

### How page-specific CSS gets onto the live page

Each therapy/lander page uses a GHL **Custom Code element** (in the page head) to load its CSS. The element must contain:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/functional-health.css?v=N">
```

Replace `functional-health` with the page slug and increment `?v=N` on every CSS update to bust the CDN cache.

### Workflow for updating live page styles

1. Edit the local `.css` file (e.g. `functional-health.css`)
2. Commit and push to `bluehatgeeks/Odin-Health-Calgary` on GitHub (`master` branch)
3. Purge jsDelivr cache: `https://purge.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/functional-health.css`
4. In GHL page editor → Custom Code (head) → bump the `?v=N` query string by 1
5. Save + Publish the GHL page

### Important: relative paths always 404 on GHL

GHL serves pages from `highlevel-backend.appspot.com` internally. Any relative path (`href="functional-health.css"`) resolves against that domain and returns a 404. **Always use the full `https://cdn.jsdelivr.net/...` URL.**

### CSS version tracking — current versions

| File | Current `?v=` | Last updated |
|---|---|---|
| `odin-shared.css` | `?v=6` | — |
| `functional-health.css` | `?v=3` | 2026-03-25 |
| `ayurveda.css` | `?v=4` | — |
| `nutritional-supplementation.css` | `?v=9` | 2026-04-07 |

**Nutritional lander:** Stats-strip disclaimer `.ns-stats-footnote`; pillar blurbs under contrast block use `.ns-pillar-copy` inside `.ns-arsenal-card` (no product-name pills).

**When you bump `?v=N`:** update BOTH the local `.html` file `<link>` tag AND the GHL Custom Code element. They must stay in sync.

### Shared CSS (`odin-shared.css`)

`odin-shared.css` is already loaded via full CDN URL on all pages. Do not change this pattern. Current version: `?v=6`.
