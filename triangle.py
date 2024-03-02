angle1 = angle2 = angle3 = 0
angle1 = float(input("Enter angle 1 : "))
angle2 = float(input("Enter angle 2 : "))
angle3 = float(input("Enter angle 3 : "))
if(angle1 + angle2 + angle3 == 180):
    print("They form a triangle")
else:
    print("They do not form a triangle")