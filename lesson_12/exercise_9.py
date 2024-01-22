
def prime_numbers_function(number):

    prime_numbers = []
    for num in range(2, number+1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            prime_numbers.append(num)

    return prime_numbers


print(prime_numbers_function(int(input())))
