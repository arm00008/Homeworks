# ● Dictionary Merge:
# ○ Given two dictionaries, merge them into a new dictionary, excluding any keys
# that start with an underscore.

dict_1 = {'jack': 38, '_michael': 48, 'guido': 57, 'john': 33}
dict_2 = {'zack': 38, 'michael': 48, '_guido': 57, 'john': 33}
new_dict = {k: v for k, v in dict_1.items() | dict_2.items() if k[0] != "_"}
print(new_dict)

