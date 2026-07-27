"""01 — Syntax reflexes: FizzBuzz over 1–20 (if/elif ordering + modulo)."""

# sourcery skip: remove-redundant-if
for number in range(1, 21):                       # range is end-exclusive → 1..20
    # check "divisible by both" FIRST — if/elif is first-match-wins,
    # so the most-specific case must come before Fizz and Buzz.
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number} is FizzBuzz")
    elif number % 3 == 0:                          # % is modulo (remainder), same as JS
        print(f"{number} is Fizz")
    elif number % 5 == 0:
        print(f"{number} is Buzz")
    else:
        print(f"{number} is neither divisible by 3 nor 5")