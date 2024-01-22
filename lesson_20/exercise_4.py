# Character ASCII Values:
# ○ Given a string, create a dictionary where keys are characters, and values are
# their ASCII values.

sentence = "hello world"
el_ascii = {k: ord(k) for k in sentence}
print(el_ascii)
