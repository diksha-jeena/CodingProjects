#checking for prime number
num = int(input("Enter a number :"))
lim = int(num / 2) + 1   #calculates limit for the loop
for i in range(2 , lim):
    rem = num % i   #remainder
    if(rem == 0):
        print(num , "is not a prime number")
        break
else:
    print(num , "is a prime number")