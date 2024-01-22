# 1. Sum
# Input two integers and print out their sum. Preserve the exact format from
# the examples (e.g. the output should contain exactly three lines)

def calculate_sum(a, b):
    result = a + b
    return result


num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

sum_result = calculate_sum(num1, num2)

print("Sum:")
print(num1)
print(num2)
print("------")
print(sum_result)
