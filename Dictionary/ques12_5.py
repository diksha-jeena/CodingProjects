M = {}
n = int(input("How many students ? "))
for i in range(n):
    rollNum = int(input("Enter your roll number : "))
    marks = float(input("Enter your marks : "))
    M[rollNum] = marks
print("Created dictionary = ",M)
