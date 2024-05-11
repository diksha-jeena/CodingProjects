def sum(a , b):
    c = a + b 
    return c
def diff(a , b):
    c = a - b
    return c
def pro(a , b):
    c = a * b
    # print(c)
    return c
dict1 = {"sum" : sum , "diff" : diff , "pro" : pro}
for i in dict1:
    print(dict1[i] (2 , 3))