import { createClient } from "https://esm.sh/@supabase/supabase-js@2.49.1";

const label =
  "Clicked on odinhealthlab.ca (unmatched control — refine mapping if this is common)";

const url = Deno.env.get("SUPABASE_URL")!.trim();
const key = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!.trim();
const supabase = createClient(url, key);

const { data, error } = await supabase
  .from("events")
  .select("url, event_name, raw_properties")
  .eq("friendly_name", label);

if (error) throw error;

const byUrl = new Map<string, number>();
for (const r of data ?? []) {
  const u = (r.url as string) || "";
  byUrl.set(u, (byUrl.get(u) || 0) + 1);
}

const sorted = [...byUrl.entries()].sort((a, b) => b[1] - a[1]);
console.log(JSON.stringify({ totalRows: data?.length, distinctUrls: sorted.length, urls: sorted }, null, 2));
