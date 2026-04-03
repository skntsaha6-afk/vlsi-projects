# Trading Agent (FYERS)

## Overview
Prototype trading bot for FYERS: handles auth, websocket data, strategy evaluation, risk management, and order execution.

## Quickstart
1. Start auth server and obtain token: `auth/generate_auth_code.py` (follow FYERS login).
2. Launch data + bot: `start_bot.py`.
3. Choose a strategy in `strategies/` and wire risk rules in `risk_management/`.

## Directory Guide
- `auth/` auth flows and `access_token.txt`.
- `agents/` orchestrator entry (`trading_agent.py`).
- `execution/` broker client + order manager.
- `strategies/` plug-in strategies.
- `risk_management/` position and exposure checks.
- `websocket/` market data stream.
- `utils/` shared helpers.
- `backtesting/` stubs for offline testing (untracked data-friendly).

## Key Docs
- Architecture sketch: `trading_archirechture.md`.
- Run steps: `steps_to_run.md`.
- FYERS notes: `fyers_api_feature.md`.

## Status
Auth + skeleton bot flow exist; needs hardening, backtesting build-out, and cleaner env handling.
