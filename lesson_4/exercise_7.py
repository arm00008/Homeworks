# 7.Birth Year
# The program prompts the user their birth year. Assuming a person’s age
# is a non-negative integer not exceeding 120, output the user’s age or the
# words “Incorrect Year”. The sample outputs assume it’s currently the year
# 2016. If you are writing this program during any other year, the correct
# answers may differ. Store the value of the current year in a variable.

current_year = 2016

birth_year = int(input("Enter your birth year: "))

if 0 <= birth_year <= current_year and current_year - birth_year <= 120:
    age = current_year - birth_year
    print("Your age is:", age)
else:
    print("Incorrect Year")
