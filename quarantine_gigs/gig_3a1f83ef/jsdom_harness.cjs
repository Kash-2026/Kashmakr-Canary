#!/usr/bin/env node
/**
 * Kashmakr Autoloop — jsdom interaction harness.
 *
 * Executes the deliverable's inline scripts in a headless DOM and validates
 * REAL behavior, closing the false-positive classes that pure syntax checks
 * cannot catch:
 *   - uncaught runtime errors (parse-time or click-time) → RUNTIME_EXCEPTION
 *   - dead interactions (click does nothing visible)     → ASSERTION_FAILURE
 *   - wrong computed values (contract mismatch)          → ASSERTION_FAILURE
 *
 * Protocol (stdout, single JSON line, always printed exactly once):
 *   { ok: bool, phase: "boot"|"runtime"|"expect",
 *     error: { name, message } | null, results: [ {step, kind, status, ...} ] }
 *
 * Usage:
 *   node jsdom_harness.js --html <file> \
 *     [--wire <json>] [--elements <json>] [--js <json>]
 *     --wire      JSON array of steps: "FILL:#id=value" | "CLICK:#id" |
 *                 "EXPECT:#id=value-or-~/regex/" | JS expression string
 *     --elements  JSON array of required CSS selectors
 *     --js        JSON array of client JS expression strings (truthy = pass)
 *
 * Exit code: 0 all pass, 1 failure.
 * Requires jsdom (resolved from ./node_modules in the sandbox).
 */
'use strict';

const fs = require('fs');
const path = require('path');

function out(obj) {
  process.stdout.write(JSON.stringify(obj) + '\n');
  process.exit(obj.ok === true ? 0 : 1);
}

const args = {};
for (let i = 2; i < process.argv.length; i++) {
  if (process.argv[i].startsWith('--')) {
    args[process.argv[i].slice(2)] = (i + 1 < process.argv.length) ? process.argv[i + 1] : true;
    i++;
  }
}

let html;
try {
  html = fs.readFileSync(args.html, 'utf8');
} catch (e) {
  out({ ok: false, phase: 'boot', error: { name: 'HarnessError', message: 'cannot read html: ' + e.message }, results: [] });
}

// ---- 0. Load jsdom ------------------------------------------------------
let JSDOM = null;
for (const candidate of [
  path.join(process.cwd(), 'node_modules', 'jsdom'),
  path.join(__dirname, 'node_modules', 'jsdom'),
  'jsdom',
]) {
  try { JSDOM = require(candidate).JSDOM; break; } catch (_) { /* next */ }
}
if (!JSDOM) {
  out({
    ok: false,
    phase: 'boot',
    error: { name: 'HarnessError', message: 'jsdom is not installed; see app/oracles.py bootstrap logic' },
    results: [],
  });
}

// ---- 1. Boot the DOM ----------------------------------------------------
const runtimeErrors = [];
let dom;
try {
  dom = new JSDOM(html, {
    runScripts: 'dangerously',
    beforeParse(window) {
      window.addEventListener('error', (e) => {
        runtimeErrors.push({ name: e.name || 'Error', message: String(e.message || e) });
      });
      window.addEventListener('unhandledrejection', (e) => {
        runtimeErrors.push({ name: 'UnhandledRejection', message: String(e.reason || e) });
      });
    },
  });
} catch (e) {
  out({ ok: false, phase: 'boot', error: { name: 'HarnessError', message: String(e && e.message || e) }, results: [] });
}

const window = dom.window;
const document = window.document;

// ---- step executor (shared by FILL/CLICK/EXPECT/JS) ---------------------
function runStep(step) {
  let kind, inner;
  if (typeof step === 'string') {
    const idx = step.indexOf(':');
    kind = idx > 0 ? step.slice(0, idx) : step;
    inner = idx > 0 ? step.slice(idx + 1) : '';
  } else if (step && typeof step === 'object') {
    kind = String(step.kind || '');
    inner = step.value !== undefined ? `${step.selector}=${step.value}` : String(step.selector || '');
  } else {
    results.push({ step, kind: '?', status: 'error', error: 'unrecognized step' });
    return;
  }

  if (kind === 'FILL') {
    const cut = inner.indexOf('=');
    if (cut < 0) { results.push({ step, kind: 'fill', status: 'error', error: 'FILL needs selector=value' }); return; }
    const sel = inner.slice(0, cut);
    const value = inner.slice(cut + 1);
    let el = null;
    try { el = document.querySelector(sel); } catch (_) {}
    if (!el) { results.push({ step, kind: 'fill', selector: sel, status: 'missing', error: 'no element for ' + sel }); return; }
    if ('value' in el) el.value = value; else el.textContent = value;
    results.push({ step, kind: 'fill', selector: sel, status: 'filled' });
    return;
  }

  if (kind === 'CLICK') {
    let el = null;
    try { el = document.querySelector(inner); } catch (_) {}
    if (!el) { results.push({ step, kind: 'click', selector: inner, status: 'missing', error: 'no element for ' + inner }); return; }
    try {
      el.click();
      results.push({ step, kind: 'click', selector: inner, status: 'clicked' });
    } catch (e) {
      runtimeErrors.push({ name: e.name || 'Error', message: String(e.message) });
      results.push({ step, kind: 'click', selector: inner, status: 'error', error: String(e.message) });
    }
    return;
  }

  if (kind === 'EXPECT') {
    const cut = inner.indexOf('=');
    if (cut < 0) { results.push({ step, kind: 'expect', status: 'error', error: 'EXPECT needs selector=value' }); return; }
    const sel = inner.slice(0, cut);
    const want = inner.slice(cut + 1);
    let text = '';
    try {
      const el = document.querySelector(sel);
      text = el ? (el.textContent ?? '') : '';
    } catch (_) {}
    let matched;
    if (want.startsWith('~/') && want.endsWith('/')) {
      try { matched = new RegExp(want.slice(2, -1)).test(text); }
      catch (e) { results.push({ step, kind: 'expect', selector: sel, status: 'error', error: 'bad regex: ' + e.message }); return; }
    } else {
      matched = text === want || text.includes(want);
    }
    results.push({
      step, kind: 'expect', selector: sel,
      status: matched ? 'matched' : 'mismatch',
      expected: want, got: String(text).trim().slice(0, 200),
    });
    return;
  }

  if (kind === 'JS') {
    let value = false;
    try { value = window.eval(inner); }
    catch (e) { results.push({ step, kind: 'js', expr: inner.slice(0, 200), status: 'error', error: String(e.message) }); return; }
    results.push({ step, kind: 'js', expr: inner.slice(0, 200), status: value ? 'matched' : 'mismatch', got: String(value).slice(0, 200) });
    return;
  }

  results.push({ step, kind, status: 'unknown-kind' });
}

const results = [];

// ---- 2. Required elements exist ----------------------------------------
let requiredElements = [];
try { requiredElements = args.elements ? JSON.parse(args.elements) : []; } catch (_) { requiredElements = []; }
const missing = [];
for (const sel of requiredElements) {
  let found = false;
  try { found = !!document.querySelector(sel); } catch (_) { /* invalid selector */ }
  if (!found) missing.push(sel);
}
if (missing.length > 0) {
  out({
    ok: false,
    phase: 'boot',
    error: { name: 'MissingDomElement', message: 'missing required elements: ' + missing.join(', ') },
    results: missing.map((sel) => ({ step: null, kind: 'element', selector: sel, status: 'missing' })),
  });
}

// ---- 3. Wire contract ---------------------------------------------------
let wire = [];
try { wire = args.wire ? JSON.parse(args.wire) : []; } catch (e) {
  out({ ok: false, phase: 'boot', error: { name: 'HarnessError', message: 'bad --wire JSON: ' + e.message }, results: [] });
}
for (const step of wire) {
  runStep(step);
}

// ---- 4. Standalone JS expression assertions ----------------------------
let jsAsserts = [];
try { jsAsserts = args.js ? JSON.parse(args.js) : []; } catch (_) { jsAsserts = []; }
for (const expr of jsAsserts) {
  if (typeof expr !== 'string') {
    results.push({ step: expr, kind: 'js', status: 'error', error: 'JS assert must be a string expression' });
    continue;
  }
  runStep('JS:' + expr);
}

// ---- 4b. Auto-smoke (no explicit contract): click every button ----------
// Surfaces dead handlers (handlers that throw) even when the caller did not
// declare an interaction contract. Deliberately checks only for *uncaught
// runtime errors*: with no declared expectation we cannot judge values, only
// that the page's own logic does not blow up under a real click.
if (String(args.autosmoke) === '1' && wire.length === 0 && jsAsserts.length === 0) {
  const candidates = document.querySelectorAll(
    'button, [role="button"], input[type="button"], input[type="submit"]'
  );
  for (const el of Array.from(candidates).slice(0, 10)) {
    const label = 'AUTOSMOKE:' + (el.id ? '#' + el.id : el.tagName.toLowerCase());
    try {
      el.click();
      results.push({ step: label, kind: 'click', status: 'clicked' });
    } catch (e) {
      runtimeErrors.push({ name: e.name || 'Error', message: String(e.message) });
      results.push({ step: label, kind: 'click', status: 'error', error: String(e.message) });
    }
  }
}

// ---- 5. Final verdict ---------------------------------------------------
if (runtimeErrors.length > 0) {
  out({
    ok: false,
    phase: 'runtime',
    error: { name: runtimeErrors[0].name || 'Error', message: runtimeErrors[0].message },
    results,
  });
}
const failed = results.filter((r) => ['missing', 'mismatch', 'error', 'unknown-kind'].includes(r.status));
if (failed.length > 0) {
  out({
    ok: false,
    phase: 'expect',
    error: {
      name: 'ExpectationFailure',
      message: failed
        .map((f) => `${String(f.step ?? f.kind)}: ${f.status}${f.error ? ' (' + f.error + ')' : ''}`)
        .join('; '),
    },
    results,
  });
}
out({ ok: true, phase: 'expect', error: null, results });
