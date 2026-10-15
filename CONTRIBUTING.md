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

## Pull request policy
- One PR = one issue. Put `Closes #N` in the PR body; the `PR policy` check requires exactly one
  open, non-epic issue. Create the issue first if needed.
- Keep the diff scoped to that issue; unrelated changes go in their own issue and PR.
- Merging requires green `lint`, `typecheck`, `test` (3.11-3.13) and `pr-policy` checks.
- Exempt from the issue link: Dependabot PRs and the `develop` -> `main` release PR.
