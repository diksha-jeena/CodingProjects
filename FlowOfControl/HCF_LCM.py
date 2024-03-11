x = int(input("Enter first number :"))
y = int(input("Enter second number :"))
if(x > y):
    smaller = x
else:
    smaller = y
for i in range(1 , smaller + 1):
    if((x % i == 0) and (y % i == 0)):
        HCF = i
LCM = (x * y) / HCF
print("The H.C.F of" , x , "and" , y , "is" , HCF)
print("The L.C.M of" , x , "and" , y , "is" , LCM)