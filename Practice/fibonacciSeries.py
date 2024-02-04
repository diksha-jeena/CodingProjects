prev = 0
next = 0
arr = [prev , next]
for i in range(0,11):
    sum = prev + next
    arr.append(sum)
    prev = next
    next = sum
print(arr)
