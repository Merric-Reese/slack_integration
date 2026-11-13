# WGHG ICT Change Control Pack

ICT change control templates and process for the West Gippsland Healthcare Group (WGHG) **Change Control Board (CCB)**. Each change gets **one** CCB submission, on the template for its risk level, plus **one** run sheet for Medium risk and above. The pack is aligned to the ITIL 4 Change Enablement practice.

**Start with [`INDEX.md`](INDEX.md).** It lists every file, why it exists and where it fits in the process.

| Need | File |
|---|---|
| The process | `WGHG_ICT_Change_Control_Process.md` / `.docx` |
| Decide which process to follow | The "Which Change Process Should I Follow?" flowchart in every template and the process document |
| Submit a Low risk change | `WGHG_CCB_ICT_Change_Submission_Template_Minor.md` / `.docx` |
| Submit a Medium risk change | `WGHG_CCB_ICT_Change_Submission_Template_Medium.md` / `.docx` (includes the A3 Plan on a Page) |
| Submit a High or Critical risk change | `WGHG_CCB_ICT_Change_Submission_Template_High-Critical.md` / `.docx` (includes the A3 Plan on a Page) |
| Plan and run the change (Medium and above) | `WGHG_CCB_ICT_Change_Run_Sheet_Template.xlsx` (includes the A3 Plan on a Page tab) |
| Set up Confluence | `WGHG_Confluence_Page_Structure.md` |

## Rebuilding the Word and Excel Files

The Markdown files are the source. Edit the shared flowchart and risk criteria in `tools/shared_blocks.py` (and the flowchart in `assets/wghg-change-process-selector.mmd`), then rebuild:

```bash
python3 tools/shared_blocks.py .      # copies shared blocks into every Markdown file
node tools/build_docs.js .            # requires the "docx" npm package
python3 tools/build_run_sheet.py .    # requires openpyxl and Pillow
```

Then open the workbook in Excel once and save it, so its formula results are stored.

## Assumptions to Confirm Against WGHG Policy

- **Risk levels:** these follow the ITIL approach of rating impact and probability. The High / Low criteria (I1–I7, P1–P7), the user threshold in I5 and the mapping to Low / Medium / High / Critical are a starting point, to be refined against the WGHG Risk Management Framework.
- **CCB arrangements:** membership, quorum, meeting frequency, agenda cut-off, lead times and freeze periods are placeholders.
- **Systems and sites:** names such as EMR, PAS and PACS are generic examples. No WGHG-specific systems or sites were assumed.
- **Example values:** the dates, times, durations and `CHG0001234` in the run sheet are examples only.
