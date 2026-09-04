# Marketing Test Records — How This Works

This folder is the durable record of every meaningful marketing test run across all funnels (Owen, Emma, and any future funnel). Personal reference only — optimized for fast recall of "what did we try, what happened, why did we change X," not for external readability.

## What counts as a test

**One test = one meaningful, isolated change**, bounded by a start date, a decision rule, and (eventually) a verdict. Not a whole campaign, not a whole day's activity — a single hypothesis you're checking.

Examples from this project: moving the qualifier into the quiz, cutting a bad placement, launching a new creative batch. Each gets its own file.

**Not every change is a "test."** Pure infrastructure/instrumentation work (e.g. fixing a tracking bug, wiring up a new webhook) doesn't have a pass/fail hypothesis — but if later tests depend on it, log it anyway using the same template with `Status: Concluded — DONE` and a note that it's infrastructure, not a hypothesis test. See `2026-07-11-owen-tracking-instrumentation.md` for the pattern.

## Folder structure

**Flat. One folder, one file per test.** No subfolders per funnel.

```
06_MARKETING_GROWTH/tests/
├── README.md              ← this file
├── TEMPLATE.md             ← copy this to start a new test
├── 2026-07-07-owen-first-image-ad-batch.md
├── 2026-07-10-owen-audience-network-cut.md
├── 2026-07-11-owen-tracking-instrumentation.md
└── 2026-08-04-owen-qualifier-in-quiz.md
```

Newest file = newest test, sorted purely by filename. This is deliberate — a flat, date-sorted list is faster to scan than hunting through per-funnel folders, and cross-funnel chronology (what were we doing across ALL funnels in a given week) matters more than grouping by funnel.

## Filename convention

```
YYYY-MM-DD-<funnel>-<short-slug>.md
```

- **Date-first**, always the date the test *started* (not logged/written).
- **Funnel identifier** immediately after the date (`owen-`, `emma-`, etc.) — this is what disambiguates concurrent tests across different funnels running in the same window, since the folder itself no longer groups by funnel.
- **Short slug** describing the change, kebab-case, no need to restate "test."

Example: `2026-08-04-owen-qualifier-in-quiz.md`

If two tests on the **same funnel** start the same day (rare), add a letter suffix: `2026-08-04-owen-qualifier-in-quiz-a.md`, `...-b.md`.

## How to log a new test

1. **Copy `TEMPLATE.md`** to a new file in this folder, named per the convention above.
2. **Fill in before launching, and lock it:**
   - Title (one-line hypothesis)
   - Funnel, status (`Planned`), start date
   - The change (concretely — what's mechanically different, not the goal)
   - Why (what evidence/prior result prompted this — link the prior test file if there is one)
   - **Decision rule** — sample size or time window to reach a verdict, the metric, the pass bar, the fail bar, and what happens in each case. Write this before you have any data. Do not edit it once data starts coming in — if the rule turns out to be wrong, that's a lesson for the next test's rule, not a reason to move the goalposts on this one.
   - Baseline — the last relevant numbers before this change, for comparison.
3. **Launch the change**, set `Status: Running`.
4. **Append to the Live Log** as you check in — short, dated, numbers-plus-one-line-of-read entries. Don't rewrite history here, just add.
5. **At conclusion**, fill in the Result section against the decision rule, write the verdict, set `Status: Concluded — PASS/FAIL/INCONCLUSIVE`, and note what changes as a result and what test (if any) it spawns next.
6. **Cross-link.** Add this test as "Prior test" / "Next test this spawns" on whichever files it connects to, and vice versa. The chain of links is what makes this useful later — six months from now you should be able to land on any one file and walk the reasoning backward or forward without re-deriving it.

## Where self-tests fit

If you personally click through a funnel to test something (as opposed to a real prospect), it will show up in Mixpanel/GHL data. **Tag it** — a distinguishable UTM (e.g. `utm_content=TEST-<slug>`) or a recognizable test email — so it can be filtered out of the real numbers a decision rule is judged against. Self-tests should never silently count toward a sample-size threshold.

## Where this fits in the vault

- **This folder** — the test records themselves (what happened, when, why, verdict).
- **`06_MARKETING_GROWTH/ad production/`** — reusable production playbooks (how to build an image ad batch, how to build a video ad) — process docs, not test records.
- **Memory files** (`~/.claude/.../memory/`) — cross-session facts that persist automatically (e.g. CAPI event architecture). These get pulled into context automatically; test records do not — you (or whoever's working the project) have to go looking for them here.
- **AGENTS.md** (project root) — has a pointer to this README, same pattern as the Mixpanel/Supabase pointer already there.
