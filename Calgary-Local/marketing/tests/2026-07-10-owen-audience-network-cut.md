# Excluding Audience Network from placements will improve real (non-junk) session quality and let true creative/funnel performance be measured

**Funnel:** owen-quiz-funnel
**Status:** Concluded — PASS
**Date started:** 2026-07-10
**Date concluded:** 2026-07-11 (verdict clear within 24 hours of clean data)

---

## The change

Ad set placements changed from automatic/expanded to manual: **unchecked Audience Network (native, banner, interstitial + rewarded videos)** and Threads. Left Facebook + Instagram feeds/Stories/Reels enabled.

## Why

Placement breakdown (Jul 8–10) showed Audience Network carrying 64% of impressions at a suspiciously cheap $3.96 CPM, but session-replay review of individual AN-sourced sessions showed clear bot/junk-traffic signatures: rapid multi-link clicks within the same second across unrelated pages (ayurveda, marma-therapy, supplements, privacy — including links only reachable from a hidden disqualification step), sessions idle for 8–12 minutes with a single click, one session opened and abandoned in a backgrounded webview. This also retroactively explained earlier "rage click" events attributed to real user frustration — they were the same bot pattern.

## Decision rule (locked before launch — do not edit after data starts coming in)

*(Reconstructed after the fact — no formal rule written in advance; the change was made same-day as the diagnosis given how clear the replay evidence was.)* Implicit rule discussed: compare CTR/CPC/frequency pre- vs. post-cut on the very next full day of data; expect quality metrics to improve even if raw impression volume and CPM rise.

## Baseline (before this change)

| Metric | Value | Window |
|---|---|---|
| Spend | CA$68.27 | Jul 10 (full day, pre-cut) |
| Impressions | 9,134 | Jul 10 |
| CTR | 0.76% | Jul 10 |
| CPC | CA$0.99 | Jul 10 |
| Frequency | 2.85 | Jul 10 |
| QuizStarts (attributed) | 5 (≥2 confirmed self-tests) | Jul 10 |
| Cost per QuizStart | CA$13.65 (inflated by junk/test traffic) | Jul 10 |

---

## Live log

- **2026-07-10:** Placements changed mid-day (AN + Threads unchecked). Expected immediate re-entry into learning phase.
- **2026-07-11:** First full clean day. CTR nearly tripled to 2.12%, CPC dropped to $0.59, frequency reset to healthy 1.13. 2 QuizStarts at $8.91 each — the first with no known test contamination. Ad set still in learning phase, spend paced below the $40 budget ($17.82) as delivery re-stabilized on the smaller placement set.
- **2026-07-11 (later same day):** One of the two clean QuizStarts completed the full quiz and submitted (traced via Mixpanel `$mp_submit` timestamp match to GHL) — the funnel's **first fully real, non-test lead**, sourced from **Not Aging Walking**, not Normal Range as initially guessed.

---

## Result

| Metric | Jul 10 (pre-cut, contaminated) | Jul 11 (clean) | Change |
|---|---|---|---|
| CTR | 0.76% | 2.12% | +179% |
| CPC | $0.99 | $0.59 | −40% |
| Frequency | 2.85 | 1.13 | normalized |
| Cost per QuizStart | $13.65 | $8.91 | −35% (and now trustworthy) |

**Verdict:** PASS. Every quality metric improved same-day, and — most importantly — this is the point at which the funnel produced its first verifiably real lead. Confirms the AN traffic was inflating cost-per-result with non-converting volume and depressing true CTR by dilution.

**What changes as a result:** AN excluded permanently from this ad set going forward (carried into the Aug 4 relaunch, no change needed there). Establishes **Jul 11 as the "clean data" cutoff** — any campaign analysis referencing dates before this must be flagged as potentially AN-contaminated.

**Next test this spawns:** The clean Jul 11–18 run (documented as prior-period baseline inside `2026-08-04-owen-qualifier-in-quiz.md`) surfaced the next real problem — 6 real leads, 0 ever reached the qualifier step — which became the qualifier-in-quiz test.

---

## Links

- Ad account: Foxboro Medical (943264693502769), ad set `male only - 35-50 - Calgary wide`
- Mixpanel session replays reviewed: via "Odin Health Labs" project, Session Replay tool, filtered to `/owen`
- Next test: `2026-08-04-owen-qualifier-in-quiz.md`
- Prior test: `2026-07-07-owen-first-image-ad-batch.md`
