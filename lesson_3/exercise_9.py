# 9. Append new string in the middle of a given (even number of characters) string

def append_string_in_middle(original_string, new_string):
    if len(original_string) % 2 != 0:
        return "Input string must have an even number of characters."

    middle_index = len(original_string) // 2
    modified_string = (
        original_string[:middle_index]
        + new_string
        + original_string[middle_index:]
    )
    return modified_string


user_input = input("Enter a string with an even number of characters: ")
new_str = input("Enter the new string to append: ")

result = append_string_in_middle(user_input, new_str)

if len(result) > 0:
    print("Modified string:", result)
else:
    print("Input string must have an even number of characters.")
