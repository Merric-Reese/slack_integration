# WGHG ICT Change Control – CCB Templates

Templates for submitting **one ICT change** to the West Gippsland Healthcare Group (WGHG) **Change Control Board (CCB)**. They are aligned to the ITIL 4 Change Enablement practice.

| File | Purpose |
|---|---|
| `WGHG_CCB_ICT_Change_Submission_Template.md` | Confluence-compatible Markdown version of the CCB change submission |
| `WGHG_CCB_ICT_Change_Submission_Template.docx` | Word version of the same submission (WGHG banner in the page header, page X of Y footer) |
| `WGHG_CCB_ICT_Change_Run_Sheet_Template.xlsx` | Draft run sheet for implementing the CCB-approved change |
| `assets/wghg-header-banner.png` | WGHG logo banner, downloaded from https://wghg.com.au/wp-content/uploads/2018/11/Untitled-design-30.png |
| `assets/wghg-logo-mark.png` | WGHG logo mark, downloaded from https://wghg.com.au/wp-content/uploads/2022/03/cropped-wghg-fav-icon-270x270.png |

## Submission template sections

1. CCB Submission Details
2. Executive Summary for the CCB
3. Change Details
4. Description of the Change
5. ITIL "7 Rs" Checklist
6. Impact Assessment (clinical / patient safety, business, information security and privacy)
7. Risk Assessment (5×5 matrix)
8. Implementation Plan (summary)
9. Test Plan
10. Backout / Remediation Plan
11. Schedule and Conflicts
12. Communication Plan
13. Roles (RACI) and Pre-CCB Endorsements
14. CCB Decision, completed by the CCB (starts on a new page in Word)
15. Implementation Record
16. Post-Implementation Review (PIR)
17. Closure

Appendices: A covers the change lifecycle and B gives definitions.

## Using the Markdown in Confluence

The file uses only standard Markdown: headings, pipe tables, bold and italics. It contains no raw HTML, so Confluence will not strip anything.

- **Paste:** paste the Markdown into the Confluence editor, or insert it with the Markdown import or macro your Confluence version provides.
- **Logo:** the logo line points to the image on wghg.com.au. If your Confluence blocks external images, upload `assets/wghg-header-banner.png` to the page and insert it in place of the first line.

## Run sheet workbook

| Tab | Contents |
|---|---|
| Change Details | CCB approval, the approved window, the Go / No-Go time and the backout decision point, plus live progress formulas |
| Run Sheet | 24 draft steps across six phases: Pre-Implementation, Go / No-Go, Implementation, Verification, Post-Implementation and Backout |
| Contacts | Contacts and escalation levels |
| Comms Log | Record of communications during the change |
| Issues & Decisions | Record of issues and decisions during the change |

How the Run Sheet tab works:

- **Planned times:** Planned Start chains from the previous step's Planned End, and Planned End and Variance are calculated.
- **Status:** a drop-down that also colour-codes the row.
- **Checkpoints:** Go / No-Go rows are highlighted.
- **Window checks:** Change Details flags it if the planned finish, or a full backout, would run past the approved window.

### Example values to replace

These are examples only. Replace them for the real change:

- the dates, times and durations
- `CHG0001234`
- all blue italic text

## Assumptions to confirm against WGHG policy

- **Risk bands:** the risk matrix bands are a common 5×5 scheme. Align them with the WGHG Risk Management Framework.
- **CCB terms of reference:** quorum, emergency CCB arrangements and the agenda cut-off are placeholders.
- **Systems and sites:** examples such as EMR, PAS and PACS are generic. No WGHG-specific system names or sites were assumed.
