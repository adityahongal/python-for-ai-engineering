# 00 — Setup & mechanics

Installing Python, the REPL, running files, virtual environments, and reading tracebacks.

## Notes

**Interpreter**
- Install a current Python via Homebrew: `brew install python` → Python 3.14 at
  `/opt/homebrew/bin/python3`. Preferred over macOS's bundled `/usr/bin/python3` (3.9, OS-owned).
- Homebrew's `bin` is first on `PATH`, so `python3` resolves to the new one; Apple's is shadowed.
- Use `python3` / `pip3` by default. Bare `python` may be absent or point at an old Python 2; it works
  only inside an active virtual environment.

**REPL**
- `python3` opens the interactive `>>>` prompt (Read–Eval–Print Loop) and auto-prints each result.
  `exit()` or Ctrl-D to leave. In a `.py` file, values must be printed with `print()` explicitly.
- First observations: `/` is float division (`10 / 3 → 3.33…`), `//` is floor division
  (`10 // 3 → 3`); `*` repeats a string (`"py" * 3 → "pypypy"`), `**` is exponent (errors on strings).

**Running a file**
- `python3 hello.py` runs top to bottom and exits — no server stays alive.

**Virtual environment**
- `python3 -m venv .venv` then `source .venv/bin/activate` (prompt shows `(.venv)`); `deactivate` to exit.
- Isolates this project's packages under `.venv/` (git-ignored), analogous to `node_modules` — but
  Python installs globally unless a venv is active.
- Package tooling maps to npm: `pip` = installer, PyPI = registry, `requirements.txt` = declared deps.

**Reading tracebacks**
- Read bottom-up: the last line is the error type + message (the answer); the line above is where
  (file + line); the middle frames are the call path. Execution halts at the first unhandled error.
  See `traceback_demo.py`.

## Gotchas
- `/usr/bin/python3` (system, 3.9) vs `/opt/homebrew/bin/python3` (yours, 3.14) — know which one `PATH` picks.
- Outside a venv, `python`/`pip` may not exist; use `python3`/`pip3`. Inside an active venv, bare
  `python`/`pip` work and point at the env.
- Forgetting to activate `.venv` installs packages globally.
- `**` on a string raises `TypeError` — `*` repeats, `**` powers.

## Files
- `hello.py` — a first runnable script.
- `traceback_demo.py` — an intentional `NameError` for practicing traceback reading.
