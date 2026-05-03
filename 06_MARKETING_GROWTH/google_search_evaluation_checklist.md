# Google Search Campaign Evaluation Checklist for Odin Labs

## Success Metrics (KPIs)
- Primary: Cost‑Per‑Lead (CPL) / Cost‑Per‑Acquisition (CPA)
- Secondary: Click‑Through Rate (CTR), Conversion Rate (CVR), Quality Score, Impression Share, Search Term Relevance

## Step‑by‑Step Process
1. **Define Success Metrics**
   - Target CPL ≤ $95 CAD (≈ $70 USD) – based on WordStream health‑industry CPA.
   - CTR ≥ 3 % (health benchmark).
   - CVR ≥ 4 % (healthy conversion floor).
2. **Set Up Tracking**
   - Google Ads conversion tracking (GHL webhook → Google Sheet).
   - UTM parameters on landing‑page URLs.
3. **Establish Baseline (Learning Phase)**
   - Run at least 48 h.
   - Collect **200‑300 clicks per ad group** before judging performance.
4. **Compute Core Metrics**
   - CPL = Spend ÷ Leads.
   - CTR = Clicks ÷ Impressions.
   - CVR = Leads ÷ Clicks.
   - Quality Score (expected CTR + ad relevance + landing‑page experience).
5. **Diagnose Gaps**
   - Low CTR → refine keywords, improve ad copy, add negatives.
   - Low CVR → test landing‑page copy, form length, CTA, page speed.
   - High CPL → adjust bids, pause under‑performing keywords.
6. **Run Controlled A/B Test**
   - Change ONE variable (headline, CTA, landing page).
   - Equal budget to control & variant.
   - Aim for **≥ 100 conversions per variant** (≈ 500 clicks) for 95 % confidence.
7. **Review & Roll Out**
   - Compare CPL, CVR, ROI.
   - Deploy variant if CPL improves ≥ 10 % with statistical significance.
8. **Ongoing Monitoring**
   - Automated rules: pause keywords with CPA > 1.5× target after 100 clicks.
   - Weekly search‑term reports → add negatives.
   - Refresh ad copy every 2‑3 weeks.

## Click Thresholds
| Scenario | Minimum Clicks | Reason |
|----------|----------------|--------|
| Initial Learning Phase | 200‑300 clicks per ad group | Gives Google enough data to exit learning; statistically meaningful CVR estimate (±~2 %). |
| A/B Test of One Variable | ~500 clicks total (≈250 per variant) → ~100+ conversions per variant | Provides 95 % confidence interval ± 9 % on conversion rate. |
| Small‑Scale Optimization | 100‑150 clicks (5‑8 conversions) | Acceptable margin of error for narrow changes. |
| Full‑Scale Scaling | ≥ 1,000 clicks (≈50+ conversions) | Reduces CPL variance (< 5 % of mean) before increasing budget. |

## Quick Success‑Check Spreadsheet Template
| Date | Campaign | Ad Group | Impr. | Clicks | Spend (CAD) | Leads | CPL (CAD) | CTR % | CVR % | Quality Score | Status |
|------|----------|----------|------|--------|------------|-------|-----------|-------|------|----------------|--------|
|      |          |          |      |        |            |       |           |       |      |                |        |

---
*All benchmark data sourced from WordStream 2025 Google Ads & Facebook Ads reports and LocalIQ 2025 SMB marketing trends.*
