# 5. Write a python program to read a file, a.txt line by line.

def read_file(file_name):
    with open(file_name) as f:
        for line in f:
            print(line)


read_file("text.txt")
