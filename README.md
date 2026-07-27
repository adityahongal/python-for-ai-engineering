# python-for-ai-engineering

Python reference notes, oriented toward AI / LLM engineering, from a developer with a JavaScript, React, and Node/MERN background.

The material is framed as a transfer from JS: syntax mappings, the memory and concurrency model, a Python-vs-Node comparison, and the practical caveats that matter in day-to-day work.

> Companion to [`gen-ai-learnings`](https://github.com/adityahongal/gen-ai-learnings) (LangChain / RAG / agents) and the full-stack work in [`nodejs-playground`](https://github.com/adityahongal/nodejs-playground) and [`Jobtracker-MERN`](https://github.com/adityahongal/Jobtracker-MERN).

## Reference notes

**[`NOTES.md`](./NOTES.md)** is the core reference — the JS→Python syntax map, the memory / GIL model, the Python-vs-Node comparison, and a consolidated caveats list.

## Running Python

Python runs a file top to bottom and exits — there is no ambient server. A long-running process exists only when a web framework (FastAPI / Flask / Django) is started explicitly.

```bash
python -m venv .venv          # isolated environment (analogous to node_modules)
source .venv/bin/activate
python 01-syntax-reflexes/example.py   # run a file — like `node file.js`
python3                        # or the interactive REPL (>>>)
```

In VS Code: install the **Python** extension → `Cmd+Shift+P` → *Python: Select Interpreter* → select `.venv` → **▶ Run**. Add **Jupyter** for notebooks and **Ruff** for linting/formatting.

## Structure

Numbered folders group the material by topic. Each folder has a `README.md` with concise notes and a **Gotchas** section.

| Folder | Topic |
|---|---|
| `00-setup` | REPL, running files, VS Code, reading tracebacks |
| `01-syntax-reflexes` | print/f-strings, variables, indentation blocks, conditionals, loops |
| `02-collections-comprehensions` | lists/dicts/tuples/sets, `[]` vs `.get()`, comprehensions |
| `03-functions` | `def`, default & keyword args, `*args`/`**kwargs` |
| `04-classes-oop` | `class`, `__init__`, `self`, inheritance |
| `05-typehints-pydantic-errors` | type hints, Pydantic `BaseModel`, `try/except` |
| `06-project-shape` | venv, `.env`, imports, generators |
| `07-consolidation` | end-to-end example tying the topics together |
