# 10 Essential AI Agents Every Engineer Must Build — Hands-On Workshop

A build-along workshop across Finance, Healthcare, Education and beyond.

Companion repository for the Packt workshop, based on the Packt title
[*30 Agents Every AI Engineer Must Build*](https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build)
by Imran Ahmad, PhD (Packt, 2026).

**Format:** Build-along — short concept framing, live code, then attendees build. Approx. two agents per hour.
**Duration:** 6 hours including 1 hour of breaks (5 hours content). Trimmable to 5 hours (see Logistics).
**Audience:** AI/ML and software engineers; technical leaders. Mixed experience welcome.
**Prerequisites:** Laptop, Python 3.10+, Git. **No API key required** — every agent runs in a no-key Simulation Mode; optional keys unlock Live Mode with OpenAI, Claude, or Gemini.

---

## The 10 Agents

The agents are sequenced to tell a story — from how a single agent reasons, to agents working
together, to specialists for regulated domains, to perception of the physical world.

| # | Agent | Book | Folder | What you'll see |
|:--|:------|:-----|:-------|:----------------|
| 1 | **Tool-Using Agent** | Ch. 7 (§7.1–7.3) | `01-tool-using-agent/` | An LLM reasons about a request, selects the right tool from a registry, and executes it through a function-calling loop — the pattern every later agent is built on. |
| 2 | **Knowledge Retrieval / RAG Agent** | Ch. 6 (§6.1) | `02-knowledge-retrieval-rag-agent/` | An end-to-end RAG pipeline — chunk, embed, FAISS index, and answers grounded only in your corpus, with source passages cited. |
| 3 | **Chain-of-Agents Orchestrator** | Ch. 7 (§7.4–7.6, §7.7b) | `03-chain-of-agents-orchestrator/` | A multi-agent insurance-claims workflow (OCR → validation → risk → payout) governed by a state machine with human-in-the-loop escalation and a full audit trail. |
| 4 | **Data Analysis Agent** | Ch. 8 | `04-data-analysis-agent/` | A plain-English question becomes code, runs over a dataset, and returns a live chart plus a statistical readout in seconds. |
| 5 | **Verification / Fact-Checking Agent** | Ch. 8 | `05-verification-fact-checking-agent/` | A news statement is broken into claims and returned with a supported / refuted verdict and its supporting evidence. |
| 6 | **Financial Advisory Agent** | Ch. 14 | `06-financial-advisory-agent/` | "RetailAdvisor": a risk profile in, a tailored portfolio recommendation out. |
| 7 | **Healthcare Intelligence Agent** | Ch. 13 (§13.1) | `07-healthcare-intelligence-agent/` | Patient inputs produce a clinical decision-support output with its reasoning surfaced. |
| 8 | **Education Intelligence Agent** | Ch. 15 (§15.1) | `08-education-intelligence-agent/` | An adaptive programming tutor diagnoses a learner's gap and adjusts its next explanation. |
| 9 | **Vision-Language Agent** | Ch. 11 (§11.1) | `09-vision-language-agent/` | An image in, a natural-language answer out — the workshop's big visual moment. |
| 10 | **Embodied Intelligence Agent** | Ch. 16 (§16.1) | `10-embodied-intelligence-agent/` | An autonomous drone mission planned under real Ottawa winter conditions, gated by a unified constraint envelope. |

**Verticals covered:** Finance · Healthcare · Education · Insurance · Data & Analytics · Media & Fact-Checking · Multimodal · Robotics.

## Workshop Run of Show

- **Act I — How an agent thinks** (~55 min): Agents 1–2
- *Break (15 min)*
- **Act II — Agents working together** (~85 min): Agents 3–5
- *Lunch (30 min)*
- **Act III — Domain specialists** (~85 min): Agents 6–8
- *Break (15 min)*
- **Act IV — Perception & the physical world** (~55 min): Agents 9–10
- **Wrap-up & Q&A** (~15 min): composing these patterns into larger systems; where to go next

Each agent is one self-contained folder, so the running order and length flex easily on the day.

## Quick Start

```bash
# Pick an agent — folders are independent, start anywhere
cd 01-tool-using-agent

# Create an environment and install that agent's dependencies
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Launch the notebook — no API key needed (Simulation Mode)
jupyter notebook 01_tool_using_agent.ipynb
```

### Before the workshop (attendees)

Run the pre-flight check at the repo root — it verifies Python, pip, venv,
network, and key detection in under a minute:

```bash
python3 check_setup.py          # add --full for a throwaway install test
```

Full setup steps, FAQ, and zero-install fallbacks (Colab / Codespaces) are in
[PRE_CLASS_SETUP.md](PRE_CLASS_SETUP.md). Instructor email copy:
[PRE_CLASS_EMAIL.md](PRE_CLASS_EMAIL.md).

### Simulation Mode vs. Live Mode

Every notebook **defaults to Simulation Mode**: all LLM calls are served by a chapter-derived
`MockLLM`, so the full workshop runs with **zero API keys and zero setup risk**. Outputs are
pedagogically equivalent to Live Mode.

To run against a real model, copy the template at the repo root and set **one** key:

```bash
cp .env.template .env
# Edit .env — set LLM_PROVIDER (openai | anthropic | google | auto) and the matching key:
#   OPENAI_API_KEY / ANTHROPIC_API_KEY / GOOGLE_API_KEY
```

Multi-provider routing is handled by `supporting/llm_provider.py`, shared by all ten agents.

## Repository Layout

```
10-agents-workshop/
├── 01-tool-using-agent/                 # Ch. 7  — tool registry + function-calling loop
├── 02-knowledge-retrieval-rag-agent/    # Ch. 6  — RAG with FAISS + cited sources
├── 03-chain-of-agents-orchestrator/     # Ch. 7  — multi-agent claims workflow + HITL
├── 04-data-analysis-agent/              # Ch. 8  — NL question → code → chart
├── 05-verification-fact-checking-agent/ # Ch. 8  — claim extraction + evidence verdicts
├── 06-financial-advisory-agent/         # Ch. 14 — RetailAdvisor portfolio recommendations
├── 07-healthcare-intelligence-agent/    # Ch. 13 — Bayesian diagnostic decision support
├── 08-education-intelligence-agent/     # Ch. 15 — adaptive tutor (BKT, IRT, SM-2)
├── 09-vision-language-agent/            # Ch. 11 — vision question answering
├── 10-embodied-intelligence-agent/      # Ch. 16 — drone mission planner (Ottawa winter)
├── supporting/llm_provider.py           # shared multi-provider LLM detection
├── check_setup.py                       # attendee pre-flight check (--full for install test)
├── PRE_CLASS_SETUP.md                   # attendee setup guide + FAQ + Colab/Codespaces fallbacks
├── PRE_CLASS_EMAIL.md                   # instructor email copy (T-5 days / T-1 day / day-of)
├── .devcontainer/                       # one-click GitHub Codespaces environment (Python 3.12)
├── .env.template                        # optional API keys for Live Mode
└── LICENSE                              # MIT
```

Each agent folder contains its own pre-executed notebook (outputs included), the helper
modules and data it needs, a trimmed `requirements.txt`, and a short README.

## What Attendees Take Home

- A working repository with all 10 agents, runnable with OpenAI, Claude, Gemini, or a no-key simulation mode.
- A mental model for composing these patterns into larger, multi-agent systems.
- A tie-in to the book *30 Agents Every AI Engineer Must Build* — each agent folder cites its chapter and sections for deeper reading.

## Logistics Notes

- **5-hour cut:** reduce Act IV to one agent (keep the Vision-Language Agent) or make the drone agent a recorded bonus.
- **6-hour version:** full 10 agents as outlined above.
- **Setup risk is low:** Simulation Mode means attendees without API keys can still follow every build.
- **Remote cohorts:** send `PRE_CLASS_EMAIL.md` copy 5 days out; attendees self-certify with `check_setup.py` and follow `PRE_CLASS_SETUP.md` (Colab and Codespaces fallbacks for locked-down laptops). Per-agent venvs are required — the agents' pinned dependencies conflict by design.
- Heavy optional dependencies (e.g. torch/transformers for live vision and NLI demos) are commented out in each `requirements.txt`; notebooks skip those demos gracefully without them.

## License

MIT — see [LICENSE](LICENSE). Code is reorganized from the book's companion repository by the author.
