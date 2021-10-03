"""List utility functions part 2."""

__author__ = "730320301"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    """Finding the even numbers in a list."""
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 != 0:
            xs.pop(i)
        i += 1
    return xs


def sub(a_list: list[int], y: int, z: int) -> list[int]:
    """Generating a list from a list."""
    final: list[int] = list()
    i: int = 0
    while len(a_list) == 0 or y == 0 or z <= 0:
        return final
    while i < (len(a_list)):
        final.append(a_list[i])
        i += 1
    if y >= 0:
        final.pop(0)
    if z <= len(a_list):
        final.pop(len(final) - 1)
    return final


def concat(x: list[int], y: list[int]) -> list[int]:
    """Joining lists together."""
    final: list[int] = list()
    i: int = 0
    s: int = 0
    while i < len(x):
        final.append(x[i])
        i += 1
    while s < len(y):
        final.append(y[s])
        s += 1
    return final
