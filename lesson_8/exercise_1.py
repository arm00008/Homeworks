# Exercise 1:
# Write a Python function that takes two sets as input and returns a new set containing
# elements that are present in both input sets.

a, b = set(input()), set(input())
c = a & b
print(c)
