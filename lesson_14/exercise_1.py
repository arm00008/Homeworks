# 1.Write a function in python to read the content from a text file "example.txt" line by line
# and display the same on screen.
def read_file(file_name):
    with open(file_name) as f:
        for line in f:
            print(line)


read_file("text.txt")
