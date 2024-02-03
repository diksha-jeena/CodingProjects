num = int(input("Enter a number to check :"))
a , b = 0 , 1
while(b < num):
  a , b = b , a + b

if(b == num):
  print(num , "is a fibonacci number")
else:
  print(num , "is not a fibonacci number")
