# NOTES.md — Python for AI Engineering

Reference notes, framed from a JavaScript background. Covers the syntax transfer map, the memory /
GIL model, the Python-vs-Node comparison, and a consolidated caveats list.

---

## §0 — Why Python for AI

Python is comparatively slow in raw loops, yet dominates AI/ML because the heavy computation does not
run in Python — `numpy` / `torch` drop into compiled C / C++ / Fortran / CUDA. Python is the
orchestration layer; the hot path is native. This gives near-native compute speed with high-level
readability. Reinforced by an unbreakable library network effect (papers ship Python) and a fast
experiment loop (REPL + Jupyter).

---

## §1 — JS → Python syntax map

| Concept | JavaScript | Python |
|---|---|---|
| Declare | `const x = 5;` | `x = 5` (no const/let, no `;`) |
| Interpolate | `` `Hi ${n}` `` | `f"Hi {n}"` |
| Array / List | `[1,2,3]` | `[1, 2, 3]` |
| Object / Dict | `{a: 1}` → `o.a` | `{"a": 1}` → `o["a"]` |
| Missing key | `o.x ?? d` | `o.get("x", d)` |
| map/filter | `arr.map(f)` | `[f(n) for n in arr]` |
| Function | `function f(){}` / `=>` | `def f():` |
| Default arg | `f(a, b=2)` | `def f(a, b=2):` |
| Loop | `for (const n of arr)` | `for n in arr:` |
| Null check | `x === null` | `x is None` |
| Literals | `true/false/null` | `True/False/None` |
| `this` | `this.name` | `self.name` (explicit 1st param) |
| Constructor | `constructor()` | `__init__(self)` |
| Async | `async/await` | `async def` / `await` (asyncio, opt-in) |

Idioms with no direct JS equivalent to internalize: f-strings, list/dict comprehensions, `dict["k"]`
vs `.get()`, indentation blocks + `:`, explicit `self`, keyword arguments at the call site,
`*args`/`**kwargs`.

```python
[n * 2 for n in nums if n > 1]          # comprehension = map + filter
ChatOpenAI(temperature=0, model="gpt-4")  # keyword args, common in library APIs
```

---

## §2 — Memory: Python vs JS vs C++

| Aspect | C++ | JavaScript | Python |
|---|---|---|---|
| Frees memory | manual (`new`/`delete`, smart ptrs) | tracing GC (V8) | reference counting + cycle collector |
| Variable holds | value / raw pointer | primitive by value, object by ref | a name bound to an object (all objects) |
| Overhead | lowest | low-ish | highest (header + refcount per object) |
| Trade-off | control + footguns | leaks via lingering refs | the GIL |

C++ gives control and responsibility; JS and Python both automate cleanup, differing in mechanism —
JS tracing GC vs Python reference counting (an object counts the names pointing at it; at zero it is
freed immediately, with a backup collector for reference cycles).

**GIL:** CPython executes one thread of Python bytecode at a time, so threads do not provide true CPU
parallelism. Options: `multiprocessing`, or numeric libraries that release the GIL and run C/CUDA in
parallel. The higher per-object memory cost is immaterial for AI work because large arrays live in
contiguous native NumPy/PyTorch buffers rather than as many Python objects.

---

## §3 — Python vs Node.js

| | Node.js | Python (CPython) |
|---|---|---|
| Engine | V8 (JIT) | CPython interpreter (bytecode) |
| Default posture | async, non-blocking (event loop) | synchronous, blocking; `asyncio` opt-in |
| Concurrency | event loop + libuv pool | threads (GIL), `asyncio`, `multiprocessing` |
| Sweet spot | real-time web, APIs, full-stack JS | data, AI/ML, scripting, science |
| Packages | `npm` + `package.json` | `pip` + `requirements.txt` |
| Env isolation | `node_modules` | `venv` |

Node's posture is non-blocking by default; Python runs top to bottom and blocks by default, which
suits data/AI work (processing a dataset or calling an LLM sequentially). `venv` is the analogue of
`node_modules`.

Neither runtime "starts a server" on its own: `node app.js` exits unless the code calls `.listen()`;
`python app.py` runs and exits unless a web framework is started. AI work is predominantly scripts and
notebooks that execute and finish.

---

## §4 — Tooling & running Python

- Interpreter: install a current Python via Homebrew (`brew install python`) rather than macOS's
  bundled `/usr/bin/python3` (old, OS-owned). Brew installs to `/opt/homebrew/bin/python3` and puts its
  `bin` first on `PATH`, shadowing the system one.
- `python3` vs `python`: use `python3` / `pip3` outside an environment (bare `python` may be absent or
  point at Python 2). Inside an active virtual environment, bare `python` / `pip` map to that env.
- REPL: `python3` opens the interactive `>>>` prompt (Read–Eval–Print Loop) and auto-prints each
  expression; `exit()` or Ctrl-D to leave. A `.py` file must call `print()` explicitly.
- Run a file: `python3 file.py` — executes top to bottom and exits (no ambient server).
- Package management (npm → Python): `pip` = installer, PyPI = registry, `requirements.txt` /
  `pyproject.toml` = declared deps, `.venv/` = installed packages (per-project, git-ignored).
- Virtual environment: `python3 -m venv .venv` → `source .venv/bin/activate` (prompt shows `(.venv)`),
  `deactivate` to exit. Unlike Node's automatic `node_modules`, Python installs globally unless a venv
  is active.
- Tracebacks: read bottom-up — the last line is the error type + message (the answer), the line above
  is where (file + line), the middle frames are the call path. Execution stops at the first unhandled error.

---

## §5 — Caveats

- Indentation defines the block — 4 spaces, consistent. A colon `:` opens every block
  (`if`/`for`/`def`/`class`). Mixed tabs/spaces raise `IndentationError`.
- `dict["missing"]` raises `KeyError`; use `.get("missing", default)` when a key may be absent.
- `self` is the explicit first parameter of every method.
- `True` / `False` / `None` are capitalized; use `is None` for identity checks.
- Mutable default arguments are evaluated once and shared across calls — use `None` and assign inside.
- `except`, not `catch`; match the exception type rather than catching everything.
- Type hints are not enforced at runtime — Pydantic or mypy performs validation.
- Read tracebacks bottom-up; the last line is the actual error and its type.
- `/` is float division (`10 / 3 → 3.33…`); `//` is floor division (`10 // 3 → 3`). `*` repeats
  strings/lists; `**` is exponent and raises `TypeError` on strings.
