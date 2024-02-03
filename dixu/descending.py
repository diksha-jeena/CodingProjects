#tc=O(N*N)
#sc=O(1)
arr=[5,9,8,4,1,6]
N=len(arr)
for i in range(0,N):
    for j in range(0,N-1):
        if(arr[j]<arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)