# Exercise 4:
# Write a Python program that generates a random number between 1 and 100 and asks
# the user to guess the number. The program should give hints whether the guessed
# number is too high or too low until the correct number is guessed.


import random

random_number = random.randint(1, 100)

n = int(input())
while n != random_number:
    if n < random_number:
        print("aveli mec")
        n = int(input())
    else:
        print("aveli poqr")
        n = int(input())


