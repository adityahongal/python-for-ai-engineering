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

## §5 — Control flow, loops & operators

- Conditionals: `if` / `elif` / `else`, each header ending in `:` with an indented block. `elif` is one word.
- Logical operators are words: `and` / `or` / `not` (not `&&` / `||` / `!`); comparisons (`==`, `!=`, `<`, `>=`) match JS.
- `if/elif/else` is first-match-wins — the first true branch runs and the rest are skipped, so order the
  most-specific condition first (the FizzBuzz trap: test "divisible by both" before the singles).
- No C-style `for`: iterate over things — `for x in seq:`, `for i in range(n):` (end-exclusive),
  `for ch in "hi":`. Use `for i, x in enumerate(seq):` when the index is needed.
- `while cond:` as usual. Compound assignment `+=` / `-=` exists; there is no `++` / `--`.
- Truthiness matches JS: `0`, `""`, `[]`, `{}`, `None` are falsy.

---

## §6 — Collections & comprehensions

- Four types: `list` `[...]` (ordered, mutable), `dict` `{"k": v}` (key→value), `tuple` `(a, b)`
  (immutable), `set` `{a, b}` (unordered, unique). Empty `{}` is a dict; empty set is `set()`.
- Lists: `xs[0]`, negative index `xs[-1]` (from the end), `len(xs)` (function), `x in xs` membership,
  slicing `xs[start:end]` (end-exclusive), `xs[::-1]` reverse. `b = a` aliases; copy with `xs[:]` / `.copy()`.
- Dicts: `d["k"]` raises `KeyError` if absent; `d.get("k", default)` is the safe read. `"k" in d` tests
  keys. Loop with `.items()` (key+value), `.keys()`, `.values()`.
- Comprehensions: `[expr for x in seq if cond]` replaces `map`/`filter`; dict form `{k: v for ...}`.
  `zip(a, b)` pairs two lists, unpacked with two loop variables. The comprehension IS the loop — do not
  wrap it in an outer `for`.
- Iterating with an index: use `for i, item in enumerate(seq):` (not `range(len(seq))`); `enumerate(seq,
  start=1)` sets the first index. `for k, v in d.items():` for dict pairs.
- Sets: `set(xs)` dedupes; membership is O(1) vs O(n) for a list; unordered, no indexing.
- Set math (operator/method): union `|`, intersection `&`, difference `-`, symmetric difference `^`;
  subset/superset `<=` / `>=`. Handy for "shared" (`a & b`) and "what's new" (`incoming - seen`).

---

## Caveats

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
- A block header ending in `:` requires an indented body on the next line, or `IndentationError`.
- `if/elif/else` is first-match-wins — order the most-specific condition first.
- No `++` / `--`; use `+= 1` / `-= 1`. `{ }` with contents is a set/dict, not grouping.
- `range(n)` is end-exclusive (`range(1, 21)` → 1..20).
- A comprehension already loops — wrapping it in an outer `for` rebuilds the whole result each pass.
- Empty `{}` is a dict, not a set; use `set()`. Negative indices count from the end (`xs[-1]` = last).
