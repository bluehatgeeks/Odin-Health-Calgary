# Agent notes (Odin Labs / Calgary)

## Marketing test records

Every meaningful marketing test (funnel changes, creative swaps, targeting/placement changes) gets logged as its own file — one hypothesis, one decision rule, one verdict. Full instructions, template, and naming convention:

**[`Calgary-Local/marketing/tests/README.md`](Calgary-Local/marketing/tests/README.md)**

Before starting a new marketing test, or when asked "what did we try before / why did we change X," check `Calgary-Local/marketing/tests/` first — flat folder, filenames sorted newest-last, each file cross-links to what it spawned and what prompted it. (Moved here 2026-09-04: this test log covers the existing Calgary-only Owen quiz funnel. New telehealth-model funnels, e.g. `Telehealth/Owen Low-T Funnel/`, will need their own test-log convention once launched.)

## Mixpanel ↔ Supabase `events`

For the full pipeline—`friendly_name` mapping, session-start RPC, Edge Function behavior, migrations, scripts, deploy, and operational caveats—read:

**[`docs/AGENT_HANDOFF_MIXPANEL_SUPABASE.md`](docs/AGENT_HANDOFF_MIXPANEL_SUPABASE.md)**

**Mixpanel MCP:** [`.cursor/mcp.json`](.cursor/mcp.json) uses **`mcp-remote`** + Mixpanel hosted MCP (OAuth via localhost) — [Mixpanel MCP](https://docs.mixpanel.com/docs/mcp). Open this repo as a folder before connecting; if `cursor://…` OAuth returns 400, avoid native `url` mode and use this config. Details in the handoff doc.

## Secrets and local files

Do **not** stage or commit `.env`, Mixpanel exports under `tmp/`, or `Calgary-Local/00_ADMIN/google_oauth_client_secret.json`. Use `.gitignore` where appropriate.

## Supabase CLI

If `supabase db push` reports migration history drift, see the “Applying the migration” section in the handoff doc; `supabase db query --linked -f <file.sql>` can apply a single migration when push is blocked.
