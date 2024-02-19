x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
z = int(input("Enter third number : "))
smallest = min(x,y,z)
largest = max(x,y,z)
mid = 0
if(smallest < x < largest):
    mid += x
elif(smallest < y < largest):
    mid += y
elif(smallest < z < largest):
    mid += z
print("Numbers in ascending order : " ,smallest , mid , largest)
