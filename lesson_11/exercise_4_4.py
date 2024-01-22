# 4.Write a python function which create dict from 2
# lists with the same length


def two_list_dict(list_1, list_2):
    my_dict = {}
    len_list_1 = len(list_1)
    for i in range(len_list_1):
        my_dict[list_1[i]] = list_2[i]

    return my_dict


print(two_list_dict(["a", "b", "c"], [1, 2, 3, 4]))
