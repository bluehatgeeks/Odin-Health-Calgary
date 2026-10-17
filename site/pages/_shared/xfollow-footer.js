// Serves the STAGED footer (/workspace/pages/_shared/odinfooter.xfollow.html) instead of the live GitHub copy, so file:// page tests see the X follow line.
// The footer's allow-list script reads location.pathname; file:// pages have a filesystem path, so the harness substitutes the page's real URL path.
// FOOTER_LIVE=1 -> test against the live (currently deployed) footer. FOOTER_PATH=/owen-lowt -> pretend the page lives at that path (negative test).
const fs = require('fs');
const FILE = process.env.FOOTER_FILE || '/workspace/pages/_shared/odinfooter.xfollow.html';
module.exports.urlPath = slug => process.env.FOOTER_PATH || ((slug === '_home' || slug === 'home') ? '/' : '/' + slug);
module.exports.serveFooter = async (page, slug) => {
  if (process.env.FOOTER_LIVE === '1') return;
  const body = fs.readFileSync(FILE, 'utf8').replace(/location\.pathname/g, JSON.stringify(module.exports.urlPath(slug)));
  await page.setRequestInterception(true);
  page.on('request', req => {
    if (/odinfooter\.html/.test(req.url())) req.respond({ status: 200, contentType: 'text/html; charset=utf-8', headers: { 'Access-Control-Allow-Origin': '*' }, body });
    else req.continue();
  });
};
