# 3.Smallest
# Write a Python program to get the smallest number from a list.

def find_smallest_number(lst):
    if not lst:
        return "The list is empty."

    smallest_number = min(lst)
    return smallest_number


numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
result = find_smallest_number(numbers)

print("The smallest number in the list:", result)
