# 2.Letters Count
# Write a Python function to calculate count of each letter in string


def count_letters(input_string):
    letters_count = {}
    n = 1

    for char in input_string.lower():
        if char not in letters_count:
            letters_count[char] = n
        else:
            letters_count[char] = n + 1
    return letters_count


print(count_letters("Ppythoon121"))
