# /testosterone-calculator (built locally 2026-10-18, NOT published). Backlog "Added 2026-10-18 #1"
Linkable tool page: testosterone unit converter plus Vermeulen free T calculator, for men in Canada and the USA (andropause / low T telehealth).

Build: `python3 build.py`. This runs the answer-page system in ../_shared (gfx.build -> common.assemble), then minifies (CSS comments and indentation stripped outside <script>, unused pi-* symbols dropped, CSS tightened). The unminified copy is kept as page.full.html.
Tool code:
- calc-core.js: math only, between `/*CORE*/ ... /*/CORE*/`. It is inlined in page.html, and test-calc.js runs this exact block.
- calc-ui.js: behaviour. Both files are inlined in one <script> after </main>.
The no-JS state is rendered server-side by Python mirrors in build.py, so the defaults show real results with JS off.

## SEO
- Title (60): `Testosterone Calculator: Free T and Units | Odin Health Lab`
- Description (144): `Free testosterone calculator (Vermeulen) and ng/dL to nmol/L converter, with normal testosterone levels for men in Canada and the USA explained.`
- H1: "Testosterone calculator: convert ng/dL to nmol/L and calculate free T". Canonical https://odinhealthlab.ca/testosterone-calculator.
- JSON-LD: Organization, WebSite, WebPage, Article (datePublished 2026-10-18), BreadcrumbList, FAQPage (6 Q, 1:1 with the DOM), WebApplication (applicationCategory HealthApplication, free Offer in CAD, featureList, areaServed CA + US).
- Listed in /workspace/homepage: seo-meta.md, sitemap.xml (23 URLs, priority 0.8) and llms.txt (new "## Tools" section). Backups in /workspace/backups-calc/.

## Tool spec
1. Converter (#cv). Live on input, both directions, comma decimals accepted. Each field has a <label>, inputmode=decimal and is 52px tall.
   - Total T: nmol/L x 28.84 = ng/dL. ng/dL shows 0 decimals (1 when under 100); nmol/L shows 2.
   - Free T: pg/mL x 3.467 = pmol/L. pmol/L shows 1 decimal; pg/mL shows 2.
   - A meter pin (0-40 nmol/L scale) moves to the value. Plain-words lines say where the value sits against each reference point.
2. Free T calculator (#fc). Inputs:
   - Total T, with an nmol/L / ng/dL radio toggle. Switching converts the value.
   - SHBG (nmol/L) and albumin (g/L, default 43).
   - Hints: a total over 100 in nmol mode is flagged as probably ng/dL; under 20 in ng mode as probably nmol/L. Albumin under 10 is read as g/dL and converted with a note. Out-of-range values show a message.
   Outputs: free T in pmol/L and pg/mL, percent free, bioavailable T (nmol/L and ng/dL), the total T used, a 3-segment bar (SHBG-bound / albumin-bound / free) and reference lines (EMAS 220 pmol/L, LifeLabs 115-577 pmol/L).
   - Constants (Vermeulen 1999 via ISSAM): K_SHBG 1e9 L/mol, K_alb 3.6e4 L/mol, albumin MW 69,000.
   - Equations: N = 1 + Ka*Alb/69000; a = N*Ks; b = N + Ks(S - T); FT = (-b + sqrt(b^2 + 4aT)) / 2a; BAT = N*FT.
   - Results update as you type (aria-live polite).
3. Reference points (table plus animated range figure). Bracketed figures are conversions:
   - Endocrine Society 9.2-31.8 nmol/L / 264-916 ng/dL
   - AUA 300 ng/dL (10.4)
   - CUA 10 nmol/L (288)
   - EMAS 11 nmol/L / 320 ng/dL and 220 pmol/L / 64 pg/mL
   - Alberta Precision Labs 8.0-35.0 (231-1,009)
   - LifeLabs BC 8.4-28.8 (242-831) and calculated free T 115-577 pmol/L (33-166 pg/mL)
   Every figure is in /workspace/research-calculator/SOURCES.md.
4. Why the units differ: McQueen JAMA 1986 (7 provinces in 1983), Huth Ann Intern Med 1987, FDA 2013, and MW 288.4 as the bridge.

## Rules followed
- No disclaimers, no "physician-aware" / "talk to your doctor" / "we don't diagnose" wording.
- Doctor words appear only in the FAQ "How does Odin Health Lab work with my doctor?". scan.py checks the DOM and JSON-LD.
- No /owen-lowt (NO_ASSESS=1 tracking check). No PEMF, hydrogen, marma or Calgary.
- No digit + % in prose. The tool shows "Percent free" with no % sign.
- No "N weeks/months/days", and no Odin prescribing claims.
- CTAs use the shared booking modal (.booking-trigger) plus organic internal links. Every link has a unique data-cta calc_* (37 tracked including modal and footer).
- Tool-use measurement: the first input in each tool fires `CTA Click {cta: calc_use_converter | calc_use_freet, page}` once per page load, through a guarded window.mixpanel.track. No new event name. No function or variable named `track`.
- Layout is tidy: one wide tool card per tool. The Keep-reading grid has 4 cards in a 2x2 grid (minmax(min(100%,300px),1fr)). No long card rows.
- Motion:
  - Loops sit in `@media all` and are gated by .js-reveal. The static CSS is the final state.
  - Elements hidden in the static state carry `fx`. Off-screen [data-live] blocks pause.
  - Reduced motion turns off transitions. Nothing is hidden without JS.
- Graphics:
  - hero: cycling units card, nmol -> ng -> free
  - converter: meter with pin and harmonized band
  - free calc: 3-segment bar with glowing free sliver
  - ranges: chart of the bands with low-T cut-offs
  - why: Canada/USA cards with a x28.84 swap
  - how: SHBG clamps vs albumin rings
  - help: CA/US results -> telehealth review -> one trend + plan icons
  - plus the related hub, FAQ motif and final needle

## Inbound links added (backups *.bak-calc in each folder)
| Page | Featured card (data-cta related_calc) | Inline link |
|---|---|---|
| /free-vs-total-testosterone | full-width "Testosterone calculator" card on top of the Keep-reading grid, so the 3x3 grid stays intact | `units_calc_link` at the end of the #units lead paragraph |
| /low-testosterone-labs-to-ask-for | same full-width card | `panel_calc_link` in "The core trio" lead paragraph |
| /trt-cost-canada-vs-usa | same full-width card | `panel_calc_link` after the free vs total link in the tests table lead |

Hub figures were not changed.

## Tests (2026-10-18)
- test-calc.js (`node test-calc.js`): 19/19 PASS. Covers the ISSAM example (N 23.43, 1.7388e-10 mol/L, 1.74 percent, 5.02 ng/dL, BAT 118 ng/dL), calcengines 325.6 pmol/L, the MW-66,430 variant (108 pg/mL, 2.17, 264 ng/dL), the conversion pairs, monotonicity and mass balance.
- /workspace/hp-test/calc-tool.js: 50/50 PASS at 1280 and 390. Covers live conversion both ways, unit toggle, hints, invalid input, bar widths, focus, labels, inputmode, 44px targets, tool-use events, no overflow, no page errors.
- Visual PASS at 1280 and 390, with FOOTER_FILE=/workspace/calc-footer/odinfooter.html:
  - CLS 0, 0 errors, no overflow, 0 offscreen loops
  - 14 live blocks, 9 figures
  - reduced hidden 0, no-JS hidden 0
  - xfollow end and footer both visible
- Tracking PASS:
  - CTA Click 37/37, Booking Link Clicked 2/2
  - title/description match seo-meta.md, FAQ/JSON-LD parity
  - NO_ASSESS, banned-claim scan 0
- scan.py PASS (0 hits). nophys pattern 0 hits. Mojibake none.
- Size: page.html 126,827 B (page.full.html 138,629 B).

## 2026-10-26 exact-query title/H1 lead (issam1026) - built locally, NOT published
- Why: GSC 28d (weekly check run 3, 2026-10-26): 'issam calculator' at pos 10 for this page; page total 107 impressions, 0 clicks, avg pos 16.4. Put the query wording at the front of the title, H1 and description.
- Method check: the tool IS the ISSAM/Vermeulen method: calc-core.js uses K_SHBG 1e9, K_alb 3.6e4, albumin MW 69,000 and the Vermeulen quadratic; test-calc.js reproduces the issam.ch/freetesuit.html worked example (N 23.43, 1.7388e-10 mol/L, 1.74 percent, 5.02 ng/dL, Bio T 118 ng/dL), 19/19 PASS. ISSAM is already cited in the sources (calc_source_issam) and the albumin default copy.
- Title (64, was 60 'Testosterone Calculator: Free T and Units | Odin Health Lab'): 'ISSAM Calculator: Free and Bioavailable Testosterone | Odin Labs' (brand suffix shortened to 'Odin Labs' to stay under 65; build.py assert relaxed to <= 65). og:title, twitter:title, WebPage name follow.
- Description (148, was 144 'Free testosterone calculator (Vermeulen) and ng/dL to nmol/L converter, with normal testosterone levels for men in Canada and the USA explained.'): 'Free ISSAM calculator: free and bioavailable testosterone from total T, SHBG and albumin (Vermeulen), plus a testosterone ng/dL to nmol/L converter.' og/twitter desc follow.
- H1 + Article headline (was 'Testosterone calculator: convert ng/dL to nmol/L and calculate free T'): 'ISSAM calculator: free and bioavailable testosterone, plus ng/dL to nmol/L conversion'. One H1. dateModified 2026-10-26 (was 2026-10-18). Rebuild also picks up the shared Organization sameAs (common.py, already live on other pages).
- No other copy, tool, motion, link, CTA, ?ref= or footer change. seo-meta.md updated (old title/desc kept as Previous).
- Tests: test-calc 19/19; calc-tool 50/50; visual 1280+390 identical to the pre-change run (CLS 0, 0 errors, 0 overflow, 0 offscreen loops, 9 figs, 14 live blocks, reduced/no-JS hidden 0); tracking 37/37 + Booking 2/2, title/desc == seo-meta PASS, og/twitter match, one h1, no /owen-lowt, banned 0 (title length shows 64 '>60' note, not a fail); scan.py PASS 0; mojibake 0. page.html 127,021 B (was 126,827). Backups *.bak-issam1026; pre-change test outputs *.pre-issam1026.
- GHL: step cf860857-efd2-46e1-8f8c-de7e11cca52e, builder GyZTry1oWhJ2Pum5kIBM. Replace the Custom Code element with http://127.0.0.1:8780/testosterone-calculator-issam1026.txt AND enter the new title + desc in the 'SEO & AI search optimization' panel.

## 2026-10-27 calc1027 (built locally)
- Title (52) `ISSAM Calculator: Free and Bioavailable Testosterone` (was `... | Odin Labs`, 64). Brand rule is "Odin Health Lab" singular; with that suffix the title is 70 chars (~623px) and truncates, so the suffix is dropped (og:site_name / Organization carry the brand). og:title, twitter:title, JSON-LD WebPage name follow. Desc, H1, dateModified unchanged.
- build.py now strips the in-body `<title>` from page.html/page.full.html (assert exactly 1 removed, 0 left): the only `<title>` on the live page should be the GHL SEO-panel head title. Local tracking harness therefore reports `title == seo-meta` FAIL / length 0 on the raw file; with a head `<title>` injected (GHL simulation) it is PASS 52.
- New inbound in-prose links (text-link): /low-testosterone-age-or-weight (aw_shbg_calc_link, 'ISSAM calculator'), /low-testosterone-symptoms (diagnosis_calc_link, 'testosterone calculator'), /andropause-vs-menopause (shbg_age_calc_link, 'ISSAM calculator').

## 2026-10-28 lab1028 (built locally, NOT published): Canadian lab report section
- New section `#canadian-lab-reports` (after #ranges, before #why-units): H2 "How to read testosterone on a Canadian lab report", lead (units nmol/L total / pmol/L free; LifeLabs, Dynacare and APL print calculated free T; ranges differ by lab and method; 150 pmol/L example; three checks: unit, calculated, printed range + age band; APL morning note), animated figure (labrep(): report sheet whose highlight steps down 4 rows, unit pills light in turn, total T/SHBG/albumin values ride an arrow into a calculator card, free T 326 pmol/L output glows; 12s loop, gated by .js-reveal, static = final state, pop/draw-on reveal once), ref-tbl of published male ranges (3 labs), and a 'Plug your report numbers in' link to #free-t (data-cta calc_lab_plug_numbers).
- FAQ +3 (now 9, DOM == JSON-LD 1:1): LifeLabs free T, Dynacare units/ranges, APL ranges. The harness 'FAQ 5-6 Qs' check reads FAIL 9 by design (parity verified separately).
- Sources +6 data-cta: calc_source_apl_freet, calc_source_apl_bulletin_2024, calc_source_lifelabs_method, calc_source_dynacare_total, calc_source_dynacare_freet, calc_source_dynacare_2014. calc_source_apl href moved from the retired indexAPL.asp?id=8932 (now redirects to a search page) to td.albertaprecisionlabs.ca TestView LAB124.
- Article dateModified 2026-10-28. Title/desc/H1 unchanged. page.html 143,731 B.
- Local copies of every lab source: /workspace/lab1028/src/ (see SOURCES.md).
