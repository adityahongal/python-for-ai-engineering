# utils.py - This is our helper/library module.
# Instead of putting every function inside main.py, we separate reusable functions.
# One Python file can provide functions to another Python file.

# 06/
# ├── utils.py   ← reusable functions
# └── main.py    ← uses those functions

def greet(name):
    return f"Hello {name}"

def add(a,b):
    return a + b

print("utils.py is running")
print(__name__)