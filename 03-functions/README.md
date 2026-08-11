# 03 — Functions

Defining and calling functions, arguments, return values, and the argument-collecting operators.

## Notes

**Definitions**
- `def name(params):` + `return`; a colon opens the block, indentation defines it.
- A function with no `return` gives back `None` (there is no `undefined`); so `x = print(...)` sets `x = None`.
- Functions are first-class objects — pass them as arguments (callbacks); pass `fn`, not `fn()`.
  `lambda x: expr` is the anonymous/arrow-function form (linters prefer `def` for named functions — Ruff E731).
- Multiple return values pack into a tuple: `return a, b` → `(a, b)`.

**Arguments**
- Default arguments: `def f(a, b=2):` — a parameter with a fallback.
- Keyword arguments at the call site: `f(a, b=3)` — matched by name, order-independent. Positional
  arguments must come before keyword arguments.
- `*args` collects extra positional arguments into a **tuple**; `**kwargs` collects extra named
  arguments into a **dict**. Signature order is fixed: normal params → `*args` → `**kwargs`.

**Packing vs unpacking**
- Packing: `*args`/`**kwargs` gather many values into one container (in the definition).
- Unpacking: `*seq` / `**dict` spread a container back into arguments at the call site
  (`add(*[1,2,3])`, `f(**config)`).

**Scope (LEGB: Local → Enclosing → Global → Built-in)**
- Reading an outer/global variable inside a function is automatic; **reassigning** one needs `global`
  (module level) or `nonlocal` (enclosing function), else you get `UnboundLocalError`.

## Gotchas
- **Mutable default arguments** (`def f(x=[])`) are created ONCE at definition and shared across every
  call — use `None` as the default and build the value inside.
- A function with no `return` yields `None`.
- Pass a callback as `fn`, not `fn()` (which calls it). Same trap as JS `setTimeout(fn)` vs `fn()`.
- Positional arguments cannot follow keyword arguments in a call → `SyntaxError`.
- Assigning inside a function makes the name local for the whole function → `UnboundLocalError` if read
  before assignment; declare `global`/`nonlocal` when you mean an outer variable.

## Files
- `functions.py` — def/return, print vs return vs None, multiple returns, callbacks, lambda, default &
  keyword args, positional vs keyword, `*args`/`**kwargs`, packing/unpacking, and the mutable-default bug.
