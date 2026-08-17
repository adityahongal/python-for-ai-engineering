# Pydantic
# A system that takes incoming data, checks it against a schema, and either gives you a valid object or an error.

# class Puppy(Dog): --> means Puppy inherits from Dog (Inheritance)
# Similarly: class User(BaseModel): --> means User inherits from BaseModel
# But BaseModel gives our class a lot of functionality automatically such as
# validation
# data parsing
# serialization
# error reporting

from pydantic import BaseModel


class User(BaseModel):                                      # Create a class called User that inherits from Pydantic's BaseModel.
    name: str
    age: int


# user1 = User(name="ABC", age="hello")                   # notice

# print(user1.name)
# print(user1.age)                                        # throws  Input should be a valid integer, unable to parse string as an integer - validation error
# print(type(user1.age))

# Pydantic Can Convert Data

# Pydantic isn't simply:
# correct → accept
# wrong → reject

# It can sometimes convert compatible data.

user2 = User(name="XYZ", age="27")                      #notice written as "27"

# Depending on the Pydantic configuration/version and type, Pydantic may convert:

# "27"
#  ↓
#  27
print(user2.age)                                      #converts and prints 27 

# Why This Is HUGE for GenAI

# Imagine asking an LLM:
# Extract the user's information.
# The LLM might return:

# {
#     "name": "John",
#     "age": 32
# }

# But another response might be:
# {
#     "name": "John",
#     "age": "thirty-two"
# }
# Or:
# {
#     "username": "John"
# }
# Or something completely unexpected.
# You don't want your application blindly trusting that output.

# So you define:
# class User(BaseModel):
#     name: str
#     age: int
# and validate the LLM's output against that structure.

# Conceptually:

# LLM
#  │
#  │ generates data
#  ↓
# Pydantic Model
#  │
#  ├── valid → ✅ continue
#  │
#  └── invalid → ❌ ValidationError

# This is the bridge to structured output.


# ------------------------------------------------------------------
# Pydantic reports ALL errors at once (the killer feature)
# ------------------------------------------------------------------

# Normal Python stops at the FIRST error it hits.
# Pydantic collects EVERY field that failed and reports them together.

# Here we break two things on purpose:
#   - name  -> missing entirely (required field not given)
#   - age   -> "oops" cannot be parsed into an int
#
# RUN this line and read the traceback bottom-up (Day-0 skill):
# you'll see "2 validation errors for User", listing BOTH fields.

# bad_user = User(age="oops")             # name missing + age invalid -> raises ValidationError
# print(bad_user)                          # never reached — the line above crashes first

# Expected output (2 errors, not 1):
#
# pydantic_core.ValidationError: 2 validation errors for User
# name
#   Field required ...
# age
#   Input should be a valid integer, unable to parse string as an integer ...
#
# Why this matters for GenAI: when an LLM returns messy JSON with
# several fields wrong, you see ALL the problems in one shot instead
# of fix -> rerun -> fix -> rerun.

# Right now a single bad field crashes our entire app. 
# In a real LLM pipeline, one messy response would take the whole thing down.
# instead of letting ValidationError crash the program, 
# we wrap it and handle it gracefully — print a friendly message, keep running.

# ------------------------------------------------------------------
#               try / except
# ------------------------------------------------------------------

# Create UserProfile
#        ↓
# Pydantic validates
#        ↓
#      ❌ invalid
#        ↓
# ValidationError
#        ↓
# except catches it
#        ↓
# Program continues

# The 4 Pieces of Error Handling
# try:
#     ...
# except:
#     ...
# else:
#     ...
# finally:
#     ...

# ValidationError is the specific exception Pydantic raises on bad data.
# (Imports normally live ONCE at the top of a file; they're repeated per
#  section here only to keep each learning block self-contained.)
from pydantic import ValidationError

try:                                                        # note: "try:" — no space before the colon (PEP 8)
    # user3 = User(name="FFF", age="70")
    user3 = User(name="FFF", age="seventy")
except ValidationError as e:                                #we can capture the error in "e" - means Give me the actual exception object and store it in e
    print("Bad data, skipping:", e)
    print(e.errors())                                       # printing a structured LIST of the errors, not just text
print("program continued ✅")


try:
    number = int("100")                         # here successfully converts the string
except ValueError:                              
    print("Invalid number")
else:                                           # else also runs when try succeeds.
    print("Successfully converted")
finally:
    print("Conversion attempt finished")        # always happens

# The flow is:

# try
#  ↓
# int("100") succeeds
#  ↓
# except ❌ skipped
#  ↓
# else ✅ runs
#  ↓
# finally ✅ runs

# try:
#     # risky operation
# except:
#     # operation failed
# else:
#     # operation succeeded
# finally:
#     # always happens

try:
    number = int("hello")                         # fails
except ValueError:                              
    print("Invalid number")                       # prints Invalid number
else:                                           # else is skipped here
    print("Successfully converted")
finally:
    print("Conversion attempt finished")        #finally is also printed

# finally means regardless of success or failure.
# So:
# Success → else → finally
# Failure → except → finally



from pydantic import BaseModel, ValidationError


class UserProfile(BaseModel):
    name: str
    age: int


try:
    user = UserProfile(
        name="Aditya",
        # age="99",
        age="hello"
    )

except ValidationError as e:
    print("Invalid user data")
    print(e)

else:
    print("User is valid")

finally:
    print("Finished")

# Sometimes you want to deliberately create an error.
# we use "raise" to throw an error
# used for our own validation/business rules in Python

def Withdraw(balance,amount):
    if amount > balance :
        raise ValueError("Insufficient Balance")                    #Stop here and throw an exception
    return balance - amount

# Withdraw(500,1500)

from pydantic import BaseModel, ValidationError


class UserProfile(BaseModel):
    name: str
    age: int
    email: str


data = {
    "name": "Aditya",
    "age": 27,
    "email": "aditya@example.com"
}


try:
    user = UserProfile(**data)

except ValidationError as e:
    print("Invalid user data")
    print(e)

else:
    print("User is valid")
    print(user)

finally:
    print("Finished")

print(type(data))            # <class 'dict'>                      — the raw input
print(type(user))            # <class '__main__.UserProfile'>      — the validated model
print(data is user)          # False — different objects. `is` checks IDENTITY (same object
                             # in memory), and a dict and a model are never the same object.
                             # `User(**data)` READS the dict and builds a NEW, separate model.


# ------------------------------------------------------------------
#           model_dump()  —  model  →  back to a plain dict
# ------------------------------------------------------------------

# A Pydantic model is perfect for VALIDATION at the edge of your app.
# But the rest of your code (web APIs, JSON responses, databases) usually
# wants a plain dict or JSON string, not a model object.
# model_dump() converts a validated model BACK into a normal dict.

#   raw dict  --User(**data)-->  validated model  --.model_dump()-->  clean dict
#   untrusted     (validate)        typed & safe       (export)      typed & safe

profile = UserProfile(name="Aditya", age="27", email="aditya@example.com")
# note: age was passed as "27" (a str) — Pydantic COERCED it to int 27 on the way in.

as_dict = profile.model_dump()               # -> {'name': 'Aditya', 'age': 27, 'email': '...'}
print(as_dict)
print(type(as_dict))                         # <class 'dict'>
print(as_dict["age"], type(as_dict["age"]))  # 27 <class 'int'>  — cleaned AND typed (not "27")

# Need JSON text instead (e.g. to send as an API response)? use model_dump_json():
as_json = profile.model_dump_json()          # -> '{"name":"Aditya","age":27,"email":"..."}'
print(as_json)
print(type(as_json))                         # <class 'str'>  — a JSON string, ready to send

# Why this matters for GenAI:
#   LLM text -> parse -> UserProfile(**data)  [VALIDATE]  -> .model_dump()  [CLEAN dict]
#   The rest of your app only ever touches a guaranteed-clean, typed dict —
#   never the raw, untrusted LLM output. That round-trip is the whole game.