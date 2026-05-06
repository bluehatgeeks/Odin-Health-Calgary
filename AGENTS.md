# Agent notes (Odin Labs / Calgary)

## Mixpanel ↔ Supabase `events`

For the full pipeline—`friendly_name` mapping, session-start RPC, Edge Function behavior, migrations, scripts, deploy, and operational caveats—read:

**[`docs/AGENT_HANDOFF_MIXPANEL_SUPABASE.md`](docs/AGENT_HANDOFF_MIXPANEL_SUPABASE.md)**

**Mixpanel MCP:** [`.cursor/mcp.json`](.cursor/mcp.json) registers Mixpanel’s hosted MCP ([docs](https://docs.mixpanel.com/docs/mcp)). Requires org-admin enablement in Mixpanel and OAuth in Cursor. EU/IN endpoints are documented in the handoff file.

## Secrets and local files

Do **not** stage or commit `.env`, Mixpanel exports under `tmp/`, or `00_ADMIN/google_oauth_client_secret.json`. Use `.gitignore` where appropriate.

## Supabase CLI

If `supabase db push` reports migration history drift, see the “Applying the migration” section in the handoff doc; `supabase db query --linked -f <file.sql>` can apply a single migration when push is blocked.
