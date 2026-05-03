/**
 * Maps Mixpanel export rows to human-readable friendly_name using ordered rules.
 * Supports legacy flat JSON { "regex": "Label" } and v1 { "version": 1, "rules": [...] }.
 */

export type MappingRule =
  | {
    type: "url_regex";
    pattern: string;
    name: string;
    re: RegExp;
    /** If set, only these event names match (default: any event — legacy behavior) */
    forEvents?: string[];
  }
  | {
    type: "properties";
    /** If null, matches any event name */
    event: string | null;
    /** Exact string match per property (all must pass) */
    match?: Record<string, string>;
    /** RegExp test per property (all must pass; patterns compiled at load time) */
    matchRegex?: Record<string, RegExp>;
    name: string;
  };

function compilePropertyRules(
  matchRegex: Record<string, string> | undefined,
): Record<string, RegExp> | undefined {
  if (!matchRegex || Object.keys(matchRegex).length === 0) return undefined;
  const out: Record<string, RegExp> = {};
  for (const [k, pat] of Object.entries(matchRegex)) {
    out[k] = new RegExp(pat);
  }
  return out;
}

export function parseMappingConfig(raw: unknown): MappingRule[] {
  if (raw && typeof raw === "object" && !Array.isArray(raw)) {
    const o = raw as Record<string, unknown>;
    if (Array.isArray(o.rules)) {
      const rules: MappingRule[] = [];
      for (const item of o.rules) {
        if (!item || typeof item !== "object") continue;
        const r = item as Record<string, unknown>;
        if (r.type === "url_regex" && typeof r.pattern === "string" && typeof r.name === "string") {
          const forEvents = Array.isArray(r.forEvents) &&
              r.forEvents.every((x) => typeof x === "string")
            ? r.forEvents as string[]
            : undefined;
          rules.push({
            type: "url_regex",
            pattern: r.pattern,
            name: r.name,
            re: new RegExp(r.pattern),
            forEvents,
          });
        } else if (r.type === "properties" && typeof r.name === "string") {
          const event = "event" in r
            ? (r.event === null ? null : (r.event as string))
            : null;
          const match = r.match && typeof r.match === "object" &&
              !Array.isArray(r.match)
            ? r.match as Record<string, string>
            : undefined;
          const matchRegexRaw = r.matchRegex && typeof r.matchRegex === "object" &&
              !Array.isArray(r.matchRegex)
            ? r.matchRegex as Record<string, string>
            : undefined;
          const hasMatch = match && Object.keys(match).length > 0;
          const hasRegex = matchRegexRaw && Object.keys(matchRegexRaw).length > 0;
          if (!hasMatch && !hasRegex && event === null) {
            continue;
          }
          rules.push({
            type: "properties",
            event,
            match: hasMatch ? match : undefined,
            matchRegex: compilePropertyRules(
              hasRegex ? matchRegexRaw : undefined,
            ),
            name: r.name,
          });
        }
      }
      return rules;
    }
  }
  if (raw && typeof raw === "object" && !Array.isArray(raw)) {
    const legacy = raw as Record<string, string>;
    const rules: MappingRule[] = [];
    for (const [pattern, name] of Object.entries(legacy)) {
      if (pattern === "version" || pattern === "rules") continue;
      rules.push({ type: "url_regex", pattern, name, re: new RegExp(pattern) });
    }
    return rules;
  }
  return [];
}

function propString(props: Record<string, unknown>, key: string): string {
  const v = props[key];
  if (v == null) return "";
  return String(v);
}

/** Prefer explicit URL from importer; else Mixpanel reserved/current props */
export function effectiveUrl(
  url: string | undefined,
  props: Record<string, unknown>,
): string | undefined {
  if (url && typeof url === "string" && url.length > 0) return url;
  const u = props.$current_url;
  if (typeof u === "string" && u.length > 0) return u;
  const domain = props.current_domain;
  const path = props.current_url_path;
  const search = props.current_url_search;
  const proto = props.current_url_protocol;
  if (
    typeof domain === "string" &&
    typeof path === "string"
  ) {
    const p = typeof proto === "string" && proto.length > 0 ? proto : "https:";
    const q = typeof search === "string" ? search : "";
    return `${p}//${domain}${path}${q}`;
  }
  return undefined;
}

export function resolveFriendlyName(
  eventName: string,
  url: string | undefined,
  props: Record<string, unknown>,
  rules: MappingRule[],
): string | null {
  const effective = effectiveUrl(url, props);
  for (const rule of rules) {
    if (rule.type === "url_regex") {
      if (
        rule.forEvents && !rule.forEvents.includes(eventName)
      ) continue;
      if (effective && rule.re.test(effective)) return rule.name;
      continue;
    }
    if (rule.type === "properties") {
      if (rule.event !== null && rule.event !== eventName) continue;
      let ok = true;
      if (rule.match) {
        for (const [k, expected] of Object.entries(rule.match)) {
          if (propString(props, k) !== expected) {
            ok = false;
            break;
          }
        }
      }
      if (!ok) continue;
      if (rule.matchRegex) {
        for (const [k, re] of Object.entries(rule.matchRegex)) {
          if (!re.test(propString(props, k))) {
            ok = false;
            break;
          }
        }
      }
      if (ok) return rule.name;
    }
  }
  return null;
}
