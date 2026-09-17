# Owen Low-T VSL — Beat-Based B-Roll Composition System

**Status:** Approved (pending per-section implementation approval)
**Date:** 2026-09-17
**Context:** Full from-scratch rebuild of the Owen Low-T Funnel VSL graphics
system. Supersedes the image-based `FullFrameInfographic` +
`RegionHighlight` architecture entirely. No component, generated
infographic image, or measured coordinate from the prior system is
reused.

## Background

The prior system rendered each diagram as a single flattened,
Nanobanana-generated image, with a `RegionHighlight` component
punching dimmed/bright regions over it via pixel-measured percentage
coordinates. Three rounds of targeted fixes (saturated-color dimming,
pixel-based repositioning, ellipse clip-paths for circular badges)
each solved a real technical bug, but a full re-render was still
rejected as looking like "an inexperienced editor['s]" work: callouts
too small, highlighting not aware of element boundaries, inconsistent
spacing, abrupt motion.

The root cause was architectural, not a bug: highlighting a *copy of a
flat image* can never be pixel-perfect against the *original* image's
element boundaries, no matter how precisely regions are measured, and
flattened images cannot carry per-element motion (scale, glow,
independent animation timing). The fix is to stop flattening diagrams
into images at all.

## Core Concept: The Beat

A **Beat** is the atomic unit of the new system: a single,
self-contained, fully-produced animated segment — a stat card, an icon
row, a kinetic text callout, or a multi-node diagram — presented B-roll
style while the speaker's video is fully hidden (full cutaway; audio
continues uninterrupted). When the beat ends, the video cuts back to
the speaker.

Every Beat is driven by one shared choreography engine (`<Beat>`) so
that entrance, hold, and exit motion is visually identical everywhere
in the video — the presenting instrument is invariant; only its
content changes. This directly addresses the "inconsistent
spacing/abrupt motion/looks unprofessional" feedback: professional
motion graphics repeat a small number of movement idioms
deliberately, they don't invent new timing per element.

### `<Beat>` (choreography engine)

```
<Beat startFrame={f} durationInFrames={d}>
  {children}
</Beat>
```

- Wraps arbitrary content in a fixed entrance/exit contract: scale
  ~0.9 → 1.0, fade in, settle (spring), mirrored on exit.
- Content authors never hand-write their own enter/exit timing or
  easing — only *what* appears, not *how* it appears.
- Renders full-screen (`AbsoluteFill`), replacing the speaker video
  for its duration.

### `<FocusStep>` (internal choreography)

For Beats containing multiple named elements (diagrams), a small
ordered list drives which element is "active" over time within the
single Beat — no separate cutaway per named step:

```
type FocusStep = { at: number /* absolute VSL seconds */; target: string /* node id */ };
```

At any given frame, the node whose `id` matches the most recent
`FocusStep.at <= currentTime` is "active": scaled up (~1.08–1.18x) and
glowing/brightened. All other nodes are "inactive": scaled down
(~0.88–0.96x) and desaturated via `grayscale(1) brightness(0.32)` — the
same CSS filter technique already validated in this project — applied
directly to the real coded element, not to a copied image layer.

This eliminates the entire prior bug class (region-to-image
misalignment, square corners on circular badges, clip-path bleed at
extreme scale ratios) by construction: there is no separate image to
align a highlight against. The "highlighted element" and the "diagram
element" are the same DOM/SVG node.

## Content Primitives

All content within a Beat is coded (React/SVG), not a flattened
generated image, with one narrow exception (icon glyphs, below).

### `<BeatBackground>`

A shared coded SVG `<pattern>` producing the approved dark
forest-green (`#0e2410`) background with a subtle repeating dot-grid
texture. Implemented once, tuned once, used behind every Beat. No
image asset, no regeneration dependency, scales crisply at any
resolution.

### `<NodeGraph>`

Renders diagram content (the aromatase loop, cortisol fork, crossed
signals, mission control, SHBG taxi, etc.) from a small data
description:

```
type Node = { id: string; icon: IconName; label: string; position: { xPct: number; yPct: number } };
type Edge = { from: string; to: string; style?: "arrow" | "line" };

type NodeGraphSpec = { nodes: Node[]; edges: Edge[] };
```

- **Nodes** render as icon + label pairs, positioned by authored
  percentage coordinates (no pixel-measurement or crop-verification
  step — positions are declared directly, since there's no background
  image to align against).
- **Edges** render as coded SVG `<path>` connectors between node
  positions, with a `drawOn` stroke-dasharray animation that can
  trigger in sync with the `FocusStep` that introduces that
  connection.
- `FocusStep.target` refers to a `Node.id` directly — no ellipse/rect
  shape guessing, no region coordinates at all.

### Icons

The only remaining generated-image assets in the system are the
approved transparent-alpha icon glyphs (Brain, Factory, Molecule,
Taxi, Pituitary, Lab report, generated so far). The icon library grows
on-demand: as each section's Beats are designed, any new icon a
diagram needs is generated through the same pipeline (Nanobanana
`generate_icon` on a solid magenta key background → ffmpeg chromakey
→ verified real alpha against the project's actual background color)
and approved before that section's Beat content is considered done.

No upfront full-library batch generation — icon needs are discovered
and resolved section by section, alongside Beat design.

## Section Structure

Each `SectionNN` becomes a sequence of Beats interleaved with speaker
cutback gaps (where the speaker's video plays normally, no Beat
active). Example, Section 3 (Cause 1 — Aromatase):

```
[speaker] → [Beat: checklist reprise] → [speaker]
  → [Beat: aromatase NodeGraph, 5 FocusSteps: Fat → Aromatase → More Fat → Bars → Brain]
  → [speaker] → [Beat: "calories in ≠ calories out" kinetic text] → [speaker]
```

Multi-step mechanisms (aromatase loop, cortisol fork, crossed
signals, mission control) are **one continuous Beat** with internal
`FocusStep`s, not a series of separate cutaways — these are narrated
as one unfolding mechanism, and repeated cutaway/cutback would feel
choppier than the single-image version being replaced, not smoother.

## Build & Approval Process

Per the brainstorming skill's architectural path and the user's
explicit constraint ("let me approve every section so that we do not
waste time"):

1. Build the shared engine first: `<Beat>`, `<FocusStep>` logic,
   `<BeatBackground>`, `<NodeGraph>`. Get this reviewed/approved as a
   working foundation (e.g. one throwaway test diagram) before any
   real section is touched.
2. Then, section by section (Section 1 → 12): design that section's
   Beat breakdown, generate any new icons it needs, build it, present
   for approval. No section's production code is written before that
   section's design is approved.
3. No component, image asset, or measured coordinate from the prior
   `FullFrameInfographic`/`RegionHighlight`/`SevenCauseChecklist`-era
   system is reused. Old section files and graphics remain on disk
   until the new system fully replaces them, then are deleted.

## Explicitly Out of Scope

- Picture-in-picture / speaker-visible-during-beat layouts (full
  cutaway only, per approved decision).
- Per-beat-type custom choreography variants (one shared engine only).
- Upfront full-icon-library generation (grows on-demand).
- Reworking the underlying HeyGen speaker footage, VSL script, or
  cut-sheet timing — this spec covers graphics presentation only.
