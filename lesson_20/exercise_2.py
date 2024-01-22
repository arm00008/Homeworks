# ● Character Frequency:
# ○ Given a string, create a dictionary where keys are characters and values are their
# frequencies in the string.

sentence = "python developer"
n = 1
character_frequency = {k: sentence.count(k) for k in sentence}
print(character_frequency)
