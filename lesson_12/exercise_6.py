# Exercise 6: Count Words Function
# Write a function that counts the number of words in a sentence.
def count_words(sentence):
    count = 1
    for i in sentence:
        if i == " ":
            count += 1

    return count


print(count_words(input()))
