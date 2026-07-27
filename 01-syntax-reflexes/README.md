# 01 — Syntax reflexes

Core syntax: output, variables, blocks, conditionals, loops — the everyday shape of Python.

## Notes

**Variables & types**
- Dynamic typing (like JS); no `let`/`const`. Common types: `str`, `int`, `float`, `bool`.
- `True` / `False` / `None` are capitalized. Inspect a value's type with `type(x)`.
- f-strings interpolate: `f"{name} is {age}"`.

**Conditionals**
- `if` / `elif` / `else`; each header ends in `:` with an indented body. `elif` is one word.
- Logical operators are words: `and` / `or` / `not` (not `&&` / `||` / `!`). Comparisons match JS.
- First-match-wins: the first true branch runs and the rest are skipped — order the most-specific case first.

**Loops**
- No C-style `for`. Iterate over things: `for i in range(5):` (end-exclusive → 0..4), `for ch in "hi":`.
- `while cond:` as usual. Compound assignment `+=` / `-=`; there is no `++` / `--`.
- Need the index while looping? `for i, x in enumerate(seq):`.

## Gotchas
- A header ending in `:` requires an indented block on the next line, or `IndentationError`.
- `if/elif/else` is first-match-wins — a value matching several conditions takes the first branch
  (the FizzBuzz trap: check "divisible by both" before the singles).
- `{ }` builds a set/dict, not a grouping — `print({x})` prints a one-element set `{x}`.
- `range(n)` stops at `n-1` (end-exclusive); `range(1, 21)` covers 1..20.
- No `++` / `--`; use `+= 1` / `-= 1`.

## Files
- `basics.py` — variables/types, conditionals, `for`/`while` loops.
- `fizzbuzz.py` — FizzBuzz over 1–20 (ordering + modulo).
