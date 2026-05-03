#!/usr/bin/env node
/**
 * Read Mixpanel Raw Export JSONL (or stdin) and print:
 * 1) Distinct event names with counts
 * 2) For interaction events, top fingerprints (event + url + href + text + tag + pathname)
 *
 * Usage:
 *   node scripts/analyze_mixpanel_export.mjs export.jsonl
 *   curl ... | node scripts/analyze_mixpanel_export.mjs
 */

import fs from "node:fs";
import readline from "node:readline";

const FINGERPRINT_KEYS = [
  "$event_type",
  "$current_url",
  "$pathname",
  "$el_tag_name",
  "$el_attr__href",
  "$el_text",
  "$el_attr__aria-label",
];

function pickFingerprint(props) {
  const parts = [];
  for (const k of FINGERPRINT_KEYS) {
    const v = props[k];
    if (v != null && String(v).length > 0) {
      parts.push(`${k}=${truncate(String(v), 120)}`);
    }
  }
  return parts.join(" | ") || "(no fingerprint keys)";
}

function truncate(s, n) {
  return s.length <= n ? s : s.slice(0, n) + "…";
}

async function* linesFromArgs(argv) {
  const path = argv[2];
  if (path && path !== "-") {
    const stream = fs.createReadStream(path, { encoding: "utf8" });
    const rl = readline.createInterface({ input: stream, crlfDelay: Infinity });
    for await (const line of rl) {
      if (line.trim()) yield line;
    }
    return;
  }
  const rl = readline.createInterface({ input: process.stdin, crlfDelay: Infinity });
  for await (const line of rl) {
    if (line.trim()) yield line;
  }
}

const INTERACTION_EVENTS = new Set([
  "$mp_click",
  "$mp_dead_click",
  "$mp_rage_click",
  "$mp_input_change",
  "$mp_submit",
  "$mp_scroll",
  "$mp_web_page_view",
]);

async function main() {
  const eventCounts = new Map();
  const fingerprintCounts = new Map();

  for await (const line of linesFromArgs(process.argv)) {
    let row;
    try {
      row = JSON.parse(line);
    } catch {
      continue;
    }
    const event = row.event;
    if (typeof event !== "string") continue;
    eventCounts.set(event, (eventCounts.get(event) || 0) + 1);

    const props = row.properties && typeof row.properties === "object" ? row.properties : {};
    if (INTERACTION_EVENTS.has(event) || event.startsWith("$mp_")) {
      const fp = `${event} :: ${pickFingerprint(props)}`;
      fingerprintCounts.set(fp, (fingerprintCounts.get(fp) || 0) + 1);
    }
  }

  console.log("=== Event names (sorted by count desc) ===\n");
  const sortedEvents = [...eventCounts.entries()].sort((a, b) => b[1] - a[1]);
  for (const [name, c] of sortedEvents) {
    console.log(`${c}\t${name}`);
  }

  console.log("\n=== Top fingerprints ($mp_* / interactions, sorted by count desc) ===\n");
  const sortedFp = [...fingerprintCounts.entries()].sort((a, b) => b[1] - a[1]).slice(0, 200);
  for (const [fp, c] of sortedFp) {
    console.log(`${c}\t${fp}`);
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
