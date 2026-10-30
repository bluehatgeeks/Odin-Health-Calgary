// usage (from /workspace/hp-test): node /workspace/pages/_shared/test-tracking.js <slug>
// Clicks EVERY [data-cta] element plus the booking trigger with a stubbed window.mixpanel and asserts each fires 'CTA Click'.
// Also: static guard against a function/var named `track`, JSON-LD / FAQ parity, meta equals seo-meta.md, links.
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const slug = process.argv[2];
const xf = require('/workspace/pages/_shared/xfollow-footer.js');
const PAGE = slug === '_home' ? 'home' : slug; // value of PAGE inside the page script (the home page is built as _home)
const file = `/workspace/pages/${slug}/page.html`;
const src = fs.readFileSync(file, 'utf8');
const seo = fs.readFileSync('/workspace/homepage/seo-meta.md', 'utf8');
const sec = seo.split(/\n## /).find(s => slug === '_home' ? /`\/`/.test(s) : new RegExp('`/' + slug + '`').test(s));
const wantTitle = sec.match(/- Title \(\d+\): (.*)/)[1].trim();
const wantDesc = sec.match(/- Description \(\d+\): (.*)/)[1].trim();
const results = {};
const ok = (k, v, detail) => { results[k] = v ? 'PASS' : 'FAIL' + (detail ? ' ' + detail : ''); };
(async () => {
  ok('no function/var/let/const named track', !/(function\s+track\s*\(|\b(var|let|const)\s+track\b|\btrack\s*=\s*function)/.test(src.replace(/mixpanel\.track/g, '')));
  ok('has function trackCta', /function trackCta\(/.test(src));
  ok('has function trackBookingLink', /function trackBookingLink\(/.test(src));
  ok('click handler is a capture-phase document listener (fires before navigation, incl. target=_blank links)', /document\.addEventListener\('click', function \(e\) \{[\s\S]*?\}, true\);/.test(src));
  ok('has ai_referrer register', /ai_referrer/.test(src) && /mixpanel\.register/.test(src));
  const b = await puppeteer.launch({ executablePath: '/usr/bin/google-chrome', headless: 'new', args: ['--no-sandbox'] });
  const p = await b.newPage(); await xf.serveFooter(p, slug); await p.setViewport({ width: 1280, height: 800 });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.evaluateOnNewDocument(() => { window.__ev = []; window.__reg = []; window.mixpanel = { track: (n, props) => window.__ev.push([n, props]), register: (props) => window.__reg.push(props) }; });
  await p.goto('file://' + file, { waitUntil: 'networkidle0' });
  await p.evaluate(() => { document.addEventListener('click', e => { const a = e.target.closest('a'); if (a && a.getAttribute('href') !== '#') e.preventDefault(); }, false); });
  const ctas = await p.evaluate(() => [...document.querySelectorAll('[data-cta]')].map(e => e.getAttribute('data-cta')));
  ok('every data-cta unique', new Set(ctas).size === ctas.length);
  // ── X follow line (Alex approved via Odin X Marketer): footer on EVERY maintained page, end-of-article line on the answer pages only ──
  const XHREF = 'https://x.com/intent/follow?screen_name=odinhealthlab', XTEXT = 'Follow Odin Health Lab on X for the daily research breakdowns.', XTEXT_OLD = 'Follow Odin Labs on X for the daily research breakdowns.'; // lnk1030: brand rule 'Odin Health Lab'; old text accepted until all pages are migrated
  const NO_END = ['_home', 'shift', 'privacy', 'functional-health', 'health-coaching', 'supplements', 'ayurveda'];
  const xinfo = await p.evaluate(() => [...document.querySelectorAll('a[data-cta^="x_follow_"]')].map(a => { const r = a.getBoundingClientRect(); const cs = getComputedStyle(a);
    return { cta: a.getAttribute('data-cta'), href: a.getAttribute('href'), target: a.getAttribute('target'), rel: a.getAttribute('rel'), text: a.textContent.trim(), w: r.width, h: r.height, vis: !!(a.offsetParent) && cs.visibility !== 'hidden' && r.width > 0,
      inMain: !!a.closest('main'), inFooter: !!a.closest('.odin-footer'), lastInMain: a.closest('main') ? (a.closest('main').lastElementChild === a.parentElement || [...a.closest('main').children].slice(-2).includes(a.parentElement)) : null, hasSvg: !!a.querySelector('svg[aria-hidden="true"]') }; }));
  const xf1 = xinfo.filter(x => x.cta === 'x_follow_footer'), xe = xinfo.filter(x => x.cta === 'x_follow_end');
  const goodX = x => x.href === XHREF && x.target === '_blank' && x.rel === 'noopener noreferrer' && (x.text === XTEXT || x.text === XTEXT_OLD) && x.vis && x.hasSvg && !/owen-lowt/.test(x.href);
  ok('X follow: exactly one footer link x_follow_footer (in .odin-footer), href/target/rel/text exact, visible, icon aria-hidden', xf1.length === 1 && xf1[0].inFooter && goodX(xf1[0]), JSON.stringify(xf1));
  if (NO_END.includes(slug)) ok('X follow: NO end-of-article link on this page (footer only)', xe.length === 0, JSON.stringify(xe));
  else ok('X follow: exactly one end link x_follow_end inside <main>, last block, href/target/rel/text exact, visible', xe.length === 1 && xe[0].inMain && xe[0].lastInMain && goodX(xe[0]), JSON.stringify(xe));
  ok('X follow: no /owen-lowt in the X follow markup', !/owen-lowt/.test(JSON.stringify(xinfo)));
  const fired = [];
  for (const c of ctas) {
    await p.evaluate(() => { window.__ev.length = 0; });
    await p.evaluate(c => { const e = document.querySelector(`[data-cta="${c}"]`); e.click(); }, c);
    const ev = await p.evaluate(() => window.__ev.slice());
    const ctaEv = ev.filter(e => e[0] === 'CTA Click');
    const good = ctaEv.length === 1 && ctaEv[0][1].cta === c && ctaEv[0][1].page === PAGE;
    fired.push([c, good]);
    // close the modal if a booking trigger opened it
    await p.evaluate(() => { const o = document.getElementById('booking-modal-overlay'); if (o.classList.contains('is-visible')) document.getElementById('booking-modal-close').click(); });
  }
  results['CTA clicks firing mixpanel.track (stub)'] = fired.filter(f => f[1]).length + '/' + fired.length + (fired.every(f => f[1]) ? ' PASS' : ' FAIL ' + fired.filter(f => !f[1]).map(f => f[0]).join(','));
  // Booking Link Clicked: modal first-time / follow-up links fire CTA Click AND Booking Link Clicked
  const bookingChecks = [];
  for (const [sel, expectBooking] of [
    ['[data-cta="modal_first_time"]', 'first_time'],
    ['[data-cta="modal_follow_up"]', 'follow_up'],
  ]) {
    await p.evaluate(() => { window.__ev.length = 0; });
    await p.evaluate(sel => { const e = document.querySelector(sel); if (e) e.click(); }, sel);
    const bev = await p.evaluate(() => window.__ev.slice());
    const hasCta = bev.some(e => e[0] === 'CTA Click');
    const bl = bev.find(e => e[0] === 'Booking Link Clicked');
    const good = hasCta && bl && bl[1].booking === expectBooking && bl[1].page === PAGE && typeof bl[1].cta === 'string';
    bookingChecks.push([expectBooking, good, JSON.stringify(bev)]);
    await p.evaluate(() => { const o = document.getElementById('booking-modal-overlay'); if (o && o.classList.contains('is-visible')) document.getElementById('booking-modal-close').click(); });
  }
  results['Booking Link Clicked on modal booking links'] = bookingChecks.filter(f => f[1]).length + '/' + bookingChecks.length + (bookingChecks.every(f => f[1]) ? ' PASS' : ' FAIL ' + bookingChecks.filter(f => !f[1]).map(f => f[0] + ':' + f[2]).join(' | '));

  // nav "Book Online" style trigger with no data-cta
  await p.evaluate(() => { window.__ev.length = 0; const d = document.createElement('a'); d.href = '#'; d.className = 'booking-trigger'; d.id = 'fake-nav-trigger'; document.body.appendChild(d); d.click(); });
  const ev2 = await p.evaluate(() => ({ ev: window.__ev.slice(), modal: document.getElementById('booking-modal-overlay').classList.contains('is-visible') }));
  ok('booking-trigger without data-cta tracked + modal opens', ev2.ev.length === 1 && ev2.ev[0][1].cta === 'book_online' && ev2.modal);
  // no mixpanel at all must not throw
  const p2 = await b.newPage(); await xf.serveFooter(p2, slug); const e2 = []; p2.on('pageerror', e => e2.push(e.message));
  await p2.goto('file://' + file, { waitUntil: 'networkidle0' });
  await p2.evaluate(() => { document.addEventListener('click', e => { const a = e.target.closest('a'); if (a) e.preventDefault(); }, false); (document.querySelector('[data-cta="hero_free_assessment"], [data-cta="hero_book_call"]') || document.querySelector('main [data-cta]')).click(); });
  ok('click with no mixpanel does not throw', e2.length === 0, e2.join('|'));
  const meta = await p.evaluate(() => { const q = (s, a) => (document.querySelector(s) || {}).getAttribute ? document.querySelector(s).getAttribute(a) : null;
    const j = JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent); const g = j['@graph']; const faq = g.find(x => x['@type'] === 'FAQPage');
    const dom = [...document.querySelectorAll('.faq-item')].map(d => [d.querySelector('.faq-question').textContent, d.querySelector('.faq-answer').textContent]);
    const links = [...document.querySelectorAll('main a[href]')].map(a => a.getAttribute('href'));
    return { title: document.title, desc: q('meta[name=description]', 'content'), ogt: q('meta[property="og:title"]', 'content'), ogd: q('meta[property="og:description"]', 'content'),
      twt: q('meta[name="twitter:title"]', 'content'), twd: q('meta[name="twitter:description"]', 'content'), canon: q('link[rel=canonical]', 'href'), ogu: q('meta[property="og:url"]', 'content'),
      types: g.map(x => x['@type']), nq: faq ? faq.mainEntity.length : 0, same: !faq ? dom.length === 0 : JSON.stringify(dom.map(d => d[0])) === JSON.stringify(faq.mainEntity.map(m => m.name)) && JSON.stringify(dom.map(d => d[1])) === JSON.stringify(faq.mainEntity.map(m => m.acceptedAnswer.text)),
      h1: document.querySelectorAll('h1').length, ids: [...document.querySelectorAll('[id]')].map(e => e.id).filter((x, i, a) => a.indexOf(x) !== i), links, assessHrefs: [...document.querySelectorAll('[data-cta]')].filter(a => /assessment/.test(a.getAttribute('data-cta'))).map(a => a.getAttribute('href')) }; });
  ok('title == seo-meta.md verbatim', meta.title === wantTitle, meta.title);
  ok('meta description == seo-meta.md verbatim', meta.desc === wantDesc);
  ok('og/twitter title+desc identical to title/desc', meta.ogt === wantTitle && meta.twt === wantTitle && meta.ogd === wantDesc && meta.twd === wantDesc);
  ok('title length', true); results['title length'] = meta.title.length + (meta.title.length <= 60 ? ' PASS' : ' (>60, verbatim from seo-meta.md; see NOTES)');
  ok('description <=160', meta.desc.length <= 160, meta.desc.length);
  ok('canonical + og:url', meta.canon === 'https://odinhealthlab.ca/' + slug && meta.ogu === meta.canon);
  // LEGAL=1 (e.g. /privacy): no FAQ by design, organization location "Calgary, Alberta, Canada" allowed, CTAs prefixed <slug>_
  const legal = process.env.LEGAL === '1';
  if (legal) {
    ok('JSON-LD has Organization, WebSite, WebPage, BreadcrumbList (legal page, no FAQPage)', ['Organization', 'WebSite', 'WebPage', 'BreadcrumbList'].every(t => meta.types.includes(t)) && !meta.types.includes('FAQPage'), meta.types.join(','));
    ok('legal page: no FAQ block (DOM and JSON-LD)', meta.nq === 0 && meta.same);
    const bad = ctas.filter(c => !c.startsWith(slug + '_') && !/^modal_/.test(c) && !/^x_follow_(footer|end)$/.test(c)); // x_follow_footer comes from the shared footer
    ok('every page CTA id prefixed ' + slug + '_ (shared booking modal excepted)', bad.length === 0, bad.join(','));
  } else {
  ok('JSON-LD has Organization, WebSite, WebPage, BreadcrumbList, FAQPage', ['Organization', 'WebSite', 'WebPage', 'BreadcrumbList', 'FAQPage'].every(t => meta.types.includes(t)));
  ok('FAQ 5-6 Qs and DOM text == JSON-LD text', meta.nq >= 5 && meta.nq <= 6 && meta.same, meta.nq);
  }
  ok('one h1', meta.h1 === 1);
  ok('no duplicate ids', meta.ids.length === 0, meta.ids.join(','));
  const need = ['https://odinhealthlab.ca/', 'https://odinhealthlab.ca/functional-health', 'https://odinhealthlab.ca/health-coaching', 'https://odinhealthlab.ca/supplements', 'https://odinhealthlab.ca/privacy'].filter(u => u !== 'https://odinhealthlab.ca/' + slug);
  ok('internal links present (home + siblings + privacy)', need.every(u => meta.links.includes(u)), need.filter(u => !meta.links.includes(u)).join(','));
  const noAssess = process.env.NO_ASSESS === '1';
  if (noAssess) ok('NO link to /owen-lowt (paid page) anywhere in the page, no assessment CTAs', !/owen-lowt/.test(src) && meta.assessHrefs.length === 0, meta.assessHrefs.join(','));
  else ok('assessment CTAs all -> /owen-lowt', meta.assessHrefs.length >= 4 && meta.assessHrefs.every(h => h === 'https://odinhealthlab.ca/owen-lowt'), meta.assessHrefs.length);
  if (legal) ok('Calgary only as the organization location ("Calgary, Alberta, Canada" / JSON-LD address)', !/calgary/i.test(src.replace(/Odin-Health-Calgary|odinlabcalgary|Calgary, Alberta, Canada|"addressLocality": "Calgary"/g, '')));
  else ok('no Calgary in-clinic wording in body', !/calgary/i.test(src.replace(/Odin-Health-Calgary|odinlabcalgary/g, '')));
  // Alex (2026-10-15): no disclaimer paragraphs or "Illustration only" captions on ANY page, so this check always runs
  ok('NO disclaimer paragraph / educational-only note / 911 / 988 / "Illustration only" caption (per Alex)', !/class="disclaimer"|call 911|\b988\b|illustration only|educational (information|only)|isn(&rsquo;|’|')t a diagnosis/i.test(src));
  ok('no pageerror', errs.length === 0, errs.join('|'));
  // ai_referrer: stub register + simulate perplexity referrer / chatgpt utm
  const pAi = await b.newPage(); await xf.serveFooter(pAi, slug);
  await pAi.evaluateOnNewDocument(() => {
    window.__reg = [];
    window.__ev = [];
    Object.defineProperty(document, 'referrer', { configurable: true, get: () => 'https://www.perplexity.ai/search?q=low+t' });
    window.mixpanel = {
      track: (n, props) => window.__ev.push([n, props]),
      register: (props) => window.__reg.push(props)
    };
  });
  await pAi.goto('file://' + file + '?utm_source=chatgpt', { waitUntil: 'networkidle0' });
  const ai = await pAi.evaluate(() => ({ reg: window.__reg.slice() }));
  ok('ai_referrer registered from utm_source or referrer', ai.reg.some(r => r && r.ai_referrer === 'chatgpt' || r && r.ai_referrer === 'perplexity'), JSON.stringify(ai.reg));
  await pAi.close();

  const banned = [/\bcure[sd]?\b/i, /\breverse/i, /\bguarantee/i, /\b\d+\s*(weeks?|months?|days?)\b/i, /\b\d+\s*%(?!\s*telehealth)/, /\bboost(s|ing)?\s+testosterone/i, /clinically proven|proven to/i];
  const text = src.replace(/<script[\s\S]*?<\/script>/g, '').replace(/<style[\s\S]*?<\/style>/g, '').replace(/<[^>]+>/g, ' ');
  const hits = banned.map(r => { const m = text.match(r); return m ? m[0] : null; }).filter(Boolean);
  results['banned-claim scan (cure/reverse/guarantee/N weeks/N%/boost testosterone/proven)'] = hits.length ? (legal ? 'INFO (legal text kept verbatim from live policy): ' : 'REVIEW: ') + hits.join(' | ') : 'PASS (0 hits)';
  console.log(JSON.stringify(results, null, 1));
  console.log('CTAs:', ctas.join(', '));
  await b.close();
})();
