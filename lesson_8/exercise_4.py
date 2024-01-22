# Exercise 4:
# Write a Python function that takes two sets as input and returns a new set containing
# elements that are present in either of the input sets, but not in both.

a, b = set(input()), set(input())
c = a ^ b
print(c)
