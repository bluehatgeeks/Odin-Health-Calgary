import {
  parseMappingConfig,
  resolveFriendlyName,
} from "./friendly_name_resolver.ts";
import mapping from "./mixpanel_event_mapping.json" with { type: "json" };
import { assertEquals } from "https://deno.land/std@0.224.0/assert/mod.ts";

const rules = parseMappingConfig(mapping);

Deno.test("homepage URL maps to Viewed Home page", () => {
  const name = resolveFriendlyName(
    "$mp_web_page_view",
    "https://odinhealthlab.ca/?gclid=1",
    {},
    rules,
  );
  assertEquals(name, "Viewed Home page");
});

Deno.test("book-now path beats home regex", () => {
  const name = resolveFriendlyName(
    "$mp_web_page_view",
    "https://odinhealthlab.ca/book-now",
    {},
    rules,
  );
  assertEquals(name, "Viewed Book Now scheduling page");
});

Deno.test("metabolic hash URL", () => {
  const name = resolveFriendlyName(
    "$mp_web_page_view",
    "https://odinhealthlab.ca/#metabolic-assessment-trigger",
    {},
    rules,
  );
  assertEquals(name, "Metabolic Stability Assessment (URL changed to #metabolic-assessment-trigger)");
});

Deno.test("$mp_click with Book Now href", () => {
  const name = resolveFriendlyName(
    "$mp_click",
    "https://odinhealthlab.ca/",
    {
      "$el_attr__href": "/book-now",
      "$pathname": "/",
    },
    rules,
  );
  assertEquals(name, "Clicked link or button targeting Book Now");
});

Deno.test("$mp_click CTA text when capture_text_content is on", () => {
  const name = resolveFriendlyName(
    "$mp_click",
    undefined,
    {
      "$el_text": "Take the Metabolic Stability Assessment",
      "$current_url": "https://odinhealthlab.ca/",
    },
    rules,
  );
  assertEquals(name, "Clicked: Take the Metabolic Stability Assessment");
});

Deno.test("legacy flat mapping still parses", () => {
  const legacy = {
    "https?://example\\.com/foo": "Foo page",
  };
  const r = parseMappingConfig(legacy);
  const n = resolveFriendlyName(
    "$mp_web_page_view",
    "https://example.com/foo",
    {},
    r,
  );
  assertEquals(n, "Foo page");
});

Deno.test("Page View uses same URL labels as $mp_web_page_view (home)", () => {
  const rules = parseMappingConfig(mapping);
  const n = resolveFriendlyName(
    "Page View",
    "https://odinhealthlab.ca/",
    { "$current_url": "https://odinhealthlab.ca/" },
    rules,
  );
  assertEquals(n, "Viewed Home page");
});

Deno.test("Page View on /supplements", () => {
  const rules = parseMappingConfig(mapping);
  const n = resolveFriendlyName(
    "Page View",
    "https://odinhealthlab.ca/supplements",
    { "$current_url": "https://odinhealthlab.ca/supplements" },
    rules,
  );
  assertEquals(n, "Viewed Supplements & herbology page");
});

Deno.test("$mp_session_record gets session replay label", () => {
  const rules = parseMappingConfig(mapping);
  const n = resolveFriendlyName(
    "$mp_session_record",
    "https://odinhealthlab.ca/",
    { "$current_url": "https://odinhealthlab.ca/" },
    rules,
  );
  assertEquals(n, "Session replay metadata (Mixpanel session recording batch)");
});

Deno.test("Lead Connector booking widget Page View", () => {
  const rules = parseMappingConfig(mapping);
  const url =
    "https://api.leadconnectorhq.com/widget/bookings/odin-labs-example";
  const n = resolveFriendlyName(
    "Page View",
    url,
    { "$current_url": url },
    rules,
  );
  assertEquals(
    n,
    "Viewed appointment booking widget (GoHighLevel / Lead Connector)",
  );
});

Deno.test("$mp_web_page_view on Lead Connector host", () => {
  const rules = parseMappingConfig(mapping);
  const url = "https://api.leadconnectorhq.com/some/other/path";
  const n = resolveFriendlyName(
    "$mp_web_page_view",
    url,
    { "$current_url": url },
    rules,
  );
  assertEquals(n, "Viewed Lead Connector / GoHighLevel hosted page");
});

Deno.test("Page View on /ayurveda", () => {
  const rules = parseMappingConfig(mapping);
  const u = "https://odinhealthlab.ca/ayurveda?utm=1";
  const n = resolveFriendlyName("Page View", u, { "$current_url": u }, rules);
  assertEquals(n, "Viewed Ayurveda page");
});

Deno.test("Page View on /marma-therapy", () => {
  const rules = parseMappingConfig(mapping);
  const u =
    "https://odinhealthlab.ca/marma-therapy?gad_source=1&gclid=test";
  const n = resolveFriendlyName("$mp_web_page_view", u, { "$current_url": u }, rules);
  assertEquals(n, "Viewed Marma therapy & tuning fork page");
});

Deno.test("$mp_web_page_view with #about-us-section hash", () => {
  const rules = parseMappingConfig(mapping);
  const u = "https://odinhealthlab.ca/#about-us-section";
  const n = resolveFriendlyName(
    "$mp_web_page_view",
    u,
    { "$current_url": u },
    rules,
  );
  assertEquals(
    n,
    "Viewed Home page — About us / clinic section (#about-us-section)",
  );
});

Deno.test("$mp_click on home root without hash", () => {
  const rules = parseMappingConfig(mapping);
  const u = "https://odinhealthlab.ca/?gad_source=1";
  const n = resolveFriendlyName("$mp_click", u, { "$current_url": u }, rules);
  assertEquals(n, "Clicked on Home page (root URL, no hash — non-CTA control)");
});
