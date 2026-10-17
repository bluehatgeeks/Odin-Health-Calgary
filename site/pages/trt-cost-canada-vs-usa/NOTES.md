# /trt-cost-canada-vs-usa: answer page 13 (BUILT LOCALLY, not published)

- Title (60): TRT Cost in Canada vs USA: Labs and Drugs | Odin Health Labs
- Description (151): What TRT costs in Canada vs the USA: lab tests, provincial and insurance coverage, injection, gel and pellet prices, and monitoring. Sourced, Oct 2026.
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
