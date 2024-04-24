total = 0 
def sum(arg1 , arg2):
    global total
    total = arg1 + arg2
    # print("total :" , total)
    return total 



#main
arg1 = int(input("Enter first number :"))
arg2 = int(input("Enter second number :"))
sum(arg1 , arg2)
print("Total :" , total)