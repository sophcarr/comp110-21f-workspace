"""List utility functions."""

__author__ = "730320301"


# TODO: Implement your functions here.
def all(needle: int, haystack: list[int]) -> bool:
    """Matching up lists."""
    i: int = 0
    total: int = 0
    while i < len(haystack):
        if needle == haystack[i]:
            total += 1
        i += 1
    if total == len(haystack):
        return True
    else:
        return False


def is_equal(x: list[int], y: list[int]) -> bool:
    """Making sure lists are the same."""
    i: int = 0
    total: int = 0
    if len(x) != len(y):
        return False
    while i < len(y):
        if y[i] == x[i]:
            total += 1
        i += 1
    if total == len(x):
        return True
    else:
        return False


def max(input: list[int]) -> int:
    """Finding the max in a list."""
    i: int = 0
    max: int = input[len(input) - 1]
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    while i < len(input):
        first: int = input[i]
        if first > max:
            max = first
        i += 1
    return max
