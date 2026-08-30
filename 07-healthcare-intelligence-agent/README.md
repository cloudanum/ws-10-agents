# Workshop Agent 7: The Healthcare Intelligence Agent

A multi-agent diagnostic-assistance system modeled on a real regional
health-network deployment. Patient inputs — vitals, reported symptoms, and
FHIR-normalized history — flow through a four-layer architecture (data
ingestion, clinical knowledge, reasoning and decision, explanation and
delivery) to produce a clinical decision-support output with its clinical
reasoning surfaced: ranked differentials with calibrated confidence, safety
escalation, audience-adapted explanations, and an immutable audit trail.

**Book reference:** *30 Agents Every AI Engineer Must Build* by Imran Ahmad
(Packt Publishing, 2026) — Chapter 13, §13.1–13.4 (pp. 362–375).

## What the notebook covers

- **2a — Bayesian Belief Update** (§13.1): POMDP belief-state update over candidate diagnoses
- **2b — Clinical Knowledge Base** (§13.1): dual-memory integration with provenance tracking
- **2c — FHIR Normalization & Patient Data Pipeline** (§13.2): multi-modal ingestion with temporal alignment
- **2d — Diagnostic Coordinator** (§13.3): full pipeline with Platt-calibrated confidence and 0.15 safety-escalation threshold
- **2e — Case Study** (§13.4): regional health network deployment metrics (200,000 patients, 20 sites)

## How to run

```bash
pip install -r requirements.txt
jupyter notebook 07_healthcare_intelligence_agent.ipynb
```

**Simulation Mode is the default** — no API key required. All LLM calls and
external services use deterministic, chapter-derived mock responses.

For **live mode**, copy the environment template from the workshop root and
set a key plus provider:

```bash
cp ../.env.template .env
# edit .env: set OPENAI_API_KEY (or ANTHROPIC_API_KEY / GOOGLE_API_KEY)
# and LLM_PROVIDER=openai | anthropic | google | auto
```

The notebook locates the shared multi-provider helper via `sys.path.insert(0, '..')`,
so run it from this folder with the workshop root as its parent.

## Files

- `07_healthcare_intelligence_agent.ipynb` — self-contained workshop notebook (pre-run in Simulation Mode)
- `requirements.txt` — minimal dependencies (heavy live-mode-only deps commented out)
- `README.md` — this file

Shared at the workshop root (not duplicated here): `supporting/llm_provider.py`, `.env.template`.

## Safety note

This is educational code, not production-ready clinical software. All patient
data is synthetic, mock responses are deterministic for reproducibility, and
the 0.15 escalation threshold is illustrative, not clinically validated.
Clinical deployment requires human oversight and regulatory review (§13.9).
