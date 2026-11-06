# [Paid] LP1 - Looking for a TRT clinic?

Status: LOCAL STAGING ONLY. Not published. No GHL, calendar, form, /book-now, sitemap or repository changes.
Prepared Nov 6, 2026 (America/Edmonton).

## Purpose and audience
Canada-wide men 40-60 searching to get TRT: TRT clinic near me; testosterone clinic near me; TRT clinic Calgary; testosterone clinic Calgary; how to get TRT in Canada; how can I get TRT; low testosterone treatment near me; testosterone doctor near me.
Only this keyword group belongs here. Cost searches belong on LP2; consultation searches on LP3.
Ads should use https://odinhealthlab.ca/trt-clinic directly after approval. Do NOT add to the organic sitemap list yet. Default robots: index,follow.

## Files and preview
- page.html: complete, self-contained Custom Code Main Content document, matching the Calgary full-document paste-pack convention.
- trt-clinic.txt: byte-identical ASCII text/plain paste copy.
- verify.py: static copy, embed, brand, safety and metadata checks.
- tracking.test.cjs: isolated Node mock tests (not a browser or actual booking).
- browser-queue.md: approval-gated GHL creation/publish and QA steps.
- Main preview: http://127.0.0.1:8780/trt-clinic.html
- Paste: http://127.0.0.1:8780/trt-clinic.txt
- Source copies: /workspace/lp1-trt-clinic/ and /workspace/pages/trt-clinic/.
- Screenshots: not captured by this executor; no browser/desktop delegation tool was available. Parent must capture desktop-1280.png and mobile-390.png in this folder and mirror them before calling browser QA complete. Do not substitute a rendering mockup for a browser screenshot.

## Copy and branding
Exact H1: Looking for a TRT clinic? Before you start, get a clear answer first.
Title: Looking for a TRT clinic? | Odin Health Lab
Description: A free 30-minute TRT Decision Review call. Talk through whether TRT or another first step makes sense. Canada-wide, by phone. No obligation.
Canonical: https://odinhealthlab.ca/trt-clinic
og:site_name: Odin Health Lab

Used the PRD copy verbatim except Labs -> Lab. Preserved the supplied subhead's "has been on TRT for 15 years" as a fact about the clinician, not an outcome claim; equivalent to the PRD copy-rule wording "has used TRT". "Start TRT now" is one possible call outcome, not an offer to prescribe: the immediately adjacent who-we-are copy states that we are not a TRT clinic and do not sell TRT.
No FAQ, quiz, extra gate, prescription promise, price list, payment form or before/after assets.

Tension resolved: the entire 172-character subhead cannot fit in two mobile lines at a readable font size. It wraps naturally on phones, never truncates, and the layout prioritizes keeping H1 + full subhead above the fold at a typical 390px-wide phone. Likewise who-we-are uses <=3 desktop lines but wraps naturally on mobile. Browser confirmation is still pending. Do not shrink or clip text to force the line-count targets.

## Visual design
Solid #1a3a1a across the page and GHL section wrappers; no darker green bands. White calendar panel is the expected booking UI exception. Lime #c4ff49; Inter/system font stack, heavy tightly spaced H1, site logo, soft calendar corners. Reused LOGO and chat icon from /workspace/pages/_shared/common.py; borrowed design tokens and motion conventions, not the long organic builder's nav/modal/FAQ machinery (which would introduce unrelated booking links and copy).
Short structure: brand, hero, plain ordered outcomes, who-we-are, embedded calendar, under-calendar reassurance, minimal privacy footer. No additional primary button: calendar is the CTA.
Small SVG branches from one conversation to three next steps; two brief pulses only, not an infinite distracting loop. Below-fold copy reveals use transform/opacity, 260ms easing. Reduced motion and no-JS show all copy in its static final state. No content is hidden until a script loads. Keyboard skip link, visible focus, semantic heading/list, titled iframe, no zoom restriction.

## Calendar (unchanged)
Calendar ID: 13UuAtuyZCao4eJyRxrG
Calendar slug: trt-decision-review
Attached form ID from PRD: 7nE9Hxt7YJGFyZ0BrXCC
Public URL returned HTTP 200 during preparation: https://api.leadconnectorhq.com/widget/booking/13UuAtuyZCao4eJyRxrG
Embedded as the standard width:100% iframe with form_embed.js, no modal or /book-now link. 660px minimum height; the standard script owns live resizing. No additional resize/custom code injected into calendar.
Expected existing configuration from PRD, NOT verified/modified here: 30-minute phone call, Alex calls from 403-710-1649; rolling 1-6 day window; auto-confirm on. First/last name optional, phone/email required, notes optional; no qualifier fields, no payments.
The iframe owns its tap targets, form validation, availability and confirmation. Parent must visually inspect on mobile; parent-page CSS cannot safely style inside this cross-origin widget. Do not claim a successful end-to-end booking from a 200 response or static check. No appointment was submitted.

## Tracking and privacy
Local previews are analytics-dry: events go to local dataLayer only, no Meta/Google/Mixpanel SDK loads. The widget itself is real/live; do not submit it without explicit approval for a test appointment.
On odinhealthlab.ca only:
- Mixpanel token 9c1ce1f2580971e0928ba7cc09cb542e: guarded SDK initialization, reuses an existing instance; autocapture and replay disabled for the page; no identify/people/audience calls, query strings, form values or raw message payloads. Page event properties are only fixed pathname /trt-clinic, paid_lp:true, source. Standard URL/referrer properties are blacklisted on a newly initialized or existing instance. Existing site/header scripts may have already fired before Main Content; audit those before launch.
- Meta Pixel 705890611034328 and Google AW-18027994169: guarded base loaders, run ONLY when an existing CMP has set window.odinAnalyticsConsent === true before this page script. No CMP is invented here. Default is NOT to load those SDKs. Existing tags are not reinitialized. This is a deliberate safety constraint for sensitive-health traffic: no explicit Meta PageView/Lead/booking event; Google send_page_view:false, allow_google_signals:false, allow_ad_personalization_signals:false, restricted_data_processing:true. No noscript ad beacon. Confirm CMP/policy with Alex before enabling ad tags. No REPLACE_LABEL was introduced or edited; calendar conversion code remains untouched.
- No audience is created by this pack. Existing header/GTM/ad-account audience rules must separately exclude this health LP. Main Content cannot undo prior tag hits or control account-side audience definitions.

Events to Mixpanel and dataLayer, deduplicated once each per page load:
1. page_view: implemented directly; pathname fixed to /trt-clinic even during local previews.
2. calendar_widget_loaded: iframe load. This proves only the frame load, NOT that dates rendered or booking was usable; a failure page could also trigger load.
3. date_picked: best effort, only an explicit trusted widget date-selected message.
4. form_started: best effort, only an explicit trusted form-start message (or input on a same-origin widget in the future).
5. booking_submitted: best effort, trusted explicit completion messages including msgsndr-booking-complete, appointment_booked, booking_complete/success. This indicates a reported confirmation, not an independently verified CRM appointment.
Message checks require exact widget origin https://api.leadconnectorhq.com AND event.source === this iframe.contentWindow. Unknown messages and resize/height arrays are ignored, never mislabelled as a date/form/booking step. Payloads and field data are never sent onward. Supported message aliases are hypotheses based on site practice, NOT an assertion that this live widget emits them.
MutationObserver and input listeners are guarded behind same-origin contentDocument access. The live LeadConnector frame is cross-origin, so no DOM/text/field observation is available; no bypass is attempted. Date selection and form start may be completely unobservable. Resizing works through GHL's external standard script. No synthetic step events are fabricated from resizing or iframe focus.
No actual live event emission or conversion was tested. Reliable full-funnel reporting would need supported widget instrumentation or approved server-side HighLevel appointment events, outside this page task. Do not change calendar code to get it.

## Publish procedure (only after Alex says yes)
See browser-queue.md. Create a NEW website page /trt-clinic in GHL JumpConvert. Paste the full text pack into Main Content only, set SEO panel to the fields above, verify desktop/mobile, then publish only with approval. Do not modify global Header Tracking when funnel-level tags exist. Audit duplicates/privacy externally; stop rather than changing existing calendars, forms, widgets or global tracking.

## QA / design review
Static PRD and isolated tracking checks can pass independently of browser QA.
Design review applies web accessibility/layout principles, not native iOS navigation conventions:
- accessibility.md > Vision: high contrast text and scalable fonts; layout.md > Adaptability: natural wrap, no clamp/truncation; motion.md > Best practices: motion optional.
- Computed contrast for #fff / #1a3a1a and #dce5d9 / #1a3a1a is recorded in qa-results.txt.
- Outstanding: true 390px/1280px screenshots, no horizontal overflow at both sizes, phone+email tap targets, real widget date selection without submit, Google app in-app-browser check. No real-device or screen-reader audit was performed.

| Before | After | Why |
| --- | --- | --- |
| Generic shared organic page with unrelated modal choices | One on-page Decision Review calendar | Keep the paid search task short and focused |
| Potential forced 2-line mobile subhead | Natural 17px wrapping, full copy | Readability over a physically impossible line count |
| Infinite decorative animation | Two finite SVG pulses + short reveals | Motion without distracting from the calendar |

## Staging validation
Preview and text paste both HTTP 200 from the existing :8780 server; response bytes exactly match page.html (16,047 bytes; SHA-256 b85c5757d46835d70d3e054314f82068cd1493fc6b43205dbb00f570c08def89). Attempting to start another server found the port already in use; reused it without changing it.

Memory logging limitation: cmem was unavailable (command not found; documented /usr/local/bin/cmem also absent). Recall/spool/save could not run. Used local reference packs; no memory recall or accepted spool event is claimed.

## Edit 2026-11-06 ~10:51 AM America/Edmonton
Alex (t215u): remove Calgary from who-line — no need to mention where we are located. Now: "Odin Health Lab." Verify 40 PASS. md5 505f312b556c1b5b00299b8213765a25.
