# 1. Write a Python program to get a string made of the first 2 and the last 2 chars from a
# given string.

def get_modified_string(input_string):
    if len(input_string) < 2:
        return "Input string should have at least 2 characters."

    modified_string = input_string[:2] + input_string[-2:]
    return modified_string


# Example of using the function
user_input = input("Enter a string: ")
result = get_modified_string(user_input)
print("Modified string:", result)
