# 06 — Project shape

Environments, configuration, imports, and generators — the structure of a real project.

## Notes
- Environment: `python -m venv .venv` → `source .venv/bin/activate` (analogous to `node_modules`).
- Packages: `pip install X`; record with `pip freeze > requirements.txt`.
- Configuration: `.env` (git-ignored) loaded via `python-dotenv` (`from dotenv import load_dotenv`).
- Imports: `from helpers import thing` — module names, no `./` prefix and no `.py` extension.
- Generators: `yield` streams values lazily, one at a time.

## Gotchas
- Keep `.env` git-ignored; commit only `.env.example`.
- Imports are module names, not file paths — no `./`, no extension.
- A `yield` function returns a generator and does not run until iterated.
