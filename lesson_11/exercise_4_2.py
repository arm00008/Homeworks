# 2.Write a python program which concat 2 dicts.


def concat_dict(my_old_contacts, my_new_contacts):
    for k, v in my_new_contacts.items():
        my_old_contacts[k] = v
    return my_old_contacts


my_old_contacts = {
        'Arman': 93380289,
        "Stepan": 98586878,
        "Koryun": 99874562
    }

my_new_contacts = {'Guido': +399611575245, "Nyuton": +925472157211}

print(concat_dict(my_old_contacts, my_new_contacts))
