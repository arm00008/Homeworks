# 3. Write a Python program to check whether a given string is number or
# not using Lambda.

sentence = input()
check_number = filter(lambda s: s.isdigit(), list(sentence))
if len(list(check_number)) == len(sentence):
    print("True")
else:
    print("False")

