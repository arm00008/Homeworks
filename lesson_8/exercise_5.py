# Exercise 5:
# You are given three lists, list1, list2, and list3. Your task is to implement a
# programm that takes these lists and prints the following:

# 1)The set of elements that are common to all three lists.
list_1 = ["a", "b", 'g']
list_2 = ["a", "b", 'c']
list_3 = ["a", "u", 'g']

a, b, c = set(list_1), set(list_2), set(list_3)
print(a & b & c)


# 2)The set of elements that are present in at least two of the three lists, but not in all
# three.

print((a | b | c)-(a ^ b ^ c))



# 3)The set of elements that are unique to each list (present in only one list).

print((a | b | c) - ((a | b | c)-(a ^ b ^ c))-(a & b & c))




