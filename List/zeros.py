lst = eval(input("Enter a list : "))
n = len(lst)
end = n - 1
i = 0
while(i <= end):
    ele = lst[i]
    if(ele == 0):
        for j in range(i , end):
            lst[j] = lst[j + 1]
        else:
            lst[end] = 0
            end -= 1
    if(lst[i] != 0):
        i += 1
print("Zero shifted : ", lst)