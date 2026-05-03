/**
 * Prefix friendly_name with "[session start] " for session boundary events
 * (see public.mark_session_start_friendly_names in migrations).
 *
 * Usage:
 *   SESSION_GAP_MINUTES=30 npx deno run --allow-env --allow-net --env-file=.env \
 *     scripts/mark_session_starts.ts
 */

import { createClient } from "https://esm.sh/@supabase/supabase-js@2.49.1";

const gap = Math.max(
  1,
  parseInt(Deno.env.get("SESSION_GAP_MINUTES") ?? "30", 10) || 30,
);

const url = Deno.env.get("SUPABASE_URL")?.trim();
const key = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")?.trim();
if (!url || !key) {
  console.error("Need SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY");
  Deno.exit(1);
}

const supabase = createClient(url, key);
const { data, error } = await supabase.rpc("mark_session_start_friendly_names", {
  session_gap_minutes: gap,
});

if (error) {
  console.error(error.message);
  console.error(
    "If the function is missing, apply supabase/migrations/20260209120000_mark_session_start_friendly_names.sql (db push or SQL editor).",
  );
  Deno.exit(1);
}

console.log(
  JSON.stringify(
    {
      ok: true,
      session_gap_minutes: gap,
      session_start_rows_updated: data,
    },
    null,
    2,
  ),
);
