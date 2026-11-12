# /trt-cost-canada-vs-usa labc1112 (Labcorp OnDemand price, 12 November 2026)

Alex approved in his own words on 12 November 2026 at 1:08 PM America/Edmonton: "Fix the Labcorp price on the cost page."

Rechecked the same Labcorp OnDemand product page on 12 November 2026: https://www.ondemand.labcorp.com/lab-tests/comprehensive-testosterone-test shows **$159** only. The $119.25 sale price is gone.

Changes in Custom Code only (SEO title/description untouched):
- Lead paragraph under US cash labs: removed "on sale for $119.25 when checked"; Labcorp panel remains $159. The "prices (October 2026)" parenthetical in that same sentence is now "prices (November 2026)" because Quest and Labcorp in that sentence were rechecked today (Quest figures unchanged).
- Labcorp OnDemand source line: checked date set to November 12, 2026.
- Article JSON-LD dateModified: 2026-11-02 -> 2026-11-12.

Base: /workspace/srv2/trt-cost-canada-vs-usa-calc-issam-1106.txt (md5 430cfea55c71127cdfe896637dd1d72d), which matches live HTML line-for-line before this edit (0 missing). Table cell "Labcorp panel with albumin $159 list" was already correct and was left alone. Other source "checked October 16, 2026" dates were left alone; those figures still matched the 12 November 2026 price recheck.

GHL: step 9e476302-ad04-4818-84b4-fb83868adc6e / builder pVNKIefQeQySu4afR9rk. Custom Code only. Do not touch booking, Header Tracking, [Paid] pages, or /owen-lowt.

After publish: python3 /workspace/labc1112/verify.py (expect ALL PASS); then python3 /workspace/labc1112/ping.py (Indexing API URL_UPDATED 200 + IndexNow 202). GitHub mirror from /workspace/ghsync-labc1112.tar.gz on bluehatgeeks/Odin-Health-Calgary; squash-merge when the PR opens.
