# Exercise 3: Word Finder
# Write a program that takes a list of words and a target word as input.
# The program should find and print all words in the list that contain the
# target word. Use a for loop, the in operator, and an if statement to
# check if the target word is present in each word in the list.

def find_words_with_target(words, target):
    found_words = [word for word in words if target in word]
    return found_words


word_list = input("Enter a list of words separated by space: ").split()
target_word = input("Enter the target word: ")
result = find_words_with_target(word_list, target_word)

print("Words containing the target word:", result)
