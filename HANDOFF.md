# Handoff – WGHG ICT Change Control Pack

**Branch:** `claude/relaxed-bell-b8219d`
**Work folder:** `wghg-change-control/`
**Status:** first full draft complete and pushed; waiting for WGHG review

---

## 1. What Was Asked

Build an ITIL-based ICT change control pack for West Gippsland Healthcare Group (WGHG), using WGHG logos from the WGHG website. Requirements, in the order they were given:

1. A change control template in Confluence-compatible Markdown and in Word.
2. A draft run sheet template in Excel.
3. The template covers **one change** and is a submission to the **Change Control Board (CCB)**, not a multi-change register.
4. A **Plan on a Page** overview, at **A3** so it is readable.
5. A **Change Control process document**, with a high-level overview included in both the Markdown and the Word versions.
6. A draft Confluence folder (page) structure to paste into Confluence.
7. An index of all files: why each exists and where it fits in the process.
8. A Slack message on completion. **Not done.** See Section 5.

---

## 2. What Was Delivered

Everything is in `wghg-change-control/`. **Read `INDEX.md` first**: it describes every file and tab and maps each to a process step.

| File | Summary |
|---|---|
| `WGHG_CCB_ICT_Change_Submission_Template.md` / `.docx` | CCB submission for a single change, in 17 sections (summary below). In Word: page 1 is the process overview, page 2 is the A3 landscape Plan on a Page, and Section 14 (CCB Decision) starts on a new page. |
| `WGHG_CCB_ICT_Change_Run_Sheet_Template.xlsx` | Workbook with tabs: Change Details, Plan on a Page (A3, auto-filled), Run Sheet (24 draft steps in 6 phases), Contacts, Comms Log, Issues & Decisions, and a hidden Lists tab. |
| `WGHG_ICT_Change_Control_Process.md` / `.docx` | Process document. In Word, Section 2 "Process at a Glance" prints on an A3 landscape page. |
| `WGHG_Confluence_Page_Structure.md` | Paste-ready Confluence page tree (as a nested list and as a text tree), plus naming conventions and labels. |
| `INDEX.md` | File index, run sheet tab descriptions and the per-change workflow. |
| `README.md` | Short overview, rebuild commands and assumptions. |
| `assets/` | WGHG banner and logo mark (downloaded from wghg.com.au), plus the process diagram in a full and a compact A4 version. |
| `tools/build_docs.js`, `tools/build_run_sheet.py` | Builders that regenerate the Word and Excel files. |

### Submission sections

- Before the numbered sections: the process overview and the Plan on a Page.
- 1–3: CCB submission details, executive summary, change details.
- 4–7: description, ITIL "7 Rs", impact assessment, 5×5 risk assessment.
- 8–12: implementation summary, test plan, backout plan, schedule and conflicts, communications.
- 13–14: RACI and pre-CCB endorsements; CCB decision.
- 15–17: implementation record, PIR, closure.
- Appendices: lifecycle and definitions.

### Logo sources (from the WGHG website)

- Banner: https://wghg.com.au/wp-content/uploads/2018/11/Untitled-design-30.png
- Logo mark: https://wghg.com.au/wp-content/uploads/2022/03/cropped-wghg-fav-icon-270x270.png
- Brand colours sampled from the banner: navy `#00577D`, orange `#F7A11A`, light blue `#78B3D0`.

---

## 3. How to Rebuild

The Markdown files are the source for the Word documents. Run these from `wghg-change-control/`:

```bash
node tools/build_docs.js .            # needs the "docx" npm package
python3 tools/build_run_sheet.py .    # needs openpyxl and Pillow
```

- **Excel:** openpyxl writes formulas without cached results. After rebuilding, open the workbook in Excel and save it, or recalculate it with LibreOffice.
- **Word:** the builder reads the Markdown structure. It replaces the "Plan on a Page (A3)" Markdown section with a native A3 page, and puts the process document's Section 2 on an A3 page. Editing table content in the Markdown is safe. **Renaming those headings will break that special handling.**

---

## 4. Verification Done

- **Word:** both documents rendered to PDF and checked page by page.
  - Submission: 11 pages; page 2 is A3, the rest A4.
  - Process document: 7 pages; page 2 is A3.
  - Both pass the DOCX schema validation.
- **Excel:** 416 formulas recalculated with **0 errors**. Computed values were spot-checked:
  - phase start and end times and the timeline bars match the Run Sheet;
  - "within approved window" and "full backout within window" both return Yes for the example data.
- **Markdown:** all tables parse as GitHub-flavoured Markdown, and the files contain no raw HTML, which Confluence would strip.
- **Not tested:** the files have **not** been opened in Microsoft Word or Excel, and nothing has been pasted into Confluence. The rendering checks used LibreOffice.

---

## 5. Open Items / Next Steps

| # | Item | Owner |
|---|---|---|
| 1 | **Slack completion message not sent.** The Slack connector failed to connect in the cloud session (proxy 403). Send it from the Mac session, or fix the connector. Suggested text is below. | User / Mac session |
| 2 | Confirm the placeholders against WGHG policy: CCB membership, quorum, meeting frequency, agenda cut-off, lead times, freeze periods, emergency CCB quorum. | WGHG ICT |
| 3 | Align the 5×5 risk matrix bands with the WGHG Risk Management Framework. | WGHG ICT / Risk |
| 4 | Replace the generic system examples (EMR, PAS, PACS) and site placeholders with WGHG's actual systems and sites. | WGHG ICT |
| 5 | Open the `.docx` and `.xlsx` files in Microsoft Office and confirm the layout, A3 printing, drop-downs and conditional formatting. | User |
| 6 | Create the Confluence pages marked "[to be created]" in the page structure: CCB Terms of Reference, meeting agenda and minutes, Change Schedule, Standard Change Catalogue, Reports. No templates exist for these yet. | WGHG ICT |
| 7 | Decide whether to keep this work in the `slack_integration` repository or move it to a dedicated repository or Confluence space. | User |

**Suggested Slack message:**

> The WGHG ICT Change Control pack is ready for review. It includes the CCB change submission (Word and Confluence) with an A3 Plan on a Page, a run sheet workbook with an auto-filled A3 Plan on a Page tab, the Change Control process document, a Confluence page structure and a file index. It's on branch `claude/relaxed-bell-b8219d`, folder `wghg-change-control/`.

---

## 6. Environment Notes

- **Network:** the cloud session's Default environment blocked wghg.com.au. With the user's approval, a personal environment named **"slack_integration (WGHG web access)"** was created, which allows `wghg.com.au` and `www.wghg.com.au`. The session was switched onto it.
- **Mac folders:** the user shared the folders "WGHG" and "Claude" via Remote Control on `Merrics-MacBook-Pro-2`. The Mac did not offer them to the cloud session (reported as "not_available"). The usual causes:
  - the folder sits inside a hidden folder directly under the home folder, or inside `~/Library`;
  - the Claude app on the Mac needs updating.

  This feature is also not available to every account yet.
- **To continue on the Mac:**
  - use **Open in CLI** on the claude.ai session (it gives a `claude --teleport …` command), **or**
  - run `git fetch origin && git checkout claude/relaxed-bell-b8219d` in a local clone.

---

## 7. Commits on This Branch

| Commit | Summary |
|---|---|
| `0d1db5a` | Add WGHG CCB ICT change submission and run sheet templates |
| `3eb40c5` | Add change control process, A3 Plan on a Page, Confluence structure and index |
| (this commit) | Add HANDOFF.md |
