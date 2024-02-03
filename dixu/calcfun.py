a=int(input("enter any number"))
b=int(input("enter any number"))
option=input("enter your choice a for addition , s for substraction , m for multiply , d for divide")
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)
if(option=="a"):
    print(add(a,b))
elif(option=="s"):
    print(sub(a,b))
elif(option=="m"):
    print(multiply(a,b))
else:
    print(divide(a,b))

