# 2.The Last Digit
# Input a natural number N and output its last digit.

def get_last_digit(n):
    return n % 10


number = int(input("Enter a natural number: "))

last_digit = get_last_digit(number)
print("Last digit:", last_digit)
