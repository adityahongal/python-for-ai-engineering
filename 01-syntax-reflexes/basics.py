"""01 — Syntax reflexes: variables/types, conditionals, and loops."""

# 1. Variables & types — dynamic, like JS
  
# sourcery skip: while-to-for
name = "Aditya"     # str
age = 25            # int
height = 5.9        # float
is_dev = True       # bool  ← capitalized!

print(f"name-{name},age-{age},height-{height},developer:{is_dev}")

#2. Conditionals — mind three swaps

if age < 18: 
      print("minor")
elif age < 65:          # ← "elif", not "else if"
      print("adult")
else:
      print("senior")
# - else if → elif (one word).
# - Colon : + indented block instead of { }.
# - Logical operators are words: and / or / not — not && / || / !

number = 67
if number < 0:
    print(f"{number} is a negative number")
elif number == 0:
    print(f"{number} is zero")
else:
     print(f"{number} is positive")

#3. Loops — there's no C-style for
# Python has no for (let i=0; i<n; i++). You loop over things:

for i in range(5):              # range(5) → 0,1,2,3,4 (end-exclusive)
    print(f"{i}")

for char in "hi":               # strings are iterable — loop yields each character
     print(char)

count = 10
while count > 0:                # counts down: 10, 9, ... 1
     print(count)
     count -= 1                 # Python has -=, +=  (but NO ++ / --)