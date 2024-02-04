num = eval(input("Enter a series of numbers in a form of list :"))
sum = 0
n = len(num)
for i in range(n):
    if(i % 2 != 0):
        sum += num[i]
print(sum)