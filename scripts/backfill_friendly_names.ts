/**
 * Recompute public.events.friendly_name from raw_properties using the same rules as the Edge Function.
 *
 * Usage:
 *   npx deno run --allow-env --allow-net --allow-read --env-file=.env scripts/backfill_friendly_names.ts
 *
 * Requires: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY
 */

import { createClient } from "https://esm.sh/@supabase/supabase-js@2.49.1";
import {
  parseMappingConfig,
  resolveFriendlyName,
} from "../supabase/functions/fetch_mixpanel_events/friendly_name_resolver.ts";
import mapping from "../supabase/functions/fetch_mixpanel_events/mixpanel_event_mapping.json" with {
  type: "json",
};

const PAGE = 500;

const rules = parseMappingConfig(mapping);

function propsObject(raw: unknown): Record<string, unknown> {
  if (raw && typeof raw === "object" && !Array.isArray(raw)) {
    return raw as Record<string, unknown>;
  }
  return {};
}

async function main() {
  const url = Deno.env.get("SUPABASE_URL")?.trim();
  const key = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")?.trim();
  if (!url || !key) {
    console.error("Set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY (e.g. --env-file=.env)");
    Deno.exit(1);
  }

  const admin = createClient(url, key);

  let scanned = 0;
  let updated = 0;
  let unchanged = 0;
  let lastId: string | null = null;

  for (;;) {
    let q = admin
      .from("events")
      .select("id,event_name,url,friendly_name,raw_properties")
      .order("id", { ascending: true })
      .limit(PAGE);
    if (lastId) q = q.gt("id", lastId);

    const { data: rows, error } = await q;
    if (error) {
      console.error(error.message);
      Deno.exit(1);
    }
    if (!rows?.length) break;

    for (const row of rows) {
      scanned++;
      const props = propsObject(row.raw_properties);
      const u = typeof row.url === "string" && row.url.length > 0
        ? row.url
        : undefined;
      const fn = resolveFriendlyName(row.event_name, u, props, rules);
      const prev = row.friendly_name;
      if (prev === fn || (prev == null && fn == null)) {
        unchanged++;
        continue;
      }
      const { error: upErr } = await admin
        .from("events")
        .update({ friendly_name: fn })
        .eq("id", row.id);
      if (upErr) {
        console.error("Update failed", row.id, upErr.message);
        Deno.exit(1);
      }
      updated++;
    }

    lastId = rows[rows.length - 1].id as string;
    console.error(`progress: scanned=${scanned} updated=${updated} …`);
  }

  console.log(
    JSON.stringify(
      {
        ok: true,
        scanned,
        updated,
        unchanged,
        note: "friendly_name recomputed with bundled mixpanel_event_mapping.json + friendly_name_resolver.ts",
      },
      null,
      2,
    ),
  );
}

main().catch((e) => {
  console.error(e);
  Deno.exit(1);
});
