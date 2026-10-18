# /low-testosterone-labs-to-ask-for (local only, NOT published)

Target query: "What labs should I ask for besides total testosterone?"
Files and regeneration: same layout as `../trt-or-fix-causes-first/NOTES.md` (`page.html`, `build.py`, `page.body.html`, `page.css`, `shots/`, `test-*.out.*`, shared `../_shared/*` incl. `gfx.py` and `answer.css`). Tests: `node ../pages/_shared/test-visual.js low-testosterone-labs-to-ask-for` and `NO_ASSESS=1 node ../pages/_shared/test-tracking.js low-testosterone-labs-to-ask-for` from `/workspace/hp-test` (`NODE_PATH=/workspace/hp-test/node_modules`).

## Per Alex's instructions (2026-10-15)
No disclaimer paragraph / educational-only note / 911 / 988 / "Illustration only" captions; no link to /owen-lowt. CTAs = booking modal (hero_book_call, order_book_call, final_book_call) + homepage and sibling links. Enforced by the tracking test.

## SEO
Title (57): `Low Testosterone Labs: What to Ask For | Odin Health Labs`. Description (152): `What labs should you ask for besides total testosterone? Free T, SHBG, LH, FSH, estradiol, prolactin, hematocrit, PSA, thyroid, A1c and what each shows.` Appended to `/workspace/homepage/seo-meta.md`; URL added to `/workspace/homepage/sitemap.xml` (not published). Canonical `https://odinhealthlab.ca/low-testosterone-labs-to-ask-for`. JSON-LD: Organization, WebSite, WebPage, Article, BreadcrumbList, FAQPage (6 Qs, same list as the on-page FAQ). Internal links: home, /functional-health, /health-coaching, /supplements, /trt-or-fix-causes-first, /privacy. Sources: Endocrine Society 2018 guideline (doi 10.1210/jc.2018-00229) and the FDA biotin-interference page (fda.gov, verified live; the older safety-communication URLs returned 404 so were not used).

## What the page says (and does not)
Covers morning/fasting/repeat timing; total T, free T, SHBG; LH, FSH, prolactin, estradiol; semen analysis if fertility matters; hematocrit/CBC, PSA (age-appropriate, individual decision), CMP; TSH, A1c/glucose, lipids, vitamin D, iron studies if indicated; a 4-step testing order; a 6-line script for asking; why ranges differ by lab. **No reference ranges, no numbers, no percentages.** Says ranges differ by lab and to use the range on your own report.

## Motion graphics (every section distinct)
Hero: rack of five test tubes, liquid levels breathe, a drop falls into each in turn. Timing: sun rides an arc, morning window highlighted; first tube then repeat tube light in turn. Core trio: SHBG carriers holding testosterone dots, free dots drifting. Signals: brain, pituitary, testes relay with pulses, feedback loop, prolactin and estradiol side nodes. Safety: red cells flowing through a tube, shield/document/heart nodes. Context: six dial tiles with sweeping needles. Order: scroll-filled timeline with four animated step icons. Ask: lab form with a pen ticking boxes. Ranges: three scales with different normal bands and one fixed marker. Sources: fanning documents. Related: hub-and-spokes. FAQ: test tube with rising bubbles and a drawn question mark. Final: sunrise with rising sun, pulsing rays and expanding rings beside a tube and a calendar. Same motion rules as the other pages.

## Compliance / content flags (human review)
1. **Who orders labs / can Odin order them?** The page does not say Odin orders labs; FAQ 6 says a free call helps you work out which labs to ask a physician about and that testing, diagnosis, prescriptions and treatment are provided by a physician. Confirm the real workflow (own doctor, Odin physician, lab requisition) and update the copy.
2. **Cross-border scope** (Canada + USA) unverified, as on the other pages. The coverage line ("in Canada public insurance coverage varies by province; in the USA by plan") is deliberately generic.
3. **Clinical statements to have a clinician check:** morning/fasting/repeat (Endocrine Society 2018); free T when total is borderline or SHBG may be altered (same guideline); SHBG moved by weight, age, thyroid and liver conditions; LH/FSH pattern (high with low T points to the testes, low or normal points to the pituitary/hypothalamus); prolactin raised by some medications and added when LH is low; estradiol "some physicians check for context"; high hematocrit as a reason for caution with TRT; PSA individual decision; iron overload can affect pituitary/testes; vitamin D optional; biotin may interfere with some tests (FDA).
4. **Estradiol and vitamin D** are included as "some physicians check" items, not as recommendations. Remove if Alex or the reviewer prefers a shorter list.
5. **Semen analysis** is mentioned for men who want children (not a blood lab, but relevant to fertility and any TRT discussion).
6. **Cardiac / urgent-care wording:** none on this page.
7. **Article schema** names the Organization only; no medical reviewer.
8. `sitemap.xml` still lists /owen-lowt: check whether it is [Paid].
9. Links to `/trt-or-fix-causes-first`: publish both pages together.

## Tested
Same suite and results format as the TRT page (see `test-visual.out.json`, `test-tracking.out.txt`): console clean, CLS 0, no overflow at 1280 and 390, reduced motion and JS-off clean, loops pause off-screen, every `data-cta` unique and tracked, no /owen-lowt, banned-claim scan 0 hits. Not checked: real-device FPS, Safari/Firefox, Lighthouse in GHL, live nav/footer loaders.

## Update 2026-10-16 (local only, not published)
Keep reading gained a 6th card "Free vs total testosterone" (data-cta related_freet -> /free-vs-total-testosterone) and a 6th hub node (drop icon at 280,170); hub aria-label now says six pages. Pre-edit backup: /workspace/backups-freet/low-testosterone-labs-to-ask-for/. Rebuilt (133,949 bytes, no minify needed); visual + tracking (NO_ASSESS) retested: all PASS, 19/19 CTAs, banned scan 0. Publish /free-vs-total-testosterone first.

## X follow line (2026-10-17, approved by Alex via Odin X Marketer) - built locally, NOT published
- End-of-article line: one calm text link, last element of `<main>` (after the final CTA section): `<p class="x-follow reveal"><a class="x-follow-link" href="https://x.com/intent/follow?screen_name=odinhealthlab" target="_blank" rel="noopener noreferrer" data-cta="x_follow_end">` + 16px X icon (inline SVG, aria-hidden) + `<b>Follow Odin Labs on X</b> for the daily research breakdowns.`. Markup is in `page.body.html` (just before `</main>`); CSS (`.pg .x-follow*`, hover tint + icon nudge only, transitions off under reduce) is in `../_shared/answer.css`. No /owen-lowt, no disclaimer, no new motion loop.
- Footer twin: the footer is NOT part of this page. Every page fetches `odinfooter.html` from GitHub master at runtime (base_loader.html), so the footer line (`data-cta="x_follow_footer"`) ships via the repo file `odinfooter.html` (staged as `/workspace/odinfooter.xfollow.html`, tarball `/workspace/ghsync-xfollow.tar.gz`); it shows only on the maintained site paths (allow-list in the footer script), never on the paid pages that share the footer.
- Tracking: both links use the existing document capture-phase handler (`trackCta` -> `CTA Click {cta, page}` via sendBeacon, before the new tab opens). No handler change was needed. 'Booking Link Clicked' untouched (2/2).
- Tests (2026-10-17): tracking 21/21 PASS CTA clicks (+1 footer link, +1 end link vs the previous build), Booking Link Clicked 2/2, visual 1280 + 390 CLS 0, 0 console errors, no horizontal overflow, 0 offscreen loops, no-JS hidden 0 (reduced-motion hidden at 390: same as before this change, see /workspace/xfollow-queue.md), scan.py result unchanged vs the pre-change build, mojibake 0. page.html 135,556 B. Backups `*.bak-xfollow`. Staged `/workspace/srv2/low-testosterone-labs-to-ask-for-xfollow.txt`.

## Calculator inbound link (2026-10-18), built locally, NOT published
- Added a full-width "Testosterone calculator" card at the top of the Keep-reading grid (data-cta related_calc, grid-column 1/-1, so the existing grid rows stay intact), plus an inline link: panel_calc_link inline in a lead paragraph. Both point to /testosterone-calculator.
- Backups: *.bak-calc (page.body.html, page.html, build.py, page.css, page.full.html if present, NOTES.md, test outputs).
- Retested: visual PASS at 1280 and 390 (CLS 0, 0 errors, no overflow, 0 offscreen loops; reduced/no-JS hidden counts identical to the pre-edit baseline). Tracking exit 0 with the new CTAs firing. Scan and nophys 0 hits. page.html 136401 B.
- Publish only AFTER /testosterone-calculator is live (otherwise the new links 404).
