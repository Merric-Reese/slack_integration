# ICT Change Control – Confluence Page Structure (Draft)

**West Gippsland Healthcare Group (WGHG) – ICT**

> **How to use:** Copy everything from "Page Tree" down and paste it into a new Confluence page called **ICT Change Control**. The nested list becomes the outline. Then create each listed item as a child page under its parent, using the name shown. Items marked **[to be created]** have no template in this pack yet. Folder and page names are a suggestion only; rename them to suit the WGHG space.

---

## Page Tree

- **ICT Change Control** (space home / parent page)
    - **01 – Change Control Process**
        - ICT Change Control Process – paste `WGHG_ICT_Change_Control_Process.md`
        - Process at a Glance – attach `assets/wghg-change-control-process.png`
        - Which Change Process Should I Follow? – from Section 3 of the process; attach `assets/wghg-change-process-selector.png` (or use a Mermaid macro with `assets/wghg-change-process-selector.mmd`)
        - Risk Levels and Templates – from Section 7 of the process
        - Roles and Responsibilities – from Section 6 of the process
        - Emergency Change Procedure – from Section 10 of the process
        - Change Freeze and Blackout Calendar **[to be created]**
    - **02 – Templates**
        - CCB Change Submission – Minor (Low Risk) – paste `WGHG_CCB_ICT_Change_Submission_Template_Minor.md`; attach the `.docx`
        - CCB Change Submission – Medium Risk – paste `WGHG_CCB_ICT_Change_Submission_Template_Medium.md`; attach the `.docx`
        - CCB Change Submission – High / Critical Risk – paste `WGHG_CCB_ICT_Change_Submission_Template_High-Critical.md`; attach the `.docx`
        - Save each as a Confluence page template, if your site allows it
        - ICT Change Run Sheet and Plan on a Page (Excel) – attach `WGHG_CCB_ICT_Change_Run_Sheet_Template.xlsx`
        - Template Index – paste `INDEX.md`
    - **03 – Change Control Board (CCB)**
        - CCB Terms of Reference **[to be created]**
        - CCB Membership and Contacts **[to be created]**
        - CCB Meetings
            - YYYY-MM-DD CCB Meeting – Agenda and Minutes **[to be created – one page per meeting]**
        - CCB Decision and Action Register **[to be created]**
    - **04 – Changes** (one page per change)
        - YYYY
            - CHG0001234 – [Change Title]
                - CCB Submission – created from the Minor, Medium or High / Critical template
                - Attachments (Medium and above): Run Sheet (Excel); Plan on a Page (A3 PDF export); test evidence
                - Implementation Record and PIR – Sections 15–17 of the submission
    - **05 – Change Schedule** – forward schedule of approved changes **[to be created]**
    - **06 – Standard Change Catalogue** – pre-authorised standard change models **[to be created]**
    - **07 – Reports and Measures** – change success, emergency changes, PIR completion (process Section 14) **[to be created]**

---

## Same Structure as a Text Tree

```text
ICT Change Control
├── 01 – Change Control Process
│   ├── ICT Change Control Process
│   ├── Process at a Glance
│   ├── Which Change Process Should I Follow?
│   ├── Risk Levels and Templates
│   ├── Roles and Responsibilities
│   ├── Emergency Change Procedure
│   └── Change Freeze and Blackout Calendar        [to be created]
├── 02 – Templates
│   ├── CCB Change Submission – Minor (Low Risk)
│   ├── CCB Change Submission – Medium Risk
│   ├── CCB Change Submission – High / Critical Risk
│   ├── ICT Change Run Sheet and Plan on a Page (Excel)
│   └── Template Index
├── 03 – Change Control Board (CCB)
│   ├── CCB Terms of Reference                      [to be created]
│   ├── CCB Membership and Contacts                 [to be created]
│   ├── CCB Meetings
│   │   └── YYYY-MM-DD CCB Meeting                  [to be created]
│   └── CCB Decision and Action Register            [to be created]
├── 04 – Changes
│   └── YYYY
│       └── CHG0001234 – [Change Title]
│           ├── CCB Submission
│           ├── Run Sheet + Plan on a Page (Medium and above)
│           └── Implementation Record and PIR
├── 05 – Change Schedule                            [to be created]
├── 06 – Standard Change Catalogue                  [to be created]
└── 07 – Reports and Measures                       [to be created]
```

---

## Naming Conventions

| Item | Convention | Example |
|---|---|---|
| Change page | `CHG number – Short title` | CHG0001234 – Core switch firmware upgrade |
| CCB submission (Word) | `CHG number_CCB_Submission_vX.Y.docx` | CHG0001234_CCB_Submission_v1.0.docx |
| Run sheet (Excel) | `CHG number_Run_Sheet_vX.Y.xlsx` | CHG0001234_Run_Sheet_v1.0.xlsx |
| Plan on a Page (PDF export) | `CHG number_Plan_on_a_Page.pdf` | CHG0001234_Plan_on_a_Page.pdf |
| CCB meeting page | `YYYY-MM-DD CCB Meeting` | 2026-12-01 CCB Meeting |

*The example change title above is illustrative only.*

---

## Suggested Page Labels

| Label | Apply To |
|---|---|
| `change-control` | Every page in this tree |
| `ccb-submission` | Each change's CCB Submission page |
| `risk-low` / `risk-medium` / `risk-high` / `risk-critical` | Each change page, by its risk level |
| `ccb-approved` / `ccb-deferred` / `ccb-rejected` | Each change page, once the CCB has decided |
| `emergency-change` | Emergency change pages |
| `pir-required` | Changes that need a Post-Implementation Review |

*Labels let you build lists of changes by status, e.g. all `ccb-approved` changes awaiting implementation.*
