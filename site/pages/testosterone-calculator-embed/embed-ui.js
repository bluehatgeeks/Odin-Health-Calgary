(function () {
  var O = OdinT, PAGE = 'testosterone-calculator-embed', used = {};
  var $ = function (id) { return document.getElementById(id); };
  function mark(k) { if (used[k]) return; used[k] = 1; try { if (window.mixpanel && typeof window.mixpanel.track === 'function') window.mixpanel.track('CTA Click', { cta: k, page: PAGE }, { transport: 'sendBeacon' }); } catch (e) { } }
  function num(el) { var v = String(el.value).trim().replace(/\s/g, '').replace(',', '.'); if (v === '' || !/^\d*\.?\d+$|^\d+\.$/.test(v)) return NaN; return parseFloat(v); }
  function cut(x, d) { var s = x.toFixed(d); return s.indexOf('.') > -1 ? s.replace(/0+$/, '').replace(/\.$/, '') : s; }
  function fx(x, d) { return x.toLocaleString('en-CA', { minimumFractionDigits: d, maximumFractionDigits: d }); }
  function where(v, lo, hi) { return v < lo ? 'below' : (v > hi ? 'above' : 'inside'); }
  function freeHTML(p) {
    var ll = where(p, 115, 577);
    return '<li class="rs-' + (p < 220 ? 'below' : 'inside') + '">' + (p < 220 ? 'Below' : 'At or above') + ' the 220 pmol/L (64 pg/mL) free T cut-off used by the European Male Ageing Study</li>' +
      '<li class="rs-' + ll + '">' + (ll === 'inside' ? 'Inside' : ll === 'below' ? 'Below' : 'Above') + ' the LifeLabs calculated free T range for men (115 to 577 pmol/L)</li>';
  }
  var fc = $('fc');
  if (!fc) return;
  var tt = $('fc-tt'), sh = $('fc-shbg'), al = $('fc-alb'), res = $('fc-out'), unitTxt = $('fc-tt-unit'), bar = $('fc-bar');
  var unit = function () { var r = fc.querySelector('input[name="fc-unit"]:checked'); return r ? r.value : 'nmol'; };
  var run = function () {
    mark('calc_use_freet');
    var t = num(tt), s = num(sh), a = num(al), u = unit(), note = '';
    if (!(t > 0) || !(s > 0) || !(a > 0)) { res.innerHTML = '<p class="rs-head">Enter total T, SHBG and albumin to see your free T.</p>'; return; }
    var n = u === 'ng' ? O.toNmol(t) : t;
    if (u === 'nmol' && t > 100) { res.innerHTML = '<p class="rs-head">' + t + ' nmol/L looks like an ng/dL result. Switch the unit to ng/dL above.</p>'; return; }
    if (u === 'ng' && t < 20) { res.innerHTML = '<p class="rs-head">' + t + ' ng/dL looks like an nmol/L result. Switch the unit to nmol/L above.</p>'; return; }
    if (a < 10) { note = '<p class="rs-note">Albumin read as ' + cut(a, 2) + ' g/dL (' + cut(a * 10, 1) + ' g/L).</p>'; a = a * 10; }
    if (s > 400 || a > 80) { res.innerHTML = '<p class="rs-head">Check the SHBG (nmol/L) and albumin (g/L) values against your report.</p>'; return; }
    var r = O.free(n, s, a);
    res.innerHTML = '<div class="fc-big"><span class="fc-k">Free testosterone</span><span class="fc-v"><b>' + fx(r.pmol, 0) + '</b> pmol/L</span><span class="fc-v2">' + fx(r.pg, 1) + ' pg/mL</span></div>' +
      '<dl class="fc-dl"><div><dt>Percent free</dt><dd>' + fx(r.pct, 2) + '</dd></div><div><dt>Bioavailable T</dt><dd>' + fx(r.bat, 1) + ' nmol/L (' + fx(r.batNg, 0) + ' ng/dL)</dd></div><div><dt>Total T used</dt><dd>' + fx(n, 1) + ' nmol/L (' + fx(O.toNg(n), 0) + ' ng/dL)</dd></div></dl>' +
      note + '<ul class="rs-list">' + freeHTML(r.pmol) + '</ul>';
    if (bar) { var fr = Math.max(r.pmol / 1e3 / n * 100, 3), al2 = r.alb / n * 100; var sb = Math.max(100 - fr - al2, 0);
      bar.children[0].style.width = sb.toFixed(1) + '%'; bar.children[1].style.width = al2.toFixed(1) + '%'; bar.children[2].style.width = fr.toFixed(1) + '%'; }
  };
  [tt, sh, al].forEach(function (el) { el.addEventListener('input', run); });
  Array.prototype.forEach.call(fc.querySelectorAll('input[name="fc-unit"]'), function (r) {
    r.addEventListener('change', function () {
      var t = num(tt); unitTxt.textContent = r.value === 'ng' ? 'ng/dL' : 'nmol/L';
      if (t > 0) tt.value = r.value === 'ng' ? cut(O.toNg(t), 0) : cut(O.toNmol(t), 2);
      run();
    });
  });
})();
