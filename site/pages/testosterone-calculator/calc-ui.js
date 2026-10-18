(function () {
  var O = OdinT, PAGE = 'testosterone-calculator', used = {};
  var $ = function (id) { return document.getElementById(id); };
  function mark(k) { if (used[k]) return; used[k] = 1; try { if (window.mixpanel && typeof window.mixpanel.track === 'function') window.mixpanel.track('CTA Click', { cta: k, page: PAGE }, { transport: 'sendBeacon' }); } catch (e) { } }
  function num(el) { var v = String(el.value).trim().replace(/\s/g, '').replace(',', '.'); if (v === '' || !/^\d*\.?\d+$|^\d+\.$/.test(v)) return NaN; return parseFloat(v); }
  function cut(x, d) { var s = x.toFixed(d); return s.indexOf('.') > -1 ? s.replace(/0+$/, '').replace(/\.$/, '') : s; }
  function fx(x, d) { return x.toLocaleString('en-CA', { minimumFractionDigits: d, maximumFractionDigits: d }); }
  function where(v, lo, hi) { return v < lo ? 'below' : (v > hi ? 'above' : 'inside'); }
  var AUA = 300 / O.F;
  function totalHTML(n) {
    var g = O.toNg(n), es = where(n, 9.2, 31.8), apl = where(n, 8.0, 35.0), ll = where(n, 8.4, 28.8), labs;
    if (apl === ll) labs = (apl === 'inside' ? 'inside both' : apl + ' both') + ' typical Canadian lab ranges (Alberta Precision Labs 8.0 to 35.0, LifeLabs 8.4 to 28.8 nmol/L)';
    else labs = apl + ' the Alberta Precision Labs range (8.0 to 35.0) and ' + ll + ' the LifeLabs range (8.4 to 28.8 nmol/L)';
    return '<p class="rs-head"><b>' + fx(n, 1) + ' nmol/L = ' + fx(g, 0) + ' ng/dL</b></p><ul class="rs-list">' +
      '<li class="rs-' + es + '">' + (es === 'inside' ? 'Inside' : es === 'below' ? 'Below' : 'Above') + ' the Endocrine Society harmonized range (9.2 to 31.8 nmol/L, 264 to 916 ng/dL)</li>' +
      '<li class="rs-' + (n < AUA ? 'below' : 'inside') + '">' + (n < AUA ? 'Under' : 'At or above') + ' the American Urological Association low-T cut-off (300 ng/dL, about 10.4 nmol/L)</li>' +
      '<li class="rs-' + (n < 10 ? 'below' : 'inside') + '">' + (n < 10 ? 'Under' : 'At or above') + ' the Canadian Urological Association threshold (10 nmol/L)</li>' +
      '<li class="rs-' + (apl === 'inside' && ll === 'inside' ? 'inside' : (apl === 'below' || ll === 'below') ? 'below' : 'above') + '">' + labs.charAt(0).toUpperCase() + labs.slice(1) + '</li></ul>';
  }
  function freeHTML(p) {
    var ll = where(p, 115, 577);
    return '<li class="rs-' + (p < 220 ? 'below' : 'inside') + '">' + (p < 220 ? 'Below' : 'At or above') + ' the 220 pmol/L (64 pg/mL) free T cut-off used by the European Male Ageing Study</li>' +
      '<li class="rs-' + ll + '">' + (ll === 'inside' ? 'Inside' : ll === 'below' ? 'Below' : 'Above') + ' the LifeLabs calculated free T range for men (115 to 577 pmol/L)</li>';
  }
  /* ── Unit converter ── */
  var cv = $('cv'), pin = $('mt-pin'), pinT = $('mt-val');
  if (cv) {
    var pairs = [['cv-nmol', 'cv-ng', O.toNg, 0, 'total'], ['cv-ng', 'cv-nmol', O.toNmol, 2, 'total'], ['cv-pmol', 'cv-pg', O.toPg, 2, 'free'], ['cv-pg', 'cv-pmol', O.toPmol, 1, 'free']];
    var out = $('cv-out'), outF = $('cv-out-free');
    var setPin = function (n) { if (!pin) return; var x = 460 * Math.min(n, 40) / 40; pin.style.transform = 'translateX(' + x.toFixed(1) + 'px)'; pinT.textContent = fx(n, 1) + (n > 40 ? '+' : ''); };
    pairs.forEach(function (pr) {
      var a = $(pr[0]), b = $(pr[1]);
      a.addEventListener('input', function () {
        mark('calc_use_converter');
        var v = num(a);
        if (!(v > 0)) { b.value = ''; (pr[4] === 'total' ? out : outF).innerHTML = '<p class="rs-head">Enter a number above zero, such as 15 or 432.</p>'; return; }
        var w = pr[2](v); b.value = cut(w, pr[3] === 0 && w < 100 ? 1 : pr[3]);
        if (pr[4] === 'total') { var n = pr[0] === 'cv-nmol' ? v : w; out.innerHTML = totalHTML(n); setPin(n); }
        else { var p = pr[0] === 'cv-pmol' ? v : w; outF.innerHTML = '<p class="rs-head"><b>' + fx(p, 0) + ' pmol/L = ' + fx(O.toPg(p), 1) + ' pg/mL</b></p><ul class="rs-list">' + freeHTML(p) + '</ul>'; }
      });
    });
  }
  /* ── Free T calculator (Vermeulen) ── */
  var fc = $('fc');
  if (fc) {
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
  }
})();
