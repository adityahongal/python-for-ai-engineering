# 05 — Type hints, Pydantic, error handling

Type annotations, runtime validation with Pydantic, and exceptions. The basis for structured LLM output.

## Notes
- Type hints: `name: str`, `age: int`, `-> bool`. Documentation and tooling; not enforced at runtime.
- Pydantic `BaseModel`: a schema class that validates and coerces data at runtime and raises on bad input.
- Exceptions: `try: ... except SomeError as e: ...` (note `except`, not `catch`).

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
```

## Gotchas
- `except`, not `catch`; matching the exception type avoids swallowing everything.
- Type hints are not enforced by Python — Pydantic or mypy performs the validation.
- Pydantic coerces where possible (`"25"` → `25`) and raises a `ValidationError` when it cannot.
