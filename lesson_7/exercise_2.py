# 2.Count
# Count all letters, digits, and special symbols from a given string

my_str = input()
chars = 0
digits = 0
symbol = 0

for i in my_str:
    if 48 <= ord(i) <= 57:
        digits += 1
    elif 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        chars += 1
    elif 33 <= ord(i) <= 47 or 58 <= ord(i) <= 64 or 91 <= ord(i) <= 96 or 123 <= ord(i) <= 126:
        symbol += 1

print(f"chars = {chars}", f"digits = {digits}", f"symbol = {symbol}", sep="\n")
