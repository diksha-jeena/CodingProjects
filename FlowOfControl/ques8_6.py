# Area of a circle / perimeter  = pie*r**2 / 2*pie*r

radius = float(input("Enter the radius :"))
pie = 3.14
print("1.Calculate Area")
print("2.Clculate perimeter")
choice = int(input("Enter your choice(1 or 2) :"))
if(choice == 1):
    area = pie * radius ** 2
    print("Area of a circle =" ,area)
else:
    peri = 2 * pie * radius
    print("Perimeter of a circle =" , peri)