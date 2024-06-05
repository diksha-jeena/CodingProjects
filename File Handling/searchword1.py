with open('temp.txt' , 'wb') as file :
    file.write(b"Non-default arguments cannot follow default argument")

with open('example1.txt', 'rb') as file:
    content = file.read()
    words = content.split()
    for i in words :
        if(i == b'follow'):
            print("Word found :" , i.decode())
            break
    else:
        print("Word not found")