# 04 — Classes & OOP

Blueprints and instances: defining classes, constructors, methods, inheritance, and attribute scope.

## Notes

**Defining a class**
- `class Dog:` defines a blueprint; `Dog("Rex")` creates an instance (no `new` keyword).
- `__init__(self, ...)` is the constructor — runs at creation and sets up instance data. It's optional
  (a class with no `__init__` still instantiates).
- `self` is Python's `this`, but the EXPLICIT first parameter of every method. `rex.bark()` runs as
  `Dog.bark(rex)` — Python passes the instance in as `self`.
- Instance attributes: `self.name = name`. Reading them inside a method needs the `self.` prefix.

**Inheritance**
- `class Puppy(Dog):` subclasses Dog (JS `extends`). The child inherits the parent's methods.
- `super().__init__(...)` runs the parent constructor so inherited attributes get set.
- Redefining a method in the child OVERRIDES the parent's version for that subclass.

**Class vs instance attributes**
- A class attribute (`species = "Canine"` in the class body) is shared by all instances.
- An instance attribute (`self.x` in `__init__`) is unique per object.

**Dunder methods**
- `__str__(self)` controls how the object prints (`print(obj)` / `str(obj)`); without it you get
  `<__main__.Dog object at 0x...>`.

## Gotchas
- Every method needs `self` as its first parameter (else `TypeError`); attribute access needs the
  `self.` prefix (else `NameError`).
- A constructor with required params must be given them — `Dog()` raises `TypeError` if `name` is required.
- **Mutable class-attribute trap:** a mutable class attribute (`tricks = []` in the class body) is
  SHARED by all instances — put it in `__init__` as `self.tricks = []` for a per-object list. (Cousin
  of the Day-3 mutable-default bug.)

## Files
- `classes-oops-inheritance-self.py` — Dog/DogIntro classes, Puppy inheritance (super + override),
  class vs instance attributes, the mutable class-attribute trap and its fix, and `__str__`.
