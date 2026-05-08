# Agent notes (Odin Labs / Calgary)

## Mixpanel ↔ Supabase `events`

For the full pipeline—`friendly_name` mapping, session-start RPC, Edge Function behavior, migrations, scripts, deploy, and operational caveats—read:

**[`docs/AGENT_HANDOFF_MIXPANEL_SUPABASE.md`](docs/AGENT_HANDOFF_MIXPANEL_SUPABASE.md)**

**Mixpanel MCP:** [`.cursor/mcp.json`](.cursor/mcp.json) uses Cursor **Streamable HTTP** (`url`) + OAuth — [Mixpanel MCP](https://docs.mixpanel.com/docs/mcp), [Cursor MCP](https://cursor.com/docs/context/mcp). Org-admin enablement required. EU/IN URLs are in the handoff doc.

## Secrets and local files

Do **not** stage or commit `.env`, Mixpanel exports under `tmp/`, or `00_ADMIN/google_oauth_client_secret.json`. Use `.gitignore` where appropriate.

## Supabase CLI

If `supabase db push` reports migration history drift, see the “Applying the migration” section in the handoff doc; `supabase db query --linked -f <file.sql>` can apply a single migration when push is blocked.
