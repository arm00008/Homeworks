# 1. Write a Python program to square and cube every number in a given list of
# integers using Lambda.
# Sample. ([1,2,3,4,5])
# Output: ([1, 4, 9, 16, 25], [1, 8, 27, 64, 125])

numbers = [1, 2, 3]
print(list(map(lambda x: x**2, numbers)))
print(list(map(lambda x: x**3, numbers)))
