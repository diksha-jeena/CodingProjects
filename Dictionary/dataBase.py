n = int(input("Enter the number of students :"))
dict1 = {}
l1 = []
for i in  range(n):
  name = input("Enter the name of the student :")
  roll = int(input("Enter the roll number of the student    :"))
  marks = int(input("Enter the marks of the student :"))
  dict1 = {"Name" : name,"Roll Number" : roll,"Marks " :    marks}
  l1.append(dict1)
print(l1)

