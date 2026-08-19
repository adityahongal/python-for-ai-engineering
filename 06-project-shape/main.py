# If I run this project, where does execution start?
# "python main.py"
# main.py will coordinate everything.

# utils.py - This is our helper/library module.
# Instead of putting every function inside main.py, we separate reusable functions.

# Python looks in the script's own directory first

# A Python file can become a module that another Python file imports.
# our main.py
#      ↓
# imports something
#      ↓
# that something lives somewhere else

from utils import greet, add                        #Go find the Python module named utils and give me the greet function from it

# print(greet("XXX"))

# print(add(10,490))

# Now we're going to ask Python:
# "Am I running main.py directly, or has somebody imported me?"

# Python answers that through:

# __name__

print("main.py is running")
print(__name__)                               # gives output as __main__

if __name__ == "__main__":                    # runs only if its __main__
      print(greet("XXX"))
      print(add(10, 490))

if __name__ == "__main__":
    print("I am running directly")

# Why "__main__"?

# When you run:
# python main.py

# Python is saying:
# "This is the file the user explicitly told me to run."

# So Python gives that file:
# __name__ = "__main__"

# When we run: python main.py
# Python treats the two files differently:

# main.py
#    ↓
# directly executed
#    ↓
# __name__ = "__main__"


# utils.py
#    ↓
# imported by main.py
#    ↓
# __name__ = "utils"

# CONTEXT MANAGERS

# We want Python to:
# open file
#    ↓
# use file
#    ↓
# automatically close file

# Instead of manually doing:
# f = open(...)
# # use it
# f.close()

# we'll use:
# with open(...) as f:
#     # use it

from pathlib import Path                                    # importing Python's path-handling utility.

notes_path = Path(__file__).parent / "notes.txt"

# if __name__ == "__main__" :
#      with open("notes.txt") as f:
#           content = f.read()
# print(content)

# why not just open("notes.txt")?
# A bare "notes.txt" is a RELATIVE path: Python resolves it from the current working
# directory (where you LAUNCHED python), NOT from where this file lives. Run from the
# repo root or via VSCode's ▶ Run button and the cwd is the workspace root, so
# "notes.txt" isn't there → FileNotFoundError.
#
# Building the path from the SCRIPT's own location fixes it for good, piece by piece:
#   __file__               -> path to THIS file        (.../06-project-shape/main.py)
#   Path(__file__)         -> wrap it as a Path object (pathlib)
#   Path(__file__).parent  -> the FOLDER holding it    (.../06-project-shape)
#   .parent / "notes.txt"  -> join the filename onto that folder
#   => .../06-project-shape/notes.txt  — an absolute path that works from ANYWHERE.
#
# Note: the "/" is NOT division here — pathlib overloads it to mean "join path parts"
# (cleaner than the older os.path.join). This is THE pattern for loading files in real
# projects — and later, documents in a RAG pipeline.

# with open(notes_path) as f: means ->Open notes.txt, temporarily give me the file object as f, and automatically clean it up when I'm finished.

if __name__ == "__main__":
    # encoding="utf-8" is a good habit: without it, Python uses the OS default,
    # which differs across machines (esp. Windows) and can garble non-ASCII text
    # (emojis, accents, LLM output). Being explicit keeps behaviour identical everywhere.
    with open(notes_path, encoding="utf-8") as f:
        content = f.read()

    print(content)

# - with is a context manager: it opens the file, and automatically closes it when the block ends
# — even if an error happens inside. No manual f.close(), no leaked file handles.

# JSON

# JSON is how LLMs, APIs, and config files move data. You'll load it → get a Python dict → feed it into a Pydantic model. 
# That's the whole LLM data path in miniature.
# Create sample.json

# The pipeline we're going to create is:
# sample.json
#     ↓
# json.load()
#     ↓
# Python dict
#     ↓
# modify dict
#     ↓
# Pydantic model
#     ↓
# validated data
#     ↓
# json.dump()
#     ↓
# sample.json

# {
#     "name": "Aditya",
#     "age": 27
# }
# This is data stored as JSON.

# Python After:
# data = json.load(f)

# we get:
# {
#     "name": "Aditya",
#     "age": 27
# }
# That's a Python dictionary.

# Then:
# user = User(**data)

# turns that dictionary into a validated Pydantic model.

import json

json_path = Path(__file__).parent / "sample.json"

with open(json_path, encoding="utf-8") as f:
     data = json.load(f)                           # reads JSON text → Python dict

print(data)
print(type(data))            # <class 'dict'>
print(data["name"])

# now modifying the dict
data["age"] = 20
# data["city"] = "Bengaluru"

with open(json_path, "w", encoding="utf-8") as f:
      json.dump(data, f, indent=4)                  # writes the dict back as JSON text
# Run it, then open sample.json — the age should now be 20 and city is added

# load  = bring JSON into Python
# dump  = send Python data into JSON

# "w" — write - the file mode - erases the whole file and writes fresh; creates it if missing
# "a" - append - keeps existing content, adds to the end
# "x" - create - fails if the file already exists

# indent=4 = pretty-print → human-readable formatting for json.dump/dumps

# - json.load(f) / json.dump(obj, f) → work with a file (note the f).
# - json.loads(s) / json.dumps(obj) → work with a string (note the s — we'll use these on LLM responses, which arrive as text)

from pydantic import BaseModel
  
class User(BaseModel):
      name: str
      age: int
      email: str
      
user = User(**data)          # dict → validated model (Day-5 unpacking)
print(user)
print(user.model_dump())     # model → clean dict again


# Generators (yield)

# A generator produces values one at a time, lazily — instead of building a whole list in memoryup front. 
# This is literally how LLM token streaming works

# The key new keyword is: "yield" same as we used "return"
# return
#   ↓
# "Here is the result. I'm finished."

# yield
#   ↓
# "Here is one result.
# Pause me.
# Come back when you need the next one."

# add a generator function:
import time

def count_up_to(n):
    i = 1
    while i <= n:
        yield i          # hand back ONE value, then PAUSE here until asked for the next
        i += 1  

# Using it
for num in count_up_to(5):
     print(num)
     time.sleep(0.2)            # mimics tokens arriving one by one

# .env
# - Secrets live in .env (git-ignored — never committed), and load_dotenv() + os.getenv() pull them in

import os

from dotenv import load_dotenv

load_dotenv()                              # reads .env into environment variables
key = os.getenv("EXAMPLE_API_KEY")         
print("Key loaded:", key[:6] + "..." if key else "NOT FOUND")   # masked — never print full keys