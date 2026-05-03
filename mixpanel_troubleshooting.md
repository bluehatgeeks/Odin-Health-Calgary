# Mixpanel Integration Troubleshooting

## Recent updates (2026-05-02)

- Disabled JWT verification for the Edge Function `fetch_mixpanel_events` (redeployed with `--no-verify-jwt`).
- Patched the function to use Unix‑timestamp range parameters instead of ISO strings.
- Switched Mixpanel Export API authentication from legacy Basic‑Auth header to query‑string auth (`api_key` and `api_secret`).
- Redeployed the function; now returns a non‑zero `fetched` count (verified after confirming Mixpanel has events).
- Updated documentation in this file to reflect the new authentication method and deployment steps.

**Current status**: Mixpanel has been successfully installed on GoHighLevel (GHL).

**Problem**: We need to capture the Mixpanel `distinct_id` when a user books an appointment. Our goal is to retrieve the `distinct_id` for each booking and map it to a user ID based on the email address. At the moment, the existing scripts are not correctly capturing the Mixpanel ID.

**Next steps**:
- Verify that the Mixpanel SDK is correctly loaded on the booking page.
- Ensure the script that copies `mixpanel.get_distinct_id()` into a hidden form field (`mixpanel_id`) is executing before the form submission.
- Confirm that the hidden field is being sent to GHL and stored in the custom contact field.
- Implement logic (server‑side or via a GHL webhook) to map the captured `distinct_id` to the user's email address and store the association.

---

**Second problem**: Convert auto‑generated Mixpanel events into human‑readable names.

When Mixpanel records an automatic event such as `[Auto] Page View = https://odinhealthlab.ca/?gad_source=1&gad_campaignid=23752865895&gclid=CjwKCAjwqazPBhALEiwAOuXqdGmgODFxg6GpKp5jXsYjGt7UjSrrCFi5PMOvMKIHCuo82-KSHf4p8BoC7qIQAvD_BwE&ref=google.com/#metabolic-assessment-trigger` we want the dashboard to display a friendly label like **"Clicked on Metabolic Assessment Quiz"** instead of the raw URL.

**Proposed approach**:
- Define a mapping table (e.g., JSON or a GHL custom field) that pairs URL patterns or query parameters with readable event names.
- Add a client‑side script (or Mixpanel‑gateway webhook) that intercepts the raw page‑view event, looks up the mapping, and sends a custom event with the friendly name.
- Optionally, use Mixpanel’s **event aliasing** feature to rename events server‑side.
- Update documentation and add tests to verify that URLs are correctly translated.

**Next steps**:
1. Create a `mixpanel_event_names.json` file in the project root with key/value pairs of URL fragments → readable names.
2. Implement a small JavaScript helper to run on the booking page that extracts the URL, matches it against the mapping, and fires `mixpanel.track('Clicked on Metabolic Assessment Quiz')`.
3. Verify in Mixpanel Live View that the friendly event name appears.
4. Document the mapping format and update the README.
