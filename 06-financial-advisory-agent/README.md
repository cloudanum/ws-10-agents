# Agent 6 — The Financial Advisory Agent

**Book:** *30 Agents Every AI Engineer Must Build* — Imran Ahmad (Packt Publishing, 2026)
**Reference:** Chapter 14, Section 14.1 (pp. 392–408), Financial Advisory Agent
(Section 14.2, the Legal Intelligence Agent, is not covered here.)

## What this agent does

RetailAdvisor is a supervised multi-agent system for retail financial advice.
A Supervisor Agent routes client queries through a LangGraph `StateGraph` to
three specialists — Market Data (yfinance/Finnhub), Financial Analysis
(Finnhub metrics), and News (Tavily search). A risk framework computes a
composite score (0.4 × volatility + 0.35 × drawdown + 0.25 × VaR), adjusted
for the client's stated tolerance. A planning layer then generates a
portfolio allocation that must pass a structural compliance gate
(suitability + 25% concentration limit) before delivery — non-compliant
recommendations are revised and re-validated in a loop. A risk profile goes
in; a tailored, compliance-validated portfolio recommendation comes out.

## How to run

    pip install -r requirements.txt
    jupyter notebook 06_financial_advisory_agent.ipynb

Simulation Mode (MockLLM + chapter-faithful mock data) is the default and
needs no API keys. For live mode, `cp ../.env.template .env` from the
workshop root, set your keys, and choose a provider with `LLM_PROVIDER`
(openai | anthropic | google). Each service (OpenAI, Finnhub, Tavily) falls
back to simulation independently when its key is absent.

## Files

- `06_financial_advisory_agent.ipynb` — self-contained workshop notebook
- `mock_llm.py` — resilience layer, color-coded logging, service config, mock LLM/chain for Simulation Mode
- `mock_data.py` — chapter-faithful synthetic market, news, and client data
- `requirements.txt` — pinned dependencies

## Disclaimer

Educational demonstration only — outputs are illustrative, not investment advice.
