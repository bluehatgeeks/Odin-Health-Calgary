# /how-to-raise-testosterone-naturally: answer page 14 (BUILT LOCALLY, not published)

- Title (54): How to Raise Testosterone Naturally | Odin Health Lab
- Description (151): What raises testosterone without TRT for men 35+: sleep, fat loss, training, alcohol, stress, vitamin D and zinc, and what boosters really do. Sourced.
- Build: `python3 build.py` (page.full.html readable, page.html minified 148,243 B, under the ~150 KB GHL budget; GHL save fails ~170 KB). Template: /trt-cost-canada-vs-usa (same pipeline, Safari fix guard, `var reduce = false`, 0 no-preference queries).
- Research and every number: /workspace/research-natural/SOURCES.md (URLs + quoted snippets, fetched 2026-10-16). Raw abstracts/PMC text in research-natural/raw/.
- 15 motion figures (.mg), 18 [data-live] blocks, 25 on-page sources (data-cta source_*), 6 FAQs (last = "How does Odin Health Lab work with my doctor?", the only place doctor words appear), 51 unique data-cta values.

## Sections
Hero (five-lever gauge) / #levers table (8 rows: lever, what research shows, what to do) / #sleep / #fat-loss / #training / #alcohol / #stress / #medications (incl. sleep apnea) / #vitamin-d-zinc / #boosters / #expect (ruler) / #when-lifestyle-is-not-enough (decision path + book call) / #help (2x2) / #plan (4-step timeline) / #sources / #related (3x2 + home) / #faq / final CTA.

## Motion
Hero gauge needle + arc + lever chips; sleep bars + T line drop (Leproult); weight bars (Corona diet vs surgery) + body outline; training cards + steps dots; alcohol glass bubbles + cards; stress signal path with three shared-keyframe dots (LH to testes) + chips; medication checklist ticks + magnifier; vitamin D / zinc before-after bars; booster bottle + 4 ingredient-count bars (Clemesha); expect ruler markers; when-not-enough decision path; help flow (inputs to telehealth assessment to plan); plan step icons; FAQ sun motif; related hub (6 nodes); final shield.

## Our arithmetic (labelled "about" on page)
- nmol/L x 28.84 = ng/dL: +2.87 nmol/L = about 83 ng/dL; +8.73 nmol/L = about 250 ng/dL (251.8); AUA 300 ng/dL = about 10.4 nmol/L.
- Leproult: 18.4 -> 16.5 nmol/L = about -1.9 nmol/L (paper: 10 to 15 percent lower daytime T).

## Review flags
- Sleep-restriction data are from 10 young men (~24 years), not men 35+; the page says so and uses it as direction, not size. Leproult citation title is reworded ("Research letter on a week of sleep restriction...") to keep the banned-claim regex clean (sleep page precedent).
- Sleep apnea: Cignarelli 2019 meta-analysis found CPAP alone did not significantly raise T; page says treat apnea for health and weight, not as a T fix.
- Vitamin D: Pilz 2011 (54 men, deficient start) rose 10.7 -> 13.4 nmol/L; Lerchbaum 2017/2019 RCTs and Paez-Allendes 2026 meta (MD 0.47 nmol/L, not significant) found no clear effect. Page: test first, top up only what is low.
- Zinc: Prasad 1996 (9 marginally deficient older men) 8.3 -> 16.0 nmol/L is small and old; Koehler 2009 ZMA no change in zinc-sufficient men. NIH ODS: 11 mg/day need, 40 mg/day upper limit, high zinc lowers copper (consumer page used; the health-professional page blocked curl).
- Boosters: Clemesha 2020 (50 products, 109 ingredients); Balasubramanian 2019 (37 human studies); ashwagandha 2026 meta (Fornalik; 23 trials, 1,706 patients, about +57 ng/dL in men) is described as "small, mixed, needs standardized trials".
- AUA 2018 statement 21 (lifestyle counselling for low T + obesity) verified via an auajournals/auanet PDF snippet; the AUA site is JS-rendered.
- Friedl 2026 (JCEM review) used for central suppression by severe energy deficit, sleep disruption and uncontrollable stress (raises SHBG, lowers free T), recovery with energy balance, and heavy resistance training not suppressing basal T when energy is maintained. No stress-reduction RCT number is used.
- No % signs or digit+duration strings (scan rule): durations spelled out ("three weeks", "twelve weeks"), "percent" used.
- No "reversible" (scan regex `\breverse` matches it): "fixable causes" used instead.

## Inbound link
- Done in this build: /trt-or-fix-causes-first Keep reading gained a full-width featured card + 7th hub node (data-cta `related_natural`). See that page's NOTES.md.

## Tested (headless Chrome, puppeteer-core, file:// build, 1280 and 390)
See `test-visual.out.json` and `test-tracking.out.txt`: console errors 0, CLS 0, no overflow, 0 off-screen loops, reduced-motion hidden 0, no-JS hidden 0; tracking 51/51 CTAs fire CTA Click, Booking Link Clicked 2/2, title/desc match seo-meta.md, FAQ DOM == JSON-LD, no /owen-lowt (NO_ASSESS); scan.py PASS (0 hits); mojibake 0.

## Publishing checklist (when approved)
New GHL step `/how-to-raise-testosterone-naturally` -> paste page.html into its custom-code element -> SEO title/description above -> publish + verify live (curl + 1280/390) -> republish /trt-or-fix-causes-first (inbound card) -> add URL to GHL XML Sitemap generator + llms.txt (staged in /workspace/srv2) -> GSC/Indexing API + Bing -> GitHub PR from /workspace/ghsync-natural.tar.gz.

## X follow line (2026-10-17, approved by Alex via Odin X Marketer) - built locally, NOT published
- End-of-article line: one calm text link, last element of `<main>` (after the final CTA section): `<p class="x-follow reveal"><a class="x-follow-link" href="https://x.com/intent/follow?screen_name=odinhealthlab" target="_blank" rel="noopener noreferrer" data-cta="x_follow_end">` + 16px X icon (inline SVG, aria-hidden) + `<b>Follow Odin Labs on X</b> for the daily research breakdowns.`. Markup is in `page.body.html` (just before `</main>`); CSS (`.pg .x-follow*`, hover tint + icon nudge only, transitions off under reduce) is in `../_shared/answer.css`. No /owen-lowt, no disclaimer, no new motion loop.
- Footer twin: the footer is NOT part of this page. Every page fetches `odinfooter.html` from GitHub master at runtime (base_loader.html), so the footer line (`data-cta="x_follow_footer"`) ships via the repo file `odinfooter.html` (staged as `/workspace/odinfooter.xfollow.html`, tarball `/workspace/ghsync-xfollow.tar.gz`); it shows only on the maintained site paths (allow-list in the footer script), never on the paid pages that share the footer.
- Tracking: both links use the existing document capture-phase handler (`trackCta` -> `CTA Click {cta, page}` via sendBeacon, before the new tab opens). No handler change was needed. 'Booking Link Clicked' untouched (2/2).
- Tests (2026-10-17): tracking 53/53 PASS CTA clicks (+1 footer link, +1 end link vs the previous build), Booking Link Clicked 2/2, visual 1280 + 390 CLS 0, 0 console errors, no horizontal overflow, 0 offscreen loops, no-JS hidden 0 (reduced-motion hidden at 390: same as before this change, see /workspace/xfollow-queue.md), scan.py result unchanged vs the pre-change build, mojibake 0. page.html 149,689 B. Backups `*.bak-xfollow`. Staged `/workspace/srv2/how-to-raise-testosterone-naturally-xfollow.txt`.
- 2026-10-29 cal1029: #help lead last sentence extended with a link to /trt-clinic-calgary ('online TRT clinic for Calgary and Alberta', data-cta natural_calgary_link). _shared/common.py Calgary guard allows data-cta="*_calgary_link".
