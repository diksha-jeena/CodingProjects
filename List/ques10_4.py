lst = []
r = int(input("How many rows ?"))
c = int(input("How many columns ?"))
for i in range(r):
    row = []
    for j in range(c):
        ele = int(input("Element" + str(i) + "," + str(j) + ":"))
        row.append(ele)
    lst.append(row)
print("List = ", lst)