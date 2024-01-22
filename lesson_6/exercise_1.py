# Exercise 1: Counting Even Numbers
# Write a program that takes a list of numbers as input and
# counts the number of even numbers in the list. Use a for
# loop, an if statement, and the modulus operator (%) to
# determine if a number is even or odd.

def count_even_numbers(numbers):
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
    return even_count


numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
result = count_even_numbers(numbers)

print("Number of even numbers in the list:", result)
