'use strict';

// Node sizes used both for the dagre layout and for drawing.
const SIZE = { access: [64, 40], lock: [46, 46], key: [40, 40] };
// Start (entrance lock) and goal (dungeon key) are drawn larger and gold, with their own shapes.
const ROLE = {
  start: { size: [62, 62], shape: 'star', text: 'START' },
  goal: { size: [58, 58], shape: 'round-octagon', text: 'GOAL' },
};
const GOLD = { fill: '#ffd54a', border: '#8a6100', halo: '#f2b705' };

function sizeOf(node) {
  return ROLE[node.role] ? ROLE[node.role].size : SIZE[node.type];
}
const COLORS = {
  access: { fill: '#dbe9f8', border: '#3b6ea8' },
  lock: { fill: '#f6d0cf', border: '#b23a36' },
  key: { fill: '#d5ecd1', border: '#3c8a36' },
};
// Separate colour-blind-friendly palettes: environment biomes colour node borders, encounter themes the centre dot.
const ENV_PALETTE = ['#6a3d9a', '#8c510a', '#01665e', '#7f3b08', '#2d004b', '#543005'];
const ENC_PALETTE = ['#e69f00', '#56b4e9', '#009e73', '#cc79a7', '#0072b2', '#d55e00', '#999933', '#882255'];
const SHORT = {
  CLOSED: 'CLOSED', OPEN: 'OPEN', PERMANENT: 'PERM', TEMPORARY: 'TEMP', DUNGEON: 'DUNGEON',
  REQUIRED: 'REQ', OPTIONAL: 'OPT', FAILABLE: 'FAIL', REUSABLE: 'REUSE', CONSUMABLE: 'CONS',
  PRIMARY: 'PRIMARY', SPARE: 'SPARE', CLUE: 'CLUE',
};
const TOOLTIP_FIELDS = [
  ['role', 'Role'], ['type', 'Type'], ['created_by', 'Created by'], ['depth', 'Depth'],
  ['logic_gate', 'Logic gate'], ['lock_state', 'Base state'], ['open_mode', 'Open mode'], ['access_mode', 'Access'],
  ['reusability', 'Key usage'], ['key_type', 'Key type'], ['lock', 'Opens lock'], ['keys', 'Keys'], ['locks', 'Locks'],
  ['env_biome', 'Environment biome'], ['enc_biome', 'Encounter biomes'], ['archetype', 'Archetype'], ['flavour', 'Flavour'],
  ['complexity', 'Complexity'],
];

const $ = (id) => document.getElementById(id);
const state = { derivation: null, frame: 0, positions: {}, biomeColors: {}, playTimer: null, productions: [] };

const cy = cytoscape({
  container: $('graph'),
  boxSelectionEnabled: false,
  autoungrabify: true,
  style: [
    {
      selector: 'node',
      style: {
        label: 'data(label)', 'text-wrap': 'wrap', 'font-size': 12, 'text-valign': 'center', 'text-halign': 'center',
        width: 'data(w)', height: 'data(h)', 'background-color': 'data(fill)', 'border-color': 'data(border)',
        'border-width': 2, color: '#1f2328',
        'text-background-color': '#f6f5f2', 'text-background-opacity': 0.85, 'text-background-padding': 2,
        'text-background-shape': 'round-rectangle',
      },
    },
    { selector: 'node[type="access"]', style: { shape: 'round-rectangle' } },
    { selector: 'node[type="lock"]', style: { shape: 'diamond' } },
    { selector: 'node[type="key"]', style: { shape: 'ellipse' } },
    { selector: 'node[envColor]', style: { 'border-color': 'data(envColor)', 'border-width': 5 } },
    {
      selector: 'node[pieCount > 0]',
      style: {
        'pie-size': '38%', 'pie-1-background-color': 'data(pie1)', 'pie-1-background-size': 'data(pieShare1)',
        'pie-2-background-color': 'data(pie2)', 'pie-2-background-size': 'data(pieShare2)',
        'pie-3-background-color': 'data(pie3)', 'pie-3-background-size': 'data(pieShare3)',
        'pie-4-background-color': 'data(pie4)', 'pie-4-background-size': 'data(pieShare4)',
      },
    },
    {
      selector: 'node[role]',
      style: {
        'background-color': GOLD.fill, 'font-weight': 'bold', 'font-size': 13,
        'underlay-color': GOLD.halo, 'underlay-opacity': 0.45, 'underlay-padding': 9, 'underlay-shape': 'ellipse',
      },
    },
    { selector: 'node[role="start"]', style: { shape: ROLE.start.shape } },
    { selector: 'node[role="goal"]', style: { shape: ROLE.goal.shape } },
    { selector: 'node[role][^envColor]', style: { 'border-color': GOLD.border, 'border-width': 3 } },
    { selector: 'node.with-badge', style: { label: 'data(labelWithBadge)', 'text-valign': 'bottom', 'text-margin-y': 4 } },
    { selector: 'node.added', style: { 'overlay-color': '#f2b705', 'overlay-opacity': 0.35, 'overlay-padding': 6 } },
    { selector: 'node.changed', style: { 'overlay-color': '#f2b705', 'overlay-opacity': 0.18, 'overlay-padding': 4 } },
    {
      selector: 'edge',
      style: { width: 2, 'curve-style': 'bezier', 'target-arrow-shape': 'triangle', 'arrow-scale': 0.9 },
    },
    { selector: 'edge[mode="access"]', style: { 'line-color': '#7b8794', 'target-arrow-color': '#7b8794' } },
    {
      selector: 'edge[mode="unlocks"]',
      style: {
        'line-color': '#b23a36', 'target-arrow-color': '#b23a36', 'line-style': 'dashed',
        'curve-style': 'unbundled-bezier', 'control-point-distances': 40, 'control-point-weights': 0.5, opacity: 0.8,
      },
    },
    { selector: 'edge.added', style: { 'line-color': '#f2b705', 'target-arrow-color': '#f2b705', width: 4 } },
    { selector: 'edge.removed', style: { opacity: 0.35, 'line-style': 'dotted', 'line-color': '#9aa4b2', 'target-arrow-color': '#9aa4b2' } },
    { selector: '.hover', style: { 'underlay-color': '#2f6fb3', 'underlay-opacity': 0.25, 'underlay-padding': 6 } },
  ],
});

// ---------- parameters and URL ----------

function readParams() {
  const params = {
    seed: parseInt($('seed').value, 10) || 0,
    steps: Math.min(200, Math.max(0, parseInt($('steps').value, 10) || 0)),
    env: $('env').checked ? 1 : 0,
    enc: $('enc').checked ? 1 : 0,
  };
  for (const production of state.productions) {
    const enabled = $(`use-${production.name}`).checked;
    params[`w_${production.name}`] = enabled ? Math.max(0, parseFloat($(`weight-${production.name}`).value) || 0) : 0;
  }
  return params;
}

function writeParams(params) {
  if ('seed' in params) $('seed').value = params.seed;
  if ('steps' in params) $('steps').value = params.steps;
  if ('env' in params) $('env').checked = params.env === '1';
  if ('enc' in params) $('enc').checked = params.enc === '1';
  for (const production of state.productions) {
    const key = `w_${production.name}`;
    if (key in params) {
      const weight = parseFloat(params[key]);
      $(`use-${production.name}`).checked = weight > 0;
      if (weight > 0) $(`weight-${production.name}`).value = weight;
    }
  }
}

function paramsFromHash() {
  return Object.fromEntries(new URLSearchParams(location.hash.slice(1)));
}

// ---------- generation ----------

async function generate() {
  stopPlaying();
  const params = readParams();
  const query = new URLSearchParams(params).toString();
  history.replaceState(null, '', `#${query}`);
  $('error').hidden = true;
  try {
    const response = await fetch(`api/derive?${query}`);
    const body = await response.json();
    if (!response.ok) throw new Error(body.error || response.statusText);
    state.derivation = body;
  } catch (error) {
    showError(`Generation failed: ${error.message}`);
    return;
  }
  computeLayout();
  assignBiomeColors();
  renderTimeline();
  showFrame(state.derivation.frames.length - 1, { fit: true });
  renderLegend();
}

// Layout once per derivation, on the final graph and access edges only, so nodes keep their place across steps.
function computeLayout() {
  const frames = state.derivation.frames;
  const final = frames[frames.length - 1].graph;
  const g = new dagre.graphlib.Graph();
  g.setGraph({ rankdir: 'TB', nodesep: 46, ranksep: 70, marginx: 20, marginy: 20 });
  g.setDefaultEdgeLabel(() => ({}));
  const allNodes = new Map();
  for (const frame of frames) for (const node of frame.graph.nodes) allNodes.set(node.id, node);
  for (const node of allNodes.values()) {
    const [w, h] = sizeOf(node);
    g.setNode(node.id, { width: w + 70, height: h + 34 });
  }
  for (const edge of final.edges) if (edge.mode === 'access') g.setEdge(edge.source, edge.target);
  dagre.layout(g);
  state.positions = Object.fromEntries(g.nodes().map((id) => [id, { x: g.node(id).x, y: g.node(id).y }]));
}

function assignBiomeColors() {
  const names = new Set();
  for (const node of state.derivation.export.nodes) {
    if (node.env_biome) names.add(`env:${node.env_biome}`);
    for (const theme of node.enc_biome || []) names.add(`enc:${theme}`);
  }
  state.biomeColors = {};
  const sorted = [...names].sort();
  for (const [prefix, palette] of [['env:', ENV_PALETTE], ['enc:', ENC_PALETTE]]) {
    sorted.filter((name) => name.startsWith(prefix))
      .forEach((name, index) => { state.biomeColors[name] = palette[index % palette.length]; });
  }
}

// ---------- rendering ----------

function badge(node) {
  if (node.type === 'lock') {
    return [node.logic_gate, SHORT[node.lock_state], SHORT[node.open_mode], SHORT[node.access_mode]].join(' · ');
  }
  if (node.type === 'key') return [SHORT[node.reusability], SHORT[node.key_type]].join(' · ');
  return node.depth === null || node.depth === undefined ? '' : `depth ${node.depth}`;
}

function nodeElement(node) {
  const [w, h] = sizeOf(node);
  const name = ROLE[node.role] ? `${ROLE[node.role].text} · ${node.id}` : node.id;
  const data = {
    ...node, label: name, labelWithBadge: `${name}\n${badge(node)}`, w, h,
    fill: COLORS[node.type].fill, border: COLORS[node.type].border,
  };
  if (node.env_biome) data.envColor = state.biomeColors[`env:${node.env_biome}`];
  // encounter themes as up to 4 equal pie slices; unused slices stay transparent and empty
  const themes = (node.enc_biome || []).slice(0, 4);
  data.pieCount = themes.length;
  for (let slice = 1; slice <= 4; slice += 1) {
    const theme = themes[slice - 1];
    data[`pie${slice}`] = theme ? state.biomeColors[`enc:${theme}`] : 'transparent';
    data[`pieShare${slice}`] = theme ? 100 / themes.length : 0;
  }
  return { group: 'nodes', data, position: { ...state.positions[node.id] } };
}

function edgeId(edge) {
  return `${edge.source}->${edge.target}:${edge.mode}`;
}

function showFrame(index, { fit = false } = {}) {
  const frames = state.derivation.frames;
  state.frame = Math.max(0, Math.min(index, frames.length - 1));
  const frame = frames[state.frame];
  const added = new Set(frame.added_nodes);
  const changed = new Set(frame.changed_nodes);
  const addedEdges = new Set(frame.added_edges.map(([source, target, mode]) => edgeId({ source, target, mode })));
  const showBadges = $('show-attributes').checked;
  const highlight = state.frame > 0;

  const elements = frame.graph.nodes.map((node) => {
    const element = nodeElement(node);
    element.classes = [
      showBadges ? 'with-badge' : '',
      highlight && added.has(node.id) ? 'added' : '',
      highlight && changed.has(node.id) ? 'changed' : '',
    ].join(' ');
    return element;
  });
  for (const edge of frame.graph.edges) {
    elements.push({
      group: 'edges', data: { id: edgeId(edge), ...edge }, classes: highlight && addedEdges.has(edgeId(edge)) ? 'added' : '',
    });
  }
  if (highlight && $('show-removed').checked) {
    for (const [source, target, mode] of frame.removed_edges) {
      elements.push({ group: 'edges', data: { id: `removed:${source}->${target}:${mode}`, source, target, mode, removed: true }, classes: 'removed' });
    }
  }
  cy.batch(() => {
    cy.elements().remove();
    cy.add(elements);
  });
  if (fit) cy.fit(undefined, 40);

  $('frame').max = frames.length - 1;
  $('frame').value = state.frame;
  $('status-seed').textContent = `Seed ${state.derivation.seed}`;
  $('status-frame').textContent = `${frame.title} · ${state.frame + 1}/${frames.length}`
    + ` · ${state.derivation.productions_applied} productions applied`
    + (state.derivation.productions_applied < state.derivation.params.steps ? ' (no enabled production matched any more)' : '');
  document.querySelectorAll('#frames li').forEach((li, i) => li.classList.toggle('current', i === state.frame));
  revealCurrentChip();
}

// Scroll only the chip strip (scrollIntoView would also scroll the page).
function revealCurrentChip() {
  const list = $('frames');
  const chip = list.querySelector('li.current');
  if (!chip) return;
  const left = chip.offsetLeft - list.offsetLeft;
  if (left < list.scrollLeft) list.scrollLeft = left - 8;
  else if (left + chip.offsetWidth > list.scrollLeft + list.clientWidth) {
    list.scrollLeft = left + chip.offsetWidth - list.clientWidth + 8;
  }
}

function renderTimeline() {
  const list = $('frames');
  list.replaceChildren(...state.derivation.frames.map((frame, index) => {
    const li = document.createElement('li');
    li.textContent = frame.title;
    li.addEventListener('click', () => { stopPlaying(); showFrame(index); });
    return li;
  }));
}

function legendItem(swatchClass, color, text, fill) {
  const item = document.createElement('div');
  item.className = 'legend-item';
  const swatch = document.createElement('span');
  swatch.className = `swatch ${swatchClass}`;
  swatch.style.borderColor = color;
  if (fill) swatch.style.background = fill;
  const label = document.createElement('span');
  label.textContent = text;
  item.append(swatch, label);
  return item;
}

function renderLegend() {
  const items = [
    legendItem('access', COLORS.access.border, 'Area (access node)', COLORS.access.fill),
    legendItem('lock', COLORS.lock.border, 'Lock: gate · state · mode · access', COLORS.lock.fill),
    legendItem('key', COLORS.key.border, 'Key: usage · type', COLORS.key.fill),
    legendItem('lock', GOLD.border, 'START: entrance lock, the player begins in the area it opens', GOLD.fill),
    legendItem('key', GOLD.border, 'GOAL: the dungeon key, the zone objective', GOLD.fill),
    legendItem('edge', '#7b8794', 'access: makes reachable'),
    legendItem('edge unlocks', '#b23a36', 'unlocks: key opens lock'),
    legendItem('edge', '#f2b705', 'added in this step'),
  ];
  for (const [name, color] of Object.entries(state.biomeColors)) {
    const [kind, biome] = name.split(':');
    items.push(kind === 'env'
      ? legendItem('access', color, `Environment: ${biome} (border)`)
      : legendItem('dot', color, `Encounter: ${biome} (centre dot)`, color));
  }
  $('legend').replaceChildren(...items);
}

// ---------- hover ----------

function formatValue(value) {
  if (Array.isArray(value)) return value.length ? value.join(', ') : '–';
  return value === null || value === undefined ? '–' : String(value);
}

// Archetype name (with its status unless confirmed) and play pattern, from the derivation's archetype table.
function addArchetypeRows(addRow, id) {
  const archetype = state.derivation.archetypes[id];
  if (!archetype) {
    addRow('Archetype', id);
    return;
  }
  addRow('Archetype', archetype.status === 'named' ? archetype.name : `${archetype.name} (${archetype.status})`);
  if (archetype.play_pattern) addRow('Play pattern', archetype.play_pattern);
}

function showTooltip(event) {
  const element = event.target;
  element.addClass('hover');
  const tooltip = $('tooltip');
  const data = element.data();
  const heading = document.createElement('h3');
  const table = document.createElement('table');
  const addRow = (name, value) => {
    const row = table.insertRow();
    row.insertCell().textContent = name;
    row.insertCell().textContent = formatValue(value);
  };
  if (element.isNode()) {
    heading.textContent = data.id;
    for (const [field, name] of TOOLTIP_FIELDS) {
      if (!(field in data)) continue;
      if (field === 'archetype') addArchetypeRows(addRow, data.archetype);
      else addRow(name, data[field]);
    }
  } else {
    heading.textContent = data.mode === 'unlocks'
      ? `${data.source} unlocks ${data.target}` : `${data.source} → ${data.target} (access)`;
    if (data.removed) addRow('Change', 'removed in this step');
  }
  tooltip.replaceChildren(heading, table);
  tooltip.hidden = false;
  moveTooltip(event);
}

function moveTooltip(event) {
  const tooltip = $('tooltip');
  const graph = $('graph').getBoundingClientRect();
  const main = document.querySelector('main').getBoundingClientRect();
  const { x, y } = event.renderedPosition;
  let left = graph.left - main.left + x + 16;
  let top = graph.top - main.top + y + 16;
  if (left + tooltip.offsetWidth > main.width) left -= tooltip.offsetWidth + 32;
  if (top + tooltip.offsetHeight > main.height) top -= tooltip.offsetHeight + 32;
  tooltip.style.left = `${left}px`;
  tooltip.style.top = `${top}px`;
}

function hideTooltip() {
  cy.elements('.hover').removeClass('hover');
  $('tooltip').hidden = true;
}

cy.on('mouseover', 'node, edge', showTooltip);
cy.on('mousemove', 'node, edge', moveTooltip);
cy.on('mouseout', 'node, edge', hideTooltip);
// Cytoscape sends no mouseout when the pointer leaves the canvas over an element
$('graph').addEventListener('mouseleave', hideTooltip);

// ---------- playback ----------

function stopPlaying() {
  clearInterval(state.playTimer);
  state.playTimer = null;
  $('play').textContent = '▶︎';
}

function togglePlay() {
  if (!state.derivation) return;
  if (state.playTimer) { stopPlaying(); return; }
  if (state.frame >= state.derivation.frames.length - 1) showFrame(0);
  $('play').textContent = '⏸';
  state.playTimer = setInterval(() => {
    if (state.frame >= state.derivation.frames.length - 1) stopPlaying();
    else showFrame(state.frame + 1);
  }, 700);
}

// ---------- export ----------

function baseName() {
  const frame = state.derivation.frames[state.frame];
  const step = frame.title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  return `explorio-seed${state.derivation.seed}-${step}`;
}

function download(name, blob) {
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = name;
  link.click();
  setTimeout(() => URL.revokeObjectURL(link.href), 1000);
}

function caption() {
  return `Explorio story graph · seed ${state.derivation.seed} · ${state.derivation.frames[state.frame].title}`;
}

function showError(message) {
  $('error').textContent = message;
  $('error').hidden = false;
}

// Run an export and show its failure in the sidebar instead of losing it as an unhandled rejection.
async function runExport(name, exporter) {
  $('error').hidden = true;
  try {
    await exporter();
  } catch (error) {
    showError(`${name} export failed: ${error.message}`);
  }
}

function exportJson() {
  const blob = new Blob([JSON.stringify(state.derivation.export, null, 2)], { type: 'application/json' });
  download(`explorio-seed${state.derivation.seed}.json`, blob);
}

// Chromium rejects canvases over about 268 million pixels or 32767 px per side; stay well below both.
const PNG_MAX_PIXELS = 100e6;
const PNG_MAX_SIDE = 16000;

function pngScale() {
  const box = cy.elements().boundingBox();
  return Math.min(2, Math.sqrt(PNG_MAX_PIXELS / (box.w * box.h)), PNG_MAX_SIDE / box.w, PNG_MAX_SIDE / box.h);
}

async function exportPng() {
  const graphImage = new Image();
  graphImage.src = cy.png({ full: true, scale: pngScale(), bg: '#ffffff' });
  await graphImage.decode();
  const captionHeight = 56;
  const canvas = document.createElement('canvas');
  canvas.width = graphImage.width;
  canvas.height = graphImage.height + captionHeight;
  const context = canvas.getContext('2d');
  context.fillStyle = '#ffffff';
  context.fillRect(0, 0, canvas.width, canvas.height);
  context.fillStyle = '#1f2328';
  context.font = '600 26px system-ui, sans-serif';
  context.fillText(caption(), 20, 38);
  context.drawImage(graphImage, 0, captionHeight);
  const blob = await new Promise((resolve) => canvas.toBlob(resolve, 'image/png'));
  if (!blob) throw new Error('the browser could not encode the image');
  download(`${baseName()}.png`, blob);
}

function escapeXml(text) {
  return String(text).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
}

// Encounter themes as equal slices of a centre dot, matching the canvas pie (pie-size 38%).
function encounterSlicesSvg(node, tx, ty) {
  const count = node.data('pieCount');
  if (!count) return [];
  const { x, y } = node.position();
  const radius = (0.38 * Math.min(node.data('w'), node.data('h'))) / 2;
  if (count === 1) return [`<circle cx="${tx(x)}" cy="${ty(y)}" r="${radius.toFixed(1)}" fill="${node.data('pie1')}"/>`];
  return Array.from({ length: count }, (_, i) => {
    const start = -Math.PI / 2 + (i * 2 * Math.PI) / count;
    const end = start + (2 * Math.PI) / count;
    const [x1, y1] = [x + radius * Math.cos(start), y + radius * Math.sin(start)];
    const [x2, y2] = [x + radius * Math.cos(end), y + radius * Math.sin(end)];
    const largeArc = end - start > Math.PI ? 1 : 0;
    return `<path d="M${tx(x)},${ty(y)} L${tx(x1)},${ty(y1)} A${radius.toFixed(1)},${radius.toFixed(1)} 0 ${largeArc} 1 ${tx(x2)},${ty(y2)} Z" fill="${node.data(`pie${i + 1}`)}"/>`;
  });
}

function starPoints(x, y, radius) {
  return Array.from({ length: 10 }, (_, i) => {
    const r = i % 2 === 0 ? radius : radius * 0.45;
    const angle = -Math.PI / 2 + (i * Math.PI) / 5;
    return [x + r * Math.cos(angle), y + r * Math.sin(angle)];
  });
}

function octagonPoints(x, y, radius) {
  return Array.from({ length: 8 }, (_, i) => {
    const angle = Math.PI / 8 + (i * Math.PI) / 4;
    return [x + radius * Math.cos(angle), y + radius * Math.sin(angle)];
  });
}

// SVG of the current step, drawn from model positions (no viewport transform).
function exportSvg() {
  const box = cy.elements().boundingBox();
  const pad = 30;
  const top = 50;
  const width = Math.ceil(box.w + 2 * pad);
  const height = Math.ceil(box.h + 2 * pad + top);
  const tx = (x) => (x - box.x1 + pad).toFixed(1);
  const ty = (y) => (y - box.y1 + pad + top).toFixed(1);
  const parts = [
    `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" font-family="system-ui, sans-serif">`,
    '<defs>',
    '<marker id="arrow-access" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="#7b8794"/></marker>',
    '<marker id="arrow-unlocks" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="#b23a36"/></marker>',
    '</defs>',
    `<rect width="100%" height="100%" fill="#ffffff"/>`,
    `<text x="${pad}" y="32" font-size="16" font-weight="600" fill="#1f2328">${escapeXml(caption())}</text>`,
  ];
  cy.edges().forEach((edge) => {
    if (edge.hasClass('removed')) return;
    const [s, t] = [edge.sourceEndpoint(), edge.targetEndpoint()];
    const mode = edge.data('mode');
    const color = mode === 'unlocks' ? '#b23a36' : '#7b8794';
    const dash = mode === 'unlocks' ? ' stroke-dasharray="6 4"' : '';
    parts.push(`<line x1="${tx(s.x)}" y1="${ty(s.y)}" x2="${tx(t.x)}" y2="${ty(t.y)}" stroke="${color}" stroke-width="2"${dash} marker-end="url(#arrow-${mode})"/>`);
  });
  cy.nodes().forEach((node) => {
    const { x, y } = node.position();
    const w = node.data('w');
    const h = node.data('h');
    const fill = node.data('fill');
    const stroke = node.data('envColor') || node.data('border');
    const strokeWidth = node.data('envColor') ? 4 : 2;
    const attrs = `fill="${fill}" stroke="${stroke}" stroke-width="${strokeWidth}"`;
    const type = node.data('type');
    const role = node.data('role');
    if (role) {
      // gold halo, then a star (start) or octagon (goal)
      parts.push(`<circle cx="${tx(x)}" cy="${ty(y)}" r="${w / 2 + 9}" fill="${GOLD.halo}" fill-opacity="0.45"/>`);
      const points = role === 'start' ? starPoints(x, y, w / 2) : octagonPoints(x, y, w / 2);
      const roleStroke = node.data('envColor') || GOLD.border;
      parts.push(`<polygon points="${points.map(([px, py]) => `${tx(px)},${ty(py)}`).join(' ')}" fill="${GOLD.fill}" stroke="${roleStroke}" stroke-width="3"/>`);
    } else if (type === 'access') {
      parts.push(`<rect x="${tx(x - w / 2)}" y="${ty(y - h / 2)}" width="${w}" height="${h}" rx="8" ${attrs}/>`);
    } else if (type === 'lock') {
      parts.push(`<polygon points="${tx(x)},${ty(y - h / 2)} ${tx(x + w / 2)},${ty(y)} ${tx(x)},${ty(y + h / 2)} ${tx(x - w / 2)},${ty(y)}" ${attrs}/>`);
    } else {
      parts.push(`<ellipse cx="${tx(x)}" cy="${ty(y)}" rx="${w / 2}" ry="${h / 2}" ${attrs}/>`);
    }
    parts.push(...encounterSlicesSvg(node, tx, ty));
    const lines = node.hasClass('with-badge') ? node.data('labelWithBadge').split('\n') : [node.data('label')];
    const firstLineY = node.hasClass('with-badge') ? y + h / 2 + 14 : y + 4;
    lines.forEach((line, index) => {
      parts.push(`<text x="${tx(x)}" y="${ty(firstLineY + index * 13)}" font-size="11" text-anchor="middle" fill="#1f2328">${escapeXml(line)}</text>`);
    });
  });
  parts.push('</svg>');
  download(`${baseName()}.svg`, new Blob([parts.join('\n')], { type: 'image/svg+xml' }));
}

// ---------- wiring ----------

async function loadProductions() {
  const response = await fetch('api/productions');
  state.productions = await response.json();
  $('productions').replaceChildren(...state.productions.map((production) => {
    const row = document.createElement('div');
    row.className = 'production';
    row.innerHTML = `<input id="use-${production.name}" type="checkbox" checked aria-label="Enable ${production.name}">`
      + `<label for="use-${production.name}">${production.name}<small></small></label>`
      + `<input id="weight-${production.name}" type="number" min="0" step="0.5" value="1" title="Relative weight" aria-label="Weight of ${production.name}">`;
    row.querySelector('small').textContent = production.description;
    return row;
  }));
}

function bind() {
  $('generate').addEventListener('click', generate);
  $('random-seed').addEventListener('click', () => { $('seed').value = Math.floor(Math.random() * 2 ** 31); generate(); });
  document.querySelectorAll('#sidebar input[type=number]').forEach((input) => {
    input.addEventListener('keydown', (event) => { if (event.key === 'Enter') generate(); });
  });
  $('first').addEventListener('click', () => { stopPlaying(); showFrame(0); });
  $('back').addEventListener('click', () => { stopPlaying(); showFrame(state.frame - 1); });
  $('forward').addEventListener('click', () => { stopPlaying(); showFrame(state.frame + 1); });
  $('last').addEventListener('click', () => { stopPlaying(); showFrame(Infinity); });
  $('play').addEventListener('click', togglePlay);
  $('frame').addEventListener('input', (event) => { stopPlaying(); showFrame(parseInt(event.target.value, 10)); });
  $('show-attributes').addEventListener('change', () => showFrame(state.frame));
  $('show-removed').addEventListener('change', () => showFrame(state.frame));
  $('fit').addEventListener('click', () => cy.fit(undefined, 40));
  $('export-json').addEventListener('click', () => runExport('JSON', exportJson));
  $('export-png').addEventListener('click', () => runExport('PNG', exportPng));
  $('export-svg').addEventListener('click', () => runExport('SVG', exportSvg));
  document.addEventListener('keydown', (event) => {
    // fields keep all their keys; a focused button keeps Space and Enter (they press it), arrows still step
    if (!state.derivation || ['INPUT', 'SELECT', 'TEXTAREA'].includes(event.target.tagName)) return;
    if (event.target.tagName === 'BUTTON' && [' ', 'Enter'].includes(event.key)) return;
    const actions = {
      ArrowLeft: () => showFrame(state.frame - 1), ArrowRight: () => showFrame(state.frame + 1),
      Home: () => showFrame(0), End: () => showFrame(Infinity), ' ': togglePlay,
    };
    if (actions[event.key]) {
      event.preventDefault();
      if (event.key !== ' ') stopPlaying();
      actions[event.key]();
    }
  });
}

async function start() {
  bind();
  await loadProductions();
  writeParams(paramsFromHash());
  await generate();
  // generate() updates the hash with replaceState, which fires no hashchange; this reacts to edits and back/forward
  window.addEventListener('hashchange', () => { writeParams(paramsFromHash()); generate(); });
}

start();
