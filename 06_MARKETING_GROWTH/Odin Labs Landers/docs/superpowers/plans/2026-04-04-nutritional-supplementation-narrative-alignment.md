# Nutritional Supplementation Page — Narrative Alignment Plan

> **For agentic workers:** Use `superpowers:subagent-driven-development` or `superpowers:executing-plans` to implement task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Align every section of `nutritional-supplementation.html` (and supporting meta/alt text where needed) with one coherent thesis: **most retail and self-chosen supplementation fails because it is not individualized or verified**; **only evidence-based, lab-matched precision supplementation can justify expectations**.

**Architecture:** Keep existing DOM sections and design components; revise copy only (plus `meta description`, image `alt` text, and optional `nutritional-supplementation.css` `?v=` bump if styles change). Maintain `design.md` voice: clinical authority, no hype, systems-thinking, data-informed.

**Tech stack:** Static HTML, `nutritional-supplementation.css`, `odin-shared.css` from CDN.

**North-star message map**

| Pillar | Meaning for copy |
|--------|------------------|
| Problem | Random stacks, wrong forms/doses, no baseline, no retest → no accountability |
| Proof | Human trials for *classes* of interventions; applicability still hinges on your data |
| Method | Baseline labs → indication → bioavailable form + dose → retest → adjust |
| Guardrails | Quality (label matches bottle), practitioner-grade, no compound without indication |

---

## Content review (current page vs thesis)

### Strong alignment (light polish only)

- **Hero subhead** — Already bridges “evidence exists” with “labs required.” **Plan:** Add one explicit clause echoing the second half of the thesis (precision + evidence together), e.g. that retail defaults fail even when the molecule is the right one.
- **Badges / contrast block** — “Random vs precision” is on-theme. **Plan:** Ensure divider line **“when labs confirm you need it”** stays visible; optional add half-sentence tying left column to “why most supplements don’t work” using the exact h1 phrase once.
- **Categories section** — Header and “only if you need them” framing fit. **Plan:** Normalize subsection **“What changes on your labs”** where bullets mix *symptoms* with *markers* (omega-3, zinc cards): either rename to **“Outcomes & markers we track”** or split into two short lines per card.
- **Botanicals** — Trial-forward framing fits. **Plan:** Soften **Lion’s Mane** mechanism line: avoid absolute **“the only botanical…”** (overclaim); prefer **“among the few botanicals with…”** or “with published human cognitive endpoints.”
- **Protocol (3 phases)** — Logically implements precision. **Plan:** Rewrite section label + intro paragraph to **repeat the contrast**: Phase 1 explicitly “stop guessing”; Phase 2 “interventions tied to gaps”; Phase 3 “only after restoration, and only if markers/goals support adds.”
- **Quality standards** — Supports “why yours don’t work” (wrong substance inside capsule). **Plan:** One-sentence intro bridge: **evidence + precision are useless if identity/potency/impurities fail.**
- **Citations** — Reinforces evidence. **Plan:** Subhead line that ties citations to **selection criteria** (“we don’t stock the page with molecules that lack human outcome data for their intended use”).
- **Footer CTA** — Close the loop: **most supplements don’t work → start with measurement.**

### Needs stronger alignment or verification

- **Stats strip** — Thematically excellent ($50B, untested use). **Risk:** `$50B` and **`67%`** must be **sourced** or reframed per practice standards (CLAUDE.md: data-informed). **Plan:** Replace with **cited** figures from reputable industry/survey sources, or rephrase as qualitative (“Industry scale is massive; most spend never touches a baseline panel”) without fake precision. Revisit **fourth stat** (`Ours are.`): emotionally punchy but visually odd as a “value”; consider **`100%`** / **`All`** + label “protocols start with labs and end with retest” for scannability.
- **Title + meta description** — Meta already mentions measurement; ensure **title** still matches positioning and **description** states both halves: failure mode + precision solution.
- **Hero CTA** — “Get Your Baseline Labs” matches; confirm booking modal flow still appropriate copy-wise.

### HTML hygiene (done)

- [x] Fix invalid curly-quote attributes on `p.ns-cat-body` (Vitamin D card) and `p.ns-herb-mechanism` (Ashwagandha card) so CSS applies.

---

## Task 1: Narrative spine & meta

**Files:**

- Modify: `nutritional-supplementation.html` (head + hero)

- [ ] **Step 1:** Draft one sentence **page thesis** (internal only or comment) ensuring hero subhead + meta description both mention: (a) generic supplementation underperforms, (b) evidence applies when matched to physiology, (c) labs + retest.

- [ ] **Step 2:** Update `<meta name="description">` to explicitly include **“evidence-based precision supplementation”** and the measurement loop.

- [ ] **Step 3:** Optionally adjust `<title>` to second clause if SEO needs “precision” literal — keep under ~60 characters or accept truncation.

**Verify:** Read head + hero aloud; thesis clear in <30 seconds.

---

## Task 2: Stats strip — accuracy + clarity

**Files:**

- Modify: `nutritional-supplementation.html` (`div.ns-stats-strip`)

- [ ] **Step 1:** For each stat, either **add footnote/citation** in a small print block below the strip (new paragraph, muted class) **or** replace numbers with defensible qualitative copy.

- [ ] **Step 2:** Redesign stat **#4** for consistency: numeric or single-word value + label; avoid ambiguous “Ours are.” unless paired with scannable label.

- [ ] **Step 3:** If adding citations section for stats, reuse `var(--white-500)` / existing tertiary text pattern from `design.md`; no new colors.

**Verify:** No unsourced statistics remain; strip still readable at 900px and 480px breakpoints.

---

## Task 3: Contrast block — micro-threads to h1

**Files:**

- Modify: `nutritional-supplementation.html` (`ns-badges-section`)

- [ ] **Step 1:** In **Random** column, add one lead bullet or `ns-contrast-verdict` clause echoing **“Most supplements don’t work…”** without duplicating h1 verbatim (avoid SEO/canonical repetition if undesirable).

- [ ] **Step 2:** In **Precision** column closing verdict, add **evidence + measurement** in one clause (“evidence-based dosing **after** labs”).

**Verify:** Section reads as direct answer to h1.

---

## Task 4: Category cards — headings + lab honesty

**Files:**

- Modify: `nutritional-supplementation.html` (`ns-categories-section`)

- [ ] **Step 1:** Rename **“What changes on your labs”** to **`Outcomes & markers`** (or equivalent) everywhere in the six cards.

- [ ] **Step 2:** In each card, ensure first sentence of **“Why it works”** states **for whom** it works (deficient / dysregulated marker / indication) to reinforce precision.

- [ ] **Step 3:** Trim or qualify any sentence that sounds like universal benefit without a lab hook.

**Verify:** No card implies “everyone should take X.”

---

## Task 5: Botanicals — accuracy pass

**Files:**

- Modify: `nutritional-supplementation.html` (`ns-botanicals-section`)

- [ ] **Step 1:** Revise Lion’s Mane intro to remove **absolute uniqueness** claims; cite MCI + acute cognitive pilot as scope.

- [ ] **Step 2:** Scan other herb intros for “works” / triumphal tone; align with **design.md** (clinical, not hype) while keeping trial facts.

**Verify:** A cautious practitioner would not cringe at overclaim.

---

## Task 6: Protocol section — tie phases to thesis

**Files:**

- Modify: `nutritional-supplementation.html` (`ns-protocol-section`)

- [ ] **Step 1:** Change **section label** from generic “How we work” to e.g. **Precision process** or **Lab-to-protocol**.

- [ ] **Step 2:** Replace intro paragraph with three beat sequence: **measure → intervene only for gaps → retest**; explicitly contrast with retail stacks.

- [ ] **Step 3:** In **Optimize** phase bullets, add one line: **no new compound without indication + monitoring plan.**

**Verify:** Reader sees why phases are the antidote to “yours don’t work.”

---

## Task 7: Quality + citations — bridge sentences

**Files:**

- Modify: `nutritional-supplementation.html` (`ns-quality-section`, `ns-citations-section`)

- [ ] **Step 1:** Quality section intro: connect **product quality** to **failed expectations** (“wrong dose **or** wrong ingredient = still doesn’t work”).

- [ ] **Step 2:** Citations intro: state that **evidence selects the menu**; **labs select the plate**.

**Verify:** Sections feel connected, not bolted on.

---

## Task 8: CTA + imagery

**Files:**

- Modify: `nutritional-supplementation.html` (`ns-cta-section`, `ns-section-image-wrap` alts)

- [ ] **Step 1:** CTA heading/sub: echo **measurement-first** and **evidence-based precision** once each.

- [ ] **Step 2:** `alt` text on section image: mention **baseline testing** or **protocol from data** if generic.

**Verify:** Last screen reinforces action that matches thesis.

---

## Task 9: CSS version + regression pass

**Files:**

- Modify: `nutritional-supplementation.html` (stylesheet query string if CSS edited)
- Modify: `nutritional-supplementation.css` (only if new classes for stats footnotes)

- [ ] **Step 1:** If new elements added, increment `nutritional-supplementation.css?v=N`.

- [ ] **Step 2:** Open page at 1300px, 768px, 375px; confirm no overflow from longer stats footnote.

- [ ] **Step 3:** Confirm all `.booking-trigger` CTAs preserved.

**Verify:** Visual parity or improvement only.

---

## Self-review

- **Thesis coverage:** Tasks 1–8 each map to problem, proof, method, or guardrails.
- **Placeholder scan:** No TBD left in tasks above.
- **Gaps:** If stats remain qualitative, Task 2 must document the exact replacement strings in the implementation PR for stakeholder sign-off.

---

## Execution handoff

Plan complete and saved to `docs/superpowers/plans/2026-04-04-nutritional-supplementation-narrative-alignment.md`. Two execution options:

1. **Subagent-driven (recommended)** — Fresh subagent per task, review between tasks.
2. **Inline execution** — Run tasks sequentially in one session with checkpoints.

Which approach do you want?
