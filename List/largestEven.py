lst1 = [1,7,8,5,6,4,9,1,5,6,10]
lst2 = []
n = len(lst1)
for i in range(n):
    if(lst1[i] % 2 == 0 ):
        lst2.append(lst1[i])
        largestEvenNumber = max(lst2)
        print("The largest even number in the given list is = ",largestEvenNumber)
    else:
        print("The list does not contain any even number ")
