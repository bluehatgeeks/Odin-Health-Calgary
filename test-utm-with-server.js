// Test UTM passthrough with local HTTP server (avoids localStorage restrictions)
const puppeteer = require('puppeteer-core');
const http = require('http');
const fs = require('fs');

const footer = fs.readFileSync('/workspace/site/pages/_shared/odinfooter.xfollow.html', 'utf8');

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  const url = new URL(req.url, `http://localhost:${PORT}`);
  const path = url.pathname;
  
  let html = `<!DOCTYPE html><html><head><meta charset="utf-8"><title>Test</title></head><body>
    <a href="https://api.leadconnectorhq.com/widget/bookings/test123" class="booking-link">Book Now</a>
    <div id="footer">${footer.replace(/location\.pathname/g, JSON.stringify(path))}</div>
  </body></html>`;
  
  res.end(html);
});

const PORT = 48321;
server.listen(PORT);

async function runTests() {
  const b = await puppeteer.launch({ 
    executablePath: '/usr/local/bin/google-chrome', 
    headless: 'new', 
    args: ['--no-sandbox'] 
  });
  
  try {
    // Test 1: UTM params stored and added to booking links
    console.log('Test 1: Explicit UTM params on organic page...');
    const p1 = await b.newPage();
    await p1.goto(`http://localhost:${PORT}/trt-side-effects?utm_source=x&utm_medium=social&utm_campaign=test`);
    await new Promise(r => setTimeout(r, 1000));
    
    const r1 = await p1.evaluate(() => {
      const stored = localStorage.getItem('odin_ft');
      const link = document.querySelector('.booking-link');
      return {
        stored: stored ? JSON.parse(stored) : null,
        linkHref: link ? link.href : null
      };
    });
    
    const pass1 = r1.stored && 
                  r1.stored.utm.utm_source === 'x' && 
                  r1.stored.utm.utm_medium === 'social' &&
                  r1.stored.utm.utm_campaign === 'test' &&
                  r1.linkHref && 
                  r1.linkHref.includes('utm_source=x') &&
                  r1.linkHref.includes('utm_medium=social') &&
                  r1.linkHref.includes('utm_campaign=test');
    console.log('  Stored:', r1.stored);
    console.log('  Link href:', r1.linkHref);
    console.log('  Result:', pass1 ? '✓ PASS' : '✗ FAIL');
    await p1.close();
    
    // Test 2: Referrer inference (t.co -> x/social) - use fresh browser context
    console.log('\nTest 2: Referrer inference (t.co)...');
    const ctx2 = await b.createIncognitoBrowserContext();
    const p2 = await ctx2.newPage();
    await p2.evaluateOnNewDocument(() => {
      Object.defineProperty(document, 'referrer', { configurable: true, get: () => 'https://t.co/xyz123' });
    });
    await p2.goto(`http://localhost:${PORT}/trt-side-effects`);
    await new Promise(r => setTimeout(r, 1000));
    
    const r2 = await p2.evaluate(() => {
      const stored = localStorage.getItem('odin_ft');
      const link = document.querySelector('.booking-link');
      return {
        stored: stored ? JSON.parse(stored) : null,
        linkHref: link ? link.href : null
      };
    });
    
    const pass2 = r2.stored && 
                  r2.stored.utm.utm_source === 'x' && 
                  r2.stored.utm.utm_medium === 'social' &&
                  r2.linkHref && 
                  r2.linkHref.includes('utm_source=x') &&
                  r2.linkHref.includes('utm_medium=social');
    console.log('  Stored:', r2.stored);
    console.log('  Link href:', r2.linkHref);
    console.log('  Result:', pass2 ? '✓ PASS' : '✗ FAIL');
    await ctx2.close();
    
    // Test 3: Paid page (not in allow-list) - no processing - use fresh browser context
    console.log('\nTest 3: Paid page (/owen-lowt) - no processing...');
    const ctx3 = await b.createIncognitoBrowserContext();
    const p3 = await ctx3.newPage();
    await p3.goto(`http://localhost:${PORT}/owen-lowt?utm_source=test&utm_medium=paid`);
    await new Promise(r => setTimeout(r, 1000));
    
    const r3 = await p3.evaluate(() => {
      const stored = localStorage.getItem('odin_ft');
      const link = document.querySelector('.booking-link');
      return {
        stored: stored,
        linkHref: link ? link.href : null,
        hasUtm: link && link.href ? link.href.includes('utm_') : false
      };
    });
    
    const pass3 = !r3.stored && !r3.hasUtm;
    console.log('  Stored:', r3.stored);
    console.log('  Link href:', r3.linkHref);
    console.log('  Has UTM:', r3.hasUtm);
    console.log('  Result:', pass3 ? '✓ PASS' : '✗ FAIL');
    await ctx3.close();
    
    const allPass = pass1 && pass2 && pass3;
    console.log('\n' + '='.repeat(50));
    console.log(allPass ? '✓ ALL TESTS PASSED' : '✗ SOME TESTS FAILED');
    console.log('='.repeat(50));
    
    await b.close();
    server.close();
    process.exit(allPass ? 0 : 1);
  } catch (err) {
    console.error('Test error:', err);
    await b.close();
    server.close();
    process.exit(1);
  }
}

runTests();
