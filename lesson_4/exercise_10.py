# 10.Salaries
# Given the salaries of three employees working at a department, find the
# amount of money by which the salary of the highest-paid employee differs
# from the salary of the lowest-paid employee. The input consists of three
# positive integers - the salaries of the employees. Output a single number,
# the difference between the top and the bottom salaries

salary1 = int(input("Enter the salary of the first employee: "))
salary2 = int(input("Enter the salary of the second employee: "))
salary3 = int(input("Enter the salary of the third employee: "))

highest_salary = max(salary1, salary2, salary3)
lowest_salary = min(salary1, salary2, salary3)
salary_difference = highest_salary - lowest_salary

print("Difference between the highest and lowest salaries:", salary_difference)
