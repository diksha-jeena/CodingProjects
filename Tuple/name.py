lst = []
n = int(input("Enter how many students ? "))
for i in range(n):
    stuName = input("Enter student's name : ")
    lst.append(stuName)
tpl = tuple(lst)
userName = input("Enter name to be searched ")
if(userName in tpl):
    print(userName , "exists in tuple")
else:
    print(userName , "does not exist in tuple")