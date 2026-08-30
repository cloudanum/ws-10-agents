# Workshop Agent 5 — The Verification / Fact-Checking Agent

A journalism-grade agent that extracts claims from a news statement, retrieves
evidence against authoritative data, and reasons about conflicting evidence.
Each claim is returned with a verdict — `Confirmed`, `Mostly True`,
`Contradicted`, or `Unverified` — together with its supporting evidence and
source provenance.

**Book reference:** *Agents* by Imran Ahmad (Packt, 2026), Chapter 8 —
*Data Analysis and Reasoning Agents*: §8.2 The Verification and Validation
Agent (pp. 211–215, including the §8.2.5 NLI demo) and §8.4 Case Study:
News Fact-Checking Assistant (pp. 220–226).

## What the notebook covers

1. **Section 0 — Environment Setup** — three-tier API key resolution and
   Simulation Mode detection.
2. **Section 2 — The Verification and Validation Agent (§8.2)** — theory of
   fact-checking, logical coherence, retrieval-augmented evaluation, and
   consistency analysis, plus the §8.2.5 NLI demo (BART-MNLI) for handling
   conflicting evidence. Without `transformers`/`torch`, the demo falls back
   to chapter-accurate precomputed scores.
3. **Section 4 — News Fact-Checking Assistant (§8.4)** — Claim Extractor
   (LLM-first with regex fallback), Evidence Retriever over a trusted
   database, and a tolerance-based Verifier producing an editorial report.

## How to run

```bash
pip install -r requirements.txt
jupyter notebook 05_verification_fact_checking_agent.ipynb
```

**Simulation Mode (default):** no API key is needed. All LLM calls use
deterministic, chapter-accurate mock responses; the notebook runs fully
offline.

**Live mode:** copy the template and set a key plus provider:

```bash
cp ../.env.template .env
# edit .env: set OPENAI_API_KEY (or ANTHROPIC/GOOGLE key) and LLM_PROVIDER
```

## Files

| File | Purpose |
|:-----|:--------|
| `05_verification_fact_checking_agent.ipynb` | Self-contained workshop notebook (pre-run) |
| `utils.py` | Re-export module for the notebook imports |
| `config.py` | Three-tier API key resolution (`.env` → env var → prompt) |
| `color_logger.py` | ANSI color-coded logging (Blue/Green/Red) |
| `mock_llm.py` | MockLLM, mock registry, `llm_call()`, `@fail_gracefully` |
| `requirements.txt` | Pinned dependencies (torch/transformers optional, commented) |
