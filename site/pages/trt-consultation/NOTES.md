# LP3 - TRT Consultation - staging only

Prepared 2026-11-06 (America/Edmonton). NOT published. No GHL page, calendar, form, global tracking, existing paid page, booking flow or repository changed. New local files only.

## Intent and ads
Destination after approval: https://odinhealthlab.ca/trt-consultation
Audience: men 40-60, Canada-wide, searching for a TRT consultation.
Ads keywords only: TRT consultation; book TRT consultation; testosterone consultation; TRT doctor consultation; low testosterone consultation.
Get-TRT -> LP1 /trt-clinic; cost -> LP2 /trt-cost (ON HOLD, not published). No remarketing audiences.
Who-line: `Odin Health Lab.` (no Calgary; clinician fact lives in subhead only). Screenshots: see dir.

## Pack / preview
- `page.html` and `trt-consultation.txt`: identical complete ASCII Custom Code document. `trt-consultation.html` is a preview alias.
- `verify.py`: static PRD, safety, copy, brand, embed, SEO and tracking checks.
- `page-tracking.js` / `tracking.test.cjs`: extracted script and isolated Node mock tests; never a live booking test.
- `browser-queue.md`: exact creation and approval-gated future publish plan. Do not execute yet.
- Local mirror: `/workspace/pages/trt-consultation/`.
- Existing `0.0.0.0:8780` server is shared and rooted at `/workspace/srv2`. It was NOT stopped or repointed. A new symlink exposes this pack at http://127.0.0.1:8780/lp2-trt-consultation/page.html . Also http://127.0.0.1:8780/page.html (server now rooted at this pack) and /trt-consultation.txt . This serves the pack's actual bytes while preserving other previews.
- Desktop/mobile screenshot targets (NOT CREATED; rendering failed): `desktop-1280.png`, `mobile-390.png`, `mobile-390-fold.png`. See Rendering limitation below.

## GHL SEO panel (required separately on future publish)
- New page name: `[Paid] TRT consultation - Decision Review`
- Slug: `trt-consultation`
- Title: `Free 30-minute TRT consultation, by phone. | Odin Health Lab`
- Description: `Book a free 30-minute TRT consultation by phone. Talk through your options and the right next step with a clinician. Canada-wide, no obligation.`
- Canonical: `https://odinhealthlab.ca/trt-consultation`
- Robots: `index,follow`
- No sitemap tick. Do not select/include in the organic sitemap.
- Same title/description/canonical are in document meta, OG and minimal WebPage JSON-LD; not MedicalClinic. Full-document meta alone may not control GHL's outer SEO head, so set panel fields too.

## Copy / design decisions
Brand is singular Odin Health Lab everywhere. Who-line starts `Odin Health Lab.` with no city; the 15-year clinician fact is in the subhead only. Exact consultation headline first, subhead, call-topics plain bullet list, three ordered outcomes, who-we-are, calendar, reassurance. No invented prices, prescription promise, diagnosis, outcome claims, video/quiz/email gate, qualifier fields, local payment UI or links to /book-now. Zero literal dollar characters in full HTML, including script. Mixpanel's reserved property names use Unicode escapes; regex end anchors use equivalent end-of-input assertions so tracking behaviour remains intact without literal dollar characters.

Reused LP1 `/workspace/lp1-trt-clinic/page.html`: solid #1a3a1a surface, lime #c4ff49, Inter/system stack, same logo and finite branching SVG, divider/spacing patterns, white calendar panel, 44px parent link targets and keyboard focus. Motion uses transform/opacity, 260ms reveal, finite decorative pulses and reduced-motion static state. No shared nav or unrelated modal booking code.

PRD line-count tension: the exact 201-character subhead cannot fit in 2-3 lines at 390px with readable 17px type; it wraps naturally rather than shrinking/truncating. Headline plus complete subhead are prioritised above the 390x844 fold. Who-copy is <=3 desktop lines but wraps naturally on mobile. Calendar deliberately follows all required copy rather than being moved above the disclosure.

## Booking: unchanged existing iframe only
- URL: https://api.leadconnectorhq.com/widget/booking/13UuAtuyZCao4eJyRxrG
- Standard `https://link.msgsndr.com/js/form_embed.js` resizing script.
- Existing calendar ID: `13UuAtuyZCao4eJyRxrG`; slug `trt-decision-review`.
- Existing form ID supplied by PRD: `7nE9Hxt7YJGFyZ0BrXCC` (not independently attached or changed by this page).
- Expected existing configuration, NOT changed or newly verified: 30 minutes, phone; Alex calls from 403-710-1649; rolling 1-6 days; auto-confirm on; first/last optional; phone/email required; notes optional; no qualifiers/payments.
- Parent CSS cannot style the cross-origin iframe's internal fields. Verify 44px phone/email targets and required/optional rules without changing calendar/form settings. No appointment submitted; no claim of CRM arrival/confirmation.

## Tracking / health privacy
LP1 pattern, pathname fixed `/trt-consultation`, `paid_lp:true`. Five deduplicated events: page_view, calendar_widget_loaded, date_picked, form_started, booking_submitted.
Local previews load no page analytics SDKs; dataLayer stays local. The third-party calendar remains live; do not submit test appointments.
On live domain only: reuse or initialize Mixpanel, autocapture/replay disabled, no identify/people/audiences, blacklist URL/referrer properties, no raw payloads, form values, dates, query strings or contact data. Same existing public analytics identifiers as LP1.
Meta/Google ad base tags require `window.odinAnalyticsConsent === true` from an existing CMP. Default off. No explicit Meta health-page events, no Google auto page_view, no Google signals/ad personalisation; restricted_data_processing true. No audience creation or remarketing code. Existing header/GTM/account rules must separately exclude health traffic; this pack cannot undo prior tag hits. Do not edit global tags as part of this task.
`calendar_widget_loaded` means iframe load only, not proof of usable dates. Remaining steps are BEST EFFORT: only explicit supported messages from this iframe's exact public widget origin; wrong origin/source, raw payloads, resize arrays and unknown messages are rejected. The widget may not emit supported date/form messages. No events fabricated from focus or height. Same-origin observation is guarded; never bypass browser policy. Reliable end-to-end reporting needs documented supported widget/server instrumentation approved separately.

## Design review (web principles, not native app conventions)

## LIVE 2026-11-06 ~12:05 PM America/Edmonton
- Public: https://odinhealthlab.ca/trt-consultation (HTTP 200)
- GHL name: [Paid] TRT consultation - Decision Review
- Builder: https://app.jumpconvert.com/location/Q6uTvwNHOg3F0JyLXiUV/page-builder/dKESibpoPlaeWCwudm5g
- Builder id: dKESibpoPlaeWCwudm5g
- Possible funnel step id (from tab URL; verify): 7a7e54ad-f727-4759-a441-0388f79d6f71
- Paste md5: 7e525dd55b3f8961b4e4d57aa93fd15c
- No IndexNow/Indexing (paid ads LP)
- /trt-cost remains Hold; booking/calendar untouched
