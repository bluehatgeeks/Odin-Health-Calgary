# Project: Odin Labs Calgary Clinic Setup
**Status:** Execution Phase
**Start Date:** 2026-04-04

> **Note (2026-09-04):** this log is historical and describes the folder structure as it existed when each entry was written — paths below (e.g. `00_ADMIN/`, `06_MARKETING_GROWTH/`) predate the 2026-09-04 vault reorg into `Calgary-Local/` / `Telehealth/` / shared root. For the current structure, see the vault root `README.md`. This file itself now lives at `Calgary-Local/00_ADMIN/PROJECT_LOG.md`. The project is also mid-pivot to telehealth-only as of 2026-09-03 — see `Telehealth/2026-09-03-telehealth-only-pivot-decision.md`.

## 🎯 North Star
Setup of the tech stack, staffing, and operational workflows for the Calgary clinic, including market research on competitors and demographics.

## 🛠 Project Assets
- **Official Website:** https://odinhealthlab.ca/
- **Service & Pricing:** `odin-calgary/SERVICES_AND_PRICING.md`
- **Patient Segments:** `odin-calgary/PATIENT_SEGMENTS.md`
- **Google Drive:** `Odin Labs Clinic Operations` (Autonomous Access)
- **Google Sheets:** `Odin_Labs_Clinic_Dashboard` (Now used for Data/KPIs; Roadmap migrated to Trello)
- **Drive/Sheets Auth:** Verified OAuth2 flow using Client ID `637011530953-a80m8p8p3qaaj0mbur47fk3it3m2su9q` (Tokens in `.oauth_tokens.json`)
- **Trello:** `Odin Labs Calgary` (Primary Roadmap & Task Management)
- **Focus:** Ayurveda and Holistic Health

## 🗺 Roadmap
- [x] Initial Research (Competitive Intel & Vendor Sourcing)
- [x] Infrastructure Setup (Drive, Sheets, Trello, GHL)
- [x] Patient Segment Definition
- [x] Ayurveda Roadmap Template Design
- [x] Functional Health Blueprint Template Design
- [x] Treatment Protocol Log Template Design
- [x] Tech Stack Integration: Patient Pipeline Automation (GHL $\rightarrow$ Sheets $\rightarrow$ Drive)
- [x] Drive Sync: Autonomous Mirroring of Local Project Files to Google Drive (Verified 2026-04-07)
- [x] OAuth2 Recovery: Restoration of autonomous Sheets/Drive access via verified Client ID
- [x] Project Reorganization: Consolidated history/ into 11 operational categories (2026-04-21)
- [x] Google Drive Sync: All 34 files uploaded with folder structure (2026-04-21)
- [ ] Procurement Execution: Final Order of Consumables
- [ ] Staffing Workflow: Clinical Role Definition & Onboarding Guideck Finalization (GHL Workflow Optimization)
- [ ] Staffing Plan
- [ ] Operational Workflow Design
- [ ] Clinic Patient Flow Design (End-to-end patient journey, touchpoints, and tool requirements)
NOTIFICATION: Reminder sent to user regarding sign-off for CONSUMABLES_FINAL_SKU.md and GROWTH_STRATEGY_PACKAGE.md in the 00_To_Be_Approved folder.

---

## Issue Resolution Log

### Major Project Reorganization (2026-04-21)
**Status:** COMPLETED
**Category:** Infrastructure/Organization

**Changes:**
- Consolidated `history/` folder into logical operational categories
- Removed empty placeholder folders (01-business-plan through 09-meetings-notes)
- Archived 15 legacy Python scripts to `archive/legacy_scripts/`
- Created comprehensive README.md documenting the new structure
- Moved OAuth credentials to secure `00_ADMIN/` folder
- Aligned folder structure with actual operational workflows

**New Structure:**
- `00_ADMIN/` - Project administration and credentials
- `01_BUSINESS_STRATEGY/` - Core business documents
- `02_MARKET_INTEL/` - Market research and keyword data
- `03_CLINICAL_OPERATIONS/` - Clinical protocols and consumables
- `04_PATIENT_EXPERIENCE/` - Patient journey and intake
- `05_STAFFING/` - HR and onboarding
- `06_MARKETING_GROWTH/` - Marketing strategy and Google Ads
- `07_TECH_STACK/` - Tech integrations and data
- `08_OPERATIONS_PLAYBOOK/` - Operational procedures
- `09_MEETINGS_LOGS/` - Meeting records
- `archive/` - Historical files

**Benefits:**
- Clearer separation of clinical vs operational documents
- Easier navigation for staff onboarding
- Better alignment with Google Drive sync structure
- Improved security for sensitive credentials

### Google Drive Full Sync & OAuth Setup (2026-04-21)
**Status:** COMPLETED
**Category:** Infrastructure/Integration

**Achievements:**
- ✅ Configured full OAuth 2.0 authentication with Google Workspace
- ✅ Obtained scopes: Drive (full), Gmail, Calendar, Sheets, Docs, Contacts
- ✅ Uploaded 34 files to Google Drive with organized folder structure
- ✅ Created sync script (`reliable_sync.py`) for future updates
- ✅ Drive folder: https://drive.google.com/drive/folders/1i0J2ICnGAbcPAqiFSS1RFyMT10kfSLjO

**Technical Details:**
- Client ID: `637011530953-a80m8p8p3qaaj0mbur47fk3it3m2su9q`
- Token location: `~/.hermes/google_token.json` (auto-refreshing)
- Sync time: 63.6 seconds for 34 files
- All subfolders created: protocols, consumables, google_ads, integrations, keyword_data, legacy_scripts

**Next Steps Enabled:**
- Automated GHL → Sheets webhook integration
- Patient intake workflow automation
- Dashboard auto-sync scripts
- Automated backup routines

---

## Issue Resolution Log

### Mixpanel Integration Updates (2026-05-02)
- Disabled JWT verification for Edge Function `fetch_mixpanel_events`.
- Patched function to use Unix‑timestamp range parameters.
- Switched Mixpanel Export API authentication to query‑string (`api_key`/`api_secret`).
- Redeployed function (no‑verify‑jwt) and verified non‑zero fetch count.
- Updated documentation in `mixpanel_troubleshooting.md`.

### Issue: Google Ads Campaign - Broken CTA Modal (2026-04-21)
**Status:** RESOLVED
**Category:** Technical/Marketing

**Problem:**
- Google Ads Ayurveda campaign generated 80+ clicks with 0 leads
- Root cause: Primary CTA "Book an Ayurvedic Assessment" modal was non-functional
- First-time client booking link was broken/not deploying correctly

**Impact:**
- ~80 potential leads lost due to broken conversion path
- Good CPC (cost per click) but zero conversion rate

**Resolution:**
- User identified and fixed the technical issue with booking link and modal deployment
- GHL calendar integration restored

**Prevention:**
- Recommend pre-launch QA checklist: Test all CTAs on mobile/desktop before campaign launch
- Implement UTM tracking on GHL calendar links for campaign attribution
- Set up monthly QA review of critical conversion paths
