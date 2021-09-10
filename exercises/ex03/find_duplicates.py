"""Finding duplicate letters in a word."""

__author__ = "730320301"

word: str = input("Enter a word: ")

i: int = 0
s: int = 0
booleantest: bool = False

while i < len(word):
    word[i]
    s = 0
    while s < len(word):
        if i != s:
            if word[i] == word[s]:
                booleantest = True
        s = s + 1
    i = i + 1

print("Found duplicate: " + str(booleantest))