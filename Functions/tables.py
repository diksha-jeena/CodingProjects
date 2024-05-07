def print_table(num , n):
    temp = 1
    for i in range(1, n+1):
        temp = (num, 'x', i, '=', num * i)
        print(temp)

#main
num = int(input("Enter the number whose table is to be printed :"))
n = int(input("Enter the number of times you want the table to be printed :"))
print_table(num , n)
