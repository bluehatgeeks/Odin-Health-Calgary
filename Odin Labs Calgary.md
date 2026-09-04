---
date: 2026-05-21
description: "Clinic operations hub for Odin Labs Calgary covering setup, clinical protocols, patient experience, growth, operations, and analytics integrations."
project: Odin Labs Calgary
status: active
quarter: Q2-2026
tags:
  - work-note
---

# Odin Labs Calgary

## Context

Clinic operations and growth hub for Odin Labs Calgary, covering business strategy, clinical protocols, patient experience, staffing, marketing, operations, and the Mixpanel to Supabase analytics pipeline.

Project files: `work/active/odin-labs-calgary/`

## Current State

- Source project status: execution phase, **mid-pivot to telehealth-only** (see [[2026-09-03-telehealth-only-pivot-decision.md]] in `Telehealth/`). Physical Calgary clinic is closing; marketing/delivery moving to Canada + USA wide.
- Current phase from `Calgary-Local/00_ADMIN/STATE.json`: procurement execution (pre-pivot state; may be superseded by the telehealth pivot — not yet reconciled).
- Current task: `consumables_sku_drafted`.
- Blocking state: awaiting user approval for procurement execution.
- Roadmap completed: initial research, infrastructure setup, patient segment definition, clinical templates, GHL-to-Sheets-to-Drive pipeline, Drive sync, OAuth recovery, project reorganization, and **2026-09-04 folder reorganization into `Calgary-Local/` / `Telehealth/` / shared root** (see `README.md`).

## Source Map

**Reorganized 2026-09-04** — see `README.md` for the full folder structure and rationale. Quick pointers:

- `README.md` - central project structure and Mixpanel to Supabase runbook.
- `Calgary-Local/00_ADMIN/PROJECT_LOG.md` - roadmap, issue log, and major milestones.
- `Calgary-Local/00_ADMIN/STATE.json` - machine-readable current phase/status (pre-pivot).
- `Calgary-Local/01_BUSINESS_STRATEGY/` - clinic overview, service/pricing, patient segments.
- `Calgary-Local/03_CLINICAL_OPERATIONS/` - Ayurveda/functional templates and consumables (in-person delivery).
- `Calgary-Local/04_PATIENT_EXPERIENCE/` - intake, journey map, and feedback loop (in-person).
- `Calgary-Local/05_STAFFING/` - roles, onboarding, and clinical QA.
- `Calgary-Local/08_OPERATIONS_PLAYBOOK/` - daily clinic operations, continuity, vendor, inventory, emergency, and maintenance docs.
- `Telehealth/` - the pivot decision and new telehealth-model funnels (Owen Low-T Funnel).
- `06_MARKETING_GROWTH/` - shared growth strategy, avatar definitions, and the landers codebase (serves both models).
- `07_TECH_STACK/` and `supabase/` - GHL/Sheets/Mixpanel/Supabase integrations (shared infrastructure).

## Workstreams

- Current source README describes the project as being in execution phase for the Calgary clinic setup, now mid-pivot to telehealth-only.
- Analytics work includes a working Mixpanel Raw Export API import into Supabase with deduplication on Mixpanel `$insert_id`.
- Procurement is centered on `Calgary-Local/03_CLINICAL_OPERATIONS/consumables/final_sku_list.md`; all listed P0/P1 items are still pending — **status uncertain given the telehealth pivot; may no longer apply if the physical clinic build-out is halted.**
- Growth execution is centered on `06_MARKETING_GROWTH/growth_strategy_package.md` and `06_MARKETING_GROWTH/implementation_checklist.md`.
- Active funnel build: Owen Low-T/Andropause funnel, see [[2026-09-04-owen-lowt-funnel-project-outline.md]] (in `Telehealth/Owen Low-T Funnel/`) — new lander forked from the proven Owen quiz/booking mechanic, free consult at launch, Canada+USA-wide targeting.
- Analytics handoff is documented in `docs/AGENT_HANDOFF_MIXPANEL_SUPABASE.md`: friendly names, session-start marking, RPC migration, Edge Function deployment, and Mixpanel MCP setup.

## Ready-To-Work

- For procurement: review and approve `final_sku_list.md`, then convert pending P0/P1 rows into actual order/vendor tasks — **confirm this is still relevant given the telehealth pivot before proceeding.**
- For growth: start with website metadata, GBP optimization, local citations, review loop, LinkedIn lead form, GHL nurture sequence, UTM tracking, and dashboard sync.
- For analytics: before changing code, confirm Supabase migration/function status, Edge secrets, `.env` hygiene, and whether the target is exploratory Mixpanel MCP analysis or warehouse SQL.
- For operations: use the operations playbook docs (`Calgary-Local/08_OPERATIONS_PLAYBOOK/`) as working checklists rather than creating new scattered notes.

## Risks / Gotchas

- `git status` shows untracked `.env`, `Calgary-Local/00_ADMIN/google_oauth_client_secret.json`, media/lander assets, and `tmp/`; do not commit secrets or export dumps.
- `Calgary-Local/00_ADMIN/PROJECT_LOG.md` contains historical OAuth/client details; treat project admin files as sensitive.
- There is exactly **one** `.git` repo, at the vault root (`work/active/odin-labs-calgary/`), tracking `github.com/bluehatgeeks/Odin-Health-Calgary`. (Corrects an earlier note here claiming a separate nested repo under the landers folder — verified 2026-09-04, no such nested repo exists.)
- The landers website codebase (`06_MARKETING_GROWTH/Odin Labs Landers/`) was deliberately **not** moved during the 2026-09-04 reorg — it's referenced by live, ad-spending campaigns via jsDelivr CDN URLs that are root-path-relative (`cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/<path>`). Moving it requires updating every CDN reference in lockstep and should be its own planned, verified step.

## Action Items
- [ ] Get user approval for the final consumables SKU list.
- [ ] Turn approved procurement items into order/vendor execution tasks.
- [ ] Run the growth implementation checklist in priority order, starting with conversion tracking and live CTA QA.
- [ ] Audit `.gitignore` coverage for `.env`, OAuth credentials, generated media/temp exports, and local system files.

## Related
- [[Index]]
- [[North Star]]
- [[Memories]]
- [[Gotchas]]
