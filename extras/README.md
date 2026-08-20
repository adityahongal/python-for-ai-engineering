# extras — supplementary references

Concept-only material outside the 00–07 core roadmap. Not required to start LangChain;
read when the need actually shows up.

## Files
- `async_concept.py` — async/await in Python vs JavaScript, and why it matters for I/O
  concurrency. Runnable demo contrasting sequential awaits (time ≈ sum) with
  `asyncio.gather` (time ≈ slowest call).

## Async — concept-only, deferred

- **Python is synchronous by default; async is opt-in.** Write `async def` / `await`, and start the
  event loop yourself with `asyncio.run(main())`. In JS the loop is always running — that explicit
  start is the main mental shift.
- Calling an `async def` does **not** run it — it returns a coroutine you must `await` or `asyncio.run()`.
- `await` = "pause here, let other tasks run, resume when ready" (same as JS). It's concurrency on one
  thread (cooperative), not parallelism.
- **Why it matters:** overlapping I/O. `asyncio.gather(...)` runs many awaits at once, so 10 LLM/API
  calls take about as long as the slowest one instead of the sum.
- **When to actually learn it:** concurrent LLM/API calls, or async FastAPI routes. FastAPI runs sync
  endpoints fine, so you can build real APIs before mastering `asyncio`. Don't front-load it.

```bash
python extras/async_concept.py
```
