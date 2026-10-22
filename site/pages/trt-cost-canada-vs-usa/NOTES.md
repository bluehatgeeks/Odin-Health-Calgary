# /trt-cost-canada-vs-usa: answer page 13 (BUILT LOCALLY, not published)

- Title (59): TRT and Testosterone Cost: Canada vs USA | Odin Health Labs
- Description (150): TRT cost in Canada vs the USA (Oct 2026): testosterone cypionate, gel and pellet prices, lab test fees, and what provincial plans and insurance cover.
- Build: `python3 build.py` (page.full.html readable, page.html minified ~141 KB). Template: /trt-side-effects (same pipeline, Safari fix guard).
- Research and every figure: /workspace/research-trtcost/SOURCES.md (URLs + quoted snippets, fetched 2026-10-16). Raw pages in research-trtcost/raw/.
- Currency: CAD for Canada, USD for USA. All prices dated "as of October 2026"; copy says prices vary by province/state/pharmacy.

## Our arithmetic (shown on page, from sourced prices)
- Injection year: 1,000 mg vial / 100 mg a week = 10 weeks, 5.2 vials a year. x $34.88 (ON/AB list) = $181.37 CAD (~$15/month); x $37.99 (Drugs.com from-price) = $197.55 USD.
- Gel month: ON generic $2.9575 x 30 = $88.73 CAD; brand AndroGel $4.5117 x 30 = $135.35 CAD.
- Private lab round: Canada LifeLabs T panel $98 + PSA $71 = $169 CAD; USA Quest T $75 + PSA $75 + CBC $35 = $185 USD. Three rounds (baseline, 3 and 6 months, per BC protocol) = $507 CAD / $555 USD.

## Review flags
- Ontario formulary prices are government list prices; pharmacies add dispensing fees and markups (said on page).
- Alberta's capsule (Taro-Testosterone 40 mg) exclusion for "androgen decline in the aging male" is specific to capsules; injections are a regular benefit.
- LU 397 wording came from the rxcoverage.ca mirror (official LU page 404'd to curl); prices/LU status from the official ODB formulary search.
- Drugs.com prices are cash/discount-card prices, "not valid with insurance plans". GoodRx blocked fetches (403/bot check) so it was not used.
- Telehealth platform costs come from a 2022 study (Jesse et al., J Sex Med); the page dates it as 2022.
- BC lab fees are "current to April 1st, 2022" in the BC protocol (page says "BC paid labs").

## Inbound link (do later, not done here)
- Add a Keep-reading card + hub node on /trt-side-effects pointing here (suggested data-cta `related_trtcost`). Second choice: /low-testosterone-labs-to-ask-for.

## X follow line (2026-10-17, approved by Alex via Odin X Marketer) - built locally, NOT published
- End-of-article line: one calm text link, last element of `<main>` (after the final CTA section): `<p class="x-follow reveal"><a class="x-follow-link" href="https://x.com/intent/follow?screen_name=odinhealthlab" target="_blank" rel="noopener noreferrer" data-cta="x_follow_end">` + 16px X icon (inline SVG, aria-hidden) + `<b>Follow Odin Labs on X</b> for the daily research breakdowns.`. Markup is in `page.body.html` (just before `</main>`); CSS (`.pg .x-follow*`, hover tint + icon nudge only, transitions off under reduce) is in `../_shared/answer.css`. No /owen-lowt, no disclaimer, no new motion loop.
- Footer twin: the footer is NOT part of this page. Every page fetches `odinfooter.html` from GitHub master at runtime (base_loader.html), so the footer line (`data-cta="x_follow_footer"`) ships via the repo file `odinfooter.html` (staged as `/workspace/odinfooter.xfollow.html`, tarball `/workspace/ghsync-xfollow.tar.gz`); it shows only on the maintained site paths (allow-list in the footer script), never on the paid pages that share the footer.
- Tracking: both links use the existing document capture-phase handler (`trackCta` -> `CTA Click {cta, page}` via sendBeacon, before the new tab opens). No handler change was needed. 'Booking Link Clicked' untouched (2/2).
- Tests (2026-10-17): tracking 44/44 PASS CTA clicks (+1 footer link, +1 end link vs the previous build), Booking Link Clicked 2/2, visual 1280 + 390 CLS 0, 0 console errors, no horizontal overflow, 0 offscreen loops, no-JS hidden 0 (reduced-motion hidden at 390: same as before this change, see /workspace/xfollow-queue.md), scan.py result unchanged vs the pre-change build, mojibake 0. page.html 142,368 B. Backups `*.bak-xfollow`. Staged `/workspace/srv2/trt-cost-canada-vs-usa-xfollow.txt`.

## Calculator inbound link (2026-10-18), built locally, NOT published
- Added a full-width "Testosterone calculator" card at the top of the Keep-reading grid (data-cta related_calc, grid-column 1/-1, so the existing grid rows stay intact), plus an inline link: panel_calc_link inline in a lead paragraph. Both point to /testosterone-calculator.
- Backups: *.bak-calc (page.body.html, page.html, build.py, page.css, page.full.html if present, NOTES.md, test outputs).
- Retested: visual PASS at 1280 and 390 (CLS 0, 0 errors, no overflow, 0 offscreen loops; reduced/no-JS hidden counts identical to the pre-edit baseline). Tracking exit 0 with the new CTAs firing. Scan and nophys 0 hits. page.html 143187 B.
- Publish only AFTER /testosterone-calculator is live (otherwise the new links 404).

## 2026-10-22 data-led title/intro tweak (fh1022) - built locally, NOT published
- Why: GSC 28d this page had 19 impressions at avg pos 24.4 (best non-brand page near page 2-3), all price queries: trt cost canada (pos 13), testosterone price (31), testosterone cypionate cost (39), testosterone gel canada price (42), testosterone from canada (52), canadian testosterone (53), canada testosterone (65). Chosen over /functional-health (10 impr, pos 53, queries 'functional health', 'functional health canada', 'holistic ayurveda' = off-topic for low T).
- Old title 'TRT Cost in Canada vs USA: Labs and Drugs | Odin Health Labs'; old desc 'What TRT costs in Canada vs the USA: lab tests, provincial and insurance coverage, injection, gel and pellet prices, and monitoring. Sourced, Oct 2026.'
- H1 + Article headline: 'How much do TRT and testosterone cost in Canada vs the USA?' (was 'How much does TRT cost in Canada vs the USA?').
- Short answer: lead 'TRT has two price tags: the testosterone itself and the lab testing around it.'; 'Gels and pellets cost more, often much more.' -> gel prices already on the page (ON generic 1% gel ~$89 CAD/month = 30 x $2.9575; Drugs.com generic 1.62% 88 g pump $55.73-$77.13 USD cash) + 'pellets cost more.'
- dateModified 2026-10-22. Rebuild also adds Organization sameAs (shared common.py). No new sections, no motion change, no new claims.
