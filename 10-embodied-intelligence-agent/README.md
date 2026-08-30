# Agent 10: The Embodied Intelligence Agent

An autonomous drone mission planner that must satisfy a **Unified Constraint
Envelope** before anything moves — weather, battery, airspace, parks, and
mission-geometry domains must all report GREEN, and a single RED domain
vetoes the entire envelope. The capstone plans a 6 km photographic survey
from Centerpointe Technology Park to the Ottawa River waterfront under real
Ottawa winter conditions.

## Book Reference

*30 Agents Every AI Engineer Must Build* by Imran Ahmad (Packt, 2026),
**Chapter 16 — Embodied and Physical World Agents** (pp. 457–491): Listings
16.1–16.3 (embodied agent), Listings 16.6–16.7 (Ottawa drone case study),
failure demos. The companion Domain-Transforming Integration Agent (Listings
16.4–16.5) is covered in the book but is not part of this workshop agent.

## What You Build

- A multi-rate control hierarchy: task planning (0.1–1 Hz, LLM) down to servo control (1–10 kHz)
- An embodied agent whose safety monitor hard-gates every action against the admissible set A_safe(s)
- A Mission Supervisor + constraint assembler that arms only when all five domains report GREEN
- Five failure demos: wind ceiling, battery floor, active NOTAM, API timeout, stale weather data

## How to Run

    pip install -r requirements.txt
    jupyter notebook 10_embodied_intelligence_agent.ipynb

**Simulation Mode is the default** — no API key required; a MockLLM replays
chapter-accurate tool-call protocols. For Live Mode: `cp ../.env.template
.env`, then set your key and `LLM_PROVIDER` (`openai`/`anthropic`/`google`).

## Files

- `10_embodied_intelligence_agent.ipynb` — self-contained workshop notebook (pre-run)
- `mock_layer.py` — MockChatOpenAI + synthetic sensor/API data (Chapter 16)
- `resilience.py` — `@fail_gracefully` decorator + `ColorLogger`
- `requirements.txt` — pinned dependencies from the book chapter
