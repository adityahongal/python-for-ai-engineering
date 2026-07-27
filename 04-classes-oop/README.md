# 04 — Classes & OOP

Class definition, constructors, `self`, inheritance. Foundational for tools, agents, and Pydantic.

## Notes
- `class Dog:` with the constructor `__init__(self, ...)`.
- `this` maps to `self`, the explicit first parameter of every method.
- Instance attributes: `self.name = name`. Usage: `d = Dog("Rex"); d.bark()`.
- Inheritance: `class Puppy(Dog):` with `super().__init__(...)`.

## Gotchas
- Omitting `self` as the first method parameter raises `TypeError`.
- Attribute access inside a method needs the `self.` prefix.
- Methods and attributes live in the indented class body.
