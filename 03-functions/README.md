# 03 — Functions

Definitions, default and keyword arguments, variadics.

## Notes
- `def name(params):` with `return`.
- Default arguments: `def f(a, b=2):`.
- Keyword arguments at the call site: `f(a, b=3)` — common across library APIs.
- `*args` collects extra positional arguments (tuple); `**kwargs` collects extra named ones (dict).

## Gotchas
- Mutable default arguments are evaluated once and shared across calls — use `None` and assign inside
  (`def f(x=None): x = x or []`).
- Keyword arguments must follow positional arguments.
- A function without `return` yields `None`.
