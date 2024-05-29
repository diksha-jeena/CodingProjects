with open('notes.txt' , 'r') as file :
    content = file.read()
    print(content)

with open('notes.txt' , 'a') as file :
    file.write("This is Diksha's husband Siddharth, \n")

