const puppeteer = require('puppeteer-core');
(async () => {
  const b = await puppeteer.launch({ executablePath: '/usr/bin/google-chrome', headless: 'new', args: ['--no-sandbox'] });
  const p = await b.newPage(); await p.setViewport({ width: 1280, height: 800 });
  await p.evaluateOnNewDocument(() => { window.__ev = []; window.mixpanel = { track: (n, props) => window.__ev.push([n, props]) }; });
  await p.goto('file:///workspace/pages/functional-health/page.html', { waitUntil: 'networkidle0' });
  await p.evaluate(() => { document.addEventListener('click', e => { const a = e.target.closest('a'); if (a && a.getAttribute('href') !== '#') e.preventDefault(); }, false); });
  for (const c of ['hero_free_assessment','hero_our_approach','related_health_coaching','related_supplements','related_home']) {
    await p.evaluate(c => document.querySelector(`[data-cta="${c}"]`).click(), c);
  }
  await p.evaluate(() => document.querySelector('.booking-trigger').click());
  const r = await p.evaluate(() => ({ ev: window.__ev, modal: document.getElementById('booking-modal-overlay').classList.contains('is-visible') }));
  console.log(JSON.stringify(r));
  const ld = await p.evaluate(() => { const j = JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent); const g = j['@graph']; const faq = g.find(x => x['@type']==='FAQPage'); const dom = [...document.querySelectorAll('.faq-item')].map(d => d.querySelector('.faq-question').textContent); return { types: g.map(x=>x['@type']), q: faq.mainEntity.length, same: JSON.stringify(dom) === JSON.stringify(faq.mainEntity.map(m=>m.name)), canon: document.querySelector('link[rel=canonical]').href, title: document.title.length, h1: document.querySelectorAll('h1').length, ids: [...document.querySelectorAll('[id]')].map(e=>e.id).filter((x,i,a)=>a.indexOf(x)!==i) }; });
  console.log(JSON.stringify(ld));
  await b.close();
})();
