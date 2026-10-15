// usage (from /workspace/hp-test): node /workspace/pages/_shared/test-tracking.js <slug>
// Clicks EVERY [data-cta] element plus the booking trigger with a stubbed window.mixpanel and asserts each fires 'CTA Click'.
// Also: static guard against a function/var named `track`, JSON-LD / FAQ parity, meta equals seo-meta.md, links.
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const slug = process.argv[2];
const file = `/workspace/pages/${slug}/page.html`;
const src = fs.readFileSync(file, 'utf8');
const seo = fs.readFileSync('/workspace/homepage/seo-meta.md', 'utf8');
const sec = seo.split(/\n## /).find(s => new RegExp('`/' + slug + '`').test(s));
const wantTitle = sec.match(/- Title \(\d+\): (.*)/)[1].trim();
const wantDesc = sec.match(/- Description \(\d+\): (.*)/)[1].trim();
const results = {};
const ok = (k, v, detail) => { results[k] = v ? 'PASS' : 'FAIL' + (detail ? ' ' + detail : ''); };
(async () => {
  ok('no function/var/let/const named track', !/(function\s+track\s*\(|\b(var|let|const)\s+track\b|\btrack\s*=\s*function)/.test(src.replace(/mixpanel\.track/g, '')));
  ok('has function trackCta', /function trackCta\(/.test(src));
  const b = await puppeteer.launch({ executablePath: '/usr/bin/google-chrome', headless: 'new', args: ['--no-sandbox'] });
  const p = await b.newPage(); await p.setViewport({ width: 1280, height: 800 });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.evaluateOnNewDocument(() => { window.__ev = []; window.mixpanel = { track: (n, props) => window.__ev.push([n, props]) }; });
  await p.goto('file://' + file, { waitUntil: 'networkidle0' });
  await p.evaluate(() => { document.addEventListener('click', e => { const a = e.target.closest('a'); if (a && a.getAttribute('href') !== '#') e.preventDefault(); }, false); });
  const ctas = await p.evaluate(() => [...document.querySelectorAll('[data-cta]')].map(e => e.getAttribute('data-cta')));
  ok('every data-cta unique', new Set(ctas).size === ctas.length);
  const fired = [];
  for (const c of ctas) {
    await p.evaluate(() => { window.__ev.length = 0; });
    await p.evaluate(c => { const e = document.querySelector(`[data-cta="${c}"]`); e.click(); }, c);
    const ev = await p.evaluate(() => window.__ev.slice());
    const good = ev.length === 1 && ev[0][0] === 'CTA Click' && ev[0][1].cta === c && ev[0][1].page === slug;
    fired.push([c, good]);
    // close the modal if a booking trigger opened it
    await p.evaluate(() => { const o = document.getElementById('booking-modal-overlay'); if (o.classList.contains('is-visible')) document.getElementById('booking-modal-close').click(); });
  }
  results['CTA clicks firing mixpanel.track (stub)'] = fired.filter(f => f[1]).length + '/' + fired.length + (fired.every(f => f[1]) ? ' PASS' : ' FAIL ' + fired.filter(f => !f[1]).map(f => f[0]).join(','));
  // nav "Book Online" style trigger with no data-cta
  await p.evaluate(() => { window.__ev.length = 0; const d = document.createElement('a'); d.href = '#'; d.className = 'booking-trigger'; d.id = 'fake-nav-trigger'; document.body.appendChild(d); d.click(); });
  const ev2 = await p.evaluate(() => ({ ev: window.__ev.slice(), modal: document.getElementById('booking-modal-overlay').classList.contains('is-visible') }));
  ok('booking-trigger without data-cta tracked + modal opens', ev2.ev.length === 1 && ev2.ev[0][1].cta === 'book_online' && ev2.modal);
  // no mixpanel at all must not throw
  const p2 = await b.newPage(); const e2 = []; p2.on('pageerror', e => e2.push(e.message));
  await p2.goto('file://' + file, { waitUntil: 'networkidle0' });
  await p2.evaluate(() => { document.addEventListener('click', e => { const a = e.target.closest('a'); if (a) e.preventDefault(); }, false); document.querySelector('[data-cta="hero_free_assessment"], [data-cta="hero_book_call"]').click(); });
  ok('click with no mixpanel does not throw', e2.length === 0, e2.join('|'));
  const meta = await p.evaluate(() => { const q = (s, a) => (document.querySelector(s) || {}).getAttribute ? document.querySelector(s).getAttribute(a) : null;
    const j = JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent); const g = j['@graph']; const faq = g.find(x => x['@type'] === 'FAQPage');
    const dom = [...document.querySelectorAll('.faq-item')].map(d => [d.querySelector('.faq-question').textContent, d.querySelector('.faq-answer').textContent]);
    const links = [...document.querySelectorAll('main a[href]')].map(a => a.getAttribute('href'));
    return { title: document.title, desc: q('meta[name=description]', 'content'), ogt: q('meta[property="og:title"]', 'content'), ogd: q('meta[property="og:description"]', 'content'),
      twt: q('meta[name="twitter:title"]', 'content'), twd: q('meta[name="twitter:description"]', 'content'), canon: q('link[rel=canonical]', 'href'), ogu: q('meta[property="og:url"]', 'content'),
      types: g.map(x => x['@type']), nq: faq.mainEntity.length, same: JSON.stringify(dom.map(d => d[0])) === JSON.stringify(faq.mainEntity.map(m => m.name)) && JSON.stringify(dom.map(d => d[1])) === JSON.stringify(faq.mainEntity.map(m => m.acceptedAnswer.text)),
      h1: document.querySelectorAll('h1').length, ids: [...document.querySelectorAll('[id]')].map(e => e.id).filter((x, i, a) => a.indexOf(x) !== i), links, assessHrefs: [...document.querySelectorAll('[data-cta]')].filter(a => /assessment/.test(a.getAttribute('data-cta'))).map(a => a.getAttribute('href')) }; });
  ok('title == seo-meta.md verbatim', meta.title === wantTitle, meta.title);
  ok('meta description == seo-meta.md verbatim', meta.desc === wantDesc);
  ok('og/twitter title+desc identical to title/desc', meta.ogt === wantTitle && meta.twt === wantTitle && meta.ogd === wantDesc && meta.twd === wantDesc);
  ok('title length', true); results['title length'] = meta.title.length + (meta.title.length <= 60 ? ' PASS' : ' (>60, verbatim from seo-meta.md; see NOTES)');
  ok('description <=160', meta.desc.length <= 160, meta.desc.length);
  ok('canonical + og:url', meta.canon === 'https://odinhealthlab.ca/' + slug && meta.ogu === meta.canon);
  ok('JSON-LD has Organization, WebSite, WebPage, BreadcrumbList, FAQPage', ['Organization', 'WebSite', 'WebPage', 'BreadcrumbList', 'FAQPage'].every(t => meta.types.includes(t)));
  ok('FAQ 5-6 Qs and DOM text == JSON-LD text', meta.nq >= 5 && meta.nq <= 6 && meta.same, meta.nq);
  ok('one h1', meta.h1 === 1);
  ok('no duplicate ids', meta.ids.length === 0, meta.ids.join(','));
  const need = ['https://odinhealthlab.ca/', 'https://odinhealthlab.ca/functional-health', 'https://odinhealthlab.ca/health-coaching', 'https://odinhealthlab.ca/supplements', 'https://odinhealthlab.ca/privacy'].filter(u => u !== 'https://odinhealthlab.ca/' + slug);
  ok('internal links present (home + siblings + privacy)', need.every(u => meta.links.includes(u)), need.filter(u => !meta.links.includes(u)).join(','));
  const noAssess = process.env.NO_ASSESS === '1';
  if (noAssess) ok('NO link to /owen-lowt (paid page) anywhere in the page, no assessment CTAs', !/owen-lowt/.test(src) && meta.assessHrefs.length === 0, meta.assessHrefs.join(','));
  else ok('assessment CTAs all -> /owen-lowt', meta.assessHrefs.length >= 4 && meta.assessHrefs.every(h => h === 'https://odinhealthlab.ca/owen-lowt'), meta.assessHrefs.length);
  ok('no Calgary in-clinic wording in body', !/calgary/i.test(src.replace(/Odin-Health-Calgary|odinlabcalgary/g, '')));
  if (noAssess) ok('NO disclaimer paragraph / educational-only note / 911 / 988 / "Illustration only" caption (per Alex)', !/class="disclaimer"|call 911|\b988\b|illustration only|educational (information|only)|isn(&rsquo;|’|')t a diagnosis/i.test(src));
  else ok('disclaimer has 911 and 988', /call 911/.test(src) && /988/.test(src));
  ok('no pageerror', errs.length === 0, errs.join('|'));
  const banned = [/\bcure[sd]?\b/i, /\breverse/i, /\bguarantee/i, /\b\d+\s*(weeks?|months?|days?)\b/i, /\b\d+\s*%(?!\s*telehealth)/, /\bboost(s|ing)?\s+testosterone/i, /clinically proven|proven to/i];
  const text = src.replace(/<script[\s\S]*?<\/script>/g, '').replace(/<style[\s\S]*?<\/style>/g, '').replace(/<[^>]+>/g, ' ');
  const hits = banned.map(r => { const m = text.match(r); return m ? m[0] : null; }).filter(Boolean);
  results['banned-claim scan (cure/reverse/guarantee/N weeks/N%/boost testosterone/proven)'] = hits.length ? 'REVIEW: ' + hits.join(' | ') : 'PASS (0 hits)';
  console.log(JSON.stringify(results, null, 1));
  console.log('CTAs:', ctas.join(', '));
  await b.close();
})();
