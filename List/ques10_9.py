lst = eval(input("Enter a list : "))
n = len(lst)
min_element = lst[0]
index = 0
for i in range(n):
    if(min_element > lst[i]):
        min_element = lst[i]
        index = i
print("List = " , lst)
print("Minimum element = " , min_element)
print("Index of minimum element is :" , index)