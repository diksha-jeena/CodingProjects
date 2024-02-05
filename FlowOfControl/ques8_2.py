x = float(input("Enter the first number : "))
y = float(input("Enter the second number : "))
z = float(input("Enter the third number : "))
if(x > y and x > z):
    print("The largest number is ",x)
if(y > x and y > z):
    print("The largest number is ",y)
if(z > y and z > x):
    print("The largest number is ",z)