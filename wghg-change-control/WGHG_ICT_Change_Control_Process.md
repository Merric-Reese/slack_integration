![West Gippsland Healthcare Group](https://wghg.com.au/wp-content/uploads/2018/11/Untitled-design-30.png)

# ICT Change Control Process

**West Gippsland Healthcare Group (WGHG) – Information & Communication Technology**

**Process document – aligned to ITIL 4 Change Enablement – DRAFT for review**

> **Draft status:** This process is a draft for WGHG review. Items in `[Enter …]` placeholders must be confirmed against WGHG policy and the CCB Terms of Reference before this document is approved: CCB membership, quorum, meeting frequency, lead times and freeze periods.

---

## 1. Document Control

| Field | Value |
|---|---|
| Document Title | ICT Change Control Process |
| Document Owner | [Enter, e.g. ICT Manager] |
| Approved By | [Enter, e.g. Chief Information Officer / Executive Director] |
| Version | [0.1 DRAFT] |
| Approval Date | [DD/MM/YYYY] |
| Next Review Date | [DD/MM/YYYY] |
| Related Policy | [Enter WGHG ICT Change Management Policy reference] |

### Version History

| Version | Date | Author | Summary of Changes |
|---|---|---|---|
| 0.1 | [DD/MM/YYYY] | [Name] | Initial draft |

---

## 2. Process at a Glance (High-Level Overview)

![WGHG ICT Change Control Process – high-level overview](assets/wghg-change-control-process.png)

*Confluence: upload `assets/wghg-change-control-process.png` to this page and insert it here. The table below is a text version of the same diagram.*

| Step | Stage | Who | What Happens | Record / Template |
|---|---|---|---|---|
| 1 | Raise & Record | Change Requester | RFC logged in the ITSM tool; CCB Submission started | ITSM record; CCB Change Submission (draft) |
| 2 | Assess & Plan | Change Owner, Change Manager | Impact, clinical safety and risk assessment; Run Sheet and Plan on a Page prepared; pre-CCB endorsements obtained | CCB Change Submission; Run Sheet; Plan on a Page (A3) |
| 3 | CCB Authorise | Change Control Board | Change presented to the CCB, which records its decision | CCB Change Submission – Section 14 |
| 4 | Schedule & Communicate | Change Manager | Window confirmed on the Change Schedule; stakeholders notified | Change Schedule; Run Sheet – Comms Log |
| 5 | Implement | Implementation Lead | Run Sheet executed; Go / No-Go checkpoint; verification or backout | Run Sheet; Issues & Decisions Log |
| 6 | Review (PIR) | Change Owner, reported to the CCB | Outcome confirmed; PIR completed where required | CCB Change Submission – Sections 15–16 |
| 7 | Close | Change Manager | ITSM record and CMDB updated; change closed | CCB Change Submission – Section 17 |

**CCB outcomes:** Deferred → return to Step 2 with the information requested. Rejected → go to Step 7 and close as Rejected.

**Emergency change:** an emergency CCB quorum authorises → implement → the change is presented to the next scheduled CCB for retrospective review (Section 9).

**Standard change:** low-risk and pre-authorised; follows its approved standard change model and is not submitted to the CCB (Section 6).

---

## 3. Purpose

This document defines how WGHG ICT changes are raised, assessed, authorised by the Change Control Board (CCB), implemented, reviewed and closed. The process aims to:

- protect patient safety and the continuity of clinical and business services;
- make sure every change is assessed for impact and risk before it is made;
- give the CCB the information it needs to authorise each change;
- reduce incidents caused by change, and restore service quickly when a change fails;
- keep an auditable record of every change.

---

## 4. Scope

| In Scope | Out of Scope |
|---|---|
| Changes to ICT infrastructure, networks, servers, storage and cloud services | Service requests (e.g. password resets, new user accounts, standard software installs) |
| Changes to clinical and business applications, interfaces and integrations | Changes to content or data that do not alter configuration (e.g. routine data entry) |
| Changes to information security controls (firewalls, access, authentication) | Non-ICT facilities changes, unless they affect ICT services |
| Changes to medical device integration managed by ICT | [Enter other exclusions confirmed by WGHG] |
| Vendor-delivered changes to WGHG ICT services | |

ITIL 4 defines a change as "the addition, modification or removal of anything that could have a direct or indirect effect on services".

---

## 5. Roles and Responsibilities

| Role | Responsibilities in this process |
|---|---|
| Change Requester | Raises the RFC; describes the change and the reason for it. |
| Change Owner | Accountable for the change end to end; prepares the CCB Submission; presents to the CCB; owns the PIR. |
| Change Manager | Owns this process; checks submissions are complete; assesses risk; maintains the Change Schedule; runs Go / No-Go; closes changes. |
| Change Control Board (CCB) | Reviews each submitted change and authorises, defers or rejects it; sets conditions; reviews PIRs and emergency changes. |
| CCB Chair | Chairs the CCB; confirms quorum; signs off CCB decisions. |
| CCB Secretariat | Manages the agenda and cut-off; distributes submission packs; records minutes and actions. |
| Implementation Lead / Implementer | Builds and tests the change; prepares and executes the Run Sheet; executes backout if required. |
| Business / Clinical Owner | Confirms business and clinical impact; endorses the change; verifies service after implementation. |
| Information Security | Reviews security and privacy impact; endorses changes with security impact. |
| ICT Service Desk | Is briefed before the change; handles user contacts; logs related incidents. |
| After-Hours Hospital Coordinator / Manager | Is notified of after-hours changes and outages; coordinates clinical areas. |

**CCB membership:** [Enter membership, e.g. ICT Manager (Chair), Change Manager, Infrastructure Lead, Applications Lead, Information Security, Clinical Informatics representative, Service Desk Lead].

---

## 6. Change Types and Authorisation

| Change Type | Definition (ITIL 4) | Authorised By | Lead Time to CCB |
|---|---|---|---|
| Standard | Low-risk, pre-authorised change that is well understood and fully documented. It can be implemented without further authorisation. | Pre-authorised standard change model (approved once by the CCB) | Not submitted to the CCB |
| Normal | Change that must be scheduled, assessed and authorised following the defined process. | CCB | Submission received by [Enter, e.g. 5 business days] before the CCB meeting |
| Emergency | Change that must be implemented as soon as possible, e.g. to resolve a major incident or apply an urgent security patch. | Emergency CCB quorum [Enter, e.g. CCB Chair plus one member] | As soon as possible; retrospective review at the next CCB |

**Risk rating:** every Normal and Emergency change is rated Low, Medium, High or Extreme using the 5×5 matrix in the CCB Change Submission (Section 7). High and Extreme risk changes also require [Enter, e.g. Executive sponsor endorsement].

---

## 7. Change Control Board (CCB)

| Item | Detail |
|---|---|
| Purpose | Assess and authorise Normal changes; review emergency changes and PIRs; maintain oversight of the Change Schedule. |
| Meeting frequency | [Enter, e.g. weekly, Tuesday 10:00] |
| Quorum | [Enter, e.g. Chair or delegate plus three members] |
| Agenda cut-off | [Enter, e.g. 5 business days before the meeting] |
| Inputs | One CCB Change Submission per change, with its Plan on a Page (A3) and draft Run Sheet attached |
| Decisions | Approved · Approved with conditions · Deferred – more information required · Rejected · Noted (retrospective emergency change) |
| Outputs | Decision recorded in Section 14 of the submission; minutes and actions; updated Change Schedule |
| Terms of Reference | [Enter link to the CCB Terms of Reference] |

---

## 8. Detailed Procedure – Normal Change

| # | Activity | Responsible | Output / Record | Template / Tool |
|---|---|---|---|---|
| 1.1 | Log the RFC in the ITSM tool and obtain a Change ID. | Change Requester | ITSM change record | ITSM tool |
| 1.2 | Create the CCB Change Submission for this change from the template. | Change Owner | Draft submission | CCB Change Submission template |
| 2.1 | Complete the change details, description and ITIL "7 Rs" checklist. | Change Owner | Submission Sections 3–5 | CCB Change Submission |
| 2.2 | Complete the clinical, business, security and privacy impact assessment. | Change Owner with the Business / Clinical Owner and Information Security | Submission Section 6 | CCB Change Submission |
| 2.3 | Complete the risk assessment and confirm the overall risk rating. | Change Owner, Change Manager | Submission Section 7 | CCB Change Submission |
| 2.4 | Prepare the draft Run Sheet, including backout steps and Go / No-Go checkpoints. | Implementation Lead | Draft Run Sheet | Run Sheet template |
| 2.5 | Complete the A3 Plan on a Page. | Change Owner | Plan on a Page | Run Sheet – Plan on a Page tab, or the A3 page in the Word submission |
| 2.6 | Check the Change Schedule and freeze periods for conflicts. | Change Manager | Submission Section 11 | Change Schedule |
| 2.7 | Obtain pre-CCB endorsements. | Change Owner | Submission Section 13.2 | CCB Change Submission |
| 2.8 | Submit to the CCB Secretariat by the agenda cut-off. | Change Owner | CCB agenda item | CCB agenda |
| 3.1 | Present the change to the CCB. | Change Owner | — | Plan on a Page |
| 3.2 | Make and record the decision, conditions and actions. | CCB Chair, CCB Secretariat | Submission Section 14; minutes | CCB Change Submission |
| 4.1 | Confirm the approved window on the Change Schedule. | Change Manager | Change Schedule entry | Change Schedule |
| 4.2 | Issue communications per the communication plan. | Change Manager | Comms Log | Run Sheet – Comms Log tab |
| 5.1 | Run the pre-implementation steps; hold the Go / No-Go decision. | Change Manager, Implementation Lead | Decision logged | Run Sheet; Issues & Decisions Log |
| 5.2 | Implement and verify the change; obtain clinical / business verification. | Implementation Lead, Business / Clinical Owner | Run Sheet status updated | Run Sheet |
| 5.3 | If a backout trigger occurs or the backout decision point is reached, decide whether to back out and execute the backout steps. | Change Manager, Implementation Lead | Backout logged | Run Sheet – Phase 6 |
| 5.4 | Notify completion; record the implementation outcome. | Change Manager | Submission Section 15 | CCB Change Submission |
| 6.1 | Complete the PIR where required and present it to the CCB. | Change Owner | Submission Section 16 | CCB Change Submission |
| 7.1 | Update the CMDB and documentation; attach the final Run Sheet; close the change. | Change Manager | Submission Section 17; closed ITSM record | ITSM tool |

---

## 9. Emergency Change Procedure

| # | Activity | Responsible |
|---|---|---|
| E1 | Log the emergency RFC in the ITSM tool and link the related major incident or security advisory. | Change Owner |
| E2 | Complete the minimum sections of the CCB Change Submission: 1, 2, 3, 6.1, 7, 10 and 13.2. | Change Owner |
| E3 | Convene the emergency CCB quorum (in person, by phone or electronically) and record its decision. | Change Manager, CCB Chair |
| E4 | Notify the Service Desk, the After-Hours Hospital Coordinator and affected clinical areas. | Change Manager |
| E5 | Implement using a Run Sheet, including backout. | Implementation Lead |
| E6 | Complete the remaining sections and the PIR, and present the change to the next scheduled CCB for retrospective review ("Noted"). | Change Owner |

---

## 10. Change Freeze and Blackout Periods

| Period | Rule |
|---|---|
| [Enter, e.g. public holiday periods / end of financial year] | [Enter, e.g. Emergency changes only] |
| [Enter, e.g. major clinical system go-live periods] | [Enter rule] |
| [Enter other periods] | [Enter rule] |

Changes during a freeze period require [Enter, e.g. CCB Chair and Executive approval].

---

## 11. Implementation Controls

- **Run Sheet:** every Normal and Emergency change is implemented from a Run Sheet with timed steps, owners and validation criteria.
- **Go / No-Go:** implementation does not start until the Go / No-Go decision is made and recorded.
- **Backout decision point:** the run sheet sets the latest time at which a backout can start and still finish within the approved window.
- **Clinical verification:** changes affecting clinical systems are verified by the Business / Clinical Owner before completion is declared.
- **Variation:** any deviation from the approved plan or CCB conditions is logged in the Issues & Decisions Log and reported in the Implementation Record.

---

## 12. Post-Implementation Review and Closure

A PIR is required when a change:

- failed or was backed out;
- was an emergency change;
- was rated High or Extreme risk;
- caused an incident; or
- was flagged for review by the CCB.

The Change Owner presents the PIR to the CCB, and the CCB Secretariat tracks PIR actions to completion. The Change Manager closes the change once the CMDB, documentation and ITSM record are updated.

---

## 13. Measures

| Measure | Target |
|---|---|
| Percentage of changes implemented successfully without backout | [Enter target] |
| Number of changes that caused an incident | [Enter target] |
| Percentage of emergency changes (of all changes) | [Enter target] |
| Number of unauthorised changes detected | [Enter target – normally zero] |
| Percentage of required PIRs completed within [Enter] days | [Enter target] |
| Percentage of CCB submissions received by the agenda cut-off | [Enter target] |

---

## 14. Records and Templates

| Record / Template | Used At Step | Location |
|---|---|---|
| CCB Change Submission (Word / Confluence) – one per change | 1–3, 5–7 | [Enter Confluence / document library link] |
| Plan on a Page (A3) – one per change | 2–3 | Run Sheet – Plan on a Page tab; A3 page in the Word submission |
| ICT Change Run Sheet (Excel) – one per change | 2, 4–5, 7 | Attached to the change's Confluence page and ITSM record |
| ITSM change record | 1–7 | [Enter ITSM tool] |
| Change Schedule | 2, 4 | [Enter location] |
| CCB agenda and minutes | 3, 6 | [Enter location] |

---

## 15. Related Documents

| Document | Reference |
|---|---|
| WGHG ICT Change Management Policy | [Enter] |
| CCB Terms of Reference | [Enter] |
| WGHG Risk Management Framework | [Enter] |
| Clinical system downtime procedures | [Enter] |
| Information Security Policy | [Enter] |
| Major Incident Management Process | [Enter] |

---

*West Gippsland Healthcare Group – ICT Change Control Process – Version 0.1 DRAFT – Uncontrolled when printed.*
