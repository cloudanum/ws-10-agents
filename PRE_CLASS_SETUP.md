# Pre-Class Setup Guide — 10 Essential AI Agents Workshop

Please complete this **before the workshop**. It takes about 30 minutes, mostly
unattended download time. Doing this ahead of time is the single biggest factor
in a smooth workshop day — we cover two agents per hour and cannot pause for
installs.

**You do NOT need an API key.** Every notebook runs in a no-key *Simulation
Mode* with pedagogically equivalent output. If you have an OpenAI or Claude key,
you can optionally unlock *Live Mode* (see Step 4).

---

## What you need

- A laptop you can install software on (macOS, Windows, or Linux)
- **Python 3.10–3.12** (3.12 recommended — see FAQ if you have 3.13+)
- Git (optional — you can download a ZIP instead)
- ~1 GB free disk space and an internet connection that can reach pypi.org

Locked-down corporate laptop or can't install anything? Skip to
**Fallback: Google Colab** — you can do the entire workshop in a browser.

## Step 1 — Get the repository (5 min)

```bash
git clone https://github.com/cloudanum/ws-10-agents
cd ws-10-agents
```

Or download the ZIP from the same link, extract it, and open a terminal in the
`ws-10-agents` folder.

## Step 2 — Run the pre-flight check (1 min)

```bash
python3 check_setup.py          # Windows: py -3.12 check_setup.py
```

You want `Result: READY`. Warnings are usually fine — read them. If you get
`NOT READY`, check the FAQ below; if still stuck, paste the whole report block
into the workshop help channel **before** class day.

Optional deeper check (installs agent 01's packages into a throwaway
environment, then deletes it):

```bash
python3 check_setup.py --full
```

## Step 3 — Install the first two agents (15–20 min, mostly unattended)

Each agent folder has its own isolated environment (their pinned dependencies
differ, so one shared environment does not work). Install only agents 1 and 2
now — the rest install quickly during breaks.

**macOS / Linux:**

```bash
cd 01-tool-using-agent
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cd ..

cd 02-knowledge-retrieval-rag-agent
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cd ..
```

**Windows (PowerShell):**

```powershell
cd 01-tool-using-agent
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd ..

cd 02-knowledge-retrieval-rag-agent
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd ..
```

Then confirm one notebook launches:

```bash
cd 01-tool-using-agent && source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
jupyter notebook 01_tool_using_agent.ipynb
```

You should see the yellow **SIMULATION MODE** banner when you run the first
cells. That's the workshop working — you're done.

## Step 4 (optional) — Add your own API key for Live Mode

Only if you already have an OpenAI or Claude key:

```bash
cp .env.template .env
# Edit .env and paste ONE key: OPENAI_API_KEY or ANTHROPIC_API_KEY
```

Tips:

- Cheapest Live Mode: the notebooks support the "fast" models
  (`gpt-4o-mini`, `claude-haiku-4-5`). A full workshop day costs well under $1.
- Set a hard spend limit ($2–5) in your provider dashboard before class.
- `.env` is git-ignored; never commit or share your key.
- Agent 06 (financial advisory) uses Finnhub/Tavily keys in Live Mode — the
  instructor demos that one; Simulation Mode covers the class.

---

## Fallback: Google Colab (zero install)

Use this if your laptop can't install software, your setup fails, or you just
prefer the browser. Works on any machine with Chrome/Edge/Firefox.

1. Open <https://colab.research.google.com> and sign in with a Google account.
2. **File → Open notebook → GitHub**, paste
   `https://github.com/cloudanum/ws-10-agents`, pick the first agent's notebook
   (e.g. `01-tool-using-agent/01_tool_using_agent.ipynb`).
3. In a first cell, run:

   ```python
   !git clone https://github.com/cloudanum/ws-10-agents repo
   %cd repo/01-tool-using-agent
   %pip install -q -r requirements.txt
   ```

4. Run the notebook as usual — Simulation Mode works out of the box.
5. For Live Mode, use Colab's **Secrets** panel (key icon, left sidebar) to add
   `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` instead of a `.env` file. The
   bootstrap cell loads them automatically — no extra code needed.
6. Repeat steps 2–3 per agent folder. Colab resets when idle, so reinstall is
   one cell per session.

## Fallback: GitHub Codespaces (cloud dev environment)

If you have a GitHub account, the repo includes a `.devcontainer` — open the
repo in a Codespace (Code → Codespaces → Create) and agents 1–2 install
automatically in a Python 3.12 environment. For agents 3–10, create per-agent
venvs exactly as in Step 3. Free tier: ~120 core-hours/month, plenty for the
workshop.

---

## FAQ

**"Do I need to buy an API key?"**
No. Simulation Mode is the default for the whole class and is pedagogically
equivalent. Keys are an optional enhancement.

**"I have Python 3.13/3.14."**
Several pinned packages (`numpy==1.26.4` in agents 06/08, `faiss-cpu` in agent
02) don't publish wheels for 3.13+ yet. Install Python 3.12 alongside (from
python.org, or `brew install python@3.12`, or `pyenv install 3.12`) and use it
for the venvs: `python3.12 -m venv .venv`.

**"I have Python 3.9 or older."**
Too old — install 3.12.

**"Windows: Activate.ps1 'cannot be loaded because running scripts is disabled'."**
Run once in PowerShell: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**"check_setup.py warns about missing SSL root certificates (macOS)."**
Classic python.org quirk — Python ships without root certificates on macOS.
Open `/Applications/Python 3.12/` and double-click **Install
Certificates.command**. pip installs work regardless, so this warning alone
won't block you.

**"pip install fails on faiss-cpu / numpy with a build error."**
Almost always a too-new Python (see above). If you're on 3.10–3.12 already,
paste the error into the help channel or use Colab.

**"My corporate laptop blocks pip / venv / python.org."**
Use the Colab fallback — no install required, works through a browser.

**"My internet is slow / I'm on hotel Wi-Fi."**
Install only agents 1 and 2 before class (Step 3). Each remaining agent's
requirements install in under a minute during breaks. Or use Colab, where
installs happen in Google's datacenters.

**"Can I use conda instead of venv?"**
Yes — `conda create -n agent01 python=3.12 && conda activate agent01`, then
`pip install -r requirements.txt` as usual.

**"Will sessions be recorded?"**
Yes — all four acts are recorded and shared with the repo link afterward.
Attendees in every timezone can catch up asynchronously.

---

## Day of the workshop

- Have open: your terminal in the `ws-10-agents` folder, Jupyter, and the
  help channel.
- Mantra: **if a run breaks, don't fall behind.** Every notebook ships with
  pre-executed outputs — keep following along, post your issue in the help
  channel, and a TA will catch you up at the next break.
- We'll do a green/yellow/red status check after each agent — answer honestly,
  it sets the pace.

## Still stuck?

Run `python3 check_setup.py --full` and paste the entire report block (it
contains OS, Python version, and every check result — never any API keys) into
the workshop help channel, or bring it to the setup office hour the day before
class.
