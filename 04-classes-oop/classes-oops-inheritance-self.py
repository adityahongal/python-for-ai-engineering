"""04 — Classes & OOP: __init__, self, methods, inheritance (super/override), class vs instance attributes, __str__."""

# Python Classes and OOPS

# The syntax skeleton
  
# class ClassName:                       # class definition (PascalCase name)
#       def __init__(self, param1, param2):   # constructor — runs at creation
#           self.attr1 = param1               # instance attributes (per-object data)
#           self.attr2 = param2   
  
#       def some_method(self):                # method — self is ALWAYS the first param
#           return f"{self.attr1} {self.attr2}"
  
# obj = ClassName("a", "b")   # create an instance (no `new`)
# print(obj.some_method())    # call a method → "a b"
# print(obj.attr1)            # read an attribute → "a"


class Dog :
    def __init__(self,name):                            # constructor — runs when you create a Dog, where self stores dog1,dog2 and name store jimmy,shiro
        self.name = name                                # store data ON this instance

    def bark(self):                                     # a method — self is ALWAYS the first param
        print(f"{self.name} says Woof WOOF!!")

    # __str__ controls how the object prints. Without it, print(dog1) shows
    # <__main__.Dog object at 0x...> (the memory address). print()/str() call it automatically.
    def __str__(self):
        return f"Dog(name={self.name})"

dog1 = Dog("Jimmy")                                     # create an instance (no `new` keyword like JS!)
dog2 = Dog("Shiro")

dog1.bark()
dog2.bark()

print(dog1)                                             # __str__ → Dog(name=Jimmy)
print(dog2)                                             # __str__ → Dog(name=Shiro)

class DogIntro :
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def intro(self):
        print(f"Hi my name is {self.name} and I'm a {self.breed}")

d1 = DogIntro("Jimmy","Golden Retriever")
d2 = DogIntro("Shiro","St Bernard")

d1.intro()
d2.intro()

# Inheritance

# in JS it's like --> class Puppy extends Dog {}
# in python ---> class Puppy(Dog):
#                      pass

# Parent
# class Dog:
#     def __init__(self, name):
#     self.name = name

# Child - super() exists here as well 
# class Puppy(Dog):
#     def __init__(self, name):
#         super().__init__(name)

# creating a new subclass caled puppy and inheriting its from parent class Dog

class Puppy(Dog):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def puppyIntro(self):
        print(f"{self.name} is a puppy and its age is {self.age}")

    # Parent Method overriding - inheritance of the parent method and overriding it
    def bark(self):
        print(f"{self.name} says yip yip")

puppy1 = Puppy("chinni",1)
puppy1.puppyIntro()
puppy1.bark()

# Instance attribute
# Every object gets its own value like dog1.name = Jimmy, dog2.name = Shiro
# seperate values

# Class attribute
# class Dog:
#     species = "Canine"
# every dog shares it --> Dog.species, dog1.species, dog2.species

class DogIntro2 :

    species = "Canine"                                  # class attribute - shared by all

    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def intro(self):
        print(f"Hi my name is {self.name} and I'm a {self.breed}")

d1 = DogIntro2("Jimmy","Golden Retriever")
d2 = DogIntro2("Shiro","St Bernard")

print(DogIntro2.species)  # Access through class
print(d1.species)         # Access through object
print(d2.species)

# Mutable Class Attribute Trap

class DogProfile:
    # Mutable class attribute
    # This single list is shared by ALL DogProfile objects
    tricks = []

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def add_trick(self, trick):
        # Appends to the shared class-level list
        self.tricks.append(trick)

    def intro(self):
        print(f"Hi, my name is {self.name} and I am a {self.breed}")


# Create two separate dog objects
d1 = DogProfile("Jimmy", "Golden Retriever")
d2 = DogProfile("Shiro", "St Bernard")

# Add a trick only to Jimmy
d1.add_trick("Sit")

# Expected:
# Jimmy -> ['Sit']
# Shiro -> []
#
# Actual:
# Both dogs show ['Sit'] because they share the same
# class attribute 'tricks'
print("Jimmy's tricks:", d1.tricks)
print("Shiro's tricks:", d2.tricks)

# Verify that both objects reference the same list
print("Same list object?", d1.tricks is d2.tricks)

# the correct way is to place tricks[] inside so iit references its particular instances
class DogProfile:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

        # Instance attribute
        # A NEW list is created for every DogProfile object
        self.tricks = []

    def add_trick(self, trick):
        # Appends to this dog's own list
        self.tricks.append(trick)

    def intro(self):
        print(f"Hi, my name is {self.name} and I am a {self.breed}")


# Create two separate dog objects
d1 = DogProfile("Jimmy", "Golden Retriever")
d2 = DogProfile("Shiro", "St Bernard")

# Add a trick only to Jimmy
d1.add_trick("Sit")                #note : it only takes one trick at a time,if we want to add multiple tricks at one time use *args

# Jimmy's list is updated
print("Jimmy's tricks:", d1.tricks)

# Shiro's list remains unaffected
print("Shiro's tricks:", d2.tricks)

# Verify that each object has its own list
print("Same list object?", d1.tricks is d2.tricks)