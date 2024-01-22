# 5. Write a Python function to get a string made of 4 copies of the last two characters of a
# specified string (length must be at least 2).

def repeat_last_two(input_string):
    if len(input_string) < 2:
        return "Input string should have at least 2 characters."

    last_two_chars = input_string[-2:]
    repeated_string = last_two_chars * 4
    return repeated_string


user_input = input("Enter a string: ")
result = repeat_last_two(user_input)
print("Modified string:", result)
