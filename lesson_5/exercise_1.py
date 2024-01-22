# 1.Multiply
# Write a Python program to multiply all the items in a list.

def multiply_list_elements(lst):
    result = 1
    for item in lst:
        result *= item
    return result


numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
result = multiply_list_elements(numbers)
print("Result of multiplying all items in the list:", result)
