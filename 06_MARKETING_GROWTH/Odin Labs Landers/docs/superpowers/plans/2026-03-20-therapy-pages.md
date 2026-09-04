# Therapy Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
> **Phases 1 & 2 (research + image gen) are fully parallelizable** — dispatch all 6 research agents and all 6 image agents concurrently. Use superpowers:dispatching-parallel-agents.

**Goal:** Build 6 therapy-specific landing pages for Odin Lab Calgary, each with unique layouts, science-backed content, and AI-generated imagery, all conforming to the established design system.

**Architecture:** Each page follows the `odintherapiestemplate.html` shell (shared nav/footer loader, hero slogan, large heading block, booking modal) but uses a distinct section arrangement and layout concept. Each page gets its own CSS file hosted alongside the others. Content is research-backed from peer-reviewed sources. Images are generated via Nano Banana matching the dual-image hero style from the template.

**Tech Stack:** HTML5, CSS3 (page-scoped files), vanilla JS (shared booking modal + nav/footer loader), Nano Banana (AI image generation), web research for content.

---

## Reference Files

| File | Purpose |
|---|---|
| `odintherapiestemplate.html` | Shell structure to replicate (nav loader, footer loader, hero slogan, booking modal JS) |
| `odintherapiestemplate.css` | CSS patterns to follow (Webflow base, `.hero-slogan`, `.core-feature-grid`, `.section`, etc.) |
| `odin-shared.css` | Global variables: `--dark-green`, `--lime-green`, `--white`, `--white-800`, `--white-500` |
| `design.md` | Single source of truth — read before every HTML/CSS decision |
| `odinnav.html` | Shared nav — loaded via fetch, never inline |
| `odinfooter.html` | Shared footer — loaded via fetch, never inline |

---

## Pages + Unique Layout Concepts

| Page | File | Unique Layout Signature |
|---|---|---|
| Hydrogen Inhalation Therapy | `hydrogen-therapy.html` | Molecule stat-strip → benefit cards (lime/purple/smoke) → How It Works numbered steps → Research citations grid → Booking CTA |
| Functional Health & Medicine | `functional-health.html` | Conventional vs Functional split comparison → Root Cause Diagnostic Steps → Conditions Addressed tag cloud → FAQ accordion → Booking CTA |
| Functional Health Coaching | `functional-coaching.html` | Coaching Pillars (icon + text, 3-col) → Transformation Journey timeline → Who This Is For profile cards → Outcome testimonial block → Booking CTA |
| Nutritional Supplementation & Herbology | `nutritional-supplementation.html` | Botanical Spotlight cards (large visual, name, action) → 3-Phase Protocol steps → Key Compounds list → Research citations → Booking CTA |
| Marma Therapy + Tuning Forks | `marma-therapy.html` | What Is Marma intro split → Energy Point cards (body zones) → Tuning Fork Frequency science strip → Session Experience walkthrough steps → Booking CTA |
| Ayurveda | `ayurveda.html` | Dosha Types 3-column cards → Ayurvedic Principles timeline → Modern Science validation citations → Seasonal Protocol cards → Booking CTA |

---

## File Structure — Created

```
odin lab landers/
├── hydrogen-therapy.html          ← NEW
├── hydrogen-therapy.css           ← NEW
├── functional-health.html         ← NEW
├── functional-health.css          ← NEW
├── functional-coaching.html       ← NEW
├── functional-coaching.css        ← NEW
├── nutritional-supplementation.html ← NEW
├── nutritional-supplementation.css  ← NEW
├── marma-therapy.html             ← NEW
├── marma-therapy.css              ← NEW
├── ayurveda.html                  ← NEW
├── ayurveda.css                   ← NEW
└── docs/superpowers/plans/2026-03-20-therapy-pages.md ← THIS FILE
```

---

## Design Rules (enforce on every page)

1. No hardcoded hex values — always `var(--lime-green)`, `var(--dark-green)`, `var(--white)`, etc.
2. No new colors, fonts, or brand tokens not in `design.md`
3. Nav and footer are NEVER inline — always the fetch loader pattern
4. All booking CTAs carry class `.booking-trigger`
5. All multi-column layouts collapse at `≤768px`
6. Increment CSS `?v=N` query string when CDN-hosted — for local files use `?v=1` initially
7. Hero must include `.hero-slogan` with exact text: *"We Do Not Practice Medicine. We Practice Health."*
8. Large heading + subheading block immediately follows hero, styled with `.h1-heading` and `.paragraph`
9. Inline SVG icons only — stroke-based, `currentColor`, 24×24 viewBox
10. Cards: semi-transparent dark surface + lime-accented heading

---

## HTML Shell Pattern (used on every page)

Every page MUST open with this exact boilerplate — adapt title/description/CSS filename only:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>[THERAPY NAME] | Odin Lab Calgary</title>
  <meta name="description" content="[SEO description]" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&family=Plus+Jakarta+Sans:wght@200;300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/odin-shared.css?v=6" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/odintherapiestemplate.css?v=1" />
  <link rel="stylesheet" href="[PAGE].css?v=1" />
  <style>
    /* hero-slogan + section spacing overrides — same as template */
    .hero-slogan{color:#c4ff49!important;opacity:0.5!important;font-size:clamp(1.25rem,3vw,2.2rem)!important;font-weight:900!important;line-height:1.1!important;letter-spacing:0.02em!important;margin:25px 0 15px 0!important;text-align:center!important;width:100%!important;white-space:nowrap!important;max-width:100%!important;}
    @media(max-width:768px){.hero-slogan{white-space:normal!important;font-size:clamp(1rem,4vw,2rem)!important;}}
    .hero-main-section{padding-top:90px!important;padding-bottom:60px!important;}
    section.banner-section{padding-bottom:0!important;}
    section.section{padding-top:60px!important;padding-bottom:60px!important;}
  </style>
</head>
<body>
<main style="padding-top:80px;">

  <!-- HERO SECTION -->
  <div class="hero-main-section w-layout-blockcontainer container">
    <p class="hero-slogan">We Do Not Practice Medicine. We Practice Health.</p>
    <h1 class="h1-heading max-width text-center">[PAGE HEADING]</h1>
    <p class="paragraph center-paragraph text-center">[SUBHEADING — 2 sentences max]</p>
    <div class="button-div">
      <a href="#" class="booking-trigger common-button">Book a Consultation</a>
    </div>
    <!-- Hero image (dual-image pattern) -->
    <div class="hero-image-wrapper" style="margin-top:40px;">
      <img src="[NANOB_BW_URL]" alt="[THERAPY] hero" class="hero-image hero-image-bw" />
      <img src="[NANOB_COLOR_URL]" alt="" class="hero-image hero-image-color" aria-hidden="true" />
    </div>
  </div>

  <!-- UNIQUE SECTIONS GO HERE -->

  <!-- BOOKING CTA (always last section before footer) -->
  <section class="section">
    <div class="w-layout-blockcontainer container text-center">
      <div class="sub-heading-div"><span class="sub-heading-text">Ready to Begin?</span></div>
      <h2 class="h3-heading center-heading">[CTA HEADING]</h2>
      <p class="paragraph center-paragraph">[CTA SUBTEXT]</p>
      <div class="button-div" style="margin-top:30px;">
        <a href="#" class="booking-trigger common-button">Book a Consultation</a>
        <a href="/odinlabcalgary.html" class="common-button button-border">Learn More</a>
      </div>
    </div>
  </section>

</main>

<!-- BOOKING MODAL -->
<div id="booking-modal-overlay" role="dialog" aria-modal="true" aria-labelledby="booking-modal-title" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,0.5);z-index:9999;align-items:center;justify-content:center;">
  <div class="booking-modal" style="background:var(--dark-green);border-radius:16px;padding:40px;max-width:480px;width:90%;position:relative;">
    <button id="booking-modal-close" aria-label="Close" style="position:absolute;top:16px;right:20px;background:none;border:none;color:var(--white);font-size:1.8rem;cursor:pointer;">&times;</button>
    <h2 id="booking-modal-title" style="color:var(--white);margin-bottom:24px;">Book Your Session</h2>
    <a href="https://api.leadconnectorhq.com/widget/bookings/odin-labs-intake" class="btn-first-time common-button" style="display:block;margin-bottom:12px;text-align:center;">First Time? Book Intake</a>
    <a href="https://api.leadconnectorhq.com/widget/bookings/odin-labs-followup" class="btn-follow-up common-button button-border" style="display:block;text-align:center;">Follow-Up Appointment</a>
  </div>
</div>

<script>
  (function(){
    function execScripts(root){root.querySelectorAll('script').forEach(function(s){var n=document.createElement('script');Array.from(s.attributes).forEach(function(a){n.setAttribute(a.name,a.value)});n.textContent=s.textContent;s.parentNode.replaceChild(n,s)});}
    var navRoot=document.createElement('div');navRoot.id='odin-nav-root';document.body.insertBefore(navRoot,document.body.firstChild);
    fetch('https://raw.githubusercontent.com/bluehatgeeks/Odin-Health-Calgary/master/odinnav.html',{cache:'no-store'}).then(function(r){return r.text()}).then(function(html){navRoot.innerHTML=html;execScripts(navRoot)});
    var footerRoot=document.createElement('div');footerRoot.id='odin-footer-root';document.body.appendChild(footerRoot);
    fetch('https://raw.githubusercontent.com/bluehatgeeks/Odin-Health-Calgary/master/odinfooter.html',{cache:'no-store'}).then(function(r){return r.text()}).then(function(html){footerRoot.innerHTML=html;execScripts(footerRoot)});
    // Booking modal
    document.addEventListener('click',function(e){
      var btn=e.target.closest('.booking-trigger');
      if(btn){e.preventDefault();var m=document.getElementById('booking-modal-overlay');m.style.display='flex';}
      if(e.target.id==='booking-modal-close'||e.target.id==='booking-modal-overlay'){document.getElementById('booking-modal-overlay').style.display='none';}
    });
    document.addEventListener('keydown',function(e){if(e.key==='Escape'){document.getElementById('booking-modal-overlay').style.display='none';}});
  })();
</script>
</body>
</html>
```

---

## PHASE 1 — Research (Parallelizable: run all 6 concurrently)

> Use `superpowers:dispatching-parallel-agents` — dispatch one research agent per therapy simultaneously.

---

### Task 1: Research — Hydrogen Inhalation Therapy

**Output:** A markdown content block saved to `docs/research/hydrogen-therapy-content.md`

- [ ] **Step 1: Web search — benefits overview**
  Search: `"hydrogen inhalation therapy" benefits peer-reviewed research site:pubmed.ncbi.nlm.nih.gov OR site:ncbi.nlm.nih.gov`
  Capture: 5–8 key benefits with brief explanations

- [ ] **Step 2: Web search — mechanism of action**
  Search: `hydrogen gas therapy antioxidant mechanism selective hydroxyl radical`
  Capture: how molecular hydrogen works at cellular level (2–3 paragraphs, plain language)

- [ ] **Step 3: Web search — clinical citations**
  Search: `hydrogen inhalation therapy clinical study 2020 2021 2022 2023`
  Capture: 3–4 real citations (author, journal, year, finding summary)

- [ ] **Step 4: Web search — conditions addressed**
  Search: `hydrogen therapy conditions treated inflammation oxidative stress neurological`
  Capture: 6–10 specific conditions or use cases

- [ ] **Step 5: Web search — how it works / session description**
  Search: `hydrogen inhalation therapy session what to expect process`
  Capture: 4–5 step process for a typical session

- [ ] **Step 6: Save content file**
  Write all captured content to `docs/research/hydrogen-therapy-content.md`

---

### Task 2: Research — Functional Health & Medicine

**Output:** `docs/research/functional-health-content.md`

- [ ] **Step 1: Web search — definition and principles**
  Search: `functional medicine definition root cause systems biology Institute for Functional Medicine`
  Capture: core definition, 4–5 foundational principles

- [ ] **Step 2: Web search — conventional vs functional comparison**
  Search: `functional medicine vs conventional medicine difference approach`
  Capture: 5–6 comparison points (symptom vs root cause, acute vs chronic, etc.)

- [ ] **Step 3: Web search — conditions and research**
  Search: `functional medicine chronic disease outcomes evidence research 2020 2023`
  Capture: 3–4 citations, 6–8 conditions addressed

- [ ] **Step 4: Web search — diagnostic tools used**
  Search: `functional medicine advanced lab testing biomarkers assessment tools`
  Capture: 5–6 types of diagnostics/assessments used

- [ ] **Step 5: Save content file**
  Write all captured content to `docs/research/functional-health-content.md`

---

### Task 3: Research — Functional Health Coaching

**Output:** `docs/research/functional-coaching-content.md`

- [ ] **Step 1: Web search — health coaching definition and evidence**
  Search: `health coaching outcomes chronic disease lifestyle change evidence peer-reviewed`
  Capture: definition, 4–5 key outcomes backed by research

- [ ] **Step 2: Web search — coaching pillars / framework**
  Search: `functional health coaching pillars nutrition sleep stress movement mindset`
  Capture: 5–6 coaching pillars with brief descriptions

- [ ] **Step 3: Web search — who benefits most**
  Search: `health coaching ideal candidate chronic fatigue burnout weight optimization performance`
  Capture: 4–5 client profiles / who this is for

- [ ] **Step 4: Web search — transformation timeline**
  Search: `functional health coaching program timeline phases results`
  Capture: 3–4 phase journey description (onboarding → assessment → protocol → optimization)

- [ ] **Step 5: Save content file**
  Write all captured content to `docs/research/functional-coaching-content.md`

---

### Task 4: Research — Nutritional Supplementation & Herbology

**Output:** `docs/research/nutritional-supplementation-content.md`

- [ ] **Step 1: Web search — evidence-based supplementation**
  Search: `nutritional supplementation functional medicine evidence based protocol 2022 2023`
  Capture: 5–6 key supplement categories with research support

- [ ] **Step 2: Web search — medicinal herbology / adaptogens**
  Search: `medicinal herbs adaptogens ashwagandha rhodiola clinical evidence stress cortisol`
  Capture: 5–6 key herbs/botanicals with mechanism and citations

- [ ] **Step 3: Web search — individualized protocol approach**
  Search: `personalized nutrition supplementation biomarker guided protocol`
  Capture: how individualized protocols are built (3–4 phases)

- [ ] **Step 4: Web search — safety and quality**
  Search: `supplement quality third party testing GMP standards functional medicine`
  Capture: 3–4 quality/safety points

- [ ] **Step 5: Save content file**
  Write all captured content to `docs/research/nutritional-supplementation-content.md`

---

### Task 5: Research — Marma Therapy with Tuning Forks

**Output:** `docs/research/marma-therapy-content.md`

- [ ] **Step 1: Web search — marma therapy definition**
  Search: `marma therapy ayurveda energy points definition benefits`
  Capture: definition, history, 5–6 key marma points and their associations

- [ ] **Step 2: Web search — tuning fork sound therapy science**
  Search: `tuning fork sound therapy vibrational healing clinical research biofield`
  Capture: mechanism (resonance, frequency, vagal tone), 2–3 citations

- [ ] **Step 3: Web search — combined marma + sound therapy**
  Search: `marma therapy tuning fork combination sound healing energy medicine`
  Capture: how the two modalities complement each other

- [ ] **Step 4: Web search — conditions and benefits**
  Search: `marma therapy benefits stress pain nervous system regulation outcomes`
  Capture: 6–8 benefits / conditions addressed

- [ ] **Step 5: Web search — session description**
  Search: `marma therapy session what to expect process steps`
  Capture: 4–5 step session walkthrough

- [ ] **Step 6: Save content file**
  Write all captured content to `docs/research/marma-therapy-content.md`

---

### Task 6: Research — Ayurveda

**Output:** `docs/research/ayurveda-content.md`

- [ ] **Step 1: Web search — ayurveda definition and principles**
  Search: `ayurveda definition doshas vata pitta kapha principles health`
  Capture: core definition, the 3 dosha types with characteristics

- [ ] **Step 2: Web search — modern science validation**
  Search: `ayurveda clinical research evidence based outcomes 2020 2023 peer-reviewed`
  Capture: 3–4 research citations validating specific ayurvedic practices

- [ ] **Step 3: Web search — ayurvedic treatments and protocols**
  Search: `ayurvedic treatments panchakarma herbs lifestyle diet seasonal protocol`
  Capture: 5–6 treatment modalities / protocols used

- [ ] **Step 4: Web search — benefits and conditions**
  Search: `ayurveda benefits conditions treated inflammation digestion stress mental clarity`
  Capture: 6–8 specific benefits

- [ ] **Step 5: Web search — seasonal / daily routine**
  Search: `ayurvedic dinacharya seasonal routine ritucharya protocol`
  Capture: 3–4 seasonal/daily protocol highlights

- [ ] **Step 6: Save content file**
  Write all captured content to `docs/research/ayurveda-content.md`

---

## PHASE 2 — Image Generation (Parallelizable: run all 6 concurrently)

> Use Nano Banana to generate images for each page. Generate two versions per page: a **black-and-white base** and a **color overlay** (matching the dual-image `.hero-image-bw` / `.hero-image-color` pattern in the template).
> Additional section images (e.g., "how it works" diagram image) should also be generated where needed.

**Nano Banana prompt style to follow** (adapt subject per therapy):
- Style: cinematic, high-contrast, clinical + earthy, dark background, moody lighting
- Composition: portrait or 3:2 landscape, centered subject
- Color palette hint: deep greens, lime accents, or desaturated for B&W version

---

### Task 7: Images — Hydrogen Therapy

- [ ] **Step 1: Generate hero B&W image**
  Prompt: `"A person wearing a hydrogen inhalation mask, seated in a clinical wellness setting, dark moody background, black and white, cinematic lighting, high contrast"`
  Save as: `img/hydrogen-hero-bw.jpg`

- [ ] **Step 2: Generate hero color image**
  Prompt: Same prompt but: `"...subtle lime green accent light, color, clinical wellness aesthetic"`
  Save as: `img/hydrogen-hero-color.jpg`

- [ ] **Step 3: Generate how-it-works image**
  Prompt: `"Molecular hydrogen gas bubbles, microscopic view, dark green background, lime green glow, scientific aesthetic"`
  Save as: `img/hydrogen-how-it-works.jpg`

---

### Task 8: Images — Functional Health & Medicine

- [ ] **Step 1: Generate hero B&W image**
  Prompt: `"Functional medicine practitioner reviewing biomarker lab results on a tablet, clinical modern office, black and white, cinematic"`
  Save as: `img/functional-health-hero-bw.jpg`

- [ ] **Step 2: Generate hero color image**
  Prompt: Same with `"...lime green screen glow, dark background, color"`
  Save as: `img/functional-health-hero-color.jpg`

- [ ] **Step 3: Generate diagnostic/systems image**
  Prompt: `"Human body systems interconnected diagram, dark background, lime green highlights, medical data visualization aesthetic"`
  Save as: `img/functional-health-systems.jpg`

---

### Task 9: Images — Functional Health Coaching

- [ ] **Step 1: Generate hero B&W image**
  Prompt: `"Health coach and client in a modern consultation session, warm lighting, black and white, cinematic portrait"`
  Save as: `img/functional-coaching-hero-bw.jpg`

- [ ] **Step 2: Generate hero color image**
  Prompt: Same with `"...warm lime accent light, color version"`
  Save as: `img/functional-coaching-hero-color.jpg`

- [ ] **Step 3: Generate transformation image**
  Prompt: `"Person standing confidently in a minimalist wellness studio, dramatic lighting, lime glow from window, cinematic"`
  Save as: `img/functional-coaching-transformation.jpg`

---

### Task 10: Images — Nutritional Supplementation & Herbology

- [ ] **Step 1: Generate hero B&W image**
  Prompt: `"Botanical herbs and supplement bottles arranged artfully on dark surface, overhead shot, black and white, high contrast"`
  Save as: `img/nutritional-hero-bw.jpg`

- [ ] **Step 2: Generate hero color image**
  Prompt: Same with `"...rich greens and golds, lime accent light, color version"`
  Save as: `img/nutritional-hero-color.jpg`

- [ ] **Step 3: Generate botanical spotlight image**
  Prompt: `"Close-up of ashwagandha and rhodiola roots with mortar and pestle, dark wooden surface, moody lighting, earthy tones"`
  Save as: `img/nutritional-botanicals.jpg`

---

### Task 11: Images — Marma Therapy + Tuning Forks

- [ ] **Step 1: Generate hero B&W image**
  Prompt: `"Practitioner placing tuning fork near the head of a person lying on a wellness table, soft moody light, black and white, cinematic"`
  Save as: `img/marma-hero-bw.jpg`

- [ ] **Step 2: Generate hero color image**
  Prompt: Same with `"...vibrational wave lime green glow effect, color version"`
  Save as: `img/marma-hero-color.jpg`

- [ ] **Step 3: Generate frequency/energy image**
  Prompt: `"Sound wave visualization in the shape of a human body silhouette, dark background, lime green frequency lines, abstract scientific"`
  Save as: `img/marma-frequency.jpg`

---

### Task 12: Images — Ayurveda

- [ ] **Step 1: Generate hero B&W image**
  Prompt: `"Ayurvedic treatment room with herbs, oils, and copper vessels on dark wood, black and white, cinematic moody lighting"`
  Save as: `img/ayurveda-hero-bw.jpg`

- [ ] **Step 2: Generate hero color image**
  Prompt: Same with `"...warm golden and green tones, color version"`
  Save as: `img/ayurveda-hero-color.jpg`

- [ ] **Step 3: Generate dosha image**
  Prompt: `"Three symbolic elemental circles representing air, fire, and earth on dark background with lime green geometric accents, abstract minimal"`
  Save as: `img/ayurveda-doshas.jpg`

---

## PHASE 3 — Build Pages (Parallelizable after Phase 1 & 2 complete)

> Use `superpowers:dispatching-parallel-agents` — dispatch all 6 build agents simultaneously once research and images are ready.
> Each agent reads its research file + design.md before writing any HTML/CSS.

---

### Task 13: Build — hydrogen-therapy.html + hydrogen-therapy.css

**Files:**
- Create: `hydrogen-therapy.html`
- Create: `hydrogen-therapy.css`

**Layout Sections (in order):**
1. Hero (shell pattern above) — heading: "Hydrogen Inhalation Therapy"
2. **Stat Strip** — 4 stats inline: e.g., "600+ Studies", "Selective Antioxidant", "Non-Invasive", "0 Known Side Effects" — dark bar with lime numbers
3. **Benefits Grid** — `.core-feature-grid` with 3 cards (lime / purple / white-smoke color variants): Antioxidant Protection, Anti-Inflammatory, Mitochondrial Support. Each card: icon + heading + 3–4 sentence paragraph
4. **How It Works** — Numbered 4-step section (2×2 grid): Inhale → Absorb → Neutralize → Restore. Each step: step number in lime, heading, paragraph
5. **Conditions Addressed** — Modality badge pills grid (`.about-us-modalities span` pattern): list of 8–10 conditions
6. **Research Citations** — 3–4 citation cards: author, journal, year, key finding. Dark card with lime left-border accent
7. **Booking CTA section**

- [ ] **Step 1: Read research file**
  Read `docs/research/hydrogen-therapy-content.md` and `design.md`

- [ ] **Step 2: Write hydrogen-therapy.css**
  Page-scoped styles only. Includes: stat strip layout, citation card styles, any layout adjustments. No global overrides. All values from design.md tokens.

- [ ] **Step 3: Write hydrogen-therapy.html**
  Follow shell pattern exactly. Wire in `hydrogen-therapy.css`. Build all 7 sections using researched content and generated image paths.

- [ ] **Step 4: Verify design rules**
  Check: no hardcoded hex colors, `.booking-trigger` on all CTAs, all grids have `≤768px` collapse media query in CSS, hero-slogan present, nav/footer loaded via fetch

- [ ] **Step 5: Commit**
  ```bash
  git add hydrogen-therapy.html hydrogen-therapy.css
  git commit -m "feat: add hydrogen inhalation therapy page"
  ```

---

### Task 14: Build — functional-health.html + functional-health.css

**Files:**
- Create: `functional-health.html`
- Create: `functional-health.css`

**Layout Sections (in order):**
1. Hero — heading: "Functional Health & Medicine"
2. **Comparison Split** — 2-column layout: "Conventional Medicine" (left, muted/bordered) vs "Functional Medicine" (right, lime-accented). 5 comparison rows: Approach / Focus / Time / Tools / Outcome
3. **Root Cause Diagnostic Steps** — Horizontal numbered step bar (4 steps): Intake → Lab Analysis → Pattern Recognition → Protocol Design
4. **Conditions We Address** — 2-column tag list (`.symptoms-tags` pattern): 10–12 chronic conditions
5. **Diagnostic Tools** — 3-column feature cards with icons: Advanced Labs, Hormone Panels, Gut Analysis, etc.
6. **Research Citations** — Same citation card pattern as Task 13
7. **FAQ Accordion** — 4–5 questions using `.faq-item`/`<details>` pattern from design.md
8. **Booking CTA section**

- [ ] **Step 1: Read research file** `docs/research/functional-health-content.md` + `design.md`
- [ ] **Step 2: Write functional-health.css**
- [ ] **Step 3: Write functional-health.html**
- [ ] **Step 4: Verify design rules**
- [ ] **Step 5: Commit**
  ```bash
  git add functional-health.html functional-health.css
  git commit -m "feat: add functional health and medicine page"
  ```

---

### Task 15: Build — functional-coaching.html + functional-coaching.css

**Files:**
- Create: `functional-coaching.html`
- Create: `functional-coaching.css`

**Layout Sections (in order):**
1. Hero — heading: "Functional Health Coaching"
2. **Coaching Pillars** — 3-column icon + heading + paragraph cards: Nutrition, Sleep, Stress Regulation, Movement, Mindset, Lab-Guided (6 cards, 2 rows of 3)
3. **Who This Is For** — 3-column profile cards (`.profile-card` pattern): Executives, Shift Workers, People with Chronic Fatigue — image placeholder + role label + 2-sentence description
4. **Transformation Journey Timeline** — Vertical or horizontal 4-phase timeline: Discovery → Assessment → Protocol → Optimization. Each phase: number + title + paragraph
5. **Outcomes Block** — 3 quoted outcome cards (`.testimonial`-style but without names — anonymized outcome statements): e.g., "Eliminated brain fog in 8 weeks", styled with quote icon
6. **Booking CTA section**

- [ ] **Step 1: Read research file** `docs/research/functional-coaching-content.md` + `design.md`
- [ ] **Step 2: Write functional-coaching.css**
- [ ] **Step 3: Write functional-coaching.html**
- [ ] **Step 4: Verify design rules**
- [ ] **Step 5: Commit**
  ```bash
  git add functional-coaching.html functional-coaching.css
  git commit -m "feat: add functional health coaching page"
  ```

---

### Task 16: Build — nutritional-supplementation.html + nutritional-supplementation.css

**Files:**
- Create: `nutritional-supplementation.html`
- Create: `nutritional-supplementation.css`

**Layout Sections (in order):**
1. Hero — heading: "Nutritional Supplementation & Herbology"
2. **Botanical Spotlight Cards** — Large horizontal cards (full-width each, alternating layout): herb name + action mechanism + research backing. 4 featured botanicals (ashwagandha, rhodiola, berberine, etc.)
3. **3-Phase Protocol** — Horizontal 3-column phase cards: Phase 1 Assess → Phase 2 Restore → Phase 3 Optimize. Each: phase number (lime), title, 4-5 bullet points
4. **Key Compounds Grid** — Modality badge pills: 10–12 supplement/compound names
5. **Quality Standards** — 3-column cards: Third-Party Tested, Bioavailable Forms, Practitioner-Grade. Icon + heading + short paragraph
6. **Research Citations** — 3–4 citation cards
7. **Booking CTA section**

- [ ] **Step 1: Read research file** `docs/research/nutritional-supplementation-content.md` + `design.md`
- [ ] **Step 2: Write nutritional-supplementation.css**
- [ ] **Step 3: Write nutritional-supplementation.html**
- [ ] **Step 4: Verify design rules**
- [ ] **Step 5: Commit**
  ```bash
  git add nutritional-supplementation.html nutritional-supplementation.css
  git commit -m "feat: add nutritional supplementation and herbology page"
  ```

---

### Task 17: Build — marma-therapy.html + marma-therapy.css

**Files:**
- Create: `marma-therapy.html`
- Create: `marma-therapy.css`

**Layout Sections (in order):**
1. Hero — heading: "Marma Therapy & Tuning Fork Enhancement"
2. **What Is Marma Split** — 2-column: left = text block (definition, history, 3 paragraphs), right = generated image (`img/marma-frequency.jpg`)
3. **Energy Zone Cards** — 4–6 cards: body zones (Head & Cranial, Chest & Heart, Abdomen, Upper Limbs, Lower Limbs) — each card: zone name (lime), associated functions, marma points listed as small tags
4. **Tuning Fork Science Strip** — Dark lime-tinted banner: 3 inline stat-style blocks: "432 Hz", "Vagal Activation", "Cellular Resonance" — each with icon and 1-sentence explanation
5. **Session Walkthrough** — Numbered 4-step process (vertical): Welcome & Intake → Tuning & Assessment → Marma Treatment → Integration & Rest
6. **Booking CTA section**

- [ ] **Step 1: Read research file** `docs/research/marma-therapy-content.md` + `design.md`
- [ ] **Step 2: Write marma-therapy.css**
- [ ] **Step 3: Write marma-therapy.html**
- [ ] **Step 4: Verify design rules**
- [ ] **Step 5: Commit**
  ```bash
  git add marma-therapy.html marma-therapy.css
  git commit -m "feat: add marma therapy and tuning forks page"
  ```

---

### Task 18: Build — ayurveda.html + ayurveda.css

**Files:**
- Create: `ayurveda.html`
- Create: `ayurveda.css`

**Layout Sections (in order):**
1. Hero — heading: "Ayurveda — Ancient Intelligence, Modern Results"
2. **Dosha Types** — 3-column cards (full-height, distinct visual treatment): Vata (Air + Space), Pitta (Fire + Water), Kapha (Earth + Water). Each: dosha name (lime), element icons, characteristics list, imbalance symptoms, recommended support
3. **Ayurvedic Principles Timeline** — Horizontal 5-node timeline (scroll-able on mobile): Dinacharya → Ritucharya → Ahara → Vihara → Panchakarma. Each node: name + 2-sentence explanation
4. **Ancient Wisdom / Modern Science Split** — 2-column: left dark card "Traditional Understanding", right lime-tinted card "Modern Research Confirms". Mirror 4 paired points
5. **Treatments We Offer** — 2×3 grid feature cards with icons: Pulse Diagnosis, Herbal Formulations, Dietary Guidance, Lifestyle Protocols, Seasonal Cleansing, Stress & Mind Therapies
6. **Research Citations** — 3–4 citation cards
7. **Booking CTA section**

- [ ] **Step 1: Read research file** `docs/research/ayurveda-content.md` + `design.md`
- [ ] **Step 2: Write ayurveda.css**
- [ ] **Step 3: Write ayurveda.html**
- [ ] **Step 4: Verify design rules**
- [ ] **Step 5: Commit**
  ```bash
  git add ayurveda.html ayurveda.css
  git commit -m "feat: add ayurveda page"
  ```

---

## PHASE 4 — QA & Cross-Page Validation

### Task 19: Final QA Check

- [ ] **Step 1: Visual scan all 6 pages**
  Open each in browser. Verify: nav loads, footer loads, hero slogan appears, booking modal opens on all `.booking-trigger` clicks, Escape key closes modal.

- [ ] **Step 2: Responsive check**
  Resize to 375px width. Verify: all multi-column grids collapse, text is readable, no horizontal scroll.

- [ ] **Step 3: Design rules audit**
  Search for any hardcoded hex values across all 6 new HTML/CSS files:
  ```bash
  grep -rn "#[0-9a-fA-F]\{3,6\}" hydrogen-therapy.html hydrogen-therapy.css functional-health.html functional-health.css functional-coaching.html functional-coaching.css nutritional-supplementation.html nutritional-supplementation.css marma-therapy.html marma-therapy.css ayurveda.html ayurveda.css
  ```
  Expected: no results (only CSS variable references allowed)

- [ ] **Step 4: Booking trigger check**
  ```bash
  grep -L "booking-trigger" hydrogen-therapy.html functional-health.html functional-coaching.html nutritional-supplementation.html marma-therapy.html ayurveda.html
  ```
  Expected: empty output (all pages have at least one `.booking-trigger`)

- [ ] **Step 5: Hero slogan check**
  ```bash
  grep -L "We Do Not Practice Medicine" hydrogen-therapy.html functional-health.html functional-coaching.html nutritional-supplementation.html marma-therapy.html ayurveda.html
  ```
  Expected: empty output

- [ ] **Step 6: Final commit**
  ```bash
  git add .
  git commit -m "qa: verify all 6 therapy pages pass design and functional checks"
  ```

---

## Execution Summary

| Phase | Tasks | Parallelizable? |
|---|---|---|
| Phase 1: Research | Tasks 1–6 | ✅ All 6 in parallel |
| Phase 2: Images | Tasks 7–12 | ✅ All 6 in parallel |
| Phase 3: Build | Tasks 13–18 | ✅ All 6 in parallel (after Phase 1+2) |
| Phase 4: QA | Task 19 | ❌ Sequential, after Phase 3 |

**Total new files:** 12 (6 HTML + 6 CSS) + 18 images + 6 research markdown files
