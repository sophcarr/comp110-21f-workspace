"""Practice with dictionaries."""

__author__ = "730320301"

# Define your functions below


def invert(list1: dict[str, str]) -> dict[str, str]:
    """Switching keys with thier corresponding values."""
    list2: dict[str, str] = dict()
    for key in list1:
        list2[list1[key]] = key
    return list2


def favorite_color(list1: dict[str, str]) -> str:
    """Counting most popular color."""
    zzz: dict[str, int] = dict()
    max: int = 0
    final: str = ""
    for key in list1:
        if list1[key] in zzz:
            zzz[list1[key]] += 1
        else:
            zzz[list1[key]] = 1
    for key in zzz:
        first: int = zzz[key]
        if first > max:
            max = first
            final = key
    return final


def count(list1: list[str]) -> dict[str, int]:
    zzz: dict[str, int] = dict()
    for key in list1:
        if key in zzz:
            zzz[key] += 1
        else:
            zzz[key] = 1
    return zzz
