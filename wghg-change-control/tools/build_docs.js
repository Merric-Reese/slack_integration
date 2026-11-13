// Builds the WGHG Word documents from their Confluence Markdown sources.
// Usage: node tools/build_docs.js <wghg-change-control folder>
// Requires the "docx" npm package.
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun,
  Header, Footer, AlignmentType, HeadingLevel, WidthType, ShadingType, BorderStyle,
  PageNumber, TableLayoutType, VerticalAlign, LevelFormat, PageOrientation, HeightRule,
} = require("docx");

const DIR = process.argv[2] || path.join(__dirname, "..");
const banner = fs.readFileSync(path.join(DIR, "assets/wghg-header-banner.png"));

const NAVY = "00577D", ORANGE = "F7A11A", LIGHT = "E6F0F5", MID = "78B3D0", PH = "0070C0";
const FONT = "Arial";
const A4 = { w: 11906, h: 16838, margin: 1080 };
const A3L = { w: 16838 * 1.414 | 0, h: 16838, margin: 720 }; // A3 = 420 x 297 mm
A3L.w = 23811;
const cw = (p) => p.w - 2 * p.margin;

// ---------- inline markdown -> runs ----------
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|`[^`]+`|\*[^*]+\*|\[[^\]]*\])/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), font: FONT, ...base }));
    const t = m[0];
    if (t.startsWith("**")) out.push(...runs(t.slice(2, -2), { ...base, bold: true }));
    else if (t.startsWith("`")) out.push(...runs(t.slice(1, -1), base));
    else if (t.startsWith("*")) out.push(...runs(t.slice(1, -1), { ...base, italics: true }));
    else out.push(new TextRun({ text: t, font: FONT, ...base, color: PH, italics: true }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), font: FONT, ...base }));
  return out;
}

const border = { style: BorderStyle.SINGLE, size: 4, color: "A6A6A6" };
const borders = { top: border, bottom: border, left: border, right: border };
const shade = (fill) => (fill ? { fill, type: ShadingType.CLEAR, color: "auto" } : undefined);

function colWidths(rows, total) {
  const n = rows[0].length;
  const weight = Array(n).fill(4), mins = Array(n).fill(n > 6 ? 550 : 900);
  rows.forEach((r) => r.forEach((c, i) => {
    weight[i] = Math.max(weight[i], Math.min(c.length, 60));
    const longest = Math.max(...c.replace(/[*`]/g, "").split(/\s+/).map((w) => w.length));
    mins[i] = Math.max(mins[i], longest * (n > 6 ? 88 : 100) + 240);
    if (/^☐ Yes ☐ No/.test(c)) mins[i] = Math.max(mins[i], 1350);
  }));
  let minSum = mins.reduce((a, b) => a + b, 0);
  if (minSum > total) { const k = total / minSum; for (let i = 0; i < n; i++) mins[i] = Math.floor(mins[i] * k); minSum = mins.reduce((a, b) => a + b, 0); }
  const spare = total - minSum, wsum = weight.reduce((a, b) => a + b, 0);
  const w = mins.map((m, i) => m + Math.floor(spare * weight[i] / wsum));
  w[n - 1] += total - w.reduce((a, b) => a + b, 0);
  return w;
}

const RATING_FILL = { Low: "C6EFCE", Medium: "FFEB9C", High: "F8CBAD", Critical: "FF9B9B" };
const ratingFill = (t) => { const m = /^(Low|Medium|High|Critical)( \(\d+\))?$/.exec(t); return m ? RATING_FILL[m[1]] : undefined; };

function cell(txtOrParas, { w, fill, run = {}, keepNext = false, minH } = {}) {
  const children = Array.isArray(txtOrParas) ? txtOrParas
    : [new Paragraph({ keepNext, spacing: { before: 0, after: 0 }, children: runs(txtOrParas, run) })];
  return new TableCell({
    borders, width: { size: w, type: WidthType.DXA }, shading: shade(fill),
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    verticalAlign: minH ? VerticalAlign.TOP : VerticalAlign.CENTER, children,
  });
}

function mdTable(rows, total) {
  const header = rows[0], body = rows.slice(1), n = header.length;
  const widths = colWidths(rows, total);
  const size = n > 6 ? 15 : 18;
  const keyValue = n === 2 && /^(Field|Question|Term|Item|Role|Period|Measure)$/.test(header[0]);
  return new Table({
    width: { size: total, type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED,
    rows: [
      new TableRow({ tableHeader: true, cantSplit: true,
        children: header.map((h, i) => cell(h, { w: widths[i], fill: NAVY, keepNext: true, run: { bold: true, color: "FFFFFF", size } })) }),
      ...body.map((r) => new TableRow({ cantSplit: true,
        children: r.map((c, i) => cell(c, {
          w: widths[i],
          fill: ratingFill(c) || ((i === 0 && (keyValue || n > 2)) ? LIGHT : undefined),
          run: { size, bold: i === 0 && keyValue ? true : undefined },
        })) })),
    ],
  });
}

// ---------- A3 Plan on a Page (native layout) ----------
function popBox(title, lines, w, size = 20) {
  return [
    new Paragraph({ shading: shade(NAVY), spacing: { before: 0, after: 60 }, children: [new TextRun({ text: " " + title, bold: true, color: "FFFFFF", font: FONT, size: 22 })] }),
    ...lines.map((l) => new Paragraph({ spacing: { before: 30, after: 30 }, children: runs(l, { size }) })),
  ];
}
function popRow(boxes, total, minH = 1500) {
  const w = Math.floor(total / boxes.length);
  const widths = boxes.map((_, i) => (i === boxes.length - 1 ? total - w * (boxes.length - 1) : w));
  return new Table({
    width: { size: total, type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED,
    rows: [new TableRow({ cantSplit: true, height: { value: minH, rule: HeightRule.ATLEAST },
      children: boxes.map((b, i) => cell(popBox(b[0], b[1], widths[i]), { w: widths[i], minH: true })) })],
  });
}
const gap = () => new Paragraph({ spacing: { before: 0, after: 100 }, children: [] });

function planOnAPage(risk) {
  const T = cw(A3L);
  const kids = [];
  kids.push(new Paragraph({
    spacing: { before: 0, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: ORANGE, space: 4 } },
    children: [
      new TextRun({ text: "Plan on a Page", bold: true, color: NAVY, font: FONT, size: 40 }),
      new TextRun({ text: "   Change ", color: NAVY, font: FONT, size: 30 }),
      ...runs("[CHG0001234] – [Enter change title]", { size: 30 }),
      new TextRun({ text: "\tFor CCB meeting: ", color: "595959", font: FONT, size: 22 }),
      ...runs("[DD/MM/YYYY]", { size: 22 }),
    ],
    tabStops: [{ type: "right", position: T }],
  }));
  // Change at a glance: 4 label/value pairs x 2 rows
  const pairs = [
    ["Change Type", "[Normal / Emergency]"], ["Overall Risk Rating", risk],
    ["Decision Requested", "[Approve for implementation]"], ["Change Owner", "[Name, position]"],
    ["Approved Window", "[DD/MM/YYYY HH:MM – HH:MM]"], ["Expected Outage", "[Duration; services affected]"],
    ["Go / No-Go Decision", "[DD/MM HH:MM]"], ["Backout Decision Point", "[DD/MM HH:MM]"],
  ];
  const lw = 2300, vw = Math.floor(T / 4) - lw;
  const gw = [lw, vw, lw, vw, lw, vw, lw, T - 3 * (lw + vw) - lw];
  kids.push(new Table({
    width: { size: T, type: WidthType.DXA }, columnWidths: gw, layout: TableLayoutType.FIXED,
    rows: [0, 1].map((r) => new TableRow({ cantSplit: true, children: pairs.slice(r * 4, r * 4 + 4).flatMap(([l, v], i) => [
      cell(l, { w: gw[i * 2], fill: LIGHT, run: { bold: true, size: 20 } }),
      cell(v, { w: gw[i * 2 + 1], run: { size: 20 } }),
    ]) })),
  }), gap());

  kids.push(popRow([
    ["What is changing", ["[Enter a plain-language description of the change.]", "[Services / CIs being changed.]"]],
    ["Why it is needed", ["[Driver, e.g. vendor end-of-support, security vulnerability, incident / problem resolution.]", "[Consequence of not proceeding.]"]],
    ["Success criteria and benefits", ["[Measurable success criterion 1]", "[Measurable success criterion 2]", "[Benefit to patients / staff / WGHG]"]],
  ], T, 2100), gap());

  // Timeline table
  const tl = [
    ["Phase", "Key Activities", "Owner", "Planned Start", "Planned End", "Readiness / Notes"],
    ["1. Pre-Implementation", "[Backups / snapshots, notifications, pre-checks, downtime procedures started]", "[Name]", "[HH:MM]", "[HH:MM]", "[Enter]"],
    ["2. Go / No-Go", "Go / No-Go decision – all pre-implementation steps complete and no blocking issues", "[Change Manager]", "[HH:MM]", "[HH:MM]", "[Enter]"],
    ["3. Implementation", "[Enter key implementation activities]", "[Name]", "[HH:MM]", "[HH:MM]", "[Enter]"],
    ["4. Verification", "[Technical verification; interface checks; clinical / business user verification]", "[Name]", "[HH:MM]", "[HH:MM]", "[Enter]"],
    ["◆ Backout decision point", "Latest time a backout can start and still finish inside the approved window", "[Change Manager]", "[HH:MM]", "—", "[Enter]"],
    ["5. Post-Implementation", "[Notify completion, end downtime procedures, monitoring, update records]", "[Name]", "[HH:MM]", "[HH:MM]", "[Enter]"],
    ["6. Backout (only if invoked)", "[Enter backout summary, e.g. restore snapshot and re-verify]", "[Name]", "[HH:MM]", "[HH:MM]", "[Enter]"],
  ];
  const tw = [3600, 9200, 2600, 1700, 1700]; tw.push(T - tw.reduce((a, b) => a + b, 0));
  const rowFill = (p) => (p.startsWith("2.") || p.startsWith("◆") ? "FDE2B3" : p.startsWith("6.") ? "F8CBAD" : undefined);
  kids.push(new Paragraph({ spacing: { before: 0, after: 60 }, keepNext: true, children: [new TextRun({ text: "Timeline", bold: true, color: NAVY, font: FONT, size: 26 })] }));
  kids.push(new Table({
    width: { size: T, type: WidthType.DXA }, columnWidths: tw, layout: TableLayoutType.FIXED,
    rows: tl.map((r, ri) => new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, {
      w: tw[i], fill: ri === 0 ? NAVY : rowFill(r[0]) || (i === 0 ? LIGHT : undefined),
      run: ri === 0 ? { bold: true, color: "FFFFFF", size: 20 } : { size: 20, bold: i === 0 },
    })) })),
  }), gap());

  kids.push(popRow([
    ["Impacted services, sites and users", ["Services / CIs: [Enter]", "Sites / departments: [Enter]", "Users affected: [Enter number]", "Clinical impact: [Enter]", "Downtime procedures: [Enter reference]"]],
    ["Top risks and mitigations", ["R1: [Risk] – [Rating] – [Mitigation]", "R2: [Risk] – [Rating] – [Mitigation]", "R3: [Risk] – [Rating] – [Mitigation]"]],
    ["Backout plan", ["Trigger(s): [Enter]", "Decision point: [HH:MM]   Decision maker: [Name]", "Estimated backout duration: [Enter]", "Backout tested: ☐ Yes ☐ No", "Data restore required: ☐ Yes ☐ No"]],
  ], T, 2500), gap());

  kids.push(popRow([
    ["Communications", ["ICT Service Desk – [when, channel]", "Clinical areas / NUMs – [when, channel]", "After-Hours Hospital Coordinator – [when, channel]", "Vendors – [when, channel]", "All affected users – start and completion"]],
    ["Readiness checklist", ["☐ Pre-CCB endorsements obtained", "☐ Testing complete (Test / UAT)", "☐ Backup / snapshot plan confirmed", "☐ Run Sheet finalised", "☐ Downtime procedures confirmed with clinical areas", "☐ Vendor support confirmed", "☐ Service Desk briefed"]],
    ["Key contacts", ["Change Manager: [Name] [Mobile]", "Implementation Lead: [Name] [Mobile]", "Business / Clinical Owner: [Name] [Mobile]", "After-Hours Hospital Coordinator: [Phone]", "Vendor support: [Phone]"]],
  ], T, 2600));
  return kids;
}

// ---------- page furniture ----------
function header(page) {
  const wpx = Math.round(cw(page) / 15); // dxa -> px at 96 dpi
  const w = Math.min(wpx, 1507), h = Math.round(w * 90 / 1507);
  return new Header({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
    new ImageRun({ type: "png", data: banner, transformation: { width: w, height: h },
      altText: { title: "WGHG logo", description: "West Gippsland Healthcare Group", name: "wghg-banner" } }),
  ] })] });
}
function footer(page, text) {
  const g = { font: FONT, size: 16, color: "595959" };
  return new Footer({ children: [new Paragraph({
    border: { top: { style: BorderStyle.SINGLE, size: 6, color: MID, space: 4 } },
    tabStops: [{ type: "right", position: cw(page) }],
    children: [new TextRun({ text, ...g }), new TextRun({ text: "\tPage ", ...g }),
      new TextRun({ children: [PageNumber.CURRENT], ...g }), new TextRun({ text: " of ", ...g }),
      new TextRun({ children: [PageNumber.TOTAL_PAGES], ...g })],
  })] });
}
function sectionProps(page, landscape) {
  return { page: {
    size: landscape ? { width: page.h, height: page.w, orientation: PageOrientation.LANDSCAPE } : { width: page.w, height: page.h },
    margin: { top: landscape ? 2050 : 1300, bottom: landscape ? 800 : 1000, left: page.margin, right: page.margin, header: 400, footer: 400 },
  } };
}

// ---------- markdown -> sections ----------
function build({ md, out, footerText, title, description, pop, popRisk, a3Heading, breakBefore }) {
  const lines = fs.readFileSync(path.join(DIR, md), "utf8").split("\n");
  const sections = [];
  let children = [];
  let page = A4, T = cw(A4);
  const flush = () => {
    const land = page === A3L;
    if (children.length) sections.push({ properties: sectionProps(page, land), headers: { default: header(page) }, footers: { default: footer(page, footerText + (land ? "   |   A3" : "")) }, children });
    children = [];
  };
  const flushA4 = flush;
  const setPage = (p) => { if (p !== page) { flush(); page = p; T = cw(p); } };
  const spacer = () => new Paragraph({ spacing: { before: 0, after: 120 }, children: [] });
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (pop && line.startsWith("## Plan on a Page")) {
      flushA4();
      sections.push({ properties: sectionProps(A3L, true), headers: { default: header(A3L) }, footers: { default: footer(A3L, footerText + "   |   Plan on a Page (A3)") }, children: planOnAPage(popRisk) });
      while (i < lines.length && lines[i].trim() !== "---") i++;
      i++; continue;
    }
    if (a3Heading && line.startsWith("## ") && a3Heading.test(line.slice(3))) setPage(A3L);
    if (line.trim() === "---" && page === A3L) { setPage(A4); i++; continue; }
    if (line.startsWith("```")) { i++; while (i < lines.length && !lines[i].startsWith("```")) i++; i++; continue; }
    if (line.startsWith("![")) {
      const m = /\]\(([^)]+)\)/.exec(line);
      if (m && !/^https?:/.test(m[1])) {
        let src = m[1];
        const a4src = src.replace(/\.png$/, "-a4.png");
        if (page === A4 && fs.existsSync(path.join(DIR, a4src))) src = a4src;
        const img = fs.readFileSync(path.join(DIR, src));
        const wpx = img.readUInt32BE(16), hpx = img.readUInt32BE(20);
        let w = Math.round(T / 15), h = Math.round(w * hpx / wpx);
        const maxH = page === A4 ? 800 : 640;
        if (h > maxH) { w = Math.round(w * maxH / h); h = maxH; }
        children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 60, after: 120 }, children: [
          new ImageRun({ type: "png", data: img, transformation: { width: w, height: h }, altText: { title: "Process overview", description: line.slice(2, line.indexOf("]")), name: path.basename(src) } })] }));
      }
      i++; continue;
    }
    if (line.startsWith("*Confluence:")) { i++; continue; }
    if (line.startsWith("|")) {
      const rows = [];
      while (i < lines.length && lines[i].startsWith("|")) {
        const cells = lines[i].trim().replace(/^\||\|$/g, "").split("|").map((c) => c.trim());
        if (!cells.every((c) => /^-+$/.test(c))) rows.push(cells);
        i++;
      }
      children.push(mdTable(rows, T), spacer());
      continue;
    }
    if (line.startsWith("# ")) children.push(new Paragraph({ heading: HeadingLevel.TITLE, children: runs(line.slice(2)) }));
    else if (line.startsWith("## ")) children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: /^\d+\. CCB Decision/.test(line.slice(3)) || (!!breakBefore && breakBefore.test(line.slice(3))), children: runs(line.slice(3)) }));
    else if (line.startsWith("### ")) children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: runs(line.slice(4)) }));
    else if (line.startsWith("> ")) children.push(new Paragraph({
      shading: shade("FEF3E0"), border: { left: { style: BorderStyle.SINGLE, size: 24, color: ORANGE, space: 8 } },
      spacing: { before: 120, after: 160 }, indent: { left: 120, right: 120 }, children: runs(line.slice(2), { size: 19 }) }));
    else if (line.startsWith("- ")) children.push(new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { before: 20, after: 40 }, children: runs(line.slice(2), { size: 20 }) }));
    else if (line.trim() !== "" && line.trim() !== "---") {
      const isGuidance = line.startsWith("*Guidance") || /^\*West Gippsland/.test(line);
      let j = i + 1; while (j < lines.length && lines[j].trim() === "") j++;
      children.push(new Paragraph({
        keepNext: j < lines.length && (lines[j].startsWith("|") || lines[j].startsWith("- ") || isGuidance),
        spacing: { before: 60, after: 100 }, children: runs(line, isGuidance ? { size: 18, color: "595959" } : { size: 20 }) }));
    }
    i++;
  }
  flushA4();

  const doc = new Document({
    creator: "WGHG ICT", title, description,
    numbering: { config: [{ reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }] },
    styles: {
      default: { document: { run: { font: FONT, size: 20 } } },
      paragraphStyles: [
        { id: "Title", name: "Title", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { font: FONT, size: 40, bold: true, color: NAVY },
          paragraph: { spacing: { before: 120, after: 120 }, keepNext: true, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: ORANGE, space: 4 } } } },
        { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { font: FONT, size: 28, bold: true, color: NAVY },
          paragraph: { spacing: { before: 320, after: 120 }, keepNext: true, outlineLevel: 0, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: MID, space: 2 } } } },
        { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { font: FONT, size: 23, bold: true, color: "006993" },
          paragraph: { spacing: { before: 200, after: 80 }, keepNext: true, outlineLevel: 1 } },
      ],
    },
    sections,
  });
  return Packer.toBuffer(doc).then((b) => { fs.writeFileSync(path.join(DIR, out), b); console.log("written", out, b.length); });
}

(async () => {
  const tpl = [
    ["Minor", "Minor (Low Risk)", false, null],
    ["Medium", "Medium Risk", true, "Medium"],
    ["High-Critical", "High / Critical Risk", true, "[High / Critical]", /^Which Change Process/],
  ];
  for (const [suffix, label, pop, popRisk, breakBefore] of tpl) {
    await build({
      md: `WGHG_CCB_ICT_Change_Submission_Template_${suffix}.md`, out: `WGHG_CCB_ICT_Change_Submission_Template_${suffix}.docx`,
      footerText: `WGHG CCB ICT Change Submission – ${label} – Change ID: [Enter]   |   Uncontrolled when printed`,
      title: `WGHG CCB ICT Change Submission Template – ${label}`,
      description: `ITIL 4 aligned single-change CCB submission template for ${label} changes`, pop, popRisk, breakBefore,
    });
  }
  await build({
    md: "WGHG_ICT_Change_Control_Process.md", out: "WGHG_ICT_Change_Control_Process.docx",
    footerText: "WGHG ICT Change Control Process – Version 0.2 DRAFT   |   Uncontrolled when printed",
    title: "WGHG ICT Change Control Process",
    description: "ITIL 4 aligned ICT change control process for the WGHG Change Control Board", pop: false,
    a3Heading: /^2\. Process at a Glance/,
  });
})();
