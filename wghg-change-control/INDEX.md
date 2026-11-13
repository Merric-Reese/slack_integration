# WGHG ICT Change Control Pack – File Index

**West Gippsland Healthcare Group (WGHG) – ICT Change Control Board (CCB)**

This pack supports **one change at a time** through the WGHG ICT Change Control process. For each change, you:

1. use the **"Which Change Process Should I Follow?"** flowchart to set its risk level;
2. complete **one** CCB Submission on the template for that risk level;
3. for Medium, High and Critical changes, complete **one** Run Sheet workbook, which includes the A3 Plan on a Page.

---

## Which Template? (Summary)

Risk level = ITIL impact × probability. The criteria are in the process document, Section 7.2, and in every template.

| Impact | Probability | Risk Level | CCB Submission Template | Run Sheet + A3 Plan on a Page |
|---|---|---|---|---|
| Low | Low | Low | Minor | Not required |
| Low | High | Medium | Medium | Required |
| High | Low | High | High / Critical | Required |
| High | High | Critical | High / Critical | Required |

Service requests and Standard (pre-authorised) changes do not go to the CCB.

---

## Process at a Glance

| Step | Stage | Files Used |
|---|---|---|
| 0 | Decide the process | Process selector flowchart (in every template and the process document) |
| 1 | Raise & Record | CCB Change Submission – Minor, Medium or High / Critical (started) |
| 2 | Assess & Plan | CCB Change Submission; Run Sheet workbook for Medium and above (Run Sheet, Plan on a Page, Contacts) |
| 3 | CCB Authorise | Plan on a Page (A3) presented for Medium and above; CCB Decision section completed |
| 4 | Schedule & Communicate | Run Sheet workbook – Comms Log (Minor: Communication section of the form) |
| 5 | Implement | Run Sheet workbook – Run Sheet, Issues & Decisions (Minor: the steps written in the form) |
| 6 | Review (PIR) | CCB Change Submission – PIR / lessons learned |
| 7 | Close | CCB Change Submission – Closure; final Run Sheet attached to the ITSM record |

---

## File Index

### Process and Guidance

| File | What It Is | Why It Exists | Process Step | Used By |
|---|---|---|---|---|
| `WGHG_ICT_Change_Control_Process.md` | Process document (Confluence) | Defines how changes are raised, assessed, authorised by the CCB, implemented, reviewed and closed. Section 2 is the high-level overview; Section 3 is the process selector flowchart; Section 7 covers change types, ITIL risk levels and templates. | All steps (reference) | Everyone involved in change |
| `WGHG_ICT_Change_Control_Process.docx` | Same process document (Word) | For formal review, approval and printing. Section 2 prints on an A3 landscape page. | All steps (reference) | Document owner, approvers |
| `WGHG_Confluence_Page_Structure.md` | Draft Confluence page tree | Paste-ready outline for setting up the ICT Change Control space, with naming conventions and labels. | Set-up (once) | Confluence space administrator |
| `INDEX.md` | This file | Explains every file, why it exists and where it fits. | Set-up and reference | Everyone |
| `README.md` | Short repository readme | Points to this index and explains how to rebuild the files. | — | Maintainers |

### CCB Submission Templates – Complete One per Change

All three templates contain the process selector flowchart and the ITIL impact and probability assessment.

| File | Risk Level | What It Contains | Process Step | Used By |
|---|---|---|---|---|
| `WGHG_CCB_ICT_Change_Submission_Template_Minor.md` / `.docx` | Low | Short form: change details, reason, impact and probability assessment, main risk, implementation / verification / backout steps, communication and endorsement, CCB decision, outcome and closure. No attachments. | 1–7 | Change Owner; CCB |
| `WGHG_CCB_ICT_Change_Submission_Template_Medium.md` / `.docx` | Medium | The A3 Plan on a Page (page 3 in Word); change details; description; impact and probability assessment; key risks; implementation, testing and backout summary; schedule and communication; endorsements; CCB decision; implementation record; PIR and closure. | 1–7 | Change Owner; CCB |
| `WGHG_CCB_ICT_Change_Submission_Template_High-Critical.md` / `.docx` | High or Critical | Full submission: process overview, A3 Plan on a Page, executive summary, ITIL "7 Rs", detailed impact assessment, impact and probability assessment with a risk register, test, backout, schedule, communication, RACI, endorsements, CCB decision, implementation record, PIR, closure. | 1–7 | Change Owner; CCB Secretariat; CCB |

### Run Sheet Workbook – Medium, High and Critical Changes

| File | What It Is | Why It Exists | Process Step | Used By |
|---|---|---|---|---|
| `WGHG_CCB_ICT_Change_Run_Sheet_Template.xlsx` | Run Sheet workbook (Excel) | The timed implementation plan for the change, plus the auto-filled A3 Plan on a Page. | 2, 3, 4, 5, 7 | Implementation Lead; Change Manager |

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
| `assets/wghg-header-banner.png` | WGHG logo banner | Page header in the Word documents and the Excel tabs. Downloaded from https://wghg.com.au/wp-content/uploads/2018/11/Untitled-design-30.png |
| `assets/wghg-logo-mark.png` | WGHG logo mark | Small logo on the Excel log tabs. Downloaded from https://wghg.com.au/wp-content/uploads/2022/03/cropped-wghg-fav-icon-270x270.png |
| `assets/wghg-change-process-selector.mmd` | Process selector flowchart – Mermaid source | Edit this to change the flowchart. It is copied into every template and the process document. |
| `assets/wghg-change-process-selector.png` | Process selector flowchart – image | For Word, and for Confluence pages without a Mermaid add-on. |
| `assets/wghg-change-control-process.png` | Process overview diagram (detailed) | High-level process overview for Confluence and the A3 page of the process document. |
| `assets/wghg-change-control-process-a4.png` | Process overview diagram (compact) | Readable version of the overview for A4 pages in the High / Critical template. |

### Tools (Maintainers Only)

| File | What It Is | Why It Exists |
|---|---|---|
| `tools/shared_blocks.py` | Shared-content script (Python) | Copies the process selector, selection table and impact / probability criteria into every Markdown file, so they stay identical. |
| `tools/build_docs.js` | Word builder (Node.js, `docx` package) | Regenerates all four Word documents from their Markdown sources, so Confluence and Word always match. |
| `tools/build_run_sheet.py` | Excel builder (Python, `openpyxl`) | Regenerates the Run Sheet workbook. |

---

## Per-Change Workflow (Which File, When)

| When | Do This | File |
|---|---|---|
| Change raised | Work through the process selector; rate impact and probability; pick the template | Process selector (any template, or process document Section 3) |
| Change raised | Create the change page in Confluence (or copy the Word template) and name it with the CHG number | Minor, Medium or High / Critical template |
| Planning (Medium and above) | Copy the Run Sheet workbook; complete Change Details, Run Sheet and Contacts | Run Sheet workbook |
| Before the CCB | Complete the submission and obtain endorsements. Medium and above: complete the A3 Plan on a Page | CCB Change Submission; Run Sheet workbook – Plan on a Page |
| At the CCB | Present the change (Plan on a Page for Medium and above); the CCB records its decision | CCB Change Submission – CCB Decision |
| Change window | Work through the Run Sheet (or the Minor template steps); log communications, decisions and issues | Run Sheet workbook, or Minor template |
| After the change | Complete the outcome, PIR (where required) and closure; attach the final Run Sheet | CCB Change Submission |
