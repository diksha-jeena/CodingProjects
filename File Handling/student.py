import csv
with open('student.csv' , 'w' ) as file :
    stuwriter = csv.writer(file)
    stuwriter.writerow(['Rollno' , 'Name' , 'Marks'])
    for i in range(2):
        print("Student record" , (i+1))
        rollno = int(input("Enter rollno :"))
        name = input("Enter name :")
        marks = float(input("Enter marks :"))
        sturec = [rollno , name , marks]
        stuwriter.writerow(sturec)

with open('student.csv' , 'r') as file :
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
