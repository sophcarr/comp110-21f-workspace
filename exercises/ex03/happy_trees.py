"""Drawing forests in a loop."""

__author__ = "730320301"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
row: str = ""

i: int = 0

while i < depth:
    i = i + 1
    row = row + TREE
    if i < depth:
        row = row + ""
    print(row)