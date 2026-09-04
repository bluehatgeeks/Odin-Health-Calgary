# Adding 5 image ad concepts to the Owen ad set will find a creative angle that outperforms the existing 2 videos and unblocks learning-phase exit

**Funnel:** owen-quiz-funnel
**Status:** Concluded — INCONCLUSIVE (superseded by AN-cut finding, not by creative performance)
**Date started:** 2026-07-07
**Date concluded:** 2026-07-10 (effectively decided by the Audience Network test, see below)

---

## The change

Published 5 new static image ads to the existing Owen ad set (`male only - 35-50 - Calgary wide`), alongside the 2 videos already running (Not Aging Walking, Voice Over Music). Concepts, each targeting a distinct emotional angle per the Andromeda creative-diversity principle:

- **3pm Wall** — symptom recognition ("You used to own 3pm")
- **Normal Range** — medical-dismissal/cynicism ("Normal. Still exhausted.")
- **You Remember** — nostalgia ("Sharp. Strong. Recovered.")
- **The Pattern** — mechanism/curiosity (3-system numbered list)
- **Doctor's Note** — frustration ("Everything looks normal.")

Photoreal bases generated via nanobanana, all typography composited programmatically (never AI-rendered text), real Odin Lab SVG logo, brand-tinted to match odinhealthlab.ca's green/lime system. Full production process documented in `06_MARKETING_GROWTH/ad production/quiz image ads playbook.md`.

Also increased ad set daily budget CA$20 → CA$40 same week, and standardized CTA buttons across ads (was mixed Learn More / See Details).

## Why

Only 2 creatives were live (below Meta's 5-creative-per-ad-set recommendation), both videos, no format diversity. Day-1 data (Jul 6) showed CTR 1.53% but 0 tracked leads — insufficient creative variation to know if that was a targeting problem or a creative problem.

## Decision rule (locked before launch — do not edit after data starts coming in)

*(Reconstructed after the fact — this test predates the formal test-record system, so no rule was written down in advance. Approximate rule discussed in-conversation: run ~72 hours untouched post-publish to let the algorithm redistribute delivery across creatives, then compare CTR/CPC per concept.)*

- **Sample size:** ~72 hours of stable delivery post-publish
- **Metric:** CTR and cost-per-QuizStart per creative concept
- **On pass (clear winner emerges):** concentrate budget/iterate on the winning angle
- **On fail (no separation):** investigate non-creative causes (targeting, tracking, page)

## Baseline (before this change)

| Metric | Value | Window |
|---|---|---|
| Spend | CA$19.70 | Jul 6 (1 day) |
| Impressions | 1,704 | Jul 6 |
| CTR | 1.53% | Jul 6 |
| Creatives live | 2 (both video) | Jul 6 |
| Tracked leads | 0 | Jul 6 |

---

## Live log

- **2026-07-07:** All 5 image ads published. 4 entered PENDING_REVIEW, 1 (3pm Image) approved same day.
- **2026-07-08:** Delivery underspending vs. new $40 budget — attributed to (a) budget increase mid-pacing-cycle, (b) 4/5 ads still in review, (c) ad set optimizing toward a conversion event (ViewContent) with zero historical volume, causing cautious bidding.
- **2026-07-09:** CTR degraded to 0.96%, CPC up to $1.99 — algorithm still redistributing across the enlarged creative set.
- **2026-07-10:** Placement breakdown pulled (Jul 8–10 cumulative): Facebook 2,912 impr / $18.14 CPM / 0 attributed QuizStarts; Instagram 1,141 impr / $24.70 CPM / 2 QuizStarts; **Audience Network 7,038 impr (64% of volume) / $3.96 CPM / 3 QuizStarts**. Session-replay review of AN-sourced sessions showed junk traffic (one session: 8 min idle, 1 click; another: single click then 12 min idle in a backgrounded webview). This diagnosis superseded the original creative-comparison question — see the AN-cut test for what happened next.

---

## Result

Never reached a clean creative-vs-creative verdict on its own terms — the Audience Network discovery (see `2026-07-10-owen-audience-network-cut.md`) revealed that ~64% of the impressions this test was measuring against were junk traffic, which invalidated any CTR/CPC comparison made before the cut. By the time clean data existed (Jul 11 onward), the question had shifted from "which image concept wins" to "does the funnel produce real leads at all" (see the Jul 13–Aug 3 run and the qualifier-in-quiz test that followed it).

**What did survive as usable signal, read with the caveat that pre-cut data is contaminated:**
- **Not Aging Walking** (pre-existing video) was the only creative to produce verified real leads across the whole Jul 6–Aug 3 period (5 of 6 identified leads).
- **Normal Range** (image) produced the single other real lead and the best CPC in one clean-traffic window (Jul 11: $2.40 cost-per-QuizStart on a small sample).
- 3pm Image, Doctor's Note, The Pattern: zero real leads across the full period. Cut from the Aug 4 relaunch.

**Verdict:** INCONCLUSIVE by its own decision rule (no clean 72-hour read was ever obtained), but downstream evidence effectively answered the underlying question — video (Walking) and one image concept (Normal Range) are the only creatives worth keeping; the other 3 images did not work for this avatar/message combination.

**What changes as a result:** Format diversity alone wasn't the lever — Not Aging Walking's UGC talking-head style, not the medium, appears to be what the avatar responds to. This directly shaped the 2026-08-04 test's creative refresh (2 new videos in the same talking-head format, only 1 image kept).

**Next test this spawns:** `2026-07-10-owen-audience-network-cut.md`, and downstream, `2026-08-04-owen-qualifier-in-quiz.md`

---

## Links

- Ad creative: `Calgary-Local/marketing/Odin Labs Calgary Meta Ads/quiz - *.png` (moved here in the 2026-09-04 reorg)
- Production process: `06_MARKETING_GROWTH/ad production/quiz image ads playbook.md`
- Ad account: Foxboro Medical (943264693502769), campaign `[Jul 6 - 26] Owen Quiz Test`
- Next test: `2026-07-10-owen-audience-network-cut.md`
