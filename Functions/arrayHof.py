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
arr = [sum , diff , pro]
n = len(arr)
def runAll(arr):
    for i in range(n):
        print(arr[i](3 , 2))
runAll(arr)