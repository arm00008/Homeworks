# DICTIONARIES
# 1.Write a python function, which add a new value
# with given key in dict.


def dict_new_value(dict_1, n):

    for i in dict_1.keys():
        dict_1[i] = n
    return dict_1


print(dict_new_value({"a": "Real", "b": "Python", "c": "Is", "d": "Great", "e": "!"}, 8))
