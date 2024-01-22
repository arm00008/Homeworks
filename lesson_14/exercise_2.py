# 2. Write a function in Python to count and display the total number of words in a text file.

def word_counter_function(file_name):
    count = 0
    with open(file_name, "r") as f:
        for i in f:
            word = i.split()
            count += len(word)
    print(count)


word_counter_function("text.txt")
