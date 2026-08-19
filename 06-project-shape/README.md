# 06 — Project shape

Environments, configuration, imports, files, JSON, and generators — the structure of a real project.

## Notes

**Modules & imports**
- Any `.py` file is a module; `from utils import greet` imports by module name (no `./`, no `.py`).
  Everything top-level is importable — no `export` keyword. Python searches the script's own directory first.
- Importing a module runs its top-level code once and caches bytecode in `__pycache__/`
  (auto-generated, git-ignored; only imported modules get cached, not the run file).

**`__name__ == "__main__"`**
- A file's `__name__` is `"__main__"` when run directly, or its module name when imported.
- Wrap demo/entry code in `if __name__ == "__main__":` so importing the file has no side effects.

**Files & paths**
- `with open(path) as f:` is a context manager — it auto-closes the file at block end, even on error.
- A bare `open("x.txt")` is relative to the current working directory, not the file — use
  `Path(__file__).parent / "x.txt"` (pathlib) for a location-independent path. Pass `encoding="utf-8"`.
- Modes: `"r"` read (default), `"w"` write (erases & rewrites), `"a"` append, `"x"` create.

**JSON**
- `json.load(f)` / `json.dump(obj, f)` for files; `json.loads(s)` / `json.dumps(obj)` for strings
  (the string forms are what you use on LLM responses). `indent=4` pretty-prints for humans.
- Path: JSON file → dict → `Model(**data)` (Pydantic validate) → `model_dump()` → clean dict.
- Pydantic ignores unknown fields by default (a filter); `extra="allow"` keeps them, `extra="forbid"` rejects.

**Generators**
- A `yield` function returns a generator and doesn't run until iterated; each step runs to the next
  `yield` then pauses (remembering state). Lazy — flat memory. This is how LLM token streaming works.

**Config & secrets**
- Keep secrets in `.env` (git-ignored; commit only `.env.example`). `load_dotenv()` + `os.getenv("KEY")`
  load them. Never print full keys; never commit `.env`.

## Gotchas
- Imports are module names, not file paths — no `./`, no extension.
- Importing a module runs its top-level code — guard demo code with `if __name__ == "__main__":`.
- `open()` relative paths resolve from the CWD, not the file → `FileNotFoundError` from other dirs.
  Use `Path(__file__).parent / name`.
- `"w"` erases the whole file before writing.
- A `yield` function returns a generator and does not run until iterated.
- Never commit `.env`; commit `.env.example`.

## Files
- `utils.py` — helper module (`greet`, `add`) imported by `main.py`.
- `main.py` — imports from `utils`, the `__main__` guard, `with open` + `pathlib` path, JSON
  load/modify/dump into a Pydantic model, a `yield` generator, and `.env` loading via `python-dotenv`.
- `notes.txt`, `sample.json` — sample data read/written by `main.py`.
- `.env.example` — template for local `.env` (real `.env` is git-ignored).
