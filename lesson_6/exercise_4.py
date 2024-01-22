# Exercise 4: Palindrome Checker
# Write a program that prompts the user to enter a word and checks if it is
# a palindrome. A palindrome is a word that reads the same backward as
# forward. Use string slicing and an if-else statement to compare the
# original word with its reverse.

def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word


user_input = input("Enter a word: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
