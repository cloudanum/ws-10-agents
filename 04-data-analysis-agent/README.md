# Workshop Agent 4 — The Data Analysis Agent

**Book:** *Agents* by Imran Ahmad (Packt Publishing, 2026)
**Chapter Ref:** Chapter 8 — Data Analysis and Reasoning Agents, §8.1–§8.1.2 (pp. 204–211)

## What it does

The Data Analysis Agent turns a plain-English question into code, runs it over
a dataset, and recommends the right visualization — a natural-language question
becomes a live chart plus a statistical readout in seconds. In this notebook you
build its four-stage cognitive loop step by step:

1. **Visualization recommendation** (§8.1.1) — rule-based intent matching maps
   queries to line, bar, scatter, or table outputs.
2. **Descriptive statistics** (§8.1.2) — summary statistics, variability, and
   Pearson correlations over the sample sales dataset.
3. **OLS regression** (§8.1.2) — quantifies the marketing_spend → revenue
   relationship with R², coefficients, and p-values.
4. **Anomaly detection + LLM interpretation** (§8.1.2) — z-score outlier
   flagging, narrated in plain business language via `llm_call()`.

## How to run

```bash
pip install -r requirements.txt
jupyter notebook 04_data_analysis_agent.ipynb
```

**Simulation Mode is the default** — with no API key the notebook runs
end-to-end on chapter-accurate `MockLLM` responses. No key is required.

For **live mode**, copy the workshop template and set a key plus provider:

```bash
cp ../.env.template .env
# edit .env: set OPENAI_API_KEY (or ANTHROPIC_API_KEY / GOOGLE_API_KEY)
# and LLM_PROVIDER=openai | anthropic | google | auto
```

## Files

| File | Purpose |
|:-----|:--------|
| `04_data_analysis_agent.ipynb` | Self-contained workshop notebook (Sections 0, 1, 1.1, 1.2) |
| `utils.py` | Re-export module for notebook imports |
| `config.py` | Three-tier API key resolution (.env → env var → prompt) |
| `color_logger.py` | Color-coded logging (Blue/Green/Red) |
| `mock_llm.py` | MockLLM, mock registry, `llm_call()`, `@fail_gracefully` |
| `data/sample_sales_data.csv` | Synthetic sales dataset (100 rows, seed=42) |
| `requirements.txt` | Pinned dependencies |
