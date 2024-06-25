def EOReplace(L):
    for i in range(len(L)):
        if(L[i] % 2 == 0 ):
            L[i] += 1
        else:
            L[i] -= 1
    return L

#main
L = [2 , 5]
print(EOReplace(L))