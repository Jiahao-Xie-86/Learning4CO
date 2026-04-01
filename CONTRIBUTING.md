# Contributing to Learning4CO

## Add or edit a paper

1. Edit `data/papers.csv` (UTF-8). Columns:

   | Column | Description |
   |--------|-------------|
   | `category` | One or more problem names, separated by `; ` (semicolon + space). Use the same names as existing rows. |
   | `title` | Full paper title. |
   | `publisher` | Venue or journal (e.g. `ICLR`, `NeurIPS`, `Arxiv`). |
   | `year` | Four-digit year. |
   | `link` | Canonical URL (arXiv, OpenReview, DOI, etc.). |
   | `authors` | Comma-separated names. |
   | `code` | Repository URL, or leave empty. |
   | `llm_for_co` | Set to `1` (or `yes`) to also list the paper in **§1 LLM for Combinatorial Optimization** at the top of the README. Leave empty for neural-only / non-LLM work. |

2. Regenerate the README:

   ```bash
   python src/generator.py
   ```

3. Commit both `data/papers.csv` and `README.md` (and `data/header.md` if you changed the intro).
