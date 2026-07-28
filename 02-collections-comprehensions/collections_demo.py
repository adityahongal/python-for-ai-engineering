"""02 — Collections & comprehensions: the six task exercises."""

# 1. Squares: a list nums = [1,2,3,4,5] → a new list of their squares, using a list comprehension. Print it.
nums = [1,2,3,4,5]
squares = [ n*n for n in nums]
print(squares)

# 2. Evens only: from the same nums, a comprehension that keeps only even numbers (add an if). Print it.
evens = [ n for n in nums if n % 2 == 0]
print(evens)

# 3. Dict access: make a user dict with name and age. Read name with [], and read a missing email with .get() giving a default. 
# Print both — notice one would crash with [] and the other doesn't.
user = {"name": "XYZ", "age": 24}

print(user["name"]) 
# print(user.get["name"]) 
# print(user.get["email"])

print(user.get("name"))
print(user.get("email"))

# 4. Loop a dict: print each key/value of user using .items().

for key, value in user.items():
      print(key, value)

# 5. Dict comprehension + zip: given names = ["Aditya","Sam","Riya"] and 
# ages = [25,30,22], build {name: age} using a dict comprehension over zip(names, ages). 
# Print it.
names = ["Aditya","Sam","Riya"]
ages = [25,30,22]
name_to_age = {name:age for name,age in zip(names,ages)}           #create key:value pair and print it
print(name_to_age)

# 6. Dedupe: take a list with duplicates like [1,2,2,3,3,3] and get the unique values using set(). Print it.
dupes = [1,2,2,3,3,3,4,5,5]
dedupes = set(dupes)                            #converting it to set removes the duplicates and prints it
print(dedupes)