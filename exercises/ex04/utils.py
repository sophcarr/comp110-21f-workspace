"""List utility functions."""

__author__ = "730320301"


# TODO: Implement your functions here.
def all(haystack: list[int], needle: int) -> bool:
    i: int = 0
    total: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            total += 1
        i += 1
    if total == len(haystack):
        return True
    else:
        return False


def is_equal(x: list[int], y: list[int]) -> bool:
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