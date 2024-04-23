def simp(p,t,r):
    si = (p * t * r)/100
    return si



#main
p = int(input("Enter the value of principal :"))
t = int(input("Enter the time :"))
r = float(input("Enter the value of rate:"))
print(simp(p,r,t))
