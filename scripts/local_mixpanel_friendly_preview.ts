/**
 * Local preview: fetch Mixpanel Raw Export (or read JSONL) and print friendly_name per row.
 *
 * Offline (no API keys):
 *   npx deno run --allow-read scripts/local_mixpanel_friendly_preview.ts --file fixtures/mixpanel_sample.jsonl
 *
 * Live sample (reads .env MIXPANEL_API_SECRET + MIXPANEL_PROJECT_TOKEN):
 *   npx deno run --allow-env --allow-net --allow-read --env-file=.env scripts/local_mixpanel_friendly_preview.ts --days 2 --limit 30
 *
 * Options:
 *   --file <path>     Use this JSONL instead of Mixpanel API
 *   --days <n>        from_date = today − n (default 2), to_date = today (UTC)
 *   --limit <n>       Max events to print (default 100)
 *   --json            Full JSON array to stdout (includes raw_properties ref)
 */

import {
  parseMappingConfig,
  resolveFriendlyName,
} from "../supabase/functions/fetch_mixpanel_events/friendly_name_resolver.ts";
import mapping from "../supabase/functions/fetch_mixpanel_events/mixpanel_event_mapping.json" with {
  type: "json",
};

type Row = {
  event: string;
  properties?: Record<string, unknown>;
};

function parseArgs(argv: string[]) {
  let file: string | undefined;
  let days = 2;
  let limit = 100;
  let jsonOut = false;
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--file" && argv[i + 1]) {
      file = argv[++i];
    } else if (a.startsWith("--file=")) {
      file = a.slice("--file=".length);
    } else if (a === "--days" && argv[i + 1]) {
      days = Math.max(1, parseInt(argv[++i], 10) || 2);
    } else if (a.startsWith("--days=")) {
      days = Math.max(1, parseInt(a.slice("--days=".length), 10) || 2);
    } else if (a === "--limit" && argv[i + 1]) {
      limit = Math.max(1, parseInt(argv[++i], 10) || 100);
    } else if (a.startsWith("--limit=")) {
      limit = Math.max(1, parseInt(a.slice("--limit=".length), 10) || 100);
    } else if (a === "--json") {
      jsonOut = true;
    }
  }
  return { file, days, limit, jsonOut };
}

function utcYmd(d: Date): string {
  return d.toISOString().slice(0, 10);
}

async function fetchMixpanelJsonl(
  fromDate: string,
  toDate: string,
): Promise<string> {
  const token = Deno.env.get("MIXPANEL_PROJECT_TOKEN")?.trim();
  const secret = Deno.env.get("MIXPANEL_API_SECRET")?.trim();
  if (!token || !secret) {
    throw new Error(
      "Set MIXPANEL_PROJECT_TOKEN and MIXPANEL_API_SECRET (e.g. via --env-file=.env), or use --file fixtures/mixpanel_sample.jsonl",
    );
  }
  const exportUrl = new URL("https://data.mixpanel.com/api/2.0/export");
  exportUrl.searchParams.set("from_date", fromDate);
  exportUrl.searchParams.set("to_date", toDate);
  const auth = btoa(`${secret}:${token}`);
  const res = await fetch(exportUrl.toString(), {
    headers: {
      Authorization: `Basic ${auth}`,
      Accept: "application/json",
    },
  });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(
      `Mixpanel export ${res.status}: ${body.slice(0, 500)}`,
    );
  }
  return await res.text();
}

function parseJsonl(text: string): Row[] {
  const out: Row[] = [];
  for (const line of text.split("\n")) {
    const t = line.trim();
    if (!t) continue;
    try {
      out.push(JSON.parse(t) as Row);
    } catch {
      // skip
    }
  }
  return out;
}

async function main() {
  const args = parseArgs(Deno.args);
  const rules = parseMappingConfig(mapping);

  let source: string;
  let rawText: string;

  if (args.file) {
    source = `file:${args.file}`;
    rawText = await Deno.readTextFile(args.file);
  } else {
    const end = new Date();
    const start = new Date(end.getTime() - args.days * 86400000);
    const from_date = utcYmd(start);
    const to_date = utcYmd(end);
    source = `mixpanel export ${from_date}..${to_date} (UTC)`;
    rawText = await fetchMixpanelJsonl(from_date, to_date);
  }

  const events = parseJsonl(rawText);
  const slice = events.slice(0, args.limit);

  const enriched = slice.map((ev) => {
    const props = ev.properties && typeof ev.properties === "object"
      ? ev.properties as Record<string, unknown>
      : {};
    const url = typeof props.$current_url === "string"
      ? props.$current_url
      : undefined;
    const friendly = resolveFriendlyName(ev.event, url, props, rules);
    return {
      event_name: ev.event,
      friendly_name: friendly,
      url: url ?? null,
      distinct_id: typeof props.distinct_id === "string"
        ? props.distinct_id
        : null,
      time_iso: typeof props.time === "number"
        ? new Date(props.time * 1000).toISOString()
        : null,
      raw_properties: props,
    };
  });

  const mapped = enriched.filter((r) => r.friendly_name != null).length;
  console.log("=== Mixpanel → friendly_name (local preview) ===\n");
  console.log(`Source: ${source}`);
  console.log(`Rows parsed: ${events.length} (showing ${enriched.length})`);
  console.log(
    `Mapped: ${mapped} / ${enriched.length} (${enriched.length ? Math.round(100 * mapped / enriched.length) : 0}%)\n`,
  );

  if (args.jsonOut) {
    const slim = enriched.map((r) => ({
      event_name: r.event_name,
      friendly_name: r.friendly_name,
      url: r.url,
      distinct_id: r.distinct_id,
      time_iso: r.time_iso,
      raw_properties: r.raw_properties,
    }));
    console.log(JSON.stringify(slim, null, 2));
    return;
  }

  const table = enriched.map((r) => ({
    event_name: r.event_name,
    friendly_name: r.friendly_name ?? "(null)",
    url: r.url == null ? "" : r.url.length > 64 ? r.url.slice(0, 61) + "…" : r.url,
    time_iso: r.time_iso ?? "",
  }));
  console.table(table);

  console.log("\n--- First row raw_properties keys (for debugging rules) ---\n");
  if (enriched[0]) {
    console.log(Object.keys(enriched[0].raw_properties).sort().join(", "));
  }
}

main().catch((e) => {
  console.error(e instanceof Error ? e.message : e);
  Deno.exit(1);
});
