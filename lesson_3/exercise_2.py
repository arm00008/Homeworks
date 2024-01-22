# 2. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
# the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string
# is less than 3, leave it unchanged.

def modify_string(input_string):
    if len(input_string) < 3:
        return input_string

    if input_string.endswith('ing'):
        modified_string = input_string + 'ly'
    else:
        modified_string = input_string + 'ing'

    return modified_string


user_input = input("Enter a string: ")
result = modify_string(user_input)
print("Modified string:", result)
