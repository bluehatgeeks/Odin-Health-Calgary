import { createClient } from "https://esm.sh/@supabase/supabase-js@2.49.1";
import mixpanelEventMapping from "./mixpanel_event_mapping.json" with {
  type: "json",
};
import {
  parseMappingConfig,
  resolveFriendlyName,
} from "./friendly_name_resolver.ts";

type MixpanelEvent = {
  event: string;
  properties?: Record<string, unknown> & {
    time?: number;
    distinct_id?: string;
    $insert_id?: string;
    $current_url?: string;
  };
};

const friendlyNameRules = parseMappingConfig(mixpanelEventMapping);

function utcYmd(ms: number): string {
  return new Date(ms).toISOString().slice(0, 10);
}

/** Inclusive Mixpanel Export API date bounds (UTC yyyy-mm-dd) for [startSec, endSec]. */
function exportDateRangeInclusive(
  startSec: number,
  endSec: number,
): { from_date: string; to_date: string } {
  const a = utcYmd(startSec * 1000);
  const b = utcYmd(endSec * 1000);
  return a <= b ? { from_date: a, to_date: b } : { from_date: b, to_date: a };
}

function parseJsonl(text: string): MixpanelEvent[] {
  const out: MixpanelEvent[] = [];
  for (const line of text.split("\n")) {
    const t = line.trim();
    if (!t) continue;
    try {
      out.push(JSON.parse(t) as MixpanelEvent);
    } catch {
      // skip malformed line
    }
  }
  return out;
}

function mixpanelAuthAndUrl(
  from_date: string,
  to_date: string,
):
  | { ok: true; url: string; authorization: string; mode: string }
  | { ok: false; message: string } {
  const projectToken = Deno.env.get("MIXPANEL_PROJECT_TOKEN");
  const apiSecret = Deno.env.get("MIXPANEL_API_SECRET");
  const svcUser = Deno.env.get("MIXPANEL_SERVICE_USERNAME");
  const svcSecret = Deno.env.get("MIXPANEL_SERVICE_SECRET");
  const projectIdRaw = Deno.env.get("MIXPANEL_PROJECT_ID")?.trim() ?? "";
  const numericProjectId = /^\d+$/.test(projectIdRaw) ? projectIdRaw : null;

  const exportUrl = new URL("https://data.mixpanel.com/api/2.0/export");
  exportUrl.searchParams.set("from_date", from_date);
  exportUrl.searchParams.set("to_date", to_date);

  // Legacy (project token + API secret) — no project_id. Basic auth is secret:token (not token:secret).
  if (projectToken && apiSecret) {
    exportUrl.searchParams.delete("project_id");
    return {
      ok: true,
      url: exportUrl.toString(),
      authorization: `Basic ${btoa(`${apiSecret}:${projectToken}`)}`,
      mode: "project_token",
    };
  }

  // Service account: needs numeric Project ID (Mixpanel → Project Settings).
  if (svcUser && svcSecret) {
    if (numericProjectId) {
      exportUrl.searchParams.set("project_id", numericProjectId);
      return {
        ok: true,
        url: exportUrl.toString(),
        authorization: `Basic ${btoa(`${svcUser}:${svcSecret}`)}`,
        mode: "service_account",
      };
    }
    if (projectIdRaw) {
      return {
        ok: false,
        message:
          "MIXPANEL_PROJECT_ID must be the numeric Project ID from Mixpanel (Project Settings or URL). " +
          "A long hex string is not valid. Remove bad MIXPANEL_PROJECT_ID and set the number, or unset " +
          "MIXPANEL_SERVICE_* and use MIXPANEL_PROJECT_TOKEN + MIXPANEL_API_SECRET only.",
      };
    }
    return {
      ok: false,
      message:
        "Service account is configured but MIXPANEL_PROJECT_ID is missing. Add the numeric Project ID, or use legacy MIXPANEL_PROJECT_TOKEN + MIXPANEL_API_SECRET instead.",
    };
  }

  return {
    ok: false,
    message:
      "Set MIXPANEL_PROJECT_TOKEN + MIXPANEL_API_SECRET, or " +
      "MIXPANEL_SERVICE_USERNAME + MIXPANEL_SERVICE_SECRET + numeric MIXPANEL_PROJECT_ID. " +
      "Sync with: supabase secrets set ...",
  };
}

Deno.serve(async (req) => {
  if (req.method !== "POST" && req.method !== "GET") {
    return new Response("Method Not Allowed", { status: 405 });
  }

  const supabaseUrl = Deno.env.get("SUPABASE_URL");
  const serviceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");

  if (!supabaseUrl || !serviceKey) {
    return new Response(
      JSON.stringify({
        error: "Missing SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY (expected in hosted Edge runtime).",
      }),
      { status: 500, headers: { "Content-Type": "application/json" } },
    );
  }

  const admin = createClient(supabaseUrl, serviceKey);

  const overlapSec = Math.max(
    60,
    parseInt(Deno.env.get("MIXPANEL_SYNC_OVERLAP_SECONDS") ?? "3600", 10) || 3600,
  );
  const lookbackDays = Math.min(
    365,
    Math.max(
      1,
      parseInt(Deno.env.get("MIXPANEL_SYNC_LOOKBACK_DAYS") ?? "30", 10) || 30,
    ),
  );

  const endSec = Math.floor(Date.now() / 1000);

  const { data: newestRow } = await admin
    .from("events")
    .select("raw_properties, event_time")
    .order("event_time", { ascending: false })
    .limit(1)
    .maybeSingle();

  let watermarkSec = 0;
  if (
    newestRow?.raw_properties && typeof newestRow.raw_properties === "object"
  ) {
    const t = (newestRow.raw_properties as Record<string, unknown>).time;
    if (typeof t === "number" && Number.isFinite(t)) watermarkSec = t;
  }
  if (watermarkSec <= 0 && newestRow?.event_time) {
    const ms = Date.parse(newestRow.event_time as string);
    if (Number.isFinite(ms)) watermarkSec = Math.floor(ms / 1000);
  }

  let syncStartSec: number;
  let emptyTable = false;
  if (watermarkSec <= 0) {
    emptyTable = true;
    syncStartSec = endSec - lookbackDays * 86400;
  } else {
    syncStartSec = Math.max(0, watermarkSec - overlapSec);
  }

  const { from_date, to_date } = exportDateRangeInclusive(syncStartSec, endSec);

  const auth = mixpanelAuthAndUrl(from_date, to_date);
  if (!auth.ok) {
    return new Response(JSON.stringify({ error: auth.message }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }

  const mixResp = await fetch(auth.url, {
    headers: {
      Authorization: auth.authorization,
      Accept: "application/json",
    },
  });

  if (!mixResp.ok) {
    const errText = await mixResp.text();
    return new Response(
      JSON.stringify({
        error: "Mixpanel export failed",
        status: mixResp.status,
        body: errText.slice(0, 2000),
        from_date,
        to_date,
      }),
      { status: 502, headers: { "Content-Type": "application/json" } },
    );
  }

  const rawText = await mixResp.text();
  const parsed = parseJsonl(rawText);

  const rows: Record<string, unknown>[] = [];
  for (const ev of parsed) {
    const props = ev.properties ?? {};
    const ts = typeof props.time === "number" ? props.time : undefined;
    if (ts === undefined) continue;
    if (ts < syncStartSec || ts > endSec) continue;

    const url =
      typeof props.$current_url === "string" ? props.$current_url : undefined;
    const distinct =
      (typeof props.distinct_id === "string" && props.distinct_id) ||
      (typeof (ev as { distinct_id?: string }).distinct_id === "string" &&
        (ev as { distinct_id?: string }).distinct_id) ||
      null;
    if (!distinct) continue;

    const insertId =
      typeof props.$insert_id === "string" ? props.$insert_id : null;
    if (insertId == null && watermarkSec > 0 && ts <= watermarkSec) {
      continue;
    }
    const eventTime = new Date(ts * 1000).toISOString();

    rows.push({
      mixpanel_insert_id: insertId,
      distinct_id: distinct,
      event_name: ev.event,
      friendly_name: resolveFriendlyName(
        ev.event,
        url,
        props as Record<string, unknown>,
        friendlyNameRules,
      ),
      url: url ?? null,
      event_time: eventTime,
      raw_properties: props as Record<string, unknown>,
    });
  }

  const withId = rows.filter((r) => r.mixpanel_insert_id != null);
  const noId = rows.filter((r) => r.mixpanel_insert_id == null);

  const batchSize = 500;
  let written = 0;

  for (let i = 0; i < withId.length; i += batchSize) {
    const batch = withId.slice(i, i + batchSize);
    const { error } = await admin.from("events").upsert(batch, {
      onConflict: "mixpanel_insert_id",
      ignoreDuplicates: false,
    });
    if (error) {
      return new Response(
        JSON.stringify({
          error: "Supabase upsert failed",
          detail: error.message,
          at_batch: i,
        }),
        { status: 500, headers: { "Content-Type": "application/json" } },
      );
    }
    written += batch.length;
  }

  for (let i = 0; i < noId.length; i += batchSize) {
    const batch = noId.slice(i, i + batchSize);
    const { error } = await admin.from("events").insert(batch);
    if (error) {
      return new Response(
        JSON.stringify({
          error: "Supabase insert failed (events without $insert_id)",
          detail: error.message,
          at_batch: i,
        }),
        { status: 500, headers: { "Content-Type": "application/json" } },
      );
    }
    written += batch.length;
  }

  return new Response(
    JSON.stringify({
      ok: true,
      authMode: auth.mode,
      incremental: {
        emptyTable,
        watermarkMixpanelTime: watermarkSec || null,
        overlapSeconds: emptyTable ? null : overlapSec,
        syncStartUtc: syncStartSec,
        endUtc: endSec,
        from_date,
        to_date,
        lookbackDaysApplied: emptyTable ? lookbackDays : null,
      },
      rawLines: parsed.length,
      rowsInSyncWindow: rows.length,
      written,
      rowsWithoutInsertId: noId.length,
      note:
        "Rows with $insert_id are upserted (idempotent). Re-run safely; overlap window re-fetches recent events.",
    }),
    { headers: { "Content-Type": "application/json" } },
  );
});
