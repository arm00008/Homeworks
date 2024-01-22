# 3. Write a python program to add text to a file and display the text in python.txt.

def my_file(file_name,text):
    with open(file_name, "a") as f:
        f.write(text)
    with open(file_name) as f:
        print(f.read())


my_file("text.txt", "qwerty")
