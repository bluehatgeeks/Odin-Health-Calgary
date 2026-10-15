# Odin backlog (work top-down, one or more items per loop; mark DONE with date)
1. DONE 2026-10-15 (llms.txt live via domain Edit dialog; sitemap live with 10 non-Paid pages; /owen-lowt left out as likely Paid). Publish llms.txt (prepared: /workspace/homepage/llms.txt) and a non-paid sitemap (/workspace/homepage/sitemap.xml) in HighLevel Domains/robots settings; verify live.
2. DEFERRED (nav is shared by [Paid] pages; only change link text/targets if verified safe): Nav: change "Take The Assessment" to point to /owen-lowt; remove PEMF/Hydrogen/Marma if in nav; update repo odinnav.html via cloud agent PR (shared by [Paid] pages: only low-risk link/text changes, verify after).
3. DONE 2026-10-15 for 10 non-Paid pages (GHL SEO fields set, live first <title>/description match). FOLLOW-UP: 8 pages still carry an old duplicate <title>/meta description (Calgary) in their custom HTML; remove when each page is rewritten (item 4). Per-page SEO titles/descriptions/canonical for non-paid pages from seo-meta.md; noindex duplicates (/owen, /emma, /quiz) only if not [Paid].
4. Rebuild non-paid therapy pages (functional-health, health-coaching, supplements, ayurveda, privacy) around andropause/telehealth with motion graphics; remove "Calgary in-clinic" wording; compliance flags in NOTES.md.
5. Fix Booking Link Clicked tracking gap; add Mixpanel events on new homepage; AI-referrer property.
6. Newsletter: GHL consent signup form + first 3 drafted issues (drafts only, never send).
7. New organic content pages (answer-style): low testosterone symptoms, andropause vs menopause, TRT vs lifestyle questions, when to see a doctor; each with motion graphics, FAQ schema, internal links.
8. Performance: compress images, alt text, Lighthouse run, fix findings.
9. Read Mixpanel traffic (web UI) weekly and log trend in /workspace/odin-site-log.md.
Every change: commit to GitHub (bluehatgeeks/Odin-Health-Calgary) via cloud agent PR and merge if additive/safe.

10. IN PROGRESS 2026-10-15: homepage tracking bug fix (function track overwritten by var track; renamed trackCta) publishing; then publish rewritten /functional-health (/workspace/pages/functional-health/page.html, built, tested, flags in its NOTES.md); then push both to GitHub; then verify Mixpanel CTA Click events arrive; then rewrite next pages (health-coaching, supplements, ayurveda, pemf, hydrogen, marma, shift, privacy) same way, removing old duplicate Calgary head tags.

## Update 2026-10-15 13:20
- DONE & LIVE: /functional-health (disclaimer paragraph removed per Alex), /health-coaching, /supplements.
- GitHub: PR #3 merged (homepage trackCta, functional-health). Health-coaching/supplements sync PR in progress.
- Shared info with Odin X Marketer (X agent): live URLs sent; he has 0 followers, no data until Oct 18 report. His question list = answer-page candidates: TRT vs fixing causes, TRT & fertility, labs to ask for (free T, SHBG, LH/FSH, estradiol), low T aging vs weight, weight-loss drugs & testosterone, peptides status CA/US (Health Canada Apr 2026 advisory).
- NEXT: rewrite remaining non-paid pages (ayurveda, pemf, hydrogen, marma, shift, privacy); new answer pages; Search Console/Bing access needed from Alex; verify Mixpanel CTA Click events.
