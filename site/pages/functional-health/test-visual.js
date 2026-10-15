const puppeteer = require('puppeteer-core');
const path = '/workspace/pages/functional-health/page.html';
const out = '/workspace/pages/functional-health/shots/';
const SECS = [['hero','.mg--hero'],['cmp','.mg--cmp'],['lev','.mg--lev'],['loop','.mg--loop'],['lab','.mg--lab'],['how','[data-timeline]'],['rel','.mg--rel'],['faq','.faq-head'],['fin','.mg--fin']];
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  const browser = await puppeteer.launch({ executablePath: '/usr/bin/google-chrome', headless: 'new', args: ['--no-sandbox'] });
  const res = {};
  for (const w of [1280, 390]) {
    const page = await browser.newPage();
    await page.setViewport({ width: w, height: w === 390 ? 844 : 800, deviceScaleFactor: 1 });
    const errs = [];
    page.on('console', m => { if (['error','warning'].includes(m.type())) errs.push(m.type()+': '+m.text()); });
    page.on('pageerror', e => errs.push('pageerror: ' + e.message));
    page.on('requestfailed', r => errs.push('reqfailed: ' + r.url()));
    await page.evaluateOnNewDocument(() => { window.__cls = 0; new PerformanceObserver(l => { for (const e of l.getEntries()) if (!e.hadRecentInput) window.__cls += e.value; }).observe({ type: 'layout-shift', buffered: true }); });
    await page.goto('file://' + path, { waitUntil: 'networkidle0' });
    await sleep(800);
    await page.screenshot({ path: `${out}top-${w}.png` });
    for (const [k, sel] of SECS) {
      await page.evaluate(s => { const e = document.querySelector(s); const r = e.getBoundingClientRect(); window.scrollTo(0, window.scrollY + r.top - 120); }, sel);
      await sleep(1800);
      const el = await page.$(sel);
      await el.screenshot({ path: `${out}${k}-${w}-a.png` });
      await sleep(3200);
      await el.screenshot({ path: `${out}${k}-${w}-b.png` });
    }
    const m = await page.evaluate(() => ({
      cls: window.__cls, sw: document.documentElement.scrollWidth, iw: innerWidth, bsw: document.body.scrollWidth,
      running: document.getAnimations().filter(a => a.playState === 'running').length,
      total: document.getAnimations().length, paused: document.querySelectorAll('.is-paused').length,
      figs: document.querySelectorAll('.mg').length,
      overflowEls: [...document.querySelectorAll('main *')].filter(e => { const r = e.getBoundingClientRect(); return r.right > innerWidth + 1 && !e.closest('svg') && getComputedStyle(e).position !== 'fixed'; }).map(e => e.tagName+'.'+e.className).slice(0,8),
    }));
    res[w] = { ...m, errs };
    await page.screenshot({ path: `${out}full-${w}.png`, fullPage: true });
    await page.evaluate(() => window.scrollTo(0, 0)); await sleep(700);
    res[w].runningOffscreen = await page.evaluate(() => document.getAnimations().filter(a => a.playState === 'running' && a.effect && a.effect.target && a.effect.target.closest && a.effect.target.closest('.mg--cmp, .mg--lev, .mg--loop, .mg--lab, .mg--rel, .mg--fin, .faq-head, [data-timeline]')).length);
    // click test
    res[w].ctaCount = await page.evaluate(() => document.querySelectorAll('[data-cta]').length);
    await page.close();
    const p2 = await browser.newPage();
    await p2.setViewport({ width: w, height: 800 });
    await p2.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }]);
    await p2.goto('file://' + path, { waitUntil: 'networkidle0' }); await sleep(800);
    res[w].reduced = await p2.evaluate(() => ({
      running: document.getAnimations().filter(a => a.playState === 'running').map(a => (a.animationName||a.transitionProperty||'?')).slice(0,10),
      hidden: [...document.querySelectorAll('.mg, .faq-head, .ci, .hi, .reveal')].filter(e => { const c = getComputedStyle(e); return c.opacity === '0' || c.visibility === 'hidden'; }).length,
      sw: document.documentElement.scrollWidth, iw: innerWidth }));
    await p2.screenshot({ path: `${out}reduced-${w}-full.png`, fullPage: true });
    await p2.close();
    const p3 = await browser.newPage();
    await p3.setJavaScriptEnabled(false);
    await p3.setViewport({ width: w, height: 800 });
    await p3.goto('file://' + path, { waitUntil: 'load' }); await sleep(800);
    await p3.screenshot({ path: `${out}nojs-${w}-full.png`, fullPage: true });
    await p3.close();
  }
  console.log(JSON.stringify(res, null, 1));
  await browser.close();
})();
