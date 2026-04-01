"""
Build README.md for Learning4CO from data/papers.csv.
Section order: (1) LLM for CO — rows with non-empty llm_for_co;
               (2) Survey Papers;
               (3) Problems — fixed PROBLEM_CATEGORY_ORDER in this file.
"""
from __future__ import annotations

import copy
import csv
from collections import Counter
from pathlib import Path
from urllib.parse import quote, urlparse

# Optional: set to "owner/repo" (e.g. "octocat/Learning4CO") to show GitHub stars/forks badges.
GITHUB_REPO_SLUG: str | None = None

abbr = {
    "Graph Matching": "GM",
    "Travelling Salesman Problem": "TSP",
    "Vehicle Routing Problem": "VRP",
    "Job Shop Scheduling Problem": "JSSP",
    "Flow Shop Problem": "FSP",
    "Bin Packing Problem": "BPP",
    "Graph Edit Distance": "GED",
    "Maximal Common Subgraph": "MCS",
    "Maximal Independent Set": "MIS",
    "Boolean Satisfiability": "SAT",
    "Quadratic Assignment Problem": "QAP",
    "Hamiltonian Cycle Problem": "HCP",
    "Multiple Travelling Salesman Problem": "mTSP",
    "Electronic Design Automation": "EDA",
    "Orienteering Problem": "OP",
    "Virtual Network Embedding": "VNE",
    "Optical Power Flow": "OPF",
    "Sorting & Ranking": "Sort&Rank",
    "Facility Location Problem": "FLP",
    "Portfolio Optimization": "PortOpt",
    "Mixed Integer Programming": "MIP",
}

PROBLEM_CATEGORY_ORDER = (
    "Job Shop Scheduling Problem",
    "Flow Shop Problem",
    "Sorting & Ranking",
    "Graph Matching",
    "Quadratic Assignment Problem",
    "Travelling Salesman Problem",
    "Portfolio Optimization",
    "Maximal Cut",
    "Vehicle Routing Problem",
    "Maximum Independent Set",
    "Generalization",
    "Orienteering Problem",
    "Knapsack",
    "Boolean Satisfiability",
    "Computing Resource Allocation",
    "Bin Packing Problem",
    "Graph Edit Distance",
    "Hamiltonian Cycle Problem",
    "Graph Coloring",
    "Maximal Common Subgraph",
    "Influence Maximization",
    "Max Clique",
    "Mixed Integer Programming",
    "Causal Discovery",
    "Game Theoretic Semantics",
    "Differentiable Optimization",
    "Car Dispatch",
    "Electronic Design Automation",
    "Conjunctive Query Containment",
    "Virtual Network Embedding",
    "Predict+Optimize",
    "Optimal Power Flow",
    "Facility Location Problem",
    "Combinatorial Drug Recommendation",
    "Stochastic Combinatorial Optimization",
    "Vertex Cover",
)


def _pad_row(row, width=8):
    r = list(row)
    while len(r) < width:
        r.append("")
    return r


def _norm_link(link: str) -> str:
    if not link:
        return ""
    try:
        p = urlparse(link.strip())
        return f"{p.scheme}://{p.netloc}{p.path}".rstrip("/").lower()
    except Exception:
        return link.strip().lower()


def _year_desc_key(paper: list) -> tuple:
    """Newest year first; same year ordered by title; bad/missing year last."""
    y_raw = (paper[3] or "").strip()
    try:
        yi = int(y_raw)
    except ValueError:
        yi = -1
    return (yi, paper[1].strip().lower())


def _slug_anchor(name: str) -> str:
    return name.replace(" ", "-").lower()


def _shield_static(
    label: str,
    message: str,
    color: str,
    *,
    logo: str | None = None,
    logo_color: str = "white",
) -> str:
    """Shields.io static/v1 URL (works well with spaces in label/message)."""
    parts = [
        f"label={quote(label)}",
        f"message={quote(str(message))}",
        f"color={quote(color)}",
        "style=for-the-badge",
    ]
    if logo:
        parts.append(f"logo={quote(logo)}")
        parts.append(f"logoColor={quote(logo_color)}")
    return "https://img.shields.io/static/v1?" + "&".join(parts)


def _typing_svg_url(lines: list[str]) -> str:
    """Animated rotating lines (renders as SVG on GitHub). Uses readme-typing-svg.demolab.com."""
    # API expects semicolon-separated phrases; use + for spaces (not %20).
    enc = ";".join(line.strip().replace(" ", "+") for line in lines if line.strip())
    return (
        "https://readme-typing-svg.demolab.com/?"
        f"lines={enc}"
        "&font=JetBrains+Mono&weight=600&size=22"
        "&duration=2800&pause=900"
        "&color=22D3EE&center=true&vCenter=true&width=640&height=55"
        "&repeat=true"
    )


def _write_at_a_glance(
    file,
    *,
    n_total: int,
    n_llm: int,
    survey_n: int,
    n_categories: int,
    n_with_code: int,
) -> None:
    """Centered typing animation + Shields badges + compact legend."""
    typing_lines = [
        "Learning4CO",
        f"{n_total} curated rows",
        f"{n_llm} LLM for CO",
        f"{survey_n} survey papers",
        f"{n_categories} problem areas",
        f"{n_with_code} with code links",
    ]
    file.write("### At a glance\n\n")
    file.write('<p align="center">\n')
    file.write(
        f'  <img src="{_typing_svg_url(typing_lines)}" alt="Learning4CO stats carousel" />\n'
    )
    file.write("</p>\n\n")
    badges: list[tuple[str, str, str, str | None]] = [
        ("Entries", str(n_total), "0f766e", "bookstack"),
        ("LLM for CO", str(n_llm), "6d28d9", "openai"),
        ("Surveys", str(survey_n), "1d4ed8", "readthedocs"),
        ("Problem areas", str(n_categories), "475569", None),
        ("With code", str(n_with_code), "15803d", "github"),
    ]
    mid = (len(badges) + 1) // 2
    for row in (badges[:mid], badges[mid:]):
        file.write('<p align="center">\n')
        for label, msg, color, logo in row:
            url = (
                _shield_static(label, msg, color, logo=logo)
                if logo
                else _shield_static(label, msg, color)
            )
            file.write(f'  <img src="{url}" alt="{label}: {msg}" />\n  &nbsp;\n')
        file.write("</p>\n\n")

    file.write('<p align="center">\n')
    file.write(
        f'  <img src="{_shield_static("README", "Markdown", "111827", logo="markdown")}" alt="README" />\n  &nbsp;\n'
    )
    file.write(
        f'  <img src="{_shield_static("Generator", "Python 3", "1e3a5f", logo="python", logo_color="ffdd54")}" alt="Python" />\n'
    )
    file.write("</p>\n\n")

    if GITHUB_REPO_SLUG:
        slug = GITHUB_REPO_SLUG.strip()
        if slug and "/" in slug:
            file.write('<p align="center">\n')
            stars = f"https://img.shields.io/github/stars/{slug}?style=for-the-badge&logo=github&label=Stars&color=181717"
            forks = f"https://img.shields.io/github/forks/{slug}?style=for-the-badge&logo=github&label=Forks&color=181717"
            file.write(f'  <a href="https://github.com/{slug}"><img src="{stars}" alt="GitHub stars" /></a>\n  &nbsp;\n')
            file.write(f'  <a href="https://github.com/{slug}"><img src="{forks}" alt="GitHub forks" /></a>\n')
            file.write("</p>\n\n")

    file.write("<details>\n<summary><strong>What these numbers mean</strong></summary>\n\n")
    file.write(
        "| Metric | Meaning |\n"
        "|--------|--------|\n"
        f"| **Entries** | Rows in `data/papers.csv` (one row can map to several problem sections). |\n"
        f"| **LLM for CO** | Rows with `llm_for_co` set — listed in the top LLM block. |\n"
        f"| **Surveys** | Papers under **Survey Papers**. |\n"
        f"| **Problem areas** | Distinct problem categories in the TOC. |\n"
        f"| **With code** | Rows that include a repository URL in the `code` column. |\n\n"
    )
    file.write("</details>\n\n")
    file.write(
        "> **Tip:** Jump with the **Navigate** table below, or search the page "
        "(`Ctrl+F` / `Cmd+F`) by venue, author, or keyword.\n\n"
    )


def _write_paper_entry(file, num: int, paper: list[str]) -> None:
    """One bibliography line + optional indented authors; compact vertical spacing."""
    if paper[6] == "":
        line = "{}. **{}** {}, {}. [{}]({})".format(
            num, paper[1], paper[2], paper[3], "paper", paper[4]
        )
    else:
        line = "{}. **{}** {}, {}. [{}]({}), [code]({})".format(
            num,
            paper[1],
            paper[2],
            paper[3],
            "paper",
            paper[4],
            paper[6],
        )
    file.write(line + "\n")
    if paper[5]:
        file.write("    *{}*\n".format(paper[5]))
    file.write("\n")


def csv2md(csv_path, md_path, header_path):
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        raise SystemExit("Empty CSV")
    raw_papers = [_pad_row(r) for r in rows[1:] if any(c.strip() for c in r)]

    discovered = set()
    for paper in raw_papers:
        cats = paper[0]
        if ";" in cats:
            for cls in cats.split(";"):
                discovered.add(cls.strip())
        else:
            discovered.add(cats.strip())

    problem_classes = [c for c in PROBLEM_CATEGORY_ORDER if c in discovered]
    unknown = discovered - {"Survey Papers"} - set(PROBLEM_CATEGORY_ORDER)
    for c in sorted(unknown):
        problem_classes.append(c)

    content_order = []
    if "Survey Papers" in discovered:
        content_order.append("Survey Papers")
    content_order.extend(problem_classes)

    papers = []
    for c in content_order:
        block = []
        for paper in raw_papers:
            if c in paper[0]:
                np = copy.deepcopy(paper)
                np[0] = c
                block.append(np)
        block.sort(key=_year_desc_key, reverse=True)
        papers.extend(block)

    # LLM section: non-empty llm_for_co (e.g. "1" or "yes"), dedupe by link then title+year
    llm_list = []
    seen = set()
    for paper in raw_papers:
        flag = (paper[7] or "").strip().lower()
        if flag in ("", "0", "no", "false"):
            continue
        key = _norm_link(paper[4]) or f"{paper[1].strip().lower()}|{paper[3].strip()}"
        if key in seen:
            continue
        seen.add(key)
        llm_list.append(copy.deepcopy(paper))
    llm_list.sort(key=_year_desc_key, reverse=True)

    section_counts: Counter[str] = Counter(p[0] for p in papers)
    n_with_code = sum(1 for p in raw_papers if (p[6] or "").strip())
    n_total = len(raw_papers)

    header_text = Path(header_path).read_text(encoding="utf-8").strip()

    with open(md_path, "w", encoding="utf-8") as file:
        file.write(header_text)
        file.write("\n\n")
        survey_n = section_counts.get("Survey Papers", 0)
        _write_at_a_glance(
            file,
            n_total=n_total,
            n_llm=len(llm_list),
            survey_n=survey_n,
            n_categories=len(problem_classes),
            n_with_code=n_with_code,
        )
        file.write("```mermaid\n")
        file.write("flowchart LR\n")
        file.write("  A[LLM for CO] --> L[Curated links]\n")
        file.write("  B[Surveys] --> L\n")
        file.write("  C[By problem] --> L\n")
        file.write("```\n\n")
        file.write(
            "*LLM* entries also appear again under **Problems** when their `category` matches. "
            "*Surveys* are cross-cutting; *By problem* follows classic CO domains.\n\n"
        )
        file.write("---\n\n")
        file.write("## [Content](#content)\n\n")
        file.write('<table>\n<thead>\n<tr><th colspan="2">Navigate</th></tr>\n</thead>\n<tbody>\n')
        file.write(
            '<tr><td colspan="2" align="center">'
            '<a href="#llm-for-combinatorial-optimization"><strong>1 · LLM for CO</strong></a> · '
            '<a href="#survey-papers"><strong>2 · Surveys</strong></a> · '
            '<a href="#problems"><strong>3 · Problems</strong></a>'
            "</td></tr>\n"
        )
        for i in range((len(problem_classes) + 1) // 2):
            name1 = problem_classes[2 * i]
            num1 = 2 * i + 1
            name_index1 = _slug_anchor(name1)
            file.write("<tr>\n")
            if name1 in abbr:
                file.write(
                    "\t<td>&emsp;<a href=#{}>3.{} {} ({})</a></td>\n".format(
                        name_index1, num1, name1, abbr[name1]
                    )
                )
            else:
                file.write(
                    "\t<td>&emsp;<a href=#{}>3.{} {}</a></td>\n".format(
                        name_index1, num1, name1
                    )
                )
            if 2 * i + 1 < len(problem_classes):
                name2 = problem_classes[2 * i + 1]
                num2 = 2 * i + 2
                name_index2 = _slug_anchor(name2)
                if name2 in abbr:
                    file.write(
                        "\t<td>&emsp;<a href=#{}>3.{} {} ({})</a></td>\n".format(
                            name_index2, num2, name2, abbr[name2]
                        )
                    )
                else:
                    file.write(
                        "\t<td>&emsp;<a href=#{}>3.{} {}</a></td>\n".format(
                            name_index2, num2, name2
                        )
                    )
            else:
                file.write("<td>&ensp;</td>\n")
            file.write("</tr>\n")
        file.write("</tbody>\n</table>\n\n")
        file.write("---\n\n")

        # --- 1. LLM for Combinatorial Optimization ---
        file.write("### [LLM for Combinatorial Optimization](#content)")
        if llm_list:
            file.write(f" · *{len(llm_list)} papers*")
        file.write("\n\n")
        file.write(
            "Papers where **large language models** (or closely related agents / prompts / "
            "automatic heuristic design with LLMs) are central. "
            "These entries are also listed under **Problems** when they match a problem category. "
            "Tag rows in `papers.csv` with `llm_for_co` = `1` to include a paper here.\n\n"
        )
        if not llm_list:
            file.write("*No rows tagged yet — set column `llm_for_co` to `1` in `data/papers.csv`.*\n\n")
        else:
            num = 0
            for paper in llm_list:
                paper = [p.strip() for p in paper]
                num += 1
                _write_paper_entry(file, num, paper)

        # --- 2. Survey + 3. Problems (existing flow) ---
        category = None
        num = 0
        for paper in papers:
            paper = [p.strip() for p in paper]
            if category is None:
                category = paper[0]
                cnt = section_counts.get(category, 0)
                file.write("### [{}](#content) · *{} papers*\n\n".format(category, cnt))
            elif paper[0] != category:
                if category == "Survey Papers":
                    file.write("---\n\n## [Problems](#content)\n\n")
                category = paper[0]
                cnt = section_counts.get(category, 0)
                file.write("### [{}](#content) · *{} papers*\n\n".format(category, cnt))
                num = 0
            num += 1
            _write_paper_entry(file, num, paper)


if __name__ == "__main__":
    import os

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv2md(
        os.path.join(root, "data", "papers.csv"),
        os.path.join(root, "README.md"),
        os.path.join(root, "data", "header.md"),
    )
    print("Wrote README.md")
