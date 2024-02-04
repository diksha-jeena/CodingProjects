t1 = eval(input("Enter a tuple :"))
mx = max(t1)
if(t1.count(mx) > 1):
    print("Contains multiple maximum element ")
else:
    print("Contains only one maximum element ")