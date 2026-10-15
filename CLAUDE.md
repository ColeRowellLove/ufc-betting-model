# CLAUDE.md

UFC fight-outcome forecasting and betting-evaluation project. Goal: calibrated probabilities
benchmarked against the de-vigged market (log loss, Brier, CLV), not profit.

## Commands (uv)
- `uv sync` install deps; `uv run <cmd>` runs inside the env. Commit `uv.lock`.
- `make check` = `ruff check` + `mypy` + `pytest` + `ruff format --check`. Must pass before a PR.
- `make format` auto-formats. `make up` / `make down` start/stop Postgres.

## Conventions
- Python 3.11+, src layout (`src/ufc_model`), full type hints (mypy strict).
- Ruff for lint and format, line length 100. Tests in `tests/`, mirror module names.
- Add a dependency with `uv add <pkg>` (runtime) or `uv add --dev <pkg>`.

## Git workflow
- `main` is releasable; `develop` is the integration branch. Branch from `develop` as
  `feat/*`, `fix/*`, `chore/*`; PR into `develop`; squash-merge. Never push directly to `main`.

## Modeling rules (non-negotiable)
1. Features only from bouts strictly before the event date. No career totals from profile pages.
2. Randomize fighter a/b order; never use red/blue corner. Train on both orderings.
3. Validation is walk-forward only; no random k-fold.
4. Judge models by out-of-sample log loss vs de-vigged market; accuracy is secondary.
5. Version features (`feature_version`) so every prediction is traceable.
6. Every feature change needs a leakage test.

## Betting rules
- Decimal odds internally. Quarter Kelly, 2% per-bet cap, 8% per-event cap, EV threshold ~4%.
- Moneylines only in v1. Track CLV = ln(d_taken / d_close) on every bet.
- Real money is gated behind the backtest + paper-trading criteria; never automate placing bets.

## Planned stack
httpx + selectolax scrapers, Postgres/SQLAlchemy/Alembic, pandera, scikit-learn, LightGBM, PyMC,
PyTorch, Optuna, MLflow, Streamlit/FastAPI.
