"""02 — Collections: extended notes on lists, dicts, tuples, sets, and comprehensions."""

# lists - just like javascript array

nums = [1, 2, 3, 4, 5]

# nums.append(6)  #just like push at the end
# print(nums)

# data = ["xyz",25,True,89.6]     #list can store different types unlike typescript
# print(data)

# Indexing just like JS
fruits = ["apple", "banana", "orange", "jackfruit", "lemon"]
# print(fruits[1])

# Negative indexing - unique in python - gives last item in the list
# print(fruits[-1])
# print(fruits[-3])               #gives first item parsing from reverse

# Instead of slicing python has
# print(fruits[1:3])                  #start is included,ending is excluded

# print(fruits[:3])                   #gives first 3

# print(fruits[-2:])                  #gives last 2 #note: [-2:] instead of [-2] here

# print(fruits[:])                    #gives everything

# print(fruits[::-1])                 #reverses the list, note- fruits[::] is same list and fruits[::0] throws cannot be zero error

# fruits.insert(2,"mango")              #just like JS splice - arr.splice(index,0,item)
# print(fruits)

# instead of arr1.push(...arr2) in JS we have extend() in python
a = [1, 2]
b = [3, 4]
a.extend(b)
# print(a)

# Removes by value - remove()
# fruits.remove(2)                    #remove() removes an element by value, not by index so this will throw error
# fruits.remove("orange")               #removes the orange
# print(fruits)

# pop() - removes last element or removes element by index
# print(fruits.pop())
# print(fruits.pop(3))

# del - deletes element
# del nums[2]
# print(nums)

# clear() - empties the list
# nums.clear()
# print(nums)

# len(nums)           # length (a function, not .length)

# Checking Membership

# Instead of arr.includes("apple")
# membership → True   (clean 'in' operator)
# if "apple" in fruits:
#     print(True)

# LOOPING
# instead of JS's for(const fruit of fruits) we write
# for fruit in fruits:
#     print(fruit)                            #prints each fruit one by one

# Instead of arr.forEach((item,index)=>{}) - we use enumerate() with for loop - to print each item with its index

# for index, fruit in fruits:                         #note: enumerate(fruits) is missing here
#     print(index,fruit)
# Python tries to unpack each string into two variables
# for the 1st iteration - index, fruit = "apple" --> But "apple" contains 5 characters ('a', 'p', 'p', 'l', 'e'), not 2 values, so Python raises:
# ValueError: too many values to unpack (expected 2)

# So correct way --> If you want both the index and the item --> use enumerate()
# for index,fruit in enumerate(fruits):
#     print(index,fruit)

# ITERATION RULE
# a good rule of thumb is:

# for item in iterable: → iterate over items.
# for index, item in enumerate(iterable): → iterate over both indices and items.
# for key, value in dict.items(): → iterate over dictionary key-value pairs.

# useful list functions

# length -> len(fruits)
# sort -> nums.sort()
# reverse ->    nums.reverse()
# Maximum ->    max(nums)
# Minimum ->    min(nums)
# Sum ->        sum(nums)

# Copying ->

# wrong method ->  Both point to the same list
# a = [1,2,3]
# b = a

# Correct method ->
# b = a.copy() or b= a[:]
# print(a)

# Tuples - Tuple is like a list but immutable.

# point = (10,20)
# point[0] = 100        #cannot do throws TypeError - does not support object assignment

# Why use tuple? --> Because values should never change.
# Examples
# Co-ordinates --> location = (18.52,73.85)
# RGB color --> color = (255,0,0)
# database row --> user = (1,"Aditya",24)

# Single element tuple
# x = (5)                             # this becomes an integer
# print(x)

# x = (5,)                            # this becomes tuple
# print(x)

# Tuple unpacking just like JS destructuring -> const [name,age] = person
# person = ("abc",25,True)
# name,age,isDev = person

# print(name,age,isDev)

# Dict or Dictionary

# A dictionary stores key-value pairs just like JS object
# Dicts — objects, but keys use [ ]

user = {"name": "XYZ", "age": 24}

# print(user["name"])                     # reads but (KeyError if missing!)
# # print(user["city"])                     # "city" key doesnot exist so throws KeyError

# print(user.get("name"))                 # safe read
# print(user.get("city"))                 # if key doesn't exist output will display none instead of error
# print(user.get("email","N/A"))           # safe read with default

# user["age"] = 20                        # To update
# print(user)

# user["city"] = "Dubai"                  # To Add
# user["email"] = "user@x.com"
# print(user)

# del user["city"]                        # TO delete
# print(user.get("city"))

# Loop in dict

# for key in user:                           # To get only key
#     print(key)
# for value in user.values():                 # To get only value
#     print(value)
# for key, value in user.items():             # To get both
#     print(key, value)

# Nested Dict
# student = {
#     "name": "Aditya",
#     "marks": {
#         "math": 95,
#         "english": 88
#     }
# }

# print(student["marks"]["math"])
# print(student["marks"])


# COMPREHENSIONS
# Instead of writing loops, you can create collections in one line.
# "give me EXPR for each x in SEQ (optionally where COND)."

# // JavaScript
#   nums.map(n => n * n)
#   nums.filter(n => n % 2 === 0)
#   nums.filter(n => n % 2 === 0).map(n => n * 2)

# Python — same result, one construct
#   [n * n for n in nums]
#   [n for n in nums if n % 2 == 0]
#   [n * 2 for n in nums if n % 2 == 0]

# Normal way -
# squares = []

# for i in range(5):
#     squares.append(i*i)

# print(squares)

# Python way - comprehension
# squares = [i * i for i in range(5)]
# print(squares)

# # With conditions
# # to print evens
# nums = [1, 2, 3, 4, 5]
# evens = [n for n in nums if n % 2 == 0]
# print(evens)

# doubled_evens = [n * 2 for n in nums if n % 2 == 0]
# print(doubled_evens)

# # Converting to upper case
# words = ["apple", "banana"]

# upper = [word.upper() for word in words]

# print(upper)


# Dict comprehension — same shape, but produces key: value:
# normal way
# square = {}

# for i in range(5):
#     square[i] = i*i

# Python way
# square = {i:i*i for i in range(10)}                         # note: square = {} in dict, not square = []
# print(square)

# Dict comprehension with condition
# square = { i:i*i for i in range(10) if i % 2 == 0 }
# print(square)

# Sets
# A set is an unordered collection of unique elements.
# set ← no JS equivalent (unordered, no duplicates)
numbers = {1, 2, 3, 3, 4, 5, 5}
print(numbers)  # duplicates 3,5 are automatically removed

# Creating set
# Method 1:
# fruits = {"apple", "banana", "orange"}

# Method 2: using set() constructor
# fruits = set(["apple", "banana", "orange"])

# Creating Empty Set
# empty = {}    --> Error : this creates dict not set
# empty = set()      --> correct method
# print(type(empty))

# usecase of set
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com", "b@gmail.com"]

unique = set(emails)

print(unique)

# Membership Testing
# One of the biggest advantages of sets.

# fruits = {"apple", "banana", "orange"}

# print("banana" in fruits)                           # True

# Time Complexity
# List  -> O(n)
# Set   -> O(1)            - very fast compared to list cz for list Python has to check elements one by one

# No indexing in Sets so ordering is not guaranteed

# A practical example you'll see in backend and AI code is removing duplicate IDs from API responses:
user_ids = [101, 102, 101, 103, 102]

unique_ids = list(set(user_ids))

print(unique_ids)

# Set Operations
# Python has clean operators for set math (in JS you'd write manual loops/filters).

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Union → everything in either set (duplicates dropped)
# print(s1 | s2)                # {1, 2, 3, 4, 5, 6}   (also s1.union(s2))

# Intersection → only elements in BOTH
# print(s1 & s2)                # {3, 4}               (also s1.intersection(s2))

# Difference → in s1 but NOT in s2
# print(s1 - s2)                # {1, 2}               (also s1.difference(s2))

# Symmetric difference → in either, but NOT both
# print(s1 ^ s2)                # {1, 2, 5, 6}         (also s1.symmetric_difference(s2))

# Subset / superset checks
# print({1, 2} <= s1)           # True  — {1,2} is a subset of s1
# print(s1 >= {1, 2})           # True  — s1 is a superset of {1,2}

# Add / remove elements
# s1.add(10)                    # add one element
# s1.discard(99)                # remove if present — no error when missing
# s1.remove(2)                  # remove — raises KeyError if the element is missing

# Real-world: shared tags between two articles
tags1 = {"python", "ai", "web"}
tags2 = {"ai", "ml", "python"}
# print(tags1 & tags2)          # {'python', 'ai'} — common tags

# Real-world: which incoming emails are NEW (not seen before)
seen = {"a@x.com", "b@x.com"}
incoming = {"b@x.com", "c@x.com", "d@x.com"}
# print(incoming - seen)        # {'c@x.com', 'd@x.com'} — only the new ones

# zip() pairs up two lists position-by-position
names = ["a", "b"]
ages = [25, 30]
zip(names, ages)  # → pairs: ("a",25), ("b",30)  — perfect for dict comprehensions
