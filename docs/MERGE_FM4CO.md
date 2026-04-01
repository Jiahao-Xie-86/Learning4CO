# Notes on merging [awesome-fm4co](https://github.com/ai4co/awesome-fm4co)

The FM4CO README uses markdown tables with shorthand problem tags (`TSP`, `MILP`, `VRP`, …). This repo uses **full category names** aligned with awesome-ml4co, for example:

| FM4CO-style tag | Typical `category` here |
|-----------------|-------------------------|
| TSP, mTSP | Travelling Salesman Problem |
| VRP, CVRP, … | Vehicle Routing Problem |
| MILP, MIP | Mixed Integer Programming |
| JSSP, FJSP, DyJSSP | Job Shop Scheduling Problem |
| BPP, OBP | Bin Packing Problem |
| SAT, PBO | Boolean Satisfiability |
| General COP / OR | pick closest problem or Multiple categories with `; ` |

For rows that are **only** about LLM modeling or benchmarks without a single CO problem, you can still assign the closest problem tag and set `llm_for_co=1` so they appear in section 1.
