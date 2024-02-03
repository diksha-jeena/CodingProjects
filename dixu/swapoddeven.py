#tc=O(N)
#sc=O(1)
arr=[2,5,6,7,8,9]
n=len(arr)
for i in range(0,n-1):
    temp=0
    if(arr[i]%2==0):
        temp=arr[i]
        arr[i]=arr[i+1]
        arr[i+1]=temp
    else:
        pass
print(arr)
    