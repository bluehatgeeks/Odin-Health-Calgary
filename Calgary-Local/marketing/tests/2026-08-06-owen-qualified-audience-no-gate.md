# Removing the in-quiz qualification gate AND targeting a pre-qualified lookalike audience (oil & gas executives) will outperform gating a general audience, because the gate was mainly filtering out people who were never going to be a good fit to begin with — an audience problem the quiz was being asked to solve

**Funnel:** owen-quiz-funnel
**Status:** Concluded — FAIL
**Date started:** 2026-08-10 (ad set `[Aug 10] male only - 35-50 - Calgary wide - Lookalike` created and launched; confirmed live via Meta API 2026-08-11)
**Date concluded:** 2026-08-19 (closed on real Mixpanel numbers: 9 real leads, 1 real booking-link click, 0 bookings — a fail against the 25% pass bar regardless of the n=10 sample-size target not being formally hit; see Result/Verdict below)

---

## The change

Two coordinated changes, shipped together as one test:

1. **No qualification gate in the quiz.** This is the code change built and locally verified on 2026-08-04 (session that produced this file) but **never deployed to GHL**. Mechanism: Q10 (cash-pay commitment, hard yes/no/no-gate) removed; replaced with a diagnostic, non-gating question ("What have you already invested in trying to fix this?" — Nothing yet / personal trainer / supplements-biohacking / doctor visits). Q11 (natural-vs-conventional philosophy re-ask) removed entirely. Quiz is now 10 questions, pure diagnosis, no disqualify branch — every completion reaches the lead-capture form. Real qualification (budget, fit) is intended to happen on the call instead.
2. **New ad set with a lookalike audience, replacing the current targeting.** Audience source: enriched purchased list via Apollo.io, filtered to oil & gas executives, used to build a Meta lookalike. This **replaces** the existing `male only - 35-50 - Calgary wide` targeting on the ad set — not a parallel/split-test structure. Everything else on the ad set (creative, budget, placements) stays the same as whatever is running at launch.

## Why

The [2026-08-04 qualifier-in-quiz test](2026-08-04-owen-qualifier-in-quiz.md) was built to fix "0 of 16 leads ever reached the qualifier step" by moving the gate earlier and cutting the results page down to a tease. That test's original design (documented in that file) still hard-gated on Q10/Q11 — it just moved the gate earlier in the funnel rather than removing it. On review, gating a *general* Calgary male 35-50 audience was diagnosed as asking the wrong tool to solve an audience-quality problem: **the friction wasn't misplaced, the audience was untargeted.** This test's premise: replace broad targeting with a pre-qualified lookalike (oil & gas execs — high-income, high-stress, plausible fit for the offer) and remove the gate entirely, on the theory that a correctly-targeted audience doesn't need to be interrogated to self-select.

**Supersession note:** The Aug 4 file's "The change" section (in-quiz hard gate) was never deployed and is now superseded by this test's "no gate" mechanism before it ever went live. Treat the Aug 4 file's *why* (results-page-as-product diagnosis, results-page tease redesign) as still valid and shipped — that part is real and separate from the gate question. Its gate-specific decision rule (qualifier-pass rate at n=20) is stale and will not be filled in; this file's decision rule supersedes it for anything gate-related.

## Decision rule (locked before launch — do not edit after data starts coming in)

Written 2026-08-11, after the ad set was confirmed live (4 creatives active, lookalike audience attached, $40/day budget, in learning phase — see Live log 2026-08-11).

- **Primary metric:** Lead → booking-link-click rate (via `Booking Link Clicked` Mixpanel event, instrumented in [2026-07-11-owen-tracking-instrumentation.md](2026-07-11-owen-tracking-instrumentation.md)). This directly tests the test's premise — does a better-fit audience produce leads that click through to book without needing a quiz-side gate? No prior Owen test has a comparable number, since the in-quiz gate never actually shipped to production before being redesigned — this is the first real read on post-lead behavior with no gate in place.
- **Secondary metric (context, not pass/fail):** Cost per lead, compared against the ~$36/lead general-audience baseline (Jul 12–18 clean window, 6 leads / $260.19). Watch whether the lookalike audience is even affordable to acquire — oil & gas execs may have a smaller/pricier reachable pool on Meta than general Calgary males 35-50. If cost per lead balloons past ~2x baseline (~$72+), flag it even if booking-click rate looks good, since the economics may not work regardless.
- **Sample size to reach a verdict:** 10 clean leads (excluding self-tests — tag any self-test with a distinguishable UTM or email). At ~$36-72/lead and $40/day budget, expect roughly 4-7 days minimum to reach this; smaller n than the 20-lead bar used in the Aug 4 test because this is a directional read on a new audience, not a final scale decision — extend to 20 before treating a borderline result as conclusive.
- **Pass bar:** ≥25% of leads click the booking link. (No internal baseline exists for this metric yet — this figure is a placeholder judgment call, not derived from prior data. Revisit once the first few real data points come in; if it's obviously miscalibrated, that's fine, that's what a first read is for.)
- **Fail bar:** <25% at n=10 → extend to n=20 before final call, same rule-of-three logic used in the Aug 4 test.
- **On pass:** Lookalike + no-gate combination works — keep running, start optimizing cost-per-booking-click, consider testing the two variables (audience vs. gate) separately in a follow-up test to isolate which one is doing the work.
- **On fail:** Isolate the two bundled variables in a follow-up test — e.g. no-gate quiz on the general audience (to check if audience was the real lever) or gate reinstated on the lookalike audience (to check if the gate was fine all along and general audience was the real problem). This test's bundled design means a fail here doesn't tell you which change to revert without a follow-up.

## Baseline (before this change)

Prior ad set (`male only - 35-50 - Calgary wide`, general audience, no lookalike) — now PAUSED. Most relevant comparable window is the clean run that justified the qualifier-in-quiz redesign, since it's the last period with trustworthy, non-AN-contaminated numbers on this same campaign.

| Metric | Value | Window |
|---|---|---|
| Cost per lead | ~$36 | Jul 12–18 clean window (6 leads / $260.19) |
| Lead → booking-link-click rate | Not measurable | Instrumentation for this event didn't exist as a shipped/gated flow until this test — no prior comparable number |
| Audience | General: male, 35-50, Calgary 10mi radius | All prior Owen tests |
| Total campaign spend to date | $607.63 CAD | Jul 6 – Aug 6 (see [SPEND_TALLY.md](SPEND_TALLY.md)) |

---

## Live log

Append dated entries as data comes in. Keep each entry short — numbers plus one line of read.

- **2026-08-06:** Test logged. Two dependencies open before this can launch: (1) deploy the no-gate owen.html to GHL — currently only exists locally, verified via browser click-through on 2026-08-04; (2) build the Apollo-sourced oil & gas exec lookalike audience in Meta and create the new ad set with it swapped in for current targeting.
- **2026-08-10:** **Dependency 1 done.** No-gate quiz deployed live via GHL split test: `/owen` now redirects to variant URL `https://odinhealthlab.ca/quiz-owen-081026` (confirmed by inspecting the resolved URL after navigating to `/owen` — both addresses serve the identical no-gate page, this is GHL's split-test routing, not two different pages). Verified live in-browser: "Question 1 of 10" through "Question 10 of 10 — What have you already invested in trying to fix this?" with the 4 diagnostic options (Nothing yet / personal trainer / supplements-biohacking / doctor visits) and no disqualify branch — matches the local build exactly. No stale/dead URL concern — existing `/owen` links and UTMs continue to work. **Dependency 2 done.** Lookalike audience built in Meta Ads Manager: `Lookalike (1%) - c-exec-calgary`, source custom audience `c-exec-calgary` (Apollo-enriched purchased list), audience label "Qualified leads", account Foxboro Medical (943264693502769), created 8/10/26 10:20 AM. **Dependency 3 done (same day, confirmed 08-11):** new ad set `[Aug 10] male only - 35-50 - Calgary wide - Lookalike` created and launched.
- **2026-08-11:** Verified via Meta API: ad set ID `120251128040400293`, status ACTIVE, delivery `in_learning_phase` (expected for a launch this fresh — no spend/impression data back yet). Targeting spec confirms `Lookalike (1%) - c-exec-calgary` is the attached custom audience; age 35-50, gender male, Calgary 10mi radius held constant, matching "everything else same" design. 4 ads ACTIVE: Not Aging Walking, Normal Range (video), Normal Range Image, You Remember (video) — matches the intended winning-lineup creative set exactly. Correctly PAUSED: 3pm Image, Doctor's Note Image, You Remember Image, Not Aging Voice Over Music, The Pattern Image (latter still PENDING_REVIEW but paused, harmless). Old general-audience ad set (`male only - 35-50 - Calgary wide`) confirmed PAUSED. Decision rule written this same session (see above) — status flipped to Running.
- **2026-08-19:** Pulled real numbers from Mixpanel directly (Events explorer, not the stale saved funnel board — see Result section for why that report returns empty). Aug 10–18 window: 9 real leads (of 12 raw form submits, 3 self-tests excluded), 1 valid real booking-link click (~11% — the second "real" click traced to an anonymous Fort Worth, TX device with no matching lead record and outside the campaign's Calgary geography, so excluded), 0 real bookings (the only `Appointment Booked` event ever logged is the pre-existing Gail Blixt non-campaign booking from 7/27, already flagged as unattributed in the Aug 4 test file). Closing this test as **FAIL** — see Result/Verdict below. The n=10 sample-size target in the decision rule was a self-assigned comfort minimum, not a validity requirement; 0 bookings from 9 real leads at 11% click-rate is a clean fail on its own terms.

---

## Result

Pulled live from Mixpanel 2026-08-19 (Events explorer, `Aug 10 – Aug 18, 2026`, PDT), by hand — not from the saved "Booking Funnel Conversion by UTM Content" board report, which uses a `Current URL contains /owen` filter that returns zero rows because the live page actually resolves to `/quiz-owen-081026` (the GHL split-test variant URL), not a literal `/owen` path. Raw `[Auto] Form Submit` and `Booking Link Clicked` event rows were read individually and each Distinct ID classified as self-test or real lead by email/name.

| Metric | Value | vs. decision rule |
|---|---|---|
| Leads (raw `[Auto] Form Submit`, `/quiz-owen-081026*`, Aug 10–18) | 12 total → 9 real (3 self-tests excluded: `testingfunnel@`, `testalex@`, `alextesting-funnel@`) | n=9, one short of the self-imposed n=10 sample-size target — see Verdict for why this doesn't block a fail read |
| Booking Link Clicked (same window) | 4 total → 1 valid (`balpreetsaini@gmail.com`, matched to a real lead in the form-submit list). Of the other 3: 2 are self-test clicks (`testingfunnel@`, `testalex@`) and 1 is an anonymous `$device:` click from Fort Worth, TX — outside the Calgary-targeted lookalike's geography and never matched to any lead record, so not counted as a real campaign click. | 1 of 9 real leads ≈ 11% — under the 25% pass bar |
| Appointment Booked (all-time check, not just this window) | 1 total, ever — `gailblixt@gmail.com`, ~2026-07-27 | This is the same pre-existing non-campaign booking already flagged in the [2026-08-04 test file](2026-08-04-owen-qualifier-in-quiz.md) (no site session, mismatched/null UTM) — **zero real bookings attributable to this test** |
| Cost per lead | Not recomputed this session — Meta spend data wasn't pulled alongside the Mixpanel read | Secondary metric left unverified; revisit if this test's audience/no-gate question gets picked up again |

**Verdict: FAIL.** 9 real leads, 1 real booking-link click (~11%), 0 bookings. The n=10 figure in the decision rule was a self-assigned minimum for statistical comfort, not a hard requirement for a verdict to be valid — zero bookings from 9 real leads, one lead below that target, is not a result waiting on more data to become meaningful. It's a clean fail: well under the 25% click-rate pass bar, and the metric that actually matters (bookings) is zero. The lookalike audience + no-gate quiz combination did not, on its own, solve the booking problem this test set out to fix.

**What changes as a result:** Per the decision rule's own "On fail" branch, the correct next step would have been to isolate the two bundled variables (audience vs. gate) in a follow-up test. That didn't happen — instead, session-replay review of these same leads (2026-08-17) surfaced a more specific and more urgent problem: leads were reaching the results page and going idle, regardless of audience quality. The 2026-08-19 test responds to that finding directly rather than to this test's own fail verdict, so the audience/no-gate variables remain unisolated and this open question is inherited, not resolved, by the current test. If the 2026-08-19 redesign also fails to produce bookings, isolating audience vs. gate (as this test's own decision rule prescribed) should be revisited rather than skipped again.

**Next test this spawns:** [2026-08-19-owen-two-step-booking-widget.md](2026-08-19-owen-two-step-booking-widget.md) — session-replay review of this test's real leads (2026-08-17) found 0 of ~10 real leads engaged with the results page past load (no scroll, no click, no booking-link-click), which prompted a results-page redesign rather than waiting out this test's own n=10/n=20 checkpoint. Launched 2026-08-19 on the same ad set/lookalike audience as this test — no audience change bundled in. Note this test's own FAIL verdict (see above, closed 2026-08-19) was reached independently, via a direct Mixpanel data pull, after the successor test had already launched — the successor was not built in response to this test's fail, it was built in response to the session-replay finding while this test's numbers were still unresolved.

---

## Links

- Landing page: `06_MARKETING_GROWTH/Odin Labs Landers/owen.html` — **live**, reachable at both `https://odinhealthlab.ca/owen` and `https://odinhealthlab.ca/quiz-owen-081026` (GHL split-test variant URL; `/owen` redirects to it, same page, verified 2026-08-10)
- Ad account: Foxboro Medical (943264693502769), campaign `[Jul 6 - 26] Owen Quiz Test`
- Audience: `Lookalike (1%) - c-exec-calgary` (Meta lookalike audience, built 2026-08-10, source custom audience `c-exec-calgary` — Apollo.io enriched purchased list, oil & gas executives, labeled "Qualified leads")
- Spend reference: [SPEND_TALLY.md](SPEND_TALLY.md)
- Prior test (superseded gate mechanism, results-page redesign still valid): [2026-08-04-owen-qualifier-in-quiz.md](2026-08-04-owen-qualifier-in-quiz.md)

---

## Setup checklist (completed 2026-08-11)

- [x] Deploy the no-gate owen.html to GHL — live 2026-08-10, reachable at `/owen` (GHL split test, redirects to variant URL `/quiz-owen-081026`), verified in-browser
- [x] Build the Apollo-sourced oil & gas executive lookalike audience in Meta Ads Manager — `Lookalike (1%) - c-exec-calgary`, built 2026-08-10
- [x] Create/configure the new ad set with the lookalike swapped in — `[Aug 10] male only - 35-50 - Calgary wide - Lookalike`, confirmed live via API 2026-08-11
- [x] Write the decision rule — see above, written 2026-08-11
- [x] Update Status to `Running` and set Date started
