# Workshop Agent 1: The Tool-Using Agent

**Book:** *30 Agents Every AI Engineer Must Build* by Imran Ahmad (Packt Publishing, 2026)
**Reference:** Chapter 7 — Tool Manipulation and Orchestration Agents, Sections 7.1–7.3 (pp. 174–186)

## What This Agent Does

An LLM that reasons about a request, selects the right tool from a registry, and
executes it through a function-calling loop — the foundational pattern every later
agent in this workshop is built on. Working from a natural-language question about an
ad-campaign dataset, the agent runs the full **Think/Plan/Act** cycle: `parse_query`
classifies intent (§7.2), a plan of tool calls is constructed, and guarded tools from
the `TOOL_REGISTRY` (§7.1) execute in sequence. You see the agent pick a tool live and
return a structured result, with color-coded log output and charts saved to `outputs/`.
Deliberate failure demos (missing file, column mismatch) show the `@graceful_fallback`
resilience layer of §7.3 in action.

## How to Run

```bash
# 1. Create a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the notebook — Simulation Mode is the default, no API key needed
jupyter notebook 01_tool_using_agent.ipynb
```

**Live Mode (optional):** `cp ../.env.template .env`, set your API key and
`LLM_PROVIDER` (openai | anthropic | google | auto), and uncomment the matching
provider package in `requirements.txt`. Without a key, every cell still runs to
completion using chapter-derived mock responses.

## Files

```
01-tool-using-agent/
├── 01_tool_using_agent.ipynb   # Self-contained notebook (Sections 0–3 of Chapter 7)
├── requirements.txt            # Dependencies (Simulation Mode needs no API key)
├── README.md                   # This file
├── helpers/                    # Shared infrastructure (Chapter 7)
│   ├── __init__.py             # Package exports
│   ├── color_logger.py         # Color-coded logging (INFO/SUCCESS/ERROR/WARNING/MOCK)
│   ├── resilience.py           # @graceful_fallback decorator, safe_invoke()
│   └── mock_llm.py             # Context-aware MockLLM for Simulation Mode
└── data/
    └── sample_ad_campaign.csv  # Synthetic ad-campaign dataset (24 rows, 5 columns)
```
