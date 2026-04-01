"""
One-shot: copy papers from sibling awesome-ml4co and add llm_for_co / llm_note columns.
Heuristic tagging for llm_for_co=1 (edit CSV to fix false positives/negatives).
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GITHUB = ROOT.parent
SRC = GITHUB / "awesome-ml4co" / "data" / "papers.csv"
OUT = ROOT / "data" / "papers.csv"

# Title substrings (lowercase) -> likely LLM-for-CO
LLM_HINTS = [
    r"\bllm\b",
    r"large language model",
    r"language models as",
    r"language model as",
    r"\bgpt\b",
    r"prompt engineering",
    r"text prompt",
    r"reevo\b",
    r"\beoh\b",
    r"evolution of heuristic",
    r"automatic heuristic design",
    r"meta-optimization",
    r"hyper-heuristic",
    r"chain-of-expert",
    r"optimus\b",
    r"\borlm\b",
    r"optibench",
    r"resocratic",
    r"g-lns\b",
    r"generative large neighborhood",
    r"vision language model",
    r"\bvitsp\b",
    r"agentic framework",
    r"llm-driven",
    r"llm-based",
    r"llms for",
    r"with llms",
    r"using llms",
    r"via llms",
    r"llm ",
    r"opro\b",
    r"funsearch",
    r"nlgraph",
    r"algorithm evolution using large language",
    r"can language models",
    r"llms can schedule",
    r"self-guiding exploration",
    r"monte carlo tree search.*llm",
    r"mcts.*heuristic",
    r"planning of heuristics",
    r"graphthought",
    r"grapharena",
    r"equivalamap",
    r"or-llm",
    r"comb-opt-for-all",
    r"co-bench: benchmarking language model agents",
    r"orqa\b",
    r"solver-informed",
    r"ormind\b",
    r"optitree",
    r"hercules\b",
    r"calm: co-evolution",
    r"redahd",
    r"llm4solver",
    r"llmopt",
    r"starjob",
    r"droc\b",
    r"dr oc",
    r"multimodal integration boost",
    r"routing solver with large language",
    r"automatic programming via large language",
    r"diagnosing infeasible optimization problems using large language",
    r"generalizable heuristic generation through",
    r"end-to-end combinatorial optimization solvers",
    r"llmcosolver",
    r"large language model-driven",
    r"decomposition and reconstruction agents",
    r"\bdragon:",
    r"evo real",
    r"llm-guided instance",
    r"heuristic set using llms",
    r"\beoh-s\b",
    r"an agentic framework with llms",
    r"refining hybrid genetic search.*llm",
    r"rfthgs",
    r"generative.*llm",
    r"llm .* vehicle routing",
    r"foundation model.*mixed integer",
]


def tag_llm(title: str) -> bool:
    t = title.lower()
    if "llm" in t or "large language model" in t or "language models" in t:
        return True
    return any(re.search(p, t) for p in LLM_HINTS)


def main():
    if not SRC.exists():
        print("Source not found:", SRC, file=sys.stderr)
        sys.exit(1)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with SRC.open(encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        sys.exit("empty source")
    header = rows[0]
    # strip trailing empty cols from header
    while header and header[-1] == "":
        header.pop()
    new_header = header[:8] + ["llm_for_co", "llm_note"]
    out_rows = [new_header]
    tagged = 0
    for row in rows[1:]:
        while len(row) < 8:
            row.append("")
        row = row[:8]
        title = row[1] if len(row) > 1 else ""
        if tag_llm(title):
            row.append("1")
            row.append("")
            tagged += 1
        else:
            row.append("")
            row.append("")
        out_rows.append(row)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(out_rows)
    print(f"Wrote {OUT} with {len(out_rows) - 1} papers; llm_for_co=1 on {tagged} rows (heuristic).")


if __name__ == "__main__":
    main()
