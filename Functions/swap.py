def swap(a,b):
    c = a
    a = b
    b = c
    return(a,b)




#main
a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
print(a,b)
print("After swapping" , swap(a,b))