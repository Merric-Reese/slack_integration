# Handoff – WGHG ICT Change Control Pack

**Branch:** `claude/relaxed-bell-b8219d`
**Work folder:** `wghg-change-control/`
**Status:** second draft complete and pushed; waiting for WGHG review

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
9. Two **simpler templates** containing only the mandatory information: **Minor** and **Medium**. The full template is kept for **High / Critical**.
10. A **flowchart (Mermaid)** in all the process files, to help people decide which change process to follow.
11. **Use ITIL to determine risk levels** for now; refine later.

### Decisions made with the user

- **Tiers follow the risk level:** Low → Minor template; Medium → Medium template; High or Critical → High / Critical template.
- **"Extreme" renamed "Critical"** everywhere.
- **Attachments:** Minor needs none, because its steps are written in the form. Medium and High / Critical attach the Run Sheet and present the A3 Plan on a Page.

---

## 2. What Was Delivered

Everything is in `wghg-change-control/`. **Read `INDEX.md` first.**

| File | Summary |
|---|---|
| `WGHG_CCB_ICT_Change_Submission_Template_Minor.md` / `.docx` | Low risk short form (5 Word pages). Includes the selector flowchart and the impact × probability checklist. |
| `WGHG_CCB_ICT_Change_Submission_Template_Medium.md` / `.docx` | Medium risk form (7 Word pages). The A3 Plan on a Page is page 3. |
| `WGHG_CCB_ICT_Change_Submission_Template_High-Critical.md` / `.docx` | Full submission (14 Word pages). The A3 Plan on a Page is page 4; the CCB Decision starts on a new page. Previously named `WGHG_CCB_ICT_Change_Submission_Template.*`. |
| `WGHG_CCB_ICT_Change_Run_Sheet_Template.xlsx` | Workbook for Medium and above. Tabs: Change Details, Plan on a Page (A3, auto-filled), Run Sheet (24 draft steps), Contacts, Comms Log, Issues & Decisions, and a hidden Lists tab. |
| `WGHG_ICT_Change_Control_Process.md` / `.docx` | Process document, v0.2 DRAFT (10 Word pages). Section 2 is the overview (A3 page). Section 3 is the process selector. Section 7 covers change types, ITIL risk levels and templates. |
| `WGHG_Confluence_Page_Structure.md` | Paste-ready Confluence page tree, naming conventions and labels. |
| `INDEX.md`, `README.md` | File index and per-change workflow; rebuild instructions and assumptions. |
| `assets/` | WGHG logos (from wghg.com.au), the process overview diagrams, and the selector flowchart (`.mmd` source and `.png`). |
| `tools/` | `shared_blocks.py`, `build_docs.js` and `build_run_sheet.py`. |

### Risk levels (ITIL impact × probability)

| Impact | Probability | Risk Level | Template |
|---|---|---|---|
| Low | Low | Low | Minor |
| Low | High | Medium | Medium |
| High | Low | High | High / Critical |
| High | High | Critical | High / Critical |

- **Criteria:** Impact is High if any of I1–I7 applies (clinical systems or patient care, medical devices, 24/7 areas, outage in hours, user / site threshold, security / privacy, interfaces). Probability is High if any of P1–P7 applies (new, untested, complex, vendor-dependent, previous failure, untested backout, tight window).
- **Source:** I confirmed from public sources that ITIL assesses change risk from impact and probability. I could **not** check the ITIL publication's own example matrix: the hosts were blocked, and no web result showed it. The documents therefore describe the criteria and the four-level mapping as a WGHG starting point, not as official ITIL wording.

### Logo sources (from the WGHG website)

- Banner: https://wghg.com.au/wp-content/uploads/2018/11/Untitled-design-30.png
- Logo mark: https://wghg.com.au/wp-content/uploads/2022/03/cropped-wghg-fav-icon-270x270.png
- Brand colours sampled from the banner: navy `#00577D`, orange `#F7A11A`, light blue `#78B3D0`.

---

## 3. How to Rebuild

Run these from `wghg-change-control/`:

```bash
python3 tools/shared_blocks.py .      # copies the selector flowchart, selection table and criteria into every .md
node tools/build_docs.js .            # rebuilds all four Word documents (needs the "docx" npm package)
python3 tools/build_run_sheet.py .    # rebuilds the workbook (needs openpyxl and Pillow)
```

- **Shared blocks:** edit the risk criteria and selection table in `tools/shared_blocks.py`, and the flowchart in `assets/wghg-change-process-selector.mmd`.
- **Flowchart image:** after changing the `.mmd`, re-render the PNG. It was rendered with mermaid 11.4.1 in headless Chromium.
- **Shared-block headings:** each block replaces the content under its fixed heading: "Which Change Process Should I Follow?", "Impact and Probability Assessment" and "Impact and Probability Criteria". **Don't rename these headings.**
- **Word-builder headings:** the builder also relies on "Plan on a Page (A3)", "2. Process at a Glance" and "N. CCB Decision".
- **Excel:** openpyxl writes formulas without cached results. Open the workbook in Excel and save it, or recalculate it with LibreOffice.

---

## 4. Verification Done

- **Word:** all four documents rendered to PDF and checked; all pass the DOCX schema validation. A3 pages: Medium page 3, High / Critical page 4, process document page 2.
- **Excel:** formulas recalculated with **0 errors**. Plan on a Page timeline values and bars spot-checked against the Run Sheet.
- **Markdown:** all tables parse as GitHub-flavoured Markdown, and the files contain no raw HTML. The only HTML-like text is `<br/>` inside the Mermaid code blocks.
- **Flowchart:** the Mermaid source renders without errors (mermaid 11.4.1).
- **Not tested:** the files have **not** been opened in Microsoft Word or Excel, nothing has been pasted into Confluence, and a Confluence Mermaid add-on has not been tested.

---

## 5. Open Items / Next Steps

| # | Item | Owner |
|---|---|---|
| 1 | **Slack completion message not sent.** The Slack connector failed to connect in the cloud session (proxy 403). Send it from the Mac session, or fix the connector. Suggested text is below. | User / Mac session |
| 2 | Refine the risk criteria (I1–I7, P1–P7), the user threshold in I5 and the Low / Medium / High / Critical mapping. Align them with the WGHG Risk Management Framework. | WGHG ICT / Risk |
| 3 | Confirm the placeholders: CCB membership, quorum, meeting frequency, agenda cut-off, lead times, freeze periods, emergency CCB quorum, and any extra endorsement for Critical changes. | WGHG ICT |
| 4 | Replace the generic system examples (EMR, PAS, PACS) and site placeholders with WGHG's actual systems and sites. | WGHG ICT |
| 5 | Open the `.docx` and `.xlsx` files in Microsoft Office and confirm the layout, A3 printing, drop-downs and conditional formatting. | User |
| 6 | Confluence: check whether the site has a Mermaid add-on. If not, use the PNG. Create the pages marked "[to be created]". | WGHG ICT |
| 7 | Decide whether to keep this work in the `slack_integration` repository or move it to a dedicated repository or Confluence space. | User |

**Suggested Slack message:**

> The WGHG ICT Change Control pack is ready for review:
> - three CCB submission templates (Minor, Medium, High / Critical) in Word and Confluence;
> - a "Which change process should I follow?" flowchart;
> - ITIL impact × probability risk levels;
> - a run sheet workbook with an A3 Plan on a Page;
> - the process document, a Confluence page structure and a file index.
>
> It's on branch `claude/relaxed-bell-b8219d`, folder `wghg-change-control/`.

---

## 6. Environment Notes

- **Network:** the cloud session's Default environment blocked wghg.com.au. With the user's approval, a personal environment named **"slack_integration (WGHG web access)"** was created, which allows `wghg.com.au` and `www.wghg.com.au`. The session was switched onto it. Other sites, such as ITIL reference pages, are still blocked from this session.
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
| `66a13a9` | Add HANDOFF.md |
| (this commit) | Add Minor and Medium templates, process selector flowchart and ITIL risk levels |
