# 4.Write a function display_words() in python to read text from a text file "example.txt",
# and display those words, which are less than 4 characters

def display_words(file_name):
    listt = []
    word = file_name.split(" ")
    for i in word:
        if len(i) < 4:
            listt.append(i)
    return listt


f = open("text.txt")
x = f.read()
print(display_words(x))
f.close()



