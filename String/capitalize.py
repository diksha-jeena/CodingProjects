str = input("Enter any random word :")
n = len(str)
str2 = " "
for i in range(0,n,2):
    str2 += str[i]
    if(i < (n-1)):
        str2 += str[i+1].upper()
print("Alternatively capitalized string = ",str2)
