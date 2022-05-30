import numpy as np


# Prints out a multi dimensional numpy array as 􏰀→ one line
# Example: np.array([['a'], ['b'], ['c']]) --> 􏰀→ abc
def glow(snippet):
    for c in snippet:
        print(*c, end="")

newspaper = np.array(
    [
        [" ", "a", "p", "p"],
        ["b", "a", "n", "a"],
        ["t", "o", "m", "t"],
        ["c", "u", "c", "a"],
        ["l", "e", "s", "e"],
        ["p", "r", "e", "s"],
        ["c", "a", "r", "s"],
        ["y", "e", "a", "r"],
    ]
)

snippet1 = newspaper[2:5, -1:][::-1]
snippet2 = newspaper[0, :]
snippet3 = newspaper[4, :-1]

# Output :- `eat apples`
