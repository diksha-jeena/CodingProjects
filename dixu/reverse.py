#tc=O(N)
#sc=O(1)
#printing each character of the string in reverse order
str=input("enter any string")
n=len(str)
for i in range((n-1),-1,-1):
    print(str[i])
    
