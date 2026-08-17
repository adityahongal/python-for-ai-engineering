# 05 — Type hints, Pydantic & error handling

Type annotations, runtime validation with Pydantic, and exceptions — the basis for
structured LLM output.

## Notes

**Type hints**
- `name: str`, `age: int`, `-> bool`, `list[str]`, `dict[str, int]`, `str | None`.
- Documentation for humans and tooling (editor, Ruff, mypy) — **not enforced at runtime**.
  `greet(123)` with `name: str` still runs.

**Pydantic**
- `class User(BaseModel):` inherits Pydantic's machinery (validation, parsing, serialization,
  error reporting) — same inheritance idea as `class Puppy(Dog)`.
- Creating `User(name=..., age=...)` validates the data against the field annotations.
- **Coercion:** converts compatible data (`age="27"` → `27`) but raises `ValidationError`
  when it can't (`age="seventy"`). Reports **every** failing field at once, not just the first.
- `Model(**data)` unpacks a dict into a model (validate at the edge of the app).
- `model.model_dump()` exports the validated model back to a clean dict; `model.model_dump_json()`
  to a JSON string. Round-trip: `raw dict → Model(**data) [validate] → .model_dump() [clean dict]`.

**Error handling**
- `try / except / else / finally` (JS `try/catch/finally`). `except ValidationError as e:` catches;
  `e.errors()` returns a structured list of the errors; `else:` runs only on success; `finally:` always.
- `raise ValueError("msg")` throws your own error for business rules.

**Why it matters:** LLM text → parse → `Model(**data)` → valid object or catchable `ValidationError`.
This is how a pipeline guarantees structured output and retries on invalid responses.

## Gotchas
- Type hints are not enforced by Python — Pydantic (runtime) or mypy (static) does the validation.
- Pydantic coerces where possible (`"27"` → `27`) and raises `ValidationError` when it cannot.
- Never name a file after a package you import (`pydantic.py`) — it shadows the real package and imports
  break. On case-insensitive macOS, capitalisation is not a safe guard; use a distinct name.
- `except`, not `catch`; match the specific exception type rather than swallowing everything.
- `else:` runs only when `try` succeeds; `finally:` runs either way.
- `Model(**data)` builds a NEW object, so `data is model` is `False`.

## Files
- `TypeHints.py` — type-hint syntax (str/int/float/bool, `list[str]`, `dict[str, int]`, `str | None`,
  return types) and a live demo that hints are not enforced.
- `Pydantic-demo.py` — `BaseModel`, coercion, `ValidationError` + `e.errors()`, `try/except/else/finally`,
  `raise`, `Model(**data)` unpacking, and `model_dump()` / `model_dump_json()`.
