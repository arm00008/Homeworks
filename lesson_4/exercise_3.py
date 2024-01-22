# 3.Digit Sum
# Input a two-digit natural number and output the sum of its digits. You can
# assume that the input will be a two-digit number and need not check that
# programmatically.

two_digit_number = int(input("Enter a two-digit natural number: "))

digit_sum = (two_digit_number // 10) + (two_digit_number % 10)

print("Sum of digits:", digit_sum)
