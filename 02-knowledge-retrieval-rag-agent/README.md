# Workshop Agent 2 — The Knowledge Retrieval / RAG Agent

Companion to **Chapter 6, §6.1 — Knowledge Retrieval Agents (pp. 146–153)** of
*30 Agents Every AI Engineer Must Build* by Imran Ahmad (Packt, 2026).
## What this agent does

Builds an end-to-end Retrieval-Augmented Generation (RAG) pipeline: it loads and
chunks documents from `docs/`, embeds them, stores them in a FAISS vector index,
and answers questions grounded only in that corpus — with source passages cited
for provenance. A diagnostic refund-policy query demonstrates retrieval-failure
analysis, and a deep dive compares fixed-size, recursive, and semantic chunking
strategies (p. 151).

## How to run

```bash
pip install -r requirements.txt
jupyter notebook 02_knowledge_retrieval_rag_agent.ipynb
```

- **Simulation Mode (default):** no API key needed. All outputs use
  chapter-derived mocks from `agent_utils.py` and are pedagogically
  equivalent to Live Mode.
- **Live Mode:** `cp ../.env.template .env`, set `OPENAI_API_KEY` (and
  optionally `LLM_PROVIDER`), and uncomment the Live Mode packages in
  `requirements.txt`.

Note: the Section 0.1 dependency check may list §6.2/§6.3 packages
(`PIL`, `rapidfuzz`, `sklearn`) as missing — this agent does not need them;
the notebook continues normally.

## Files

| File | Purpose |
|------|---------|
| `02_knowledge_retrieval_rag_agent.ipynb` | Self-contained workshop notebook (pre-run in Simulation Mode) |
| `agent_utils.py` | Shared utilities: ColorLogger, fail_gracefully, MockLLM, MockEmbeddings, MockRetrievalQAResult |
| `docs/knowledge_base_rag.txt` | RAG concepts corpus for the retrieval pipeline |
| `docs/compliance_policy.txt` | Corporate policy corpus (data retention, refunds) |
| `requirements.txt` | Dependencies for this agent (trimmed from Chapter 6) |
