tpl = eval(input("Enter a series of random numbers in a tuple form :"))
maximum = max(tpl)
if(tpl.count(maximum) > 1):
    print("The tuple contains multiple maximum elements")
else:
    print("The tuple contains only one maximum element")