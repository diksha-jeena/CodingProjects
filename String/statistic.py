""" It is a program that prints 
    Number of uppercase letters :
    Number of lowecase letters :
    Number of alphabets :
    Number of symbols :
    Number of digits : """


line = input("Enter any line :")
upperCount = loweCount = 0
alphaCount = SymbolsCount = digitsCount = 0
for i in line:
    if(i.islower()):
        loweCount += 1
    elif(i.isupper()):
        upperCount += 1
    elif(i.isalpha()):
        alphaCount += 1
    elif(i.isdigit()):
        digitsCount += 1
    elif(i.isalnum != True and i != " " , ":"):
        SymbolsCount += 1
print("Number of uppercase letters :" , upperCount)
print("Number of lowecase letters :" , loweCount)
print("Number of alphabets :" , alphaCount) 
print("Number of symbols :" , SymbolsCount)
print("Number of digits :" , digitsCount)