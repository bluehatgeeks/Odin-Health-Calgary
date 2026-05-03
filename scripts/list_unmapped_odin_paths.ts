/** One-off: distinct urls where friendly_name is the odin generic catch-all. */
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.49.1";

const label =
  "Viewed a page on odinhealthlab.ca (path not covered by a named route)";

const url = Deno.env.get("SUPABASE_URL")!.trim();
const key = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!.trim();
const supabase = createClient(url, key);

const { data, error } = await supabase
  .from("events")
  .select("url")
  .eq("friendly_name", label)
  .not("url", "is", null);

if (error) throw error;
const set = new Set((data ?? []).map((r) => r.url as string));
const sorted = [...set].sort();
console.log(JSON.stringify(sorted, null, 2));
console.error("distinct:", sorted.length, "rows:", data?.length);
