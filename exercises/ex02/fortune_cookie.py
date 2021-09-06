"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730320301"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
guess: int = int(randint(1, 4))

if guess == 1:
    print("Love is in the air.")
else:
    if guess == 2:
        print("Now is the time to buy a house.")
    else:
        if guess == 3:
            print("Beware of the dog.")
        else:
            if guess == 4:
                print("Your life is going to be long and happy.")
            else:
                print("Guess you're not getting a fortune today.")

print("Now, go spread positive vibes!")