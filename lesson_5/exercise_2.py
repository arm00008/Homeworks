# 2.Largest
# Write a Python program to get the largest number from a list

def find_largest_number(lst):
    if not lst:
        return "The list is empty."

    largest_number = max(lst)
    return largest_number


numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
result = find_largest_number(numbers)

print("The largest number in the list:", result)
