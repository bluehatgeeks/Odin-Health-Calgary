# Odin Labs Calgary - Clinic Operations Hub

**Last Updated:** 2026-05-03  
**Status:** Execution Phase  
**Website:** https://odinhealthlab.ca/  
**Location:** Calgary, Alberta  

---

## 📋 Overview

This is the central repository for Odin Labs Calgary clinic setup, operations, and growth. It contains clinical protocols, operational procedures, marketing strategies, and technical integrations.

---

## 📁 Folder Structure

### `00_ADMIN/` - Project Administration
- `PROJECT_LOG.md` - Active changelog and project status
- `STATE.json` - Current project state
- `google_oauth_client_secret.json` - OAuth credentials (restricted access)

### `01_BUSINESS_STRATEGY/` - Core Business Documents
- `services_and_pricing.md` - Service menu and pricing
- `patient_segments.md` - Target patient demographics and personas

### `02_MARKET_INTEL/` - Market Research
- `research.md` - Market research findings
- `keyword_data/` - SEO and keyword research data (JSON files)

### `03_CLINICAL_OPERATIONS/` - Clinical Protocols & Standards
#### `protocols/`
- `ayurveda_roadmap_template.md` - Standard Ayurveda treatment pathway
- `functional_health_blueprint_template.md` - Functional health assessment template
- `treatment_protocol_log_template.md` - Treatment logging format
- `min_browser_protocol.md` - Minimum browser requirements for digital tools

#### `consumables/`
- `sourcing.md` - Vendor information and sourcing guide
- `final_sku_list.md` - Approved consumables list

### `04_PATIENT_EXPERIENCE/` - Patient Journey
- `patient_intake_protocol.md` - Standard intake process
- `patient_journey_map.md` - End-to-end patient experience map
- `patient_feedback_loop.md` - Feedback collection and response system

### `05_STAFFING/` - Human Resources
- `roles_and_responsibilities.md` - Clinical and operational roles
- `onboarding_guide.md` - New staff onboarding process
- `clinical_qa_framework.md` - Quality assurance standards

### `06_MARKETING_GROWTH/` - Marketing & Customer Acquisition
#### `google_ads/`
- `strategy.md` - Google Ads strategic approach
- `paid_search_blueprint.md` - Paid search execution guide

- `implementation_checklist.md` - Growth initiative checklist
- `growth_strategy_package.md` - Comprehensive growth strategy

### `07_TECH_STACK/` - Technology & Integrations
#### `integrations/`
- `ghl_sheets_webhook_blueprint.md` - GoHighLevel to Google Sheets automation

#### `keyword_data/`
- `serp_market_data.json` - SERP analysis data
- `keyword_volume_matrix.json` - Keyword volume research
- `keyword_demand_validation.json` - Demand validation metrics

### `08_OPERATIONS_PLAYBOOK/` - Operational Procedures
- `daily_clinic_checklist.md` - Daily opening/closing procedures
- `facility_vendor_guide.md` - Vendor contacts and management
- `modality_integration_guide.md` - Integrating treatment modalities
- `equipment_maintenance.md` - Equipment maintenance schedules
- `emergency_response_protocol.md` - Emergency procedures
- `continuity_plan.md` - Business continuity planning
- `lead_intake_form_spec.md` - Lead intake form specifications
- `inventory_management_system.md` - Inventory tracking system

### `09_MEETINGS_LOGS/` - Meeting Records
- `session_log.md` - Session and meeting logs

### `archive/` - Historical & Deprecated Files
- `legacy_scripts/` - Archived automation scripts (15 files)

### `supabase/` - Supabase project (CLI)
- `config.toml` - Local Supabase config; `[functions.fetch_mixpanel_events] verify_jwt = false`
- `functions/fetch_mixpanel_events/` - Edge Function that imports Mixpanel → `public.events`
- `migrations/` - Database migrations (e.g. `mixpanel_insert_id` unique index for upserts)
- `mixpanel_hourly_cron.sql` - Optional hosted-only SQL to schedule the function every hour (Vault + pg_cron)
- `seed.sql` - Empty seed placeholder for `supabase db reset`

---

## 📦 Mixpanel → Supabase import (runbook)

**Status (2026-05-03):** End-to-end import is working. The Edge Function `fetch_mixpanel_events` calls Mixpanel’s Raw Export API, incrementally loads new events into `public.events`, and deduplicates on Mixpanel `$insert_id` via `mixpanel_insert_id`. Any agent can reproduce the setup by following the steps below in order.

### Replication checklist (strict order)

1. Create `.env` with `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `MIXPANEL_PROJECT_TOKEN`, `MIXPANEL_API_SECRET` (see table below). Do not commit it.
2. Ensure `public.events` exists (`create_events_table.sql`) and apply `supabase/migrations/20260503120000_events_mixpanel_insert_id.sql` (full unique index on `mixpanel_insert_id`).
3. `npx supabase@latest login` then `npx supabase@latest link --project-ref <project-ref>`.
4. Confirm `supabase/config.toml` has `[functions.fetch_mixpanel_events] verify_jwt = false`.
5. `npx supabase@latest functions deploy fetch_mixpanel_events --no-verify-jwt`.
6. `npx supabase@latest secrets set` for `MIXPANEL_PROJECT_TOKEN` and `MIXPANEL_API_SECRET` (and optional `MIXPANEL_SYNC_*` / service-account vars).
7. Smoke-test with `curl` `POST` to `/functions/v1/fetch_mixpanel_events` using the service role key; expect `"ok": true`.
8. (Optional) Configure Vault + run `supabase/mixpanel_hourly_cron.sql` for hourly UTC runs.

### What gets imported

- **Source:** [Mixpanel Raw Data Export](https://developer.mixpanel.com/reference/raw-event-export) (`https://data.mixpanel.com/api/2.0/export`).
- **Target table:** `public.events` (see `create_events_table.sql` in the repo root for the baseline schema).
- **Incremental logic:** The function reads the newest stored event (by `event_time`, with `raw_properties.time` as the Mixpanel watermark). If the table is empty, it pulls the last **N** days (`MIXPANEL_SYNC_LOOKBACK_DAYS`, default **30**). If data exists, it pulls from **watermark − overlap** through **now** (`MIXPANEL_SYNC_OVERLAP_SECONDS`, default **3600**), then filters by Mixpanel event `time`. Rows with `$insert_id` are **upserted** on `mixpanel_insert_id` (safe to re-run).

### Critical detail: Export API Basic authentication

For **legacy project credentials** (`MIXPANEL_PROJECT_TOKEN` + `MIXPANEL_API_SECRET`), Mixpanel expects HTTP Basic credentials in this order: **`API_SECRET:PROJECT_TOKEN`** (secret first, then token). Encoding the pair the other way returns `400 Unable to authenticate request`. The Edge Function uses `api_secret:project_token`.

**Service accounts** (`MIXPANEL_SERVICE_USERNAME` + `MIXPANEL_SERVICE_SECRET`) are supported only together with a **numeric** `MIXPANEL_PROJECT_ID` (from Mixpanel project settings). If `MIXPANEL_PROJECT_TOKEN` and `MIXPANEL_API_SECRET` are both set as secrets, they take precedence in the function.

### Environment variables (local `.env`, never commit)

Use a `.env` at the repo root for local runs and as the source for Supabase Edge secrets. Required names:

| Variable | Purpose |
|----------|---------|
| `SUPABASE_URL` | Project URL, e.g. `https://<project-ref>.supabase.co` |
| `SUPABASE_SERVICE_ROLE_KEY` | Service role key (invoking the function manually; hosting injects keys into Edge automatically) |
| `MIXPANEL_PROJECT_TOKEN` | Mixpanel **project token** (public tracking token / project settings) |
| `MIXPANEL_API_SECRET` | Mixpanel **API secret** (export auth; pair with token using Basic `secret:token`) |

Optional:

| Variable | Purpose |
|----------|---------|
| `MIXPANEL_SERVICE_USERNAME` / `MIXPANEL_SERVICE_SECRET` / `MIXPANEL_PROJECT_ID` | Service-account path (numeric project ID only) |
| `MIXPANEL_SYNC_LOOKBACK_DAYS` | First-run depth when `events` is empty (default `30`, max `365`) — set as Edge secret if needed |
| `MIXPANEL_SYNC_OVERLAP_SECONDS` | Replay window behind watermark when table has data (default `3600`, min `60`) |

### One-time: database schema

1. In the Supabase SQL editor (or via CLI against the linked project), run `create_events_table.sql` if `public.events` does not exist yet.
2. Apply the migration that adds **`mixpanel_insert_id`** and a **unique index** on it (required for PostgREST `.upsert` with `onConflict: mixpanel_insert_id`):
   - File: `supabase/migrations/20260503120000_events_mixpanel_insert_id.sql`
   - If `supabase db push` fails because remote migration history disagrees with this repo, apply the same SQL with:
     ```bash
     cd /path/to/odin-labs-calgary
     npx supabase@latest db query --linked -f supabase/migrations/20260503120000_events_mixpanel_insert_id.sql
     ```

The index must be a **full** unique index on `mixpanel_insert_id` (not partial), or upserts will error.

### One-time: Supabase CLI and link

Use **`npx supabase@latest`** if the global CLI is not installed.

```bash
cd /path/to/odin-labs-calgary
npx supabase@latest login
npx supabase@latest link --project-ref <project-ref>
```

`supabase init` should have created `supabase/config.toml`. Confirm it contains:

```toml
[functions.fetch_mixpanel_events]
verify_jwt = false
```

### Deploy the Edge Function

```bash
cd /path/to/odin-labs-calgary
npx supabase@latest functions deploy fetch_mixpanel_events --no-verify-jwt
```

Bundled assets include `index.ts` and `supabase/functions/fetch_mixpanel_events/mixpanel_event_mapping.json` (URL → friendly label for dashboards).

### Push Mixpanel secrets to Supabase (Edge)

Secrets are **not** read from your laptop at runtime; they must exist on the project:

```bash
cd /path/to/odin-labs-calgary
set -a && source .env && set +a
npx supabase@latest secrets set \
  MIXPANEL_PROJECT_TOKEN="$MIXPANEL_PROJECT_TOKEN" \
  MIXPANEL_API_SECRET="$MIXPANEL_API_SECRET"
```

Add service-account variables only if you use that path. Add optional `MIXPANEL_SYNC_*` keys if you want non-default lookback/overlap.

### Invoke manually (smoke test)

```bash
set -a && source .env && set +a
curl -sS -X POST "$SUPABASE_URL/functions/v1/fetch_mixpanel_events" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_ROLE_KEY" \
  -H "apikey: $SUPABASE_SERVICE_ROLE_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

Expect JSON with `"ok": true`, `authMode` (`project_token` or `service_account`), `incremental` (watermark and date window), `rawLines`, `rowsInSyncWindow`, and `written`.

### Optional: hourly schedule (hosted Postgres)

JWT verification is off for this function; the scheduler should call it with the **anon / publishable** key, stored in **Supabase Vault**, per [Scheduling Edge Functions](https://supabase.com/docs/guides/functions/schedule-functions).

1. Enable **pg_cron**, **pg_net**, and **Vault** as needed in the dashboard.
2. Run the Vault `create_secret` snippets for `project_url` and `publishable_key`.
3. Run `supabase/mixpanel_hourly_cron.sql` in the SQL editor (adjust placeholders). Schedule is **`0 * * * *`** (minute 0 of every hour, UTC).

### Troubleshooting (quick)

| Symptom | Likely cause |
|---------|----------------|
| `400 Unable to authenticate request` (Mixpanel) | Basic auth order wrong; use `API_SECRET:PROJECT_TOKEN`, or wrong token/secret |
| `Expected project_id parameter to be a number` | `MIXPANEL_PROJECT_ID` must be numeric for service-account export |
| `no unique or exclusion constraint matching the ON CONFLICT` | Missing or partial unique index on `mixpanel_insert_id`; apply migration above |
| Empty `written` but Mixpanel has data | Date window or filters excluded events; check `incremental` in the JSON response |

### Related files

- `supabase/functions/fetch_mixpanel_events/index.ts` — importer implementation
- `supabase/functions/fetch_mixpanel_events/mixpanel_event_mapping.json` — regex → friendly name (bundled with the function)
- `mixpanel_troubleshooting.md` — GHL / client-side Mixpanel notes (separate from this server import)

## 🔧 Connected Tools

### Google Workspace
- **Drive:** Odin Labs Clinic Operations
  - Folder: https://drive.google.com/drive/folders/1i0J2ICnGAbcPAqiFSS1RFyMT10kfSLjO
- **Sheets:** Odin_Labs_Clinic_Dashboard
- **Auth:** OAuth2 configured with full Drive access
- **Client ID:** `637011530953-a80m8p8p3qaaj0mbur47fk3it3m2su9q`

### Trello
- **Board:** Odin Labs Calgary
- **Purpose:** Primary roadmap and task management

### GoHighLevel (GHL)
- **Purpose:** CRM, calendar booking, patient intake
- **Integration:** Webhook to Google Sheets

---

## 📋 Key Workflows

### Patient Intake Flow
1. Lead captured via Google Ads → GHL
2. Automated intake form sent
3. Booking confirmed via GHL calendar
4. Patient data synced to Google Sheets
5. Treatment protocol logged in Drive

### Treatment Documentation
1. Initial consultation using protocol templates
2. Treatment plan created (Ayurveda/Functional Health)
3. Follow-up scheduled
4. Progress tracked in treatment log

### File Sync to Drive
```bash
cd /Users/alexandertretjakov/Downloads/odin-labs-calgary
python3 reliable_sync.py
```
This uploads all local files to the Google Drive folder with the same structure.

---

## 🔐 Access & Security

### OAuth Credentials
- **Token Location:** `~/.hermes/google_token.json` (auto-refreshing)
- **Client Secret:** `00_ADMIN/google_oauth_client_secret.json` (restricted)
- **Scopes:** Full Drive, Gmail (read/send/modify), Calendar, Sheets, Docs, Contacts

### Access Levels
- **Clinical Documents:** All staff
- **OAuth Credentials:** Admin only
- **Financial Data:** Admin only

---

## 📊 Current Services

| Service | Price | Notes |
|---------|-------|-------|
| Ayurveda Initial Consultation | $300 | Includes 2 visits (intake + follow-up) |
| Ayurveda Follow-up | $100 | Subsequent visits |
| Marma Therapy Initial | $150 | First consultation |
| Marma Therapy Standard | $100 | Regular treatment |
| PEMF Treatment | $60 | Per session |
| Hydrogen Inhalation | $60 | Per session |
| Health Coaching | $300/month | Includes intake and monthly review |

---

## 🚀 Next Steps / Open Items

- [ ] Procurement: Final order of consumables
- [ ] Staffing: Finalize clinical role definitions
- [ ] Staffing: Complete onboarding guide
- [ ] Operations: Design complete patient flow
- [ ] Tech: Optimize GHL workflow automation
- [ ] Marketing: Launch persona-based landing pages

---

## 📝 Version History

**2026-05-03:** Mixpanel → Supabase import documented and operational
- Edge Function `fetch_mixpanel_events`: incremental sync, upsert by `mixpanel_insert_id`, legacy auth `api_secret:project_token`
- README runbook added for full agent replication; optional hourly cron via `supabase/mixpanel_hourly_cron.sql`
- Removed redundant Python importer, root mapping duplicate, and naming-plan doc (Edge Function + bundled JSON only)

**2026-04-21:** Major reorganization & Google Drive sync
- Consolidated `history/` folder into 11 operational categories
- Removed empty placeholder folders
- Archived 15 legacy Python scripts
- Created comprehensive README
- Synced 34 files to Google Drive
- Configured full OAuth 2.0 access

**Previous:** Files organized in `history/` folder with subdirectories (ops/, tech/, growth/, personnel/)

---

## 📞 Contact & Support

**Project Owner:** Alexander Tretjakov  
**Business:** Odin Labs Calgary  
**Website:** https://odinhealthlab.ca/  
**Email:** calwebprod@gmail.com  

---

## 🛠 Technical Notes

### Running the Sync Script
```bash
# Ensure Python dependencies are installed
pip install google-api-python-client google-auth-oauthlib google-auth-httplib2

# Run sync
python3 reliable_sync.py
```

### OAuth Token Refresh
The token auto-refreshes when needed. If authentication fails:
```bash
# Revoke old token
cd ~/.hermes/skills/productivity/google-workspace/scripts
python3 setup.py --revoke

# Re-authenticate
python3 setup.py --auth-url
# Then follow the OAuth flow
```

### Folder IDs
- **Main Drive Folder:** `1i0J2ICnGAbcPAqiFSS1RFyMT10kfSLjO`
- **Trello Board:** `69d1375de0ea6c9778b41883`

---

*This repository is actively maintained. Check `00_ADMIN/PROJECT_LOG.md` for the latest updates.*
