# Workshop Agent 8: The Education Intelligence Agent

An adaptive programming tutor that tracks student progress and tailors its
feedback to each learner: the tutor maintains an evolving model of the
student's knowledge state, and when a learner stumbles it diagnoses the gap
and adjusts its next explanation.

**Book reference:** *30 Agents Every AI Engineer Must Build* (Packt
Publishing, 2026), Chapter 15 — Education and Knowledge Agents, §15.1
(Part I, pp. 421–441).

## What the notebook covers

- **Knowledge-graph curriculum** — DAG of objectives with prerequisite gating and ZPD-aligned ranking.
- **Adaptive placement test** — 2PL IRT item selection; solves the cold-start problem in 5–15 items.
- **Bayesian Knowledge Tracing** — two-step posterior + learning-transition mastery updates.
- **Spaced repetition** — modified SM-2 scheduling driven by recall quality.
- **Feedback generator** — two-stage misconception detection (rule-based, then LLM fallback).
- **Case study** — "Alex" end-to-end walkthrough of all components together.

## Running the notebook

```bash
pip install -r requirements.txt
jupyter notebook 08_education_intelligence_agent.ipynb
```

**Simulation Mode is the default** — with no API key, all LLM calls route
through `MockLLM` and return pre-authored, section-mapped responses. For
**Live Mode**: `cp ../.env.template .env`, then set `OPENAI_API_KEY` and
`LLM_PROVIDER` in `.env`.

## Files

- `08_education_intelligence_agent.ipynb` — self-contained workshop notebook (pre-run in Simulation Mode)
- `mock_llm.py` — MockLLM class + section-mapped response registry
- `resilience.py` — ColorLogger + `@graceful_fallback` decorator
- `requirements.txt` — pinned dependencies
