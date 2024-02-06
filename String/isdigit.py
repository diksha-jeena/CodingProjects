string = input("Enter any string :")
digits = "123456789"
for i in string:
  if(i in digits):
    print("This string conatins digit")
    break
else:
  print("This string does not contain any digit")
