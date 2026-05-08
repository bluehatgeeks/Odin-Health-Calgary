# Agent handoff: Mixpanel → Supabase `events` pipeline

This document summarizes work on importing Mixpanel exports into Supabase, deriving **`friendly_name`**, and marking **session boundaries** with a **`[session start] `** prefix. Use it as context for future automation, debugging, or schema changes.

---

## Goals (what we built)

1. **Human-readable labels** — Map Mixpanel event names + URLs + `properties` to **`friendly_name`** on insert (Edge Function).
2. **Session markers** — After data is in `public.events`, label the first row of each “session” per **`distinct_id`** by prefixing **`friendly_name`** with **`[session start] `**.
3. **Session definition** — A new session starts when:
   - it is the **first event** we have for that `distinct_id`, or  
   - **`event_time`** is more than **`session_gap_minutes`** (default **30**) after the **previous** event for the same `distinct_id` (ordered by `event_time`, then `id`).
4. **Automatic marking on sync** — The importer Edge Function calls the database RPC **once after** successful writes (when `written > 0`).

---

## Key files

| Area | Path |
|------|------|
| Importer (Mixpanel export → `events`) | `supabase/functions/fetch_mixpanel_events/index.ts` |
| Friendly-name rules engine | `supabase/functions/fetch_mixpanel_events/friendly_name_resolver.ts` |
| Ordered mapping rules (JSON) | `supabase/functions/fetch_mixpanel_events/mixpanel_event_mapping.json` |
| Resolver unit tests (Deno) | `supabase/functions/fetch_mixpanel_events/friendly_name_resolver_test.ts` |
| Session-start RPC migration | `supabase/migrations/20260209120000_mark_session_start_friendly_names.sql` |
| Optional: run RPC from CLI (Deno + `.env`) | `scripts/mark_session_starts.ts` |
| Recompute `friendly_name` from stored columns | `scripts/backfill_friendly_names.ts` |
| Local / export analysis helpers | `scripts/local_mixpanel_friendly_preview.ts`, `scripts/analyze_mixpanel_export.mjs` |
| Audits for unmapped paths / clicks | `scripts/list_unmapped_odin_paths.ts`, `scripts/list_unmatched_click_urls.ts` |
| Sample JSONL fixture | `fixtures/mixpanel_sample.jsonl` |
| Cursor: Mixpanel hosted MCP | `.cursor/mcp.json` |

---

## Database: `mark_session_start_friendly_names`

- **Function:** `public.mark_session_start_friendly_names(session_gap_minutes integer default 30) returns integer`
- **Permissions:** `GRANT EXECUTE … TO service_role` (so the Edge Function can call it).
- **Behavior (idempotent):**
  1. Strip leading **`[session start] `** from all non-null `friendly_name` values.
  2. Recompute session boundaries with `lag(event_time)` over `partition by distinct_id order by event_time asc, id asc`.
  3. For boundary rows, set `friendly_name` to `'[session start] ' || coalesce(trimmed_name, '(unmapped)')`.
- **Return value:** Count of rows updated by the final `UPDATE` (boundary rows), not necessarily “only new imports.”

**Applying the migration**

- `supabase db push --linked` may fail if **remote migration history** does not match the local `supabase/migrations/` folder. In that case, apply the SQL with **`supabase db query --linked -f supabase/migrations/20260209120000_mark_session_start_friendly_names.sql`** (or paste into the SQL editor).
- After history is repaired (`supabase migration repair`, `supabase db pull`, etc.), `db push` should work again.

---

## Edge Function: `fetch_mixpanel_events`

- **Role:** Fetches Mixpanel Export API JSONL for a computed date range, maps each line to a row, **upserts** on `mixpanel_insert_id` where present, otherwise **inserts**.
- **`friendly_name`:** Set via **`resolveFriendlyName(event_name, url, properties, rules)`** using `mixpanel_event_mapping.json`.
- **After successful batches:** If **`written > 0`**, calls **`admin.rpc('mark_session_start_friendly_names', { session_gap_minutes })`**.
- **`SESSION_GAP_MINUTES`:** Optional Edge secret / env; default **30**. Parsed with the same `Math.max(1, …)` pattern as in code.
- **Response:** JSON includes **`sessionStart`**: `{ gapMinutes, skipped, rowsUpdated, error }`. Import can succeed while `sessionStart.error` is set if the RPC fails—investigate logs.

**Deploy (CLI)**

```bash
npx supabase functions deploy fetch_mixpanel_events
```

**Mixpanel auth (secrets)** — Typical vars: `MIXPANEL_PROJECT_TOKEN` + `MIXPANEL_API_SECRET`, or service account vars + numeric `MIXPANEL_PROJECT_ID`. See comments in `index.ts` for exact combinations.

**Supabase runtime** — `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` are expected in the hosted Edge environment.

---

## Operational notes

1. **Full-table recompute:** Each RPC run rescans **`public.events`** for ordering. Acceptable for moderate size; for very large tables consider batching, scheduling off-peak, or a narrower strategy.
2. **No-op sync:** If **`written === 0`**, the Edge Function **skips** the RPC to avoid an unnecessary full pass.
3. **Out-of-order events:** Late-arriving rows with older `event_time` can change which row is the session start until the next RPC run.
4. **Manual RPC (SQL):**  
   `select public.mark_session_start_friendly_names(30);`
5. **Git hygiene:** Do **not** commit `.env`, `tmp/` exports, or `00_ADMIN/google_oauth_client_secret.json`. Prefer `.gitignore` updates if these paths keep appearing.

---

## Git reference (this workstream)

Commit **`e4c6e0b`** (message: `feat(mixpanel): run session-start RPC after import`) includes:

- `supabase/functions/fetch_mixpanel_events/index.ts` — post-import RPC
- `supabase/migrations/20260209120000_mark_session_start_friendly_names.sql`
- `scripts/mark_session_starts.ts`

Earlier work (mapping, resolver, audits, backfill, tests, fixture) may live in other commits on `main`. This handoff doc describes the **current intended behavior** of the pipeline, not every historical diff.

---

## Quick checklist for new agents

- [ ] Migration applied on the target Supabase project (function exists: `select proname from pg_proc where proname = 'mark_session_start_friendly_names';`)
- [ ] Edge Function deployed after changing `index.ts` or bundled assets
- [ ] Secrets set: Mixpanel + `SESSION_GAP_MINUTES` if not using default 30
- [ ] After mapping changes: run **`backfill_friendly_names`** then optional manual **`mark_session_start_friendly_names`** if you need consistency without a full import
- [ ] **Mixpanel MCP:** Org admin enables MCP in Mixpanel; in Cursor, OAuth the **mixpanel** server (see `.cursor/mcp.json` and section below)

---

## Mixpanel MCP (Cursor and other AI clients)

Mixpanel hosts an MCP server so assistants can run insights, funnels, list projects/events, manage dashboards/Lexicon, etc. Official reference: [Mixpanel MCP docs](https://docs.mixpanel.com/docs/mcp).

**This repo** ships [`.cursor/mcp.json`](../.cursor/mcp.json) using **Mixpanel’s documented Cursor setup**: `mcp-remote` → US endpoint (pinned package version):

```json
"mixpanel": {
  "command": "npx",
  "args": ["-y", "mcp-remote@0.1.38", "https://mcp.mixpanel.com/mcp"]
}
```

For **EU** or **IN**, replace the URL with `https://mcp-eu.mixpanel.com/mcp` or `https://mcp-in.mixpanel.com/mcp`.

**Why not Cursor’s native `"url": …` OAuth?** Cursor uses `cursor://anysphere.cursor-mcp/oauth/callback`. Some users see **400 Bad Request** on that flow (Mixpanel or Cursor edge cases). **`mcp-remote` uses a localhost redirect** (HTTP), which matches [Mixpanel’s MCP docs](https://docs.mixpanel.com/docs/mcp) and is usually reliable.

**Before you click Connect:** Open this **repo as a folder** in Cursor — not an empty / no‑folder window. OAuth `state` tied to **`empty-window`** has been associated with failed callbacks.

**Org setup:** A Mixpanel org admin must enable MCP under **Settings → Org → Overview** (may take up to ~15 minutes).

**Troubleshooting**

- **“Missing scope”** (Mixpanel): `rm -rf ~/.mcp-auth`, restart Cursor, reconnect ([Mixpanel troubleshooting](https://docs.mixpanel.com/docs/mcp#troubleshooting)).
- **Stuck or stale auth:** same `rm -rf ~/.mcp-auth`, then reconnect.
- **Debug:** `npx -y mcp-remote@0.1.38 https://mcp.mixpanel.com/mcp --debug` (logs under `~/.mcp-auth/`).
- **Optional native `url` mode:** You can try `"url": "https://mcp.mixpanel.com/mcp"` per [Cursor MCP](https://cursor.com/docs/context/mcp) only if **`mcp-remote` is removed** to avoid duplicate servers — use with a **real workspace folder** and latest Cursor if you experiment.

**Logs in Cursor:** **View → Output → MCP Logs**.

**Compliance / security:** Mixpanel states MCP is not HIPAA-eligible; connecting sends Mixpanel data to your AI provider. See [Mixpanel MCP security](https://docs.mixpanel.com/docs/mcp#security-considerations).

This MCP complements—but does not replace—the **Supabase `events` warehouse**: use Mixpanel MCP for exploratory analytics and Lexicon; use Supabase for SQL, joins with other tables, and your `friendly_name` / session-start pipeline.

---

## Related dashboard

Project ref from a successful CLI deploy (verify in your own `supabase link` output if needed): functions live under Supabase Dashboard → **Edge Functions** for the linked project.
