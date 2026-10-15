// usage (from /workspace/hp-test): node /workspace/pages/_shared/test-visual.js <slug>
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const slug = process.argv[2];
const path = `/workspace/pages/${slug}/page.html`;
const out = `/workspace/pages/${slug}/shots/`;
const sleep = ms => new Promise(r => setTimeout(r, ms));
const SEL = '.mg, .faq-head, [data-timeline]';
(async () => {
  const browser = await puppeteer.launch({ executablePath: '/usr/bin/google-chrome', headless: 'new', args: ['--no-sandbox'] });
  const res = {};
  for (const w of [1280, 390]) {
    const page = await browser.newPage();
    await page.setViewport({ width: w, height: w === 390 ? 844 : 800, deviceScaleFactor: 1 });
    const errs = [];
    page.on('console', m => { if (['error', 'warning'].includes(m.type())) errs.push(m.type() + ': ' + m.text()); });
    page.on('pageerror', e => errs.push('pageerror: ' + e.message));
    page.on('requestfailed', r => errs.push('reqfailed: ' + r.url()));
    await page.evaluateOnNewDocument(() => { window.__cls = 0; new PerformanceObserver(l => { for (const e of l.getEntries()) if (!e.hadRecentInput) window.__cls += e.value; }).observe({ type: 'layout-shift', buffered: true }); });
    await page.goto('file://' + path, { waitUntil: 'networkidle0' });
    await sleep(800);
    await page.screenshot({ path: `${out}top-${w}.png` });
    const n = await page.evaluate(s => document.querySelectorAll(s).length, SEL);
    for (let i = 0; i < n; i++) {
      await page.evaluate((s, i) => { const e = document.querySelectorAll(s)[i]; const r = e.getBoundingClientRect(); window.scrollTo(0, window.scrollY + r.top - 120); }, SEL, i);
      await sleep(1700);
      const el = (await page.$$(SEL))[i];
      const name = await page.evaluate((s, i) => { const e = document.querySelectorAll(s)[i]; const sec = e.closest('section'); return (sec && (sec.id || (sec.classList.contains('final-cta') ? 'final' : 'hero'))) || 'x'; }, SEL, i);
      const nm = `${String(i).padStart(2, '0')}-${name}`;
      await el.screenshot({ path: `${out}${nm}-${w}-a.png` });
      await sleep(3000);
      await el.screenshot({ path: `${out}${nm}-${w}-b.png` });
    }
    const m = await page.evaluate(() => ({
      cls: window.__cls, sw: document.documentElement.scrollWidth, iw: innerWidth, bsw: document.body.scrollWidth,
      running: document.getAnimations().filter(a => a.playState === 'running').length,
      total: document.getAnimations().length, paused: document.querySelectorAll('.is-paused').length,
      figs: document.querySelectorAll('.mg').length,
      overflowEls: [...document.querySelectorAll('main *')].filter(e => { const r = e.getBoundingClientRect(); return r.right > innerWidth + 1 && !e.closest('svg') && getComputedStyle(e).position !== 'fixed'; }).map(e => e.tagName + '.' + e.className).slice(0, 8),
    }));
    res[w] = { ...m, errs };
    await page.screenshot({ path: `${out}full-${w}.png`, fullPage: true });
    await page.evaluate(() => window.scrollTo(0, 0)); await sleep(1200);
    // loops must pause off-screen: any running animation whose nearest [data-live] is >200px outside the viewport is a failure
    res[w].runningOffscreen = await page.evaluate(() => document.getAnimations().filter(a => {
      if (a.playState !== 'running' || !a.effect || !a.effect.target || !a.effect.target.closest) return false;
      const live = a.effect.target.closest('[data-live]'); if (!live) return false;
      const r = live.getBoundingClientRect(); return r.bottom < -200 || r.top > innerHeight + 200;
    }).length);
    res[w].liveBlocks = await page.evaluate(() => document.querySelectorAll('[data-live]').length);
    await page.close();
    const p2 = await browser.newPage();
    await p2.setViewport({ width: w, height: 800 });
    await p2.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }]);
    await p2.goto('file://' + path, { waitUntil: 'networkidle0' }); await sleep(800);
    res[w].reduced = await p2.evaluate(() => ({
      running: document.getAnimations().filter(a => a.playState === 'running').map(a => (a.animationName || a.transitionProperty || '?')).slice(0, 10),
      hidden: [...document.querySelectorAll('.mg, .faq-head, .ci, .hi, .reveal')].filter(e => { const c = getComputedStyle(e); return c.opacity === '0' || c.visibility === 'hidden'; }).length,
      hiddenSvg: [...document.querySelectorAll('.mg svg [class]')].filter(e => getComputedStyle(e).opacity === '0' && !/(hs-lit|sy-ember|hb-sweep|br-ring|pz-ring|sp-flash|qs-ring|so-ring|cl-a|cl-b|cl-burst|cl-dot|ly-lit|sb-pol|sc-bar|sc-ring)/.test(e.getAttribute('class'))).map(e => e.getAttribute('class')).slice(0, 10),
      sw: document.documentElement.scrollWidth, iw: innerWidth }));
    await p2.screenshot({ path: `${out}reduced-${w}-full.png`, fullPage: true });
    await p2.close();
    const p3 = await browser.newPage();
    await p3.setJavaScriptEnabled(false);
    await p3.setViewport({ width: w, height: 800 });
    await p3.goto('file://' + path, { waitUntil: 'load' }); await sleep(800);
    res[w].nojs = await p3.evaluate(() => ({ hidden: [...document.querySelectorAll('.mg, .faq-head, .ci, .hi, .reveal, .timeline-list > li')].filter(e => { const c = getComputedStyle(e); return c.opacity === '0' || c.visibility === 'hidden'; }).length, running: document.getAnimations().filter(a => a.playState === 'running').length }));
    await p3.screenshot({ path: `${out}nojs-${w}-full.png`, fullPage: true });
    await p3.close();
  }
  console.log(JSON.stringify(res, null, 1));
  await browser.close();
})();
