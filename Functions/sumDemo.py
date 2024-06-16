p = 5
def sum(q , r = 2):
    global p
    p = r + q ** 2
    print(p , end = "#")

a = 10
b = 5
sum(a,b)
sum(r = 5 , q = 1)
