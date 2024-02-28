#checking for an armstrong number
num = int(input("Enter any number to check if its an armstrong number or not :"))
digit = int(input("Enter the number of digits :"))
sum = 0
while(num // 10 == 0):
    temp = num % 10
    num = num // 10
    sum = sum + temp ** digit
if(sum == num):
    print("It is an armstrong number .")
else:
    print("It is not an armstrong number .")
