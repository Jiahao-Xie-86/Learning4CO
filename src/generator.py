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
    style: str = "flat-square",
) -> str:
    """Shields.io static/v1 URL (works well with spaces in label/message)."""
    parts = [
        f"label={quote(label)}",
        f"message={quote(str(message))}",
        f"color={quote(color)}",
        f"style={quote(style)}",
    ]
    if logo:
        parts.append(f"logo={quote(logo)}")
        parts.append(f"logoColor={quote(logo_color)}")
    return "https://img.shields.io/static/v1?" + "&".join(parts)


def _write_stat_badges(
    file,
    *,
    n_papers: int,
    n_llm: int,
    survey_n: int,
    n_categories: int,
    n_with_code: int,
) -> None:
    """Centered flat Shields row; counts use plain 'papers' wording (no 'indexed')."""
    file.write('<div align="center">\n\n')
    badges: list[tuple[str, str, str, str | None]] = [
        ("Papers", str(n_papers), "4f46e5", "bookstack"),
        ("LLM for CO", str(n_llm), "7c3aed", "openai"),
        ("Surveys", str(survey_n), "0e7490", "readthedocs"),
        ("Categories", str(n_categories), "475569", None),
        ("With code", str(n_with_code), "059669", "github"),
    ]
    file.write('<p dir="auto">\n')
    for label, msg, color, logo in badges:
        url = (
            _shield_static(label, msg, color, logo=logo, style="flat-square")
            if logo
            else _shield_static(label, msg, color, style="flat-square")
        )
        file.write(f'  <img src="{url}" alt="{label}: {msg}" />\n')
    file.write("</p>\n\n")

    if GITHUB_REPO_SLUG:
        slug = GITHUB_REPO_SLUG.strip()
        if slug and "/" in slug:
            stars = f"https://img.shields.io/github/stars/{slug}?style=flat-square&logo=github&label=stars&color=181717"
            forks = f"https://img.shields.io/github/forks/{slug}?style=flat-square&logo=github&label=forks&color=181717"
            file.write(
                f'<p dir="auto">\n'
                f'  <a href="https://github.com/{slug}"><img src="{stars}" alt="GitHub stars" /></a>\n'
                f'  <a href="https://github.com/{slug}"><img src="{forks}" alt="GitHub forks" /></a>\n'
                f"</p>\n\n"
            )

    file.write("</div>\n\n")


def _write_paper_entry(file, num: int, paper: list[str]) -> None:
    """One bibliography line (title, venue, year, links); authors omitted for a uniform list."""
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
    file.write(line + "\n\n")


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
        _write_stat_badges(
            file,
            n_papers=n_total,
            n_llm=len(llm_list),
            survey_n=survey_n,
            n_categories=len(problem_classes),
            n_with_code=n_with_code,
        )
        file.write("---\n\n")
        file.write("## [Content](#content)\n\n")
        file.write("### Navigate\n\n")
        file.write(
            '<table>\n'
            "<thead>\n"
            '<tr><th align="left">Three tracks — pick where to start</th></tr>\n'
            "</thead>\n"
            "<tbody>\n"
            '<tr><td valign="top"><a href="#llm-for-combinatorial-optimization"><strong>① LLM for CO</strong></a><br />\n'
            "LLMs, agents &amp; tool use for combinatorial optimization</td></tr>\n"
            '<tr><td valign="top"><a href="#survey-papers"><strong>② Surveys</strong></a><br />\n'
            "Broad reviews &amp; methodology surveys</td></tr>\n"
            '<tr><td valign="top"><a href="#problems"><strong>③ Problems</strong></a><br />\n'
            "Papers by <strong>problem type</strong> (TSP, MIP, SAT, …)</td></tr>\n"
            "</tbody>\n"
            "</table>\n\n"
        )
        file.write("---\n\n")
        file.write("#### Problem categories\n\n")
        file.write(
            '<table>\n<thead>\n<tr><th colspan="2" align="center">Quick links by domain</th></tr>\n</thead>\n<tbody>\n'
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
            "Papers on **LLM for combinatorial optimization** — work where large language models "
            "(or closely related agents and tool use) are central to CO.\n\n"
        )
        if not llm_list:
            file.write("*No papers in this section yet.*\n\n")
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
