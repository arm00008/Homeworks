# Exercise 2:
# Write a Python function that takes two sets as input and returns a new set containing all
# unique elements from both input sets.

a, b = set(input()), set(input())
c = a ^ b
print(c)
