# TypeHints

# Without Type Hints:

# def greet(name):
#     return f"Hello {name}"
# Python doesn't tell us what name should be.

# With Type Hints:

def greet(name:str) -> str:
    return f"hello {name}"
print(greet("ABC"))
# read as ---- name should be a string
#              function returns a string

# Note --- Type hints are hints. Not enforcement.

print(greet(123))        # ← a NUMBER, not a str. Does Python complain?
print(greet(["a","b"]))  # ← a list.
# These print without failing

# Basic Type Hints

# String
# name: str = "Aditya"

# Integer
# age: int = 27

# Float
# price: float = 99.99

# Boolean
# is_active: bool = True

# List

# names: list[str] = [
#     "Aditya",
#     "Sam"
# ]

# Meaning:
# List containing strings

# Dictionary

# scores: dict[str, int] = {
#     "math": 95,
#     "science": 90
# }

# Meaning:
# key = string
# value = integer


# Optional Values

# Suppose email may exist or may not exist.
# email: str | None

# Function Return Types

# def add(a: int, b: int) -> int:
#     return a + b

# Reads as:
# takes two integers
# returns an integer

# Type hints
#     ↓
# "I'm telling Python/developers what I expect" - it isn't enforcing yet
#     ↓
# Pydantic
#     ↓
# "I'm actually validating the data" - enforced validation before runtime
# Pydantic gives us runtime validation