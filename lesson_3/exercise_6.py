# 6. Write a Python function to get a string made of its first three characters of a specified string. If
# the length of the string is less than 3 then return the original string.

def get_first_three(input_string):
    if len(input_string) < 3:
        return input_string

    first_three_chars = input_string[:3]
    return first_three_chars


user_input = input("Enter a string: ")
result = get_first_three(user_input)
print("Modified string:", result)
