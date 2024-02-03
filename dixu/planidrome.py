#tc=O(N)
#sc=O(1)
str="nitin"
def isPalindrome(str):
    i=0
    j=len(str)-1
    while(i!=j):
        if(str[i]!= str[j]):
            return False
        i= i + 1
        j = j - 1
    return True

print(isPalindrome("racecar"))
print(isPalindrome("dixu"))
