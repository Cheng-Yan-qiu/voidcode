# Development Guide

This guide summarizes the local workflow for contributing to VoidCode.

## Tooling baseline

VoidCode uses:

- `mise` for environment and task management
- `uv` for dependency and package management
- Python 3.14 as the preferred local version, with 3.13 or 3.12 as fallback options

## Initial setup

Install toolchain dependencies and project dependencies:

```bash
mise install
uv sync --extra dev
```

Confirm the CLI entrypoint is available:

```bash
uv run voidcode --help
```

## mise tasks

The repository defines these `mise` tasks:

- `mise run lint` → `uv run ruff check .`
- `mise run format` → `uv run ruff format .`
- `mise run typecheck` → `uv run mypy src`
- `mise run test` → `uv run pytest`
- `mise run check` → runs lint, typecheck, and test
- `mise run pre-commit` → `uv run pre-commit run --all-files`

## Common uv commands

If you prefer running tools directly instead of through `mise`, the equivalents are:

```bash
uv sync --extra dev
uv run voidcode --help
uv run ruff check .
uv run ruff format .
uv run mypy src
uv run pytest
uv run pre-commit run --all-files
```

## pre-commit setup

Install the git hook locally:

```bash
uv run pre-commit install
```

The current configuration includes:

- trailing whitespace cleanup
- end-of-file normalization
- YAML validation
- large-file checks
- Ruff linting
- Ruff formatting checks
- mypy

## Running tests

Run the full test suite with:

```bash
mise run test
```

or:

```bash
uv run pytest
```

For the standard local validation pass before opening a contribution, use:

```bash
mise run check
mise run pre-commit
```

## Project layout

The current source tree reserves space for three main implementation areas:

- `src/voidcode/runtime/`
- `src/voidcode/graph/`
- `src/voidcode/tools/`

Tests live under `tests/`, and the original planning documents remain at the repository root in Chinese.
