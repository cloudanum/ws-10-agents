#!/usr/bin/env python3
"""Pre-flight setup check — 10 Essential AI Agents workshop.

Run this at the repository root BEFORE the workshop:

    python3 check_setup.py            # fast check (under a minute, nothing installed)
    python3 check_setup.py --full     # also creates a throwaway venv and installs
                                      # agent 01's requirements (a few minutes)
    python3 check_setup.py --full 04-data-analysis-agent   # check a specific agent

It verifies Python version, pip, venv, git, network access, disk space, and
whether an API key is available (Live Mode) or not (Simulation Mode — expected
for most attendees). If anything fails, paste the final report block into the
workshop help channel.

Standard library only — nothing needs to be installed to run this script.
"""

import argparse
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

MIN_PYTHON = (3, 10)
# numpy==1.26.4 (agents 06/08) and faiss-cpu (agent 02) have no 3.13 wheels yet
MAX_TESTED_PYTHON = (3, 12)

PYPI_URL = "https://pypi.org/simple/"
NETWORK_TIMEOUT = 5

# Import names used to smoke-test each agent's requirements after --full install
SMOKE_IMPORTS = {
    "01-tool-using-agent": ["pandas", "matplotlib", "dotenv", "ipykernel"],
    "02-knowledge-retrieval-rag-agent": ["numpy", "pandas", "langchain", "faiss"],
    "03-chain-of-agents-orchestrator": ["pandas", "matplotlib", "dotenv"],
    "04-data-analysis-agent": ["numpy", "pandas", "matplotlib", "statsmodels"],
    "05-verification-fact-checking-agent": ["dotenv"],
    "06-financial-advisory-agent": ["langchain", "langgraph", "yfinance", "finnhub", "tavily"],
    "07-healthcare-intelligence-agent": ["numpy", "dotenv", "nest_asyncio"],
    "08-education-intelligence-agent": ["numpy", "networkx", "dotenv"],
    "09-vision-language-agent": ["numpy", "PIL", "dotenv"],
    "10-embodied-intelligence-agent": ["langchain", "langgraph", "pydantic", "dotenv"],
}

PLACEHOLDER_MARKERS = ("your-key", "your_key", "xxx", "placeholder")
PROVIDER_ORDER = ["openai", "anthropic", "google"]
PROVIDER_ENV_KEYS = {
    "OPENAI_API_KEY": "openai",
    "ANTHROPIC_API_KEY": "anthropic",
    "GOOGLE_API_KEY": "google",
}


class Report:
    def __init__(self):
        self.lines = []

    def ok(self, label, detail=""):
        self.lines.append(("PASS", label, detail))

    def warn(self, label, detail=""):
        self.lines.append(("WARN", label, detail))

    def fail(self, label, detail=""):
        self.lines.append(("FAIL", label, detail))

    def counts(self):
        fails = sum(1 for s, _, _ in self.lines if s == "FAIL")
        warns = sum(1 for s, _, _ in self.lines if s == "WARN")
        return fails, warns

    def render(self):
        out = ["", "=" * 62, "  WORKSHOP SETUP CHECK — paste this block if you need help", "=" * 62]
        out.append(f"  OS: {platform.system()} {platform.release()} ({platform.machine()})")
        out.append(f"  Python: {sys.version.split()[0]}  ({sys.executable})")
        out.append("-" * 62)
        for status, label, detail in self.lines:
            line = f"  [{status}] {label}"
            if detail:
                line += f" — {detail}"
            out.append(line)
        out.append("-" * 62)
        fails, warns = self.counts()
        if fails:
            verdict = "NOT READY — fix the FAIL lines above (see PRE_CLASS_SETUP.md FAQ)"
        elif warns:
            verdict = "READY (with warnings — read them, you can likely proceed)"
        else:
            verdict = "READY — see you at the workshop!"
        out.append(f"  Result: {verdict}")
        out.append("=" * 62)
        return "\n".join(out)


def check_python(report):
    v = sys.version_info
    version_str = f"{v.major}.{v.minor}.{v.micro}"
    if (v.major, v.minor) < MIN_PYTHON:
        report.fail("Python version", f"{version_str} found, 3.10+ required — install Python 3.12")
    elif (v.major, v.minor) > MAX_TESTED_PYTHON:
        report.warn(
            "Python version",
            f"{version_str} is newer than the tested range (3.10–3.12). "
            "Some pinned packages (numpy==1.26.4, faiss-cpu) may not install — Python 3.12 recommended",
        )
    else:
        report.ok("Python version", version_str)


def check_pip(report):
    try:
        out = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True, text=True, timeout=30,
        )
        if out.returncode == 0:
            report.ok("pip", out.stdout.strip().splitlines()[0])
        else:
            report.fail("pip", "pip is not working — reinstall Python from python.org with pip enabled")
    except Exception as exc:
        report.fail("pip", f"could not run pip ({exc})")


def check_venv(report):
    try:
        import ensurepip  # noqa: F401
        import venv  # noqa: F401
        report.ok("venv module", "can create virtual environments")
    except ImportError:
        report.fail(
            "venv module",
            "missing — on Debian/Ubuntu run: sudo apt install python3-venv",
        )


def check_git(report):
    git = shutil.which("git")
    if git:
        try:
            out = subprocess.run(["git", "--version"], capture_output=True, text=True, timeout=15)
            report.ok("git", out.stdout.strip())
        except Exception:
            report.ok("git", git)
    else:
        report.warn("git", "not found — you can still use the ZIP download instead of cloning")


def check_network(report):
    last_exc = None
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(PYPI_URL, method=method)
            with urllib.request.urlopen(req, timeout=NETWORK_TIMEOUT):
                pass
            report.ok("network", f"reached {PYPI_URL} (needed for pip installs)")
            return
        except Exception as exc:
            last_exc = exc
    reason = getattr(last_exc, "reason", last_exc)
    if "CERTIFICATE_VERIFY_FAILED" in str(reason):
        report.warn(
            "network",
            "SSL root certificates missing (common with python.org Python on macOS). "
            "Fix: run the 'Install Certificates.command' in your /Applications/Python 3.x folder "
            "(Linux: sudo apt install ca-certificates). pip installs are unaffected.",
        )
    else:
        report.warn(
            "network",
            f"could not reach {PYPI_URL} ({last_exc.__class__.__name__}) — check proxy/VPN; "
            "the Colab fallback in PRE_CLASS_SETUP.md works around locked-down networks",
        )


def check_disk(report):
    free_gb = shutil.disk_usage(REPO_ROOT).free / (1024 ** 3)
    if free_gb < 1:
        report.fail("disk space", f"only {free_gb:.1f} GB free — need at least 1 GB")
    elif free_gb < 2:
        report.warn("disk space", f"{free_gb:.1f} GB free — tight but workable")
    else:
        report.ok("disk space", f"{free_gb:.1f} GB free")


def _read_env_file(path):
    values = {}
    if not os.path.exists(path):
        return values
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def check_api_keys(report):
    from_file = _read_env_file(os.path.join(REPO_ROOT, ".env"))
    found = []
    for env_var, provider in PROVIDER_ENV_KEYS.items():
        value = os.environ.get(env_var, "").strip() or from_file.get(env_var, "").strip()
        if value and not any(p in value.lower() for p in PLACEHOLDER_MARKERS):
            found.append(provider)
    if found:
        active = next(p for p in PROVIDER_ORDER if p in found)
        report.ok(
            "API key (optional)",
            f"{active} key detected — you can run Live Mode. Key values are never displayed.",
        )
    else:
        report.ok(
            "API key (optional)",
            "no key found — you will run in Simulation Mode, which is fully supported. "
            "To use your own key later: cp .env.template .env and paste it in.",
        )


def full_install_check(report, agent_dir):
    req_path = os.path.join(REPO_ROOT, agent_dir, "requirements.txt")
    if not os.path.exists(req_path):
        report.fail("full check", f"no requirements.txt found at {agent_dir}/")
        return

    print(f"\nInstalling {agent_dir}/requirements.txt into a throwaway venv — "
          "this takes a few minutes on first run...")
    with tempfile.TemporaryDirectory(prefix="workshop-check-") as td:
        try:
            subprocess.run([sys.executable, "-m", "venv", td], check=True,
                           capture_output=True, text=True, timeout=180)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
            report.fail("full check — create venv", str(exc)[:200])
            return

        venv_py = os.path.join(td, "Scripts" if os.name == "nt" else "bin",
                               "python.exe" if os.name == "nt" else "python")
        install = subprocess.run(
            [venv_py, "-m", "pip", "install", "--quiet", "--disable-pip-version-check",
             "-r", req_path],
            capture_output=True, text=True,
        )
        if install.returncode != 0:
            tail = "\n".join((install.stderr or install.stdout).splitlines()[-8:])
            report.fail("full check — pip install", f"failed. Last lines:\n{tail}")
            return
        report.ok("full check — pip install", f"{agent_dir} requirements installed cleanly")

        imports = SMOKE_IMPORTS.get(agent_dir, [])
        if imports:
            smoke = subprocess.run(
                [venv_py, "-c", "import " + ", ".join(imports)],
                capture_output=True, text=True,
            )
            if smoke.returncode == 0:
                report.ok("full check — imports", ", ".join(imports))
            else:
                tail = "\n".join((smoke.stderr or "").splitlines()[-5:])
                report.fail("full check — imports", f"failed:\n{tail}")


def main():
    parser = argparse.ArgumentParser(description="Workshop pre-flight setup check")
    parser.add_argument(
        "--full", nargs="?", const="01-tool-using-agent", metavar="AGENT_DIR", default=None,
        help="also install requirements into a throwaway venv (default agent: 01-tool-using-agent)",
    )
    args = parser.parse_args()

    report = Report()
    check_python(report)
    check_pip(report)
    check_venv(report)
    check_git(report)
    check_network(report)
    check_disk(report)
    check_api_keys(report)
    if args.full:
        full_install_check(report, args.full)

    print(report.render())
    fails, _ = report.counts()
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
