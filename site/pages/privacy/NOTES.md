# /privacy (refreshed LOCALLY, NOT published)
Legal page rebuilt on the shared page system (`../_shared/`: base_head/base_motion/base_loader/base_tail, common.py icons/ci(), gfx.py Gen/path/node/dr/dot, answer.css). Own assemble step in `build.py` because (a) no FAQ / no FAQPage JSON-LD on a legal page, (b) the organization's location "Calgary, Alberta, Canada" must stay, which the shared `common.assemble()` forbids. `build.py` asserts Calgary appears ONLY as "Calgary, Alberta, Canada" (+ JSON-LD addressLocality), no /owen-lowt, no PEMF/Hydrogen/Marma/therapy/physician/clinic/"Illustration only"/disclaimer.
Regenerate: `python3 build.py`. Tests from /workspace/hp-test (`NODE_PATH=/workspace/hp-test/node_modules`): `node ../pages/_shared/test-visual.js privacy` and `LEGAL=1 NO_ASSESS=1 node ../pages/_shared/test-tracking.js privacy`.
Paste copy: /tmp/srv2/privacy.txt (http://127.0.0.1:8780/privacy.txt). Source: live page fetched 2026-10-15 with cache-buster, backed up at /workspace/backups-privacy/privacy-live-2026-10-15.html.

## Files
- `page.body.html` = the policy text (edit here, conservatively) + hero, at-a-glance, contents, questions block, final CTA. `page.css` = legal layout + graphics (final state first; loops inside `prefers-reduced-motion: no-preference` + `.js-reveal`; every loop sits in a `[data-live]` block). `build.py` = SEO, JSON-LD, SVGs, section icons.
- `policy-text-live.txt`, `policy-text-new.txt`, `policy-text.diff` = text diff old vs new (header + sections 1-14).

## SEO
- Title (33, unchanged): `Privacy Policy | Odin Health Labs`
- Description (151): `How Odin Health Labs collects, uses and protects personal and health information for telehealth clients in Canada and the USA, and your privacy rights.` (also in /workspace/homepage/seo-meta.md)
- Canonical https://odinhealthlab.ca/privacy; og/twitter = title/desc; robots index,follow.
- JSON-LD: Organization (+ PostalAddress Calgary/AB/CA, ContactPoint email+phone from the live policy, areaServed CA+US), WebSite, WebPage (datePublished 2026-03-19, dateModified 2026-10-15), BreadcrumbList. No FAQPage.
- The live custom HTML carried a second `<title>` and an old meta description "Privacy Policy for Odin Health Labs — Calgary, AB…" plus og:title. The new page.html carries only the single new head (no Calgary, AB meta). The GHL page-level SEO settings should be set to the title/description above when publishing.
- Sitemap: /privacy already in /workspace/homepage/sitemap.xml (yearly, 0.2). No file in the sitemap has <lastmod>, so none was added (kept consistent). llms.txt already lists the privacy policy.

## Policy wording changes (full list; everything else is verbatim)
1. Header: added "Last updated: October 15, 2026" (Effective Date March 19, 2026, Organization, Location kept).
2. S1: "book therapy sessions with us" -> "book a consultation or program with us".
3. S1: "We operate in Calgary, Alberta, Canada and comply with … PIPEDA … PIPA" -> "We are based in Calgary, Alberta, Canada, serve clients by telehealth across Canada and the USA, and comply with … PIPEDA … PIPA" (no new laws named).
4. S2: "goals relevant to your therapy sessions" -> "goals relevant to your consultations and programs".
5. S3: "manage your therapy appointments" -> "manage your appointments".
6. S3: "To provide safe and appropriate health coaching and PEMF therapy services" -> "To deliver our health coaching and telehealth programs safely and appropriately".
7. S5 Analytics & Advertising Partners: added Mixpanel entry (same style as the Google/Meta entries, links mixpanel.com/legal/privacy-policy/). Meta (Facebook) Pixel entry already named Facebook and Instagram: unchanged.
8. S6: "Analytics cookies (Google Analytics)" -> "Analytics cookies (Google Analytics, Mixpanel)".
9. S7: "appropriate and safe therapy services" -> "appropriate and safe health coaching and telehealth services".
10. S13: 'we will revise the "Effective Date"' -> 'we will revise the "Last updated" date' (so the page matches its own stated practice while keeping the original effective date visible). LEGAL REVIEW FLAG.
- Not a wording change: the email shows as plain `office@odinhealthcoaching.com` (live page shows "[email protected]" only because of Cloudflare obfuscation; same address). Links now use rel="noopener noreferrer" + data-cta tracking.
- New presentation copy outside the policy body (restates the policy, no new commitments): "At a glance" cards (not sold / health info not shared without explicit consent except where required by law / access-correction-withdrawal-deletion under PIPEDA and Alberta's PIPA / respond within 30 days), sharing diagram labels (Booking & CRM, Payments, Email tools, Analytics & ads, Not sold), "Questions about your privacy?" block (same email/phone, 30 days), final CTA (telehealth Canada + USA; low T/andropause support, health coaching, functional health, supplement plans).

## Design / motion
Hero: shield + padlock; four source icons (form, calendar, message, heart) send data dots along curves into the shield; keyhole pulses + ring every 2 s as each arrives; dashed orbit turns; sparkles twinkle. At-a-glance cards with pulsing icon chips. Contents card (sticky at >=1024px, 2 cols 600-1023, 1 col mobile) with anchor links; 14 numbered sections each with its own animated icon chip (doc+shield pop, form dot slide, gear spin, scale tip, share-node hop, cookie crumb blink, heart beat, clock hand, check pop, lock keyhole beat, link bob, shield pop, refresh spin, envelope flap). S4 and S9 lists as icon cards. S5 sharing diagram (you -> Odin -> 4 provider types, pulses; crossed "Not sold" tag). Questions block with envelope (message drops in, tick confirms). Final CTA halo. All transform/opacity; draw-on once.
CTAs (all data-cta prefixed privacy_, plus shared modal_first_time/modal_follow_up): crumb_home, hero_contents, hero_contact, glance_sharing/health/rights/contact, link_google_policy/mixpanel_policy/meta_policy/ga_optout/oipc, rights_email, s14_email, s14_phone, ask_email, ask_phone, final_book_call (booking modal), final_home, explore_lowt/health_coaching/functional_health/supplements. No /owen-lowt.

## Tests (2026-10-15 ~20:15 MDT)
- Visual 1280 + 390: 0 console errors, CLS 0, no horizontal overflow, reduced-motion 0 running / 0 hidden, no-JS 0 hidden, 0 running loops offscreen (19 [data-live] blocks). (One run under heavy box load reported no-JS hidden 1 at 390 from the shared hero entrance timing; isolated recheck + rerun = 0.) The test's own full-*.png only scrolls to figures, so lower reveals look blank there; a manual scroll-through confirmed every .reveal turns on (shots/scrolled-1280-full.png, view-*-390.png, reduced-*-full.png show the full page).
- Tracking (LEGAL=1 NO_ASSESS=1): 25/25 CTAs fire 'CTA Click' with page:privacy; all checks PASS. Banned-claim scan = INFO only ("30 days", "100% secure", retention periods: legal text kept verbatim).
- Shared test change: `../_shared/test-tracking.js` got a `LEGAL=1` mode (no FAQPage expected, Calgary allowed only as the org location, CTA prefix check, banned scan reported as INFO), a null-safe FAQ read and a fallback for the "no mixpanel" click when a page has no hero_book_call. Default behaviour for the other pages is unchanged. Backup: /workspace/backups-privacy/test-tracking.js.bak.

## Legal review flags (for Alex)
1. Section 13: changed "Effective Date" -> "Last updated" date. Alternative: keep S13 verbatim and instead set the Effective Date to the publish date.
2. Mixpanel retention: S8 still lists analytics retention only for Google Analytics (up to 26 months). No Mixpanel retention period was added (not invented); Alex should confirm the Mixpanel project's retention setting if he wants it stated.
3. US clients: the policy still names only Canadian law (PIPEDA, Alberta PIPA) and Canadian regulators. No US/state-law or HIPAA claims were added. Serving US residents by telehealth may bring US federal/state privacy obligations (for example state consumer-health-data laws); worth a lawyer's look. Data location / cross-border transfer (GoHighLevel, Google, Meta, Mixpanel are US-based services) is not discussed in the live policy and was not added.
4. "Client and appointment records … minimum of 7 years to comply with Alberta health and business record-keeping requirements" kept verbatim; whether that basis applies to a coaching/telehealth business is for Alex/counsel.
5. Contact email is on a different domain (odinhealthcoaching.com) than the site (odinhealthlab.ca); reused as-is from the live page. Confirm it is still monitored.
6. Google Analytics is kept as named on the live page; if GA is no longer installed on the site, Alex may want it removed (not removed here).
7. Children's section says services are not directed to under-18s; kept verbatim.

## Publishing checklist (when approved)
GHL /privacy page: replace the custom-code element with page.html (http://127.0.0.1:8780/privacy.txt), set page SEO title/description from seo-meta.md, publish, verify with a cache-busted curl (single <title>, no "Calgary, AB" meta). Then GitHub PR (pages/privacy, pages/_shared/test-tracking.js, homepage/seo-meta.md).
