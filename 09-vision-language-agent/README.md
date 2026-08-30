# Workshop Agent 9: The Vision-Language Agent

A **Vision Question-Answering (VQA) agent** that loads a vision-language model
and answers natural-language questions about what it sees — an image in, a
natural-language answer out. The agent pairs a visual encoder with a large
language model through an alignment mechanism, reasons step by step with
Chain-of-Thought prompting, and degrades gracefully via the
`@graceful_fallback` resilience decorator.

**Book reference:** *30 Agents Every AI Engineer Must Build* — Imran Ahmad,
Packt Publishing, 2026. Chapter 11, §11.1: Architecture of Vision-Language
Agents (p.308-309), Building a Vision Question-Answering Agent (p.310-312).

## What you will see

Running against a synthetic workspace image generated inside the notebook, the
agent describes the scene, counts partially occluded people, and analyzes
spatial relationships between objects — followed by an error-handling demo that
turns an invalid input into a structured, logged fallback response.

## How to run

```bash
pip install -r requirements.txt
jupyter notebook 09_vision_language_agent.ipynb
```

The notebook runs in **Simulation Mode** by default — mock backends, no GPU,
no API key. Nothing else to configure.

For **Live Mode** (real LLaVA 1.5 inference + provider LLM):

```bash
cp ../.env.template .env   # then edit .env
# set OPENAI_API_KEY (or ANTHROPIC_API_KEY / GOOGLE_API_KEY) and LLM_PROVIDER
# plus HUGGINGFACE_TOKEN, and uncomment torch/transformers/accelerate
# in requirements.txt — a CUDA GPU with 16+ GB VRAM is required
```

## Files

| File | Purpose |
|------|---------|
| `09_vision_language_agent.ipynb` | Self-contained workshop notebook (§0 setup + §1.1-§1.7) |
| `agent_logger.py` | Color-coded logger (Blue/Green/Red) + `@graceful_fallback` decorator |
| `mock_backends.py` | Simulation Mode backends (`MockProcessor`, `MockVLM`, and the other chapter mocks) |
| `requirements.txt` | Core dependencies; heavy Live Mode deps commented out |
| `assets/` | Created at runtime — holds the generated `sample_workspace.png` |
