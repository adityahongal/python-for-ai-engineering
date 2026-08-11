"""03 — Functions: definitions, arguments, return values, callbacks, and lambdas."""

# Functions in python
# def functionName():
# A colon ":" starts the block and indentation defines it (instead of braces "{}").

def hello():
    print("hello")
# hello()    

def greet(name):                                    #name is a parameter, "xyz" is an argument, "greet" is the function name
    return f"hello {name}"
# print(greet("xyz"));                                #greet("xyz") --> function call

# Program Starts
#         │
#         ▼
# Reads def greet
#         │
#         ▼
# Stores function in memory
#         │
#         ▼
# Moves on and Nothing is executed yet

#calling greet() causes
# Call greet()
#        │
#        ▼
# Create execution frame
#        │
#        ▼
# Run function body
#        │
#        ▼
# Destroy frame
#        │
#        ▼
# Continue program

#   1. Python pauses the current line and jumps into the function.
#   2. It creates a frame — a private workspace holding that function's local variables
#   (parameters live here).
#   3. It runs the body line by line.
#   4. When it hits return (or the function ends), it produces a value, throws away the 
#   frame, and jumps back to where you called it.
#   5. The caller resumes with that returned value.

# def square(n):
#       result = n * n       # ② frame created: local n = 3 → result = 9
#       return result        # ③ hand back 9, frame destroyed
      
# x = square(3)            # ① jump in with n=3 ... ④ x now = 9
# print(x)                 # ⑤ resume: prints 9

# The key word is blocking: the caller waits. Line ⑤ does not run until square fully
# finishes. That's synchronous execution — exactly the call-stack behavior you already
# know, minus the async machinery.

#Defining a function tells Python what code belongs to the function and stores it in memory.
#Calling a function executes that code.

# def greet1():
#     print("prints in after start")

# print("Start")

# greet1()

# print("End")

# def greet2():
#     print("Hello")

# print(greet2)                   # output is like <function greet2 at 0x1031628d0>,"<function"-This is a function object,"0x1031628d0>" - memory address

#functions can have multiple input params

# def add(a,b):
#     print(a+b)
# add(40,60)

# def introduce(name, city):
#     print("Name:", name)
#     print("City:", city)

# introduce("XYX", "Pune")

# FUNCTIONS with print() vs return() vs None

# print() displays a value on the screen.
# return sends a value back to the caller so it can be stored, reused, or further processed.

#using print() the value is lost
# 10 + 20
#    │
#    ▼
#   30
#    │
#    ▼
# Printed to screen
#    │
#    ▼
# Gone - The value is not handed back.

#output will be -
#90                     ->inside function it will be 90 but value will not be returned
#none                   -> so it will come as none

def add1(a,b):
    print(a+b)              
    
result1 = add1(30,60)

print(result1)

#using return() the value is stored
# 10 + 20
#    │
#    ▼
#    30
#    │
#    ▼
# Returned
#    │
#    ▼
# Stored in variable - The caller receives it.
#output will be 90 only

def add2(a,b):
    return a+b

result2 = add2(30,60)
print(result2)

# with print() we cant do x = add(10, 20) + 5
# cz it returns none and becomes x= none + 5 ---> Error

# with return() we can do x = add(10, 20) + 5
# it becomes x = 30 + 5 ====> o/p. 35

x = add2(10,20) + 5
print(x)

# Functions Without return

# def greet():
#    print("Hello")
#  there is no return

# Python effectively treats it as:
# def greet():
#     print("Hello")
#     return None

# Because every Python function returns something.
# If you don't specify a return value,
# Python automatically returns:   None

def greet3():
    print("Hello")

x1 = greet3()

print(x1)                       #o/p = Hello and None because x = None

# Multiple Returns

# A function can return multiple values.
# Python automatically creates a tuple.

def get_user():
    return "XYZ",26,"xyz@x.com"

data = get_user()
print(data)

# Callbacks

# Callback = a function passed as an argument to another function. 
# Python functions are first-class objects (just like JS), so you can pass them around:

def greet4(name):
      return f"Hi {name}"

def run_twice(fn, value):    # fn is a CALLBACK — a function received as an argument
      print(fn(value))
  
run_twice(greet4, "Sam")      # pass greet WITHOUT () — the function itself, not its 
#   result
#   ⚠️  Same trap as JS: pass greet (the function), not greet() (which calls it and passes
#   the result). Like setTimeout(fn) vs setTimeout(fn())

# Python's arrow-function equivalent is lambda function

# in JS
# const greet = (name) => `Hi ${name}`;
# console.log(greet("Sam")); // Hi Sam

# in python
# Python lambda can contain only a single expression:
# For anything more than a simple expression, Python uses a normal function:
greet5 = lambda: print("This is an anonymous lambda function")
greet5()

greet6 = lambda name: f"Hi {name}"
print(greet6("XXX"))
# note: assigning a lambda to a name works, but linters (Ruff E731) prefer a normal def for named functions

# Default arguments

# Default argument = a parameter given a fallback value, so the caller can skip it:
# Python lets you provide a default value.

# Non-default parameter first.
# Default parameter after.

def greet7(name,punct="!"):                                         # punct="!" -> If caller doesn't provide punct,use "!"
     print(f"Hello {name}{punct}")

greet7("AAA")
greet7("ZZZ","??")

# Keyword Arguments

# Python lets us explicitly name the parameters.
# create_user(
#     name="Aditya",
#     age=26,
#     city="Pune"
# )    

# ---> we can instantly read it as
# name = "Aditya"
# age = 26
# city = "Pune"

def user(name, age):
    print(name, age)

user(age=26, name="YYYY")

def user2(name, age):
    print(name, age)

user2("RRRR", age=26)          # here positional arg is "RRRR", keyword arg is "age=26"
# Always Positional arg is considered first then keyword arg, if vice versa then error 

# Positional Args vs Keyword Args

# def user3(name, age):
#     print(name, age)

# user3(name="Aditya", 26) 