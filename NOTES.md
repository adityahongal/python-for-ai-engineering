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

## §7 — Functions

- `def name(params):` + `return`; no `return` → returns `None` (there is no `undefined`).
- First-class objects: pass them as callbacks (pass `fn`, not `fn()`); `lambda x: expr` is the
  arrow-function form. Multiple return values pack into a tuple.
- Default args `def f(a, b=2):`; keyword args at the call `f(a, b=3)` (order-independent; positional
  before keyword). `*args` → tuple of extra positionals, `**kwargs` → dict of extra keywords; signature
  order is params → `*args` → `**kwargs`.
- Packing vs unpacking: `*args`/`**kwargs` gather in the definition; `*seq` / `**dict` spread at the call
  (`add(*[1,2,3])`, `f(**config)`).
- Scope is LEGB (Local → Enclosing → Global → Built-in): reading outer names is automatic; reassigning
  needs `global` / `nonlocal`.
- Type hints (`name: str -> int`) and docstrings (`"""..."""` as the first statement, readable via
  `.__doc__` / `help()`) document functions; hints are not enforced at runtime (Pydantic/mypy do that).

---

## §8 — Classes & OOP

- `class Name:` defines a blueprint; `Name(...)` creates an instance (no `new`). `__init__(self, ...)`
  is the constructor (optional); `self` is `this` but the EXPLICIT first parameter of every method
  (`obj.m()` runs as `Class.m(obj)`).
- Instance attributes `self.x = ...` are per-object; attributes in the class body are shared by all instances.
- Inheritance: `class Child(Parent):`; `super().__init__(...)` runs the parent constructor; redefining a
  method overrides it.
- Dunder methods customise behaviour — `__str__(self)` controls how the object prints.

---

## §9 — Type hints, Pydantic & error handling

- **Type hints** (`name: str`, `-> int`, `list[str]`, `dict[str, int]`, `str | None`) document intent
  for humans/tools but are NOT enforced at runtime — `greet(123)` with `name: str` still runs.
- **Pydantic `BaseModel`** turns hints into runtime validation. `class User(BaseModel):` inherits the
  machinery; creating `User(name=..., age=...)` validates the data against the annotations.
- **Coercion:** Pydantic converts compatible data (`age="27"` → `27`) but raises `ValidationError`
  when it can't (`age="seventy"`). It also reports EVERY failing field at once, not just the first.
- **`ValidationError`** (`from pydantic import ValidationError`) is the exception raised on bad data;
  `e.errors()` returns it as a structured list of dicts (type/loc/msg/input) — machine-readable, ideal
  for feeding an LLM's mistakes back to it.
- **`try / except / else / finally`** (JS `try/catch/finally`): `except SomeError as e:` catches;
  `else:` runs only when `try` succeeded; `finally:` always runs. Catch the specific type, not everything.
- **`raise ValueError("msg")`** throws your own error for business rules (e.g. withdraw > balance).
- **`Model(**data)`** unpacks a dict into a model (validate at the edge); **`model.model_dump()`** exports
  it back to a clean dict, **`model.model_dump_json()`** to a JSON string. Round-trip:
  `raw dict → Model(**data) [validate] → .model_dump() [clean, typed dict]`.
- **The GenAI bridge:** LLM text → parse → `Model(**data)` → valid object or catchable `ValidationError`.
  This is how LangChain guarantees structured output and retries on invalid responses.

---

## §10 — Project shape (modules, config, files, generators)

- **Modules & imports:** any `.py` file is a module; `from utils import greet` imports by MODULE NAME
  (no `./`, no `.py`). Everything top-level is importable — no `export` keyword. Python looks in the
  script's own directory first. Importing a module RUNS its top-level code once and caches bytecode in
  `__pycache__/` (auto-generated, git-ignored; only imported modules get cached, not the run file).
- **`__name__ == "__main__"`:** a file's `__name__` is `"__main__"` when run directly, or its module name
  when imported. Wrap demo/entry code in `if __name__ == "__main__":` so importing has no side effects.
- **Context managers (`with`):** `with open(path) as f:` auto-closes the file at block end (even on error)
  — no manual `.close()`. Same pattern for DB connections and API clients.
- **Robust file paths:** a bare `open("x.txt")` is relative to the CWD (where you launched python), not the
  file — breaks from other dirs or the VSCode ▶ Run button (→ `FileNotFoundError`). Use
  `Path(__file__).parent / "x.txt"` (pathlib; `/` joins path parts) for a location-independent path.
  Pass `encoding="utf-8"` explicitly for consistent text across machines.
- **JSON:** `json.load(f)` / `json.dump(obj, f)` for FILES; `json.loads(s)` / `json.dumps(obj)` for STRINGS
  (use the string forms on LLM responses). Modes: `"r"` read (default), `"w"` write (ERASES & rewrites),
  `"a"` append, `"x"` create. `indent=4` pretty-prints for humans (cosmetic; machines parse either).
- **Pydantic extra fields:** by default unknown fields are IGNORED/dropped — the model acts as a
  filter/cleaner. `model_config = ConfigDict(extra="allow")` keeps them; `extra="forbid"` raises. Handy for
  messy LLM output with more keys than the schema declares.
- **Generators (`yield`):** a `yield` function returns a generator object and does NOT run until iterated;
  each `next()`/loop step runs to the next `yield`, then PAUSES (remembering state). Lazy — never holds all
  values at once, so memory stays flat. This is how LLM token streaming works.
- **Secrets/config (`.env`):** keep secrets in `.env` (git-ignored; commit only `.env.example`);
  `load_dotenv()` + `os.getenv("KEY")` load them. Never print full keys; never commit `.env`.

---

## §11 — HTTP & APIs (the on-ramp to LLM calls)

- **`httpx`** is the HTTP client (like `fetch`/`axios`). `httpx.get(url)` sends a GET; `httpx.post(url,
  json=..., headers=...)` sends a POST. `pip install httpx`.
- **Response:** `response.status_code` (200 ok, 404 not found, 401 auth, 500 server); `response.json()`
  parses the JSON body into a Python dict.
- **`response.raise_for_status()`** turns a 4xx/5xx into an exception — a bad status is NOT an error by
  default in httpx, so call this to make `except` able to catch it (else `.json()` blows up later).
- **Error family:** `httpx.HTTPError` is the base covering both network failures (bad domain, timeout,
  no internet) and bad statuses (`HTTPStatusError`) — one `except` catches the whole family.
- **The LLM connection:** a Claude/OpenAI call is the SAME shape — `httpx.post` with the prompt in the
  JSON body and the API key in the headers → JSON response → parse → validate with Pydantic. The full
  pipeline: `GET/POST → JSON → Model(**data) [validate] → error-handled → model_dump() → save/use`.
- Nullable API fields (`name: null` → `None`) need `str | None` on the model, or Pydantic rejects them.

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
- Mutable default arguments (`def f(x=[])`) are created once and shared across calls — use `None`, build inside.
- Reassigning a global/enclosing variable inside a function needs `global`/`nonlocal` (else `UnboundLocalError`).
- Pass a callback as `fn`, not `fn()`; positional args cannot follow keyword args in a call.
- Every method needs `self` first (else `TypeError`); attribute access needs the `self.` prefix (else `NameError`).
- A mutable class attribute (`tricks = []` in the class body) is shared across all instances — put it in `__init__` as `self.tricks = []`.
- Never name a file the same as a package you import (`pydantic.py`) — it shadows the real package and imports break. On case-insensitive macOS, capitalisation is not a safe guard; use a distinct name.
- Pydantic coerces where it can (`"27"` → `27`) but raises `ValidationError` when it can't, and lists ALL failing fields at once — not just the first.
- `else:` runs only when `try` succeeds; `finally:` runs either way. `e.errors()` gives errors as structured data; `raise` throws your own.
- `model_dump()` → plain dict, `model_dump_json()` → JSON string. `Model(**data)` builds a NEW object, so `data is model` is `False`.
- Importing a module runs its top-level code once — guard demo/entry code with `if __name__ == "__main__":`.
- `open()` relative paths resolve from the CWD, not the file — use `Path(__file__).parent / name` to be location-independent.
- `"w"` mode ERASES the whole file before writing; read and write are separate `with` blocks.
- A generator doesn't run until iterated and yields one value at a time (lazy) — don't expect a list back.
- Pydantic ignores extra fields by default (`extra="forbid"` to reject, `"allow"` to keep).
- Never commit `.env` (keep it git-ignored); commit only `.env.example`. Never print full secrets.
