#tc=O(N)
#SC=O(1)
def ispalindrom(str):
    i=0
    j=len(str)-1
    while(i!=j):
        if(str[i]!=str[j]):
            return False
        i=i+1
        j=j-1
    return True

print(ispalindrom("racecar"))

