# Contributing

## Branching
- `main`: always releasable; only updated by merging `develop` via PR.
- `develop`: integration branch; feature branches are cut from here.
- Feature branches: `feat/<topic>`, `fix/<topic>`, `chore/<topic>`; open a PR into `develop`.

## Workflow
1. `make install` (uses [uv](https://docs.astral.sh/uv/))
2. Branch from `develop`, make changes, add tests.
3. `make check` must pass (ruff lint + format, mypy strict, pytest).
4. Open a PR into `develop` using the template. CI must be green; squash-merge.

## Conventions
- Conventional-style commit prefixes: `feat:`, `fix:`, `chore:`, `docs:`, `test:`.
- Every feature must be computable from data available before the event date.
