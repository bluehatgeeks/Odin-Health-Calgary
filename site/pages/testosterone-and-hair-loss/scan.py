"""Banned-word scan for /testosterone-and-hair-loss (per Alex's standing rules). Run: python3 scan.py"""
import re, html, sys
p = sys.argv[1] if len(sys.argv) > 1 else '/workspace/pages/testosterone-and-hair-loss/page.html'
src = open(p, encoding='utf-8').read()
res = {}
res['prefers-reduced-motion: no-preference queries'] = len(re.findall(r'@media[^{]*prefers-reduced-motion\s*:\s*no-preference', src))
res['var reduce = false'] = 'var reduce = false' in src
res['/owen-lowt'] = src.count('owen-lowt')
body = re.sub(r'<script(?![^>]*ld\+json)[^>]*>[\s\S]*?</script>', '', src)
body = re.sub(r'<style[\s\S]*?</style>', '', body)
text_all = html.unescape(re.sub(r'<[^>]+>', ' ', body))
banned = {'physician-aware': r'physician[- ]aware', 'not a treatment': r'not a (medical )?treatment', 'not medical advice': r'not (medical|health) advice',
          'disclaimer': r'disclaim', 'illustration only': r'illustration only', 'PEMF': r'\bPEMF\b|electromagnetic', 'hydrogen': r'hydrogen', 'marma': r'marma',
          'Calgary': r'calgary'}
for k, r in banned.items():
    res[k] = [m.group(0) for m in re.finditer(r, re.sub(r'Odin-Health-Calgary|odinlabcalgary', '', text_all), re.I)]
# doctor words: only allowed inside the doctor FAQ (DOM <details> and its JSON-LD Question)
doc = r'\b(doctors?|physicians?|clinicians?|urologists?|endocrinologists?|GPs?|prescrib\w*|diagnos\w*|healthcare providers?|medical providers?)\b'
dom = re.sub(r'<details class="faq-item">\s*<summary><span class="faq-question">How does Odin Health Labs work with my doctor\?</span>[\s\S]*?</details>', '', body)
dom = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>', '', dom)
t = html.unescape(re.sub(r'<[^>]+>', ' ', dom))
res['doctor words outside doctor FAQ (DOM)'] = [t[max(0, m.start()-50):m.end()+30] for m in re.finditer(doc, t, re.I)]
ld = re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>', src).group(1)
import json
g = json.loads(ld)['@graph']
faq = [x for x in g if x['@type'] == 'FAQPage'][0]['mainEntity']
ldtext = ' '.join(json.dumps(x, ensure_ascii=False) for x in g if x['@type'] != 'FAQPage') + ' ' + ' '.join(q['name'] + ' ' + q['acceptedAnswer']['text'] for q in faq if 'my doctor' not in q['name'])
res['doctor words outside doctor FAQ (JSON-LD)'] = re.findall(doc, ldtext, re.I)
# test-tracking banned claims (same regexes)
text = re.sub(r'<[^>]+>', ' ', re.sub(r'<style[\s\S]*?</style>', '', re.sub(r'<script[\s\S]*?</script>', '', src)))
claims = [r'\bcure[sd]?\b', r'\breverse', r'\bguarantee', r'\b\d+\s*(weeks?|months?|days?)\b', r'\b\d+\s*%(?!\s*telehealth)', r'\bboost(s|ing)?\s+testosterone', r'clinically proven|proven to']
res['banned claims'] = [m.group(0) for r in claims for m in [re.search(r, text, re.I)] if m]
for k, v in res.items(): print(k, ':', v)
bad = res['prefers-reduced-motion: no-preference queries'] or not res['var reduce = false'] or res['/owen-lowt'] or any(res[k] for k in banned) or res['doctor words outside doctor FAQ (DOM)'] or res['doctor words outside doctor FAQ (JSON-LD)'] or res['banned claims']
print('SCAN', 'FAIL' if bad else 'PASS (0 hits)')
