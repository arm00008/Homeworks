# 1.Max of Three
# Write a Python function to find the Max of three numbers.
def max_of_tree(a, b, c):
    result = 0
    for i in a, b, c:
        if i > result:
            result = i
    return result


print(max_of_tree(1000, 25, 36))
print(max_of_tree(256, 5, 37))
