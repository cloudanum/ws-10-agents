# The Chain-of-Agents Orchestrator

**Workshop Agent 3** — *10 Essential AI Agents Every Engineer Must Build* Workshop
Companion to *30 Agents Every AI Engineer Must Build* by Imran Ahmad (Packt, 2026)

## What This Agent Does

A multi-agent insurance-claims workflow governed by a state machine with
human-in-the-loop escalation. You first build a Chain-of-Agents orchestrator:
a `ManagerAgent` coordinates specialist agents (`NewsAgent`, `FinancialAgent`,
`SentimentAgent`) under a four-pillar Cooperation Protocol, stores their
findings in shared episodic memory, and a `synthesize_report` function detects
disagreement between outputs with a calibrated `conflict_score`. The same
orchestration principles then drive an insurance claims pipeline — intake
(OCR-style field extraction), policy validation, risk classification, and
payout — traced end-to-end on three test claims: auto-approved on the
confident path, escalated to a human reviewer below the confidence threshold,
and rejected at validation, with a full audit trail of every state transition.

## Book Reference

Chapter 7 — Tool Manipulation and Orchestration Agents:
Sections 7.4–7.6 (Chain-of-Agents Orchestrator, episodic memory, conflict
resolution) and Section 7.7b (Insurance Claims Processing state machine).

## How to Run

```bash
pip install -r requirements.txt
jupyter notebook 03_chain_of_agents_orchestrator.ipynb
```

**Simulation Mode (default):** no API key required — all LLM calls return
chapter-derived mock responses via `MockLLM`.

**Live Mode:** `cp ../.env.template .env`, set your API key (and optionally
`LLM_PROVIDER`), then run the notebook as above.

## Files

| File | Purpose |
|:---|:---|
| `03_chain_of_agents_orchestrator.ipynb` | Self-contained workshop notebook (pre-run) |
| `helpers/__init__.py` | Package exports |
| `helpers/color_logger.py` | Color-coded logging for all agent actions |
| `helpers/resilience.py` | `@graceful_fallback` decorator, `safe_invoke()` |
| `helpers/mock_llm.py` | Context-aware `MockLLM` for Simulation Mode |
| `requirements.txt` | Pinned dependencies |
