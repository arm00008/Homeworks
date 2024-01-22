# Exercise 3:
# Write a Python function that takes two sets as input and returns a new set containing
# elements that are present in the first set but not in the second set.

a, b = set(input()), set(input())
c = a - b
print(c)
