# Password Checker:
# Write a function that will get a function string and check if the password is strong
# or not.
# Strong password must contain | One uppercase letter | one special symbol | one
# number
# Length of the password should be 8 or more
# If your password is Strong you will return True. else return False

def password_checker_function(password):
    res = False
    number = 0
    uppercase_letter = 0
    special_symbol = 0
    if len(password) >= 8:
        for i in password:
            if i.isdigit():
                number += 1
            if i.isupper():
                uppercase_letter += 1
            if i in ".,:;!_*-+()/#¤%&)":
                special_symbol += 1
        if number >= 1 and uppercase_letter >= 1 and special_symbol >= 1:
            res = True
    return res


print(password_checker_function(input()))




