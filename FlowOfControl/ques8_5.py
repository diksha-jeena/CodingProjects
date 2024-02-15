divisor = int(input("Enter divisor number :"))
print("Now enter 5 numbers below :")
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))
num4 = int(input("Enter fourth number :"))
num5 = int(input("Enter fifth number :"))
count =0
if(divisor % num1 == 0):
    count += 1
if(divisor % num2 == 0):    
    count += 1
if(divisor % num3 == 0):
    count += 1
if(divisor % num4 == 0):
    count += 1
if(divisor % num5 == 0):
    count += 1
print(count , "multiples of" , divisor , "found")
