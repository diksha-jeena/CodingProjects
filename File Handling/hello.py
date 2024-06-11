with open('hello.txt' , 'w') as file:
    file.write("Welcome my class" '\n' "It is a fun place" '\n' "You will learn and play")
    file.flush()
    
with open('hello.txt' , 'r') as file:
    content = file.read()
    print(content)
    file.flush()