// Vermeulen + unit-conversion validation for /testosterone-calculator.
// Runs the EXACT math block shipped in page.html (between /*CORE*/ and /*/CORE*/) and asserts published worked examples.
// usage: node /workspace/pages/testosterone-calculator/test-calc.js
const fs = require('fs'), vm = require('vm'), path = require('path');
const html = fs.readFileSync(path.join(__dirname, 'page.html'), 'utf8');
const m = html.match(/\/\*CORE\*\/([\s\S]*?)\/\*\/CORE\*\//); if (!m) { console.log('FAIL: core block not found in page.html'); process.exit(1); }
const ctx = {}; vm.createContext(ctx); vm.runInContext(m[1] + ';this.OdinT=OdinT;', ctx); const O = ctx.OdinT;
let pass = 0, fail = 0; const rows = [];
const near = (name, got, want, tol, src) => { const good = Math.abs(got - want) <= tol; good ? pass++ : fail++; rows.push(`${good ? 'PASS' : 'FAIL'}  ${name}: got ${got.toFixed(4)}, expected ${want} +/- ${tol}  [${src}]`); };
// 1. Unit conversions (PubChem MW 288.4 g/mol; Endocrine Society 2018 paired values)
near('1 nmol/L in ng/dL', O.toNg(1), 28.84, 1e-9, 'PubChem CID 6013: 288.4 g/mol');
near('300 ng/dL in nmol/L (AUA cut-off)', O.toNmol(300), 10.40, 0.005, 'AUA 2018 300 ng/dL');
near('264 ng/dL in nmol/L', O.toNmol(264), 9.2, 0.06, 'ES 2018 pair 264 ng/dL = 9.2 nmol/L');
near('916 ng/dL in nmol/L', O.toNmol(916), 31.8, 0.06, 'ES 2018 pair 916 ng/dL = 31.8 nmol/L');
near('1 pg/mL in pmol/L', O.toPmol(1), 3.467, 1e-9, 'PubChem-derived 1000/288.4');
near('64 pg/mL in pmol/L', O.toPmol(64), 220, 2.5, 'ES 2018 / EMAS pair 64 pg/mL = 220 pmol/L (ES rounds 221.9)');
// 2. ISSAM published worked example (issam.ch/freetesuit.html): TT 10 nmol/L (288.4 ng/dL), SHBG 40 nmol/L, albumin 4.3 g/dL
let r = O.free(10, 40, 43);
near('ISSAM N (1 + Ka*[Alb])', r.N, 23.43, 0.005, 'ISSAM: (1 + 22.43)[S] = 23.43 [S]');
near('ISSAM free T, mol/L x 1e10', r.pmol / 100, 1.7388, 0.0005, 'ISSAM: [S] = 1.7388 x 10^-10 mol/L');
near('ISSAM percent free', r.pct, 1.74, 0.005, 'ISSAM: [S] % = 1.74 %');
near('ISSAM free T ng/dL', r.pg / 10, 5.02, 0.01, 'ISSAM: FT = 5.02 ng/dl');
near('ISSAM bioavailable T ng/dL', r.batNg, 118, 0.6, 'ISSAM: Bio T = 118 ng/dL');
// 3. calcengines.com worked example: TT 15 nmol/L, SHBG 30 nmol/L, albumin 4.3 g/dL -> 325.6 pmol/L (N = 23.43, b = 38.43)
r = O.free(15, 30, 43);
near('calcengines free T pmol/L', r.pmol, 325.6, 0.05, 'calcengines.com worked example: 3.256 x 10^-10 mol/L = 325.6 pmol/L');
near('calcengines b term', r.N + 1e9 * (30e-9 - 15e-9), 38.43, 0.005, 'calcengines: b = N + 10^9 (S - T) = 38.43');
// 4. Same solver with albumin MW 66,430 (used by alphahealthfinder.com / aresmensclinic.com): 500 ng/dL, SHBG 30, Alb 4.3 g/dL
//    -> FT 10.8 ng/dL (108 pg/mL), 2.17 percent, bioavailable 264 ng/dL, N = 24.30. Verifies the quadratic independently of the MW constant.
const v66 = (tt, s, alb) => { const T = tt * 1e-9, S = s * 1e-9, N = 1 + 3.6e4 * alb / 66430, a = N * 1e9, b = N + 1e9 * (S - T); const ft = (-b + Math.sqrt(b * b + 4 * a * T)) / (2 * a); return { N, pg: ft * 288.4 * 1e9 /* g/L -> pg/mL */, pct: 100 * ft / T, batNg: ft * N * 1e9 * 28.84 }; };
const q = v66(500 / 28.84, 30, 43);
near('MW 66,430 variant N', q.N, 24.30, 0.005, 'alphahealthfinder.com: N = 24.30');
near('MW 66,430 variant free T pg/mL', q.pg, 108, 0.6, 'alphahealthfinder.com: 108 pg/mL');
near('MW 66,430 variant percent free', q.pct, 2.17, 0.006, 'alphahealthfinder.com: 2.17%');
near('MW 66,430 variant bioavailable ng/dL', q.batNg, 264, 0.6, 'alphahealthfinder.com: 264 ng/dL');
// 5. Sanity: free fraction rises as SHBG falls; pools add up to total
const lo = O.free(15, 10, 43), hi = O.free(15, 80, 43);
const okMono = lo.pct > r.pct && r.pct > hi.pct; okMono ? pass++ : fail++; rows.push(`${okMono ? 'PASS' : 'FAIL'}  percent free falls as SHBG rises (${lo.pct.toFixed(2)} > ${r.pct.toFixed(2)} > ${hi.pct.toFixed(2)})`);
near('pools sum to total (free + albumin-bound + SHBG-bound)', r.pmol / 1000 + r.alb + r.shbgB, 15, 1e-9, 'mass balance');
console.log(rows.join('\n')); console.log(fail ? `VERMEULEN TEST FAIL (${fail} of ${pass + fail})` : `VERMEULEN TEST PASS (${pass}/${pass + fail})`); process.exit(fail ? 1 : 0);
