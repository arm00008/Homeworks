# 4. Write a Python program to change a given string to a new string where the first and last chars
# have been exchanged.

def swap_first_and_last(input_string):
    if len(input_string) < 2:
        return input_string

    modified_string = input_string[-1] + input_string[1:-1] + input_string[0]
    return modified_string


user_input = input("Enter a string: ")
result = swap_first_and_last(user_input)
print("Modified string:", result)
