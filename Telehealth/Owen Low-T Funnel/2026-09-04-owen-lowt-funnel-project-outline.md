---
date: 2026-09-04
description: "Project outline for a new Andropause/Low-T/Stress & Fatigue funnel targeting Optimiser Owen, built on the Serious Buyer Protocol framework and Owen's existing proven quiz/booking mechanics."
project: Odin Labs Calgary
status: active
quarter: Q3-2026
tags:
  - marketing
  - strategy
  - funnel
  - owen
  - work-note
---

# Owen Low-T Funnel: Project Outline

## Context

New funnel targeting **Optimiser Owen** (the existing secondary avatar defined in [[avatar.md]]), specifically positioned around **Male Andropause / Low-T, Stress & Fatigue**. Chosen as the next build because it requires zero new avatar work, reuses proven funnel mechanics, has a low-complexity clinical protocol (diet, exercise, sleep, adaptogens — no delicate feedback-loop interpretation required), and already has demand signal from the live Owen quiz funnel.

This project is informed by two inputs reviewed 2026-09-04:
1. **Five training videos** ("The Serious Buyer Protocol" / Health Business Mastery course) — see Framework section below.
2. **The existing, data-validated Owen quiz funnel** (`owen.html`, documented in [[2026-08-19-owen-two-step-booking-widget.md]]) — proven mechanics this project reuses rather than reinvents.

## Framework Source: The Serious Buyer Protocol

Five-video course teaching a "Serious Buyer Engine" for health practitioner marketing. Summary of the doctrine this project applies:

- **Video 1 — Patient language, not clinical language.** Write from symptoms/feelings ("gassing out by 3pm," "wakes at 3am with a racing mind"), not diagnoses. People search from pain, not from a diagnostic vocabulary they don't have.
- **Video 2 — Belief over impulse.** Marketing must build belief (in the methodology, in the practitioner, in the client's own ability to succeed) rather than urgency/scarcity/discounts. Belief-driven clients ("evangelists") follow through on protocols; discount-driven clients ("effort tourists") don't.
- **Video 3 — Paid ads over organic/social, but only once positioning is differentiated.** Organic/social is a poor primary volume channel even at scale (cited example: a major health account converts ~2-3 consults per viral reel). Paid ads work well for health (claimed 5-7x ROAS) but fail when positioning is generic ("red ocean") — differentiation is the actual lever, not targeting or ad mechanics.
- **Video 4 — Paid consult over free discovery call.** Charging a small fee for the consult (their example: $27) filters for serious buyers, raises show-rate dramatically, and removes the "convince" dynamic — the call becomes genuine help rather than a sales pitch.
- **Video 5 — The full "Serious Buyer Engine":** long-form trust ad (belief-building, can run long) → health landing page (message-match, not curiosity-bait) → free belief-shift mini-class (15-20 min, educational, no scarcity) → paid consultation (intake form, real value) → consult script → premium value program close.

**Direct relevance to Odin Labs:** the Owen funnel's existing two-step results/booking redesign (2026-08-19) already independently arrived at a similar insight — that the booking ask needs a belief-building step, not just a CTA. This framework sharpens that with a specific mechanism (a dedicated mini-class) and validates the paid-consult direction as a deliberate next test rather than a novel idea.

## Decisions Made (2026-09-04)

| Decision | Choice | Rationale |
|---|---|---|
| New page vs. modify `owen.html` | **New separate lander** (working name `owen-lowt.html`) | Isolates this as its own test; keeps Owen's existing funnel data clean; consistent with this project's practice of changing one variable at a time. |
| Paid vs. free consult at launch | **Free**, matching Owen's current proven booking mechanic | Avoids compounding two unvalidated variables (new positioning + new payment friction) in one test. Paid consult is explicitly logged as the next planned test once this funnel has its own baseline data. |
| Belief-shift mini-class placement | **Before the quiz**, on the landing page | Mirrors the course's ad → landing page → belief class sequence most closely; builds belief in the mechanism before asking for quiz engagement. |
| Mini-class format | **Short video (60-90s)** | Closer to the course's actual mechanic than a text block; requires new production (script + recording/AI-avatar + editing) — logged as an open item, not yet scoped. |
| Mini-class content | **Belief-shift only, no protocol/dosing reveal** | The class's job is reframing "this isn't age, it's a fixable cortisol/adaptogen-responsive metabolic pattern" — not delivering the herb stack or protocol details. Protocol specifics stay downstream of the booked call. |
| Geo targeting | **Canada + USA wide**, from launch | This is a net-new funnel, not a change to the live Owen campaign — launching under the new telehealth-wide model avoids inheriting Owen's unresolved Calgary-only pivot debt (see [[2026-09-03-telehealth-only-pivot-decision.md]]). |
| Ad creative | **New Low-T-targeted ads**, not reuse of existing Owen creative | Per the course's trust-ad doctrine: long-form, belief-building creative built specifically for this positioning, following Video 1's symptom-first language principle. Not a copy-paste of Owen's generic quiz creative. |
| Avatar research | **None — reuse Owen's existing avatar.md unchanged** | Per the original brief: "zero new avatar work." Owen's demographics, buying psychology, and messaging table already cover Low-T/performance-decline framing. |

## Funnel Shape (5 Steps)

1. **New Low-T-targeted trust ads.** Built specifically for this positioning; symptom-first language per Video 1 (avoid "andropause"/"testosterone" as headline hooks — use Owen's own language: "gassing out by 3pm," belly fat "that wasn't there at 35," libido decline). Long-form allowed per Video 5's trust-ad doctrine if it builds genuine belief.
2. **Landing page + belief-shift mini-class.** New lander. Mini-class (60-90s video) plays or sits prominently before Q1 of the quiz. Reframes the mechanism: not age, a fixable cortisol/adaptogen-responsive pattern. No protocol/dosing shown at this stage.
3. **Quiz.** Reuses Owen's existing 10-question quiz mechanic and results-bucket logic from `owen.html`. Copy retargeted to Low-T/stress/fatigue-specific symptom language.
4. **Results page → free booked clinician call.** Reuses Owen's proven two-step results/booking mechanic exactly: collapsed results section, expanded booking section with lazy-loaded iframe + 8-second failure fallback link, UTM/attribution passthrough via `buildBookingUrl()`. Free at launch.
5. **Booking confirmed.** Existing GHL/Mixpanel event pipeline (`Outcome Shown`, `Booking Iframe Loaded`, `Appointment Booked`, etc.) reused as-is.

## Explicitly Out of Scope for This Launch

- Paid consult (logged as the next planned test once this funnel has baseline booking data).
- Protocol/dosing reveal in the mini-class or anywhere pre-call.
- New avatar research — Owen's avatar.md is reused unchanged.
- Changes to the live Owen quiz funnel or its Calgary-only targeting/pivot migration — tracked separately in [[2026-09-03-telehealth-only-pivot-decision.md]].

## Open Items

- [ ] **Mini-class production plan** — script, recording method (real practitioner vs. AI avatar), editing. Not yet scoped.
- [ ] **New trust-ad creative production plan** — script, format (video length, talking-head vs. other), editing. Not yet scoped.
- [ ] **Email/nurture sequence** — the originating brief referenced "the email sequence" as already existing; no such sequence was found in this vault during this project's research. Needs confirming: does one exist elsewhere (GHL directly, another doc), or does it need to be built as part of this project?
- [ ] **New lander build** — `owen-lowt.html`, forked from `owen.html`'s proven quiz/results/booking structure, with new copy, new mini-class section, and Low-T-specific quiz questions/outcome buckets.
- [ ] **Ad set setup** — new campaign/ad set, Canada+USA-wide targeting, new creative once produced.
- [ ] **Decision rule for this funnel's own test** — once launched, needs its own baseline and pass/fail bar (following the same pattern as [[2026-08-19-owen-two-step-booking-widget.md]]), separate from Owen's existing test.

## Related
- [[avatar.md]] — Owen's full avatar definition (demographics, psychology, messaging), reused unchanged.
- [[2026-08-19-owen-two-step-booking-widget.md]] — the proven quiz/results/booking mechanic this funnel forks from.
- [[2026-09-03-telehealth-only-pivot-decision.md]] — telehealth pivot and Canada+USA-wide targeting context.
- [[2026-09-04-owen-lowt-messaging.md]] — core positioning, symptom-language, belief-shift copy, and applied funnel copy for this project.
- [[2026-09-04-andropause-low-t-client-language.md]] — dedicated Andropause/Low-T client-language entry, built to match the "What Your Clients Are Actually Typing" library pattern.
- [[2026-09-04-andropause-low-t-belief-shifts.md]] — dedicated Andropause/Low-T belief-shift entry, built to match the "Belief Shifts That Make Clients Commit" library pattern.
- [[Odin Labs Calgary]] — project hub.
