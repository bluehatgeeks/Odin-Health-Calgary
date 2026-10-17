// usage: node test-xfollow-footer.js <slug>   (slug _home = homepage). Footer-only check at 1280 and 390 with the STAGED footer: link visible, inside viewport, no horizontal overflow, <=3 lines, screenshot.
// Negative mode: FOOTER_PATH=/owen-lowt node test-xfollow-footer.js <slug>  -> the X line must stay HIDDEN (paid pages share the footer).
const puppeteer = require('puppeteer-core'); const xf = require('/workspace/pages/_shared/xfollow-footer.js');
const sleep = ms => new Promise(r => setTimeout(r, ms)); const slug = process.argv[2];
const file = slug === '_home' ? '/workspace/homepage/home.html' : `/workspace/pages/${slug}/page.html`;
(async () => {
  const b = await puppeteer.launch({ executablePath: '/usr/bin/google-chrome', headless: 'new', args: ['--no-sandbox'] }); const res = { slug, negative: !!process.env.FOOTER_PATH };
  for (const w of [1280, 390]) {
    const p = await b.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await xf.serveFooter(p, slug); await p.setViewport({ width: w, height: w === 390 ? 760 : 800 });
    await p.goto('file://' + file, { waitUntil: 'networkidle0' }); await sleep(600);
    await p.evaluate(() => window.scrollTo(0, document.body.scrollHeight)); await sleep(1200);
    const m = await p.evaluate(() => { const a = document.querySelector('a[data-cta="x_follow_footer"]'); if (!a) return { present: false }; const r = a.getBoundingClientRect(); const sp = a.querySelector('span').getBoundingClientRect(); const lh = parseFloat(getComputedStyle(a).lineHeight);
      return { present: true, hiddenAttr: a.parentElement.hidden, visible: !!a.offsetParent && r.width > 0, inside: r.left >= 0 && r.right <= innerWidth, w: Math.round(r.width), h: Math.round(r.height), lines: Math.round(sp.height / lh), sw: document.documentElement.scrollWidth, iw: innerWidth, href: a.href, target: a.target, rel: a.rel, count: document.querySelectorAll('a[data-cta^="x_follow_"]').length }; });
    res[w] = { ...m, errs: errs.filter(e => !/Failed to load resource/.test(e)) };
    if (!process.env.FOOTER_PATH) await p.screenshot({ path: `/tmp/xt/footer-${slug}-${w}.png` });
    await p.close();
  }
  const pos = !process.env.FOOTER_PATH;
  const good = w => pos ? (res[w].present && res[w].visible && res[w].inside && res[w].sw === res[w].iw && res[w].lines <= 3 && res[w].count === 1 && res[w].target === '_blank' && res[w].rel === 'noopener noreferrer' && !res[w].errs.length) : (res[w].present && !res[w].visible && res[w].hiddenAttr === true);
  res.verdict = (good(1280) && good(390)) ? 'PASS' : 'FAIL'; console.log(JSON.stringify(res)); await b.close();
})();
