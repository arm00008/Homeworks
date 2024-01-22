# Exercise 7: Find youngest student
# Write a function that takes a dictionary with information about students. Return info
# about the youngest student

def find_youngest_student(a, b, c):

    students_info = {
            'student1': {
                'name': 'John Doe',
                'age': a,
                'subjects': ['Math', 'Physics', 'English'],
                'scores': [7, 9, 9, 6],
            },
            'student2': {
                'name': 'Jane Smith',
                'age': b,
                'subjects': ['Chemistry', 'Biology', 'History'],
                'scores': [5, 6, 8, 10],
            },
            'student3': {
                'name': 'Bob Johnson',
                'age': c,
                'subjects': ['Computer Science', 'Statistics', 'Psychology'],
                'scores': [8, 8, 9, 9, 9],
            },
        }
    min_age = a
    for k, v in students_info.items():
        for j, i in v.items():
            if j == 'age':
                if i < min_age:
                    youngest_student = k
    return youngest_student



print(find_youngest_student(10, 25, 36))
