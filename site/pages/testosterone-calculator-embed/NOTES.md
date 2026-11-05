# /testosterone-calculator-embed (emb1105, 2026-11-05)

Lightweight iframe target for the ISSAM / Vermeulen free testosterone calculator.
Built for backlinks: men's-health coaches, gyms and bloggers paste one iframe.

## SEO choice
- Indexable (`index, follow`).
- **Canonical points to /testosterone-calculator** so ranking signals consolidate on the full calculator page (converter + free T + ranges + FAQ). The embed URL stays publicly 200 and usable as `iframe src`.
- Title: Embeddable ISSAM Free Testosterone Calculator
- In-body credit: "Calculator by Odin Health Lab" -> https://odinhealthlab.ca/testosterone-calculator

## What it is / is not
- Free-T tool only (same calc-core.js math as the main page). No unit-converter block, no nav/footer chrome, no booking CTAs, no /owen-lowt.
- Brand singular "Odin Health Lab". Does not prescribe or provide TRT; natural health clinic / natural alternative OK.
- Pure ASCII. Subtle SVG pulse respects prefers-reduced-motion.

## Size
- page.html 15328 bytes.

## Framing note
- Our HTML does not send X-Frame-Options. Live odinhealthlab.ca responses (checked 2026-11-05) also had no X-Frame-Options / CSP frame-ancestors. If GHL later adds DENY, the embed breaks for third-party sites - recheck headers after publish.

## Visual (2026-11-05 emb1105)
- Chrome headless: 720 and 390 widths, no horizontal overflow, credit visible, #1a3a1a bg.
- prefers-reduced-motion: pulse-ring and fc-bar glow animationName=none.
- Suggested iframe height 780 (390-wide stacked layout ~766px content).
- test-calc.js via shared CORE: 19/19; embed CORE ISSAM example PASS.
