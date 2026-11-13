"""Builds the WGHG ICT Change Run Sheet (single change, CCB-approved) Excel template.
Usage: python3 tools/build_run_sheet.py [wghg-change-control folder]   (requires openpyxl, Pillow)"""
import sys, os
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule, CellIsRule, DataBarRule
from openpyxl.comments import Comment
from openpyxl.utils import get_column_letter

D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(D, "WGHG_CCB_ICT_Change_Run_Sheet_Template.xlsx")
BANNER = os.path.join(D, "assets/wghg-header-banner.png")
MARK = os.path.join(D, "assets/wghg-logo-mark.png")

NAVY, ORANGE, LIGHT, MID = "00577D", "F7A11A", "E6F0F5", "78B3D0"
F = "Arial"
thin = Side(style="thin", color="A6A6A6")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
INPUT = PatternFill("solid", fgColor="FFF8E1")      # cells to fill in
HEAD = PatternFill("solid", fgColor=NAVY)
LBL = PatternFill("solid", fgColor=LIGHT)
CALC = PatternFill("solid", fgColor="F2F2F2")       # formula cells
DT = "dd/mm/yyyy hh:mm"

def font(**k):
    k.setdefault("name", F); k.setdefault("size", 10)
    return Font(**k)

def style(c, *, f=None, fill=None, wrap=True, h="left", v="center", fmt=None, border=True):
    c.font = f or font()
    if fill: c.fill = fill
    c.alignment = Alignment(wrap_text=wrap, horizontal=h, vertical=v)
    if border: c.border = BOX
    if fmt: c.number_format = fmt

def banner(ws, path, w, h, anchor="A1"):
    img = XLImage(path); img.width, img.height = w, h; ws.add_image(img, anchor)

def legend(ws, row, col=1, span=6):
    ws.cell(row, col, "Legend:").font = font(bold=True, size=9)
    c = ws.cell(row, col + 1, "Fill in"); style(c, f=font(size=9), fill=INPUT)
    c = ws.cell(row, col + 2, "Formula – do not edit"); style(c, f=font(size=9), fill=CALC)
    c = ws.cell(row, col + 3, "Blue italic text = example / placeholder. Replace it."); c.font = font(size=9, italic=True, color="0070C0")

wb = Workbook()

# ------------------------------------------------------------------ Lists (hidden)
L = wb.active; L.title = "Lists"
lists = {
    "A": ("Phase", ["1. Pre-Implementation", "2. Go / No-Go", "3. Implementation", "4. Verification", "5. Post-Implementation", "6. Backout"]),
    "B": ("Status", ["Not Started", "In Progress", "Complete", "Failed", "Skipped", "Backed Out"]),
    "C": ("YesNo", ["Yes", "No"]),
    "D": ("Channel", ["Email", "Phone", "SMS", "Teams / Chat", "Intranet", "Huddle / In person", "Bridge call"]),
    "E": ("LogType", ["Issue", "Decision", "Risk", "Variation to plan"]),
    "F": ("OpenClosed", ["Open", "Closed"]),
    "G": ("Decision", ["Approved", "Approved with conditions"]),
    "H": ("ChangeType", ["Normal", "Emergency"]),
    "I": ("Risk", ["Low", "Medium", "High", "Extreme"]),
}
for col, (name, vals) in lists.items():
    L[f"{col}1"] = name
    for i, v in enumerate(vals, start=2): L[f"{col}{i}"] = v
def dv(ws, col_letter, n, rng, allow_blank=True):
    d = DataValidation(type="list", formula1=f"=Lists!${col_letter}$2:${col_letter}${n + 1}", allow_blank=allow_blank)
    d.error, d.errorTitle = "Please select a value from the list.", "Invalid entry"
    ws.add_data_validation(d); d.add(rng)

# ------------------------------------------------------------------ Change Details
C = wb.create_sheet("Change Details", 0)
C.sheet_view.showGridLines = False
C.column_dimensions["A"].width = 2
C.column_dimensions["B"].width = 38
C.column_dimensions["C"].width = 62
C.column_dimensions["D"].width = 4
C.column_dimensions["E"].width = 30
C.column_dimensions["F"].width = 18
C.row_dimensions[1].height = 42
banner(C, BANNER, 1000, 60, "B1")
C["B3"] = "ICT Change Run Sheet – Change Control Board (CCB) Approved Change"
C["B3"].font = font(size=16, bold=True, color=NAVY)
C["B4"] = "One run sheet per change. Complete this sheet first; the Run Sheet tab reads the window, Go / No-Go and backout times from here."
C["B4"].font = font(size=9, italic=True, color="595959")
c = C["B5"]; c.value = "Legend:  Fill in"; style(c, f=font(size=9, bold=True), fill=INPUT, wrap=False)
c = C["C5"]; c.value = "Formula – do not edit"; style(c, f=font(size=9), fill=CALC, wrap=False)
C["E5"] = "Blue italic text = example / placeholder. Replace it."; C["E5"].font = font(size=9, italic=True, color="0070C0")

C["B7"] = "Change Details"; C["B7"].font = font(size=12, bold=True, color=NAVY)
fields = [
    ("Change ID / RFC Number", "CHG0001234", None),
    ("Change Title", "[Enter short descriptive title]", None),
    ("Change Type", "Normal", ("H", 2)),
    ("Overall Risk Rating (from CCB submission)", "Medium", ("I", 4)),
    ("CCB Meeting Date", None, "date"),
    ("CCB Decision", "Approved", ("G", 2)),
    ("CCB Minutes Reference", "[Enter]", None),
    ("CCB Conditions of Approval", "[Enter conditions, or \"Nil\"]", None),
    ("Approved Window – Start", "=DATE(2026,12,5)+TIME(22,0,0)", "dt"),
    ("Approved Window – End", "=DATE(2026,12,6)+TIME(3,0,0)", "dt"),
    ("Go / No-Go Decision Time", "=DATE(2026,12,5)+TIME(23,10,0)", "dt"),
    ("Backout Decision Point (latest time)", "=DATE(2026,12,6)+TIME(1,15,0)", "dt"),
    ("Expected Service Outage", "[Enter, e.g. 60 minutes – full outage of <service>]", None),
    ("Change Manager", "[Name, mobile]", None),
    ("Implementation Lead", "[Name, mobile]", None),
    ("Business / Clinical Owner", "[Name, mobile]", None),
    ("Bridge / Conference Call Details", "[Enter Teams link or dial-in and PIN]", None),
    ("Run Sheet Version", "0.1 DRAFT", None),
    ("Run Sheet Prepared By / Date", "[Name] / [DD/MM/YYYY]", None),
]
REF = {}
r = 8
for label, val, kind in fields:
    style(C.cell(r, 2, label), f=font(bold=True), fill=LBL)
    c = C.cell(r, 3, val)
    example = isinstance(val, str) and (val.startswith("[") or val.startswith("CHG") or val.startswith("=DATE") or val == "0.1 DRAFT")
    style(c, fill=INPUT, f=font(italic=example, color="0070C0" if example else "000000"))
    if kind == "dt": c.number_format = DT
    if kind == "date": c.number_format = "dd/mm/yyyy"
    if isinstance(kind, tuple): dv(C, kind[0], kind[1], c.coordinate)
    REF[label] = f"'Change Details'!$C${r}"
    r += 1
C.cell(8 + [f[0] for f in fields].index("Approved Window – Start"), 3).comment = Comment(
    "Example date/time only – overwrite with the CCB-approved window (DD/MM/YYYY HH:MM).", "WGHG ICT")

# Progress summary (formulas)
C["E7"] = "Run Sheet Progress"; C["E7"].font = font(size=12, bold=True, color=NAVY)
FIRST, LAST = 6, 60  # run sheet data rows
rs = "'Run Sheet'"
summary = [
    ("Total steps", f"=COUNTA({rs}!$C${FIRST}:$C${LAST})", "0"),
    ("Complete", f"=COUNTIF({rs}!$N${FIRST}:$N${LAST},\"Complete\")", "0"),
    ("In Progress", f"=COUNTIF({rs}!$N${FIRST}:$N${LAST},\"In Progress\")", "0"),
    ("Not Started", f"=COUNTIF({rs}!$N${FIRST}:$N${LAST},\"Not Started\")", "0"),
    ("Failed", f"=COUNTIF({rs}!$N${FIRST}:$N${LAST},\"Failed\")", "0"),
    ("Backed Out", f"=COUNTIF({rs}!$N${FIRST}:$N${LAST},\"Backed Out\")", "0"),
    ("% Complete (excl. backout steps)", None, "0%"),
    ("Planned finish (excl. backout)", None, DT),
    ("Within approved window?", None, None),
    ("Full backout completes within window?", None, None),
]
for i, (lab, frm, fmt) in enumerate(summary):
    rr = 8 + i
    style(C.cell(rr, 5, lab), f=font(bold=True), fill=LBL)
    c = C.cell(rr, 6, frm); style(c, fill=CALC, h="center", fmt=fmt)
REF["summary_row"] = 8
wb._sum_rows = None

# ------------------------------------------------------------------ Run Sheet
R = wb.create_sheet("Run Sheet", 1)
R.sheet_view.showGridLines = False
R.row_dimensions[1].height = 40
banner(R, MARK, 48, 48, "A1")
R["C1"] = "ICT Change Run Sheet"; R["C1"].font = font(size=16, bold=True, color=NAVY)
R["C1"].alignment = Alignment(vertical="center")
R["D1"] = f'="Change: "&{REF["Change ID / RFC Number"]}&" – "&{REF["Change Title"]}'
R["D1"].font = font(size=11, bold=True); R["D1"].alignment = Alignment(vertical="center")
R["D2"] = (f'="Approved window: "&TEXT({REF["Approved Window – Start"]},"dd/mm/yyyy hh:mm")&" to "&TEXT({REF["Approved Window – End"]},"dd/mm/yyyy hh:mm")'
           f'&"   |   Go / No-Go: "&TEXT({REF["Go / No-Go Decision Time"]},"hh:mm")&"   |   Backout decision point: "&TEXT({REF["Backout Decision Point (latest time)"]},"hh:mm")')
R["D2"].font = font(size=10, color=NAVY)
legend(R, 3, col=3)

cols = [
    ("Step #", 7), ("Phase", 20), ("Task / Activity", 38), ("Detailed Instructions / Reference", 42),
    ("System / CI", 18), ("Responsible", 16), ("Support / Backup", 16), ("Depends On (Step #)", 11),
    ("Planned Start", 16), ("Duration (mins)", 10), ("Planned End", 16), ("Go / No-Go Checkpoint?", 11),
    ("Validation / Expected Result", 34), ("Status", 13), ("Actual Start", 16), ("Actual End", 16),
    ("Variance (mins, + = late)", 11), ("Comments", 34),
]
HR = 5
for i, (h, w) in enumerate(cols, start=1):
    c = R.cell(HR, i, h); style(c, f=font(bold=True, color="FFFFFF"), fill=HEAD, h="center")
    R.column_dimensions[get_column_letter(i)].width = w
R.row_dimensions[HR].height = 32

P = [p for p in lists["A"][1]]
steps = [
    # phase, task, detail, system, responsible, dur, gonogo, validation
    (P[0], "Confirm CCB approval and any conditions are met", "Check CCB decision and conditions on the Change Details tab", "ITSM tool", "Change Manager", 10, "No", "CCB approval recorded; conditions satisfied"),
    (P[0], "Open bridge call and confirm all resources present", "See Contacts tab", "Bridge call", "Change Manager", 10, "No", "All implementers and support on call"),
    (P[0], "Notify ICT Service Desk and After-Hours Hospital Coordinator that the change is starting", "Use agreed comms template; record in Comms Log", "Email / phone", "Change Manager", 5, "No", "Notifications sent and logged"),
    (P[0], "Confirm clinical areas have commenced downtime procedures (if required)", "Contact NUM / After-Hours Coordinator", "Phone", "Business / Clinical Owner", 10, "No", "Downtime procedures in place"),
    (P[0], "Take backup / snapshot of affected systems", "[Enter backup job / snapshot procedure reference]", "[Enter CI]", "[Engineer]", 20, "No", "Backup completed successfully; ID recorded in Comments"),
    (P[0], "Run pre-change health checks and capture baseline", "[Enter checks: services running, disk, replication, interfaces]", "[Enter CI]", "[Engineer]", 15, "No", "Baseline captured; no existing faults"),
    (P[1], "Go / No-Go decision", "Confirm all pre-implementation steps are complete and no blocking issues exist", "Bridge call", "Change Manager", 5, "Yes", "GO recorded in Issues & Decisions log"),
    (P[2], "Stop / drain affected services", "[Enter procedure]", "[Enter CI]", "[Engineer]", 10, "No", "Services stopped cleanly; users disconnected"),
    (P[2], "[Enter implementation step]", "[Enter commands / work instruction reference]", "[Enter CI]", "[Engineer]", 30, "No", "[Enter expected result]"),
    (P[2], "[Enter implementation step]", "[Enter commands / work instruction reference]", "[Enter CI]", "[Engineer]", 20, "No", "[Enter expected result]"),
    (P[2], "Start services", "[Enter procedure]", "[Enter CI]", "[Engineer]", 10, "No", "Services running; no errors in logs"),
    (P[3], "Technical verification / smoke test", "[Enter test script reference]", "[Enter CI]", "[Engineer]", 15, "No", "All technical tests pass"),
    (P[3], "Interface / integration verification", "[Enter: e.g. HL7 message flow, API responses]", "[Enter interface]", "[Integration Analyst]", 10, "No", "Messages flowing; no queued errors"),
    (P[3], "Business / clinical user verification", "[Enter test patient / workflow to verify]", "[Enter service]", "Business / Clinical Owner", 15, "Yes", "Clinical owner confirms service is fit for use"),
    (P[4], "Notify ICT Service Desk, After-Hours Coordinator and clinical areas of completion", "Record in Comms Log", "Email / phone", "Change Manager", 5, "No", "Completion notifications sent"),
    (P[4], "Confirm clinical areas have ceased downtime procedures and back-entered data", "Contact NUM / After-Hours Coordinator", "Phone", "Business / Clinical Owner", 10, "No", "Normal operations resumed"),
    (P[4], "Enhanced monitoring period", "[Enter monitoring dashboards / alerts to watch]", "[Enter CI]", "[Engineer]", 30, "No", "No new alerts or incidents"),
    (P[4], "Update ITSM change record, CMDB and documentation", "Record outcome; attach this run sheet", "ITSM tool", "Implementation Lead", 10, "No", "Change record updated for closure / PIR"),
    (P[5], "Backout decision", "Invoke backout if verification fails or the backout decision point is reached", "Bridge call", "Change Manager", 5, "Yes", "Decision recorded in Issues & Decisions log"),
    (P[5], "Notify stakeholders that backout is in progress", "Record in Comms Log", "Email / phone", "Change Manager", 5, "No", "Notifications sent"),
    (P[5], "[Enter backout step, e.g. restore snapshot / revert configuration]", "[Enter procedure reference]", "[Enter CI]", "[Engineer]", 30, "No", "[Enter expected result]"),
    (P[5], "Verify service restored to pre-change state", "Repeat baseline health checks from the pre-implementation phase", "[Enter CI]", "[Engineer]", 15, "No", "Service matches pre-change baseline"),
    (P[5], "Clinical / business confirmation of restored service", "[Enter test patient / workflow]", "[Enter service]", "Business / Clinical Owner", 10, "No", "Clinical owner confirms service restored"),
    (P[5], "Notify stakeholders of backout outcome; raise incident if required", "Record in Comms Log", "Email / phone", "Change Manager", 5, "No", "Notifications sent; incident ID recorded"),
]
backout_first = None
row = FIRST
for idx, (ph, task, det, sysci, resp, dur, gng, val) in enumerate(steps):
    is_backout = ph == P[5]
    if is_backout and backout_first is None: backout_first = row
    R.cell(row, 1, idx + 1)
    R.cell(row, 2, ph); R.cell(row, 3, task); R.cell(row, 4, det); R.cell(row, 5, sysci)
    R.cell(row, 6, resp); R.cell(row, 7, None); R.cell(row, 8, idx if idx > 0 and row != backout_first else None)
    if row == FIRST:
        R.cell(row, 9, f"={REF['Approved Window – Start']}")
    elif row == backout_first:
        R.cell(row, 9, f"={REF['Backout Decision Point (latest time)']}")
    elif ph == P[1]:
        R.cell(row, 9, f"=MAX(K{row - 1},{REF['Go / No-Go Decision Time']})")
    else:
        R.cell(row, 9, f"=K{row - 1}")
    R.cell(row, 10, dur)
    R.cell(row, 11, f'=IF(OR(I{row}="",J{row}=""),"",I{row}+J{row}/1440)')
    R.cell(row, 12, gng); R.cell(row, 13, val); R.cell(row, 14, "Not Started")
    R.cell(row, 17, f'=IF(OR(P{row}="",K{row}=""),"",ROUND((P{row}-K{row})*1440,0))')
    row += 1
last_step_row = row - 1
impl_last = backout_first - 1

# blank rows for additional steps, with formulas ready
for rr in range(row, LAST + 1):
    R.cell(rr, 11, f'=IF(OR(I{rr}="",J{rr}=""),"",I{rr}+J{rr}/1440)')
    R.cell(rr, 17, f'=IF(OR(P{rr}="",K{rr}=""),"",ROUND((P{rr}-K{rr})*1440,0))')

formula_cols = {11, 17}
for rr in range(FIRST, LAST + 1):
    for cc in range(1, len(cols) + 1):
        cell = R.cell(rr, cc)
        v = cell.value
        placeholder = isinstance(v, str) and v.startswith("[")
        is_formula_col = cc in formula_cols or (cc == 9 and isinstance(v, str) and v.startswith("="))
        style(cell, fill=CALC if is_formula_col else INPUT,
              f=font(italic=placeholder, color="0070C0" if placeholder else "000000"),
              h="center" if cc in (1, 8, 10, 12, 14, 17) else "left", v="top")
        if cc in (9, 11, 15, 16): cell.number_format = DT
        if cc in (10, 17): cell.number_format = "0"
R.cell(FIRST, 9).comment = Comment("Planned Start defaults to the previous step's Planned End. Step 1 reads the approved window start; the Go / No-Go and first backout steps read their times from the Change Details tab. Overwrite any Planned Start to set a fixed time.", "WGHG ICT")
R.cell(FIRST, 10).comment = Comment("Durations are draft estimates only. Replace them with the implementation team's estimates.", "WGHG ICT")

dv(R, "A", 6, f"B{FIRST}:B{LAST}")
dv(R, "B", 6, f"N{FIRST}:N{LAST}")
dv(R, "C", 2, f"L{FIRST}:L{LAST}")
dvi = DataValidation(type="whole", operator="between", formula1="0", formula2="1440", allow_blank=True)
dvi.error = "Duration must be a whole number of minutes (0–1440)."; R.add_data_validation(dvi); dvi.add(f"J{FIRST}:J{LAST}")

rng = f"A{FIRST}:R{LAST}"
status_fill = {"Complete": "C6EFCE", "In Progress": "FFEB9C", "Failed": "FFC7CE", "Backed Out": "F8CBAD", "Skipped": "D9D9D9"}
for s, col in status_fill.items():
    R.conditional_formatting.add(f"N{FIRST}:N{LAST}", CellIsRule(operator="equal", formula=[f'"{s}"'], fill=PatternFill("solid", fgColor=col), font=Font(name=F, bold=True)))
R.conditional_formatting.add(rng, FormulaRule(formula=[f'$L{FIRST}="Yes"'], fill=PatternFill("solid", fgColor="FDE2B3"), font=Font(name=F, bold=True)))
R.conditional_formatting.add(f"B{FIRST}:B{LAST}", FormulaRule(formula=[f'$B{FIRST}="6. Backout"'], fill=PatternFill("solid", fgColor="F8CBAD")))
R.conditional_formatting.add(f"Q{FIRST}:Q{LAST}", FormulaRule(formula=[f'AND(ISNUMBER($Q{FIRST}),$Q{FIRST}>0)'], font=Font(name=F, color="C00000", bold=True)))

R.freeze_panes = f"D{FIRST}"
R.auto_filter.ref = f"A{HR}:R{LAST}"
R.print_title_rows = f"{HR}:{HR}"
R.page_setup.orientation = "landscape"; R.page_setup.paperSize = R.PAPERSIZE_A3
R.page_setup.fitToWidth = 1; R.page_setup.fitToHeight = 0; R.sheet_properties.pageSetUpPr.fitToPage = True
R.oddFooter.left.text = "WGHG ICT Change Run Sheet – Uncontrolled when printed"; R.oddFooter.right.text = "Page &P of &N"

# notes under the table
nr = LAST + 2
R.cell(nr, 1, "Notes:").font = font(bold=True, size=9)
notes = [
    "Rows shaded orange are Go / No-Go checkpoints. Do not proceed past a checkpoint without recording the decision in the Issues & Decisions log.",
    "Phase 6 (Backout) is executed only if the backout decision is made. Its timing starts from the Backout Decision Point on the Change Details tab.",
    "All step text in blue italics and all durations are draft examples. Replace them with the technical steps for this change.",
]
for i, n in enumerate(notes):
    R.cell(nr + 1 + i, 1, f"{i + 1}. {n}").font = font(size=9, color="595959")

# Fill the summary formulas now that the row layout is known
C["F14"] = f'=IFERROR(COUNTIF({rs}!$N${FIRST}:$N${impl_last},"Complete")/COUNTA({rs}!$C${FIRST}:$C${impl_last}),0)'
C["F15"] = f"=MAX({rs}!$K${FIRST}:$K${impl_last})"
C["F16"] = f'=IF(F15="","",IF(F15<={REF["Approved Window – End"]},"Yes","NO – review plan"))'
C.conditional_formatting.add("F16", CellIsRule(operator="equal", formula=['"NO – review plan"'], fill=PatternFill("solid", fgColor="FFC7CE"), font=Font(name=F, bold=True, color="9C0006")))
C["F17"] = f'=IF(COUNT({rs}!$K${backout_first}:$K${LAST})=0,"",IF(MAX({rs}!$K${backout_first}:$K${LAST})<={REF["Approved Window – End"]},"Yes","NO – review backout timing"))'
C.conditional_formatting.add("F17", CellIsRule(operator="equal", formula=['"NO – review backout timing"'], fill=PatternFill("solid", fgColor="FFC7CE"), font=Font(name=F, bold=True, color="9C0006")))
C["E19"] = f"Counts cover run sheet rows {FIRST}–{LAST}. % complete and planned finish exclude Phase 6 (Backout)."
C["E19"].font = font(size=8, italic=True, color="595959")
C.page_setup.paperSize = C.PAPERSIZE_A4; C.page_setup.orientation = "landscape"; C.page_setup.fitToWidth = 1; C.page_setup.fitToHeight = 0
C.sheet_properties.pageSetUpPr.fitToPage = True

# ------------------------------------------------------------------ helper for simple log sheets
def log_sheet(title, heading, headers, widths, rows, validations, nrows=30):
    ws = wb.create_sheet(title)
    ws.sheet_view.showGridLines = False
    ws.row_dimensions[1].height = 40
    banner(ws, MARK, 48, 48, "A1")
    ws["B1"] = heading; ws["B1"].font = font(size=16, bold=True, color=NAVY); ws["B1"].alignment = Alignment(vertical="center")
    ws["B2"] = f'="Change: "&{REF["Change ID / RFC Number"]}&" – "&{REF["Change Title"]}'; ws["B2"].font = font(bold=True)
    legend(ws, 3, col=2)
    for i, (h, w) in enumerate(zip(headers, widths), start=1):
        style(ws.cell(5, i, h), f=font(bold=True, color="FFFFFF"), fill=HEAD, h="center")
        ws.column_dimensions[get_column_letter(i)].width = w
    for r_i in range(nrows):
        vals = rows[r_i] if r_i < len(rows) else [None] * len(headers)
        for c_i, v in enumerate(vals, start=1):
            ph = isinstance(v, str) and v.startswith("[")
            c = ws.cell(6 + r_i, c_i, v)
            style(c, fill=INPUT, f=font(italic=ph, color="0070C0" if ph else "000000"), v="top")
    for col_letter, n, colrange in validations:
        dv(ws, col_letter, n, f"{colrange}6:{colrange}{5 + nrows}")
    ws.freeze_panes = "A6"
    ws.page_setup.paperSize = ws.PAPERSIZE_A4; ws.page_setup.orientation = "landscape"; ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_title_rows = "5:5"
    return ws

contacts = [
    ["Change Manager", "[Name]", "ICT", "[Mobile]", "[Email]", "Full window", "1"],
    ["Implementation Lead", "[Name]", "ICT", "[Mobile]", "[Email]", "Full window", "1"],
    ["Engineer(s)", "[Name]", "ICT", "[Mobile]", "[Email]", "Full window", "1"],
    ["Application / Vendor Support", "[Name]", "[Vendor]", "[Phone]", "[Email]", "[Enter hours]", "2"],
    ["Information Security", "[Name]", "ICT", "[Mobile]", "[Email]", "On call", "2"],
    ["ICT Service Desk", "[Name]", "ICT", "[Phone]", "[Email]", "[Enter hours]", "1"],
    ["Business / Clinical Owner", "[Name]", "[Department]", "[Mobile]", "[Email]", "Verification phase", "1"],
    ["After-Hours Hospital Coordinator / Manager", "[Name]", "Operations", "[Phone]", "[Email]", "Full window", "1"],
    ["ICT Manager / Escalation", "[Name]", "ICT", "[Mobile]", "[Email]", "On call", "3"],
    ["Executive on Call", "[Name]", "Executive", "[Mobile]", "[Email]", "On call (High / Extreme risk)", "4"],
]
log_sheet("Contacts", "Contacts & Escalation", ["Role", "Name", "Team / Organisation", "Phone / Mobile", "Email", "Availability During Change", "Escalation Level"],
          [36, 22, 20, 18, 28, 28, 12], contacts, [], nrows=15)

comms = [["=" + REF["Approved Window – Start"], "[Change Manager]", "ICT Service Desk; After-Hours Hospital Coordinator", "Email", "Change CHG0001234 has started. Expected completion [HH:MM].", "[Name]"]]
cs = log_sheet("Comms Log", "Communications Log", ["Date / Time", "From", "To / Audience", "Channel", "Message Summary", "Logged By"],
               [18, 20, 36, 16, 60, 18], comms, [("D", 7, "D")])
for rr in range(6, 36): cs.cell(rr, 1).number_format = DT

issues = [["=" + REF["Go / No-Go Decision Time"], "Decision", "Go / No-Go: all pre-implementation steps complete", "[Change Manager]", "[Change Manager]", "GO – proceed to implementation", "Closed"]]
iss = log_sheet("Issues & Decisions", "Issues & Decisions Log", ["Date / Time", "Type", "Description", "Raised By", "Owner", "Action / Decision", "Status"],
                [18, 16, 50, 18, 18, 44, 12], issues, [("E", 4, "B"), ("F", 2, "G")])
for rr in range(6, 36): iss.cell(rr, 1).number_format = DT

# ------------------------------------------------------------------ Plan on a Page (A3)
from openpyxl.styles import Alignment as _A
L["K1"] = "SlotLength"
L["K2"] = f"=({REF['Approved Window – End']}-{REF['Approved Window – Start']})/24"
P_ = wb.create_sheet("Plan on a Page", 1)
P_.sheet_view.showGridLines = False
P_.sheet_view.zoomScale = 90
widths = {"A": 2, "B": 31, "C": 26, "D": 15, "E": 15, "F": 8, "G": 10}
for k, v in widths.items(): P_.column_dimensions[k].width = v
SLOT0 = 8  # column H
for k in range(24): P_.column_dimensions[get_column_letter(SLOT0 + k)].width = 3.7
LASTC = get_column_letter(SLOT0 + 23)  # AE
BOXES = [("B", "D"), ("E", "O"), ("P", LASTC)]

def mbox(rng, value=None, *, fill=None, f=None, h="left", v="top", wrap=True, fmt=None):
    first = rng.split(":")[0]
    for row in P_[rng]:
        for c in row:
            c.border = Border(left=thin, right=thin, top=thin, bottom=thin)
            if fill: c.fill = fill
    c = P_[first]; c.value = value
    c.font = f or font(); c.alignment = _A(wrap_text=wrap, horizontal=h, vertical=v)
    if fmt: c.number_format = fmt
    if ":" in rng and rng.split(":")[0] != rng.split(":")[1]: P_.merge_cells(rng)
    return c

def hdr(rng, text):
    mbox(rng, text, fill=HEAD, f=font(bold=True, color="FFFFFF", size=12), v="center", wrap=False)

def ph(v):
    return isinstance(v, str) and v.startswith("[")

P_.row_dimensions[1].height = 70
banner(P_, BANNER, 1490, 89, "B1")
mbox(f"B3:{LASTC}3", f'="Plan on a Page – "&{REF["Change ID / RFC Number"]}&" – "&{REF["Change Title"]}',
     f=font(size=20, bold=True, color=NAVY), v="center", wrap=False)
P_.row_dimensions[3].height = 30
for c in P_[f"B3:{LASTC}3"][0]: c.border = Border(bottom=Side(style="medium", color=ORANGE))
mbox(f"B4:{LASTC}4", f'="CCB meeting: "&IF({REF["CCB Meeting Date"]}="","[DD/MM/YYYY]",TEXT({REF["CCB Meeting Date"]},"dd/mm/yyyy"))&"   |   CCB decision: "&{REF["CCB Decision"]}&"   |   Single change – one Plan on a Page per change"',
     f=font(size=11, color="595959"), v="center", wrap=False)
for c in P_[f"B4:{LASTC}4"][0]: c.border = Border()

# Change at a glance
hdr(f"B6:{LASTC}6", "Change at a Glance (from the Change Details tab)")
glance = [
    [("Change Type", "Change Type", None), ("Overall Risk Rating", "Overall Risk Rating (from CCB submission)", None), ("CCB Decision", "CCB Decision", None)],
    [("Approved Window – Start", "Approved Window – Start", DT), ("Approved Window – End", "Approved Window – End", DT), ("Expected Outage", "Expected Service Outage", None)],
    [("Go / No-Go Decision", "Go / No-Go Decision Time", DT), ("Backout Decision Point", "Backout Decision Point (latest time)", DT), ("Change Manager", "Change Manager", None)],
]
lab_rng = [("B", "B"), ("E", "G"), ("P", "U")]
val_rng = [("C", "D"), ("H", "O"), ("V", LASTC)]
for i, rowitems in enumerate(glance):
    rr = 7 + i
    for j, (lab, key, fmt) in enumerate(rowitems):
        mbox(f"{lab_rng[j][0]}{rr}:{lab_rng[j][1]}{rr}", lab, fill=LBL, f=font(bold=True), v="center")
        mbox(f"{val_rng[j][0]}{rr}:{val_rng[j][1]}{rr}", f'=IF({REF[key]}="","",{REF[key]})', fill=CALC, v="center", fmt=fmt)
    P_.row_dimensions[rr].height = 24

def box_row(r0, titles, contents, nrows):
    for (a, b), t in zip(BOXES, titles): hdr(f"{a}{r0}:{b}{r0}", t)
    for (a, b), txt in zip(BOXES, contents):
        mbox(f"{a}{r0 + 1}:{b}{r0 + nrows}", txt, fill=INPUT, f=font(size=10, italic=ph(txt), color="0070C0" if ph(txt) else "000000"))
    for k in range(1, nrows + 1): P_.row_dimensions[r0 + k].height = 18

box_row(11, ["What is changing", "Why it is needed", "Success criteria and benefits"],
        ["[Enter a plain-language description of the change and the services / CIs being changed.]",
         "[Enter the driver, e.g. vendor end-of-support, security vulnerability, incident / problem resolution, and the consequence of not proceeding.]",
         "[Enter measurable success criteria and the benefit to patients, staff and WGHG.]"], 4)

# Timeline
hdr(f"B17:{LASTC}17", "Timeline – auto-filled from the Run Sheet tab (bars show planned timing across the approved window in 24 equal slots)")
heads = ["Phase", "Owner", "Planned Start", "Planned End", "Steps", "% Complete"]
for k, h in enumerate(heads):
    style(P_.cell(18, 2 + k, h), f=font(bold=True, color="FFFFFF"), fill=PatternFill("solid", fgColor="006993"), h="center")
for k in range(24):
    c = P_.cell(18, SLOT0 + k)
    c.value = f"={REF['Approved Window – Start']}" if k == 0 else f"={get_column_letter(SLOT0 + k - 1)}18+Lists!$K$2"
    c.number_format = "hh:mm"; c.font = font(size=8, color="FFFFFF", bold=True)
    c.fill = PatternFill("solid", fgColor="006993"); c.border = BOX
    c.alignment = _A(text_rotation=90, horizontal="center", vertical="center")
P_.row_dimensions[18].height = 40
rsP, rsI, rsK, rsN = (f"'Run Sheet'!$B${FIRST}:$B${LAST}", f"'Run Sheet'!$I${FIRST}:$I${LAST}",
                      f"'Run Sheet'!$K${FIRST}:$K${LAST}", f"'Run Sheet'!$N${FIRST}:$N${LAST}")
phase_rows = []
owners = ["[Implementation Lead]", "Change Manager", "[Implementation Lead]", "[Business / Clinical Owner]", "Change Manager", "[Implementation Lead]"]
for k, ph_name in enumerate(lists["A"][1]):
    rr = 19 + k; phase_rows.append(rr)
    style(P_.cell(rr, 2, ph_name), f=font(bold=True), fill=LBL)
    style(P_.cell(rr, 3, owners[k]), fill=INPUT, f=font(italic=ph(owners[k]), color="0070C0" if ph(owners[k]) else "000000"))
    style(P_.cell(rr, 4, f'=IF(COUNTIF({rsP},$B{rr})=0,"",_xlfn.MINIFS({rsI},{rsP},$B{rr}))'), fill=CALC, fmt=DT, h="center")
    style(P_.cell(rr, 5, f'=IF(COUNTIF({rsP},$B{rr})=0,"",_xlfn.MAXIFS({rsK},{rsP},$B{rr}))'), fill=CALC, fmt=DT, h="center")
    style(P_.cell(rr, 6, f"=COUNTIF({rsP},$B{rr})"), fill=CALC, fmt="0", h="center")
    style(P_.cell(rr, 7, f'=IFERROR(COUNTIFS({rsP},$B{rr},{rsN},"Complete")/F{rr},0)'), fill=CALC, fmt="0%", h="center")
milestones = [("◆ Go / No-Go decision", "Go / No-Go Decision Time"), ("◆ Backout decision point", "Backout Decision Point (latest time)")]
for k, (lab, key) in enumerate(milestones):
    rr = 25 + k
    style(P_.cell(rr, 2, lab), f=font(bold=True), fill=PatternFill("solid", fgColor="FDE2B3"))
    style(P_.cell(rr, 3, "Change Manager"), fill=INPUT)
    style(P_.cell(rr, 4, f'=IF({REF[key]}="","",{REF[key]})'), fill=CALC, fmt=DT, h="center")
    for cc in (5, 6, 7): style(P_.cell(rr, cc, None), fill=CALC)
for rr in range(19, 27):
    P_.row_dimensions[rr].height = 18
    for k in range(24):
        col = get_column_letter(SLOT0 + k)
        if rr <= 24:
            frm = f'=IF(OR($D{rr}="",$E{rr}=""),"",IF(AND({col}$18<$E{rr},{col}$18+Lists!$K$2>$D{rr}),1,""))'
        else:
            frm = f'=IF($D{rr}="","",IF(AND($D{rr}>={col}$18,$D{rr}<{col}$18+Lists!$K$2),1,""))'
        c = P_.cell(rr, SLOT0 + k, frm); c.number_format = ";;;"
        c.border = Border(left=Side(style="hair", color="BFBFBF"), right=Side(style="hair", color="BFBFBF"), top=thin, bottom=thin)
bar = {19: "4A90B8", 20: ORANGE, 21: NAVY, 22: "2E8B57", 23: MID, 24: "E06666", 25: ORANGE, 26: "C00000"}
for rr, colr in bar.items():
    P_.conditional_formatting.add(f"H{rr}:{LASTC}{rr}", CellIsRule(operator="equal", formula=["1"], fill=PatternFill("solid", fgColor=colr)))
P_.conditional_formatting.add("G19:G24", DataBarRule(start_type="num", start_value=0, end_type="num", end_value=1, color="78B3D0"))

box_row(28, ["Impacted services, sites and users", "Top risks and mitigations", "Backout plan"],
        ["[Services / CIs:]\n[Sites / departments:]\n[Users affected:]\n[Clinical impact:]\n[Downtime procedures reference:]",
         "[R1: risk – rating – mitigation]\n[R2: risk – rating – mitigation]\n[R3: risk – rating – mitigation]",
         "[Trigger(s):]\n[Decision point and decision maker: see timeline]\n[Estimated backout duration:]\n[Backout tested: Yes / No]\n[Data restore required: Yes / No]"], 6)

# Communications / readiness / contacts
for (a, b), t in zip(BOXES, ["Communications", "Readiness checklist", "Key contacts (from the Contacts tab)"]): hdr(f"{a}36:{b}36", t)
comms_aud = ["ICT Service Desk", "Clinical areas / NUMs", "After-Hours Hospital Coordinator", "Executive (High / Extreme risk)", "Vendors / third parties", "All affected users", ""]
ready = ["Pre-CCB endorsements obtained", "Testing complete (Test / UAT)", "Backup / snapshot plan confirmed", "Run Sheet finalised",
         "Downtime procedures confirmed with clinical areas", "Vendor support confirmed", "Service Desk briefed"]
contact_rows = [("Change Manager", 6), ("Implementation Lead", 7), ("Business / Clinical Owner", 12), ("After-Hours Hospital Coordinator", 13),
                ("Application / Vendor Support", 9), ("ICT Service Desk", 11), ("Executive on Call", 15)]
for k in range(7):
    rr = 37 + k
    P_.row_dimensions[rr].height = 20
    mbox(f"B{rr}:B{rr}", comms_aud[k] or None, fill=LBL if comms_aud[k] else INPUT, f=font(bold=bool(comms_aud[k])), v="center")
    w = "[When / channel]" if comms_aud[k] else None
    mbox(f"C{rr}:D{rr}", w, fill=INPUT, f=font(italic=True, color="0070C0"), v="center")
    mbox(f"E{rr}:M{rr}", ready[k], fill=LBL, v="center")
    mbox(f"N{rr}:O{rr}", "No", fill=INPUT, h="center", v="center")
    lab, crow = contact_rows[k]
    mbox(f"P{rr}:W{rr}", lab, fill=LBL, f=font(bold=True), v="center")
    mbox(f"X{rr}:{LASTC}{rr}", f'=Contacts!$B${crow}&"   "&Contacts!$D${crow}', fill=CALC, v="center")
dv(P_, "C", 2, "N37:N43")
P_.conditional_formatting.add("N37:N43", CellIsRule(operator="equal", formula=['"Yes"'], fill=PatternFill("solid", fgColor="C6EFCE"), font=Font(name=F, bold=True, color="006100")))
P_.conditional_formatting.add("N37:N43", CellIsRule(operator="equal", formula=['"No"'], fill=PatternFill("solid", fgColor="FFC7CE"), font=Font(name=F, bold=True, color="9C0006")))
P_["B45"] = "Cream cells: fill in on this tab. Grey cells are formulas fed from the Change Details, Run Sheet and Contacts tabs. Prints as one A3 landscape page."
P_["B45"].font = font(size=8, italic=True, color="595959")

P_.print_area = f"A1:{LASTC}45"
P_.page_setup.orientation = "landscape"; P_.page_setup.paperSize = P_.PAPERSIZE_A3
P_.page_setup.fitToWidth = 1; P_.page_setup.fitToHeight = 1; P_.sheet_properties.pageSetUpPr.fitToPage = True
P_.print_options.horizontalCentered = True
P_.page_margins.left = P_.page_margins.right = 0.4; P_.page_margins.top = P_.page_margins.bottom = 0.5
P_.oddFooter.left.text = "WGHG ICT Change – Plan on a Page (A3) – Uncontrolled when printed"; P_.oddFooter.right.text = "&D"

L.sheet_state = "hidden"
wb.active = 0
wb.properties.title = "WGHG ICT Change Run Sheet Template"
wb.properties.creator = "WGHG ICT"
wb.save(OUT)
print("saved", OUT, "impl_last", impl_last, "backout_first", backout_first, "last_step", last_step_row)
