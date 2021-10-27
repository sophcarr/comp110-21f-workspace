"""An exercise in remainders and boolean logic."""

<<<<<<< HEAD
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
=======
__author__ = "730243388"


# Begin your solution here...
num: int = int(input("Enter an int: "))

if (num % 14 == 0):
    print("TAR HEELS")
elif (num % 7 == 0):
    print("HEELS")
elif (num % 2 == 0):
    print("TAR")
else:
    print("CAROLINA")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
