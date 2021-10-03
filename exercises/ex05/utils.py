"""List utility functions part 2."""

__author__ = "730320301"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    """Finding the even numbers in a list."""
    final: list[int] = list()
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            final.append(xs[i])
        i += 1
    return final


def sub(a_list: list[int], y: int, z: int) -> list[int]:
    """Generating a list from a list."""
    final: list[int] = list()
    if len(a_list) == 0 or y > len(a_list) or z <= 0:
        return final
    if y <= 0:
        y = 0
    if z >= len(a_list):
        z = len(a_list)
    while y < z:
        final.append(a_list[y])
        y += 1
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
