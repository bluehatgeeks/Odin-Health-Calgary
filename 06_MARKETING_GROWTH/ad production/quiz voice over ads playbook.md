# NOT-JUST-AGING — Ad Production Playbook

How this ad was built end-to-end: branding source, tech stack, structure, motion system, B-roll sourcing, and audio mix. Use this as the template for the next Odin Lab video ad.

---

## 1. Tech stack

- **Remotion** (React-based video framework) — every frame is a pure function of frame number, no timeline editor
- Project location: `/Users/alexandertretjakov/Downloads/openhuman/remotion`
- Composition file: `src/NotJustAging.tsx`
- Registered in `src/Root.tsx` as composition id `"NOT-JUST-AGING"`, 1080×1080, 30fps
- Render command:
  ```bash
  cd /Users/alexandertretjakov/Downloads/openhuman/remotion
  npx remotion render src/index.ts NOT-JUST-AGING "<output path>.mp4"
  ```
- Always `npx tsc --noEmit` before rendering — catches prop/type errors before burning render time.

---

## 2. Brand extraction (do this first, every time)

We didn't invent the visual style — we extracted it directly from the live site so the ad matches the lander pixel-for-pixel in tone.

**Process:**
1. Open the lander (`https://odinhealthlab.ca/`) via browser automation (kimi-webbridge or similar).
2. Pull computed styles via JS injection:
   ```js
   getComputedStyle(document.body).backgroundColor
   getComputedStyle(element).fontFamily / fontSize / fontWeight
   ```
3. Record the exact hex/rgb values — don't eyeball colors from a screenshot, read them from the DOM.

**What we found and used:**

| Token | Value | Source |
|---|---|---|
| Background | `#1a3a1a` (deep forest green) | `body` background-color |
| Accent | `#c4ff49` (electric lime) | CTA buttons, headline highlight spans |
| Dark panel | `#142e14` | secondary section backgrounds |
| Near-black panel | `#0e2410` | used for high-contrast scenes (Scene 5, Scene 8 Beat A) |
| Headline font | System sans-serif, **weight 900** | `-apple-system, "system-ui", "Segoe UI", Roboto, sans-serif` — NOT a serif, NOT Helvetica Neue. Confirmed via `getComputedStyle(h1).fontWeight === "900"` |
| Body text | White / `rgba(255,255,255,0.55–0.88)` for secondary | |

**Mistake to avoid:** the first draft used `'Helvetica Neue', Arial, serif` and assumed a display serif font because it "looked premium." Always verify against the live site's actual computed font, not assumption.

**Logo:** Use the real brand SVG, not a text wordmark. Get the exported SVG (Illustrator export, `viewBox="0 0 640 175"`), inline its `<path>` data directly into a reusable `OdinLogo` component so it renders crisp at any size without an external asset dependency:
```tsx
const OdinLogo: React.FC<{ fill?: string; width?: number }> = ({ fill = "#fff", width = 260 }) => {
  const height = width * (175 / 640);
  return (
    <svg width={width} height={height} viewBox="0 0 640 175">
      {LOGO_PATHS.map((d, i) => <path key={i} d={d} fill={fill} />)}
    </svg>
  );
};
```

---

## 3. Layout system

### Footer band (logo + divider, never collides with anything)

Early draft put decorative corner brackets in every scene AND a logo near the bottom-left corner — they visually collided. **Fix: removed corner decoration entirely.** One `Footer` component owns the bottom-of-frame real estate:

```tsx
const Footer: React.FC<{ frame: number; startF: number }> = ({ frame, startF }) => (
  <div style={{ position: "absolute", zIndex: 10, left: PAD_X, right: PAD_X, bottom: 64,
    display: "flex", flexDirection: "column", gap: 22 }}>
    <LimeDivider frame={frame} startF={startF} />   {/* animated width bar */}
    <div style={{ opacity: fadeIn(frame, startF + 6, 18) }}>
      <OdinLogo width={150} fill="rgba(255,255,255,0.4)" />
    </div>
  </div>
);
```
Every scene calls `<Footer frame={frame} startF={someTimecode} />` once. Nothing else is allowed to render in that bottom band.

### Padding constant
`const PAD_X = 84;` — every scene's horizontal padding, every divider width calc (`1080 - PAD_X*2`), every footer inset. One constant, used everywhere, so margins always line up across scene cuts.

### Density rule (learned the hard way)
First draft of Scene 4 ("the systems") crammed 3 boxes side-by-side at 1080px width — text wrapped mid-word ("Hormonal Floor" broke against the box edge). **Fix:** never use cramped multi-column boxes for text-heavy content. Use a vertical list instead:
```tsx
const SystemRow = ({ n, label, sub }) => (
  <div style={{ display: "flex", alignItems: "center", gap: 28, padding: "18px 0", borderBottom: "1px solid rgba(255,255,255,0.08)" }}>
    <div>{n}</div>            {/* "01", "02", "03" */}
    <div>{label}</div>        {/* big, white, 900 weight */}
    <div>{sub}</div>          {/* smaller, dim */}
  </div>
);
```
Same fix applied to the CTA scene: it used to stack headline + 3 stat cards + 3 lines of body copy + button + logo all at once (overloaded, overlapping). **Fix: split into two hard-cut beats** (see §5).

---

## 4. Motion system

### Helpers (write these once, reuse everywhere)
```tsx
const ci = (frame, [a,b], [from,to]) => interpolate(frame, [a,b], [from,to], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
const fadeIn  = (f, start, dur=14) => ci(f, [start, start+dur], [0, 1]);
const blurIn  = (f, start, dur=14) => ci(f, [start, start+dur], [10, 0]);
const slideUp = (f, start, dur=18, dist=46) => dist * (1 - ci(f, [start, start+dur], [0,1]));

// Combined entrance — blur + rise + fade together. Looks far less "basic CSS transition"
// than a plain fade alone.
const enter = (frame, startF, dur=16, dist=40) => ({
  opacity: fadeIn(frame, startF, dur),
  filter: `blur(${blurIn(frame, startF, dur)}px)`,
  transform: `translateY(${slideUp(frame, startF, dur, dist)}px)`,
});

// Spring with slight overshoot for "pop-in" headline moments
const popIn = (frame, startF, fps, stiff=200, damp=14) =>
  spring({ frame: frame - startF, fps, config: { stiffness: stiff, damping: damp } });
```
Apply `enter()` to every headline/body text block via spread: `style={{ ...enter(frame, s(1.2), 15, 30), fontSize: 60, ... }}`.

### Timing convention
```tsx
const FPS = 30;
const s = (sec: number) => Math.round(sec * FPS);   // seconds → frames, always round
```
Every animation start time is written in **seconds**, converted via `s()`. Never hardcode raw frame numbers — it makes re-timing against a VO track unreadable.

### Sequence-relative frame math
Every scene component receives `frame` already relative to its own start (`frame - s(CUT.sN_in)`), so internal animation code never needs to know what scene number it is or when the overall video started. This is what made it possible to prepend a cold open later without touching any scene's internal timing — see §6.

---

## 5. Scene structure (the 8-beat script)

Built against a pre-recorded VO track (`not-just-aging-vo.mp3`) with hand-verified timestamps. **The golden rule: get the VO timestamps right via Whisper or manual scrubbing BEFORE writing scene code** — every `s(X.X)` constant in the file is a direct transcript timestamp, not a guess.

| Scene | Window | VO beat | Visual idea |
|---|---|---|---|
| 1 | 0.0–4.0s | "You're not 25 anymore. You know that." | Giant lime "25" centered, white headline above/below |
| 2 | 4.0–8.6s | "But there's a difference between aging and breaking down early." | Word-by-word reveal, "aging" isolated huge |
| 3 | 8.6–26.4s | Symptom list → "That's not aging. That's a system running below potential." | Vertical bullet list with animated indicator bars, last one red/highlighted |
| 4 | 26.4–39.0s | The 3 systems (stress axis, hormonal floor, metabolic) → "they decline in a pattern" | Numbered vertical list (see §3 density rule) |
| 5 | 39.0–42.0s | "And that pattern is addressable." | Near-black panel, single huge lime word, pulse rings |
| 6 | 42.0–53.8s | "Not with pharma / TRT... with root-cause approach... removes it." | Cross-out list → reveal of the approach |
| 7 | 53.8–63.0s | Assessment offer, 2 checkmarked promises | Headline + animated checkmarks |
| 8 | 63.0–70.4s | Stats (3 min / 0 generic / 1 clear picture) + CTA | **Two hard-cut beats**, not one crowded stack (see below) |

### Scene 8 two-beat fix
Original Scene 8 put headline + 3 stat cards + 3 lines of body + CTA button + logo all in one composition simultaneously — visually overloaded, text overlapped controls in review. Fixed by splitting on a hard cut inside the same `Sequence`:
```tsx
const Scene8 = ({ frame }) => {
  const CUT_AT = s(3.6);
  if (frame < CUT_AT) {
    return <BeatA />;   // headline + stat cards only, dark panel
  }
  return <BeatB frame={frame - CUT_AT} />;  // body copy + CTA + logo only, green panel
};
```
Never put more than ~3 visual elements on screen simultaneously. If a scene's copy needs more, split it into sequential beats with a hard cut, not a denser single frame.

---

## 6. Cold open — flash montage hook

**Problem:** the ad originally started cold on flat green with no motion — weak first-impression for a feed scroll.

**Fix:** prepended a ~1.3s silent flash montage before any VO/text, built as 4 quick B-roll cuts with hard lime flashes between them:

```tsx
const COLD_OPEN_CLIPS = [
  { src: "broll/symptoms-tired.mp4", word: "Tired.", startFrom: 60 },
  { src: "broll/systems-gym.mp4",   word: "Grinding.", startFrom: 90 },
  { src: "broll/assessment-lab.mp4", word: "Testing.", startFrom: 30 },
  { src: "broll/cta-running.mp4",   word: "Nothing changes.", startFrom: 45 },
];
const CUT_LEN = 8;     // frames per clip (~0.27s)
const FLASH_LEN = 2;   // frames of hard lime flash between cuts
export const COLD_OPEN_LEN = COLD_OPEN_CLIPS.length * (CUT_LEN + FLASH_LEN); // 40 frames
```
Each clip: **hard cut in at full opacity** (not a fade-in — a fade-in on a 6-8 frame clip means the clip is invisible for its first frame, which was an actual bug we hit and fixed), fast snap-zoom (1.22→1.08 scale), heavy desaturation/contrast filter so it doesn't look like raw stock footage, and a punchy all-caps single-word caption bottom-left.

**Wiring without breaking VO sync:** rather than shifting every scene's timestamp later (which would desync the hand-tuned VO timestamps), wrap the *entire* existing composition in one outer `Sequence from={COLD_OPEN_LEN}`, and put the cold open in its own `Sequence from={0} durationInFrames={COLD_OPEN_LEN}` before it. Every inner scene's frame math stays `frame - COLD_OPEN_LEN - s(CUT.sN_in)` — only one offset term added, the original per-scene timing untouched.

Composition's total `durationInFrames` must then be extended by the same constant — export `COLD_OPEN_LEN` from the scene file and import it into `Root.tsx` rather than hardcoding the number twice (we hit a drift bug doing this manually once).

---

## 7. B-roll: sourcing, tinting, integration

### Where we got it
**Pexels** (pexels.com/videos) — free for commercial use, no attribution required. Searched by scene intent, not generic terms:
- "tired man office" → symptoms/fatigue scenes
- "gym training slow motion" → systems/effort scenes
- "blood test lab" → assessment/diagnostic scenes
- "man running sunrise" → CTA/outcome scene

Confirmed each clip on its Pexels page (creator name, license) before downloading. Clicking the page's "Free download" button triggers a direct browser download — no resolution picker appears for most clips, it just downloads at the default master quality.

### File organization
```
remotion/public/broll/
  symptoms-tired.mp4
  systems-gym.mp4
  assessment-lab.mp4
  cta-running.mp4
```
Renamed by scene intent immediately on copy, not left as Pexels' numeric IDs — makes the component code self-documenting (`staticFile("broll/symptoms-tired.mp4")` reads correctly without cross-referencing a spreadsheet).

### Tinting recipe (so real footage doesn't fight the brand colors)
```tsx
const BrollBg = ({ src, tint = C.bg, dim = 0.78, sceneFrame }) => {
  const scale = 1.04 + ci(sceneFrame, [0, 600], [0, 0.05]); // slow creep-in, never static
  return (
    <AbsoluteFill style={{ overflow: "hidden" }}>
      <OffthreadVideo src={src} muted style={{
        width: "100%", height: "100%", objectFit: "cover",
        transform: `scale(${scale})`,
        filter: "saturate(0.55) brightness(0.75) contrast(1.05)",   // desaturate + darken first
      }} />
      <AbsoluteFill style={{ background: tint, opacity: dim, mixBlendMode: "multiply" }} />  {/* brand color wash */}
      <AbsoluteFill style={{ background: `linear-gradient(180deg, ${C.bgDeep}99 0%, transparent 35%, transparent 65%, ${C.bgDeep}cc 100%)` }} />  {/* top/bottom scrim for text contrast */}
    </AbsoluteFill>
  );
};
```
Three layers, in order: (1) desaturate/darken the source video itself via CSS filter, (2) multiply-blend the brand background color over it at ~78% opacity so the green dominates, (3) a vertical gradient scrim so text at top/bottom of frame always has contrast regardless of what's happening in the footage underneath. Skipping any one of these three layers either looks like raw stock footage (no brand tint) or has unreadable text (no scrim).

`OffthreadVideo` (not `<Video>`) — required for reliable frame-accurate rendering in Remotion's render pipeline.

---

## 8. Music bed and audio mix

### Sourcing
**Pixabay Music** (pixabay.com/music) — free for commercial use. Searched "cinematic tension corporate" for a track that wouldn't compete with VO. Picked **"Epic Moving Emotion" by RoyaltyFreeMusicStudio** (tags: Corporate, Epic, Cinematic, 2:24 long — longer than the ad, just gets trimmed by Remotion's Sequence duration).

### Volume envelope — the part that actually matters
A flat background volume is wrong for this format: loud enough to matter during the silent cold open, but needs to duck hard the instant VO starts, with small swells at emotional beats where there's room.

```tsx
const musicVolume = (frame) => interpolate(frame,
  [
    0,                                    // cold open: louder, no VO yet
    COLD_OPEN_LEN - 8,                    // start ducking before VO begins
    COLD_OPEN_LEN + s(CUT.s1_in) + 10,    // settled low under VO
    COLD_OPEN_LEN + s(CUT.s5_in),         // swell into "Addressable." payoff
    COLD_OPEN_LEN + s(CUT.s5_in) + 20,
    COLD_OPEN_LEN + s(CUT.s6_in),         // back down for approach/assessment
    COLD_OPEN_LEN + s(CUT.s8_in),         // swell for CTA
    COLD_OPEN_LEN + s(CUT.s8_in) + 20,
    COLD_OPEN_LEN + s(CUT.end),
  ],
  [0.32, 0.10, 0.06, 0.06, 0.10, 0.06, 0.06, 0.11, 0.0],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
);

<Audio src={staticFile("not-just-aging-music.mp3")} volume={musicVolume} />
```
**Tuning note:** first pass at 0.55/0.22/0.13 still read too loud against VO on playback — halved every value (0.32/0.10/0.06) on user feedback. If a future track sounds hot/dense in isolation, expect to need to go even lower than feels intuitive — verify with `ffmpeg -af volumedetect` comparing `mean_volume` during a VO-only window vs. cold-open-only window, don't just eyeball the interpolate() numbers.

### Two separate Audio tracks
VO (`not-just-aging-vo.mp3`) stays at default volume 1.0, scoped inside the post-cold-open `Sequence` (so it starts exactly when the cold open ends). Music spans the *entire* composition at root level with its own envelope. Never try to duck the VO — always duck the music around the fixed VO.

---

## 9. Verification workflow (no browser preview — this is a render pipeline)

1. `npx tsc --noEmit` after every edit — catches prop mismatches instantly, before spending render time.
2. `npx remotion render src/index.ts NOT-JUST-AGING <output>.mp4` — full render, ~30-90s for a 70s 1080×1080 clip depending on B-roll complexity.
3. Extract spot-check frames with `ffmpeg -ss <time> -i <file> -frames:v 1 <out>.png` and `Read` them — this is how every layout bug in this doc was actually caught (logo collision, cramped boxes, invisible cold-open frame-zero, etc). Don't trust the code read-through alone; always pull real frames.
4. Check audio balance with `ffmpeg -ss <t> -t <dur> -af volumedetect -f null -` and compare `mean_volume` between a VO section and a music-only section.

---

## 10. Reusable checklist for the next ad

- [ ] Pull brand colors/fonts from the live site's computed styles, not from a screenshot guess
- [ ] Inline the real logo SVG, never a text wordmark substitute
- [ ] One `Footer` component owns the bottom band; no competing decoration (corner marks, etc.)
- [ ] One `PAD_X` constant drives every margin
- [ ] Never more than ~3 elements on screen at once — split into hard-cut beats if copy demands more
- [ ] Get VO timestamps exact before writing scene timing — every `s(X.X)` is a transcript timestamp
- [ ] Cold open: 3-5 quick B-roll flashes + one-word captions, hard cuts (not fades) on entry, wrap as a prepended `Sequence` so existing VO-synced timing never shifts
- [ ] B-roll tint recipe: desaturate/darken filter → brand-color multiply wash → gradient scrim — all three, always
- [ ] Music: separate track from VO, envelope that ducks hard under VO and swells only at clear emotional beats, verify loudness with `volumedetect` not by ear alone
- [ ] Verify via rendered frame screenshots, not code review alone
