# 7. Write a Python program to print the floating numbers upto 2 decimal places
# (number must be not greater than 10)

def print_float_up_to_2_decimal(number):
    if 0 <= number <= 10:
        formatted_number = "{:.2f}".format(number)
        print("Formatted number:", formatted_number)
    else:
        print("Number must be between 0 and 10 (inclusive).")


user_input = float(input("Enter a floating-point number (not greater than 10): "))
print_float_up_to_2_decimal(user_input)
