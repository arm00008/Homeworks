# 3.Write a python function, which create a dictionary
# for given number N, where keys are numbers from
# 1 to N, and values are cubs of that numbers

cub_of_numbers = {}


def create_cubes_dictionary(number):
    for i in range(1, number+1):
        cub_of_numbers[i] = i**3
    return cub_of_numbers


print(create_cubes_dictionary(int(input())))
