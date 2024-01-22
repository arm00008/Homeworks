# 3.Factorial
# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.

def factorial_of_number(number):
    factorial_number = 1
    if number >= 0:
        for i in range(number):
            factorial_number *= number
            number -= 1
        return factorial_number


print(factorial_of_number(int(input())))
