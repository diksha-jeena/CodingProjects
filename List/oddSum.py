lst = eval(input("Enter a list : "))
sum = 0
for i in lst:
    if(i % 2 != 0):
        sum += i
print("Sum of all odd numbers = ",sum)