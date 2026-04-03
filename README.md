# AI_Projects

## Objective
Build a portfolio that combines agentic AI experimentation with VLSI-focused tooling so recruiters and collaborators can see progress across both domains.

## Repository Layout
- `python_practice/` — learning playground (separate git repo) with VLSI analyzers, LangChain experiments, and general Python exercises.
- `trading_agent/` — FYERS trading bot experiments, auth scripts, strategies, and backtesting stubs.
- `open_ai/` — assorted OpenAI API practice scripts.
- `tools/` — small utilities and one-off helpers.
- `steps_for_env_setup` — personal environment bootstrap notes.

## How to Work With This Repo
1. Use `python -m venv .venv && source .venv/bin/activate` (or your preferred env) at the root; install deps from `requirement.txt` if needed.
2. The `python_practice` directory is its own git project; run git commands from inside it when working on VLSI/LangChain code.
3. For trading work, copy `.env` templates in `trading_agent/` and keep credentials local; logs and venvs are ignored via updated `.gitignore`.
4. Avoid committing large logs or secrets; `.gitignore` is tuned to keep noise out while leaving source and docs tracked.

## Recruiter Snapshot
- Focus: Agentic AI workflows, LangChain tooling, and VLSI debug automation.
- Recent highlight: LangChain-based DRC analyzer that returns structured JSON for downstream automation.
- Comfort zone: Python, prompts/LLMs, EDA-oriented debugging flows, and applied scripting.
