t1 = eval(input("Enter a series of numbers inside parentheses :"))
largest = max(t1)
n = len(t1)
secLargest = 0
for i in range(n):
    if(secLargest < t1[i] < largest):
        secLargest = t1[i]
print("Second largest number =",secLargest)
