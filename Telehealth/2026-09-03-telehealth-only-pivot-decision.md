---
date: 2026-09-03
description: "Decision record: Odin Labs Calgary is closing its physical clinic location and moving to telehealth-only delivery, expanding the addressable market from Calgary-local to Canada + USA wide. Supersedes the 'local Calgary first' recommendation in local_vs_online_strategy_study.md."
project: Odin Labs Calgary
status: decided
quarter: Q3-2026
tags:
  - marketing
  - strategy
  - decision
  - pivot
  - telehealth
---

# Decision: Telehealth-Only, Canada + USA Wide

## The decision

Odin Labs is **closing the physical clinic location in Calgary** and moving to **telehealth-only delivery**. This is a business-model decision made by the user (owner), recorded here as of 2026-09-03.

**Why:** financial, not strategic preference. Financing for the Calgary physical location dried up — there isn't enough capital to cover rent while the clinic is still building up its client base. This is a forced/necessity-driven pivot, not a conclusion that telehealth is the better long-term model on its own merits. Worth keeping distinct from the marketing-strategy question: the [local_vs_online_strategy_study.md](local_vs_online_strategy_study.md) analysis weighed local vs. USA on trust, compliance, and market-size grounds — none of that reasoning is what triggered this decision. The clinic's underlying economics forced the choice regardless of which channel scored better.

**What this changes:** the practice is no longer geographically bound to Calgary. Marketing, targeting, and offer delivery open up to **Canada and USA wide**. This is the new default going forward for all marketing and growth work in this project, effective immediately.

## Why this matters to marketing/growth specifically

This directly reverses the standing recommendation in [local_vs_online_strategy_study.md](local_vs_online_strategy_study.md) (2026-06-30), which weighed "local Calgary first" against a "USA lab funnel" parallel/future test and concluded local should be the near-term operating foundation (weighted score 493/645 vs. 439/645), specifically because in-person presence was scored as the trust/proof/compliance advantage:

> "A real Calgary location. A practitioner he can meet. Local relevance to energy-sector and executive life... For Owen, the offer should feel like executive metabolic performance medicine, not a generic online lab package."

That advantage no longer exists as a lever — there is no physical location to point to. **This file supersedes that study's operating recommendation, not its analysis.**

**Compliance status per the user (2026-09-03): no unresolved compliance issues.** The user states that based on the actual services Odin Labs provides, everything is within scope — the open compliance questions raised in the June `local_vs_online_strategy_study.md` do not apply to this pivot. Recorded as the user's statement.

## What changes in active campaigns

The Owen quiz funnel (`Calgary-Local/marketing/tests/2026-08-19-owen-two-step-booking-widget.md`, currently running) is built entirely around Calgary-local targeting:

- Ad set name: `[Aug 10] male only - 35-50 - Calgary wide - Lookalike - Aug 19 2 Step Test`
- Geo targeting: `Calgary (+10 mi), Alberta` — hard-locked, no expansion (per the 2026-08-31 targeting lockdown)
- Lookalike seed: `c-exec-calgary` — a Calgary-executive-specific custom audience
- Landing page hero/copy: implicitly assumes local delivery (booking language, "clinician call" — needs a read-through for any Calgary-specific or in-person-implying claims once USA/national copy is drafted)

**None of this has been changed yet.** This file records the decision and its implications; it does not itself modify the ad set, audience, or landing page. Those are separate, deliberate follow-up actions — see Open Items below.

## New funnel launching under this pivot

**2026-09-04 update:** the first new funnel built under the expanded Canada+USA-wide targeting is the **Owen Low-T/Andropause funnel** — a net-new lander (not a change to the existing Calgary-only quiz funnel referenced below), launching Canada+USA-wide from day one rather than inheriting Owen's unmigrated Calgary-only setup. Full project docs: `06_MARKETING_GROWTH/Owen Low-T Funnel/`, starting with [2026-09-04-owen-lowt-funnel-project-outline.md](Owen Low-T Funnel/2026-09-04-owen-lowt-funnel-project-outline.md).

This does not resolve the open items below — the existing Owen quiz funnel (`2026-08-19-owen-two-step-booking-widget.md`) is still running Calgary-only and still needs its own pivot migration decided separately.

## Open items before executing this pivot in the live campaign

- [ ] Decide sequencing: pause/retarget the existing Calgary-only ad set, or run it alongside new Canada/USA-wide targeting as a parallel test (consistent with this project's practice of isolating one changed variable at a time — expanding geo *and* keeping the Calgary lookalike would conflate the two)
- [ ] Decide new audience strategy for the expanded footprint — the `c-exec-calgary` lookalike doesn't make sense as the seed for USA-wide targeting; likely needs a new seed audience or broader targeting logic
- [ ] Landing page / ad copy review for any Calgary-specific or in-person-implying language that no longer matches the offer
- [x] USA compliance questions from `local_vs_online_strategy_study.md` — per the user, 2026-09-03: not applicable / within scope given the actual services provided.
- [ ] Update the ad set's naming convention going forward — "Calgary wide" in the current ad set name will be misleading once geo actually expands
- [ ] Decide whether Emma (the other avatar referenced in the strategy study) is also moving to telehealth-only, or if this decision is Owen-specific

## Source

- Recorded directly from user instruction, 2026-09-03.
- Supersedes the operating recommendation (not the underlying research) in [local_vs_online_strategy_study.md](local_vs_online_strategy_study.md).
- Affects: `Calgary-Local/marketing/tests/2026-08-19-owen-two-step-booking-widget.md` (currently running, Calgary-only) and all future Owen-avatar campaigns.
- Enacted by: `06_MARKETING_GROWTH/Owen Low-T Funnel/` (2026-09-04) — the first funnel built and targeted under this pivot's Canada+USA-wide default.

## Related
- [[2026-09-04-owen-lowt-funnel-project-outline.md]] — new funnel launching under this pivot's expanded geo.
