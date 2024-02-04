lst1 = eval(input("Enter a list : "))
lst2 = []
M , N = eval(input("Enter two numbers as M and N : "))
for num in lst1:
    if(num % M == 0 and num % N == 0):
        lst2.append(num)
print("New created list is : ",lst2)  


# accha haan wo file handling abhi maine "Reading data from files" tak kar liya hai baki ka sara kal complete ho jaega 