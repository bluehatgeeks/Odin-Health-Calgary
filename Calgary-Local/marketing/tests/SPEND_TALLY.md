# Owen Campaign — Spend Tally by Test

Source: Meta Ads Manager, campaign `[Jul 6 - 26] Owen Quiz Test` (Foxboro Medical, account 943264693502769), pulled day-by-day via API. Pulled 2026-08-06.

This is a derived/reference file, not a test record — it exists to answer "how much did each test actually cost" without re-deriving it from Ads Manager each time. Update by re-running the day-by-day pull and re-mapping to whatever test windows exist at the time.

## Day-by-day raw spend (campaign-level, all creatives combined)

| Date | Spend (CAD) |
|---|---|
| Jul 6 | $19.70 |
| Jul 7 | $24.99 |
| Jul 8 | $5.01 |
| Jul 9 | $45.66 |
| Jul 10 | $68.30 |
| Jul 11 | $50.33 |
| Jul 12 | $41.11 |
| Jul 13 | $39.23 |
| Jul 14 | $41.24 |
| Jul 15 | $42.21 |
| Jul 16 | $33.27 |
| Jul 17 | $43.62 |
| Jul 18 | $19.51 |
| Jul 19 – Aug 3 | $0.00 (campaign paused) |
| Aug 4 | $46.56 |
| Aug 5 | $67.38 |
| Aug 6 (partial day at pull time) | $18.91 |

**Total spend, Jul 6 – Aug 6:** $607.63 CAD

## Spend by test

| Test | File | Window | Spend (CAD) | Note |
|---|---|---|---|---|
| Pre-test baseline | — | Jul 6 | $19.70 | 2 videos only, before first image batch |
| First image ad batch | [2026-07-07-owen-first-image-ad-batch.md](2026-07-07-owen-first-image-ad-batch.md) | Jul 7–9 | $75.66 | Superseded by AN finding before reaching its own verdict |
| Audience Network cut | [2026-07-10-owen-audience-network-cut.md](2026-07-10-owen-audience-network-cut.md) | Jul 10–11 | $118.63 | Jul 10 = contaminated (AN still live most of the day), Jul 11 = first clean day |
| Tracking instrumentation | [2026-07-11-owen-tracking-instrumentation.md](2026-07-11-owen-tracking-instrumentation.md) | Jul 11 | $0 attributable | Infra shipped same day as above — no separate spend, rides on the AN-cut window |
| Clean run (unlogged as its own test — this is the run whose result justified the qualifier-in-quiz test) | — | Jul 12–18 | $260.19 | 6 real leads, 0 reached qualifier step — see "Why" section of the qualifier test |
| *(campaign paused)* | — | Jul 19 – Aug 3 | $0 | No test running |
| Qualifier-in-quiz + creative refresh | [2026-08-04-owen-qualifier-in-quiz.md](2026-08-04-owen-qualifier-in-quiz.md) | Aug 4 – ongoing | $132.85 *(running total, through Aug 6 partial)* | Live test, spend will keep climbing — re-pull before using this number in the Result section |

## Reconciliation note

The "$272" baseline figure quoted inside `2026-08-04-owen-qualifier-in-quiz.md`'s Baseline table (window "Jul 13 – Jul 18") is Jul 13–18 only ($260.19 by this pull — close enough to be the same figure, small variance likely from Meta's rounding/currency display at time of writing vs. this re-pull). It does **not** include Jul 6–12 ($213.10) or the paused period. Total actual spend before the qualifier test's Aug 4 launch, across everything: **$474.79** (Jul 6 – Aug 3).

## How to update this file

1. Re-run `ads_get_ad_entities` at `level: campaign`, `fields: ["amount_spent"]`, `time_increment: 1`, over the full date range needed.
2. Paste the new daily rows into the raw table above (append, don't overwrite history).
3. Re-map to test windows using each test file's `Date started` / `Date concluded`.
4. If a test is still `Running`, label its spend figure as a running total with the pull date, since it'll be stale the moment you save the file.
