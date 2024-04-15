def fun(abc):
    u1 = l1 = 0
    n = len(abc)
    for i in range(0,n):
        ch = abc[i]
        if(ch.islower()):
            l1 += 1
        elif(ch.isupper()):
            u1 += 1
    return(l1,u1)


#main
str_input = input("Enter the string : ")
print(fun(str_input))