# Contributing to Learning4CO

Thank you for helping extend the list. **Do not edit `README.md` by hand** — it is produced by `src/generator.py` from `data/papers.csv` (and `data/header.md` for the intro).

---

## Add a paper (short version)

1. Edit **`data/papers.csv`** in **UTF-8** (use a spreadsheet or editor that preserves CSV quoting when the title has commas or quotes).
2. **Add one row** with the columns below. Set **`category`** to the right problem name(s) or **`Survey Papers`** (see [Where the row shows up](#where-the-row-shows-up)).
3. From the **repository root**, run:
   ```bash
   python src/generator.py
   ```
4. Open a **pull request** that includes **`data/papers.csv`** and the updated **`README.md`**. Include **`data/header.md`** only if you changed the blurb under the title.

---

## Where the row shows up

| What you set | Effect in the generated README |
|--------------|--------------------------------|
| **`category`** | **Survey Papers** → survey block. Any **problem name** (e.g. `Travelling Salesman Problem`) → that subsection under **Problems**. Multiple: `Name A; Name B` (semicolon **and** a space). |
| **`llm_for_co`** = `1` or `yes` | Also listed under **[LLM for CO](README.md#llm-for-co-core)** inside *LLM for Combinatorial Optimization*, **unless** the same row is already listed under **Benchmark papers** (see next row). |
| **`title`** contains **`benchmark`** (any case) | That row is also listed under **[Benchmark papers](README.md#llm-benchmark-papers)** (built from the **whole CSV**, any `category`). It does **not** depend on `llm_for_co`. |

**No duplicate lines between Benchmark and LLM for CO:** if a row qualifies for both, it appears **only** under **Benchmark papers**; it still appears under **Problems** / **Survey Papers** according to `category`.

**`authors`** are optional in the CSV and are **not** rendered in the README.

---

## CSV columns (in order)

| # | Column | Required | Description |
|---|--------|----------|-------------|
| 1 | `category` | yes | `Survey Papers` and/or problem names exactly as in the README or existing rows. Multi-label: `A; B`. |
| 2 | `title` | yes | Full title. Quote the cell if it contains commas. |
| 3 | `publisher` | yes | Short venue (`ICLR`, `NeurIPS`, `Arxiv`, journal abbr., etc.). |
| 4 | `year` | yes | Four-digit year. |
| 5 | `link` | yes | Stable URL (arXiv, OpenReview, DOI, publisher, …). |
| 6 | `authors` | no | Optional; not shown in the README. |
| 7 | `code` | no | Repository URL, or empty. |
| 8 | `llm_for_co` | no | `1` or `yes` only if LLMs (or LLM-centric agents / tool use) are **central** to the method — not for every neural CO paper. |

`llm_for_co` and `category` are **independent**: e.g. a TSP paper can still be tagged for **LLM for CO**.

---

## Categories and naming

- **Surveys** — exact label **`Survey Papers`**.
- **Problems** — copy the **full** heading string from the README **Problems** list or from another row (e.g. `Mixed Integer Programming`, `Boolean Satisfiability`). Spelling and spacing must match.
- **New problem name** — you may add a string that does not exist yet; it will still get a README subsection. For a predictable order in the nav, the name can be added to **`PROBLEM_CATEGORY_ORDER`** in `src/generator.py`; open an issue if you want help with that.

---

## Before you open a PR

- [ ] The **link** opens and matches the paper.
- [ ] **Year** and **publisher** look correct.
- [ ] **`category`** is spelled like existing sections (or you intend a new name).
- [ ] **`llm_for_co`** is set only for genuine **LLM-for-CO** work.
- [ ] `python src/generator.py` completes without errors and **`README.md`** is included in the commit.

---

## Questions

If you are unsure about `category` or `llm_for_co`, open an issue with the **title** and **URL**; a maintainer can suggest the row.
