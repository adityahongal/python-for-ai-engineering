"""00 — Setup: an intentional NameError, for practicing how to read a traceback.

Read the output bottom-up: the last line is the error type + message (the answer),
the line above is where it happened. Python stops at the first unhandled error.
"""

print("about to break")
# result = undefined_variable + 1   # NameError: this name is never defined(uncomment to check this later)
print("you will never see this line")
