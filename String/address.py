add = eval(input("Enter your address and pincode :"))
pincode = []
for i in add:
  if(i.isdigit()):
    pincode.append(i)
print("address = ",add)
print("Pincode is :",pincode)


