# /functional-health rewrite (local only, NOT published)

Files: `page.html` (self-contained, paste into the GHL custom-code "Main Content" element), `build.py` + `page.template.part1.html` (head, base CSS), `part2` (motion CSS + JSON-LD slot), `part3` (body, graphics slots, JS). Run `python3 build.py` to regenerate. FAQ HTML and the FAQPage JSON-LD come from one list in `build.py`. `shots/` holds screenshots (1280 and 390, two moments per loop, reduced-motion and no-JS full pages). `test-visual.js` / `test-tracking.js` are the puppeteer-core checks (copies; they run from /workspace/hp-test).

Page is the same pattern as `/workspace/homepage/home.html`: inline CDN CSS (odin-shared.css, odinlabcalgary.css), inline nav/footer loaders, booking modal kept (nav "Book Online" needs it), CTA tracking via guarded `mixpanel.track('CTA Click', {cta, page:'functional-health'})`.

## SEO
- Title (58 chars): "Functional Health for Men: Find the Root Cause | Odin Labs". Description (159 chars) in `build.py`.
- Canonical `https://odinhealthlab.ca/functional-health`, OG + Twitter tags. og:image reuses `og-home.png` (needs committing to the repo as `img/og-home.png`, same dependency as the homepage). A page-specific OG image would be better.
- JSON-LD: Organization (same @id as the homepage), WebSite, WebPage (with breadcrumb + mainEntity FAQ), BreadcrumbList, FAQPage (6 Q&As, text identical to the on-page FAQ with link tags stripped).
- Internal links: homepage (hero, FAQ, related card, breadcrumb), /health-coaching and /supplements (step 3, related cards), /privacy (FAQ), CTA to /owen-lowt (hero, labs, how-it-works, final). All have `data-cta`.
- `cta` values: hero_free_assessment, hero_our_approach, hero_home_link, crumb_home, labs_free_assessment, how_free_assessment, how_health_coaching, how_supplements, related_health_coaching, related_supplements, related_home, final_free_assessment, final_book_call, modal_first_time, modal_follow_up, nav_book_online.

## Motion graphics (every section has its own, all inline SVG/CSS, `aria-hidden`, no text inside, no numbers)
| Section | Graphic |
|---|---|
| Hero | "Look below the surface": three symptom chips above a dotted ground line, five roots draw down to five cause nodes (sleep, stress, nutrition, training, weight), a magnifier sweeps across and lights each node in turn |
| Symptoms vs root cause | Left: a ring and a dot going round and round. Right: a line draws straight down through nodes to a root, a dot falls along it and a ring pulses, two branches fan out |
| Five areas | Five dials (equalizer): bars scale and knobs slide at different paces; each card icon chip pulses in turn |
| Why together | Closed loop: four nodes (sleep, stress, weight, hormone drop) joined by drawn arrows, a dot travels the ring and each node lights as it passes |
| Labs / physician | Fork: one lane to a plan, one dashed lane to a physician; a flask fills and bubbles; packets travel each lane in turn; end nodes pulse |
| How it works | Scroll-filled timeline (as homepage) with four new step icons: clipboard lines drawing, two chat bubbles alternating, map pin bouncing over a route, calendar with a moving day marker |
| Related support | Coach and supplement nodes linked to you; packets flow along both links, the capsule sways, rings pulse |
| FAQ | A magnifier sways while a question mark draws inside it; sparkles blink |
| Final CTA | A compass needle swings once and settles on north, then wobbles slightly; halo rings; the existing button halo |

Rules followed (motion-checklist.md, Emil Kowalski animate / animation-performance, Apple HIG): transform and opacity for every loop (no offset-path, no dash-flow loops, no filters, no `transition: all`, nothing starts below scale .7), stroke-dashoffset only for one-shot draw-on of small paths, ease-out custom curves for entrances, loops 3-14s and slow, hover only on `(hover:hover) and (pointer:fine)`, `:active` scale .97, 48px buttons, visible focus rings. Loops pause off-screen through the existing `[data-live].is-paused` IntersectionObserver. Default CSS is the final state: every animation is gated by `prefers-reduced-motion: no-preference` AND the `.js-reveal` class that JS adds, so reduced-motion and no-JS users get complete static graphics and nothing hidden. Each figure has a fixed `aspect-ratio` (CLS 0).

## Tested (headless Chrome 154, puppeteer-core, file:// build, 1280 and 390 wide)
Console errors/warnings 0, failed requests 0, CLS 0, no horizontal overflow, one h1, no duplicate ids, JSON-LD parses and FAQ questions match the DOM one-to-one, reduced motion: 0 running animations and nothing hidden, JS disabled renders everything, 0 figure animations running while scrolled to the top (pause works). Tracking: stubbed `window.mixpanel`, clicked 5 CTAs plus the booking trigger, all fired `CTA Click` with `page:'functional-health'`. Not checked: real-device FPS, Safari/Firefox, Lighthouse inside GHL.

## Compliance flags (human / legal review)
1. **What was removed from the old page** (all unverifiable or promissory): "We Do Not Practice Medicine", the Cleveland Clinic study numbers (7,252 patients, 31%), "6 advanced diagnostic panels", the condition list (IBD, Hashimoto's, PCOS, rheumatoid arthritis, chronic fatigue, type 2 diabetes...), "reduce or eliminate dependency on medications", "chronic illness reversal", "optimal vs normal ranges" claims, the 4-8 week and 3-6 month timelines, "60-90 minute intake" and the naturopathy and family-doctor comparisons. The old clinical-evidence section and citations are gone. If you want evidence on the page, add sourced, hedged citations.
2. **"Clinician" and who staffs the calls.** Copy says "a clinician" (same as the homepage). Confirm titles and licences, and whether they may practise in every province and state served.
3. **Who orders and reviews labs and who prescribes.** Copy says tests are "ordered and reviewed by a physician where required" and that medical treatment including hormone therapy is "handled by a physician". Confirm that matches how Odin actually works (own physician network vs the man's family doctor) before publishing; adjust the lab card, FAQ 1 and FAQ 3.
4. **Cross-border scope:** "serves men across Canada and the USA" needs the same licensing check as the homepage (not verified).
5. **General health statements, unsourced on the page** (worded with "can" / "may"): extra weight around the middle can be linked with lower testosterone and the link can run both ways; poor sleep, stress and weight can each pull testosterone down; "total and free testosterone" are different measurements; blood tests are "usually taken in the morning"; loud snoring plus daytime sleepiness should be raised with a physician. Add citations or have a clinician sign off.
6. **Fertility line** ("If you plan to have children, say so early") and the medication line ("Never change a prescription on your own") are safety nudges, not claims; keep them.
7. **Supplements** copy is deliberately generic ("targeted support where it fits... never a substitute for medical care"). The /supplements page itself has not been reviewed here and may need the same pass.
8. **Graphics** are labelled "Illustration only" where they look data-like; none shows numbers or outcomes. The hero graphic implies "causes underneath symptoms" and the final compass implies "finding direction"; neither implies a result.
9. **Disclaimer** at the bottom adds "Medical testing, diagnosis, prescriptions and treatment are provided by a physician" plus 911/988. Same wording flag as the homepage (988 is a US/Canada line; confirm).
10. No testimonials, no statistics, no urgency or scarcity, no before/after.
11. **Shared nav/footer** still contain Calgary wording ("Made with ♥ in Calgary" was kept on purpose by the owner). The page body has none.
12. Noindex/other pages: /owen, /emma, /quiz duplicates are not touched by this page.

## Found while testing (affects the live homepage too)
`home.html` / `home.template.html` define `function track(cta)` and later `var track = tl.querySelector('.tl-track')` inside the same IIFE. The `var` hoists and overwrites the function with a DOM element once the timeline block runs (any browser with motion enabled), so every `track(cta)` call throws and **no "CTA Click" event reaches Mixpanel from the homepage**. Fix: rename the function (this page uses `trackCta`) and rebuild + republish the homepage. This also may explain the "Booking Link Clicked tracking gap" on the pending list.

## Publishing checklist (when approved)
Paste `page.html` into the page's custom-code element (Version History keeps the old one), confirm the CDN nav/footer render, check `/functional-health` live at 1280 and 390, then commit `page.html` + source to the repo under `pages/functional-health/`. Also add `/functional-health` to the custom sitemap and `llms.txt`.

## X follow line (2026-10-17, approved by Alex via Odin X Marketer): footer only - no change to this page's HTML
The footer line "Follow Odin Labs on X for the daily research breakdowns." (`data-cta="x_follow_footer"`, https://x.com/intent/follow?screen_name=odinhealthlab, new tab) lives in the shared repo file `odinfooter.html` that this page fetches at load time, so this page file is unchanged (no republish needed). Staged footer: `/workspace/odinfooter.xfollow.html`; ships by merging it to GitHub master (tarball `/workspace/ghsync-xfollow.tar.gz`). It shows only on the maintained site paths (allow-list in the footer script), not on the paid pages. Tests with the staged footer: tracking PASS (existing handler fires CTA Click for x_follow_footer), footer visible at 1280 and 390 with no overflow. Details: `/workspace/xfollow-queue.md`.

## Common questions accordion (2026-10-19, iklinks; built locally, not published)
Why: Search Console reports /trt-or-fix-causes-first, /trt-and-fertility, /peptides-canada-usa, /testosterone-and-hair-loss, /testosterone-calculator, /trt-side-effects and /how-to-raise-testosterone-naturally as "URL is unknown to Google"; this Google-indexed page now links to them with plain crawlable `<a href>`.
- Section `#common-questions` (page.template.part3.html (section before FAQ) + page.template.part2.html (CSS before </style>, .fh scope, fh-bob)). Same pattern as /health-coaching (hclinks): two columns, native `<details class="cq-d">` rows in 2 groups, one-line answers paraphrased from each linked page's Short answer, no card grid. Generated by /workspace/tools/iklinks_gen.py (`python3 iklinks_gen.py fh html|css|links`), pasted as static source.
- Links + data-cta: fh_q_home -> /#common-questions, fh_q_trt_or_fix -> /trt-or-fix-causes-first, fh_q_natural -> /how-to-raise-testosterone-naturally, fh_q_sleep -> /low-testosterone-and-sleep, fh_q_hairloss -> /testosterone-and-hair-loss, fh_q_labs -> /low-testosterone-labs-to-ask-for, fh_q_calc -> /testosterone-calculator, fh_q_trtse -> /trt-side-effects, fh_q_fertility -> /trt-and-fertility, fh_q_peptides -> /peptides-canada-usa.
- Motion accent `.mg--iq`: question bubble (page glyph) sends a packet to each of three answer cards; card lights, tick pops; bubble bobs. transform/opacity only, 7s loop, paused off-screen via the section's `[data-live]`; static default = final state; reduced motion = soft card glow only (no travel/bob/pop, accordion easing off). Side column + groups use `.reveal`.
- Tests: hp-test/ikq.js `functional-health fh` PASS 1280+390; shared test-visual PASS; tracking 26/26 (was 16) CTA Click, Booking Link Clicked 2/2; nophys/banned scan unchanged. Backups *.bak-iklinks.
- In-body TITLE aligned to the GHL head title / seo-meta.md: 'Functional Health for Men: Root Causes | Odin Health Lab' (was '...Find the Root Cause | Odin Labs'); <title>, og:title, twitter:title, JSON-LD WebPage name. DESC unchanged (matches the live GHL head description; note seo-meta.md lists a different description).
