#!/usr/bin/env python3
"""Insert a Google Colab bootstrap cell into every workshop notebook.

The cell is a no-op outside Colab (prints a one-liner and continues).
On Colab it clones the repo, cd's into the agent folder, installs
that agent's requirements, and loads any API keys from Colab Secrets
into env vars — making the student flow "open notebook -> Run all".
"""

import json
import os
import sys

REPO_URL = "https://github.com/cloudanum/ws-10-agents"

AGENTS = {
    "01-tool-using-agent": "01_tool_using_agent.ipynb",
    "02-knowledge-retrieval-rag-agent": "02_knowledge_retrieval_rag_agent.ipynb",
    "03-chain-of-agents-orchestrator": "03_chain_of_agents_orchestrator.ipynb",
    "04-data-analysis-agent": "04_data_analysis_agent.ipynb",
    "05-verification-fact-checking-agent": "05_verification_fact_checking_agent.ipynb",
    "06-financial-advisory-agent": "06_financial_advisory_agent.ipynb",
    "07-healthcare-intelligence-agent": "07_healthcare_intelligence_agent.ipynb",
    "08-education-intelligence-agent": "08_education_intelligence_agent.ipynb",
    "09-vision-language-agent": "09_vision_language_agent.ipynb",
    "10-embodied-intelligence-agent": "10_embodied_intelligence_agent.ipynb",
}

CELL_TEMPLATE = '''# Google Colab bootstrap — runs only on Colab, no-op everywhere else.
# Locally you are already inside the agent folder with requirements installed.
import os
import sys

if "google.colab" in sys.modules:
    AGENT_DIR = "{agent_dir}"
    if not os.path.exists("/content/repo"):
        os.system("git clone --depth 1 {repo_url} /content/repo")
    os.chdir(f"/content/repo/{{AGENT_DIR}}")
    # On Colab, prefer requirements-colab.txt when present: it drops pins that
    # cannot coexist with Colab's preinstalled stack (e.g. langchain 0.2.16
    # requires numpy<2 on Python 3.13, while Colab ships numpy 2.x).
    req_file = "requirements-colab.txt" if os.path.exists("requirements-colab.txt") else "requirements.txt"
    # Keep Colab's preinstalled scientific/kernel stack: the kernel already has
    # numpy, pandas, pydantic and ipykernel loaded, so letting pip replace them
    # (e.g. building numpy 1.26.4 from source or upgrading ipykernel) breaks the
    # running kernel with ABI errors or an OOM kill. Filter those lines out of
    # requirements and constrain the rest of the install to the installed versions.
    import re
    from importlib.metadata import PackageNotFoundError, version
    filtered = [
        line for line in open(req_file)
        if not re.match(r"\\s*(numpy|pandas|pydantic|jupyter|ipykernel)\\b", line, re.IGNORECASE)
    ]
    with open("/tmp/colab_requirements.txt", "w") as fh:
        fh.writelines(filtered)
    pins = []
    for pkg in ("numpy", "pandas", "pydantic", "ipykernel"):
        try:
            pins.append(f"{{pkg}}=={{version(pkg)}}")
        except PackageNotFoundError:
            pass
    with open("/tmp/colab_constraints.txt", "w") as fh:
        fh.write("\\n".join(pins) + "\\n")
    import subprocess
    res = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-q",
         "-r", "/tmp/colab_requirements.txt",
         "--constraint", "/tmp/colab_constraints.txt"],
        capture_output=True, text=True,
    )
    if res.returncode != 0:
        print("pip install failed — re-running without -q for the full resolver report:\\n")
        subprocess.run(
            [sys.executable, "-m", "pip", "install",
             "-r", "/tmp/colab_requirements.txt",
             "--constraint", "/tmp/colab_constraints.txt"],
        )
        raise RuntimeError("Colab bootstrap: pip install failed (see resolver report above)")
    # Load API keys from Colab Secrets (key icon, left sidebar) into env vars, so
    # detect_provider() / os.getenv() find them exactly like a local .env file.
    # Missing secrets are skipped silently — the notebook then runs in Simulation Mode.
    try:
        from google.colab import userdata
        for _secret in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GOOGLE_API_KEY",
                        "FINNHUB_API_KEY", "TAVILY_API_KEY"):
            if not os.environ.get(_secret):
                try:
                    _value = userdata.get(_secret)
                except Exception:
                    _value = None
                if _value:
                    os.environ[_secret] = _value
                    print(f"Loaded {{_secret}} from Colab Secrets.")
    except Exception:
        pass
    print(f"Colab setup complete ({{req_file}}) — working directory: {{os.getcwd()}}")
else:
    print("Not on Colab — skipping bootstrap (local setup already in place).")'''


def make_cell(agent_dir):
    src = CELL_TEMPLATE.format(agent_dir=agent_dir, repo_url=REPO_URL)
    lines = [line + "\n" for line in src.split("\n")]
    lines[-1] = lines[-1].rstrip("\n")
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": "colab-bootstrap",
        "metadata": {},
        "outputs": [],
        "source": lines,
    }


def main():
    changed = []
    for agent_dir, nb_name in AGENTS.items():
        path = os.path.join("10-agents-workshop", agent_dir, nb_name)
        with open(path) as fh:
            nb = json.load(fh)
        cells = nb.get("cells", [])
        if not cells:
            print(f"SKIP {path}: no cells")
            continue
        for i, c in enumerate(cells):
            if c.get("id") == "colab-bootstrap":
                cells[i] = make_cell(agent_dir)
                with open(path, "w") as fh:
                    json.dump(nb, fh, indent=1, ensure_ascii=False)
                    fh.write("\n")
                changed.append(path + " (replaced)")
                break
        else:
            if cells[0].get("cell_type") != "markdown":
                print(f"SKIP {path}: first cell is {cells[0].get('cell_type')}, expected markdown")
                continue
            cells.insert(1, make_cell(agent_dir))
            with open(path, "w") as fh:
                json.dump(nb, fh, indent=1, ensure_ascii=False)
                fh.write("\n")
            changed.append(path)
    print(f"\nUpdated {len(changed)} notebooks")
    for p in changed:
        print(" -", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
