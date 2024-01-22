# Filtering Word Lengths:
# ○ Given a list of words, create a dictionary where keys are words, and values are
# their lengths, but only for words with lengths greater than 3.

words_list = ["python", "abc", "comprehension"]
len_word = {w: len(w) for w in words_list if len(w) > 3}
print(len_word)
