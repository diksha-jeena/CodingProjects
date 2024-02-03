n = int(input("Enter the number of students :"))
stu = {}
lst1 = []
lst2 = []
for _i in range(n):
  rno = int(input("Enter your roll number :"))
  name = input("Enter your name :")
  marks = float(input("Enter your marks :"))
  stu = {"Roll no." : rno , "Name" : name , "Marks" : marks}
  lst1.append(stu)

for i in range(n):
  if(lst1[i]["Marks"] > 75):
    lst2.append(lst1[i])
print(lst2)    
    