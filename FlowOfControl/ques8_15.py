n = int(input("How many numbers are you gonna give : "))
sumEven = 0
sumOdd  = 0
# length = len(n)
for i in range(n):
    num = int(input("Enter a number : "))
    if(num % 2 == 0):
        sumEven += num
    else:
        sumOdd += num

print("Sum of even numbers =" , sumEven)
print("Sum of odd numbers =" , sumOdd)