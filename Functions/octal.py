def oct2others(n):
    print("Passed octal number :" , n)
    numString = str(n)
    decNum = int(numString , 8)
    print("Number in decimal :" , decNum)
    print("Number in binary :" , bin(decNum))
    print("Number in Hexadecimal :" , hex(decNum))

num = int(input("Enter an octal number :"))
oct2others(num)