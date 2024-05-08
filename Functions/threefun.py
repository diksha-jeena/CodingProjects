def sum(a,b):
    c = a + b
    print(c)
    return c
    
def diff(a,b):
    c = a - b
    print(c)
    sum(c , 10)
    return c

def pro(a , b , c):
    temp = a * b * c
    print(temp)
    diff(temp , 1)
    return temp
print(pro(2,3,4))