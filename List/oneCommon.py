
lst1 = list(map(int, input("Enter first list, space-separated: ").split()))
lst2 = list(map(int, input("Enter second list, space-separated: ").split()))
n = len(lst1)
for i in range(n):
    if lst1[i] in lst2:
        print("They have elements in common :" , lst1[i])
        break
    else:
        print("They have no same elements")
        
