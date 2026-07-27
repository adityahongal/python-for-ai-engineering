# 01 — Syntax reflexes

Core syntax: output, variables, blocks, conditionals, loops.

## Notes
- `print(...)` and f-strings: `f"Hi {name}, {count}"`.
- Variables are plain assignments — no `const`/`let`, no `;`.
- Blocks are defined by indentation and a trailing `:` — `if` / `elif` / `else`.
- Loops: `for x in seq:` and `while cond:`; ranges via `range(n)`.

## Gotchas
- Indentation defines the block — 4 spaces, consistent (mixing tabs raises `IndentationError`).
- Every block header ends in `:`.
- `True` / `False`, not `true` / `false`.
