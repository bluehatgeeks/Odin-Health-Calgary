# GHL → Mixpanel "Appointment Booked" Webhook

Sends every booked appointment into Mixpanel under the contact's email identity,
completing the funnel view: ad → session → quiz → lead → **booking**.
Payload shape validated against `api.mixpanel.com/track` on 2026-07-11 (`status: 1`).

Depends on the lander-side `mixpanel.identify(email)` call (deployed in owen.html /
emma.html) — that's what makes `distinct_id = email` land on the right Mixpanel user.

## Workflow setup (GHL)

1. **Automation → Workflows → Create Workflow**
2. **Trigger:** `Customer Booked Appointment`
   - Optional filter: Calendar = `odin-labs-first-time` (or leave open for all calendars)
3. **Action:** `Webhook` (Custom Webhook)
   - **Method:** POST
   - **URL:** `https://api.mixpanel.com/track`
   - **Headers:**
     | Key | Value |
     |---|---|
     | Content-Type | application/json |
     | Accept | text/plain |
   - **Body (raw JSON):**

```json
[{
  "event": "Appointment Booked",
  "properties": {
    "token": "9c1ce1f2580971e0928ba7cc09cb542e",
    "distinct_id": "{{contact.email}}",
    "$insert_id": "{{appointment.id}}",
    "calendar": "{{appointment.calendar_name}}",
    "appointment_start": "{{appointment.start_time}}",
    "quiz": "{{contact.quiz}}",
    "utm_content": "{{contact.utm_content}}",
    "utm_campaign": "{{contact.utm_campaign}}",
    "mixpanel_device_id": "{{contact.mixpanel_id}}"
  }
}]
```

4. Save + publish the workflow.

## Merge-tag notes

- `{{contact.email}}` and `{{appointment.*}}` are standard GHL tags — verify exact
  appointment tag names in the workflow editor's merge-tag picker (varies by GHL version:
  may be `{{appointment.startTime}}` etc.).
- `{{contact.quiz}}`, `{{contact.utm_content}}`, `{{contact.utm_campaign}}`,
  `{{contact.mixpanel_id}}` refer to **custom fields** — use the actual custom-field keys
  as created when mapping the quiz webhook payload. If a field doesn't exist, drop that
  line rather than sending literal `{{...}}` text.
- `$insert_id` deduplicates retries — keep it if an appointment-id tag exists.
- The `token` is the public Mixpanel project token (same one embedded in the site JS) —
  safe to include in the payload; it only allows writes, not reads.

## Verify

1. Book a test appointment (use a `+test` email or known test contact).
2. Mixpanel → Events: filter `Appointment Booked` (arrives within ~1 min).
3. Open the user profile by email — the booking should sit on the same identity as
   their quiz session and ad attribution.
4. A setup-test event exists from 2026-07-11: distinct_id `webhook-setup-test@odinlab.test`,
   property `is_setup_test: true` — exclude/ignore in reports.

## Extend later (same pattern)

- `Appointment Cancelled` / `No Show` triggers → same webhook with different event names.
- Payment received → `"event": "Purchase"` with `amount` property → true ROAS per ad
  concept inside Mixpanel.
