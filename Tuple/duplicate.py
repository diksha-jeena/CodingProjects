t1 = eval(input("Enter a tuple :"))
for i in t1:
    if(t1.count(i) > 1):
        print("Yes this tuple contains duplicate elemets ")
        break
else:
    print("No it does not contain any duplicate element ")

