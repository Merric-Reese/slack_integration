# WGHG ICT Change Control Pack – File Index

**West Gippsland Healthcare Group (WGHG) – ICT Change Control Board (CCB)**

This pack supports **one change at a time** through the WGHG ICT Change Control process. For each change, you complete one CCB Submission and one Run Sheet workbook. The Plan on a Page is part of both.

---

## Process at a Glance

| Step | Stage | Files Used |
|---|---|---|
| 1 | Raise & Record | CCB Change Submission (started) |
| 2 | Assess & Plan | CCB Change Submission; Run Sheet workbook (Run Sheet, Plan on a Page, Contacts) |
| 3 | CCB Authorise | Plan on a Page (A3) presented; CCB Change Submission Section 14 completed |
| 4 | Schedule & Communicate | Run Sheet workbook – Comms Log |
| 5 | Implement | Run Sheet workbook – Run Sheet, Issues & Decisions; CCB Change Submission Section 15 |
| 6 | Review (PIR) | CCB Change Submission Section 16 |
| 7 | Close | CCB Change Submission Section 17; final Run Sheet attached to the ITSM record |

---

## File Index

### Process and Guidance

| File | What It Is | Why It Exists | Process Step | Used By |
|---|---|---|---|---|
| `WGHG_ICT_Change_Control_Process.md` | Process document (Confluence) | Defines how changes are raised, assessed, authorised by the CCB, implemented, reviewed and closed. Section 2 is the high-level overview. | All steps (reference) | Everyone involved in change |
| `WGHG_ICT_Change_Control_Process.docx` | Same process document (Word) | For formal review, approval and printing. The Process at a Glance section prints on an A3 landscape page. | All steps (reference) | Document owner, approvers |
| `WGHG_Confluence_Page_Structure.md` | Draft Confluence page tree | Paste-ready outline for setting up the ICT Change Control space, with naming conventions and labels. | Set-up (once) | Confluence space administrator |
| `INDEX.md` | This file | Explains every file, why it exists and where it fits. | Set-up and reference | Everyone |
| `README.md` | Short repository readme | Points to this index and explains how to rebuild the Word and Excel files. | — | Maintainers |

### Templates – Complete One Set per Change

| File | What It Is | Why It Exists | Process Step | Used By |
|---|---|---|---|---|
| `WGHG_CCB_ICT_Change_Submission_Template.md` | CCB Change Submission (Confluence) | The single record of one change: details, impact, risk, plans, endorsements, CCB decision, implementation record, PIR and closure. Includes the process overview and the Plan on a Page. | 1, 2, 3, 5, 6, 7 | Change Owner (author); CCB (Section 14); Change Manager |
| `WGHG_CCB_ICT_Change_Submission_Template.docx` | Same CCB Change Submission (Word) | For CCB packs, printing and signature. Page 1 is the process overview; page 2 is the **A3 landscape Plan on a Page**; the rest is A4. Section 14 (CCB Decision) starts on a new page. | 1, 2, 3, 5, 6, 7 | Change Owner; CCB Secretariat; CCB |
| `WGHG_CCB_ICT_Change_Run_Sheet_Template.xlsx` | Run Sheet workbook (Excel) | The timed implementation plan for the change, plus the auto-filled A3 Plan on a Page. Tabs are listed below. | 2, 3, 4, 5, 7 | Implementation Lead; Change Manager |

#### Run Sheet Workbook Tabs

| Tab | Purpose | Process Step |
|---|---|---|
| Change Details | CCB decision, the approved window, the Go / No-Go time and the backout decision point. Live progress summary, including whether the plan and a full backout fit inside the window. | 2–5 |
| Plan on a Page | **A3 landscape** one-page summary for the CCB. The timeline and bars fill automatically from the Run Sheet; contacts fill from the Contacts tab. | 2–3 |
| Run Sheet | 24 draft steps across six phases, including Go / No-Go checkpoints and backout. Planned times chain automatically; status and variance are tracked. Prints on A3. | 2, 5 |
| Contacts | People, phone numbers and escalation levels for the change window. | 2, 5 |
| Comms Log | Record of communications before, during and after the change. | 4–5 |
| Issues & Decisions | Go / No-Go and backout decisions, issues and variations to the plan. | 5 |
| Lists (hidden) | Drop-down values and the timeline slot length. Do not edit. | — |

### Assets

| File | What It Is | Why It Exists |
|---|---|---|
| `assets/wghg-header-banner.png` | WGHG logo banner | Page header in the Word documents and the Excel tabs. Downloaded from the WGHG website: https://wghg.com.au/wp-content/uploads/2018/11/Untitled-design-30.png |
| `assets/wghg-logo-mark.png` | WGHG logo mark | Small logo on the Excel log tabs. Downloaded from https://wghg.com.au/wp-content/uploads/2022/03/cropped-wghg-fav-icon-270x270.png |
| `assets/wghg-change-control-process.png` | Process diagram (detailed) | High-level process overview for Confluence pages and the A3 page of the process document. |
| `assets/wghg-change-control-process-a4.png` | Process diagram (compact) | Readable version of the overview for A4 pages, used on page 1 of the Word submission. |

### Tools (Maintainers Only)

| File | What It Is | Why It Exists |
|---|---|---|
| `tools/build_docs.js` | Word builder (Node.js, `docx` package) | Regenerates both Word documents from their Markdown sources, so Confluence and Word always match. |
| `tools/build_run_sheet.py` | Excel builder (Python, `openpyxl`) | Regenerates the Run Sheet workbook. |

---

## Per-Change Workflow (Which File, When)

| When | Do This | File |
|---|---|---|
| Change raised | Create the change page in Confluence (or copy the Word template) and name it with the CHG number | CCB Change Submission |
| Planning | Copy the Run Sheet workbook; complete Change Details, Run Sheet and Contacts | Run Sheet workbook |
| Before the CCB | Complete the Plan on a Page (A3) and the remaining submission sections; obtain endorsements | Run Sheet workbook – Plan on a Page; CCB Change Submission |
| At the CCB | Present the Plan on a Page; the CCB records its decision in Section 14 | CCB Change Submission |
| Change window | Work through the Run Sheet; log communications, decisions and issues | Run Sheet workbook |
| After the change | Complete the Implementation Record, PIR (if required) and Closure; attach the final Run Sheet | CCB Change Submission |
