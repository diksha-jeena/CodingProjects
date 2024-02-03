class Student():
    #properties
    rollNumber=0
    class_=0
    name=""
    dob=""
    section=""
    #methods
    def study(self):
        print("student",self.name,"studies")
    def play(self):
        print("student",self.name,"plays")
s1=Student()
s1.name="Dixu"
s1.dob=10
s1.rollNumber=4
s1.study()
s1.play()

s2=Student()
s2.name="Siddharth"
s2.dob=21
s2.rollNumber=38
s2.study()
s2.play()

