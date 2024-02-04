def even_number():
    lst1 = eval(input("Enter a list of random numbers :"))
    lst2 = []
    for i in lst1:
        if(i % 2 == 0):
            lst2.append(i)
    return lst2
    
print(even_number())








