# WGHG ICT Change Control Pack

ICT change control templates and process for the West Gippsland Healthcare Group (WGHG) **Change Control Board (CCB)**. Each change gets **one** CCB submission and **one** run sheet. The pack is aligned to the ITIL 4 Change Enablement practice.

**Start with [`INDEX.md`](INDEX.md).** It lists every file, why it exists and where it fits in the process.

| Need | File |
|---|---|
| The process | `WGHG_ICT_Change_Control_Process.md` / `.docx` |
| Submit a change to the CCB | `WGHG_CCB_ICT_Change_Submission_Template.md` / `.docx` (includes the A3 Plan on a Page) |
| Plan and run the change | `WGHG_CCB_ICT_Change_Run_Sheet_Template.xlsx` (includes the A3 Plan on a Page tab) |
| Set up Confluence | `WGHG_Confluence_Page_Structure.md` |

## Rebuilding the Word and Excel Files

The Markdown files are the source. After editing them, rebuild:

```bash
node tools/build_docs.js .            # requires the "docx" npm package
python3 tools/build_run_sheet.py .    # requires openpyxl and Pillow
```

Then open the workbook in Excel once and save it, so its formula results are stored.

## Assumptions to Confirm Against WGHG Policy

- **Risk bands:** the 5×5 risk matrix bands are a common scheme; align them with the WGHG Risk Management Framework.
- **CCB arrangements:** membership, quorum, meeting frequency, agenda cut-off, lead times and freeze periods are placeholders.
- **Systems and sites:** names such as EMR, PAS and PACS are generic examples. No WGHG-specific systems or sites were assumed.
- **Example values:** the dates, times, durations and `CHG0001234` in the run sheet are examples only.
