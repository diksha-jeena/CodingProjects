name = input("Enter your name : ")
phn_number = input("Enter your phone number : ")
with open('contacts.txt' , 'w') as fh:
    fh.write(f"Name : {name}          Phone : {phn_number} ")

with open('contacts.txt' , 'r') as fh :
    info = fh.read()
    print(info)