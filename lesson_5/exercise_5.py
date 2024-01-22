# 5.Duplicates
# Write a Python program to remove duplicates from a list.

def remove_duplicates(input_list):
    seen = set()
    result = []

    for item in input_list:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result


numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
result = remove_duplicates(numbers)

print("List after removing duplicates:", result)
