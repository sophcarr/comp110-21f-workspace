"""Examples of optional parameters and Union type parameters."""


from typing import Union

# union means the variable can be this or this


def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting function."""
    result: str = "Hello, "
    if isinstance(name, str):
        # is name a string? if so, then....
        return result + name
    elif isinstance(name, float):
        result + "alien from sector " + str(name)
    else:
        return result + "COMP" str(name)


# Calling hello with no arguments leads to use of default value
print(hello())
# Calling hello with one argument overrides the default value
print(hello("Sophia"))
print(hello(3.14))