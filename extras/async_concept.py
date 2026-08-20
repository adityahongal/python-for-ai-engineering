"""
Async in Python — CONCEPT-ONLY reference (deferred).

This is NOT part of the 00–07 core roadmap. You do not need it to start LangChain,
and a basic FastAPI app runs fine with plain sync endpoints. Revisit this when you
actually need concurrency — e.g. firing many LLM/API calls at once, or writing
async FastAPI routes.

The idea vs JavaScript:
  - JS is async from birth: the event loop is always running, most APIs are async.
  - Python is SYNC by default; async is opt-in. You write `async def` / `await`,
    and you must START the loop yourself with `asyncio.run(...)`.
  - `await` means the same in both: "pause here, let other tasks run, resume when ready."
  - This is concurrency on ONE thread (cooperative), not parallelism.

Run:  python extras/async_concept.py
"""

import asyncio
import time


# An `async def` function is a COROUTINE. Calling it does NOT run the body — it
# returns a coroutine object. You must `await` it (or pass it to asyncio.run()).
async def fake_api_call(name, seconds):
    print(f"  -> start {name}")
    await asyncio.sleep(seconds)      # await: yield control while "waiting" (mimics a slow API/LLM call)
    print(f"  <- done  {name} ({seconds}s)")
    return f"{name} result"


# 1) SEQUENTIAL — await one, then the next. Total time ≈ the SUM of all waits.
async def run_sequential():
    start = time.perf_counter()
    await fake_api_call("A", 1)
    await fake_api_call("B", 1)
    await fake_api_call("C", 1)
    print(f"sequential took ~{time.perf_counter() - start:.1f}s\n")


# 2) CONCURRENT — start all three, await them together with asyncio.gather().
#    Total time ≈ the SLOWEST single call, not the sum. This is why async matters
#    for I/O: 10 LLM calls can overlap instead of running back-to-back.
async def run_concurrent():
    start = time.perf_counter()
    results = await asyncio.gather(
        fake_api_call("A", 1),
        fake_api_call("B", 1),
        fake_api_call("C", 1),
    )
    print(f"concurrent took ~{time.perf_counter() - start:.1f}s  ->  {results}\n")


async def main():
    print("SEQUENTIAL (one after another):")
    await run_sequential()
    print("CONCURRENT (all at once with asyncio.gather):")
    await run_concurrent()


if __name__ == "__main__":
    # asyncio.run() starts the event loop, runs main() to completion, then stops it.
    # In JS the loop is always running; in Python you start it explicitly — that is
    # the main mental shift for a JS dev.
    asyncio.run(main())

    # JS equivalent, for reference:
    #   async function main() { ... await ... }
    #   main();                       // loop already running, no explicit start
