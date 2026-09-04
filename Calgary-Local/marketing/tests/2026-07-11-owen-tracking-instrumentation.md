# [INFRASTRUCTURE — not a test] Fixing UTM capture and instrumenting the qualifier funnel in Mixpanel

**Funnel:** owen-quiz-funnel
**Status:** Concluded — DONE (not a pass/fail test; foundational fix + instrumentation that later tests depend on)
**Date started:** 2026-07-11
**Date concluded:** 2026-07-11

---

## The change

Three separate fixes/additions to `owen.html`, all shipped same day:

1. **UTM capture fix.** GHL renders the quiz's custom-code block in an iframe whose own URL carries no query string, so `URL_PARAMS` was reading `window.location.search` and always getting nothing. Fixed with a fallback chain: own URL → `window.parent.location.search` → `document.referrer` parsed as a URL. This is what let the webhook payload finally carry `utm_content`/`utm_campaign`/`fbclid` on lead submission. Verified live with a tagged test submission (`utm_content=TEST-utm-fix`) — confirmed present in the GHL webhook payload.
2. **Mixpanel identity + device-id bridge.** Added `mixpanel_id` (device distinct_id, read from `window.parent.mixpanel`) to the webhook payload, and `mixpanel.identify(email)` + `people.set()` fired on lead submission — merges the visitor's full anonymous pre-lead session history (ad click, quiz answers, replay) into an email-keyed profile the moment they convert.
3. **Qualifier-funnel event instrumentation.** Added 4 custom Mixpanel events that didn't exist before: `Results CTA Clicked`, `Qualifier Answer` (props: gate, answer), `Qualifier Passed` (props: payment, philosophy), `Booking Link Clicked`. Previously the entire post-lead journey (did they click through to book?) was invisible in Mixpanel — only the Meta AddToCart pixel fired, with no per-step visibility.
4. **GHL → Mixpanel booking webhook.** New GHL workflow (trigger: Customer Booked Appointment → POST to `api.mixpanel.com/track`) sends an `Appointment Booked` event keyed to the contact's email, completing the chain: ad → session → quiz → lead → booking, all under one identity. Payload validated live against the Mixpanel track API before handoff (test event `webhook-setup-test@odinlab.test`, `is_setup_test: true`).

Same fixes applied to `emma.html` (identical bug, not yet in active use).

## Why

Before this, attribution required manual timestamp-matching between a GHL lead's submission time and Mixpanel session data — workable at ~1 lead/day, not scalable, and the post-lead funnel (results page → CTA → qualifier → booking) had zero step-level visibility. This blocked any rubric-style analysis of *where* leads were dropping off, which became essential once the "6 leads, 0 qualifier reaches" pattern emerged.

## Decision rule

N/A — infrastructure fix, not a hypothesis test.

## Baseline (before this change)

| Metric | Value |
|---|---|
| UTMs on lead webhook payload | None (bug — iframe URL always empty) |
| Mixpanel↔GHL lead matching | Manual timestamp correlation only |
| Post-lead funnel visibility in Mixpanel | None (only Meta pixel AddToCart, no per-step breakdown) |
| Bookings visible in Mixpanel | None |

---

## Live log

- **2026-07-11:** All 4 changes shipped to `owen.html` and `emma.html`, syntax-checked, deployed to GHL. UTM fix verified live with tagged test URL. Booking webhook payload validated via direct API call before GHL workflow setup instructions were handed off (GHL workflow itself must be created manually in the GHL UI — outside what can be done via API).
- **2026-07-11 (later):** Live end-to-end test run through the full funnel (quiz → email → CTA → both qualifiers "yes" → booking link) confirmed all 4 new events fire and attach to the identified email, not an anonymous device ID.
- **2026-08-04:** Built the "Booking Funnel Conversion by UTM Content (/owen)" saved Mixpanel funnel report (5 steps: Form Submit → Results CTA Clicked → Qualifier Answer → Qualifier Passed → Booking Link Clicked, broken down by utm_content) — this is the reporting layer that consumes the instrumentation added here. Saved to the "Owen Quiz Test" board.

---

## Result

Instrumentation confirmed working end-to-end. This is what made the `2026-08-04-owen-qualifier-in-quiz.md` test's decision rule (qualifier-pass rate as primary metric) measurable at all — without this, that test would have no way to see the funnel step it's trying to fix.

**One open gap noted at the time, not yet closed:** the GHL booking webhook has no calendar/source filter, so it captures *every* clinic booking, not just Owen-funnel-attributed ones. This caused two false positives during the Jul 13–Aug 3 review (Jill Norman, Gail Blixt — both traced to non-Owen sources via missing/mismatched UTMs). Flagged as a to-do, not yet fixed.

**Verdict:** N/A (infrastructure)

**What changes as a result:** All subsequent Owen tests can measure qualifier-step and booking-step conversion directly instead of inferring it from session replays.

**Next test this spawns:** N/A directly, but is a hard dependency of `2026-08-04-owen-qualifier-in-quiz.md`

---

## Links

- Code changes: `06_MARKETING_GROWTH/Odin Labs Landers/owen.html`, `emma.html`
- Webhook setup doc: `06_MARKETING_GROWTH/ghl-mixpanel-booking-webhook.md`
- Mixpanel report: "Owen Quiz Test" board → "Booking Funnel Conversion by UTM Content (/owen)"
- Related memory: `project_meta-capi-status.md`
- Open to-do: filter/tag the GHL→Mixpanel booking webhook to only fire for Owen-sourced bookings (or add a source property to the payload)
