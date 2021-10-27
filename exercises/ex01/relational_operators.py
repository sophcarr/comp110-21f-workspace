<<<<<<< HEAD
"""Practice with relational operators."""

__author__ = "730320301"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
answer1: int = left < right
answer2: int = left >= right
answer3: int = left == right
answer4: int = left != right

print(str(left) + " < " + str(right) + " is " + str(answer1))
print(str(left) + " >= " + str(right) + " is " + str(answer2))
print(str(left) + " == " + str(right) + " is " + str(answer3))
print(str(left) + " != " + str(right) + " is " + str(answer4))
=======
"""Demonstrates python relational operators for two number inputs."""

__author__ = "730243388"

string_one = input("Left-hand side: ")
string_two = input("Right-hand side: ")

number_one = int(string_one)
number_two = int(string_two)

print(string_one + " < " + string_two + " is " + str(number_one < number_two))
print(string_one + " >= " + string_two + " is " + str(number_one >= number_two))
print(string_one + " == " + string_two + " is " + str(number_one == number_two))
print(string_one + " != " + string_two + " is " + str(number_one != number_two))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
