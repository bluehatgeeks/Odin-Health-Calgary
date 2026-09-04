# Moving the cash-pay/philosophy qualifier into the quiz (before the email gate) will produce leads that actually book, instead of leads that read the results and leave

**Funnel:** owen-quiz-funnel
**Status:** Superseded — never deployed. See [2026-08-06-owen-qualified-audience-no-gate.md](2026-08-06-owen-qualified-audience-no-gate.md).
**Date started:** 2026-08-04 (build/local-verify only)
**Date concluded:** 2026-08-06 (superseded before launch)

**Correction (2026-08-06):** The line below previously claimed owen.html was "deployed live to GHL" and the ad set relaunched — this was **incorrect**. The in-quiz hard-gate mechanism described in "The change" below was built and verified locally on 2026-08-04 but was never pushed to GHL and the ad set was never relaunched with it. Before deployment happened, the underlying premise was revisited: gating a general audience was diagnosed as solving an audience-quality problem with quiz friction. The gate mechanism here was replaced (not deployed, then redesigned) by a no-gate approach paired with a pre-qualified lookalike audience — see the superseding test. The results-page tease redesign described below (cutting the full protocol delivery down to a teaser) is real, was verified locally, and its status independent of the gate question is unclear — confirm current owen.html state before assuming either piece is live.

---

## The change

1. **Qualifier moved upstream.** The two qualifier questions (cash-pay willingness, natural-protocol philosophy) used to appear *after* the results page, gated behind a second click on "Book Your Full Intake." They are now **Q10 and Q11 inside the quiz itself**, before the email capture step. A "no" answer routes straight to the disqualified screen — the visitor never becomes a lead.
2. **Results page cut from full delivery to a tease.** Previously showed all 5 symptom-pattern bullets, a "why standard protocols miss this" block, an age-adjustment block, and a full 4-phase protocol timeline. Now shows only 3 pattern bullets and a single teaser block ("On your call, we'll walk through: ...") — one CTA, straight to the booking widget, no second qualifier step.
3. **Creative refresh, same avatar/format.** Keeping the only creative that has ever produced a real lead (**Not Aging Walking** — UGC-style talking-head selfie video, same avatar, same burned-in caption style) as the control, and adding two new videos in the same format: **Normal Range** (cynicism/"normal range" angle) and **You Remember** (nostalgia angle). Keeping **Normal Range (image)** as the one surviving image creative. Cutting Voice Over Music (video) and the 3 image creatives that never produced a lead (3pm, Doctor's Note, The Pattern).

## Why

2026-07-13 to 2026-08-03 result (the run that followed [2026-07-10-owen-audience-network-cut.md](2026-07-10-owen-audience-network-cut.md), measured using the instrumentation from [2026-07-11-owen-tracking-instrumentation.md](2026-07-11-owen-tracking-instrumentation.md)): ~16 total leads across the test period, **0 ever clicked through to the qualifier step**. Rule-of-three math on 0/16 puts the true CTA-click rate below ~17% at 95% confidence — under viability. Session-replay review of all 6 clean, fully-tracked lead journeys (post the mid-test tracking fix) showed the same pattern every time: engaged quiz completion (2-4 min, real answers) → email submitted → results page read in full → nothing. The results page over-delivered (full protocol timeline) and gave no reason to click further. Root cause read as: qualification happening too late, and the results page being the product instead of the trailer.

*Note: the two "Appointment Booked" events seen in this window (Jill Norman 7/13, Gail Blixt 7/27) were traced via Mixpanel session data to NOT be attributed to this campaign — no site session, no quiz, mismatched/null UTM. True campaign-attributed bookings for the prior test: 0.*

## Decision rule (locked before launch — do not edit after data starts coming in)

- **Sample size to reach a verdict:** 20 clean leads (post-GHL-deploy, excluding any self-tests — tag self-tests with a distinguishable UTM or email so they can be filtered)
- **Metric:** qualifier-pass rate (visitors who answer both Q10 and Q11 "yes"/"maybe" and reach the email gate, as a % of quiz starts) — this is the primary metric, since the whole point of the change is to stop unqualified people from becoming leads at all. Track it alongside lead→booking-link-click rate as a secondary check that the tease-results-page change didn't kill conversion for people who DO qualify.
- **Pass bar:** ≥15% qualifier-pass rate at n=20 (rule-of-three viability floor established in the prior test's economics: ~$36/lead × ~$150 assumed value of a booked intake → need ≥1 in ~15 qualified)
- **Fail bar:** <15% at n=20 → extend to 30 leads before final call, per rule-of-three (30 leads ≈ full price of a conclusive answer)
- **On pass:** funnel is viable, keep running, start optimizing cost-per-qualified-lead and watch actual booking rate among the qualified
- **On fail:** the disqualify-early hypothesis was right about being *needed*, but something else is still broken downstream (booking-link click-through, or the results-page tease isn't compelling enough) — next test targets that specifically

## Baseline (before this change)

| Metric | Value | Window |
|---|---|---|
| Total spend | ~CA$272 | Jul 13 – Jul 18 (active), through Aug 3 (paused) |
| CTR | 2.54% | Jul 13–18 |
| Cost per QuizStart | CA$6.09 | Jul 13–18 |
| Leads (real, identified) | 6 | Jul 13–18 |
| Cost per lead | ~CA$36 | Jul 13–18 |
| Qualifier-step reach rate | 0% (0 of 6) | Jul 13–18 |
| Campaign-attributed bookings | 0 | Jul 6 – Aug 3 |

---

## Live log

Append dated entries as data comes in. Keep each entry short — numbers plus one line of read.

- **2026-08-04:** owen.html restructure built and verified locally (full click-through test of disqualify path and happy path, both confirmed working). New Normal Range and You Remember video ads received from HeyGen, verified (720×1280, 30–34s, correct avatar), filed in `Odin Labs Calgary Meta Ads/`. **Correction:** this entry originally claimed the deploy and ad relaunch had happened — they had not. Local verification only; nothing pushed to GHL, ad set not relaunched.
- **2026-08-06:** Premise revisited before deploy ever happened — see the superseding test file. This test's gate mechanism will not be deployed as designed here.

---

## Result

*(Intentionally empty — not an oversight.)* The gate mechanism described in "The change" was never deployed to GHL and the ad set was never relaunched with it (see the correction note at the top of this file). There is no traffic, no leads, and no click data that ever ran against this design, so there is nothing to measure against the decision rule above. The results-page tease redesign bundled into this same file's "The change" section (cutting full protocol delivery down to a teaser) is a separate, real, shipped change — but this file's decision rule was written specifically around qualifier-pass rate, which requires the gate to have existed in production. Confirmed 2026-08-19 via Mixpanel: no `Qualifier Answer`/`Qualifier Passed` events exist in the funnel's production event history for any window after this file's build date, consistent with the mechanism never having shipped.

**Verdict:**

**What changes as a result:**

**Next test this spawns:**

---

## Links

- Landing page: `06_MARKETING_GROWTH/Odin Labs Landers/owen.html` (restructured and live on GHL)
- Ad creative: `Calgary-Local/marketing/Odin Labs Calgary Meta Ads/` (moved here in the 2026-09-04 reorg) — `quiz - Normal Range - video ad.mp4`, `quiz - You Remember - video ad.mp4`, `quiz - Not Aging Walking...`, `quiz - normal range - image ad.png`
- Ad account: Foxboro Medical (943264693502769), campaign `[Jul 6 - 26] Owen Quiz Test` / ad set `male only - 35-50 - Calgary wide`
- Mixpanel: Odin Health Labs project, "Owen Quiz Test" board, "Booking Funnel Conversion by UTM Content (/owen)" saved funnel report
- Related memory: `project_meta-capi-status.md` (event architecture — quiz events are browser-side, only Schedule is server-side via GHL)
- Prior tests (logged retroactively 2026-08-04):
  - `2026-07-07-owen-first-image-ad-batch.md` — 5-image creative batch, inconclusive on its own terms but established Not Aging Walking + Normal Range as the only working creatives
  - `2026-07-10-owen-audience-network-cut.md` — AN placement cut, PASS, established Jul 11 as the clean-data cutoff
  - `2026-07-11-owen-tracking-instrumentation.md` — UTM fix, Mixpanel identity bridge, qualifier-funnel event instrumentation, booking webhook (infrastructure, not a test, but this test's decision rule depends on it)
