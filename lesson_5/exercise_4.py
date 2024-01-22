# 4.Second smallest
# Write a Python program to find the second smallest number in a list.

def find_second_smallest_number(lst):
    if len(lst) < 2:
        return "List should have at least two numbers."

    sorted_unique_numbers = sorted(set(lst))

    if len(sorted_unique_numbers) < 2:
        return "List should have at least two unique numbers."

    second_smallest_number = sorted_unique_numbers[1]
    return second_smallest_number


numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
result = find_second_smallest_number(numbers)

print("The second smallest number in the list:", result)
