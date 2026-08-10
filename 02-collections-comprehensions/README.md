# 02 — Collections & comprehensions

Lists, dicts, tuples, sets, and comprehensions — the backbone of most data and LLM code.

## Notes

**Types**
- `list` `[...]` (ordered, mutable), `dict` `{"k": v}` (key→value), `tuple` `(a, b)` (immutable),
  `set` `{a, b}` (unordered, unique). Empty `{}` is a dict; an empty set is `set()`.

**Lists**
- Index `xs[0]`, negative index `xs[-1]` (from the end), `len(xs)` (a function, not `.length`).
- Membership with `in`; slicing `xs[start:end]` (end-exclusive), `xs[::-1]` reverses.
- Methods: `append`, `extend`, `insert`, `remove` (by value), `pop` (by index/last), `sort`, `reverse`.
- Copy with `xs.copy()` or `xs[:]` — `b = a` only aliases the same list.

**Dicts**
- `d["k"]` raises `KeyError` if absent; `d.get("k", default)` is the safe read. `"k" in d` checks keys.
- Loop with `.items()` (key + value), `.keys()`, `.values()`.

**Iterating**
- Prefer `for i, item in enumerate(seq):` over `range(len(seq))`; `enumerate(seq, start=1)` sets the
  first index. Use `for k, v in d.items():` for dict pairs.

**Comprehensions**
- `[expr for x in seq if cond]` replaces `map`/`filter` in one construct.
- Dict comprehension: `{k: v for ...}`. `zip(a, b)` pairs two lists; unpack with two loop variables.
- The comprehension IS the loop — don't wrap it in an outer `for` (that rebuilds the result each pass).

**Sets**
- `set(xs)` removes duplicates; membership is O(1) vs O(n) for a list. Unordered, no indexing.
- Set math (operator or method form): union `|`, intersection `&`, difference `-`, symmetric
  difference `^`; subset/superset `<=` / `>=`. Mutate with `.add()`, `.discard()` (safe),
  `.remove()` (raises `KeyError`). Common uses: `tags1 & tags2` (shared), `incoming - seen` (new).

## Gotchas
- `d["missing"]` raises `KeyError`; use `.get()` when a key may be absent.
- Empty `{}` is a dict, not a set — use `set()` for an empty set.
- A comprehension already loops — wrapping it in a `for` rebuilds the whole result every iteration.
- Slicing and `range` are end-exclusive; negative indices count from the end (`xs[-1]` = last).
- Sets and dicts have no guaranteed display order — don't rely on element order.

## Files
- `collections_demo.py` — the six task exercises (comprehensions, dict access, zip, dedup).
- `lists_dicts_tuples_sets.py` — extended personal notes: indexing/slicing, list methods, tuples,
  nested dicts, comprehensions, and set operations/complexity.
