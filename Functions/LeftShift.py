def LShift(Arr , n):
    L = len(Arr)
    for i in range(0 , n):
        y = Arr[0]
        for i in range(0 , L-1):
            Arr[i] = Arr[i+1]
        Arr[L-1] = y
    print(Arr)

Arr = [10 , 20 , 5 , 30]
n = 3
LShift(Arr , n)