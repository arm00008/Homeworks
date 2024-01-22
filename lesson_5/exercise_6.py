# 6.Square
# Turn every item of a list into its square

def square_list_elements(lst):
    squared_list = [item**2 for item in lst]
    return squared_list


numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
result = square_list_elements(numbers)

print("List after squaring each element:", result)
