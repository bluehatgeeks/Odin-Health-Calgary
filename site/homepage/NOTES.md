# Homepage rewrite: notes

Files: `home.html` (paste into the HighLevel custom-code block), `llms.txt`, `robots.txt`, `sitemap.xml` (live one is empty), `seo-meta.md` (10 pages), `og-home.png`, `build.py` + `home.template.html` (source; FAQ HTML and FAQPage JSON-LD are generated from one list so they stay identical).

## Before pasting
1. Commit `og-home.png` to the repo as `img/og-home.png` (og:image points to its jsDelivr URL).
2. Mixpanel init and the "Page View" event are NOT in the repo. They live in the site-level tracking code in GHL and stay untouched. `home.html` only adds `mixpanel.track('CTA Click', {cta, page:'home'})` (guarded, no-ops if Mixpanel is absent). `cta` values: hero_free_assessment, hero_how_it_works, symptoms_free_assessment, how_free_assessment, final_free_assessment, final_book_call, modal_first_time, modal_follow_up, nav_book_online.
3. Removed the `YOUR_PIXEL_ID` fbq block and its noscript twin. A real pixel (705890611034328) is already injected site-level, so Meta PageView still fires.
4. Shared nav/footer are NOT changed and still say "Calgary" (footer: "Functional Health Calgary", "Made in Calgary"). Nav "Take The Assessment" points to `/#metabolic-assessment-trigger`; the home page keeps that id on the final CTA so it still works. Better: point it to /owen-lowt.
5. The booking modal and its script are kept because the nav "Book Online" button depends on them. The old metabolic quiz panel and its JS were removed (replaced by the link to /owen-lowt). The About section is now visible in the HTML, no longer hidden behind a toggle. FAQ hover-open behaviour removed (native click/keyboard only).

## Compliance flags: human/legal review
- **"Clinician" vs "we do not practice medicine".** I dropped the slogan and the "Do you practice medicine? No" FAQ, since they contradict the strategy notes' "clinician call". The page now says "a clinician from the Odin Health Labs team". Confirm who staffs the calls, their licences and title (also "Clinical Director & Founder" on the founder card, "Hormone and Functional Lab Interpretation").
- **Cross-border licensing/scope:** "serves men across Canada and the USA" needs a licence/scope check per province and US state. The pivot note records the owner's view that this is fine; I have not verified it.
- **Hormone therapy wording (FAQ 5):** says medical treatment "including hormone therapy" is handled by the physician who provides it, and does not state whether Odin prescribes. Confirm that is true.
- **Medical-claim language:** page avoids diagnose/treat/cure and has no efficacy numbers, urgency or scarcity (removed "14–30 days", "Limited spots"). "Total vs free testosterone" and "cause list" content comes from your taxonomy notes and is unsourced on-page; add citations if desired. The "40% of men over 45" stat in the notes was left out (no source link).
- **Disclaimer + 988/911 line** at the bottom: review wording. Privacy policy still says "Calgary, AB" and needs PIPEDA/PHIPA/HIPAA-style review for Canada+USA health data (assessment answers).
- **Testimonials removed:** the three "Calgary ..." quotes were unattributed and Calgary-framed. Add real, consented ones later.
- **Schema:** Organization uses the phone (+1 587 324 8710) and email from the footer. No address, no sameAs (add social profiles if you want them). Typed `Organization`, not `MedicalBusiness`, until licensing is confirmed.
- **Linked pages not yet rewritten:** /pemf, /hydrogen-inhalation, /marma-therapy, /shift, /privacy and others still describe in-clinic or Calgary services. They are linked for internal linking only; each needs a telehealth/andropause pass (see `seo-meta.md` notes). The old hero image (Calgary skyline, women, new mother) and "New Mothers" profile were removed; a men-focused hero photo is still needed.
- The nav links to /owen-lowt were not changed. That page is only linked, never modified.

## Motion graphics (v2, 2026-10-15)
Source: `home.template.html` (edit this, then `python3 build.py` → `home.html`). Previous version: `home.v1.html` (+ `home.template.v1.html`). Screenshots and test runs: `shots/`.
- **Hero**: inline SVG "signal" card beside the headline (stacked under it on mobile, fixed `aspect-ratio` so no layout shift). One path (flat line → rising curve) draws on in an 11s loop (muted grey → lime gradient stroke), nodes pop in as the pen passes them, a white "pen" dot rides the path (CSS `offset-path`), soft radial-gradient glow + pulse ring on the end node, floating particles. Labelled "illustration only, not a measurement or a promise of results". No numbers, no stats.
- **Symptom icons**: 11 inline SVGs, strokes draw on (`stroke-dashoffset`, `pathLength=1`) when each pill scrolls in, staggered 60ms. The same `.draw` class also animates the authority-bar icons.
- **How it works timeline**: `[data-timeline]` wrapper with a track + fill. Scroll sets `scaleY` on the fill (one rAF-throttled passive listener, active only while the section is near the viewport); each step's dot fills and card fades in when the line reaches it, with a one-shot ring. Fully drawn with JS off.
- **Reveal**: existing IntersectionObserver `.reveal` (opacity + translateY 12px, 320ms, 50ms stagger via `--i`). Hero copy has a 560ms load stagger (`.hero-in`; the H1 is deliberately not animated, to protect LCP).
- **Buttons/cards**: hover lift gated by `(hover:hover) and (pointer:fine)`; `:active` scale(.97). **FAQ**: plus icon rotates to ×, answer fades/slides in 280ms, `::details-content` height eases where supported. **Final CTA**: three expanding halo rings behind the button.
- **Rules followed**: transform/opacity for UI motion (only exception: SVG stroke draw on tiny paths); custom ease-out `cubic-bezier(.23,1,.32,1)`; no `transition: all`; no filters/blur; loops pause off-screen (`[data-live].is-paused`, set by IntersectionObserver); hidden tabs are throttled by the browser.
- **Reduced motion / no JS**: loops, draw-ons and reveals are off and every element shows its final state (verified: 0 running animations under `prefers-reduced-motion`, nothing hidden with JS disabled).
- **Tested** (headless Chrome 154, 1280 and 390 wide): no console errors/warnings, no failed requests, CLS 0, no horizontal overflow. Not yet checked: real-device FPS, Lighthouse in GHL (run it after pasting; the nav/footer fetch and tracking are outside this file).
- **Not changed**: SEO head, JSON-LD (byte-identical to v1), FAQ content, nav loader, booking modal, all `data-cta` events.
