# /trt-cost-canada-vs-usa: answer page 13 (BUILT LOCALLY, not published)

- Title (59): TRT and Testosterone Cost: Canada vs USA | Odin Health Lab
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
- Old title 'TRT Cost in Canada vs USA: Labs and Drugs | Odin Health Lab'; old desc 'What TRT costs in Canada vs the USA: lab tests, provincial and insurance coverage, injection, gel and pellet prices, and monitoring. Sourced, Oct 2026.'
- H1 + Article headline: 'How much do TRT and testosterone cost in Canada vs the USA?' (was 'How much does TRT cost in Canada vs the USA?').
- Short answer: lead 'TRT has two price tags: the testosterone itself and the lab testing around it.'; 'Gels and pellets cost more, often much more.' -> gel prices already on the page (ON generic 1% gel ~$89 CAD/month = 30 x $2.9575; Drugs.com generic 1.62% 88 g pump $55.73-$77.13 USD cash) + 'pellets cost more.'
- dateModified 2026-10-22. Rebuild also adds Organization sameAs (shared common.py). No new sections, no motion change, no new claims.

## 2026-10-23 clinic price block (price1023) - built locally, NOT published
- Source: Alex (owner, Alexander Tretjakov, Founder) on 2026-10-23: TRT clinic pricing is typically about $100-$300 per month, NOT including medication; varies by clinic (visit frequency, extra medication and supplement support). First-hand; attributed on page as the range Odin Health Lab sees across clinics (no outside source). Currency not specified by Alex; copy leaves the range in plain dollars and labels only the drug figure CAD.
- Hero short answer: + 'Most TRT clinics charge about $100 to $300 a month for visits and monitoring, not counting the medication; the fee varies with how often you're seen and what support is included.' (after the 2022 telehealth sentence).
- New section id="clinic-fees" between #sample-year and #help: H2 'How much does a TRT clinic cost per month?'; worked example = range + ~$15 CAD/month cypionate (Ontario list, from #sample-year) -> roughly $115 to $315 a month all in, before labs and dispensing fee (labelled our arithmetic); gel line ~$89 CAD/month. Motion graphic (.mg, 560x230): two range bars stretch (cf-b, reuses te-b keyframes) + three tags light in turn (cf-t: visit frequency, extra medication, supplement support). CTA booking-trigger data-cta clinic_book_call (no /owen-lowt).
- FAQ 6 -> 7: 'How much does TRT cost per month at a clinic?' (2nd), DOM == JSON-LD 1:1. Harness 'FAQ 5-6 Qs' FAIL 7 by design.
- Desc (149): 'TRT cost per month in Canada vs the USA (Oct 2026): clinic fees, testosterone cypionate, gel and pellet prices, lab tests, and what insurance covers.' Title unchanged (59). dateModified 2026-10-23.
- Tests: visual 1280+390 CLS 0, 0 errors, 0 overflow, 0 offscreen loops, reduced/no-JS hidden 0 (unchanged vs pre-change run); figs 14->15, animations 146->151; tracking 47/47 + Booking 2/2, title/desc == seo-meta PASS, no /owen-lowt; scan.py PASS 0; mojibake 0. page.html 150,087 B. Backups *.bak-price1023; pre-change test outputs *.pre-price1023.

## 2026-10-26 currency wording + exact-query lead (cur1026) - built locally, NOT published
- Alex 2026-10-23: the $100-$300/month clinic fee (medication not included) is roughly the same in CAD and USD. Hero short answer, #clinic-fees lead and FAQ 'How much does TRT cost per month at a clinic?' (DOM == JSON-LD) now say 'in either Canadian or US dollars'. Worked example now explicitly 'in our example a Canadian clinic in that range comes to roughly $115 to $315 CAD a month' (CAD + CAD, arithmetic honest); section line 'That is our own arithmetic, not a clinic quote.'; graphic labels 'Clinic fee per month (CAD or USD), medication not included' / 'Our example in CAD: generic cypionate added (about $15 a month)' + aria-label. Drug/lab prices unchanged.
- GSC 'trt cost canada' pos ~13: title (60) 'TRT Cost in Canada vs USA: Monthly Prices | Odin Health Lab'; desc (149) 'TRT cost in Canada vs the USA per month (Oct 2026): clinic fees, testosterone cypionate, gel and pellet prices, lab tests, and what insurance covers.'; H1 + Article headline 'TRT cost in Canada vs the USA: how much do TRT and testosterone cost?'; dateModified 2026-10-26.
- Tests: visual 1280+390 identical to pre-change (CLS 0, 0 errors, 0 overflow, 0 offscreen loops, figs 15, anims 151, reduced/no-JS hidden 0); tracking all PASS except harness 'FAQ 5-6 Qs' (7 by design); scan.py PASS 0; mojibake 0. page.html 150,383 B. Backups *.bak-cur1026.

## AndroGel cost answer block (and1029, 2026-10-29, built locally)
- Target: GSC 'how much does AndroGel cost in Canada' (pos ~10). Backlog TOP 10-28 item 1.
- New answer box id="androgel-cost" inside #prices, right after the price-chart figure (the figure's bar animation covers motion; box uses .reveal): tag 'AndroGel in Canada', H3 'How much does AndroGel cost in Canada?', 3-sentence answer. New CSS .pg .ag-box / .ag-q in page.css.
- FAQ 8 -> 9, new #3 'How much does AndroGel cost in Canada?' (DOM == JSON-LD 1:1).
- Sources +2: source_odb_androgel (detail.xhtml?drugId=02245346), source_odb_taro_gel (detail.xhtml?drugId=02463806). Raw copies /workspace/and1029/src (odb.html search, odb-androgel.html, odb-tarogel.html; Alberta DBL via fetch, curl 403).
- Facts re-checked 2026-10-29: ODB AndroGel 1% 5.0 g packet DIN 02245346 unit price 4.5117, Amount MOH Pays 2.9575, Limited Use, interchangeable; Taro-Testosterone Gel 1% 5.0 g DIN 02463806 2.9575; 2.5 g packets AndroGel 2.5514 / Taro 1.6726. Alberta DBL ptc 680800: AndroGel 2.5 g and 5 g packets NOT A BENEFIT (no price); Taro cypionate 3.4878/mL REGULAR BENEFIT (unchanged).
- Our arithmetic: 30 x 4.5117 = $135.35; 30 x 2.9575 = $88.73; cypionate ~$15.11/month (5.2 vials x 34.88 / 12); 88.73/15.11 = 5.9, 135.35/15.11 = 9.0 -> 'about six to nine times'.
- dateModified 2026-10-29. Title/desc/H1 unchanged.

## Injection cost without insurance block (inj1029, 2026-10-29, built locally)
- Target: GSC injection-cost / without-insurance queries; backlog TOP 2026-10-29 item 1. Page got its first organic click Oct 28.
- New answer box id="injection-cost" (class answer-box ag-box reveal, same style as #androgel-cost) inside #prices, right after the price-chart figure and BEFORE #androgel-cost: tag 'Injections without insurance', H3 'How much do testosterone injections cost in Canada without insurance?'. No new CSS (reuses .ag-box/.ag-q); .reveal respects reduced motion (existing pipeline).
- FAQ 9 -> 10, new #3 'How much is TRT without insurance?' (DOM == JSON-LD 1:1). Only reuses already-sourced page figures + today's ODB/AB per-mL prices.
- Sources +3: source_bc_formulary (pharmacareformularysearch.gov.bc.ca), source_odb_taro_cyp (detail.xhtml?drugId=02496003), source_odb_enanthate (detail.xhtml?drugId=02536315); source_alberta_dbl 'checked' date -> October 29, 2026.
- Facts fetched 2026-10-29 ~3:10 PM MDT (raw /workspace/inj1029/src): ODB search 'testosterone' + details: Taro-Testosterone Cypionate 100 mg/mL 10 mL DIN 02496003 unit price 34.8780 (MOH pays 34.8780, LU yes); Testosterone Enanthate Injection USP (Hikma) 1000 mg/5 mL 5 mL DIN 02536315 35.5943 (LU yes); Depo-Testosterone and Delatestryl Not a Benefit. Alberta DBL ptc 680800 (curl 403, WebFetch saved as abdbl-webfetch.md): Taro cypionate 3.4878/mL REGULAR BENEFIT; enanthate USP 200 mg/mL 7.1189/mL REGULAR BENEFIT (Delatestryl 11.8403/mL, LCA 7.1189). BC PharmaCare Formulary Search (form POST; bc-testosterone.html, bc-02496003.html, bc-02536315.html): Maximum PharmaCare Covers cypionate $3.8800/mL, enanthate $7.6884/mL, Special Authority yes.
- Our arithmetic (dose assumption: a common 100 mg a week = 1 mL/week of 100 mg/mL cypionate, or 0.5 mL/week of 200 mg/mL enanthate; 52/12 = 4.333 weeks a month):
  - Cypionate: 34.878/10 = $3.4878/mL (== AB) -> $3.49/mL; 3.4878 x 4.333 = $15.11/month (vial lasts 10 weeks; matches existing ~$15 page figure, no correction needed).
  - Enanthate: 35.5943/5 = $7.1189/mL (== AB) -> $7.12/mL; 0.5 mL x 7.1189 = $3.559/week x 4.333 = $15.42/month (5 mL = 1000 mg, lasts 10 weeks). -> 'about $15 a month' for either.
  - BC: 3.88 x 4.333 = $16.81/month; 0.5 x 7.6884 x 4.333 = $16.66/month -> 'a little higher' ($7.6884 shown as $7.69).
  - Clinic: $100-$300/month (Alex, same in CAD and USD) + ~$15 = ~$115-$315 CAD (existing #clinic-fees arithmetic).
- Dispensing fees, pharmacy markup, needles/syringes and clinic fee stated as extra; no needle price given (no source).
- Title/desc/H1 unchanged; dateModified already 2026-10-29.

## 2026-10-30 lnk1030
- FAQ 1 renamed "How much does TRT cost per month in Canada?" -> "How much does TRT cost in Canada?" (verbatim GSC query, pos ~19.5; seranking CA volume 90/mo, KD 9). Answer's first sentence now "Per month, the drug itself often costs less than people expect."; rest unchanged. FAQ count stays 10, DOM == JSON-LD.
- X follow text -> "Follow Odin Health Lab on X". dateModified 2026-10-30. Title/desc/H1/SEO panel unchanged. Staged :8780/trt-cost-canada-vs-usa-lnk1030.txt.
