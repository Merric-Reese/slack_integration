"""Shared Markdown blocks used in the WGHG change templates and process document.

Edit the text here, then run:  python3 tools/shared_blocks.py .
It rewrites the block under each fixed heading (see HEADINGS) in every Markdown file,
so the process selector, selection table and risk criteria stay identical everywhere.
"""
import os, re, sys

D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MMD = open(os.path.join(D, "assets", "wghg-change-process-selector.mmd"), encoding="utf-8").read().strip()

SELECTOR = f"""*Use this flowchart and the impact and probability criteria to decide whether the work is a change, which type of change it is, its risk level, and which CCB submission template to use.*

| Impact | Probability | Risk Level | Template to Use | Attachments |
|---|---|---|---|---|
| Low | Low | Low | **Minor** | None – implementation and backout steps are written in the form |
| Low | High | Medium | **Medium** | Run Sheet (Excel) and A3 Plan on a Page |
| High | Low | High | **High / Critical** | Run Sheet (Excel) and A3 Plan on a Page; PIR always required |
| High | High | Critical | **High / Critical** | Run Sheet (Excel) and A3 Plan on a Page; PIR always required; [Enter any extra endorsement WGHG requires, e.g. Executive sponsor] |

*Risk levels follow the ITIL approach of assessing a change's impact and the probability of the risk occurring. The High / Low criteria below and the mapping to Low / Medium / High / Critical are a WGHG starting point, to be refined.*

```mermaid
{MMD}
```

![Which change process should I follow?](assets/wghg-change-process-selector.png)

*Confluence: Confluence does not draw Mermaid diagrams without an add-on. Upload `assets/wghg-change-process-selector.png` and insert it here, or paste the Mermaid code above into a Mermaid macro if your site has one.*"""

IMPACT = [
    ("I1", "Affects a clinical system, patient care, or the availability of patient information"),
    ("I2", "Affects a medical device or a medical device interface"),
    ("I3", "Affects a 24/7 critical area (e.g. Emergency, ICU / HDU, Maternity, Theatres)"),
    ("I4", "Causes a user-facing outage or degraded service during clinical or business hours"),
    ("I5", "Affects more than [Enter threshold, e.g. 50] users, or more than one site"),
    ("I6", "Changes security controls, access, firewall rules, or how health or personal information is handled"),
    ("I7", "Affects integrations or interfaces with other systems"),
]
PROB = [
    ("P1", "The change has not been done before at WGHG"),
    ("P2", "The change has not been tested in a test / UAT environment"),
    ("P3", "The change is complex: many steps, several teams or several CIs"),
    ("P4", "Success depends on a vendor or third party"),
    ("P5", "A similar change has failed or caused an incident before"),
    ("P6", "The backout has not been tested, or the change cannot be backed out"),
    ("P7", "The implementation window is tight for the work plus a full backout"),
]

def criteria(answer_cols: bool) -> str:
    if answer_cols:
        hi = "| # | High-Impact Criterion | Applies? | Details |\n|---|---|---|---|\n" + "\n".join(f"| {k} | {t} | ☐ Yes ☐ No | [Enter] |" for k, t in IMPACT)
        hp = "| # | High-Probability Criterion | Applies? | Details |\n|---|---|---|---|\n" + "\n".join(f"| {k} | {t} | ☐ Yes ☐ No | [Enter] |" for k, t in PROB)
    else:
        hi = "| # | High-Impact Criterion |\n|---|---|\n" + "\n".join(f"| {k} | {t} |" for k, t in IMPACT)
        hp = "| # | High-Probability Criterion |\n|---|---|\n" + "\n".join(f"| {k} | {t} |" for k, t in PROB)
    return (f"**Impact is High if ANY of these apply:**\n\n{hi}\n\n"
            f"**Probability is High if ANY of these apply:**\n\n{hp}\n\n"
            "| Impact ↓ / Probability → | Low Probability | High Probability |\n|---|---|---|\n"
            "| **High Impact** | High | Critical |\n| **Low Impact** | Low | Medium |")

# Each block lives under a fixed heading and runs until the next heading or "---" line.
HEADINGS = {
    "## Which Change Process Should I Follow?": SELECTOR,
    "### Impact and Probability Assessment": criteria(True),
    "### Impact and Probability Criteria": criteria(False),
}

def apply(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    out, i, n = [], 0, 0
    while i < len(lines):
        out.append(lines[i])
        key = re.sub(r"^(#+ )\d+(\.\d+)*\. ", r"\1", lines[i].strip())
        body = HEADINGS.get(key)
        if body is not None:
            j = i + 1
            while j < len(lines) and not (lines[j].startswith("#") or lines[j].strip() == "---"):
                j += 1
            out += [""] + body.split("\n") + [""]
            i, n = j, n + 1
            continue
        i += 1
    open(path, "w", encoding="utf-8").write("\n".join(out))
    return n

if __name__ == "__main__":
    for f in sorted(os.listdir(D)):
        if f.endswith(".md"):
            n = apply(os.path.join(D, f))
            if n: print(f"{f}: {n} block(s) updated")
