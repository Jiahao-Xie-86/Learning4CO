# Contributing

## Add or edit a paper

1. Edit `data/papers.csv` (UTF-8). Columns:

   | Column | Description |
   |--------|-------------|
   | `category` | One or more problem names, separated by `; ` (semicolon + space). Use the same names as existing rows. |
   | `title` | Full paper title. |
   | `publisher` | Venue or journal (e.g. `ICLR`, `NeurIPS`, `Arxiv`). |
   | `year` | Four-digit year. |
   | `type` | e.g. `paper`, `journal`. |
   | `link` | Canonical URL (arXiv, OpenReview, DOI, etc.). |
   | `authors` | Comma-separated names. |
   | `code` | Repository URL, or leave empty. |
   | `llm_for_co` | Set to `1` (or `yes`) to also list the paper in **§1 LLM for Combinatorial Optimization** at the top of the README. Leave empty for neural-only / non-LLM work. |
   | `llm_note` | Optional short tag shown next to the entry in the LLM section (e.g. `Algorithm`, `Formulation`). |

2. Regenerate the README:

   ```bash
   cd src
   python generator.py
   ```

3. Open a PR with both `data/papers.csv` and `README.md` updated.

## Merging entries from [awesome-fm4co](https://github.com/ai4co/awesome-fm4co)

Add new rows manually: map the **Problem** column to one or more of our `category` values, set `llm_for_co` to `1` for the LLM table, and fill `link` / `code` from the FM4CO row. Prefer deduplicating against existing rows (same arXiv ID or OpenReview forum).

## Re-importing from Thinklab awesome-ml4co

If you keep a clone of `awesome-ml4co` next to this repo, you can refresh the base CSV (overwrites `llm_for_co` heuristics):

```bash
python scripts/bootstrap_from_ml4co.py
```

Then re-tune `llm_for_co` / `llm_note` for your taste and run `python src/generator.py`.
