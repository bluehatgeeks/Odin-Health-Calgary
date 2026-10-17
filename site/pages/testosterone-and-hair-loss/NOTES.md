# /testosterone-and-hair-loss: answer page 15 (BUILT LOCALLY, not published)

- Title (58): Testosterone and Hair Loss: DHT and TRT | Odin Health Labs
- Description (153): Does low T or TRT cause hair loss? How DHT and genes drive balding, finasteride and dutasteride on TRT, other causes, and labs for men in Canada and USA.
- H1: Testosterone and hair loss: what DHT, genes and TRT really do
- Canonical: https://odinhealthlab.ca/testosterone-and-hair-loss
- Build: `python3 build.py` (page.full.html readable 159,794 B, page.html minified 149,236 B, under the ~165 KB working budget; GHL save fails ~170 KB). Template: /how-to-raise-testosterone-naturally (same pipeline, Safari fix guard, `var reduce = false`, 0 no-preference queries, hero-entrance `.mg--hero.hero-in.is-paused` running fix).
- Research and every number: /workspace/research-hairloss/SOURCES.md (URLs + quoted snippets, fetched 2026-10-17). Raw abstracts, FDA label, FDA 2012 Q&A, Health Canada 2026 SSR and MedlinePlus text in research-hairloss/raw/.
- 14 motion figures (.mg), 17 [data-live] blocks, 22 on-page sources (data-cta source_*), 6 FAQs (last = "How does Odin Health Labs work with my doctor?", the only place doctor words appear), 48 unique data-cta values.

## Target queries
"testosterone and hair loss" / "does testosterone cause hair loss" / "does low T cause hair loss" / "does TRT cause hair loss" / "will TRT make me bald" / "DHT hair loss" / "finasteride and TRT" / "dutasteride with TRT" / "finasteride fertility libido" / "male pattern baldness genetics" / "hair loss labs for men" (Canada + USA).

## Sections
Hero (T -> 5-alpha reductase -> DHT -> three follicles) / #at-a-glance / #dht (growth-cycle bars) / #low-t (low T or high T?) / #genetics (AR gene, mother's side, 63 loci) / #trt (does TRT cause hair loss) / #finasteride (basics, DHT suppression + extra hairs) / #with-trt (5-ARI alongside TRT, PSA trend) / #fertility-libido (label side-effect bars, sperm, mood) / #other-causes (patterned / diffuse / patches) / #labs (checklist) / #help (assessment, labs, hair tracking, written plan) / #plan (4-step timeline) / #sources / #related (featured TRT side effects + fertility, labs, weight-loss drugs, free vs total, symptoms, home) / #faq / final CTA.

## Motion
Hero T-to-DHT gate + follicles shrinking; growth-phase bars (typical vs DHT-sensitive); three groups of men, same share thinning at every T level (Kische); X chromosome AR band + 63 locus dots lighting row by row; TRT level dot rising into the normal band + three evidence rows; DHT suppression bars (fin 1 mg 65, fin 5 mg 73, dut 0.5 mg 94) + extra hairs vs placebo; TRT pulses to muscle/bone/fat loss kept, prostate path blocked at DHT gate (Borst); paired side-effect bars (945 vs 934 men, year one); three scalps (patterned / diffuse / patches); labs checklist + magnifier; help flow (history + labs + goals -> telehealth assessment -> plan); sources fan; related hub (6 nodes); final shield breathing between a hair icon and a lab tube.

## Sources summary (22 on page)
- Guidelines/regulators: Endocrine Society 2018 (pattern balding in men with a family tendency = uncommon TRT effect, weak evidence; gels/axillary solution give moderately high DHT of unknown significance); European Dermatology Forum S3 2018 (finasteride 1 mg first line, assess at 6 to 12 months, minoxidil, dutasteride 0.5 mg second line off-label); Health Canada 2026 Summary Safety Review (finasteride link to suicidal ideation; dutasteride precautionary warning); FDA Propecia label 2022 (DHT -65 percent in 24 h, T/E2 +~15 percent within range, PSA 0.7 -> 0.5 ng/mL, year-one sexual AE table, persistent postmarketing reports); FDA 2012 label-change Q&A (421 reports, 59 lasting 3+ months after stopping); MedlinePlus Genetics (50 million US men; more than half of men over 50; growth 2 to 6 years).
- Studies: Kische 2017 JAMA Dermatol (373 men, no link between blood sex hormones and hair loss); Hillmer 2005 (AR gene, maternal line); Heilmann-Heimbach 2017 (63 loci, ~39 percent of variance); Kaufman 1998 (1,553 men, +107 / +138 hairs vs placebo at 1 / 2 years); Gupta 2022 J Dermatolog Treat + JAMA Dermatol network meta (dutasteride 0.5 mg > finasteride 1 mg at 24 weeks; approved in Japan and Korea); Amory 2007 (dutasteride/finasteride 5 mg semen changes, reversible); Overstreet 1999 (finasteride 1 mg, no sperm effect in 181 men); Bhasin 2012 JAMA (139 men, TRT benefits same with dutasteride); Borst 2014 (60 men 60+, finasteride kept TRT benefits and prevented 11.4 cm3 prostate growth); Nickel & Carson 2014 review; Bergfeld 2026 CCJM + Malkud 2015 (telogen effluvium); Walker 2026 JAAPA (TSH, CBC, iron studies); Trost 2006 JAAD (iron deficiency); Viquez Burboa 2026 (GLP-1 RA alopecia OR 1.40, telogen effluvium aOR 1.76).

## Compliance notes (Alex's standing rules)
- Positioning: andropause/low-T telehealth for men in Canada and the USA; copy says what Odin does (free call, plan the right tests, read results in plain language, one written plan covering hormones and hair, hair-tracking photos, PSA/hematocrit tracking, coaching). Never claims Odin prescribes TRT, finasteride or dutasteride; medicines described factually.
- No disclaimer block, no "educational only", no "illustration only", no 911/988 lines, no physician-aware/not-a-treatment wording.
- Doctor words only in the FAQ "How does Odin Health Labs work with my doctor?" (DOM and JSON-LD). Two citation titles were shortened on page to keep that rule (S14 Walker 2026 shown as "Hair loss: a systematic approach to evaluation and management"; S15 Trost 2006 shown as "Iron deficiency, its treatment and its potential relationship to hair loss"); DOIs unchanged.
- No /owen-lowt links, no assessment CTAs; CTAs = booking modal + organic internal links; trackCta / trackBookingLink only.
- No PEMF / hydrogen / marma; no Calgary in-clinic wording.
- Scan rules: no % signs or digit+duration strings ("percent" and spelled-out durations used); no "reverse/reversible", "cure", "guarantee", "proven", "boost testosterone".
- Mojibake 0 (scan for the UTF-8-as-Latin-1 sequences and U+FFFD replacement characters).

## Review flags
- Kische 2017 is cross-sectional (373 men, NE Germany); the page uses it for "blood T level does not predict balding", not for causation.
- Low-T graphic ("three groups of eight men, same share thinning") is a schematic of the null finding, not study counts.
- Health Canada 2026 SSR and FDA persistent-sexual-effect reports are stated as regulator findings; no incidence numbers beyond the label table are given.
- Dutasteride for hair loss is described as off-label outside Japan and South Korea.
- GLP-1 hair shedding described as mostly weight-loss / micronutrient related (meta-analysis wording).

## Inbound link
- Done in this build: /trt-and-fertility Keep reading gained a full-width featured card "Testosterone and hair loss" + 7th hub node (hair icon, data-cta `related_hairloss`); see that page's backups *.bak-hairloss. Its hero entrance fix (`.mg--hero.hero-in.is-paused` running) was added at the same time so reduced-motion hidden is 0 at 390.

## Tested (headless Chrome, puppeteer-core, file:// build, 1280 and 390)
See `test-visual.out.json` and `test-tracking.out.txt`: console errors 0, CLS 0, no overflow, 0 off-screen loops, reduced-motion hidden 0, no-JS hidden 0; tracking 48/48 CTAs fire CTA Click, Booking Link Clicked 2/2, title/desc match seo-meta.md, FAQ DOM == JSON-LD, no /owen-lowt (NO_ASSESS=1); scan.py PASS (0 hits); mojibake 0.
Commands (from /workspace/hp-test): `NODE_PATH=/workspace/hp-test/node_modules node ../pages/_shared/test-visual.js testosterone-and-hair-loss` and `NO_ASSESS=1 NODE_PATH=/workspace/hp-test/node_modules node ../pages/_shared/test-tracking.js testosterone-and-hair-loss`; `python3 scan.py`.

## Publishing checklist (when approved)
New GHL step "Testosterone and Hair Loss" `/testosterone-and-hair-loss` (funnel Odin Health Lab Main Site) -> paste :8780/testosterone-and-hair-loss.txt into its custom-code element -> SEO title/description above -> publish + verify live (curl + 1280/390) -> republish /trt-and-fertility from :8780/trt-and-fertility.txt (inbound card) -> add URL to GHL XML Sitemap generator + llms.txt (:8780/llms.txt) -> GSC/Indexing API + Bing -> GitHub PR from /workspace/ghsync-hairloss.tar.gz.
