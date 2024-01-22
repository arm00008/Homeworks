# Exercise 2: Vowel Counter
# Write a program that takes a string as input and counts the
# number of vowels (a, e, i, o, u) in the string. Use a for
# loop, an if statement, and the in operator to check if a
# character is a vowel.

def count_vowels(input_string):
    vowels = "aeiou"
    vowel_count = 0
    for char in input_string:
        if char.lower() in vowels:
            vowel_count += 1
    return vowel_count


input_str = input("Enter a string: ")
result = count_vowels(input_str)

print("Number of vowels in the string:", result)
