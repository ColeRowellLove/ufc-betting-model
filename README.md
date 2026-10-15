# UFC Betting Model

End-to-end UFC fight-outcome forecasting: scraped data, a leak-free feature store, calibrated
models, an honest walk-forward backtest, and a small rule-bound betting pool. The real target is
not profit but well-calibrated probabilities that can be compared fairly against the de-vigged
betting market.

## Quick start

Requires [uv](https://docs.astral.sh/uv/) and (for the database) Docker.

```bash
make install   # uv sync + pre-commit hooks
make check     # ruff, mypy (strict), pytest
make up        # Postgres via docker compose
```

## Layout

```
src/ufc_model/   package code (src layout)
tests/           pytest suite
.github/         CI, PR + issue templates, dependabot
```

## Milestones

M0 Setup, M1 Data pipeline, M2 Features + baselines, M3 Models + ensemble, M4 Betting backtest,
M5 Paper trade + deploy, M6 Write-up. See `CLAUDE.md` and `CONTRIBUTING.md`.

## Disclaimer

Research project. Not financial advice. Check each site's scraping terms before running at scale.

## License

MIT
