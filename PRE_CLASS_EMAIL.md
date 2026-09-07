# Pre-Class Emails — Instructor Copy

Three ready-to-send messages. Replace the `<...>` placeholders, then send:

- **Email 1** — 5 days before the workshop
- **Email 2** — 1 day before (with the setup office hour)
- **Email 3** — morning of the workshop, also pasted into the chat at kickoff

---

## Email 1 — 5 days before

**Subject:** 10 Essential AI Agents workshop — 30 minutes of setup before `<date>`

Hi all,

Welcome to *10 Essential AI Agents Every Engineer Must Build*. Over 6 hours we
build ten working agents together — from a tool-using agent and a RAG pipeline
to a multi-agent claims workflow, domain specialists for finance, healthcare
and education, a vision-language agent, and an embodied drone-mission planner.
The format is build-along: short concept framing, live code, then you build.

**One thing matters before we meet: 30 minutes of setup on your laptop.**

1. Open the setup guide: <https://github.com/cloudanum/ws-10-agents> → `PRE_CLASS_SETUP.md`
2. Clone the repo and run `python3 check_setup.py` — it verifies your machine
   in under a minute.
3. Install the first two agents' requirements (Step 3 of the guide).

**You do not need an API key.** Every notebook runs in a no-key Simulation
Mode with equivalent output. If you happen to have an OpenAI or Claude key,
Step 4 of the guide shows how to optionally unlock Live Mode (cost for the day:
well under $1 — set a $2–5 spend cap first).

Can't install software on your laptop (corporate lockdown)? No problem — the
guide has a zero-install Google Colab path that runs everything in a browser.

**Setup office hour:** `<date/time>` at `<meeting link>`. Bring any failure
output — or post it in `<help channel link>` anytime; a TA will pick it up.

Agenda for the day (all times `<timezone>`):

- Act I — How an agent thinks (Agents 1–2)
- Act II — Agents working together (Agents 3–5)
- Act III — Domain specialists: finance, healthcare, education (Agents 6–8)
- Act IV — Perception & the physical world (Agents 9–10)
- Wrap-up & Q&A

See you `<date>`,
`<instructor name>`

---

## Email 2 — 1 day before

**Subject:** Tomorrow: AI Agents workshop — final setup check + office hour today

Hi all,

We start tomorrow at `<time> <timezone>`: `<meeting link>`.

Two-minute checklist:

- [ ] `python3 check_setup.py` in the repo folder prints **READY**
- [ ] Agents 1 and 2 requirements installed (guide Step 3)
- [ ] Help channel joined: `<help channel link>`

If anything is red, today's **setup office hour** is your safety net:
`<date/time>` at `<meeting link>`. Can't make it? Post the `check_setup.py`
report block in the help channel — a TA will respond async.

Behind on setup? **Come anyway.** The Colab fallback takes five minutes in a
browser, and every notebook ships pre-executed so you can follow along while a
TA catches you up at the first break.

`<instructor name>`

---

## Email 3 — morning of (also pinned in chat)

**Subject:** Starting at `<time>` today — links inside

- Join: `<meeting link>`
- Repo: <https://github.com/cloudanum/ws-10-agents> (setup guide: `PRE_CLASS_SETUP.md`)
- Help channel: `<help channel link>`
- Setup failed this morning? Open Colab path: <https://github.com/cloudanum/ws-10-agents> →
  `PRE_CLASS_SETUP.md` → "Fallback: Google Colab"

House rules for the day:

1. **If a run breaks, don't fall behind** — the notebooks are pre-executed;
   keep following along and post the issue in the help channel. TAs fix things
   at the breaks.
2. Status checks after every agent: reply green / yellow / red in chat.
3. Questions that go deep go in the parking lot (help channel thread) — we
   answer them in the wrap-up.
4. No API key? You're on Simulation Mode like most of the room — full
   experience, zero cost.

See you in `<N>` hours!
