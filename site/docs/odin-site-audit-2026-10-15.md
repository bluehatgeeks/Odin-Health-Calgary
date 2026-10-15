# Odin Health Labs — First Site Audit (SEO + chatbot/LLM readiness + source map)
Date: 2026-10-15 (read-only audit; nothing changed on the site, repo or HighLevel)
Scope: https://odinhealthlab.ca/ , /owen-lowt , robots.txt, sitemap.xml, llms.txt, repo bluehatgeeks/Odin-Health-Calgary, Mixpanel instrumentation in code.
Raw fetches saved in /workspace/audit/.

## 0. Executive summary
- The site is crawlable (server-rendered HTML, no noindex) but is **almost invisible to search engines and AI answer engines**: robots.txt, sitemap.xml and llms.txt are all empty; no canonical tags; no OpenGraph/Twitter tags; no JSON-LD anywhere; internal nav only exists after JS runs.
- The homepage still says "Metabolic Optimisation in Calgary / We Do Not Practice Medicine / Health coaching" while the money funnel (/owen-lowt) says "clinician call", "Low T", "TRT", "80% of men". Positioning, geography and compliance posture contradict each other.
- Live /owen-lowt and /owen are the same page (duplicate content, no canonical). Old landers (/owen, /emma, /quiz, /marma-therapy) are all publicly indexable.
- The repo does NOT contain owen-lowt.html. The live /owen-lowt page is custom code pasted directly in HighLevel; the repo (branch master = what the CDN serves) only supplies CSS, nav and footer. Repo owen.html on `main` is stale versus live.
- Mixpanel: public token in page JS, autocapture + 100% session recording on a health quiz (privacy flag). Custom events listed in section 4.

## 1. Live site findings

### 1.1 Fetch status
| URL | HTTP | Notes |
|---|---|---|
| / | 200 | HTML 202 KB raw / 40 KB gzip, TTFB ~0.15 s (Cloudflare+GHL cache) |
| /owen-lowt | 200 | HTML 264 KB raw / 53 KB gzip |
| /robots.txt | 200 | **0 bytes** (empty; no Sitemap: line, no rules) |
| /sitemap.xml | 200 | Valid but **empty** `<urlset>` (0 URLs) |
| /llms.txt | 200 | **0 bytes** (empty) |
| www.odinhealthlab.ca | 301 -> apex | OK |
| http://odinhealthlab.ca | timed out from our box | not verified; recheck from another network |
| /functional-coaching, /bio, /about, /blog, /shift-calgary, /hydrogen-therapy, /nutritional-supplementation | 301 -> / | nav in repo links to /health-coaching and /supplements instead (those return 200) |
| /health-coaching, /supplements, /functional-health, /ayurveda, /privacy, /owen, /emma, /quiz, /marma-therapy | 200 | all indexable, no canonical |

### 1.2 Homepage (/)
- Title: "Metabolic Optimisation in Calgary | Odin Lab" (46 chars, OK length; Calgary-only framing vs telehealth Canada+USA doctrine)
- Meta description: "Metabolic optimisation in Calgary. Unlock lasting energy, clarity, and vitality through the Odin Labs Systems Optimisation Framework. Assessment, recalibration, and ongoing support." (good length, no keywords people search)
- H1: "Your Symptoms Are Not Random." (no keyword; no topic/entity)
- H2s: Metabolic Stability Assessment; Metabolism Is Not Just About Weight.; The Symptoms May Look Different...; You Feel Functional — But Not Optimal.; The Odin Labs Systems Optimisation Framework™; What Working With Odin Labs Looks Like; What Happens When Metabolic Stability Returns; Frequently Asked Questions; Your Health Partner, Not Just Another Clinic; Your Symptoms Are Signals. Quiz questions are rendered as H3 (11 H3s from quiz, one empty H3) — pollutes outline.
- Canonical: **none**. OpenGraph: only `og:type=website` (no og:title/description/image/url). Twitter: only `twitter:type` (invalid; should be twitter:card). No `robots` meta (indexable by default).
- JSON-LD / schema: **none** (no Organization, MedicalBusiness/Physician, FAQPage, Person, WebSite).
- Images: 7 `<img>`; 3 with missing/empty alt (a 1x1 Facebook pixel noscript tag, and the same hero PNG twice with alt=""). Others have short alt text. Three 0.98–1.33 MB PNGs from filesafe.space, no width/height, no lazy-loading, not WebP/AVIF.
- Mobile: `<meta name=viewport content="width=device-width, initial-scale=1">` present (duplicated, one with 1.0). Fine.
- Language: `<html lang="en">` (use en-CA).
- Crawlable without JS: **mostly yes** — body copy (~9 KB of text) and FAQ are in server HTML. **No** for global nav and footer: injected at runtime by odin-loader.js from jsDelivr, so crawlers/LLMs that don't run JS see only 7 links on the whole page (4 are `#`, 1 anchor, 2 booking widgets). The therapy pages (functional-health, ayurveda, health-coaching, supplements) get zero internal links in raw HTML.
- Internal links in raw HTML: `#` x3, `#about-us-section`, two api.leadconnectorhq.com booking-widget URLs.
- Tracking present: Mixpanel (autocapture + session recording 100%), Google Ads gtag AW-18027994169, Meta pixel 705890611034328 **and also a second `fbq('init','YOUR_PIXEL_ID')` placeholder** plus a noscript pixel `id=YOUR_PIXEL_ID` (broken, creates Meta noise/errors).
- Page-speed red flags: 113 KB inline JS + 53 KB inline CSS in HTML; render-blocking external CSS from jsDelivr pinned to `@master` (odin-shared.css?v=6, odinlabcalgary.css?v=4); heavy PNGs; Mixpanel 100% replay + autocapture; nav/footer waterfall fetch (CLS risk); Nuxt/GHL preview bundle `stcdn.leadconnectorhq.com/_preview/Bk79ukVa.js`. No Core Web Vitals measured yet (no Lighthouse run — see blockers).

### 1.3 /owen-lowt
- Title: "Low-T Pattern Assessment | Odin Lab" ; description: "Take the free 3-minute assessment. Find out if your fatigue, drive, and body composition changes are a fixable pattern - before you try TRT or another supplement stack."
- H1: "Fix Low T Without TRT - The Approach That Works for 80% of Men." H2: "Currently Completing: Low-T Pattern Assessment (Step 1)". 8 quiz questions as H3 + results/redirect H3s. Very thin non-quiz text (~4.8 KB total visible; much is quiz options).
- Canonical none; OG only og:type; no JSON-LD; 0 `<img>` (video thumbnail handled in JS); 2 forms; 4 links (booking widget, AHS, Health Canada, homepage).
- Duplicate: `/owen` serves identical title/H1/description. No canonical -> two competing URLs. Paid-ad lander; consider noindex or canonical decision (see fixes).
- Quiz/results/booking content is JS-gated by design (fine for ads), but it means little rankable content. Inline JS 154 KB, inline CSS 82 KB.
- Brand/entity inconsistencies: "Odin Lab" (title), "Odin Labs", "Odin Health Labs", "Odin Lab Calgary", footer "Odin Labs Functional Health Calgary".

## 2. Source-code map
Repo: github.com/bluehatgeeks/Odin-Health-Calgary (public). Default branch **master** (HEAD 3295f32, 2026-09-22 "remove PEMF, Hydrogen, Marma from Our Therapies menu"). Second branch **main** (3b3b31c) is a much larger monorepo snapshot (362 files incl. Calgary-Local ops, supabase, scripts, Telehealth docs).
- **master (flat, 106 files) = what GHL loads via jsDelivr `cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/...`:**
  - Live pages' shared assets: `odin-shared.css` (?v=6), `odinlabcalgary.css` (?v=4) — loaded on homepage; `odin-shared.css` on /owen-lowt.
  - `odin-loader.js` fetches `odinnav.html` and `odinfooter.html?v=2` at runtime and injects into the page (this is why nav/footer are not in raw HTML). Footer text rebrand "Odin Labs Functional Health Calgary".
  - Page source HTML (pasted by hand into GHL custom-code blocks, not fetched live): `odinlabcalgary.html` (homepage; 57 KB), `functional-health.html`, `functional-coaching.html` (live as /health-coaching), `ayurveda.html`, `nutritional-supplementation.html` (live as /supplements), `hydrogen-therapy.html`, `marma-therapy.html`, `privacy.html`, `bio.html`, `shift-calgary.html`, `odintherapiestemplate.html/.css`, plus per-page CSS. Also `index.html`, `optithx.html`, `templatetest.html` (2 MB), `hero_*` assets (not live pages).
  - `design.md`, `CLAUDE.md` (rules: use CSS tokens, `.booking-trigger` on CTAs, bump `?v=N` on CSS edits, nav/footer via shared loader).
  - Weight: ~25 MB of PNG/JPG in `img/` and root (many 0.7–2 MB) — only relevant if served via jsDelivr to the site.
- **main:** adds `06_MARKETING_GROWTH/Odin Labs Landers/` with `owen.html` (73 KB, Owen quiz lander), `emma.html`, `quiz.html`, `optimalhealth*.html`, `img/owen-lowt-miniclass-thumbnail.jpg`, `ghl-mixpanel-booking-webhook.md`, `meta-capi-session-notes.md`, test logs (`Calgary-Local/marketing/tests/*`), Mixpanel->Supabase sync (`supabase/functions/fetch_mixpanel_events/`, `mixpanel_event_mapping.json`), `Telehealth/` docs and Remotion video source, `keyword_data/*.json` (SEO keyword research already exists: `07_TECH_STACK/keyword_data/`).
- **Key finding:** **there is no `owen-lowt.html` in either branch.** Live /owen-lowt is a GHL-only custom code page (~154 KB inline JS), a newer fork of `owen.html` (has `Video Lead Captured`, `Quiz Reveal Clicked` events that owen.html doesn't). The thumbnail jpg for it is in `main` only. Risk: no version control / rollback for the revenue page. The repo's `owen.html` is stale; live `/owen` is another stale copy.
- Not in repo/GHL-visible via code: `robots.txt`, `sitemap.xml`, `llms.txt` (all empty) — configured in GHL Settings > Domains/SEO (to check once GHL access is used).
- Caching note: jsDelivr `@master` caches branch content (hours). CSS/nav changes need `?v=` bump or jsDelivr purge, or pin to commit SHA.
- Repo README.md is outdated marketing-style boilerplate (claims 95/100 mobile score etc.) — do not trust.
- Contains secrets? Public Mixpanel project token (9c1c…e2b5) is intentionally public. Did not scan for other secrets in `main` (`getting-started-with-browserbase/.env.example`, `.cursor/mcp.json` exist: recommend a secret scan since repo is public).

## 3. Mixpanel (from code + repo docs)
Init (both live pages): `mixpanel.init('9c1ce1f2580971e0928ba7cc09cb542e', {autocapture:true, record_sessions_percent:100})`; `identify`/`people.set` with UTM/fbclid attribution; `mixpanel.track("Page View", attribution)`; `mixpanel_id` forwarded to GHL.
Custom events in live /owen-lowt:
- `Page View` (homepage and Owen)
- `Quiz Reveal Clicked` {quiz:'owen-lowt'}
- `Video Lead Captured` {quiz, source:'miniclass_video'}
- `Step1 Results Expanded`
- `Outcome Shown`
- `Investment History Answer`
- `Booking Link Clicked`
- `Booking Iframe Loaded`
- `Booking Iframe Failed`
- Meta pixel via helper: ViewContent / Lead (content_name 'owen-lowt-quiz') and `trackFbqVideo`.
Server-side (documented, GHL workflow): `Appointment Booked` (distinct_id = email, calendar, utm_*, mixpanel_device_id). Known gap: no calendar/source filter (counts all clinic bookings).
Docs in `main` mention events not in current live code: `Results CTA Clicked`, `Qualifier Answer`, `Qualifier Passed` (legacy owen.html funnel) — verify in Mixpanel which still receive data.
Homepage: only `Page View` + autocapture; **no custom events** for CTA clicks, quiz start/complete, or booking-widget open on the homepage -> homepage funnel is largely blind. No events for organic/search source (no SEO-specific tagging, no `referrer`/AI-referrer capture).
Not checked: actual Mixpanel data (no access yet — blocker).

## 4. Compliance-sensitive copy (FLAGS ONLY — no changes made)
Per owner doc (2026-09-03) compliance is considered in-scope, but these are worth an explicit review by the owner/counsel (Health Canada, Alberta CPSA/regulated health professions, US FTC/FDA if USA targeted, Meta/Google health ad policies):
1. /owen-lowt H1: "Fix Low T Without TRT - The Approach That Works for 80% of Men." — unsubstantiated efficacy statistic; implies treatment of a medical condition; no source/disclaimer.
2. "Doctors are pushing you towards TRT." / "Why standard bloodwork misses this pattern" / "internet… miracle solutions that do not work" — disparages medical care; anti-TRT advice may be read as medical advice.
3. Naming "TRT" and "Low T" (prescription-drug-adjacent terms) in ad/landing copy; "clinician" / "Clinician Interpretation of Results" — implies a licensed clinician. Who is the clinician and what licence? Homepage says "We Do Not Practice Medicine… do not diagnose disease". Direct contradiction between pages.
4. Quiz "identifies your pattern" / "Pattern Identified" results — pseudo-diagnostic output; screens for opioids/corticosteroids/steroid use (health data collection) with email capture, plus **Mixpanel autocapture + 100% session replay on this quiz** = sensitive health info collection (PIPEDA/Alberta HIA/US state health-data laws, CCPA/WA My Health My Data). No consent banner seen; privacy policy exists at /privacy (check it covers Mixpanel replay, Meta pixel, cross-border).
5. Homepage: "Many clients notice meaningful shifts within 14–30 days", "restore stability", "recalibrate hormones", "Hormones stabilise", testimonials ("My hormones feel stable for the first time in years") — outcome claims/testimonials without disclaimer; named only by role ("Calgary Mother").
6. Homepage "Precision herbal protocols, Pulsed Electromagnetic Field Therapy" (PEMF) — device claims (Health Canada device licensing); (PEMF/Hydrogen/Marma removed from nav on 2026-09-22 but still on homepage and live pages).
7. /health-coaching: "168K+ Study Participants Covered" and "clinically meaningful reductions in HbA1c…" with a citation; "8 years of afternoon energy crashes — gone within 14 weeks" (testimonial claim).
8. Homepage "Clinical Director & Founder", "since 1998" — title implies clinical credentials; verify licensure/credential wording.
9. Homepage quiz asks biological sex and cycle questions and shows "Limited client spots per month" scarcity line — conflicts with the stated doctrine "belief over urgency/scarcity".
10. Pixel placeholder `YOUR_PIXEL_ID` and Meta Pixel on health-adjacent pages (Meta restricts health data events).
11. Calgary-only geographic claims ("Calgary-Based Practice", "Our Clinic", Calgary-named testimonials) conflict with telehealth-only pivot (patient-trust and false-impression risk once clinic closed).

## 5. Top 10 fixes — ranked by traffic impact vs effort
(Impact H/M/L, Effort S/M/L; order = recommended execution order.)
1. **Fill robots.txt + sitemap.xml** (H / S). Currently empty. Add `User-agent: *` Allow, `Sitemap:` line; populate sitemap with the 5–8 pages that should rank (/, /functional-health, /health-coaching, /supplements, /ayurveda, /privacy; exclude ad landers). In GHL: Settings > Business Profile/Domains > SEO or per-page "Include in sitemap". Submit to Google Search Console + Bing.
2. **Add canonical tags + resolve /owen vs /owen-lowt (and /emma, /quiz) duplicates** (H / S). Canonical to self on all pages; noindex (or 301) the legacy ad landers and decide indexing for /owen-lowt.
3. **Rewrite homepage title/H1/meta for telehealth Canada+USA + searchable intent** (H / S-M). e.g. title "Online Men's Health & Low-T Support (Canada & USA) | Odin Health Labs". Remove "Calgary"-only framing. H1 should state who/what/where. Needs owner decision on positioning (and compliance wording).
4. **Make nav/footer/internal links present in server HTML** (H / M). Inline the nav and footer links (or at minimum a crawlable `<nav>` with plain `<a href>` to /functional-health, /health-coaching, /supplements, /ayurveda, /privacy) rather than JS-only injection; add footer links, breadcrumbs on therapy pages.
5. **Add JSON-LD structured data** (H / S-M): Organization + MedicalBusiness/ProfessionalService (telehealth, areaServed Canada/USA, sameAs, logo), WebSite, Person (Alexander Tretjakov, credentials as legally permitted), FAQPage on homepage FAQ and therapy pages. Validate with Rich Results Test.
6. **OpenGraph/Twitter cards + favicon/brand name consistency** (M / S): og:title/description/image/url, `twitter:card=summary_large_image`; unify to one brand name ("Odin Health Labs"). Better social/AI link previews and click-through.
7. **Create content that can rank: SEO pages/blog** (H / L): keyword research already exists in repo (`07_TECH_STACK/keyword_data/*.json`). Build 6–10 answer-style pages ("Low testosterone symptoms in men over 40", "Andropause vs burnout", "TRT alternatives…", "How telehealth consults work in Canada") with FAQ, author, date, sources. /blog currently 301s to homepage. Needs compliance review first.
8. **Fix image performance + alt text** (M / S-M): convert 1–1.3 MB homepage PNGs to WebP/AVIF ≤150 KB, add width/height, `loading="lazy"` below the fold, meaningful alt (duplicate hero image has alt=""), remove broken `YOUR_PIXEL_ID` tracking pixel/second fbq init.
9. **Core Web Vitals pass** (M / M): move/trim 113–154 KB inline JS, defer Mixpanel session replay (lower `record_sessions_percent` and mask quiz inputs), avoid render-blocking jsDelivr CSS (inline critical CSS, or pin to commit SHA with long cache), preload hero. Measure with Lighthouse/PageSpeed first.
10. **Add owen-lowt.html to the repo + homepage event tracking + SEO tracking** (M / S): commit the live lander for version control; add Mixpanel events on homepage (`Quiz Started/Completed`, `Booking CTA Clicked`, `FAQ Opened`), capture `referrer`/utm/AI-referrers (chatgpt.com, perplexity.ai, gemini) as a property so SEO/AI traffic can be measured.
(Compliance copy review, section 4, is a parallel gating item, especially #3 and #7 before publishing new copy.)

## 6. Newsletter + chatbot/LLM-readiness recommendations
Chatbot / LLM readiness
- Publish **/llms.txt** (currently empty): 1-paragraph business summary (telehealth, Canada+USA, who it's for, what it is/isn't — e.g. "does not diagnose/prescribe" wording as legally accurate), key URLs with one-line descriptions, contact/booking URL, last-updated date. Optional `/llms-full.txt` with core page text in markdown.
- Make sure robots.txt does not block GPTBot, ClaudeBot, PerplexityBot, Google-Extended, etc. (currently no rules = allowed; keep explicit Allow once file is filled). Cloudflare is in front: check Cloudflare "AI crawlers / bot fight mode" settings aren't blocking them.
- FAQPage JSON-LD on homepage and each therapy page; write FAQs as direct questions with 40–80 word first-sentence answers ("What is andropause? ...", "Is Odin Labs a doctor? ...", "Do you serve patients outside Alberta?", "How much does it cost / is it covered?").
- Answer-style content: definitions, symptom checklists, "who this is not for", comparison tables, dated authorship, cited sources. Add visible author byline + credentials, Last updated dates, About/Team page (E-E-A-T; YMYL health content is held to a high standard).
- Put key facts in server HTML (nav, footer, address/service area, hours, pricing statement). Do not hide key content behind the quiz.
- Add entity consistency: same name/description across site, Google Business Profile (update from Calgary clinic to telehealth), LinkedIn, Meta, directories (sameAs in schema).
- Track AI referrals in Mixpanel (referrer domains) and monitor "odin health labs" mentions in ChatGPT/Perplexity/Gemini monthly.
Newsletter
- Add a lightweight email capture on the homepage and therapy pages (GHL form -> tag `newsletter`), separate from quiz leads; consent checkbox (CASL for Canada, CAN-SPAM for USA), unsubscribe + physical address in footer.
- Cadence: weekly or biweekly; format = 1 education piece (symptom-first language, belief-shift per doctrine, no scarcity/discount), 1 "ask the practitioner" Q&A, 1 soft CTA to the quiz/intake. Each issue republished as an SEO/answer-style web page (feeds #7).
- Use GHL email/Workflows + Mixpanel events `Newsletter Subscribed` with UTM source; welcome sequence of 3 emails from the mini-class video.
- Segment by quiz outcome (Owen Low-T vs general metabolic) for relevance.
- All claims reviewed against section 4 flags before send.

## 7. Blockers / missing access
1. **Mixpanel**: no access (connector can't auth from here). Need a service account (username + secret) + project ID, or an exported report. Without it I can't measure traffic, sources, funnels, or baseline.
2. **HighLevel editing**: logged in as the new user (Odin Health Labs Calgary account) but I have not yet verified what I can edit (Sites > Funnels/Websites > custom code, Settings > SEO/Domains, robots.txt/sitemap/llms.txt location) — this audit was read-only.
3. **Google Search Console / Bing Webmaster / GA**: not connected — need ownership verification (DNS or HTML tag via GHL) to see impressions, indexed pages, queries, and submit sitemap. Unknown how many pages are indexed today.
4. **Lighthouse/CrUX numbers**: not measured (no headless browser run); page-speed items above are static-analysis red flags only.
5. **GitHub write path**: reading works through cursor-github (connected as @bluehatgeeks, admin on the repo). Any edit should go on a branch/PR; note CDN is pinned to `master` (cache) and live HTML is pasted into GHL manually, so repo changes alone do not change pages.
6. **http:// (port 80) check timed out** from our box; recheck HTTP->HTTPS redirect from another network.
7. `/owen-lowt` source is only in GHL: needs a copy exported into the repo before we edit it (rollback safety).
8. Owner decisions needed: homepage positioning (telehealth vs Calgary coaching), whether /owen-lowt should be indexed, compliance sign-off on health claims, which pages to remove/redirect.
