# Lighthouse audit — Odin Health Labs live site (backlog item 8)

Run: 2026-10-15 ~9:07–9:12 PM MDT, Lighthouse 13.5.0, headless Chrome, mobile default (simulated 4G + 4x CPU), categories perf/a11y/bp/seo, cache-buster ?lhcb=. Two runs in parallel, so perf numbers carry some CPU-contention noise. Raw JSON: /workspace/lighthouse/live/*.json

## Live scores (before any change)

| page | perf | a11y | bp | seo | FCP | LCP | CLS | TBT | SI |
|---|---|---|---|---|---|---|---|---|---|
| ayurveda | 81 | 96 | 77 | 100 | 3.4 s | 3.8 s | 0 | 50 ms | 3.4 s |
| functional-health | 82 | 96 | 77 | 100 | 3.5 s | 3.6 s | 0 | 100 ms | 3.5 s |
| health-coaching | 83 | 96 | 77 | 100 | 3.4 s | 3.5 s | 0 | 80 ms | 3.4 s |
| home | 74 | 96 | 77 | 100 | 3.8 s | 4.3 s | 0 | 160 ms | 3.8 s |
| low-testosterone-age-or-weight | 83 | 96 | 77 | 100 | 3.4 s | 3.5 s | 0 | 80 ms | 3.4 s |
| low-testosterone-labs-to-ask-for | 74 | 96 | 77 | 100 | 4.1 s | 4.5 s | 0 | 90 ms | 4.1 s |
| peptides-canada-usa | 83 | 96 | 77 | 100 | 3.4 s | 3.6 s | 0 | 80 ms | 3.4 s |
| privacy | 81 | 100 | 77 | 100 | 3.4 s | 3.9 s | 0 | 90 ms | 3.4 s |
| shift | 71 | 96 | 77 | 100 | 4.3 s | 4.8 s | 0 | 100 ms | 4.3 s |
| supplements | 72 | 96 | 77 | 100 | 4.3 s | 4.6 s | 0 | 80 ms | 4.5 s |
| trt-and-fertility | 80 | 96 | 77 | 100 | 3.5 s | 3.9 s | 0 | 50 ms | 3.5 s |
| trt-or-fix-causes-first | 75 | 96 | 77 | 100 | 4.0 s | 4.3 s | 0 | 140 ms | 4.0 s |
| weight-loss-drugs-and-testosterone | 80 | 96 | 77 | 100 | 3.6 s | 3.9 s | 0 | 90 ms | 3.6 s |

Averages: perf ~78 (71–83), a11y 96 (privacy 100), best-practices 77 everywhere, SEO 100 everywhere. CLS 0 on every page. LCP element = the hero H1 (text), so LCP ≈ FCP; LCP 3.5–4.8 s is driven by when the page first paints, not by an image.

## Top failing audits and who owns them

| Audit | Pages | Detail | Owner |
|---|---|---|---|
| color-contrast | 12/13 (all but privacy) | "How it works" timeline steps not yet scrolled to were dimmed to opacity 0.4 → step label 2.84:1, h3 3.26:1, body 3.59:1, links 3.26:1 (need 4.5:1) | **(a) ours — FIXED locally** |
| forced-reflow-insight | 13/13 | Our reveal script read `getBoundingClientRect()` per `.reveal` element right after writing classes (layout thrash), ~230–316 ms total reflow on live | **(a) ours — FIXED locally** (reads batched before writes; one unavoidable first layout remains) |
| unsized-images | 13/13 | Header logo `<img alt="OdinLab Logo" style="height:40px;width:auto">` has no width/height attributes | (a)-shared: lives in the GitHub nav component `odinnav.html` (loaded on every page incl. [Paid] pages). No CLS because the header is fixed. Not changed; optional fix = add `width="…" height="40"` in odinnav.html |
| aria-hidden-focus (local runs only) | – | `#mega-mobile-sub` aria-hidden="true" contains focusable links | (a)-shared: `odinnav.html` nav component. Passes on live. Optional fix = `inert`/tabindex=-1 on hidden submenu links |
| unused-javascript (166 KiB) | 13/13 | `stcdn.leadconnectorhq.com/_preview/BOAEhAhK.js` (267 KB, 64% unused) | (b) HighLevel platform |
| FCP/LCP/Speed Index/TTI | 13/13 | Chain: HTML → HL BOAEhAhK.js → ~20 HL chunks + attribution/stats calls; supplements also had a 1.09 s server response (one-off) | (b) mostly HighLevel shell; see notes below |
| mainthread-work-breakdown (2.1–2.4 s) | 12/13 | Style & Layout ~1.5 s, "Other" ~1.3 s, script ~0.5 s | mixed: our SVG/CSS motion + large inline pages, HL JS |
| third-party-cookies / inspector-issues (BP 77) | 13/13 | `__cf_bm` Cloudflare cookies on images.leadconnectorhq.com and HL favicon | (b) HighLevel CDN |
| bf-cache | 13/13 | "Internal error / Not actionable" | (b) platform/Chrome |
| cache-insight | 13/13 | Cloudflare insights beacon 1-day TTL; jsdelivr CSS 7-day TTL (~1 KB savings) | (b) / negligible |

### Notes on category (a) items not changed (documented only)
- Nav + footer are fetched at runtime from `raw.githubusercontent.com/.../odinnav.html` and `odinfooter.html` with `cache: 'no-store'` (base_loader.html). That is an uncached cross-origin round trip on every page view. Moving them to jsDelivr (cacheable) or inlining them would help, but the loader is shared with the [Paid] pages and changes the nav source. Worth a separate decision.
- Hero H1 is the LCP element. It currently fades/slides in via `.hero-in` (560 ms + stagger). Lighthouse counts LCP when the text paints, so the entrance animation adds a little render delay (~0.9 s "element render delay" on home). Could start the H1 at opacity 1 and only animate transform, but that changes the hero motion, so left alone.
- Pages are 85–141 KB of inline HTML/CSS/SVG each, pasted into the HL custom-code block. Fine for now; trimming SVG would be a larger refactor.

## Fixes made locally (category a)
1. **Timeline contrast**: inactive steps now dim to opacity **0.7** instead of 0.4 (worst-case contrast now ≥5.6:1). The scroll-driven timeline motion is unchanged: line fill, moving head, dot switching on, 10 px slide-in and opacity transition.
   - `/workspace/pages/_shared/base_head.html` (all `.pg` pages)
   - `/workspace/pages/functional-health/page.template.part1.html` (`.fh`)
   - `/workspace/homepage/home.template.html` (`.home-v2`)
2. **Forced reflow**: the reveal init now reads all `.reveal` element positions first (one layout), then adds `js-reveal`/`is-in` classes and starts the IntersectionObserver. Same behaviour: above-the-fold items show at once and the rest reveal on scroll.
   - `/workspace/pages/_shared/base_tail.html`, `/workspace/pages/functional-health/page.template.part3.html`, `/workspace/homepage/home.template.html`

Rebuilt (each differs from the previous build by exactly these 2 hunks, 11 diff lines):
/workspace/homepage/home.html (also /workspace/pages/_home/page.html, a symlink), /workspace/pages/{ayurveda,functional-health,health-coaching,low-testosterone-age-or-weight,low-testosterone-labs-to-ask-for,peptides-canada-usa,privacy,shift,supplements,trt-and-fertility,trt-or-fix-causes-first,weight-loss-drugs-and-testosterone}/page.html

Backups: /workspace/backups-perf/pre-perf-20261015-2112.tgz (all sources + built pages) plus copies of the 5 edited source files.

## Local before/after (served via serve_utf8.py, no HL shell, so perf is higher than live)
| page | before perf/a11y | after perf/a11y | reflow ms before→after | color-contrast |
|---|---|---|---|---|
| home | 97 / 92 | 97 / 96 | 322 → 303 | fail → pass |
| shift | 97 / 92 | 98 / 96 | 438 → 231 | fail → pass |
| trt-or-fix-causes-first | 97 / 92 | 97 / 96 | 286 → 271 | fail → pass |
(Locally, a11y stays at 96 only because of the nav component's aria-hidden-focus, which passes on live.) Expected live result after publishing: a11y 96 → 100 on 12 pages; perf change small.

## Tests (after rebuild)
- test-visual (all 12 pages + home t.js): 0 console errors/pageerrors/failed requests, CLS 0, no horizontal overflow, 0 loops running offscreen, reduced-motion OK, at 390 and 1280.
- test-tracking: all CTA-click tracking PASS on every page. The remaining FAILs were already there and are identical when the old builds are re-tested: functional-health seo-meta/`track` name checks, privacy FAQ/JSON-LD checks, and the `/owen-lowt` check on answer pages. These are harness mismatches, not regressions.
- home-tracking: 21/21 PASS (title-length note only).

## Needs publishing in HighLevel
Re-paste custom code for all 13 non-paid pages (home + 12) from the rebuilt files above. No [Paid] page was touched. Then mirror the 5 source files and 13 built pages to GitHub (bluehatgeeks/Odin-Health-Calgary).
