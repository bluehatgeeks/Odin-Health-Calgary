/* ── Odin Health Labs — Component Loader ── */
/* Fetches nav and footer HTML from CDN and injects into the page */
(function () {
  var CDN = 'https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master';

  /* Re-execute <script> tags after innerHTML injection */
  function execScripts(container) {
    container.querySelectorAll('script').forEach(function (oldScript) {
      var newScript = document.createElement('script');
      Array.from(oldScript.attributes).forEach(function (attr) {
        newScript.setAttribute(attr.name, attr.value);
      });
      newScript.textContent = oldScript.textContent;
      oldScript.parentNode.replaceChild(newScript, oldScript);
    });
  }

  /* Create nav placeholder as first child of body — runs immediately */
  var navRoot = document.createElement('div');
  navRoot.id = 'odin-nav-root';
  document.body.insertBefore(navRoot, document.body.firstChild);

  /* Fetch and inject nav immediately */
  fetch(CDN + '/odinnav.html')
    .then(function (r) { return r.text(); })
    .then(function (html) {
      navRoot.innerHTML = html;
      execScripts(navRoot);
    })
    .catch(function (err) { console.error('[odin-loader] Nav fetch failed:', err); });

  /* Footer must be appended after the full DOM is parsed */
  document.addEventListener('DOMContentLoaded', function () {
    var footerRoot = document.createElement('div');
    footerRoot.id = 'odin-footer-root';
    document.body.appendChild(footerRoot);

    fetch(CDN + '/odinfooter.html?v=2')
      .then(function (r) { return r.text(); })
      .then(function (html) {
        footerRoot.innerHTML = html;
        execScripts(footerRoot);
      })
      .catch(function (err) { console.error('[odin-loader] Footer fetch failed:', err); });
  });
})();
