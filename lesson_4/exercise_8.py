# 8.Three Numbers
# Input three integers. Output the word “Sorted” if the numbers are listed in
# a non-increasing or non-decreasing order and “Unsorted” otherwise.

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

if num1 <= num2 <= num3 or num1 >= num2 >= num3:
    print("Sorted")
else:
    print("Unsorted")
