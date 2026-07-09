/* BPA interactive viewer.
 * Consumes window.BPA (injected at build time by tools/build_bpa.py):
 *   client   {name, period, title, intro_html, labels{}}
 *   domains  [{number, title, intro_html, process, scenarios:[codes]}]
 *   scenarios{ code: {code,title,section,domain,fit,addon,gap,status,requirements:[],html} }
 *   coverage [{code,title,domain,scope,fit,note}]
 *   requirements [{id,title,source,html,scenarios:[]}]
 *   gaps     [{id,title,html,scenarios:[]}]
 * Fit values: "standard" | "addon" | "workaround" | "gap" | "none".
 */
(function () {
  "use strict";
  var D = window.BPA;
  if (!D) { document.getElementById("app").textContent = "Geen BPA-data gevonden."; return; }

  // Built-in language packs. Add a language: add a key here (and translate the
  // process-flow labels); per-client overrides go in bpa-config.json "labels".
  var LANGS = {
    nl: {
      processes: "Processen", scope: "Scope", requirements: "Requirements", gaps: "GAPs",
      intro: "Inleiding", search: "Zoek scenario of code…", inScope: "in scope",
      outScope: "buiten scope", legendStandard: "Standaard BC", legendAddon: "Add-on",
      legendWorkaround: "Workaround", legendGap: "GAP (maatwerk)", legendNone: "Niet gedocumenteerd",
      otherScenarios: "Alle scenario's in dit domein", noResults: "Geen resultaten",
      gotoProcess: "Ga naar processtroom", metRequirements: "Gekoppelde requirements",
      fit: { standard: "Standaard BC", addon: "Add-on", workaround: "Workaround", gap: "GAP", none: "—" },
      domainDocOnly: "Voor dit domein is geen processtroom gedefinieerd; de scenario's staan hieronder.",
      scopeCols: ["Code", "Scenario", "Domein", "Scope", "Invulling", "Toelichting"],
      filterAll: "alle", generated: "opgemaakt",
      catalog: { verified: "Catalogus: geverifieerd", unverified: "Catalogus: nog niet geverifieerd",
                candidate: "Catalogus: nieuw voorstel", retired: "Catalogus: retired ⚠" },
      exportBtn: "PDF exporteren", exportTitle: "Exporteer als PDF",
      exportHint: "Kies wat het document bevat. Het afdrukvenster opent — kies daar ‘Opslaan als PDF’.",
      exportDomains: "Domeinen", exportParts: "Onderdelen",
      exportAllNone: "alles / niets", exportGo: "Maak PDF", exportCancel: "Annuleer",
      toc: "Inhoud", coverClient: "Klant", coverPeriod: "Periode",
      coverVersion: "Versie", coverDate: "Datum", coverModel: "Procesmodel"
    },
    en: {
      processes: "Processes", scope: "Scope", requirements: "Requirements", gaps: "GAPs",
      intro: "Introduction", search: "Search scenario or code…", inScope: "in scope",
      outScope: "out of scope", legendStandard: "Standard BC", legendAddon: "Add-on",
      legendWorkaround: "Workaround", legendGap: "GAP (customisation)", legendNone: "Not documented",
      otherScenarios: "All scenarios in this domain", noResults: "No results",
      gotoProcess: "Go to process flow", metRequirements: "Linked requirements",
      fit: { standard: "Standard BC", addon: "Add-on", workaround: "Workaround", gap: "GAP", none: "—" },
      domainDocOnly: "No process flow is defined for this domain; its scenarios are listed below.",
      scopeCols: ["Code", "Scenario", "Domain", "Scope", "Coverage", "Notes"],
      filterAll: "all", generated: "generated",
      catalog: { verified: "Catalog: verified", unverified: "Catalog: not yet verified",
                candidate: "Catalog: new proposal", retired: "Catalog: retired ⚠" },
      exportBtn: "Export PDF", exportTitle: "Export as PDF",
      exportHint: "Choose what the document contains. The print dialog opens — pick ‘Save as PDF’ there.",
      exportDomains: "Domains", exportParts: "Sections",
      exportAllNone: "all / none", exportGo: "Create PDF", exportCancel: "Cancel",
      toc: "Contents", coverClient: "Client", coverPeriod: "Period",
      coverVersion: "Version", coverDate: "Date", coverModel: "Process model"
    }
  };
  var lang = D.client.language || "nl";
  var L = Object.assign({}, LANGS.nl, LANGS[lang] || {}, D.client.labels || {});
  L.fit = Object.assign({}, LANGS.nl.fit, (LANGS[lang] || {}).fit || {}, (D.client.labels || {}).fit || {});

  // Process-flow labels may be plain strings or {nl: "...", en: "..."} objects.
  function lbl(v) {
    if (v && typeof v === "object") return v[lang] || v.nl || v.en || "";
    return v || "";
  }

  var app = document.getElementById("app");
  var domByNum = {};
  D.domains.forEach(function (d) { domByNum[d.number] = d; });

  /* ---------------- helpers ---------------- */
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function el(html) {
    var t = document.createElement("template");
    t.innerHTML = html.trim();
    return t.content.firstChild;
  }
  function scen(code) { return D.scenarios[code]; }
  function fitOf(code) {
    var s = scen(code);
    return s && s.fit ? s.fit : "none";
  }
  function fitChip(fit, addon) {
    var lbl = fit === "addon" && addon ? L.fit.addon + ": " + addon : (L.fit[fit] || fit);
    return '<span class="chip ' + esc(fit) + '">' + esc(lbl) + "</span>";
  }
  function catalogNote(code) {
    var s = scen(code);
    if (!s || !s.catalog_status) return "";
    var label = (L.catalog && L.catalog[s.catalog_status]) || s.catalog_status;
    var suffix = s.catalog_last_verified ? " · " + esc(s.catalog_last_verified) : "";
    return '<span class="cat-note cat-' + esc(s.catalog_status) + '">' + esc(label) + suffix + "</span>";
  }
  function wrapText(text, max) {
    var words = String(text).split(/\s+/), lines = [], cur = "";
    words.forEach(function (w) {
      if ((cur + " " + w).trim().length > max && cur) { lines.push(cur); cur = w; }
      else cur = (cur + " " + w).trim();
    });
    if (cur) lines.push(cur);
    return lines;
  }

  /* ---------------- BPMN layout ---------------- */
  var NW = 176, NH = 56, GX = 78, ROW = 92, LANE_PAD = 14, CORR = 34, LBL_W = 34, M = 16;

  function shapeHalf(n) {
    if (n.type === "start" || n.type === "end") return { w: 20, h: 20 };
    if (n.type.indexOf("gateway") === 0) return { w: 26, h: 26 };
    return { w: NW / 2, h: NH / 2 };
  }

  function layoutProcess(p) {
    var byId = {}, out = {}, incoming = {};
    p.nodes.forEach(function (n) { byId[n.id] = n; out[n.id] = []; incoming[n.id] = 0; });
    p.flows.forEach(function (f) { out[f.from].push(f.to); });

    // classify back edges with DFS from start nodes (then any unvisited)
    var back = {}, state = {}; // 0 unseen, 1 on stack, 2 done
    function dfs(u) {
      state[u] = 1;
      out[u].forEach(function (v) {
        if (state[v] === 1) back[u + ">" + v] = true;
        else if (!state[v]) dfs(v);
      });
      state[u] = 2;
    }
    p.nodes.filter(function (n) { return n.type === "start"; }).forEach(function (n) { if (!state[n.id]) dfs(n.id); });
    p.nodes.forEach(function (n) { if (!state[n.id]) dfs(n.id); });

    var fwd = p.flows.filter(function (f) { return !back[f.from + ">" + f.to]; });
    fwd.forEach(function (f) { incoming[f.to]++; });

    // longest-path layering (Kahn)
    var layer = {}, q = [];
    p.nodes.forEach(function (n) { layer[n.id] = 0; if (!incoming[n.id]) q.push(n.id); });
    var order = [], deg = Object.assign({}, incoming);
    while (q.length) {
      var u = q.shift(); order.push(u);
      fwd.forEach(function (f) {
        if (f.from !== u) return;
        if (layer[f.to] < layer[u] + 1) layer[f.to] = layer[u] + 1;
        if (--deg[f.to] === 0) q.push(f.to);
      });
    }

    // rows per (lane, layer)
    var laneIdx = {}, laneRows = {};
    p.lanes.forEach(function (l, i) { laneIdx[l.id] = i; laneRows[l.id] = 1; });
    var cellCount = {};
    var rowOf = {};
    p.nodes.forEach(function (n) {
      var key = n.lane + "|" + layer[n.id];
      rowOf[n.id] = cellCount[key] = (cellCount[key] || 0);
      cellCount[key]++;
      if (cellCount[key] > laneRows[n.lane]) laneRows[n.lane] = cellCount[key];
    });

    var lanes = [], y = M;
    p.lanes.forEach(function (l) {
      var h = LANE_PAD * 2 + laneRows[l.id] * ROW + CORR;
      lanes.push({ id: l.id, label: l.label, y: y, h: h });
      y += h;
    });
    var laneBy = {}; lanes.forEach(function (l) { laneBy[l.id] = l; });

    var maxLayer = 0;
    p.nodes.forEach(function (n) { if (layer[n.id] > maxLayer) maxLayer = layer[n.id]; });
    var width = M + LBL_W + (maxLayer + 1) * (NW + GX) - GX + M + 60;
    var height = y + M;

    var pos = {};
    p.nodes.forEach(function (n) {
      var ln = laneBy[n.lane];
      pos[n.id] = {
        node: n,
        cx: M + LBL_W + layer[n.id] * (NW + GX) + NW / 2,
        cy: ln.y + LANE_PAD + rowOf[n.id] * ROW + ROW / 2 - CORR / 4,
        layer: layer[n.id]
      };
    });

    // route edges
    var edges = p.flows.map(function (f) {
      var s = pos[f.from], t = pos[f.to];
      var sh = shapeHalf(s.node), th = shapeHalf(t.node);
      var pts, labelAt;
      var isBack = back[f.from + ">" + f.to] || t.layer <= s.layer;
      if (!isBack && t.layer - s.layer > 1) {
        // long edge: route through the node-free corridor at the bottom of the
        // source lane so it never crosses nodes in the layers it skips
        var lnS = laneBy[s.node.lane];
        var corrY = lnS.y + lnS.h - CORR / 2;
        var xo = s.cx + sh.w, xi = t.cx - th.w;
        pts = [[xo, s.cy], [xo + GX / 2 - 8, s.cy], [xo + GX / 2 - 8, corrY],
               [xi - GX / 2 + 8, corrY], [xi - GX / 2 + 8, t.cy], [xi, t.cy]];
        labelAt = [xo + 8, s.cy - 7];
      } else if (!isBack) {
        var x0 = s.cx + sh.w, x1 = t.cx - th.w;
        if (Math.abs(s.cy - t.cy) < 2) {
          pts = [[x0, s.cy], [x1, t.cy]];
        } else {
          var mx = x1 - GX / 2 + 8;
          pts = [[x0, s.cy], [mx, s.cy], [mx, t.cy], [x1, t.cy]];
        }
        labelAt = [x0 + 8, s.cy - 7];
      } else {
        var ln = laneBy[s.node.lane];
        var cy = ln.y + ln.h - CORR / 2;
        pts = [[s.cx, s.cy + sh.h], [s.cx, cy], [t.cx, cy], [t.cx, t.cy + th.h]];
        labelAt = [Math.min(s.cx, t.cx) + 14, cy - 6];
      }
      return { flow: f, pts: pts, labelAt: labelAt };
    });

    return { lanes: lanes, pos: pos, edges: edges, width: width, height: height };
  }

  /* ---------------- BPMN render ---------------- */
  function svgNode(pos) {
    var n = pos.node, cx = pos.cx, cy = pos.cy;
    var s = scen(n.scenario);
    var fit = n.scenario ? fitOf(n.scenario) : null;
    var cls = "node n-" + n.type + (fit ? " fit-" + fit : "") +
      (n.scenario || n.goto ? " clickable" : "");
    var g = '<g class="' + cls + '" data-node="' + esc(n.id) + '"' +
      (n.scenario ? ' data-scenario="' + esc(n.scenario) + '"' : "") +
      (n.goto ? ' data-goto="' + esc(n.goto) + '"' : "") + ">";
    var title = lbl(n.label) || (s ? s.title : n.id);

    if (n.type === "start" || n.type === "end") {
      g += '<circle class="shape" cx="' + cx + '" cy="' + cy + '" r="20"/>';
      wrapText(title, 20).slice(0, 2).forEach(function (ln, i) {
        g += '<text class="evt-label" x="' + cx + '" y="' + (cy + 34 + i * 13) + '" text-anchor="middle">' + esc(ln) + "</text>";
      });
    } else if (n.type.indexOf("gateway") === 0) {
      var h = 26;
      g += '<path class="shape" d="M' + cx + " " + (cy - h) + " L" + (cx + h) + " " + cy +
        " L" + cx + " " + (cy + h) + " L" + (cx - h) + " " + cy + ' Z"/>';
      if (n.type === "gateway-parallel") {
        g += '<path class="gw-mark" d="M' + (cx - 9) + " " + cy + " H" + (cx + 9) + " M" + cx + " " + (cy - 9) + " V" + (cy + 9) + '"/>';
      } else {
        g += '<path class="gw-mark" d="M' + (cx - 7) + " " + (cy - 7) + " L" + (cx + 7) + " " + (cy + 7) +
          " M" + (cx + 7) + " " + (cy - 7) + " L" + (cx - 7) + " " + (cy + 7) + '"/>';
      }
      if (title) {
        var glines = wrapText(title, 18).slice(0, 2);
        var gy = cy - h - 8 - (glines.length - 1) * 13;
        glines.forEach(function (ln, i) {
          g += '<text class="gw-label" x="' + cx + '" y="' + (gy + i * 13) + '" text-anchor="middle">' + esc(ln) + "</text>";
        });
      }
    } else { // task / subprocess
      var x = cx - NW / 2, yy = cy - NH / 2;
      g += '<rect class="shape" x="' + x + '" y="' + yy + '" width="' + NW + '" height="' + NH + '" rx="9" stroke-width="2"/>';
      if (n.scenario) {
        g += '<text class="code" x="' + (x + 9) + '" y="' + (yy + 14) + '">' + esc(n.scenario) + "</text>";
      }
      var lines = wrapText(title, 26).slice(0, 2);
      var ty = cy + (n.scenario ? 6 : 0) - (lines.length - 1) * 7;
      lines.forEach(function (ln, i) {
        g += '<text class="title" x="' + cx + '" y="' + (ty + i * 15) + '" text-anchor="middle">' + esc(ln) + "</text>";
      });
      if (n.type === "subprocess") {
        var bx = cx - 7, by = yy + NH - 15;
        g += '<rect class="sub-mark" x="' + bx + '" y="' + by + '" width="14" height="14" rx="2"/>' +
          '<path class="gw-mark" style="stroke-width:1.6" d="M' + (bx + 3) + " " + (by + 7) + " H" + (bx + 11) +
          " M" + (bx + 7) + " " + (by + 3) + " V" + (by + 11) + '"/>';
      }
    }
    return g + "</g>";
  }

  function renderDiagram(p, selected) {
    var lay = layoutProcess(p);
    var s = '<svg class="bpmn" viewBox="0 0 ' + lay.width + " " + lay.height + '" width="' + lay.width + '" height="' + lay.height + '">';
    s += '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7.5" markerHeight="7.5" orient="auto-start-reverse">' +
      '<path d="M0 0 L10 5 L0 10 z" fill="#6b7c8f"/></marker></defs>';
    // lanes
    lay.lanes.forEach(function (l, i) {
      s += '<rect class="lane-band-' + (i % 2) + '" x="' + M + '" y="' + l.y + '" width="' + (lay.width - 2 * M) + '" height="' + l.h + '" stroke="#d7dee7" stroke-width="1" />';
      s += '<text class="lane-label" transform="translate(' + (M + 20) + " " + (l.y + l.h / 2) + ') rotate(-90)" text-anchor="middle">' + esc(lbl(l.label)) + "</text>";
    });
    // edges
    lay.edges.forEach(function (e) {
      var d = e.pts.map(function (pt, i) { return (i ? "L" : "M") + pt[0] + " " + pt[1]; }).join(" ");
      s += '<path class="flow" d="' + d + '" marker-end="url(#arr)"/>';
      var flabel = lbl(e.flow.label);
      if (flabel) {
        var w = flabel.length * 6 + 8;
        s += '<rect class="flow-label-bg" x="' + (e.labelAt[0] - 3) + '" y="' + (e.labelAt[1] - 10) + '" width="' + w + '" height="14" rx="3"/>' +
          '<text class="flow-label" x="' + e.labelAt[0] + '" y="' + (e.labelAt[1] + 1) + '">' + esc(flabel) + "</text>";
      }
    });
    // nodes
    p.nodes.forEach(function (n) {
      var g = svgNode(lay.pos[n.id]);
      if (selected && n.scenario === selected) g = g.replace('class="node', 'class="node selected');
      s += g;
    });
    return s + "</svg>";
  }

  /* ---------------- views ---------------- */
  function chrome(active) {
    var tabs = [["#/intro", L.intro]];
    if (D.coverage.length) tabs.push(["#/scope", L.scope]);
    if (D.requirements.length) tabs.push(["#/requirements", L.requirements]);
    if (D.gaps.length) tabs.push(["#/gaps", L.gaps]);
    var nav = tabs.map(function (t) {
      return '<a href="' + t[0] + '"' + (active === t[0] ? ' class="on"' : "") + ">" + esc(t[1]) + "</a>";
    }).join("");
    var doms = D.domains.map(function (d) {
      var cnt = d.scenarios.length;
      return '<a href="#/domain/' + d.number + '" data-dom="' + d.number + '">' +
        '<span class="n">' + d.number + "</span><span>" + esc(d.title) + "</span>" +
        (cnt ? '<span class="cnt">' + cnt + "</span>" : "") + "</a>";
    }).join("");
    app.innerHTML =
      '<header class="hdr"><div class="logo" role="img" aria-label="Cegeka"></div>' +
      '<div class="brand">' + esc(D.client.title || "Business Process Analyse") +
      "<small>" + esc(D.client.name) + (D.client.period ? " · " + esc(D.client.period) : "") + "</small></div>" +
      "<nav>" + nav + '<button class="export" id="exportbtn">⤓ ' + esc(L.exportBtn) + "</button></nav></header>" +
      '<div class="main"><aside class="side">' +
      '<div class="search"><input id="q" type="search" placeholder="' + esc(L.search) + '"></div>' +
      '<div class="domlist" id="domlist">' + doms + '</div><div class="hits" id="hits" style="display:none"></div>' +
      '</aside><section class="content"><div class="inner" id="view"></div></section></div>' +
      '<div class="panel-wrap" id="panelwrap"><div class="veil"></div><div class="panel" id="panel"></div></div>' +
      '<div class="exp-wrap" id="expwrap"><div class="veil"></div><div class="exp" id="expdlg"></div></div>';

    document.getElementById("q").addEventListener("input", onSearch);
    document.querySelector("#panelwrap .veil").addEventListener("click", closePanel);
    document.getElementById("exportbtn").addEventListener("click", openExport);
    document.querySelector("#expwrap .veil").addEventListener("click", closeExport);
  }

  /* ---------------- PDF export (print-CSS) ---------------- */
  function openExport() {
    var dlg = document.getElementById("expdlg");
    var parts = [["intro", L.intro, !!D.client.intro_html]];
    if (D.coverage.length) parts.push(["scope", L.scope, true]);
    if (D.requirements.length) parts.push(["requirements", L.requirements, true]);
    if (D.gaps.length) parts.push(["gaps", L.gaps, true]);
    dlg.innerHTML =
      "<h2>" + esc(L.exportTitle) + '</h2><p class="hint">' + esc(L.exportHint) + "</p>" +
      "<h3>" + esc(L.exportDomains) + ' — <button type="button" class="all" id="exptoggle">' + esc(L.exportAllNone) + "</button></h3>" +
      '<div class="doms">' + D.domains.map(function (d) {
        return '<label><input type="checkbox" class="expdom" value="' + d.number + '" checked>' +
          '<span class="n">' + d.number + "</span><span>" + esc(d.title) + "</span></label>";
      }).join("") + "</div>" +
      "<h3>" + esc(L.exportParts) + "</h3>" +
      parts.map(function (p) {
        return '<label><input type="checkbox" class="exppart" value="' + p[0] + '"' + (p[2] ? " checked" : " disabled") + ">" +
          "<span>" + esc(p[1]) + "</span></label>";
      }).join("") +
      '<div class="row"><span class="sp"></span>' +
      '<button type="button" class="cancel" id="expcancel">' + esc(L.exportCancel) + "</button>" +
      '<button type="button" class="go" id="expgo">' + esc(L.exportGo) + "</button></div>";
    dlg.querySelector("#expcancel").addEventListener("click", closeExport);
    dlg.querySelector("#exptoggle").addEventListener("click", function () {
      var boxes = dlg.querySelectorAll(".expdom");
      var any = Array.prototype.some.call(boxes, function (b) { return b.checked; });
      boxes.forEach(function (b) { b.checked = !any; });
    });
    dlg.querySelector("#expgo").addEventListener("click", function () {
      var doms = [];
      dlg.querySelectorAll(".expdom:checked").forEach(function (b) { doms.push(+b.value); });
      var opts = {};
      dlg.querySelectorAll(".exppart:checked").forEach(function (b) { opts[b.value] = true; });
      if (!doms.length && !Object.keys(opts).length) return;
      closeExport();
      buildPrintDoc(doms, opts);
      document.body.classList.add("printing");
      // let the print DOM paint before the dialog opens
      setTimeout(function () { window.print(); }, 60);
    });
    document.getElementById("expwrap").classList.add("open");
  }

  function closeExport() {
    document.getElementById("expwrap").classList.remove("open");
  }

  window.addEventListener("afterprint", function () {
    document.body.classList.remove("printing");
    document.getElementById("printdoc").innerHTML = "";
  });

  function printScen(code) {
    var s = scen(code);
    if (!s) return "";
    var fit = fitOf(code);
    var chips = fitChip(fit, s.addon);
    if (s.gap) chips += ' <span class="chip gap">' + esc(s.gap) + "</span>";
    (s.requirements || []).forEach(function (r) {
      chips += ' <span class="chip req">' + esc(r) + "</span>";
    });
    var cat = catalogNote(code);
    return '<div class="pv-scen"><div class="codes"><code>' + esc(code) + "</code>" +
      (s.section ? " · § " + esc(s.section) : "") + "</div>" +
      "<h3>" + esc(s.title) + '</h3><div class="chips">' + chips + (cat ? " " + cat : "") + "</div>" +
      '<div class="md">' + (s.html || "") + "</div></div>";
  }

  function buildPrintDoc(domNums, opts) {
    var sel = {};
    domNums.forEach(function (n) { sel[n] = true; });
    var doms = D.domains.filter(function (d) { return sel[d.number]; });
    var h = "";

    // cover
    h += '<div class="pv-cover"><div class="logo"></div>' +
      '<div class="title"><h1>' + esc(D.client.title) + '</h1>' +
      '<p class="sub">' + esc(D.client.name) + (D.client.period ? " · " + esc(D.client.period) : "") + "</p></div>" +
      '<div class="meta">' +
      "<div><b>" + esc(L.coverClient) + ":</b> " + esc(D.client.name) + "</div>" +
      (D.client.period ? "<div><b>" + esc(L.coverPeriod) + ":</b> " + esc(D.client.period) + "</div>" : "") +
      (D.meta && D.meta.version ? "<div><b>" + esc(L.coverVersion) + ":</b> " + esc(D.meta.version) + "</div>" : "") +
      "<div><b>" + esc(L.coverDate) + ":</b> " + esc((D.meta && D.meta.generated) || "") + "</div>" +
      (D.meta && D.meta.model ? "<div><b>" + esc(L.coverModel) + ":</b> " + esc(D.meta.model) + "</div>" : "") +
      "</div>" +
      '<div class="art"><i class="a1"></i><i class="a2"></i><i class="a3"></i></div></div>';

    // everything after the cover lives in a table whose <thead> the browser
    // repeats at the top of every printed page — the running header
    h += '<table class="pv-doc"><thead><tr><td><div class="pv-run"><span>' +
      esc(D.client.title) + " — " + esc(D.client.name) +
      (D.meta && D.meta.version ? " · v" + esc(D.meta.version) : "") +
      '</span><div class="logo"></div></div></td></tr></thead><tbody><tr><td>';

    // table of contents
    var toc = [];
    if (opts.intro) toc.push(["", L.intro]);
    doms.forEach(function (d) { toc.push([d.number + ".", d.title]); });
    if (opts.scope) toc.push(["", L.scope]);
    if (opts.requirements) toc.push(["", L.requirements]);
    if (opts.gaps) toc.push(["", L.gaps]);
    h += '<div class="pv-toc"><h2>' + esc(L.toc) + "</h2><ol>" + toc.map(function (t) {
      return '<li><span class="n">' + esc(t[0]) + "</span><span>" + esc(t[1]) + "</span></li>";
    }).join("") + "</ol></div>";

    if (opts.intro && D.client.intro_html) {
      h += '<div class="pv-section"><h1>' + esc(L.intro) + '</h1><div class="md">' + D.client.intro_html + "</div></div>";
    }

    // domains: intro + flow + full scenario documentation
    doms.forEach(function (d) {
      h += '<div class="pv-section"><h1><span class="n">' + d.number + ".</span> " + esc(d.title) + "</h1>";
      if (d.intro_html) h += '<div class="pv-intro md">' + d.intro_html + "</div>";
      if (d.process) {
        h += '<div class="pv-diagram">' + renderDiagram(d.process, null) +
          '<div class="pv-legend">' +
          '<span><i style="border-color:var(--fit-standard);background:var(--fit-standard-bg)"></i>' + esc(L.legendStandard) + "</span>" +
          '<span><i style="border-color:var(--fit-addon);background:var(--fit-addon-bg)"></i>' + esc(L.legendAddon) + "</span>" +
          '<span><i style="border-color:var(--fit-workaround);background:var(--fit-workaround-bg)"></i>' + esc(L.legendWorkaround) + "</span>" +
          '<span><i style="border-color:var(--fit-gap);background:var(--fit-gap-bg)"></i>' + esc(L.legendGap) + "</span></div></div>";
      }
      h += d.scenarios.map(printScen).join("");
      h += "</div>";
    });

    // scope matrix (rows limited to the selected domains)
    if (opts.scope) {
      var rows = D.coverage.filter(function (c) { return sel[c.domain]; });
      h += '<div class="pv-section"><h1>' + esc(L.scope) + '</h1><table class="pv-table"><thead><tr>' +
        L.scopeCols.map(function (c) { return "<th>" + esc(c) + "</th>"; }).join("") + "</tr></thead><tbody>" +
        rows.map(function (c) {
          var s = scen(c.code);
          var dm = domByNum[c.domain];
          return "<tr><td><code>" + esc(c.code) + "</code></td><td>" + esc(c.title) + "</td>" +
            "<td>" + (dm ? dm.number + ". " + esc(dm.title) : esc(c.domain)) + "</td>" +
            "<td>" + (c.scope ? esc(L.inScope) : esc(L.outScope)) + "</td>" +
            "<td>" + (c.scope ? fitChip(c.fit || (s && s.fit) || "none", (s && s.addon) || c.addon) : "—") + "</td>" +
            "<td>" + esc(c.note || "") + "</td></tr>";
        }).join("") + "</tbody></table></div>";
    }

    // requirements / gaps registers (entries touching the selected domains,
    // plus unlinked entries — nothing silently dropped)
    function inSel(codes) {
      if (!codes || !codes.length) return true;
      return codes.some(function (c) { var s = scen(c); return s && sel[s.domain]; });
    }
    if (opts.requirements) {
      h += '<div class="pv-section"><h1>' + esc(L.requirements) + "</h1>" +
        D.requirements.filter(function (r) { return inSel(r.scenarios); }).map(function (r) {
          return '<div class="pv-scen"><div class="codes"><code>' + esc(r.id) + "</code>" +
            (r.source ? " · " + esc(r.source) : "") + "</div><h3>" + esc(r.title) + "</h3>" +
            '<div class="md">' + (r.html || "") + "</div>" +
            (r.scenarios && r.scenarios.length ? '<div class="codes">' + r.scenarios.map(function (c) { return "<code>" + esc(c) + "</code>"; }).join(" ") + "</div>" : "") +
            "</div>";
        }).join("") + "</div>";
    }
    if (opts.gaps) {
      h += '<div class="pv-section"><h1>' + esc(L.gaps) + "</h1>" +
        D.gaps.filter(function (g) { return inSel(g.scenarios); }).map(function (g) {
          return '<div class="pv-scen"><div class="codes"><code>' + esc(g.id) + "</code></div><h3>" + esc(g.title) + "</h3>" +
            '<div class="md">' + (g.html || "") + "</div>" +
            (g.scenarios && g.scenarios.length ? '<div class="codes">' + g.scenarios.map(function (c) { return "<code>" + esc(c) + "</code>"; }).join(" ") + "</div>" : "") +
            "</div>";
        }).join("") + "</div>";
    }

    h += "</td></tr></tbody></table>";
    document.getElementById("printdoc").innerHTML = h;
  }

  function onSearch(ev) {
    var q = ev.target.value.trim().toLowerCase();
    var hits = document.getElementById("hits"), doms = document.getElementById("domlist");
    if (q.length < 2) { hits.style.display = "none"; doms.style.display = ""; return; }
    var res = [];
    Object.keys(D.scenarios).forEach(function (code) {
      var s = D.scenarios[code];
      if (code.toLowerCase().indexOf(q) >= 0 || (s.title || "").toLowerCase().indexOf(q) >= 0) res.push(s);
    });
    res = res.slice(0, 40);
    hits.innerHTML = res.length
      ? res.map(function (s) {
        return '<a class="hit" href="#/domain/' + s.domain + "/doc/" + esc(s.code) + '"><code>' + esc(s.code) + "</code> " + esc(s.title) + "</a>";
      }).join("")
      : '<div class="none">' + esc(L.noResults) + "</div>";
    hits.style.display = ""; doms.style.display = "none";
  }

  function markDomain(num) {
    document.querySelectorAll("#domlist a").forEach(function (a) {
      a.classList.toggle("on", a.getAttribute("data-dom") === String(num));
    });
  }

  function legend() {
    return '<div class="legend">' +
      '<span><i style="border-color:var(--fit-standard);background:var(--fit-standard-bg)"></i>' + esc(L.legendStandard) + "</span>" +
      '<span><i style="border-color:var(--fit-addon);background:var(--fit-addon-bg)"></i>' + esc(L.legendAddon) + "</span>" +
      '<span><i style="border-color:var(--fit-workaround);background:var(--fit-workaround-bg)"></i>' + esc(L.legendWorkaround) + "</span>" +
      '<span><i style="border-color:var(--fit-gap);background:var(--fit-gap-bg)"></i>' + esc(L.legendGap) + "</span>" +
      '<span><i style="border-color:var(--fit-none);background:var(--fit-none-bg);border-style:dashed"></i>' + esc(L.legendNone) + "</span></div>";
  }

  function scenCard(code) {
    var s = scen(code);
    if (!s) return "";
    var fit = fitOf(code);
    return '<div class="scen-card ' + fit + '" data-scenario="' + esc(code) + '">' +
      '<div class="m"><code class="bs">' + esc(code) + "</code>" + (s.section ? " · " + esc(s.section) : "") + "</div>" +
      '<div class="t">' + esc(s.title) + "</div>" +
      '<div class="m">' + fitChip(fit, s.addon) +
      (s.gap ? ' <span class="chip gap">' + esc(s.gap) + "</span>" : "") + "</div>" +
      '<div class="m">' + catalogNote(code) + "</div></div>";
  }

  function viewDomain(num, docCode) {
    var d = domByNum[num];
    if (!d) return viewIntro();
    markDomain(num);
    var v = document.getElementById("view");
    var h = '<h1 class="pg">' + d.number + ". " + esc(d.title) + "</h1>";
    if (d.process) h += '<p class="pg-sub">' + esc(lbl(d.process.subtitle)) + "</p>";
    if (d.intro_html) h += '<div class="card md">' + d.intro_html + "</div>";
    if (d.process) {
      h += '<div class="card diagram-card"><div class="diagram-head">' + legend() +
        '<div class="zoom"><button data-z="-">−</button><button data-z="0">⤢</button><button data-z="+">+</button></div></div>' +
        '<div class="diagram-scroll" id="dscroll">' + renderDiagram(d.process, docCode) + "</div></div>";
    } else if (d.scenarios.length) {
      h += '<p class="pg-sub">' + esc(L.domainDocOnly) + "</p>";
    }
    if (d.scenarios.length) {
      h += '<h2 class="sect">' + esc(L.otherScenarios) + ' (' + d.scenarios.length + ')</h2><div class="scen-grid">' +
        d.scenarios.map(scenCard).join("") + "</div>";
    }
    if (!d.process && !d.scenarios.length) h += '<div class="empty">—</div>';
    v.innerHTML = h;

    var zoom = 1, svg = v.querySelector("svg.bpmn");
    var baseW = svg ? +svg.getAttribute("width") : 0;
    v.querySelectorAll(".zoom button").forEach(function (b) {
      b.addEventListener("click", function () {
        var z = b.getAttribute("data-z");
        zoom = z === "+" ? Math.min(zoom * 1.2, 3) : z === "-" ? Math.max(zoom / 1.2, .4) : 1;
        if (svg) { svg.setAttribute("width", baseW * zoom); svg.removeAttribute("height"); }
      });
    });
    v.querySelectorAll("[data-scenario]").forEach(function (n) {
      n.addEventListener("click", function () {
        location.hash = "#/domain/" + num + "/doc/" + n.getAttribute("data-scenario");
      });
    });
    v.querySelectorAll("svg [data-goto]:not([data-scenario])").forEach(function (n) {
      n.addEventListener("click", function () {
        var target = findProcessDomain(n.getAttribute("data-goto"));
        if (target != null) location.hash = "#/domain/" + target;
      });
    });
    if (docCode) openPanel(docCode, num); else closePanel();
  }

  function findProcessDomain(pid) {
    for (var i = 0; i < D.domains.length; i++) {
      if (D.domains[i].process && D.domains[i].process.id === pid) return D.domains[i].number;
    }
    return null;
  }

  function openPanel(code, domNum) {
    var s = scen(code);
    var wrap = document.getElementById("panelwrap"), panel = document.getElementById("panel");
    if (!s) { closePanel(); return; }
    var fit = fitOf(code);
    var d = domByNum[s.domain];
    var chips = fitChip(fit, s.addon);
    if (s.gap) chips += ' <span class="chip gap link" data-nav="#/gaps">' + esc(s.gap) + "</span>";
    (s.requirements || []).forEach(function (r) {
      chips += ' <span class="chip req" data-nav="#/requirements">' + esc(r) + "</span>";
    });
    var goto_ = null;
    if (d && d.process) {
      d.process.nodes.some(function (n) { if (n.scenario === code && n.goto) { goto_ = n.goto; return true; } return false; });
    }
    panel.innerHTML =
      '<div class="p-head"><button class="p-close" title="Sluiten">✕</button>' +
      '<div class="codes"><code class="bs">' + esc(code) + "</code>" + (s.section ? '<span class="chip none">§ ' + esc(s.section) + "</span>" : "") + "</div>" +
      "<h2>" + esc(s.title) + "</h2>" +
      '<div class="dom">' + (d ? d.number + ". " + esc(d.title) : "") + "</div></div>" +
      '<div class="p-body"><div class="p-meta">' + chips + "</div>" +
      '<div class="p-meta">' + catalogNote(code) + "</div>" +
      (goto_ != null && findProcessDomain(goto_) != null
        ? '<p><span class="chip req" data-nav="#/domain/' + findProcessDomain(goto_) + '">↗ ' + esc(L.gotoProcess) + "</span></p>" : "") +
      '<div class="md">' + (s.html || "<p><em>—</em></p>") + "</div></div>";
    panel.querySelector(".p-close").addEventListener("click", closePanel);
    panel.querySelectorAll("[data-nav]").forEach(function (c) {
      c.addEventListener("click", function () { location.hash = c.getAttribute("data-nav"); });
    });
    panel.querySelector(".p-body").scrollTop = 0;
    wrap.classList.add("open");
  }

  function closePanel() {
    document.getElementById("panelwrap").classList.remove("open");
    var m = location.hash.match(/^#\/domain\/(\d+)\/doc\//);
    if (m) history.replaceState(null, "", "#/domain/" + m[1]);
  }

  function viewIntro() {
    markDomain(null);
    var v = document.getElementById("view");
    v.innerHTML = '<h1 class="pg">' + esc(L.intro) + "</h1>" +
      '<p class="pg-sub">' + esc(D.client.name) + (D.client.period ? " · " + esc(D.client.period) : "") +
      (D.meta && D.meta.model ? " · " + esc(D.meta.model) : "") +
      (D.meta && D.meta.version ? " · v" + esc(D.meta.version) : "") +
      (D.meta && D.meta.generated ? " · " + esc(L.generated) + " " + esc(D.meta.generated) : "") + "</p>" +
      '<div class="card md">' + (D.client.intro_html || "") + "</div>";
  }

  function viewScope() {
    markDomain(null);
    var v = document.getElementById("view");
    var filters = ["all", "standard", "addon", "workaround", "gap", "out"];
    var flabel = { all: L.filterAll, standard: L.fit.standard, addon: L.fit.addon, workaround: L.fit.workaround, gap: L.fit.gap, out: L.outScope };
    var h = '<h1 class="pg">' + esc(L.scope) + '</h1><p class="pg-sub">' +
      D.coverage.filter(function (c) { return c.scope; }).length + " " + esc(L.inScope) + " · " +
      D.coverage.filter(function (c) { return !c.scope; }).length + " " + esc(L.outScope) + "</p>" +
      '<div class="filters">' + filters.map(function (f) {
        return '<button data-f="' + f + '"' + (f === "all" ? ' class="on"' : "") + ">" + esc(flabel[f]) + "</button>";
      }).join("") + "</div>" +
      '<table class="reg"><thead><tr>' + L.scopeCols.map(function (c) { return "<th>" + esc(c) + "</th>"; }).join("") + "</tr></thead><tbody>" +
      D.coverage.map(function (c) {
        var s = scen(c.code);
        var fit = c.scope ? (c.fit || (s && s.fit) || "none") : "out";
        var dom = domByNum[c.domain];
        return '<tr class="' + (s ? "click " : "") + (c.scope ? "" : "dim") + '" data-fit="' + fit + '"' +
          (s ? ' data-scenario="' + esc(c.code) + '" data-dom="' + c.domain + '"' : "") + ">" +
          '<td><code class="bs">' + esc(c.code) + "</code></td><td>" + esc(c.title) + "</td>" +
          "<td>" + (dom ? dom.number + ". " + esc(dom.title) : esc(c.domain)) + "</td>" +
          "<td>" + (c.scope ? esc(L.inScope) : esc(L.outScope)) + "</td>" +
          "<td>" + (c.scope ? fitChip(c.fit || (s && s.fit) || "none", (s && s.addon) || c.addon) : "—") + "</td>" +
          "<td>" + esc(c.note || "") + "</td></tr>";
      }).join("") + "</tbody></table>";
    v.innerHTML = h;
    v.querySelectorAll(".filters button").forEach(function (b) {
      b.addEventListener("click", function () {
        v.querySelectorAll(".filters button").forEach(function (x) { x.classList.remove("on"); });
        b.classList.add("on");
        var f = b.getAttribute("data-f");
        v.querySelectorAll("tbody tr").forEach(function (tr) {
          tr.style.display = f === "all" || tr.getAttribute("data-fit") === f ? "" : "none";
        });
      });
    });
    v.querySelectorAll("tr.click").forEach(function (tr) {
      tr.addEventListener("click", function () {
        location.hash = "#/domain/" + tr.getAttribute("data-dom") + "/doc/" + tr.getAttribute("data-scenario");
      });
    });
  }

  function linkedScenChips(codes) {
    return (codes || []).map(function (c) {
      var s = scen(c);
      return s ? '<span class="chip req link" data-nav="#/domain/' + s.domain + "/doc/" + esc(c) + '">' + esc(c) + "</span>" : '<span class="chip none">' + esc(c) + "</span>";
    }).join(" ");
  }

  function viewRequirements() {
    markDomain(null);
    var v = document.getElementById("view");
    v.innerHTML = '<h1 class="pg">' + esc(L.requirements) + '</h1><p class="pg-sub">' + D.requirements.length + "</p>" +
      (D.requirements.length ? D.requirements.map(function (r) {
        return '<div class="card req-card" id="' + esc(r.id) + '"><h3><code class="bs">' + esc(r.id) + "</code> " + esc(r.title) + "</h3>" +
          (r.source ? '<div class="src">' + esc(r.source) + "</div>" : "") +
          '<div class="md">' + (r.html || "") + "</div>" +
          (r.scenarios && r.scenarios.length ? "<p>" + linkedScenChips(r.scenarios) + "</p>" : "") + "</div>";
      }).join("") : '<div class="empty">—</div>');
    bindNav(v);
  }

  function viewGaps() {
    markDomain(null);
    var v = document.getElementById("view");
    v.innerHTML = '<h1 class="pg">' + esc(L.gaps) + '</h1><p class="pg-sub">' + D.gaps.length + "</p>" +
      (D.gaps.length ? D.gaps.map(function (g) {
        return '<div class="card gap-card" id="' + esc(g.id) + '"><h3><code class="bs">' + esc(g.id) + "</code> " + esc(g.title) + "</h3>" +
          '<div class="md">' + (g.html || "") + "</div>" +
          (g.scenarios && g.scenarios.length ? "<p>" + linkedScenChips(g.scenarios) + "</p>" : "") + "</div>";
      }).join("") : '<div class="empty">—</div>');
    bindNav(v);
  }

  function bindNav(root) {
    root.querySelectorAll("[data-nav]").forEach(function (c) {
      c.addEventListener("click", function () { location.hash = c.getAttribute("data-nav"); });
    });
  }

  /* ---------------- router ---------------- */
  function route() {
    var h = location.hash || "";
    var active = "#/intro";
    var m;
    if ((m = h.match(/^#\/domain\/(\d+)(?:\/doc\/([A-Za-z0-9.\-]+))?/))) {
      active = null;
      chromeOnce(active);
      viewDomain(+m[1], m[2] || null);
      return;
    }
    if (h === "#/scope") { chromeOnce(h); viewScope(); return; }
    if (h === "#/requirements") { chromeOnce(h); viewRequirements(); return; }
    if (h === "#/gaps") { chromeOnce(h); viewGaps(); return; }
    chromeOnce("#/intro"); viewIntro();
  }

  var chromed = null;
  function chromeOnce(active) {
    // rebuild header nav highlight cheaply; full chrome only once
    if (!chromed) { chrome(active); chromed = true; }
    document.querySelectorAll(".hdr nav a").forEach(function (a) {
      a.classList.toggle("on", a.getAttribute("href") === active);
    });
  }

  window.addEventListener("hashchange", route);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closePanel(); });
  route();
})();
