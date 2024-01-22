# Exercise 2:
# Write a Python program that asks the user to enter a password. Keep asking for the
# password until the correct password "secret" is entered. Provide appropriate feedback
# to the user.

passw = input()
while passw != "secret":
    print("Nepravilno")
    passw = input()
else:
    print("Pravilno")



