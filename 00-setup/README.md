# 00 — Setup & mechanics

Running Python, the REPL, VS Code, and reading errors.

## Notes
- Install: `brew install python`; verify with `python3 --version`.
- REPL: `python3` opens `>>>` (analogous to Node's `>`); exit with `exit()` or Ctrl-D.
- Run a file: `python3 example.py` — executes top to bottom and exits. No server.
- VS Code: Python extension → `Cmd+Shift+P` → *Select Interpreter* → `.venv` → **▶ Run**.
- Environment: `python -m venv .venv && source .venv/bin/activate`.

## Gotchas
- Read tracebacks bottom-up — the last line is the real error.
- `python` vs `python3` (and `pip` vs `pip3`) — know which the shell resolves to.
- An unactivated `.venv` installs packages into global Python.
