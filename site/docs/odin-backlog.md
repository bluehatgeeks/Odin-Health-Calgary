# Odin backlog (work top-down, one or more items per loop; mark DONE with date)
1. DONE 2026-10-15 (llms.txt live via domain Edit dialog; sitemap live with 10 non-Paid pages; /owen-lowt left out as likely Paid). Publish llms.txt (prepared: /workspace/homepage/llms.txt) and a non-paid sitemap (/workspace/homepage/sitemap.xml) in HighLevel Domains/robots settings; verify live.
2. DEFERRED (nav is shared by [Paid] pages; only change link text/targets if verified safe): Nav: change "Take The Assessment" to point to /owen-lowt; remove PEMF/Hydrogen/Marma if in nav; update repo odinnav.html via cloud agent PR (shared by [Paid] pages: only low-risk link/text changes, verify after).
3. DONE 2026-10-15 for 10 non-Paid pages (GHL SEO fields set, live first <title>/description match). FOLLOW-UP: 8 pages still carry an old duplicate <title>/meta description (Calgary) in their custom HTML; remove when each page is rewritten (item 4). Per-page SEO titles/descriptions/canonical for non-paid pages from seo-meta.md; noindex duplicates (/owen, /emma, /quiz) only if not [Paid].
4. PARTIAL DONE 2026-10-15: functional-health, health-coaching, supplements, ayurveda, shift live. Still: privacy (+ pemf/hydrogen/marma educational). Rebuild non-paid therapy pages (functional-health, health-coaching, supplements, ayurveda, privacy) around andropause/telehealth with motion graphics; remove "Calgary in-clinic" wording; compliance flags in NOTES.md.
5. Fix Booking Link Clicked tracking gap; add Mixpanel events on new homepage; AI-referrer property.
6. Newsletter: GHL consent signup form + first 3 drafted issues (drafts only, never send).
7. DONE 2026-10-15 first two live (trt-or-fix-causes-first, low-testosterone-labs-to-ask-for). MORE New organic content pages (answer-style): low testosterone symptoms, andropause vs menopause, TRT vs lifestyle questions, when to see a doctor; each with motion graphics, FAQ schema, internal links.
8. Performance: compress images, alt text, Lighthouse run, fix findings.
9. Read Mixpanel traffic (web UI) weekly and log trend in /workspace/odin-site-log.md.
Every change: commit to GitHub (bluehatgeeks/Odin-Health-Calgary) via cloud agent PR and merge if additive/safe.

10. PARTIAL 2026-10-15: therapy rewrites — functional-health, health-coaching, supplements, shift, ayurveda DONE live; remaining: pemf, hydrogen-inhalation, marma-therapy, privacy. Answer pages 2/N live. GitHub through PR #7 merged.

## Update 2026-10-15 14:42 MDT
- DONE & LIVE this loop: /shift, /ayurveda (motion + andropause/telehealth, Canada+USA). llms.txt Answers section live. GitHub: PR #6 (answer pages) and #7 (shift+ayurveda) merged.
- Already live earlier: /, /functional-health, /health-coaching, /supplements, /trt-or-fix-causes-first, /low-testosterone-labs-to-ask-for.
- Leftover: page/nav still references #metabolic-assessment-trigger on /shift (and appears on /ayurveda — likely shared loader/nav); page-local Navigation on /shift needs assessment link → /owen-lowt (deferred with item 2 if shared).
- NEXT: educational reframes /pemf, /hydrogen-inhalation, /marma-therapy; /privacy legal pass; more answer pages (TRT+fertility, aging vs weight, peptides CA/US); Mixpanel CTA Click verify; Search Console/Bing (needs Alex).

## Update 2026-10-15 14:35 MDT
- LIVE: /shift rewrite published (funnel Odin Health Lab Main Site, step Shift Work Page). llms.txt Answers section live. Answer pages GitHub PR #6 merged.
- IN PROGRESS: /ayurveda GHL publish; GitHub PR #7 for shift+ayurveda sources.
- Leftover on /shift: page-level Navigation custom-code still links "Take The Assessment" to #metabolic-assessment-trigger (dead); fix to /owen-lowt in a follow-up (page-local nav only, not shared Paid nav).
- NEXT: finish ayurveda publish+verify; then pemf/hydrogen/marma educational reframes, privacy, more answer pages, Mixpanel CTA verify.

## Update 2026-10-15 14:15 MDT (continuous loop)
- DONE & LIVE already: /functional-health, /health-coaching, /supplements, answer pages /trt-or-fix-causes-first and /low-testosterone-labs-to-ask-for (titles+content verified). GitHub PRs #1–#5 merged earlier; answer-page sources PR launching now.
- IN PROGRESS this run: rewrite /shift (highest low-T relevance among remaining therapy pages); publish updated llms.txt (add answer-page links); GitHub sync for answer pages + _shared (gfx.py, answer.css) + seo/sitemap/llms.
- NEXT after shift: /ayurveda, then educational reframes for in-clinic modalities (/pemf, /hydrogen-inhalation, /marma-therapy), /privacy (legal), more answer pages (fertility+TRT, labs aging vs weight, peptides CA/US), Mixpanel CTA Click verify, Search Console/Bing (needs Alex).
- DEFERRED: nav shared-by-[Paid] changes (item 2).

## Update 2026-10-15 13:20
- DONE & LIVE: /functional-health (disclaimer paragraph removed per Alex), /health-coaching, /supplements.
- GitHub: PR #3 merged (homepage trackCta, functional-health). Health-coaching/supplements sync PR in progress.
- Shared info with Odin X Marketer (X agent): live URLs sent; he has 0 followers, no data until Oct 18 report. His question list = answer-page candidates: TRT vs fixing causes, TRT & fertility, labs to ask for (free T, SHBG, LH/FSH, estradiol), low T aging vs weight, weight-loss drugs & testosterone, peptides status CA/US (Health Canada Apr 2026 advisory).
- NEXT: rewrite remaining non-paid pages (ayurveda, pemf, hydrogen, marma, shift, privacy); new answer pages; Search Console/Bing access needed from Alex; verify Mixpanel CTA Click events.

## Update 2026-10-15 14:30 MDT (copy pass: lead with what we do, no physician-aware boilerplate) — LOCAL ONLY, NOT PUBLISHED
- Alex instruction (t39u): remove constant physician-aware / "what we don't do" wording everywhere except FAQ answers about working with doctors; rephrase supplements intro positively.
- DONE locally (source + generated page.html rebuilt): homepage, functional-health, health-coaching, supplements, trt-or-fix-causes-first, low-testosterone-labs-to-ask-for. Backups of pre-edit files in /workspace/backups-nophys/ and homepage/*.bak-nophys.
- TODO: re-publish all six pages in GHL (+ push to GitHub); the two answer pages need re-publish after their current publish finishes. Meta descriptions of /functional-health and /trt-or-fix-causes-first still contain "physicians" / "decide with a physician" (seo-meta.md values, left unchanged on purpose): ask Alex whether to reword.
- Not mine, untouched: /shift has "do not diagnose disease or replace your physician" + "Do you practice medicine? No." FAQ; /pemf has a testimonial mentioning a doctor.
