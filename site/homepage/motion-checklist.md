# Motion checklist (use for every new page)
1. Every page needs real motion graphics (inline SVG / CSS), not text alone: one hero visual, animated icons, a scroll-driven element.
2. Ask first: does it explain, give feedback, or prevent a jarring change? If not, don't animate it.
3. Animate `transform` and `opacity`; SVG stroke draw-on only on small paths; no `transition: all`, no heavy filters or blur.
4. Curves: `cubic-bezier(0.23,1,0.32,1)` for entrances; UI 150-300ms, press 100-160ms, marketing up to ~600ms; never `ease-in`, never `scale(0)` (start at .9+).
5. Stagger 30-80ms; reveal once with IntersectionObserver; no scroll-jacking, one passive rAF scroll listener at most.
6. Buttons/cards: hover lift only inside `(hover:hover) and (pointer:fine)`; `:active` scale(.97).
7. Loops are decorative and slow (6-12s); pause them when off-screen (IntersectionObserver) (browsers already throttle hidden tabs).
8. Default CSS = final state. Gate motion behind `prefers-reduced-motion: no-preference`; content must be fully visible with JS off.
9. Reserve space (width/height or aspect-ratio) for every animated graphic: CLS must stay 0. Never animate the H1/LCP element's opacity.
10. No statistics or efficacy claims in animated graphics; label illustrations; test at 1280 and 390, console clean, screenshots saved to `shots/`.
