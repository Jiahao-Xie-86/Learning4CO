"""
Build README.md from data/papers.csv.
Section order: (1) LLM for CO — rows with non-empty llm_for_co;
               (2) Survey Papers;
               (3) Problems — same ordering as awesome-ml4co PROBLEM_CATEGORY_ORDER.
"""
import copy
import csv
import shutil
from urllib.parse import urlparse

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


def _pad_row(row, width=10):
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


def sort_by_year(elem):
    return elem[3]


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
        block.sort(key=sort_by_year)
        papers.extend(block)

    # LLM section: non-empty llm_for_co (e.g. "1" or "yes"), dedupe by link then title+year
    llm_list = []
    seen = set()
    for paper in raw_papers:
        flag = (paper[8] or "").strip().lower()
        if flag in ("", "0", "no", "false"):
            continue
        key = _norm_link(paper[5]) or f"{paper[1].strip().lower()}|{paper[3].strip()}"
        if key in seen:
            continue
        seen.add(key)
        llm_list.append(copy.deepcopy(paper))
    llm_list.sort(key=sort_by_year)

    shutil.copy(header_path, md_path)
    with open(md_path, "a", encoding="utf-8") as file:
        for i in range((len(problem_classes) + 1) // 2):
            name1 = problem_classes[2 * i]
            num1 = 2 * i + 1
            name_index1 = name1.replace(" ", "-").lower()
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
                name_index2 = name2.replace(" ", "-").lower()
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
        file.write("</table>\n\n")

        # --- 1. LLM for Combinatorial Optimization ---
        file.write("### [LLM for Combinatorial Optimization](#content)\n\n")
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
                note = (paper[9] or "").strip()
                suffix = f" *({note})*" if note else ""
                if paper[7] == "":
                    line = "{}. **{}** {}, {}. [{}]({}){}".format(
                        num, paper[1], paper[2], paper[3], paper[4], paper[5], suffix
                    )
                else:
                    line = "{}. **{}** {}, {}. [{}]({}), [code]({}){}".format(
                        num,
                        paper[1],
                        paper[2],
                        paper[3],
                        paper[4],
                        paper[5],
                        paper[7],
                        suffix,
                    )
                file.write(line + "\n\n")
                file.write("    *{}*\n\n".format(paper[6]))

        # --- 2. Survey + 3. Problems (existing flow) ---
        category = None
        num = 0
        for paper in papers:
            paper = [p.strip() for p in paper]
            if category is None:
                category = paper[0]
                file.write("### [{}](#content)\n\n".format(category))
            elif paper[0] != category:
                if category == "Survey Papers":
                    file.write("## [Problems](#content)\n\n")
                category = paper[0]
                file.write("### [{}](#content)\n\n".format(category))
                num = 0
            num += 1
            if paper[7] == "":
                file.write(
                    "{}. **{}** {}, {}. [{}]({})".format(
                        num, paper[1], paper[2], paper[3], paper[4], paper[5]
                    )
                )
            else:
                file.write(
                    "{}. **{}** {}, {}. [{}]({}), [code]({})".format(
                        num,
                        paper[1],
                        paper[2],
                        paper[3],
                        paper[4],
                        paper[5],
                        paper[7],
                    )
                )
            file.write("\n\n")
            file.write("    *{}*\n\n".format(paper[6]))


if __name__ == "__main__":
    import os

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv2md(
        os.path.join(root, "data", "papers.csv"),
        os.path.join(root, "README.md"),
        os.path.join(root, "data", "header.md"),
    )
    print("Wrote README.md")
