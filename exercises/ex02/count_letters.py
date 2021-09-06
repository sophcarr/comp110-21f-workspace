"""Counting letters in a string."""

__author__ = "730320301"


# Begin your solution here...
letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")

i: int = 0
letters_found: int = 0

while i < len(word):
    if word[i] == letter:
        letters_found = letters_found + 1
    i = i + 1

print("Count: " + str(letters_found))