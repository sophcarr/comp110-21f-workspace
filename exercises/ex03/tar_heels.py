"""An exercise in remainders and boolean logic."""

__author__ = "730320301"


# Begin your solution here...
number: int = int(input("Enter an int: "))


remainder_two: int = number % 2
remainder_seven: int = number % 7
total: int = remainder_two + remainder_seven

if total == 0:
    print("TAR HEELS")
else:
    if remainder_two == 0:
        print("TAR")
    else:
        if remainder_seven == 0:
            print("HEELS")
        else:
            print("CAROLINA")