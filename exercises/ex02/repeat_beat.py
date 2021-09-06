"""Repeating a beat in a loop."""

__author__ = "730320301"


# Begin your solution here...
beat: str = input("What beat do you want me to repeat? ")
repetitions: int = int(input("How many times do you want me to repeat it? "))
answer: str = ""

i: int = 0

while i < repetitions:
    i = i + 1
    answer = answer + beat 
    if i < repetitions:
        answer = answer + " "

if repetitions <= 0:
    print("No beat...")
else:
    print(answer)