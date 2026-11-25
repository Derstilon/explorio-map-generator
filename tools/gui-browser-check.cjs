#!/usr/bin/env node
// Headless browser check of the generator GUI (gui.py).
//
// Usage: start `python gui.py --no-browser --port 8765`, then
//   node tools/gui-browser-check.cjs [base-url] [screenshot-path]
// Defaults: http://127.0.0.1:8765/ and ./gui-check.png.
// Playwright is loaded with require('playwright'), or from the path in
// PLAYWRIGHT_MODULE (a playwright package directory). Every line prints PASS or
// FAIL; the exit code is the number of failures.
'use strict';

const fs = require('fs');
const path = require('path');
const os = require('os');

const playwright = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const baseUrl = process.argv[2] || 'http://127.0.0.1:8765/';
const screenshotPath = process.argv[3] || 'gui-check.png';

let failures = 0;
function check(name, condition, detail = '') {
  console.log(`${condition ? 'PASS' : 'FAIL'} ${name}${detail ? ` (${detail})` : ''}`);
  if (!condition) failures += 1;
}

async function waitForFrames(page, count) {
  await page.waitForFunction((n) => document.querySelectorAll('#frames li').length === n, count, { timeout: 15000 });
}

async function download(page, buttonId) {
  const [file] = await Promise.all([page.waitForEvent('download'), page.click(`#${buttonId}`)]);
  const target = path.join(os.tmpdir(), `explorio-gui-check-${Date.now()}-${file.suggestedFilename()}`);
  await file.saveAs(target);
  const content = fs.readFileSync(target);
  fs.unlinkSync(target);
  return { name: file.suggestedFilename(), content };
}

(async () => {
  const browser = await playwright.chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 }, acceptDownloads: true });
  const consoleProblems = [];
  page.on('console', (message) => {
    if (['error', 'warning'].includes(message.type())) consoleProblems.push(message.text());
  });
  page.on('pageerror', (error) => consoleProblems.push(error.message));

  // 1. Load with parameters in the URL hash.
  await page.goto(`${baseUrl}#seed=42&steps=9`);
  await waitForFrames(page, 12);
  check('loads with seed 42 and 12 frames (seed, 9 steps, 2 biome passes)',
    (await page.textContent('#status-seed')) === 'Seed 42');
  check('starts on the last frame', (await page.textContent('#status-frame')).startsWith('Encounter biomes · 12/12'));
  const nodeCount = await page.evaluate(() => cy.nodes().length);
  check('final graph has 30 nodes (3 seed + 3 per production)', nodeCount === 30, `got ${nodeCount}`);

  // 2. Start and goal markers.
  const roles = await page.evaluate(() => ({
    start: cy.nodes('[role="start"]').map((node) => [node.id(), node.style('shape'), node.data('label')]),
    goal: cy.nodes('[role="goal"]').map((node) => [node.id(), node.style('shape'), node.data('label')]),
  }));
  check('the entrance lock is marked START as a star', JSON.stringify(roles.start) === JSON.stringify([['L0', 'star', 'START · L0']]),
    JSON.stringify(roles.start));
  check('the dungeon key is marked GOAL as an octagon', JSON.stringify(roles.goal) === JSON.stringify([['K0', 'round-octagon', 'GOAL · K0']]),
    JSON.stringify(roles.goal));

  // 3. Stepping and highlights.
  await page.click('#first');
  check('reset shows the seed graph', (await page.textContent('#status-frame')).startsWith('Seed graph · 1/12'));
  check('seed graph has 3 nodes', (await page.evaluate(() => cy.nodes().length)) === 3);
  await page.click('#forward');
  const step1 = await page.evaluate(() => ({
    title: document.querySelector('#status-frame').textContent,
    nodes: cy.nodes().length,
    added: cy.nodes('.added').map((node) => node.id()).sort(),
    removedEdges: cy.edges('.removed').length,
  }));
  check('step forward applies one production', step1.title.startsWith('Step 1:') && step1.nodes === 6, step1.title);
  check('the step highlights its 3 new nodes', step1.added.length === 3, step1.added.join(','));
  check('the step shows the moved edge as removed', step1.removedEdges === 1);
  const positionBefore = await page.evaluate(() => cy.$id('A0').position());
  await page.keyboard.press('End');
  const positionAfter = await page.evaluate(() => cy.$id('A0').position());
  check('nodes keep their position across steps',
    positionBefore.x === positionAfter.x && positionBefore.y === positionAfter.y);

  // 3. Hover tooltip on a lock.
  const lockPoint = await page.evaluate(() => {
    const box = document.getElementById('graph').getBoundingClientRect();
    const position = cy.$id('L1').renderedPosition();
    return { x: box.left + position.x, y: box.top + position.y };
  });
  await page.mouse.move(lockPoint.x, lockPoint.y);
  await page.waitForSelector('#tooltip:not([hidden])', { timeout: 5000 });
  const tooltip = await page.textContent('#tooltip');
  check('hovering a lock shows its attributes',
    tooltip.includes('L1') && tooltip.includes('Logic gate') && tooltip.includes('AND') && tooltip.includes('Created by'),
    tooltip.slice(0, 80));
  await page.mouse.move(5, 5);
  check('tooltip hides when the pointer leaves', await page.isHidden('#tooltip'));

  // 4. Exports.
  const json = await download(page, 'export-json');
  const exported = JSON.parse(json.content.toString());
  check('JSON export is the final graph with schema and seed',
    exported.schema === 'explorio.story-graph.v1' && exported.seed === 42 && exported.nodes.length === 30, json.name);
  const png = await download(page, 'export-png');
  check('PNG export is a PNG image', png.content.subarray(1, 4).toString() === 'PNG' && png.content.length > 10000,
    `${png.name}, ${png.content.length} bytes`);
  const svg = await download(page, 'export-svg');
  const svgText = svg.content.toString();
  check('SVG export has the seed caption and all nodes',
    svgText.startsWith('<svg') && svgText.includes('seed 42') && svgText.includes('START · L0')
    && svgText.includes('GOAL · K0') && (svgText.match(/>L\d+</g) || []).length === 9, svg.name);
  const encounterColors = await page.evaluate(() => [...new Set(cy.nodes('[pieCount > 0]')
    .flatMap((node) => [1, 2, 3, 4].slice(0, node.data('pieCount')).map((i) => node.data(`pie${i}`))))]);
  check('SVG export draws every encounter colour the canvas shows',
    encounterColors.length > 0 && encounterColors.every((color) => svgText.includes(`fill="${color}"`)),
    encounterColors.join(','));

  // 5. Controls: disable L1, so L2 has nothing to match on the seed graph.
  await page.uncheck('#use-L1');
  await page.click('#generate');
  await waitForFrames(page, 3);
  check('with only L2 enabled generation stops early and says why',
    (await page.textContent('#status-frame')).includes('no enabled production matched'));
  check('URL hash records the parameters', (await page.evaluate(() => location.hash)).includes('w_L1=0'));
  await page.check('#use-L1');
  await page.fill('#seed', '7');
  await page.fill('#steps', '4');
  await page.press('#steps', 'Enter');
  await waitForFrames(page, 7);
  check('Enter in a field regenerates with the new seed', (await page.textContent('#status-seed')) === 'Seed 7');
  await page.fill('#seed', '9');
  await page.focus('#generate');
  await page.keyboard.press('Space');
  await page.waitForFunction(() => document.querySelector('#status-seed').textContent === 'Seed 9', null, { timeout: 15000 })
    .catch(() => {});
  await page.focus('#back');
  const beforeArrow = await page.textContent('#status-frame');
  await page.keyboard.press('ArrowLeft');
  check('arrow keys still step while a timeline button has focus',
    (await page.textContent('#status-frame')) !== beforeArrow);
  check('Space on a focused button presses it instead of playing',
    (await page.textContent('#status-seed')) === 'Seed 9' && (await page.textContent('#play')) !== '⏸');
  await page.goto('about:blank');
  await page.goto(`${baseUrl}#seed=-5&steps=4`);
  await waitForFrames(page, 7);
  check('a negative seed from the URL is kept',
    (await page.textContent('#status-seed')) === 'Seed -5' && (await page.evaluate(() => location.hash)).includes('seed=-5'));
  await page.fill('#seed', '7');
  await page.click('#generate');
  await page.waitForFunction(() => document.querySelector('#status-seed').textContent === 'Seed 7', null, { timeout: 15000 });

  // 6. Same seed, same graph.
  const fingerprint = () => page.evaluate(() => JSON.stringify(cy.nodes().map((node) => [node.id(), node.data('env_biome')])));
  const first = await fingerprint();
  await page.click('#generate');
  await waitForFrames(page, 7);
  check('regenerating the same seed gives the same graph', first === (await fingerprint()));

  // 7. Many steps on a small window: the page must not grow, the sidebar stays visible,
  //    and the step strip scrolls to the current step without scrolling the page.
  await page.setViewportSize({ width: 1024, height: 700 });
  await page.goto('about:blank');
  await page.goto(`${baseUrl}#seed=42&steps=200`);
  await waitForFrames(page, 203);
  const layout = async () => page.evaluate(() => {
    const strip = document.getElementById('frames');
    const chip = strip.querySelector('li.current').getBoundingClientRect();
    const box = strip.getBoundingClientRect();
    return {
      pageWidth: document.documentElement.scrollWidth, pageHeight: document.documentElement.scrollHeight,
      scrollX: window.scrollX, scrollY: window.scrollY,
      sidebarLeft: document.getElementById('sidebar').getBoundingClientRect().left,
      chipVisible: chip.left >= box.left - 1 && chip.right <= box.right + 1,
      stripScroll: strip.scrollLeft,
    };
  });
  let measured = await layout();
  check('200 steps: the page fits the window and does not scroll',
    measured.pageWidth === 1024 && measured.pageHeight === 700 && measured.scrollX === 0 && measured.scrollY === 0,
    JSON.stringify(measured));
  check('200 steps: the sidebar stays visible', measured.sidebarLeft === 0);
  check('200 steps: the strip shows the current (last) step', measured.chipVisible && measured.stripScroll > 0);
  await page.keyboard.press('Home');
  measured = await layout();
  check('Home scrolls the strip back to the first step without moving the page',
    measured.chipVisible && measured.stripScroll === 0 && measured.scrollX === 0 && measured.scrollY === 0);
  await page.keyboard.press('End');
  const bigPng = await download(page, 'export-png');
  check('200 steps: PNG export still produces a PNG',
    bigPng.content.subarray(1, 4).toString() === 'PNG' && (await page.isHidden('#error')), `${bigPng.content.length} bytes`);
  const bigSvg = await download(page, 'export-svg');
  check('200 steps: SVG export has all nodes', (bigSvg.content.toString().match(/<text /g) || []).length >= 600);
  await page.screenshot({ path: screenshotPath.replace(/\.png$/, '-200-steps.png') });

  await page.setViewportSize({ width: 1400, height: 900 });
  await page.goto('about:blank');
  await page.goto(`${baseUrl}#seed=42&steps=9`);
  await waitForFrames(page, 12);
  await page.screenshot({ path: screenshotPath });
  check('no console errors or warnings', consoleProblems.length === 0, consoleProblems.slice(0, 3).join(' | '));

  await browser.close();
  process.exit(failures);
})().catch((error) => {
  console.log(`FAIL check crashed: ${error.message}`);
  process.exit(100);
});
