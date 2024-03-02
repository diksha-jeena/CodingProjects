x = float(input("Enter the value of x"))
n = int(input("Enter value of n (for x ** n ) :"))
s = 0
for i in range(n +1 ):
    s += x ** i
print("Sum of first" , n , "terms : " , s)