def diff(N1,N2):
    if(N1 > N2):
        return N1 - N2
    else :
        return N2 - N1
NUM = [10 , 23 , 14 , 54 , 32]
for i in range(4 , 0 , -1):
    A = NUM[i]
    B = NUM[i-1]
    print(diff(A,B) , "#" , end = " ")
