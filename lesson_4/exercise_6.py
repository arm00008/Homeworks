# 6.Comparison
# Input two positive integers, and output a line describing their relation.
# Follow the sample format.

num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))

if num1 > num2:
    relation = "greater than"
elif num1 < num2:
    relation = "less than"
else:
    relation = "equal to"

print(f"{num1} is {relation} {num2}.")
