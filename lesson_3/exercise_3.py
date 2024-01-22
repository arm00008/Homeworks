# 3. Write a Python program to remove the n-th index character from a nonempty string

def remove_character(input_string, n):
    if len(input_string) == 0:
        return "Input string should be non-empty."

    if n < 0 or n >= len(input_string):
        return "Invalid index. Index should be in the range [0, length of string - 1]."

    modified_string = input_string[:n] + input_string[n+1:]
    return modified_string


user_input = input("Enter a string: ")
index_to_remove = int(input("Enter the index to remove: "))

result = remove_character(user_input, index_to_remove)
print("Modified string:", result)
