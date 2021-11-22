"""Examples of optional parameters and Union types."""

from typing import Union


def hello(name: Union[str, int] = "World") -> str:
    """A delightful greeting."""
    greeting: str = name
    return greeting


# Single-argument
print(hello("Sally", 2))

# No arguments!
print(hello())