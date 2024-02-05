num = input("Enter a tuple of numbers separated by commas :").split(",")
tpl = tuple(map(int , num))
minElement = min(tpl)
minIndex = tpl.index(minElement)
if(minIndex == len(tpl) // 2):
    print("The minimum element is in the middle")
else:
    print("The minimum element is not in the middle")    