lst = eval(input("Enter a list : "))
item = int(input("Enter a element to be removed : "))
if(item in lst):
    ele = lst.index(item)
    lst.pop(ele)
    print("List after removing the given element.",lst)
else:
    print("Element is not in the list.")

