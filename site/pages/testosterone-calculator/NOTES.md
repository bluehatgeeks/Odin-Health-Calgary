# CALC-HOWTO-1106 NOTES (stage only — NOT published)
America/Edmonton · Fri Nov 6 2026 ~10:35 AM

Handoff: `/workspace/odin-x/traffic-drafts/wm-handoff-calculator-issam-howto-2026-11-06.md`
SERP baselines: `/workspace/odin-x/serp/*-20261106-1030.json`

## Staged file
| file | bytes | md5 | lines |
|------|------:|-----|------:|
| testosterone-calculator-calc-howto-1106.txt | 155501 | `14714a5fdceef19ad9cba8a158ce82a1` | 1202 |

Mirrored to `/workspace/srv2/testosterone-calculator-calc-howto-1106.txt` → `http://127.0.0.1:8780/testosterone-calculator-calc-howto-1106.txt`.

### Base (100% match vs live Custom Code)
- `/workspace/cal-paa-1106/testosterone-calculator-cal-paa-1106.txt`
- md5 `afcd943c984513d7694494610f38294e` (149524 B)
- Live curl 2026-11-06: FAQ DOM 9 / HowTo false / title without brand pipe

### Deltas vs live
- Title / og / twitter / WebPage name → `ISSAM Calculator: Free & Bioavailable Testosterone | Odin Health Lab` (HTML attrs use `&amp;`)
- Meta / og:description / twitter:description / JSON descriptions → handoff CTR meta (146 chars)
- Visible H2 + lead + `<ol class="q-list">` 5 steps + source line under `#fc` (`#howto-issam`)
- HowTo JSON-LD 5 HowToStep; step `text` == visible (tag-stripped) word-for-word
- FAQ #1 + #2 DOM + FAQPage JSON-LD (existing 9 kept → **11==11**)
- Article `dateModified` → `2026-11-06`
- Source URL: `https://www.issam.ch/freetesto.htm` (both .htm and .html 200; handoff FAQ uses .htm)
- Kept: calculator widget, tracking, CTAs, `#1a3a1a`, motion, `calc_help_calgary_link`, `id="embed"`, `calc_embed_copy`, booking markers
- Pure ASCII / HTML entities (no mojibake)

### Conflict note
- `/workspace/isscalc1106/` was an earlier unpublished prep (different 3-step HowTo + 1 FAQ; title unchanged). **Superseded** by CALC-HOWTO-1106. Do not paste isscalc1106.
- `/workspace/pages/testosterone-calculator/page.html` previously mirrored isscalc1106; now overwritten with this pack (+ `.bak-calc-howto-1106`).

### Verify
```
python3 /workspace/calc-howto-1106/verify.py          # staged ALL PASS
python3 /workspace/calc-howto-1106/verify.py --live   # expect FAIL on new markers until publish
```

### Do NOT (this ticket)
- Publish to GHL / JumpConvert
- IndexNow / Indexing API
- Edit x-ghl-daily.md
- Message anyone / change booking / calendars / hours / [Paid] pages
- Parent asks Alex before live
