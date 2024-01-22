# 1.Arrange
# Arrange string characters such that lowercase letters should come first

word = input()
lower = ""
upper = ""

for i in word:
    if i.islower():
        lower = lower + i
    else:
        upper = upper + i

print(lower+upper)
