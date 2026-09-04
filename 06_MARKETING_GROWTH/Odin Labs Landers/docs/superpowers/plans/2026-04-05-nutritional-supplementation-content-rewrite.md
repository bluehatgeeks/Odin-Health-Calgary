# Nutritional Supplementation — Content Rewrite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite all copy and headings in `nutritional-supplementation.html` to lead with a sharp, confrontational "most supplements don't work because no one measured you" argument, add a Random vs. Precision contrast block, and carry the evidence-based precision narrative through every section — same HTML structure, new voice throughout.

**Architecture:** HTML-only content rewrite — no CSS changes, no new sections (except a Random vs. Precision contrast block inserted in Section 2 before the arsenal grid), no structural changes to existing sections. Every task targets a specific section's text nodes, headings, and subheadings. Visual verification via preview MCP after all tasks complete.

**Tech Stack:** HTML5. No CSS, JS, or framework changes.

---

## File Map

| File | Role |
|---|---|
| `nutritional-supplementation.html` | All changes go here — text content only |
| `nutritional-supplementation.css` | Add styles for contrast block only (Task 3) |

---

## Design System Rules (must follow throughout)
- No hardcoded hex values — use `var(--lime-green)`, `var(--white)`, `var(--white-800)`, etc.
- All new CSS classes use prefix `ns-`
- Multi-column layouts must collapse at `≤768px`
- Booking CTAs must carry class `.booking-trigger`

---

## Task 1: Rewrite Hero Section (Section 1)

**Files:**
- Modify: `nutritional-supplementation.html` (lines ~63–85, `.ns-hero` section)

- [ ] **Step 1.1: Rewrite hero heading, subheading, and slogan**

In `nutritional-supplementation.html`, replace the hero content text as follows:

**`<p class="hero-slogan">`** — change to:
```
Most supplements don't work. Yours probably don't either.
```

**`<h1 class="ns-hero-h1">`** — change to:
```
Not because the science is wrong. Because no one measured you first.
```

**`<p class="ns-hero-sub">`** — change to:
```
The evidence for targeted supplementation is strong. Berberine moves HbA1c in 37 RCTs. Magnesium shifts sleep, blood pressure, and insulin signaling when you're actually low. But "probably low" isn't a protocol. Your labs are.
```

**`<a class="btn-primary booking-trigger">`** — change button text to:
```
Get Your Baseline Labs
```

**`<meta name="description">`** in `<head>` — update to:
```
Most supplements don't work — not because the science is wrong, but because no one measured you first. At Odin Lab Calgary, we build precision supplementation protocols from your actual biomarkers, not guesswork.
```

- [ ] **Step 1.2: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html
git commit -m "content: rewrite hero — hard open on supplementation guesswork problem"
```

---

## Task 2: Rewrite Stats Strip (below hero)

**Files:**
- Modify: `nutritional-supplementation.html` (lines ~90–109, `.ns-stats-strip`)

- [ ] **Step 2.1: Replace stats strip values and labels**

Replace the four `.ns-stat` blocks entirely with:

```html
      <div class="ns-stat">
        <span class="ns-stat__value">$50B</span>
        <span class="ns-stat__label">Spent annually on supplements in North America — most of it without a single baseline lab</span>
      </div>
      <div class="ns-stat">
        <span class="ns-stat__value">67%</span>
        <span class="ns-stat__label">Of supplement users have never tested the markers their stack is supposed to fix</span>
      </div>
      <div class="ns-stat">
        <span class="ns-stat__value">0</span>
        <span class="ns-stat__label">Generic protocols built on your markers, your forms, your dose — that number is zero</span>
      </div>
      <div class="ns-stat">
        <span class="ns-stat__value">Ours are.</span>
        <span class="ns-stat__label">Every protocol at Odin Lab starts with labs, ends with a retest. That's the whole model.</span>
      </div>
```

- [ ] **Step 2.2: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html
git commit -m "content: rewrite stats strip — consequence framing on supplementation without baseline"
```

---

## Task 3: Add Random vs. Precision Contrast Block (Section 2, before arsenal grid)

**Files:**
- Modify: `nutritional-supplementation.html` (insert before `.ns-arsenal-grid` inside `.ns-badges-section`)
- Modify: `nutritional-supplementation.css` (add contrast block styles)

- [ ] **Step 3.1: Update badges section label and insert contrast block HTML**

In `nutritional-supplementation.html`, inside `.ns-badges-inner`:

1. Change `<span class="ns-badges-label">The Clinical Toolkit</span>` to:
```html
<span class="ns-badges-label">Two ways to supplement. One works.</span>
```

2. Insert this contrast block **before** `<div class="ns-arsenal-grid">`:

```html
      <div class="ns-contrast-block">
        <div class="ns-contrast-col ns-contrast-col--random">
          <span class="ns-contrast-tag">Random Supplementation</span>
          <ul class="ns-contrast-list">
            <li>Pick a stack from a blog or a friend's recommendation</li>
            <li>Guess the dose — maybe match the label, maybe double it</li>
            <li>Buy whatever form is cheapest at the pharmacy</li>
            <li>Never test whether you were actually deficient</li>
            <li>Never retest to see if anything changed</li>
            <li>Wonder why you don't feel different after three months</li>
          </ul>
          <p class="ns-contrast-verdict">Result: expensive urine. Occasionally a placebo effect.</p>
        </div>
        <div class="ns-contrast-col ns-contrast-col--precision">
          <span class="ns-contrast-tag">Precision Supplementation</span>
          <ul class="ns-contrast-list">
            <li>Run a baseline: 25-OH D, RBC magnesium, omega-3 index, homocysteine, HbA1c, ferritin, zinc</li>
            <li>Identify actual deficiencies — not assumed ones</li>
            <li>Select bioavailable forms that your physiology can actually use</li>
            <li>Dose from data, not from packaging</li>
            <li>Retest at 8–12 weeks to confirm the markers moved</li>
            <li>Adjust based on what the labs show — not how you feel that week</li>
          </ul>
          <p class="ns-contrast-verdict">Result: measurable change. Documented on a lab sheet.</p>
        </div>
      </div>
      <p class="ns-contrast-divider-label">What we work with — when labs confirm you need it</p>
```

- [ ] **Step 3.2: Add contrast block CSS to `nutritional-supplementation.css`**

Find the `/* ════... ARSENAL GRID */` comment block in `nutritional-supplementation.css`. **Before** that block, insert:

```css
/* ════════════════════════════════════════════════════════
   RANDOM VS. PRECISION CONTRAST BLOCK
   ════════════════════════════════════════════════════════ */
.ns-contrast-block {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2px;
  margin: 32px 0 20px 0;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid rgba(196, 255, 73, 0.2);
}

.ns-contrast-col {
  padding: 32px 28px;
}

.ns-contrast-col--random {
  background: rgba(255, 255, 255, 0.03);
  border-right: 1px solid rgba(255, 255, 255, 0.07);
}

.ns-contrast-col--precision {
  background: rgba(196, 255, 73, 0.05);
}

.ns-contrast-tag {
  display: inline-block;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  padding: 4px 12px;
  border-radius: 20px;
  margin-bottom: 20px;
}

.ns-contrast-col--random .ns-contrast-tag {
  background: rgba(255, 255, 255, 0.07);
  color: var(--white-500);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.ns-contrast-col--precision .ns-contrast-tag {
  background: rgba(196, 255, 73, 0.15);
  color: var(--lime-green);
  border: 1px solid rgba(196, 255, 73, 0.35);
}

.ns-contrast-list {
  list-style: none;
  margin: 0 0 20px 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ns-contrast-list li {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 0.92rem;
  font-weight: 400;
  line-height: 1.5;
  padding-left: 18px;
  position: relative;
}

.ns-contrast-col--random .ns-contrast-list li {
  color: var(--white-500);
}

.ns-contrast-col--random .ns-contrast-list li::before {
  content: '×';
  position: absolute;
  left: 0;
  color: rgba(255, 100, 100, 0.6);
  font-weight: 700;
}

.ns-contrast-col--precision .ns-contrast-list li {
  color: var(--white-800);
}

.ns-contrast-col--precision .ns-contrast-list li::before {
  content: '→';
  position: absolute;
  left: 0;
  color: var(--lime-green);
  font-weight: 700;
}

.ns-contrast-verdict {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 0.88rem;
  font-weight: 600;
  font-style: italic;
  margin: 0;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.07);
}

.ns-contrast-col--random .ns-contrast-verdict {
  color: var(--white-500);
}

.ns-contrast-col--precision .ns-contrast-verdict {
  color: var(--lime-green);
}

.ns-contrast-divider-label {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--lime-green);
  text-align: center;
  margin: 28px 0 4px 0;
  opacity: 0.8;
}

@media (max-width: 768px) {
  .ns-contrast-block {
    grid-template-columns: 1fr;
  }

  .ns-contrast-col--random {
    border-right: none;
    border-bottom: 1px solid rgba(255, 255, 255, 0.07);
  }

  .ns-contrast-col {
    padding: 24px 20px;
  }
}
```

- [ ] **Step 3.3: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html nutritional-supplementation.css
git commit -m "feat: add Random vs. Precision contrast block to supplementation page"
```

---

## Task 4: Rewrite Supplement Categories Section (Section 3)

**Files:**
- Modify: `nutritional-supplementation.html` (`.ns-categories-section`, lines ~163–234)

- [ ] **Step 4.1: Rewrite section header**

Replace the section header copy:

**`<span class="ns-section-label">`** → `Evidence-based protocols`

**`<h2 class="ns-section-heading">`** → `Six nutrients. Measurable outcomes. Only if you actually need them.`

**`<p class="ns-section-sub">`** → `These aren't recommendations based on general wellness trends. They're compounds with human trial data behind specific endpoints — and we only use them when your labs confirm a real gap.`

- [ ] **Step 4.2: Rewrite all 6 category card subheadings and titles**

Change `<span class="ns-cat-subheading">Mechanism</span>` → `<span class="ns-cat-subheading">Why it works</span>` on ALL 6 cards.

Change `<span class="ns-cat-subheading">Outcomes we target</span>` → `<span class="ns-cat-subheading">What changes on your labs</span>` on ALL 6 cards.

- [ ] **Step 4.3: Rewrite card 1 opener (Omega-3)**

Replace the Omega-3 mechanism paragraph (`<p class="ns-cat-body">`) — first one only:
```
If your omega-3 index is low, your triglycerides are higher than they need to be, your inflammatory load is harder to manage, and your cardiovascular risk is elevated — and most people don't know their index. EPA and DHA remodel cell membranes, shift eicosanoid balance toward resolution, and suppress inflammatory transcription. A meta-analysis of 14 RCTs covering 135,291 patients showed significant reductions in cardiovascular death and myocardial infarction. That's the evidence. The question is whether you're actually deficient — which is a lab question, not a guess.
```

- [ ] **Step 4.4: Rewrite card 2 opener (Magnesium)**

Replace the Magnesium mechanism paragraph (`<p class="ns-cat-body">`) — first one only:
```
Magnesium is involved in over 600 enzymatic reactions. ATP synthesis, DNA repair, neuromuscular signaling, insulin receptor function, nitric oxide tone — all of it depends on adequate magnesium. Between 14 and 48% of type 2 diabetes patients are low on labs. Most general practitioners don't test it. Standard serum magnesium is a poor proxy for intracellular status — you can look normal on a basic panel and be functionally depleted. We test it properly.
```

- [ ] **Step 4.5: Rewrite card 3 opener (Vitamin D3/K2)**

Replace the Vitamin D mechanism paragraph (`<p class="ns-cat-body">`) — first one only:
```
Vitamin D deficiency is endemic in northern climates. Calgary sits at 51° north. If you haven't tested in the last year, you're guessing. Calcitriol binds VDR receptors on immune cells, shifts immunity toward regulatory phenotypes, and modulates cytokine production — including the overactive inflammatory response seen in autoimmune conditions. The VITAL trial showed lower incidence of new-onset autoimmune disease at 2,000 IU/day. The right dose is the one that gets your 25-OH to an optimal range, not a fixed number off a label.
```

- [ ] **Step 4.6: Rewrite card 4 opener (B-Complex)**

Replace the B-Complex mechanism paragraph (`<p class="ns-cat-body">`) — first one only:
```
If you have an MTHFR variant — and roughly 40% of people do — standard folic acid does almost nothing. Your body can't convert it to the active form fast enough. Methylfolate (5-MTHF) bypasses that bottleneck entirely. Combined with methylcobalamin (B12) and P-5-P (B6), it drives the one-carbon metabolism network: DNA synthesis, neurotransmitter production, homocysteine clearance. High homocysteine is a cardiovascular and neurological risk factor we can move — with the right form, at the right dose, confirmed by retesting.
```

- [ ] **Step 4.7: Rewrite card 5 opener (Zinc)**

Replace the Zinc mechanism paragraph (`<p class="ns-cat-body">`) — first one only:
```
Zinc is required for immune cell maturation, cytokine regulation, wound repair, and thyroid hormone synthesis. It's also commonly suboptimal — especially in plant-forward diets, high-stress physiology, and anyone on long-term proton pump inhibitors. The difference between "within range" and "optimal" on a zinc panel is often the difference between an immune system that responds and one that lingers. We test plasma zinc, not serum, and we dose to a functional target.
```

- [ ] **Step 4.8: Rewrite card 6 opener (Probiotics)**

Replace the Probiotics mechanism paragraph (`<p class="ns-cat-body">`) — first one only:
```
Probiotics are one of the most over-purchased and under-targeted supplements in existence. Most people buy a random multi-strain product and take it indefinitely with no clear indication. We use probiotics when the clinical picture points to gut-immune dysregulation — IBS patterns, antibiotic aftermath, inflammatory bowel involvement, or mood-gut signaling issues. The strains matter. The dose matters. The indication matters. Without a reason, you're just feeding your gut at random.
```

- [ ] **Step 4.9: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html
git commit -m "content: rewrite supplement categories — precision argument, evidence-first framing"
```

---

## Task 5: Rewrite Botanical Spotlights Section (Section 4)

**Files:**
- Modify: `nutritional-supplementation.html` (`.ns-botanicals-section`, lines ~239–342)

- [ ] **Step 5.1: Rewrite section header**

**`<span class="ns-section-label">`** → `Clinical botanicals — not folklore`

**`<h2 class="ns-section-heading">`** → `Four botanicals with human trial data. Not anecdote. Not tradition. Trials.`

**`<p class="ns-section-sub">`** → `We use botanicals that have been through randomized, controlled trials measuring endpoints you can feel and test — cortisol, HbA1c, cognitive scores, fatigue indices. If the evidence isn't there, neither are we.`

- [ ] **Step 5.2: Change all "Human data highlights" labels**

Change every `<span class="ns-herb-uses-label">Human data highlights</span>` to:
```html
<span class="ns-herb-uses-label">What the trials showed</span>
```
(4 instances — one per herb card)

- [ ] **Step 5.3: Rewrite Ashwagandha mechanism paragraph**

Replace `<p class="ns-herb-mechanism">` on the Ashwagandha card:
```
Ashwagandha works. That's the short version. The longer version: KSM-66 extract at 600 mg/day reduced serum cortisol by 27.9% in a placebo-controlled trial of stressed adults. Multiple double-blind RCTs show significant reductions in PSS and DASS stress scores within 6–8 weeks. The mechanism is HPA-axis modulation — withanolides tune cortisol output and thyroid receptor sensitivity without sedating you. It normalizes stress physiology. That's different from suppressing it.
```

- [ ] **Step 5.4: Rewrite Rhodiola mechanism paragraph**

Replace `<p class="ns-herb-mechanism">` on the Rhodiola card:
```
Rhodiola's clinical use case is precise: cognitive performance under sustained load. Night-shift workers. High-output executives. People running on a sleep deficit and needing their prefrontal cortex to stay online. Salidroside and rosavins inhibit MAO-A and MAO-B — prolonging dopamine, serotonin, and norepinephrine availability. A controlled trial in 56 physicians showed statistically significant improvement in mental performance during night duty. Another in 161 cadets showed pronounced antifatigue effects from a single standardized dose. It's not a stimulant. It's a buffer against depletion.
```

- [ ] **Step 5.5: Rewrite Berberine mechanism paragraph**

Replace `<p class="ns-herb-mechanism">` on the Berberine card:
```
Berberine has more human trial data than most pharmaceutical cardiometabolic agents that never made it to market. An umbrella meta-analysis of 37 RCTs showed significant reductions in fasting glucose, HbA1c, HOMA-IR, LDL, triglycerides, and blood pressure. AMPK activation is the primary driver — it increases muscle glucose disposal, suppresses hepatic gluconeogenesis, and shifts oxidation toward lipids. Fasting insulin dropped 28.1% in controlled studies. HOMA-IR by 44.7%. No hypoglycemia risk — the effect is conditional on hyperglycemia being present. We use it when the metabolic markers justify it.
```

- [ ] **Step 5.6: Rewrite Lion's Mane mechanism paragraph**

Replace `<p class="ns-herb-mechanism">` on the Lion's Mane card:
```
Lion's Mane is the only botanical with human trial data showing actual cognitive improvement in mild cognitive impairment — not just subjective reports, but measured test performance. In a 16-week RCT in 30 MCI patients, cognitive scores improved significantly versus placebo — and reversed after discontinuation, which is exactly what you'd expect from a mechanism-based effect. Hericenones and erinacines stimulate NGF and BDNF synthesis. Erinacines cross the blood–brain barrier. A 2023 double-blind RCT in healthy adults showed faster Stroop task performance within 60 minutes of dosing. The evidence is still building — but it's real evidence.
```

- [ ] **Step 5.7: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html
git commit -m "content: rewrite botanical section — trials-first framing, direct voice throughout"
```

---

## Task 6: Add Pull Quote to Section Image (Section 5)

**Files:**
- Modify: `nutritional-supplementation.html` (`.ns-section-image-wrap`, lines ~347–354)
- Modify: `nutritional-supplementation.css` (add pull quote styles)

- [ ] **Step 6.1: Add pull quote overlay HTML**

Replace the entire `.ns-section-image-wrap` block with:

```html
  <!-- ══════════════════════════════════════
       SECTION 5 — SECTION IMAGE
       ══════════════════════════════════════ -->
  <div class="ns-section-image-wrap">
    <div class="ns-section-image-inner">
      <img
        src="https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/nutritional-section.jpg?v=2"
        alt="Precision supplement protocol preparation at Odin Lab Calgary"
      >
      <div class="ns-image-pullquote">
        <p>"Supplementing without data is expensive guessing.<br>We don't guess."</p>
      </div>
    </div>
  </div>
```

- [ ] **Step 6.2: Add pull quote CSS**

In `nutritional-supplementation.css`, find `.ns-section-image-inner` and add after it:

```css
.ns-section-image-inner {
  position: relative;
}

.ns-image-pullquote {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 40px 40px 32px;
  background: linear-gradient(to top, rgba(15, 35, 15, 0.92) 0%, rgba(15, 35, 15, 0.6) 60%, transparent 100%);
}

.ns-image-pullquote p {
  font-family: 'Poppins', sans-serif;
  font-size: clamp(1.1rem, 2.5vw, 1.6rem);
  font-weight: 600;
  font-style: italic;
  color: var(--white);
  margin: 0;
  line-height: 1.4;
  max-width: 700px;
}

.ns-image-pullquote p::before {
  content: '';
  display: block;
  width: 40px;
  height: 3px;
  background: var(--lime-green);
  margin-bottom: 16px;
}

@media (max-width: 768px) {
  .ns-image-pullquote {
    padding: 24px 20px 20px;
  }
}
```

Note: `.ns-section-image-inner` already has a rule in the CSS. Add `position: relative;` to the existing rule rather than duplicating it.

- [ ] **Step 6.3: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html nutritional-supplementation.css
git commit -m "content: add pull quote overlay to section image — core precision message"
```

---

## Task 7: Rewrite 3-Phase Protocol Section (Section 6)

**Files:**
- Modify: `nutritional-supplementation.html` (`.ns-protocol-section`, lines ~359–460)

- [ ] **Step 7.1: Rewrite section header**

**`<span class="ns-section-label">`** → `How we work`

**`<h2 class="ns-section-heading">`** → `Assess. Fix. Prove it worked.`

**`<p class="ns-section-sub">`** → `Three phases. Every one anchored to your labs. Not a wellness program — a protocol with measurable checkpoints.`

- [ ] **Step 7.2: Rewrite Phase 1 (Assess)**

Change `<h3 class="ns-phase-name">Assess</h3>` to:
```html
<h3 class="ns-phase-name">We find out what's actually low.</h3>
```

Keep the bullet list content but replace the 5 bullet text spans with:

Bullet 1:
```
Comprehensive biomarker panel: 25-OH vitamin D, RBC magnesium, ferritin, B12, zinc, omega-3 index, hsCRP, homocysteine, fasting glucose, HbA1c, insulin, lipid panel. Not a "wellness check" — a targeted deficiency screen.
```

Bullet 2:
```
Detailed intake: symptoms, diet, stress load, sleep quality, current medications, prior supplementation, and what you've already tried that didn't work.
```

Bullet 3:
```
Functional thresholds — not just "within normal range." A vitamin D of 52 nmol/L is technically "normal." It's also suboptimal for immune regulation. We work to targets that match the clinical evidence, not the lab's reference range.
```

Bullet 4:
```
Genetic context where it changes the protocol: MTHFR variants, COMT polymorphisms, methylation-related SNPs that affect which forms of nutrients your body can actually use.
```

Bullet 5:
```
Gut function assessment: absorption capacity, bowel history, microbiome indicators. If you can't absorb a nutrient, the dose doesn't matter.
```

- [ ] **Step 7.3: Rewrite Phase 2 (Restore)**

Change `<h3 class="ns-phase-name">Restore</h3>` to:
```html
<h3 class="ns-phase-name">We fix the gaps with the right forms.</h3>
```

Bullet 1:
```
Targeted repletion using bioavailable, practitioner-grade forms only: magnesium glycinate not oxide, methylfolate not folic acid, methylcobalamin not cyanocobalamin, cholecalciferol D3 not ergocalciferol D2. Form is not a detail — it's the difference between absorption and excretion.
```

Bullet 2:
```
Gut repair where the intake points to absorption failure: mucosal support (L-glutamine, zinc carnosine), probiotic reseeding, removal of dietary triggers that are keeping inflammatory tone elevated.
```

Bullet 3:
```
Foundational stack established from your actual panel results — not a template. Two people with fatigue can have completely different deficiency profiles. Their protocols look different.
```

Bullet 4:
```
Retest at 8–12 weeks. This is non-negotiable. Without a retest, we have no confirmation that the protocol is working. Symptoms improve for many reasons. Labs don't lie.
```

Bullet 5:
```
Symptom tracking alongside lab data — correlating subjective improvement with objective markers. The goal is both: you feel better and the numbers move.
```

- [ ] **Step 7.4: Rewrite Phase 3 (Optimize)**

Change `<h3 class="ns-phase-name">Optimize</h3>` to:
```html
<h3 class="ns-phase-name">We raise the ceiling — once the floor is solid.</h3>
```

Bullet 1:
```
You can't optimize a depleted system. Phase 3 only begins when Phase 2 has been confirmed by labs. Performance support on top of deficiency is expensive noise.
```

Bullet 2:
```
Targeted botanicals and nootropics aligned with your goals: cognitive performance (Lion's Mane, Rhodiola), stress resilience (Ashwagandha), metabolic optimization (Berberine, ALA, Chromium). Based on your history and current markers — not a "cognitive stack."
```

Bullet 3:
```
Mitochondrial support for sustained energy output: CoQ10 ubiquinol (not ubiquinone), NMN/NR, PQQ. Relevant when markers and history point to mitochondrial inefficiency — not as a default add-on.
```

Bullet 4:
```
Maintenance dosing calibrated to your ongoing biomarker targets. Not a fixed monthly subscription — a protocol that evolves as your physiology changes.
```

Bullet 5:
```
Quarterly or semi-annual monitoring panels to confirm optimization is holding and catch drift before it becomes deficiency again.
```

- [ ] **Step 7.5: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html
git commit -m "content: rewrite 3-phase protocol — lab-anchored language, direct phase names"
```

---

## Task 8: Rewrite Quality Standards Section (Section 7)

**Files:**
- Modify: `nutritional-supplementation.html` (`.ns-quality-section`, lines ~465–510)

- [ ] **Step 8.1: Rewrite section header**

**`<span class="ns-section-label">`** → `Non-negotiable standards`

**`<h2 class="ns-section-heading">`** → `The supplement industry doesn't regulate itself. We do.`

**`<p class="ns-section-sub">`** → `No FDA pre-market approval. No mandatory third-party testing. No minimum bioavailability standards. The gap between what's on the label and what's in the bottle — and what your body actually absorbs — is real. Here's how we close it.`

- [ ] **Step 8.2: Rewrite quality card titles and body copy**

**Card 1 title:** Change to `Third-party tested. Or we don't stock it.`

**Card 1 body:** Replace with:
```
Dietary supplements are not FDA-approved before reaching shelves. A manufacturer can print any claim on a label and sell it legally — unless someone independently tests it. NSF Certified for Sport, USP Verified, and Informed Sport test finished products at the batch level: label accuracy, contaminant presence, and freedom from 270+ prohibited substances. That's not branding. That's verification. We don't recommend products that haven't been through it.
```

**Card 2 title:** Change to `Bioavailable forms only. Because inactive forms don't work.`

**Card 2 body:** Replace with:
```
Folic acid is not methylfolate. Cyanocobalamin is not methylcobalamin. Magnesium oxide has roughly 4% absorption — glycinate is over 80%. Ubiquinone requires conversion to ubiquinol in tissues that are often too compromised to do it efficiently. These aren't minor variations. If you have an MTHFR variant, folic acid supplementation does almost nothing. We match the form to your physiology — confirmed by genotype screening where relevant.
```

**Card 3 title:** Change to `Practitioner-grade — because dose and purity are not marketing.`

**Card 3 body:** Replace with:
```
Retail supplements are formulated to hit a price point. That means synthetic forms, doses calibrated to minimum label requirements, and quality oversight that stops at GMP certification. Practitioner-grade manufacturers supply licensed clinicians, undergo independent audits, and use doses drawn from the clinical literature — not the cheapest dose that still allows a health claim. The difference shows up in your labs. That's the only metric that matters.
```

- [ ] **Step 8.3: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html
git commit -m "content: rewrite quality standards — hard stance on industry self-regulation gap"
```

---

## Task 9: Rewrite Citations Section Header (Section 8)

**Files:**
- Modify: `nutritional-supplementation.html` (`.ns-citations-section`, lines ~515–545)

- [ ] **Step 9.1: Rewrite citations section header only**

**`<span class="ns-section-label">`** → `The evidence base`

**`<h2 class="ns-section-heading">`** → `We don't make claims without citations.`

**`<p class="ns-section-sub">`** → `Every protocol recommendation at Odin Lab is grounded in published, peer-reviewed human trials. These are the key studies behind the compounds we use most frequently. Read them. Ask questions about them. That's what we're here for.`

(Leave the 4 citation cards exactly as they are — content is already strong.)

- [ ] **Step 9.2: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html
git commit -m "content: rewrite citations section header — direct evidence-base framing"
```

---

## Task 10: Rewrite CTA Section (Section 9)

**Files:**
- Modify: `nutritional-supplementation.html` (`.ns-cta-section`, lines ~509–518)

- [ ] **Step 10.1: Rewrite CTA copy**

**`<span class="ns-cta-label">`** → `Ready to stop guessing`

**`<h2 class="ns-cta-heading">`** → `Stop guessing. Start measuring.`

**`<p class="ns-cta-sub">`** → `Book a functional assessment. We'll run the baseline, identify what's actually low, build a protocol from your markers — not a template — and retest at 8–12 weeks to confirm the numbers moved. That's the whole model.`

**`<a class="btn-primary booking-trigger">`** — change button text to:
```
Book a Functional Assessment
```

- [ ] **Step 10.2: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html
git commit -m "content: rewrite CTA — hard close matching precision narrative"
```

---

## Task 11: Increment CSS Version

**Files:**
- Modify: `nutritional-supplementation.html` (CSS link tag)

- [ ] **Step 11.1: Increment version**

Change `nutritional-supplementation.css?v=3` to `nutritional-supplementation.css?v=4`.

- [ ] **Step 11.2: Commit**

```bash
cd "/Users/alexandertretjakov/Downloads/odin lab landers"
git add nutritional-supplementation.html
git commit -m "chore: increment CSS to v=4 after content rewrite"
```

---

## Task 12: Visual Verification

**No file changes — verification only.**

- [ ] **Step 12.1: Start preview server**

Use `preview_start` MCP tool with name `odin-landers` to serve the directory.

- [ ] **Step 12.2: Navigate and screenshot**

Use `preview_eval` to navigate to `http://localhost:8765/nutritional-supplementation.html`, then take a `preview_screenshot`.

- [ ] **Step 12.3: Verify hero**

Use `preview_inspect` on `.ns-hero-h1` — confirm text contains "Not because the science is wrong."

Use `preview_inspect` on `.ns-hero-sub` — confirm updated copy is present.

- [ ] **Step 12.4: Verify stats strip**

Use `preview_eval` to check all 4 `.ns-stat__value` texts:
```js
Array.from(document.querySelectorAll('.ns-stat__value')).map(el => el.textContent.trim())
// Expected: ["$50B", "67%", "0", "Ours are."]
```

- [ ] **Step 12.5: Verify contrast block**

Use `preview_eval`:
```js
!!document.querySelector('.ns-contrast-block')
// Expected: true
```

Use `preview_screenshot` after scrolling to the badges section to visually confirm the two-column contrast layout.

- [ ] **Step 12.6: Verify section image pull quote**

Use `preview_eval`:
```js
document.querySelector('.ns-image-pullquote p').textContent.includes('guessing')
// Expected: true
```

- [ ] **Step 12.7: Verify CTA**

Use `preview_inspect` on `.ns-cta-heading` — confirm `color: rgb(196, 255, 73)` and text "Stop guessing. Start measuring."

- [ ] **Step 12.8: Full-page screenshot**

Scroll through the page taking screenshots at each section. Confirm no layout breaks, no regressions on existing sections.

If any issues found: diagnose from CSS/HTML, fix, re-screenshot.

---

## Summary of Changes

| File | Changes |
|---|---|
| `nutritional-supplementation.html` | All section copy rewritten (Tasks 1–10); new contrast block HTML (Task 3); pull quote HTML (Task 6); CSS version v=4 (Task 11) |
| `nutritional-supplementation.css` | Contrast block styles added (Task 3); pull quote overlay styles added (Task 6) |

## Verification Gate

Before claiming completion:
1. Hero opens with "Not because the science is wrong. Because no one measured you first."
2. Stats strip shows $50B / 67% / 0 / "Ours are."
3. Random vs. Precision contrast block is visible and two-column on desktop
4. Pull quote overlay appears on section image
5. Protocol phases read "We find out…" / "We fix the gaps…" / "We raise the ceiling…"
6. CTA heading reads "Stop guessing. Start measuring."
7. CSS version is v=4
8. No regressions — existing layout, cards, citations all intact
