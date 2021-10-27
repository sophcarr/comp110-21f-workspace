"""Finding duplicate letters in a word."""

<<<<<<< HEAD
__author__ = "730320301"
=======
__author__ = "123456789"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1

word: str = input("Enter a word: ")

i: int = 0
<<<<<<< HEAD
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
=======
duplicate: bool = False
while (i < len(word)):
    j: int = i + 1
    while(j < len(word)):
        if (word[i] == word[j]):
            duplicate = True
        j += 1
    i += 1

print("Found duplicate: " + str(duplicate))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
