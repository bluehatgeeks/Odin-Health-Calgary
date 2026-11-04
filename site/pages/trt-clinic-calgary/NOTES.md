# /trt-clinic-calgary (t2-1028, BUILT LOCALLY 2026-10-28, not published)
- Why: Odin X Marketer T2 item 5. Path was a soft 404 (200 + homepage title/canonical). treg Google CA volumes (2026-10-28): trt calgary 210, testosterone replacement therapy calgary 140, testosterone clinic calgary 50, trt alberta 30; 'trt clinic calgary' no data. SERP top: drbobby.ca, precisioncliniccalgary.ca, varsitymedical.ca, avovita.ca, gamedaymenshealth.ca (x2), vitalityatgloantiaging.com (raw: /workspace/t2-1028/kw.json, serp.json).
- Title (57) 'TRT Calgary: Online Testosterone Clinic | Odin Health Lab'; desc (146); H1 'TRT clinic in Calgary: low testosterone care by telehealth'. Byline Alexander Tretjakov, Founder; Article author = Person #alexander-tretjakov; WebPage spatialCoverage Calgary/Alberta.
- Sections: hero (loop motion), #how (3 panels), #alberta-labs (APL range bars), #cost (fee bars), Keep reading (4 cards, 2-col), FAQ 6 (DOM == JSON-LD), final CTA, x-follow end line.
- Facts reused only from sourced pages: Alberta DBL cypionate $34.88/10 mL regular benefit, gels not a benefit, capsule criteria (/trt-cost SOURCES C9); APL LAB124 8.0-35.0 nmol/L (up to 25% lower later in day), LAB1756 175-700 pmol/L, 07:00-10:00 (lab1028); clinic fee $100-$300/month excl. medication (Alex 2026-10-23).
- NOT stated (unverified): street address, hours, in-person visits, prescribing.
- common.assemble Calgary guard skips this slug; other pages may say Calgary only as 'trt-clinic-calgary' / 'TRT clinic for Calgary and Alberta' / 'in or near Calgary'.

# cal1102 (BUILT LOCALLY 2026-11-02 12:15 MDT, not published) - Calgary striking-distance edit
- Base: live-equal /workspace/srv2/trt-clinic-calgary-enc1102.txt (md5 7b7538b916c8769d8c0a8d1fde81551e; all 599 non-blank lines present in live 2026-11-02 12:14 MDT). Output md5 23112512a024723340973a282861802c, 84,478 bytes, pure ASCII. Old page.html backed up as page.html.bak-cal1102 (it predated the Oct 31 positioning rewrite).
- GSC targets: 'low testosterone clinic calgary' pos 16, 'online trt clinic canada' 14, 'online testosterone clinic' 13, 'online trt clinic' 20. treg CA volume: testosterone clinic calgary 50/mo (CPC $3.38, KD 24); low testosterone clinic calgary, online testosterone clinic canada, online trt clinic canada, natural alternative to trt = no data.
- Answer box lead now: "Odin Health Lab is a low testosterone clinic in Calgary: a natural health clinic offering a natural alternative to TRT ... We do not provide TRT."
- Answer box prose: "We work as an online testosterone clinic with natural protocols instead of TRT: no waiting room and no drive across the city."
- New FAQ #1 "Is there a low testosterone clinic in Calgary?" (visible + FAQPage JSON-LD; 7 == 7).
- Meta/og/twitter description + WebPage/Article JSON-LD description: "Low testosterone clinic in Calgary offering a natural alternative to TRT by video call: low-T assessment, Alberta labs explained, written plan. Free call." (154). Old 'TRT clinic for Calgary and Alberta men, by telehealth' removed. og/twitter image:alt -> natural alternative wording.
- dateModified 2026-11-02; byline "Updated November 2, 2026". Title/H1 unchanged.
- Tidy: removed stray leftover hero markup (</svg>, duplicate "Canada, in CAD / USA, in USD" legend that rendered under the hero, </figure>, extra </div>) and closed the authority-bar </ul>; <main> now tag-balanced. Links, booking triggers, scripts, CSS, motion graphics unchanged.
- GHL: funnel cjRsrbdHz4azEp9PTvzh, page/builder id o0QMraiDMH0ZxioPl1UU (stepId 85303dce-d8a5-455e-8ea2-47fb6009ab83). Verify live: python3 /workspace/cal1102/verify.py

## 2026-11-02 nat1102 (built locally, staged :8780/trt-clinic-calgary-nat1102.txt)
- Base = live cal1102 (srv2/trt-clinic-calgary-cal1102.txt, md5 23112512...). One change: in the #how lead paragraph after "...ready for your next appointment." added "See how this compares with other <a class="text-link" href="https://odinhealthlab.ca/natural-alternative-to-trt" data-cta="how_natalt_link">TRT alternatives</a>." (2nd link to /natural-alternative-to-trt; treg US: 'trt alternatives' 590/mo). Title/desc/FAQ/dateModified unchanged (already 2026-11-02). GHL builder o0QMraiDMH0ZxioPl1UU, step 85303dce-d8a5-455e-8ea2-47fb6009ab83; Custom Code only, SEO panel untouched.

## 2026-11-03 mon1103 (built locally, staged :8780/trt-clinic-calgary-mon1103.txt, md5 ba43ca406bce46d875725f51f8c695d9)
- Base = live nat1102 (srv2/trt-clinic-calgary-nat1102.txt, md5 baa6d536...; all 608 non-blank lines live 2026-11-03 16:02 MDT).
- H1 + Article headline: "A natural alternative to TRT in Calgary: low testosterone support by video call" -> "A natural low testosterone clinic in Calgary: low-T support by video call" (GSC 'low testosterone clinic calgary' pos 17). Short answer still opens with "...a natural health clinic offering a natural alternative to TRT...".
- New FAQ #2 "What monitoring and support do I get with an online low-T program in Canada?" (wording from the nat1102 monitoring FAQ on /natural-alternative-to-trt; DOM 8 == JSON-LD 8). Targets GSC 'best online testosterone therapy with comprehensive monitoring and support in canada' / '...testing and treatment at home in canada'.
- Hero authority bar 1 -> 4 cards (+ Natural protocols, not TRT / A written plan, adjusted as you go / Free first call; markup+icons from /natural-alternative-to-trt).
- dateModified 2026-11-03, byline Updated November 3, 2026. Title, meta description, canonical, links, booking, scripts, CSS, motion unchanged.

## 2026-11-04 ahs1104 (built locally, staged :8780/trt-clinic-calgary-ahs1104.txt, md5 c5f71015e4a427ff9e3f41cbf8038ba1)
- Base = live mon1103 (srv2/trt-clinic-calgary-mon1103.txt, md5 ba43ca40...; all 623 non-blank lines live 2026-11-04 08:4x MDT).
- Idea #10: 2 new FAQs inserted as #3 and #4 (visible + FAQPage JSON-LD; DOM 10 == JSON-LD 10): "Is low testosterone care covered by AHS in Calgary, and how long is the wait?" and "Who do you see for low testosterone in Calgary?". No new links.
- Sources: alberta.ca/ahcip-what-is-covered (AHCIP covers medically required physician services + medically required lab/diagnostic services; physician decides medical necessity); albertahealthservices.ca/info/Page14282.aspx + assets/info/ard/if-ard-faq.pdf (ARD = AHS official referral source, waits are routine estimates, not guaranteed, may change; most services need a healthcare-professional referral; family physician or Health Link 811); ARD profile 1139451 (Calgary endocrinology, Rockyview Health Centre Bldg II: routine within 6 months); ARD 1133084 (Calgary Zone urology FAST central access, estimate Not Available).
- dateModified 2026-11-04, byline Updated November 4, 2026. Title, meta, canonical, H1, links, booking, scripts, CSS, motion unchanged.

## 2026-11-04 hrm1104 (built locally, staged :8780/trt-clinic-calgary-hrm1104.txt, md5 7150a35798f630f1eca715baa7b14966)
- Base = live ahs1104 (ahs1104/trt-clinic-calgary-ahs1104.txt, md5 c5f71015...; all 647 non-blank lines live 2026-11-04 ~12:05 MDT).
- Backlog 11-04 item 2 (Calgary synonym capture): 1 new FAQ inserted as #2 (visible + FAQPage JSON-LD; DOM 11 == JSON-LD 11): "Is there a male hormone clinic in Calgary for hormone testing?" Uses "male hormone clinic in Calgary", "hormone testing clinic", "hormone testing in Calgary". No new links, no H2.
- Facts reused from the existing page only (family doctor orders labs, APL reports them, two early-morning total T tests + free T/SHBG when borderline, we help decide which tests to ask your doctor for). Page has no requisition/home-test wording, so none added.
- treg CA volumes: hormone testing calgary 210, men's health clinic calgary 110, hormone clinic calgary 50, testosterone clinic calgary 50; male hormone clinic calgary / hormone testing clinic calgary / men's hormone therapy near me: no data.
- dateModified/byline already 2026-11-04 (unchanged). Title, meta, canonical, H1, links, ?ref=, booking, scripts, CSS, motion unchanged.
