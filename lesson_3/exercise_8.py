# 8.Create a string made of the first, middle and last character of given string with odd number of
# symbols

def create_string_with_odd_length_chars(input_string):
    if len(input_string) % 2 == 0:
        return "Input string must have an odd number of symbols."

    middle_index = len(input_string) // 2
    result_string = input_string[0] + input_string[middle_index] + input_string[-1]
    return result_string


user_input = input("Enter a string with an odd number of symbols: ")
result = create_string_with_odd_length_chars(user_input)

if len(result) > 0:
    print("Resulting string:", result)
else:
    print("Input string must have an odd number of symbols.")
