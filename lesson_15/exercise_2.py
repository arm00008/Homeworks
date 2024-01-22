# Random Password Generator:
# Write a function that generates a random password for the user. Allow the user
# to specify the length and complexity of the password (include letters, numbers,
# and symbols).
import random as r
import string as s


def generator_password_function(length, complexity):
    x = s.ascii_uppercase + s.ascii_lowercase + s.digits + s.punctuation
    password = ''
    n = 0
    if complexity == "weak":
        for i in range(length):
            password += r.choice(x)
    elif complexity == "strong":
        for i in range(length):
            if n < 1:
                password += r.choice(s.digits) + r.choice(s.ascii_uppercase) + r.choice(s.punctuation)
                n += 1
            else:
                password += r.choice(s.ascii_lowercase)
    res = list(password)
    r.shuffle(res)

    return "".join(res)


print(generator_password_function(int(input()), input()))

