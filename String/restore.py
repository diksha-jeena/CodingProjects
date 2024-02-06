str1 = input("Enter string 1:")
str2 = input("Enter string 2:")
str3 = " "
if(str1 in str2):
    str3 = str2[0:4] + "Restore"
print(str3)