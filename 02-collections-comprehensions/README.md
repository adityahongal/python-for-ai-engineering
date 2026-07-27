# 02 — Collections & comprehensions

Lists, dicts, tuples, sets, and comprehensions — the backbone of most data and LLM code.

## Notes
- `list` `[...]` (array), `dict` `{"k": v}` (object), `tuple` `(a, b)` (immutable), `set` `{a, b}` (unique).
- Access: `list[0]`, `dict["k"]`; `dict["missing"]` raises — use `dict.get("k", default)`.
- List comprehension = map + filter: `[f(n) for n in seq if cond]`.
- Dict comprehension: `{k: v for k, v in pairs}`.

```python
[n * 2 for n in nums if n > 1]
{name: len(name) for name in names}
```

## Gotchas
- `dict["missing"]` raises `KeyError`; `.get()` is the safe read.
- Comprehension order reads as `expr` first, then `for`, then `if`.
- Tuples and strings are immutable; string methods return new strings.
